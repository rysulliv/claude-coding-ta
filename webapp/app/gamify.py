"""Turn the raw progress data into the game layer: streaks, XP, and levels.

Deliberately Duolingo-flavoured (streaks + XP + levels), aimed at an 18-year-old
— motivating, not childish. All of it is derived from real activity dates in
the journal and quiz log, so it can't be gamed by clicking around.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta

from . import progress

# XP economy — tuned so a normal session is a satisfying chunk of a level.
XP_PER_SESSION = 100
XP_PER_QUIZ_POINT = 2          # a 90% quiz = 180 XP
XP_PER_CONCEPT = 10
XP_PER_MASTERY_PCT = 2         # per mastery-percent, summed across all areas
LEVEL_STEP = 500              # XP per level


def _activity_dates() -> set[date]:
    dates: set[date] = set()
    for e in progress.journal():
        try:
            dates.add(datetime.strptime(e["date"], "%Y-%m-%d").date())
        except ValueError:
            pass
    for q in progress.quiz_log():
        try:
            dates.add(datetime.strptime(q["date"], "%Y-%m-%d").date())
        except ValueError:
            pass
    return dates


def streak(today: date | None = None) -> dict:
    today = today or date.today()
    days = _activity_dates()
    if not days:
        return {"current": 0, "longest": 0, "active_today": False, "last_active": None}

    # current streak: walk back from today (or yesterday, so a missed-today
    # doesn't instantly zero a real streak) while consecutive days are present.
    current = 0
    cursor = today if today in days else today - timedelta(days=1)
    while cursor in days:
        current += 1
        cursor -= timedelta(days=1)

    # longest streak across all recorded days
    longest = 0
    run = 0
    prev: date | None = None
    for d in sorted(days):
        run = run + 1 if prev and d - prev == timedelta(days=1) else 1
        longest = max(longest, run)
        prev = d

    return {
        "current": current,
        "longest": longest,
        "active_today": today in days,
        "last_active": max(days).isoformat(),
    }


def xp_breakdown() -> dict:
    st = progress.state()
    quizzes = progress.quiz_log()
    concepts = progress.concepts()

    session_xp = st["sessions_done"] * XP_PER_SESSION
    quiz_xp = sum(q["score"] for q in quizzes) * XP_PER_QUIZ_POINT
    concept_xp = len(concepts) * XP_PER_CONCEPT
    mastery_xp = sum(m["pct"] for m in st["mastery"]) * XP_PER_MASTERY_PCT

    return {
        "sessions": session_xp,
        "quizzes": quiz_xp,
        "concepts": concept_xp,
        "mastery": mastery_xp,
    }


def profile() -> dict:
    parts = xp_breakdown()
    total = sum(parts.values())
    level = total // LEVEL_STEP + 1
    into_level = total % LEVEL_STEP
    return {
        "xp": total,
        "level": level,
        "into_level": into_level,
        "level_step": LEVEL_STEP,
        "level_pct": round(into_level / LEVEL_STEP * 100),
        "to_next": LEVEL_STEP - into_level,
        "breakdown": parts,
        "streak": streak(),
    }
