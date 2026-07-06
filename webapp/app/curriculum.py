"""Parse the phase/session structure out of the curriculum Markdown so the
dashboard can render a progress tracker and cross it against completed work."""

from __future__ import annotations

import re

from . import config, progress

_PHASE_RE = re.compile(r"^##\s*Phase\s*(\d+)\s*[—-]+\s*(.+?)\s*(?:\((.*?)\))?\s*$")
# session bullets: "- 0.1 — Title ..."  or  "- 3.13–3.15 — Build weeks"
_SESSION_RE = re.compile(r"^-\s*(\d+\.\d+(?:[–-]\d+\.?\d*)?)\s*[—-]+\s*(.+)$")


def _short_title(text: str) -> str:
    """First clause of a session description — enough for a tracker chip."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # drop bold
    # cut at the first sentence-ish boundary
    for sep in (". ", " — ", ": ", " ("):
        idx = text.find(sep)
        if 0 < idx < 80:
            return text[:idx].strip()
    return text[:80].strip()


def phases() -> list[dict]:
    md = config.curriculum_file()
    try:
        text = md.read_text(encoding="utf-8")
    except OSError:
        return []

    done_nums = {s["num"].strip() for s in progress.state()["sessions"] if s["num"].strip()}

    result: list[dict] = []
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        pm = _PHASE_RE.match(line)
        if pm:
            if current:
                result.append(current)
            current = {
                "num": int(pm.group(1)),
                "title": pm.group(2).strip(),
                "weeks": (pm.group(3) or "").strip(),
                "sessions": [],
            }
            continue
        if current is None:
            continue
        sm = _SESSION_RE.match(line.strip())
        if sm:
            num = sm.group(1).strip()
            current["sessions"].append(
                {
                    "num": num,
                    "title": _short_title(sm.group(2)),
                    "done": num in done_nums,
                }
            )
    if current:
        result.append(current)

    for ph in result:
        total = len(ph["sessions"]) or 1
        done = sum(1 for s in ph["sessions"] if s["done"])
        ph["done_count"] = done
        ph["total"] = len(ph["sessions"])
        ph["pct"] = round(done / total * 100)
        ph["complete"] = done == len(ph["sessions"]) and ph["sessions"] != []
    return result


def overview() -> dict:
    ph = phases()
    total_sessions = sum(len(p["sessions"]) for p in ph)
    done_sessions = sum(p["done_count"] for p in ph)
    return {
        "phases": ph,
        "total_sessions": total_sessions,
        "done_sessions": done_sessions,
        "pct": round(done_sessions / total_sessions * 100) if total_sessions else 0,
    }
