"""Read the local Claude Code transcript store.

Each session is a JSONL file at ``~/.claude/projects/<slug>/<uuid>.jsonl`` where
every line is one event (user message, assistant message, tool use/result,
summary...). The format is undocumented and can change between Claude Code
versions, so every access is defensive: a malformed line is skipped, never fatal.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from . import config

# session ids are UUIDs / safe slugs; validate before using one in a path
_SID_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def _iter_lines(path: Path):
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue
    except OSError:
        return


def _blocks_to_parts(content) -> list[dict]:
    """Normalise a message ``content`` (string or list of blocks) into display
    parts: {kind: text|tool_use|tool_result|image, ...}."""
    parts: list[dict] = []
    if isinstance(content, str):
        if content.strip():
            parts.append({"kind": "text", "text": content})
        return parts
    if not isinstance(content, list):
        return parts
    for block in content:
        if not isinstance(block, dict):
            continue
        btype = block.get("type")
        if btype == "text":
            parts.append({"kind": "text", "text": block.get("text", "")})
        elif btype == "thinking":
            parts.append({"kind": "thinking", "text": block.get("thinking", "")})
        elif btype == "tool_use":
            parts.append(
                {
                    "kind": "tool_use",
                    "name": block.get("name", "tool"),
                    "input": block.get("input", {}),
                }
            )
        elif btype == "tool_result":
            rc = block.get("content", "")
            if isinstance(rc, list):
                rc = "\n".join(
                    b.get("text", "") for b in rc if isinstance(b, dict) and b.get("type") == "text"
                )
            parts.append({"kind": "tool_result", "text": str(rc), "is_error": bool(block.get("is_error"))})
        elif btype == "image":
            parts.append({"kind": "image"})
    return parts


def _fmt_ts(ts: str | None) -> str:
    if not ts:
        return ""
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d %H:%M")
    except (ValueError, AttributeError):
        return ts


def _project_dirs():
    root = config.claude_projects_dir()
    if not root.exists():
        return []
    return [d for d in root.iterdir() if d.is_dir()]


def list_sessions(scope: str = "project") -> list[dict]:
    """List sessions, newest first. ``scope='project'`` keeps only sessions whose
    recorded ``cwd`` is inside this repo; ``scope='all'`` returns everything."""
    repo = str(config.repo_root()).replace("\\", "/").lower()
    out: list[dict] = []
    for pdir in _project_dirs():
        for f in pdir.glob("*.jsonl"):
            meta = _session_meta(f)
            if not meta:
                continue
            if scope == "project":
                cwd = (meta.get("cwd") or "").replace("\\", "/").lower()
                if not cwd or repo not in cwd:
                    continue
            out.append(meta)
    out.sort(key=lambda m: m["mtime"], reverse=True)
    return out


def _session_meta(path: Path) -> dict | None:
    title = ""
    cwd = ""
    first_user = ""
    count = 0
    first_ts = None
    try:
        stat = path.stat()
    except OSError:
        return None
    for obj in _iter_lines(path):
        count += 1
        if not cwd and isinstance(obj.get("cwd"), str):
            cwd = obj["cwd"]
        if obj.get("type") == "summary" and not title:
            title = obj.get("summary", "")
        if not first_ts and obj.get("timestamp"):
            first_ts = obj["timestamp"]
        if not first_user and obj.get("type") == "user":
            msg = obj.get("message", {})
            parts = _blocks_to_parts(msg.get("content") if isinstance(msg, dict) else msg)
            text = next((p["text"] for p in parts if p["kind"] == "text"), "")
            if text and not text.startswith("<"):
                first_user = text.strip()
    if count == 0:
        return None
    if not title:
        title = (first_user[:70] + "…") if len(first_user) > 70 else (first_user or "(untitled session)")
    return {
        "id": path.stem,
        "title": title,
        "cwd": cwd,
        "messages": count,
        "started": _fmt_ts(first_ts),
        "updated": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
        "mtime": stat.st_mtime,
        "project": path.parent.name,
    }


def find_session_file(session_id: str) -> Path | None:
    if not session_id or not _SID_RE.match(session_id):
        return None
    for pdir in _project_dirs():
        candidate = pdir / f"{session_id}.jsonl"
        if candidate.exists():
            return candidate
    return None


def load_session(session_id: str) -> dict | None:
    """Full transcript for replay: an ordered list of display messages."""
    path = find_session_file(session_id)
    if not path:
        return None
    messages: list[dict] = []
    cwd = ""
    for obj in _iter_lines(path):
        cwd = obj.get("cwd") or cwd
        otype = obj.get("type")
        if otype not in ("user", "assistant"):
            continue
        msg = obj.get("message", {})
        if not isinstance(msg, dict):
            continue
        parts = _blocks_to_parts(msg.get("content"))
        # skip pure tool-result "user" turns that are just plumbing, but keep visible ones
        if not parts:
            continue
        messages.append(
            {
                "role": msg.get("role", otype),
                "parts": parts,
                "ts": _fmt_ts(obj.get("timestamp")),
            }
        )
    meta = _session_meta(path)
    return {"id": session_id, "cwd": cwd, "messages": messages, "meta": meta}
