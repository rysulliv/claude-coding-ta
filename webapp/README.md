# Companion dashboard

Your live dashboard for the course — streaks, progress, quizzes and review, a concept map, how-to guides, app mockups, and a built-in **Claude Code client** for browsing and continuing your own sessions. It runs entirely **on your computer**; nothing is sent anywhere.

## Run it

From the `webapp/` folder, in your terminal:

```bash
uv run uvicorn app.main:app
```

Then open **http://localhost:8000** in your browser. That's it — [uv](https://docs.astral.sh/uv/) installs the dependencies the first time automatically. Leave that terminal running while you work; press **Ctrl+C** in it to stop the app.

> **You** start the dashboard yourself each day — running a dev server in the terminal is a real skill, and it's how your streak and progress stay live. Your mentor walks you through it the first time and reminds you at the start of each session. (Add `--reload` if you're editing the app's own code and want it to restart on changes.)

## What it reads

- **`../progress/`** — your streaks, mastery map, review queue, quizzes, journal, and concepts.
- **`../curriculum/ai-developer-curriculum.md`** — the phase/session roadmap.
- **`~/.claude/projects/`** — your local Claude Code session transcripts (for the Sessions view and the client). These never leave your machine.

## The Claude Code client

The **Claude Client** page can *continue* a session, not just view it. Each turn it runs your local `claude` CLI:

```
claude -p "<your message>" --resume <session-id> --output-format stream-json …
```

and streams the reply back into the page live. If the `claude` command isn't on your PATH, the page still lets you browse and replay sessions and tells you what's missing.

**Heads up on concurrency:** continuing a session here writes to the same transcript file VS Code uses. If the same session is open in both places at once, use a **new session** or the **fork** toggle so they don't clobber each other.

## Configuration (optional)

Environment variables, all optional:

- `MENTOR_REPO_ROOT` — override the course repo location (defaults to the folder above `webapp/`).
- `CLAUDE_PROJECTS_DIR` — override where Claude Code transcripts live (defaults to `~/.claude/projects`).
- `CLAUDE_CLI` — the CLI command name (defaults to `claude`).

## For the mentor

This app is **course infrastructure, not curriculum**. Per `CLAUDE.md`, the mentor owns and extends it as the student progresses (unlock views, add guides in `app/content/guides/`, drop mockups in `app/static/mockups/`) and does **not** run the teaching loop on its code. Keep it small and modular — the same rules you teach.
