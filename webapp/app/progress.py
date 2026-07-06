"""Read and structure the mentor's memory files in ``progress/``.

These are Markdown files a human (and the mentor) edit, so parsing is
deliberately tolerant: blank templates are the normal starting state and must
produce empty-but-valid structures, never crash.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path

from . import config

LEVEL_PCT = {"—": 0, "": 0, "intro": 25, "practicing": 55, "solid": 80, "mastered": 100}


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return ""


def _table_rows(md: str, header_contains: str) -> list[list[str]]:
    """Return data rows (as cell lists) of the first pipe-table whose header row
    contains ``header_contains``. Skips the header and the ``---`` separator and
    any HTML-comment lines."""
    rows: list[list[str]] = []
    in_table = False
    seen_separator = False
    for raw in md.splitlines():
        line = raw.strip()
        if line.startswith("<!--") or line.endswith("-->"):
            continue
        is_row = line.startswith("|") and line.endswith("|")
        if not in_table:
            if is_row and header_contains.lower() in line.lower():
                in_table = True
                seen_separator = False
            continue
        if not is_row:
            break  # table ended
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not seen_separator and set("".join(cells)) <= set("-: "):
            seen_separator = True
            continue
        rows.append(cells)
    return rows


def _field(md: str, label: str) -> str:
    """Pull ``**Label:** value`` from the top of a file."""
    m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", md)
    return m.group(1).strip() if m else ""


# --------------------------------------------------------------------------- #
# curriculum-state.md
# --------------------------------------------------------------------------- #
def state() -> dict:
    md = _read(config.progress_dir() / "curriculum-state.md")

    mastery = []
    for cells in _table_rows(md, "Area"):
        if len(cells) < 2:
            continue
        area, level = cells[0], cells[1].lower()
        if level not in LEVEL_PCT:
            level = "—"
        mastery.append(
            {
                "area": area,
                "level": level if level != "—" else "not started",
                "pct": LEVEL_PCT.get(level, 0),
                "evidence": cells[2] if len(cells) > 2 else "",
            }
        )

    sessions = []
    for cells in _table_rows(md, "Topic"):
        if len(cells) < 3 or not any(cells):
            continue
        sessions.append(
            {
                "num": cells[0],
                "date": cells[1] if len(cells) > 1 else "",
                "topic": cells[2] if len(cells) > 2 else "",
                "quiz": cells[3] if len(cells) > 3 else "",
                "notes": cells[4] if len(cells) > 4 else "",
            }
        )

    gate = []
    for m in re.finditer(r"^- \[([ xX])\]\s*(.+)$", md, re.MULTILINE):
        gate.append({"done": m.group(1).lower() == "x", "label": m.group(2).strip()})

    handoff = ""
    hm = re.search(r"## Handoff note for next session\s*(.*)$", md, re.DOTALL)
    if hm:
        handoff = re.sub(r"<!--.*?-->", "", hm.group(1), flags=re.DOTALL).strip()

    flags = ""
    fm = re.search(r"## Active flags\s*(?:<!--.*?-->)?\s*(.*?)(?:\n##|\Z)", md, re.DOTALL)
    if fm:
        flags = fm.group(1).strip()

    mastered = [m for m in mastery if m["pct"] >= 80]
    return {
        "student": _field(md, "Student"),
        "started": _field(md, "Started"),
        "current_phase": _field(md, "Current phase"),
        "next_session": _field(md, "Next session"),
        "pace": _field(md, "Pace to date"),
        "mastery": mastery,
        "mastery_score": round(sum(m["pct"] for m in mastery) / len(mastery)) if mastery else 0,
        "areas_solid": len(mastered),
        "areas_total": len(mastery),
        "sessions": sessions,
        "sessions_done": len(sessions),
        "gate": gate,
        "handoff": handoff,
        "flags": flags,
    }


# --------------------------------------------------------------------------- #
# review-queue.md  (spaced repetition)
# --------------------------------------------------------------------------- #
_QUEUE_RE = re.compile(
    r"\[?(?P<concept>[^|\]]+?)\]?\s*\|\s*source:\s*(?P<source>[^|]+?)\s*\|\s*"
    r"misses:\s*(?P<misses>\d+)\s*\|\s*streak:\s*(?P<streak>\d+)\s*\|\s*"
    r"next_due:\s*(?P<due>[0-9-]+|\w+)\s*\|\s*status:\s*(?P<status>\w+)",
    re.IGNORECASE,
)


def review_queue() -> list[dict]:
    md = _read(config.progress_dir() / "review-queue.md")
    items = []
    today = date.today()
    for line in md.splitlines():
        m = _QUEUE_RE.search(line)
        if not m:
            continue
        d = m.groupdict()
        due_iso = d["due"].strip()
        try:
            due_dt = datetime.strptime(due_iso, "%Y-%m-%d").date()
            overdue = due_dt <= today
        except ValueError:
            due_dt, overdue = None, True
        items.append(
            {
                "concept": d["concept"].strip(),
                "source": d["source"].strip(),
                "misses": int(d["misses"]),
                "streak": int(d["streak"]),
                "due": due_iso,
                "status": d["status"].strip().lower(),
                "overdue": overdue and d["status"].strip().lower() != "retired",
            }
        )
    return items


def due_reviews() -> list[dict]:
    return [i for i in review_queue() if i["overdue"]]


# --------------------------------------------------------------------------- #
# journal.md
# --------------------------------------------------------------------------- #
_JOURNAL_HEADER = re.compile(r"^##\s*(\d{4}-\d{2}-\d{2})\s*[—-]*\s*(.*)$")


def journal(limit: int | None = None) -> list[dict]:
    md = _read(config.progress_dir() / "journal.md")
    entries: list[dict] = []
    current: dict | None = None
    body: list[str] = []
    for line in md.splitlines():
        h = _JOURNAL_HEADER.match(line.strip())
        if h:
            if current:
                current["body"] = "\n".join(body).strip()
                entries.append(current)
            current = {"date": h.group(1), "title": h.group(2).strip(), "body": ""}
            body = []
        elif current is not None:
            body.append(line)
    if current:
        current["body"] = "\n".join(body).strip()
        entries.append(current)
    entries.reverse()  # newest first
    return entries[:limit] if limit else entries


# --------------------------------------------------------------------------- #
# quiz-log.md
# --------------------------------------------------------------------------- #
_QUIZ_RE = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}).*?\b(?P<type>session|weekly|phase|bug-drill)\b.*?"
    r"(?P<score>\d{1,3})\s*%",
    re.IGNORECASE,
)


def quiz_log() -> list[dict]:
    md = _read(config.progress_dir() / "quiz-log.md")
    out = []
    for line in md.splitlines():
        m = _QUIZ_RE.search(line)
        if m:
            out.append(
                {
                    "date": m.group("date"),
                    "type": m.group("type").lower(),
                    "score": int(m.group("score")),
                }
            )
    return out


# --------------------------------------------------------------------------- #
# concepts.md
# --------------------------------------------------------------------------- #
def concepts() -> list[dict]:
    md = _read(config.progress_dir() / "concepts.md")
    out = []
    for line in md.splitlines():
        line = line.strip()
        if not line.startswith("-") and not line.startswith("*"):
            continue
        item = line.lstrip("-*").strip()
        if not item:
            continue
        # "term — definition"  or  "term: definition"
        m = re.match(r"(.+?)\s*[—:-]\s*(.+)", item)
        if m:
            out.append({"term": m.group(1).strip(" *`"), "definition": m.group(2).strip()})
        else:
            out.append({"term": item.strip(" *`"), "definition": ""})
    return out


def struggles() -> str:
    return _read(config.progress_dir() / "struggles.md")
