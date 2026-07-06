# From Zero to Shipped: An AI Developer Curriculum

**Audience:** An 18-year-old with little/no coding background who wants to build real AI-powered applications — not toy exercises.
**Duration:** ~22 weeks at 8–12 hours/week (flexible; phases gate on competence, not calendar).
**North star:** Every phase ends with something deployed that a real person (friend or family) actually uses — built *fast*, the way real developers build now: with AI doing much of the typing. This is a course in **grounded vibe coding**. You'll vibe-code real apps at speed, and — this is the whole point — you'll understand, read, debug, and steer every line that ships. Understanding is enforced, not assumed: every session ends with a walkthrough and a quiz, and you can't move on until you can explain what was built. The graduate is an excellent vibe coder who never ships slop.

**What matters most (priority order):** (1) deeply understanding programming and systems concepts — APIs, authentication, backend vs. frontend, databases and queries, caching, concurrency and race conditions, security across the frontend↔backend boundary, and keeping code modular (no mega-files); (2) being able to **read and explain any code in the project** — yours, the mentor's, or a library's; (3) being able to **prompt and steer the AI to produce senior-quality work** — decompose the task, give the right context, spot slop and reject it, turn a weak result into a strong one. Writing non-trivial code unaided is a real goal too, trained *progressively* as a **diagnostic** (proof the understanding is real, and that you could work without a net if the AI got stuck): lighter in the early phases, ramping up toward the solo rebuilds in Phases 3–4. Early on, reading, predicting, steering, and modifying code matters more than writing it from a blank file.

---

## The Tech Stack (professional, cheap, simple)

| Layer | Choice | Why | Cost |
|---|---|---|---|
| Language | **Python 3.12+** | Industry standard for AI work, readable, huge ecosystem | Free |
| Package/env mgmt | **uv** | One tool for Python versions, venvs, and dependencies; fast and modern | Free |
| Web framework | **FastAPI** | Professional-grade, async, auto-generated API docs, teaches real HTTP concepts | Free |
| Frontend (early) | **Jinja2 templates + HTMX** | Ship interactive apps without learning a JS framework first | Free |
| Frontend (later, optional) | **React (Vite)** | Only if/when a project demands it | Free |
| Database | **PostgreSQL via Supabase** | Real Postgres + auth + storage + row-level security in one free tier | Free tier |
| DB access | **Raw SQL first, then SQLAlchemy** | SQL is a career skill; ORMs make sense only after you know what they're hiding | Free |
| Deployment | **Railway** | `git push` → live URL; env vars, logs, Postgres add-ons if needed | ~$5/mo |
| API testing | **curl → Bruno** | curl teaches raw HTTP; Bruno is an open-source Postman alternative whose collections are plain files committed to git (so the mentor harness sees them). Postman covered by name-recognition only | Free |
| AI | **Anthropic API (Claude)** | Messages API, tool use, streaming, structured outputs | Pay-per-use (~$5–20/mo at learning scale) |
| Version control | **Git + GitHub** | Non-negotiable professional habit from day one | Free |
| Payments (Phase 5) | **Stripe** | Industry standard, great docs, test mode | Free until revenue |
| Dev environment | **VS Code + Claude Code** | Claude Code is the AI pair — governed by the mentor harness (see companion doc) | Claude subscription |

**Total fixed cost: roughly $10–25/month.** Everything on this list is what real startups actually use — nothing here is a "learning toy" that gets thrown away later.

---

## Curriculum Structure

Five phases. Each phase = one shipped project + a defined concept set. Each **session** (2–3 hrs) follows the same loop, enforced by the Claude Code harness:

1. **Plan** (10 min) — student states today's goal in plain English and sketches the approach before any code.
2. **Build** (60–90 min) — pair with Claude, often prompting it to build a whole piece at once (that's the skill). Claude explains as it goes; the student's core job is to **direct the build, then read and understand every diff** and hit the session's comprehension checkpoints — explain a block line by line, predict a snippet's output, spot a planted mistake, steer a weak generation into a good one, or modify/extend a piece. Some checkpoints are designated "you-write-this" blocks, kept light in early phases and a regular mode by Phase 3+.
3. **Walkthrough** (20 min) — trace the new code path end-to-end. Student explains it back in their own words.
4. **Quiz** (15 min) — 5–7 questions on today's concepts: recall, code-reading ("what does this print?"), and prediction ("what happens if X fails?"). Score < 70% → misses go to the review queue and get re-tested next session.
5. **Log** (5 min) — student writes the journal entry and the git commit message themselves.

**Weekly checkpoint:** cumulative quiz (pulls from the review queue with spaced repetition), one "explain it to a non-programmer" written summary, and one small refactor or bug-hunt exercise done *without* AI assistance.

**Threads that run through every phase:**

**Reading fluency (the primary skill).** Reading and explaining code is trained every session, not left to chance — most of what the mentor writes (a lot, since we vibe-code), the student reads back and narrates ("what does this line do, and what breaks if it's wrong?"). This is exactly how you judge whether an AI generation is right or slop, so it's non-negotiable. The bar is that the student can open *any* file in the project and explain what it does and why it's there. Walkthroughs, the "explain your own repo" drill, and code-reading quiz questions all serve this; writing from scratch ramps up behind it.

**Prompting & steering (the driver's skill).** Getting senior-quality output from AI is a taught, graded skill, run through the `prompt-craft` playbook. From session one the student drafts the prompts that drive the build, learns the levers that separate a sharp prompt from a slop-generating one (context, constraints, output shape, edge cases named up front, what *not* to do), and practices the core loop: **prompt → read the result → steer it better**. When a generation comes out weak, the mentor doesn't silently fix it — the student diagnoses *why at the prompt level* and re-steers. Roughly every other week a diagnostic exercise is a pure prompting task: "here's a spec, get the AI to build it well in one prompt."

**Code structure (small, focused files).** Keeping code modular is a habit, not a one-time lesson. Whenever a file starts doing too many things, the mentor names the smell and the pair refactors it — splitting routes, services, and helpers along their seams. The recurring question is "why is this file getting long, and where are the seams to split it on?" Session 3.6 formalizes it, but the habit starts as soon as the app has more than one file.

**Operations literacy.** From Phase 0 onward, sessions include hands-on time in the tools around the code — because a developer who can't inspect their own database or read their own server logs is flying blind. Recurring rituals: after any write feature ships, open the data (Supabase table editor and a raw SQL query) and verify the rows actually look right; after any deploy, open Railway logs and watch a live request flow through; when anything errors in production, the *first* move is logs, not code. Specific sessions below teach each tool properly, but the habit is practiced constantly.

**Bug drills (planted bugs).** Debugging is taught deliberately, not just when accidents happen. Claude periodically introduces a realistic bug on purpose, and the student's independence ramps up in four stages:
1. **Guided (Phases 0–1):** Claude announces "I've planted a bug," then walks the full method out loud — read the error, form a hypothesis, add a print/log, test the hypothesis, fix, verify.
2. **Hinted (Phase 2):** bug announced, student drives, Claude only answers direct questions and offers escalating hints on request.
3. **Solo-announced (Phase 3):** "there's a bug somewhere in what we just built — find and fix it." No help; timed; result logged.
4. **Unannounced (Phase 4+):** occasionally a session's code simply doesn't work as expected and nobody says it's a drill — because that's exactly what real development is. Revealed as a drill afterward, always.
Bugs are drawn from the classics of each phase: off-by-one and type errors early; NULL handling, missing WHERE clauses, and misnamed env vars in Phase 1; malformed JSON handling, silent API failures, and context-window overruns in Phase 2; auth leaks (missing RLS), timezone bugs, and race-y double-submits in Phase 3.

**Phase gates:** to finish a phase, the student must (a) have the project live and used by ≥1 real person, (b) pass a cumulative phase exam at 80%+, and (c) rebuild one small component of the project from scratch, solo, in a timed session.

---

## Phase 0 — Foundations & First Deploy (Weeks 1–2)

**Goal:** A live URL on the internet within 10 days. Demystify the whole pipeline before going deep on any one part.

**Sessions:**
- 0.1 — **Your workshop: VS Code + Claude Code.** (This is the only session that starts *before* the mentor is fully running — the README's Day 0 checklist gets Claude Code talking, then Claude gives the tour.) Full tour of VS Code: the Explorer, editor tabs, the integrated terminal (open it, resize it, run your first command), the Command Palette, Settings, and the Extensions view. Then the Claude Code extension itself: the Spark icon and the chat panel, how @-mentioning files works, and — critically for this curriculum — **the diff-review discipline**: Claude proposes edits as side-by-side diffs and the student reviews every change before accepting; auto-accept stays OFF for the whole curriculum, because reading diffs is how you stay the author of your own codebase. Install the supporting extensions and learn what each one actually does: **Python** (Microsoft — language support, debugging, interpreter picker), **Ruff** (instant lint/format feedback — squiggles that teach), **GitLens** (see the history behind every line), **Error Lens** (errors inline where they happen), and later **SQLTools** when the database arrives. Finish with the meta-lesson: how these mentored sessions work — the plan → build → walkthrough → quiz → log loop, the progress files, and the deal (Claude explains everything, the student can ask "why" about anything, and quizzes aren't optional). *Concepts: editor vs. terminal vs. shell, what an extension is, what a linter is, reading a diff.*
- 0.2 — Environment setup, guided by the mentor: install git and uv, use uv to install Python, first "hello world" script run from the integrated terminal, create the GitHub account. Terminal fundamentals throughout: `cd`, `ls`, paths, what PATH is, tab completion, ctrl-C. *Concepts: what a shell is, PATH, files vs. processes, interpreters, package managers.*
- 0.3 — Python fundamentals I: variables, types, strings, f-strings, lists, dicts, loops, conditionals — learned by building a CLI "Magic 8-Ball / decision maker." *Concepts: mutability, indexing, control flow.*
- 0.4 — Python fundamentals II: functions, arguments/returns, modules, imports, reading errors and stack traces. Refactor the CLI into functions. *Concepts: scope, DRY, the anatomy of a traceback.*
- 0.5 — Git for real: init, add, commit, branch, push this curriculum repo to GitHub, .gitignore, why commits are small and messages matter. Then a GitLens moment: click through the history of the files you've already made. *Concepts: snapshots vs. diffs, remotes.*
- 0.6 — First deploy: minimal FastAPI app ("family fortune cookie" — one endpoint, one HTML page), pushed to Railway. Share the URL with family. Then the first **ops tour**: open the Railway dashboard, find the deploy logs vs. runtime logs, watch a request hit the server live, add a `print`/log line and see it appear, and deliberately crash the app once to see what a stack trace looks like in production logs. Name the **frontend vs. backend** split explicitly here — the HTML page in the browser is the frontend, the FastAPI process is the backend, and they are two separate programs talking over HTTP. *Concepts: what a server is, frontend vs. backend (the two-programs model), request/response, ports, HTTP verbs, environment variables, stdout → logs.*
- 0.7 — **First guided bug drill:** Claude plants a classic beginner bug (off-by-one or a type error) in the fortune cookie app and walks the full debugging method out loud: read the traceback bottom-up → hypothesis → add a print → confirm → fix → verify → explain root cause. *Concepts: the scientific method of debugging, tracebacks as maps not walls.*

**Phase project:** the deployed fortune-cookie/decision-maker page. Trivial by design — the win is the *pipeline*: code → git → deploy → someone else's phone.

---

## Phase 1 — Real App, Real Database (Weeks 3–6)

**Goal:** A CRUD web app with a Postgres database that a family member uses weekly.

**App ideas (pick one, or invent your own):**
- **Family Recipe Box** — everyone submits recipes, browse/search, "what should we cook tonight?" picker
- **Chore & Allowance Tracker** — siblings log chores, parents approve, running balances
- **Team Stats Tracker** — for a rec-league team (pool, hoops, whatever): log matches, standings, streaks
- **Gift Vault** — family members keep wish lists; others mark items "claimed" secretly

**Sessions cover:**
- 1.1 — Data modeling on paper first: entities, relationships, drawing the schema. *Concepts: tables, rows, primary/foreign keys, one-to-many.*
- 1.2 — Supabase tour + SQL basics: project setup, then a proper walk through the dashboard — table editor, SQL editor, database settings (where the connection string lives), logs, and API keys (and which ones must never be exposed). Then SQL by hand in the editor: CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY — no Python yet. *Concepts: types in SQL, NULL, constraints, what a connection string encodes (host/port/user/db).*
- 1.3 — Connecting to Postgres two ways: first from the terminal with `psql` (connect, `\\dt`, run queries against the live database, feel like a real DBA), then from Python with psycopg and parameterized queries. Establish the **inspect-the-data ritual**: after any code writes to the database, immediately query the table and confirm the rows are what you think they are. *Concepts: clients vs. servers again, SQL injection and why we never f-string queries.*
- 1.4 — FastAPI routes + Jinja templates: list page, detail page. First look at FastAPI's auto-generated `/docs` (Swagger UI) — the app already has an interactive API console for free. *Concepts: routing, path/query params, template rendering, what OpenAPI docs are.*
- 1.5 — Forms and writes: POST endpoints, validation with Pydantic. *Concepts: GET vs POST, server-side validation, redirect-after-post.*
- 1.6 — HTMX for interactivity: inline edits, deletes without page reloads. *Concepts: partial rendering, the request/response cycle again but sharper.*
- 1.7 — JOINs and aggregates: the "standings" or "balances" page. *Concepts: JOIN types, GROUP BY, thinking in sets.*
- 1.8 — Deploy to Railway with Supabase env vars; onboard the first real users. Then **production debugging bootcamp**: keep the Railway logs open while family uses the app for the first time — watch real requests, identify a slow one, find the first real error, and trace it from log line → code line → data. Learn what error language actually says: status codes in logs, Python tracebacks vs. HTTP errors vs. database errors, and how to tell which layer broke. *Concepts: secrets management, log levels, reading production errors, the debugging triage question: "is it the code, the data, or the config?"*
- 1.9 — **Guided bug drills, database edition:** Claude plants two bugs across the session — a missing WHERE clause (the update that changes every row) and a misnamed env var (works locally, dies on Railway). Student drives with Claude coaching. Both bug archetypes go in the concept ledger; the env-var one is the first "works on my machine" lesson. *Concepts: local vs. production config drift, why UPDATE without WHERE is famous.*

**Phase exam includes:** writing a JOIN query from a word problem, explaining what Pydantic validation prevents, and tracing a form submission from browser to database and back.

---

## Phase 2 — Adding AI (Weeks 7–10)

**Goal:** The Phase 1 app (or a new one) gains genuinely useful AI features. Student understands tokens, prompts, context, and tool use — not just "call the magic function."

**Feature ideas layered onto the existing app:**
- Recipe Box → "paste any recipe URL/photo text and AI structures it into the database"; "suggest dinner from what's in the fridge"
- Chore Tracker → natural-language logging ("I did dishes and walked the dog") parsed into structured entries
- Stats Tracker → AI-written weekly recap of the team's performance in a sports-journalist voice
- Any app → a chat assistant that can answer questions about the app's own data

**Sessions cover:**
- 2.1 — First API call: the Messages API, roles, system prompts. Build a CLI chatbot. *Concepts: tokens, context windows, temperature, why the model "forgets" (stateless APIs).*
- 2.2 — Prompt engineering deliberately: instructions, examples, output formats. A/B test prompts on a real task from the app. Explicitly connect it to the **prompting-your-AI-pair** skill you've been practicing since session one — same levers (context, constraints, output shape, edge cases), one aimed at a feature inside your product, the other at the AI building your product. *Concepts: few-shot, specificity, evaluating outputs, prompt-as-spec.*
- 2.3 — Structured outputs: getting JSON reliably, validating with Pydantic, handling failures. *Concepts: schemas as contracts, retries, never trusting model output blindly.*
- 2.4 — Streaming responses into the web UI. *Concepts: server-sent events, chunked responses, perceived latency.*
- 2.5 — Tool use: give Claude a function that queries your database; build "chat with your app's data." *Concepts: the tool-use loop, function schemas, agent loops at their simplest.*
- 2.6 — Your first real API endpoint: expose the AI feature as a JSON endpoint (`POST /api/summarize` or similar) separate from the HTML pages — the first true client/server split. Test it three ways: the `/docs` console, raw `curl` from the terminal (headers, `-d` bodies, watching status codes), and from a second tiny Python script acting as a "client." *Concepts: API vs. website, JSON request/response contracts, content-type headers, why machines talk JSON.*
- 2.7 — Cost, latency, and safety: token counting, choosing model tiers, rate limits, what not to send to an API. *Concepts: pricing math, prompt injection basics, PII hygiene.*
- 2.8 — **Hinted bug drill, AI edition:** Claude plants a silent failure — the API call errors but the code swallows the exception and shows the user nothing. Student drives the hunt; Claude answers direct questions only. Then add proper error handling and logging so this class of bug can never hide again. *Concepts: silent failures, why bare `except:` is a trap, logging as insurance.*
- 2.9 — Build week: ship the AI feature to your real users, gather reactions, iterate — Railway logs open while they try it.

**Phase exam includes:** hand-computing a rough cost for a feature at N users, diagnosing a malformed-JSON failure, and explaining the tool-use loop with a diagram.

---

## Phase 3 — A Public-Ready App: API, Users & Security (Weeks 11–16)

**Goal:** A second, more ambitious app built for people *beyond* family — with a real API layer, full user accounts, security, and polish. This is the app that could be monetized in Phase 5, built the way a professional team would: a JSON API server with the web pages as just one client of it.

**App ideas:**
- **AI Study Buddy** — upload notes, get flashcards and adaptive quizzes (very meta: the student has been living this loop)
- **Group Trip Planner** — friends vote on options, AI drafts itineraries and splits costs
- **Hobby Coach** — workout/golf/pool practice logger with AI feedback on trends
- **Local Discovery Bot** — "what should we do tonight" for their town, personalized over time

**Sessions cover:**
**Block A — the API layer (sessions 3.1–3.2):**
- 3.1 — API design for real: REST principles — resources as nouns, verbs as methods, status codes as vocabulary (200 vs 201 vs 400 vs 401 vs 403 vs 404 vs 422 vs 500, and when each is correct). Design the app's API on paper first, then build versioned JSON routes (`/api/v1/...`) with Pydantic request/response models, separate from any HTML. *Concepts: REST, resource modeling, versioning, serialization, the API as a contract.*
- 3.2 — API testing as a discipline: start with `curl` to feel raw HTTP, then set up **Bruno** and build a collection covering every endpoint — happy paths AND failure cases (bad input → expect 422, missing resource → expect 404). The collection is plain files, committed to the repo, and kept green from now on: every new endpoint gets its Bruno requests the same session it's built. (Postman is the same idea and the name recruiters know — mention it, show a screenshot, move on.) *Concepts: headers, request bodies, environments (local vs. prod base URLs), asserting on status codes, testing the failure paths on purpose.*

**Block B — user management (sessions 3.3–3.5):**
- 3.3 — Accounts I, signup & login: Supabase Auth with email + password, plus a `profiles` table for username (unique constraint, since auth identities are email-based), display name, and avatar. Email verification flow — send it, click it, understand the token behind it. Login, logout, sessions. *Concepts: password hashing (why plaintext passwords are a fireable offense), JWTs and what's inside one (decode a real token together), verification tokens, cookies vs. bearer tokens.*
- 3.4 — Accounts II, the full lifecycle: password reset flow, profile editing, changing email, and account deletion — including the grown-up question of what happens to the user's data when they delete (cascade vs. anonymize). **Optional but encouraged: social login** — add "Sign in with Google" via Supabase OAuth, and walk the redirect dance step by step (app → Google → consent → callback → session) until it's not magic. Handle the edge case: same email signs up with password AND Google. *Concepts: the OAuth authorization-code flow, redirect URIs, identity linking, why "Sign in with X" exists.*
- 3.5 — Securing the endpoints: protect API routes with JWT bearer auth (FastAPI dependencies), enforce ownership with row-level security, and understand the difference between "who are you" and "what may you do." Then attack your own API in Bruno: no token → expect 401, expired token → 401, valid token but someone else's resource ID → 403/404, and keep those attack requests in the collection permanently as security regression tests. Finish with CORS (what it protects and how to configure it for a future separate frontend), basic rate limiting, and API keys for machine-to-machine clients. *Concepts: authn vs. authz, bearer auth, RLS, insecure direct object reference (IDOR), CORS, rate limiting, why security tests live in the collection forever.*

**Block C — engineering maturity (sessions 3.6–3.15):**
- 3.6 — Project structure at scale: routers, services, config; environment separation (dev/prod). The formal treatment of the small-files habit practiced since Phase 1 — take the app's biggest file and split it along its seams, out loud. *Concepts: separation of concerns, cohesion vs. coupling, why mega-files rot, twelve-factor basics.*
- 3.7 — Testing: pytest, testing routes and the AI-adjacent logic with mocks; how pytest and the Bruno collection complement each other. *Concepts: unit vs. integration tests, fixtures, why tests let you change code fearlessly.*
- 3.8 — Migrations: evolving the schema without losing data (Alembic or Supabase migrations). *Concepts: schema versioning, backwards compatibility.*
- 3.9 — Background work, concurrency & race conditions: move slow AI jobs off the request path, then confront what happens when two requests run at once. Reproduce a real race — two rapid submits creating duplicate rows, or two updates clobbering each other (the lost-update problem) — then fix it properly. *Concepts: queues conceptually, task status polling; concurrency vs. parallelism, race conditions, the lost update, atomicity and database transactions, optimistic locking (version columns), and idempotency (why "submit once" is a lie and how to make repeats safe).*
- 3.10 — Caching & performance: make a slow page fast without changing what it does. When is stale data acceptable, and when is it dangerous? Cache-aside pattern, TTLs, and the hard part — **invalidation** (why "there are only two hard problems" is a joke about this). Where caches live: in-process vs. a shared store (Redis-style) vs. the HTTP layer itself — set cache headers / ETags so the *browser* stops re-fetching, tying caching back to the frontend↔backend boundary. Measure before and after. *Concepts: cache-aside, TTL, cache invalidation and staleness, cache hit/miss, where to cache (app vs. shared vs. HTTP), ETags and conditional requests, the cost of a cache-miss stampede.*
- 3.11 — **Solo bug drill (announced):** "there are two bugs somewhere in the auth flow and API we built — find and fix them." Timed, no help; one is an authorization hole (user A can read user B's data through the API — your Bruno attack requests should catch it), one is mundane. Results go to the mastery map. Debugging is now a graded skill, not an emergency.
- 3.12 — Polish: error pages, loading states, empty states, mobile layout.
- 3.13–3.15 — Build weeks: closed beta with 5–10 friends, feedback loop, fix, repeat. From here on, occasional **unannounced** bug drills: sometimes the session's code just doesn't work, and figuring out why is the session — revealed as a drill afterward.

**Phase exam includes:** designing a small REST API from a word problem (endpoints, methods, status codes), a security walkthrough ("attack your own API": what happens if I change the ID, drop the token, replay an expired one?), explaining the OAuth redirect flow from memory, writing a test for a given route, and a live schema migration.

---

## Phase 4 — Understanding What You Built (Weeks 17–18)

**Goal:** Ground your vibe coding all the way down. Two weeks of deliberately going *down* the stack, using the student's own apps as the case study — so the layers the AI usually handles for you (the request lifecycle, the event loop, the query planner) stop being magic. This is what turns a fast vibe coder into a dangerous-good one who can debug anything.

- 4.1 — What actually happens on a request: DNS → TLS → load balancer → your process. Read Railway logs like a pro. *Concepts: HTTP over the wire, status codes deeply, headers.*
- 4.2 — Python under the hood: how imports work, virtualenvs, what `async` actually does in FastAPI. *Concepts: the event loop, blocking vs. non-blocking.*
- 4.3 — Database internals lite: indexes (add one to your slowest query and measure), EXPLAIN, transactions. *Concepts: why the app got faster, ACID in plain English.*
- 4.4 — Read code you didn't write: pick one dependency, read its source for an hour, present how one function works.
- 4.5 — Solo rebuild challenge: rebuild a core slice of Phase 1's app from an empty folder, **no AI assistance**, in one sitting. This isn't a rejection of AI — it's the diagnostic that proves the understanding is genuinely yours and that you could keep going if the AI were down. Pass it and you *know* your vibe coding is grounded. This is the graduation exam for technical understanding.

---

## Phase 5 — Monetization & Public Launch (Weeks 19–22+)

**Goal:** The Phase 3 app goes public with a payment path. Even $1 of revenue changes how you think.

- 5.1 — Pricing & packaging: free tier vs. paid, what to gate. Study 3 comparable products' pricing pages.
- 5.2 — Stripe integration: checkout, webhooks, subscription state in the database. *Concepts: webhooks (signed events), idempotency, never trusting the client about payment state.*
- 5.3 — Landing page & copy: the one-sentence pitch, screenshots, a real domain (~$10/yr).
- 5.4 — Analytics & observability: basic event tracking, error alerting, uptime monitoring. *Concepts: measuring activation/retention, the difference between "deployed" and "operated."*
- 5.5 — Launch: post to one community where target users actually are (a subreddit, a Discord, school groups). Handle real strangers' feedback.
- 5.6 — Legal/ops lite: terms & privacy templates, handling user data responsibly, when it'd be time to form an LLC.
- Ongoing — the operating loop: weekly metrics review, support, iteration. This phase never really ends; that's the point.

---

## Concept Ledger (what "done" looks like)

By graduation the student can, without AI help: explain HTTP request/response and status codes; write and read SQL including JOINs and aggregates; design a normalized schema; write Python functions/classes with error handling; use git fluently; explain tokens, context, prompting, structured outputs, and tool use; design and build a versioned REST API and test every endpoint (including failure and attack cases) in curl/Bruno; implement full user management — email+username signup, verification, password reset, deletion, and OAuth social login — and explain hashing/JWTs/RLS/CORS; explain and apply caching (what to cache, TTLs, and the invalidation problem, including HTTP caching/ETags); reason about concurrency and race conditions (the lost update, database transactions, optimistic locking, and idempotency); structure a codebase into small, focused modules and articulate the seams they split on; write basic tests; deploy and debug a production app; integrate payments via webhooks; connect to and query a production database to verify data; read server logs to triage whether a failure is code, data, or config; debug systematically from an error message with no AI help; **prompt and steer an AI pair to produce senior-quality code — naming constraints and edge cases, spotting slop, and iterating a weak result into a strong one**; and — most importantly — **read any file in their own codebase and explain what it does and why it's there.**

## Rules of Engagement (grounded vibe coding, enforced by the harness)

The point isn't to slow down the AI — it's to make sure the person driving it understands what ships. Build as fast as you like; these gates keep it from becoming slop.

1. No code is committed until the student explains the diff out loud/in writing. Generate freely; ship nothing you can't explain.
2. The AI can write whole chunks at once — but the student directs each one (ideally with a prompt they wrote), and every chunk gets a comprehension checkpoint before it's accepted. The bigger the generation, the harder the read-back.
3. Every session has at least 2 **comprehension checkpoints** — read-and-explain, predict-the-output, spot-the-bug, steer-the-weak-result, or modify — including some "you-write-this" blocks (kept light in early phases, a regular mode from Phase 3 on).
4. Reading is a primary skill: the student can open any file in the project and explain what it does and why.
5. Prompting is a primary skill: the student drafts the prompts that drive the build, catches slop, and re-steers weak output (graded via `prompt-craft`).
6. Quizzes are not optional; failed concepts recycle via spaced repetition until passed twice.
7. One AI-free **diagnostic** exercise per week, minimum (reading/explanation early, write-it-yourself later) — to prove the understanding is real, not to ban the AI.
8. "It works" is never the finish line — "I can explain why it works, and I could debug it if it broke" is.
