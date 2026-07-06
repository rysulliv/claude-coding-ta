"""Locating the pieces the dashboard reads: the repo it lives in, and the
local Claude Code transcript store. Everything here is filesystem-only and
local — the dashboard never talks to a remote server."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


@lru_cache
def repo_root() -> Path:
    """The course repo = the parent of the ``webapp/`` folder this file lives in.

    ``config.py`` is at ``<repo>/webapp/app/config.py``, so three parents up is
    the repo root. Overridable with MENTOR_REPO_ROOT for tests / odd layouts.
    """
    override = os.environ.get("MENTOR_REPO_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


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
