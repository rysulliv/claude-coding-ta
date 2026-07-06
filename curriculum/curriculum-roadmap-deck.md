---
marp: true
title: "From Zero to Shipped — Grounded Vibe Coding"
description: "Course roadmap: build real AI apps fast, understand every line."
paginate: true
size: 16:9
theme: uncover
style: |
  :root {
    --brand: #6d5efc;
    --brand-2: #22c55e;
    --ink: #0f1222;
    --muted: #5b6178;
    --bg: #ffffff;
    --card: #f4f4fb;
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  section {
    background: var(--bg);
    color: var(--ink);
    font-size: 30px;
    padding: 60px 70px;
    line-height: 1.35;
  }
  h1 { color: var(--ink); font-size: 60px; letter-spacing: -1px; }
  h2 { color: var(--brand); font-size: 40px; letter-spacing: -0.5px; }
  h3 { color: var(--ink); font-size: 30px; }
  strong { color: var(--brand); }
  a { color: var(--brand); }
  em { color: var(--muted); font-style: normal; }
  code { background: var(--card); color: #3b2fd6; padding: 2px 8px; border-radius: 6px; }
  ul { margin-top: 0.2em; }
  li { margin: 0.28em 0; }
  section.lead { text-align: left; }
  section.lead h1 { font-size: 66px; }
  .pill { display:inline-block; background: var(--brand); color:#fff; padding: 6px 16px; border-radius: 999px; font-size: 22px; font-weight: 700; letter-spacing: 0.3px; }
  .pill.green { background: var(--brand-2); }
  .muted { color: var(--muted); font-size: 24px; }
  .big { font-size: 40px; line-height: 1.25; }
  footer { color: var(--muted); font-size: 18px; }
  section::after { color: var(--muted); font-size: 18px; }
---

<!-- _class: lead -->

<span class="pill">COURSE ROADMAP</span>

# From Zero to Shipped

## Build real AI apps *fast* — and understand every line.

<span class="muted">A grounded vibe-coding curriculum · ~22 weeks · you ship something real every phase</span>

---

<!-- _class: lead -->

## What is *grounded* vibe coding?

You'll build fast with AI doing much of the typing — **that's the point.**

But you'll also:

- **Read** any file and explain what it does
- **Debug** it when it breaks — and know *why*
- **Prompt** the AI to produce senior-quality work, not slop

<span class="big">Build fast. Understand deeply. **Ship no slop.**</span>

---

## The deal

- The AI can build whole chunks at once — **you direct it, and you understand every line before it's accepted.**
- Every session ends with a **walkthrough** and a **quiz**. Miss something? It comes back via spaced repetition.
- You **review every diff** and write every commit message. That's how you stay the author.
- *"It works"* is never the finish line. *"I can explain why it works — and fix it if it breaks"* is.

---

## How every session runs

<span class="pill green">THE LOOP</span>

1. **Plan** — you state the goal and draft the prompt
2. **Build** — pair with the AI in small, understood steps
3. **Walk through it** — you trace how the code runs, out loud
4. **Quiz** — short, so it sticks
5. **Log & commit** — you write the message; your progress is saved

*Plus: weekly AI-free diagnostics · deliberate bug drills · prompt-craft practice*

---

<!-- _class: lead -->

## The journey — 5 phases

<span class="muted">Each phase ends with something deployed that a real person actually uses. Pace follows understanding, not the calendar.</span>

---

## Phase 0 · Foundations & First Deploy
<span class="muted">Weeks 1–2</span>

**Goal: a live URL on the internet within 10 days.**

- Your workshop: VS Code + Claude Code
- Terminal, Python, Git, GitHub
- First deploy — frontend vs. backend, reading logs
- First guided bug drill

---

## Phase 1 · Real App, Real Database
<span class="muted">Weeks 3–6</span>

**Goal: a CRUD app a family member uses weekly.**

- Data modeling · SQL by hand
- Python ↔ Postgres · routes & templates
- Forms, validation, HTMX
- JOINs & aggregates · deploy + prod debugging

---

## Phase 2 · Adding AI
<span class="muted">Weeks 7–10</span>

**Goal: genuinely useful AI features you understand.**

- The Messages API · tokens & context
- Prompt engineering · structured outputs
- Streaming · tool use ("chat with your data")
- Your first real API endpoint · cost, latency & safety

---

## Phase 3 · Public-Ready: API, Users & Security
<span class="muted">Weeks 11–16</span>

**Goal: a real app for people beyond family.**

- REST API design · testing with Bruno
- Accounts, login & "Sign in with Google"
- Auth, permissions, CORS, RLS
- Structure, tests, migrations, **concurrency & caching**

---

## Phase 4 · Understanding What You Built
<span class="muted">Weeks 17–18</span>

**Goal: ground your vibe coding all the way down.**

- What really happens on a request
- Python under the hood (async)
- Database internals (indexes, transactions)
- **Solo rebuild challenge** — the graduation exam

---

## Phase 5 · Monetization & Public Launch
<span class="muted">Weeks 19–22+</span>

**Goal: go public with a payment path.**

- Pricing · Stripe · landing page & domain
- Analytics & monitoring
- Launch to real strangers
- The operating loop that never ends

---

## Your companion dashboard

<span class="pill green">RUNS ON YOUR MACHINE</span>

A little app that keeps the journey **visible and motivating**:

- 🔥 **Streaks** & progress through the phases
- 🧠 **Quizzes** & spaced-repetition review
- 🗺️ **Concept map** of what you've learned
- 📖 How-to guides & mockups of your app
- 💬 A built-in **Claude Code client** — browse & continue your sessions

---

<!-- _class: lead -->

## The graduate

Someone who can **build a real, deployed, AI-powered app fast** —

and **read it, debug it, secure it, and explain every line.**

<span class="big">An excellent vibe coder who never ships slop.</span>

<span class="muted">Ready? Open the Claude panel and say: **"Let's start the curriculum."**</span>
