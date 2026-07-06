"""Locating the pieces the dashboard reads: the repo it lives in, and the
local Claude Code transcript store. Everything here is filesystem-only and
local — the dashboard never talks to a remote server."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


@lru_cache
def repo_root() -> Path:
    """The course repo this dashboard belongs to — the folder the student cloned.

    We find it by walking up from this file looking for the course markers
    (``CLAUDE.md`` + ``curriculum/``), so it resolves to the student's own repo
    no matter what they named the clone or how it's nested. ``config.py`` lives at
    ``<repo>/webapp/app/config.py``; the fixed-layout fallback (three parents up)
    is used only if the markers can't be found. Overridable with MENTOR_REPO_ROOT.
    """
    override = os.environ.get("MENTOR_REPO_ROOT")
    if override:
        return Path(override).resolve()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "CLAUDE.md").is_file() and (parent / "curriculum").is_dir():
            return parent
    return here.parents[2]


def working_dir(session_id: str | None = None) -> Path:
    """The folder Claude Code should run in for a client turn — the single source
    of truth shared by the subprocess launcher and the UI.

    - New conversation: the student's repo root (where ``CLAUDE.md`` lives, so the
      mentor harness loads and Claude operates on their actual project).
    - Resumed conversation: the ``cwd`` recorded in that session's transcript, so a
      session continues in the exact folder it started in. Falls back to the repo
      root if that folder is missing or the transcript has no ``cwd``.
    """
    root = repo_root()
    if not session_id:
        return root
    # local import avoids a circular import at module load
    from . import sessions

    recorded = sessions.session_cwd(session_id)
    if recorded:
        p = Path(recorded)
        if p.is_dir():
            return p
    return root


def progress_dir() -> Path:
    return repo_root() / "progress"


def curriculum_file() -> Path:
    return repo_root() / "curriculum" / "ai-developer-curriculum.md"


def guides_dir() -> Path:
    """Where how-to guides live. Ships inside the webapp so it's self-contained."""
    return Path(__file__).resolve().parent / "content" / "guides"


def mockups_dir() -> Path:
    """Student-app UI mockups the mentor drops in as the project takes shape.
    Lives under static/ so the images are served directly by the static mount."""
    return Path(__file__).resolve().parent / "static" / "mockups"


@lru_cache
def claude_projects_dir() -> Path:
    """Root of the local Claude Code transcript store (``~/.claude/projects``).

    Overridable with CLAUDE_PROJECTS_DIR. This is the only path outside the repo
    the dashboard reads, and it never leaves the machine.
    """
    override = os.environ.get("CLAUDE_PROJECTS_DIR")
    if override:
        return Path(override).resolve()
    return Path.home() / ".claude" / "projects"


def claude_cli() -> str:
    """Executable name for the Claude Code CLI (overridable for odd installs)."""
    return os.environ.get("CLAUDE_CLI", "claude")
