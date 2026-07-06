"""Drive the Claude Code CLI to *continue* a session from the browser.

This is what makes the dashboard a real client and not just a transcript viewer.
For each turn we invoke:

    claude -p "<message>" --resume <session_id> \
        --output-format stream-json --include-partial-messages --verbose \
        --permission-mode <mode>

and translate the newline-delimited JSON event stream into simple events the
frontend renders live (text deltas, tool calls, tool results, final result).

Why a thread + queue instead of asyncio subprocess: uvicorn on Windows can run
on a selector event loop, which cannot spawn subprocesses. Reading the process
in a plain thread and handing lines to the async layer via a queue works the
same on every platform. The generator terminates the subprocess on disconnect
so a closed browser tab can never leave a headless ``claude`` running.
"""

from __future__ import annotations

import asyncio
import json
import subprocess
import threading
import uuid
from pathlib import Path

from . import config, sessions

# Full set the engine understands. bypassPermissions is intentionally NOT
# offered to the browser (see CLIENT_PERMISSION_MODES) — a drive-by POST to
# localhost must not be able to run claude with every gate off.
PERMISSION_MODES = ["default", "acceptEdits", "plan", "bypassPermissions"]
CLIENT_PERMISSION_MODES = ["default", "acceptEdits", "plan"]

IDLE_TIMEOUT_S = 300  # kill a turn that produces no output for this long
_SENTINEL = object()


def cli_available() -> dict:
    """Is the Claude Code CLI usable? Shown in the client UI so the failure mode
    is 'install the CLI', not a cryptic stream error."""
    try:
        out = subprocess.run(
            [config.claude_cli(), "--version"],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if out.returncode == 0:
            return {"ok": True, "version": out.stdout.strip()}
        return {"ok": False, "error": (out.stderr or out.stdout).strip() or "non-zero exit"}
    except FileNotFoundError:
        return {"ok": False, "error": f"'{config.claude_cli()}' not found on PATH"}
    except Exception as exc:  # noqa: BLE001 - surface any failure to the UI
        return {"ok": False, "error": str(exc)}


def _translate(obj: dict) -> list[dict]:
    """Map one CLI stream-json object to zero+ frontend events."""
    events: list[dict] = []
    otype = obj.get("type")

    if otype == "system" and obj.get("subtype") == "init":
        events.append({"type": "init", "session_id": obj.get("session_id", "")})

    elif otype == "stream_event":
        ev = obj.get("event", {})
        if ev.get("type") == "content_block_delta":
            delta = ev.get("delta", {})
            if delta.get("type") == "text_delta" and delta.get("text"):
                events.append({"type": "text", "text": delta["text"]})
            elif delta.get("type") == "thinking_delta" and delta.get("thinking"):
                events.append({"type": "thinking", "text": delta["thinking"]})

    elif otype == "assistant":
        msg = obj.get("message", {})
        for block in msg.get("content", []) if isinstance(msg, dict) else []:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                events.append(
                    {"type": "tool_use", "name": block.get("name", "tool"), "input": block.get("input", {})}
                )

    elif otype == "user":
        msg = obj.get("message", {})
        for block in msg.get("content", []) if isinstance(msg, dict) else []:
            if isinstance(block, dict) and block.get("type") == "tool_result":
                rc = block.get("content", "")
                if isinstance(rc, list):
                    rc = "\n".join(
                        b.get("text", "") for b in rc if isinstance(b, dict) and b.get("type") == "text"
                    )
                events.append({"type": "tool_result", "text": str(rc)[:4000], "is_error": bool(block.get("is_error"))})

    elif otype == "result":
        events.append(
            {
                "type": "result",
                "session_id": obj.get("session_id", ""),
                "is_error": bool(obj.get("is_error")),
                "cost_usd": obj.get("total_cost_usd"),
                "text": obj.get("result", "") if obj.get("is_error") else "",
            }
        )
    return events


def _run_cli(cmd, cwd, queue, loop, holder):
    """Blocking (runs in a thread): run the CLI, push translated events onto the
    async queue. ``holder`` is a one-slot list so the async side can reach the
    process object and terminate it on disconnect."""
    def push(item):
        loop.call_soon_threadsafe(queue.put_nowait, item)

    try:
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # merge, so a full stderr pipe can't deadlock stdout
            text=True,
            bufsize=1,
        )
    except FileNotFoundError:
        push({"type": "error", "message": f"'{config.claude_cli()}' not found on PATH"})
        push(_SENTINEL)
        return

    holder.append(proc)
    tail: list[str] = []  # last few non-JSON lines, for an error message
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            tail.append(line)
            del tail[:-5]
            continue
        for ev in _translate(obj):
            push(ev)
    proc.wait()
    if proc.returncode not in (0, None):
        push({"type": "error", "message": "\n".join(tail) or f"claude exited with code {proc.returncode}"})
    push(_SENTINEL)


async def stream_turn(
    message: str,
    session_id: str | None,
    permission_mode: str = "default",
    fork: bool = False,
):
    """Async generator of frontend events for one turn of conversation.

    Guarantees the ``claude`` subprocess is terminated when the consumer stops
    iterating (client disconnect) or an inactivity timeout fires."""
    if permission_mode not in CLIENT_PERMISSION_MODES:
        permission_mode = "default"

    cmd = [
        config.claude_cli(),
        "-p",
        message,
        "--output-format",
        "stream-json",
        "--include-partial-messages",
        "--verbose",
        "--permission-mode",
        permission_mode,
    ]

    cwd = str(config.repo_root())
    if session_id:
        cmd += ["--resume", session_id]
        if fork:
            cmd.append("--fork-session")
        sfile = sessions.find_session_file(session_id)
        if sfile:
            for obj in sessions._iter_lines(sfile):
                if isinstance(obj.get("cwd"), str) and obj["cwd"]:
                    cwd = obj["cwd"]
                    break
    else:
        cmd += ["--session-id", str(uuid.uuid4())]

    if not Path(cwd).exists():
        cwd = str(config.repo_root())

    queue: asyncio.Queue = asyncio.Queue()
    loop = asyncio.get_running_loop()
    holder: list = []
    thread = threading.Thread(target=_run_cli, args=(cmd, cwd, queue, loop, holder), daemon=True)
    thread.start()

    try:
        while True:
            try:
                item = await asyncio.wait_for(queue.get(), timeout=IDLE_TIMEOUT_S)
            except asyncio.TimeoutError:
                yield {"type": "error", "message": f"No response for {IDLE_TIMEOUT_S}s — stopping the turn."}
                break
            if item is _SENTINEL:
                break
            yield item
    finally:
        # client disconnected, timed out, or finished — never leave claude running
        proc = holder[0] if holder else None
        if proc and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
