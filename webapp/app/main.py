"""The companion dashboard web app.

Local-first: it reads the course repo's ``progress/`` and ``curriculum/`` files
and the machine's Claude Code transcripts, and can drive the Claude CLI to
continue a session. It never talks to a remote server. Run it with:

    uv run uvicorn app.main:app --reload    # from the webapp/ directory
"""

from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt

from . import claude_client, config, curriculum, gamify, progress, sessions

APP_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Mentor Kit — Companion Dashboard")
app.mount("/static", StaticFiles(directory=APP_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))
md = MarkdownIt("commonmark", {"html": False, "linkify": True, "typographer": True}).enable("table")


def ctx(request: Request, **extra) -> dict:
    """Shared template context: the nav needs the game profile on every page."""
    base = {
        "request": request,
        "profile": gamify.profile(),
        "state": progress.state(),
        "nav_due": len(progress.due_reviews()),
    }
    base.update(extra)
    return base


# --------------------------------------------------------------------------- #
# Pages
# --------------------------------------------------------------------------- #
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        ctx(
            request,
            overview=curriculum.overview(),
            due=progress.due_reviews(),
            journal=progress.journal(limit=4),
        ),
    )


@app.get("/tracker", response_class=HTMLResponse)
def tracker(request: Request):
    return templates.TemplateResponse(request, "tracker.html", ctx(request, overview=curriculum.overview()))


@app.get("/reviews", response_class=HTMLResponse)
def reviews(request: Request):
    concepts = {c["term"].lower(): c["definition"] for c in progress.concepts()}
    due = progress.due_reviews()
    for item in due:
        item["note"] = concepts.get(item["concept"].lower(), "")
    return templates.TemplateResponse(
        request,
        "reviews.html",
        ctx(request, due=due, queue=progress.review_queue(), quiz_log=progress.quiz_log()),
    )


@app.get("/concepts", response_class=HTMLResponse)
def concept_map(request: Request):
    return templates.TemplateResponse(request, "concepts.html", ctx(request, concepts=progress.concepts()))


@app.get("/guides", response_class=HTMLResponse)
def guides(request: Request):
    return templates.TemplateResponse(request, "guides.html", ctx(request, guides=_guide_index()))


@app.get("/guides/{slug}", response_class=HTMLResponse)
def guide(request: Request, slug: str):
    path = config.guides_dir() / f"{slug}.md"
    if not path.exists() or ".." in slug:
        return templates.TemplateResponse(request, "guide.html", ctx(request, title="Not found", body="<p>That guide doesn't exist yet.</p>", guides=_guide_index()), status_code=404)
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").strip() if text else slug
    return templates.TemplateResponse(
        request,
        "guide.html", ctx(request, title=title, body=md.render(text), guides=_guide_index(), slug=slug)
    )


@app.get("/mockups", response_class=HTMLResponse)
def mockups(request: Request):
    return templates.TemplateResponse(request, "mockups.html", ctx(request, mockups=_mockup_index()))


@app.get("/sessions", response_class=HTMLResponse)
def session_list(request: Request, scope: str = "project"):
    return templates.TemplateResponse(
        request,
        "sessions.html", ctx(request, sessions=sessions.list_sessions(scope), scope=scope)
    )


@app.get("/sessions/{session_id}", response_class=HTMLResponse)
def session_detail(request: Request, session_id: str):
    data = sessions.load_session(session_id)
    if not data:
        return templates.TemplateResponse(request, "session_detail.html", ctx(request, session=None), status_code=404)
    return templates.TemplateResponse(request, "session_detail.html", ctx(request, session=data))


@app.get("/client", response_class=HTMLResponse)
def client(request: Request, session: str = ""):
    transcript = sessions.load_session(session) if session else None
    return templates.TemplateResponse(
        request,
        "client.html",
        ctx(
            request,
            session_id=session,
            transcript=transcript,
            cli=claude_client.cli_available(),
            modes=claude_client.CLIENT_PERMISSION_MODES,
            recent=sessions.list_sessions("project")[:8],
        ),
    )


# --------------------------------------------------------------------------- #
# API
# --------------------------------------------------------------------------- #
@app.get("/api/status")
def api_status():
    return JSONResponse(claude_client.cli_available())


@app.get("/api/profile")
def api_profile():
    return JSONResponse(gamify.profile())


def _same_origin(request: Request) -> bool:
    """Block drive-by cross-site POSTs. A same-origin fetch sends no Origin (or a
    localhost one); a malicious page on another site sends its own Origin."""
    origin = request.headers.get("origin")
    if not origin:
        return True
    host = (origin.split("//", 1)[-1]).split("/", 1)[0]
    return host.startswith("localhost") or host.startswith("127.0.0.1") or host.startswith("[::1]")


@app.post("/api/client/stream")
async def api_client_stream(
    request: Request,
    message: str = Form(...),
    session_id: str = Form(""),
    permission_mode: str = Form("default"),
    fork: str = Form("false"),
):
    if not _same_origin(request):
        return JSONResponse({"error": "cross-origin requests are not allowed"}, status_code=403)
    if permission_mode not in claude_client.CLIENT_PERMISSION_MODES:
        permission_mode = "default"

    async def event_stream():
        try:
            async for event in claude_client.stream_turn(
                message=message,
                session_id=session_id or None,
                permission_mode=permission_mode,
                fork=(fork == "true"),
            ):
                yield f"data: {json.dumps(event)}\n\n"
        except Exception as exc:  # noqa: BLE001
            yield f"data: {json.dumps({'type': 'error', 'message': str(exc)})}\n\n"
        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# --------------------------------------------------------------------------- #
# Content indexes
# --------------------------------------------------------------------------- #
def _guide_index() -> list[dict]:
    out = []
    gdir = config.guides_dir()
    if gdir.exists():
        for f in sorted(gdir.glob("*.md")):
            text = f.read_text(encoding="utf-8")
            lines = [ln for ln in text.splitlines() if ln.strip()]
            title = lines[0].lstrip("# ").strip() if lines else f.stem
            blurb = ""
            for ln in lines[1:]:
                if not ln.startswith("#"):
                    blurb = ln.strip()
                    break
            out.append({"slug": f.stem, "title": title, "blurb": blurb})
    return out


def _mockup_index() -> list[dict]:
    out = []
    mdir = config.mockups_dir()
    if not mdir.exists():
        return out
    manifest = mdir / "manifest.json"
    captions = {}
    if manifest.exists():
        try:
            captions = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            captions = {}
    for f in sorted(mdir.iterdir()):
        if f.suffix.lower() in (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"):
            out.append(
                {
                    "src": f"/static/mockups/{f.name}",
                    "name": f.stem.replace("-", " ").replace("_", " ").title(),
                    "caption": captions.get(f.name, ""),
                }
            )
    return out
