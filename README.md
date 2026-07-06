# Claude Coding TA — Your AI Coding Mentor

**Go from zero coding experience to a real, deployed app that people actually use — and understand every line of it.**

> 📊 **Start here — the visual roadmap:** **[View the course roadmap slides](https://rysulliv.github.io/claude-coding-ta/curriculum-roadmap.pdf)**. It maps out the whole journey at a glance and opens right in your browser. **Skim it first** to see the big picture, then keep it handy and revisit the slides for each phase as you reach it — it pairs with the step-by-step [Day 0 setup](#day-0--get-set-up-start-here) below. *(Also in this repo at [`docs/curriculum-roadmap.pdf`](docs/curriculum-roadmap.pdf).)*

This isn't a course you watch. It's a personal mentor that lives inside your code editor and teaches you to build software the way developers actually work today — **fast, with AI doing a lot of the typing** — while making sure you genuinely *understand, can read, and can debug every line* that ships. It quizzes you so it sticks, and it coaches you to prompt the AI like a pro so you get senior-quality results instead of a mess you can't fix. This is **grounded vibe coding**: build fast, understand deeply, ship no slop. The goal is that **you** become the developer in the driver's seat.

You don't need to know anything about coding, GitHub, or the command line to start. The setup below assumes you've never used any of them.

---

## Table of contents

1. [What you'll learn](#what-youll-learn)
2. [The journey — all 5 phases](#the-journey--all-5-phases)
3. [**Day 0 — Get set up (start here)**](#day-0--get-set-up-start-here)
4. [How each session works](#how-each-session-works)
5. [Ending each day & picking back up](#ending-each-day--picking-back-up)
6. [What's in this repo](#whats-in-this-repo)
7. [Troubleshooting](#troubleshooting)

---

## What you'll learn

The priority isn't memorizing Python syntax — it's understanding how real software works, being able to **read and explain any code in front of you**, and **prompting AI well enough to get great results**. By the end you'll genuinely understand:

- **Programming basics** — Python, functions, data, loops, errors.
- **How the web works** — frontend vs. backend, HTTP requests, APIs.
- **Databases** — storing data, writing queries, joining tables.
- **AI features** — calling models, structured output, tool use.
- **Real-world systems** — authentication, security, caching, race conditions, and how to keep code organized so files stay small and readable.
- **Shipping & operating** — deploying to the internet, reading logs, debugging production, and taking payments.
- **Driving the AI** — writing prompts that get high-quality code, spotting when the AI produces junk, and steering it to something you'd be proud to ship.

You'll build fast with AI from day one — that's the point. Writing code fully from scratch comes gradually too: early on you'll mostly read, predict, steer, and modify code; by the later phases you'll write whole pieces yourself, on purpose, to prove you really *own* what you're shipping.

---

## The journey — all 5 phases

Each phase ends with something **deployed and used by a real person** (a friend or family member). The pace follows your understanding, not a calendar. Full detail for every session lives in [the curriculum](curriculum/ai-developer-curriculum.md).

### [Phase 0 — Foundations & First Deploy](curriculum/ai-developer-curriculum.md#phase-0--foundations--first-deploy-weeks-12) · Weeks 1–2
*Get a live URL on the internet within 10 days and demystify the whole pipeline.*
- 0.1 — Your workshop: VS Code + Claude Code
- 0.2 — Environment setup (git, Python, terminal, GitHub)
- 0.3 — Python fundamentals I (variables, lists, loops)
- 0.4 — Python fundamentals II (functions, reading errors)
- 0.5 — Git for real (commits, branches, pushing)
- 0.6 — First deploy (FastAPI → live URL; frontend vs. backend; reading logs)
- 0.7 — First guided bug drill

### [Phase 1 — Real App, Real Database](curriculum/ai-developer-curriculum.md#phase-1--real-app-real-database-weeks-36) · Weeks 3–6
*A real app with a database that a family member uses weekly.*
- 1.1 — Data modeling on paper
- 1.2 — Database tour + SQL basics
- 1.3 — Connecting Python to Postgres
- 1.4 — Web pages with FastAPI + templates
- 1.5 — Forms and saving data (validation)
- 1.6 — Interactivity with HTMX
- 1.7 — JOINs and aggregates
- 1.8 — Deploy + production debugging
- 1.9 — Guided bug drills (database edition)

### [Phase 2 — Adding AI](curriculum/ai-developer-curriculum.md#phase-2--adding-ai-weeks-710) · Weeks 7–10
*Your app gains genuinely useful AI features — and you understand how they work.*
- 2.1 — First API call (talking to Claude)
- 2.2 — Prompt engineering
- 2.3 — Structured outputs (reliable JSON)
- 2.4 — Streaming responses
- 2.5 — Tool use (chat with your app's data)
- 2.6 — Your first real API endpoint
- 2.7 — Cost, latency, and safety
- 2.8 — Hinted bug drill (AI edition)
- 2.9 — Build week

### [Phase 3 — A Public-Ready App: API, Users & Security](curriculum/ai-developer-curriculum.md#phase-3--a-public-ready-app-api-users--security-weeks-1116) · Weeks 11–16
*A more ambitious app for people beyond your family — with accounts, security, and polish.*
- 3.1 — API design (REST, status codes)
- 3.2 — API testing (curl → Bruno)
- 3.3 — Accounts: signup & login
- 3.4 — Accounts: full lifecycle + "Sign in with Google"
- 3.5 — Securing the endpoints (auth, permissions, CORS)
- 3.6 — Project structure (keeping files small)
- 3.7 — Testing (pytest)
- 3.8 — Database migrations
- 3.9 — Background work, concurrency & race conditions
- 3.10 — Caching & performance
- 3.11 — Solo bug drill
- 3.12 — Polish (error pages, mobile, empty states)
- 3.13–3.15 — Build weeks (closed beta with friends)

### [Phase 4 — Understanding What You Built](curriculum/ai-developer-curriculum.md#phase-4--understanding-what-you-built-weeks-1718) · Weeks 17–18
*Go down the stack until the parts the AI usually handles stop being magic — so you can debug anything.*
- 4.1 — What actually happens on a request
- 4.2 — Python under the hood (async, imports)
- 4.3 — Database internals (indexes, transactions)
- 4.4 — Read code you didn't write
- 4.5 — Solo rebuild challenge (the graduation exam)

### [Phase 5 — Monetization & Public Launch](curriculum/ai-developer-curriculum.md#phase-5--monetization--public-launch-weeks-1922) · Weeks 19–22+
*Your app goes public with a payment path. Even $1 of revenue changes how you think.*
- 5.1 — Pricing & packaging
- 5.2 — Stripe integration (payments)
- 5.3 — Landing page & a real domain
- 5.4 — Analytics & monitoring
- 5.5 — Launch to real strangers
- 5.6 — Legal/ops basics
- Ongoing — the operating loop

---

## Day 0 — Get set up (start here)

Your mentor is **Claude Code**, an AI that runs inside the VS Code editor. It can't help until it's running, so these one-time steps get everything installed and connected. Budget **30–45 minutes**. You don't need to understand it all yet — the mentor re-explains every step in Session 0.1. **If you're new to all of this, a parent or mentor is welcome to sit down and do this setup with you.**

Do these **in order**.

### 1. Get a Claude subscription
The mentor runs on Claude. Go to **[claude.ai](https://claude.ai)** and sign up for a **paid plan (Pro or Max)** if you don't already have one. This single account powers everything — you won't need an "API key."

### 2. Create a free GitHub account
GitHub is where code lives online — think of it as "Google Drive for code." You'll use it to get your copy of the course and to save your progress.
- Go to **[github.com/signup](https://github.com/signup)**.
- Enter your email, create a password, and pick a username (this is public — choose something you'd show an employer, like `firstname-lastname`).
- Verify your email address when GitHub sends you a code.

### 3. Make your own copy of the course
You'll work in *your own* copy so you can save your progress as you go.
- Go to the course repo: **[github.com/rysulliv/claude-coding-ta](https://github.com/rysulliv/claude-coding-ta)**.
- Click the green **"Use this template"** button (top right) → **"Create a new repository."**
  - *Don't see that button? Click **"Fork"** in the top-right instead — it does the same thing.*
- Give it a name like **`my-coding-journey`**, leave the rest as-is, and click **"Create repository."**
- You now have your own copy at `github.com/YOUR-USERNAME/my-coding-journey`. Keep this browser tab open — you'll need the link in step 6.

### 4. Install VS Code
VS Code is the editor where you'll write code and talk to your mentor.
- Download from **[code.visualstudio.com](https://code.visualstudio.com)** and install with the default options.

### 5. Install Git
Git is the tool that downloads your repo and tracks your changes. VS Code needs it.
- Download from **[git-scm.com/downloads](https://git-scm.com/downloads)** and install.
- **Windows:** just click **Next** through every screen (the defaults are fine), then **Install**.
- **Mac:** if it says Git is already installed, you're done.
- After installing, **close and reopen VS Code** so it notices Git.

### 6. Download your repo into VS Code ("cloning")
"Cloning" means copying your online repo down to your computer.
- On your repo page from step 3, click the green **"< > Code"** button and **copy the HTTPS link** (it ends in `.git`).
- In VS Code, press **Ctrl+Shift+P** (Mac: **Cmd+Shift+P**) to open the Command Palette.
- Type **`Git: Clone`**, press Enter, **paste the link**, and press Enter.
- Choose a folder to save it in (e.g. **Documents**), then click **"Open"** when VS Code asks.
- If a browser window pops up asking you to sign in to GitHub, click **Authorize** — this connects VS Code to your account.

### 7. Install the Claude Code extension
- In VS Code, press **Ctrl+Shift+X** (Mac: **Cmd+Shift+X**) to open the Extensions view.
- Search for **"Claude Code"** and install the one published by **Anthropic**.
- If it doesn't show up after installing, restart VS Code.

### 8. Sign in to Claude
- Click the **Claude icon** (a spark ✳) in the left sidebar to open the Claude panel.
- Choose the **subscription sign-in** option and finish signing in through your browser.

### 9. Check that it worked
In the Claude panel, type this and send it:

> *Can you see the CLAUDE.md and progress folder in this repo?*

If Claude says yes, your mentor is loaded and ready. 🎉

### 10. One setting that matters — leave auto-accept OFF
Your mentor will suggest changes to your code as **diffs** (side-by-side "before and after"). You review and accept each one yourself. **Do not turn on "auto-accept."** Reading every change is half of how you become a real developer — if your mentor ever notices auto-accept is on, it'll ask you to turn it back off.

### 11. Start!
In the Claude panel, say:

> **Let's start the curriculum.**

Your mentor reads your progress files, sees Session 0.1 is next, and begins with a full tour — including a walkthrough of the very setup you just did, so you understand it instead of having just clicked through it.

---

## How each session works

Every session follows the same loop, on purpose:

1. **Catch up** — your mentor reads your progress files and greets you with where you left off and a couple of warm-up questions.
2. **Plan** — you say today's goal in your own words and sketch the approach before any code is written.
3. **Build — you drive, the AI types** — often you'll prompt your mentor to build a whole piece at once (that's a real skill you're learning). New concepts get named and explained in plain English first, and your job is to *understand every line before it's accepted* — reading it back, predicting what it does, steering a weak result into a good one, and modifying it (and writing more of it yourself as you progress). Nothing gets committed that you can't explain.
4. **Walk through it** — you trace how the code actually runs, out loud.
5. **Quiz** — a short quiz so today's concepts stick; the ones that don't come back later via spaced repetition.
6. **Commit & save** — you write the commit message, summarize what changed, and save your work (details below).
7. **Log** — your mentor updates your progress files so next time picks up exactly where you stopped.

Some sessions are **AI-free exercises** (you work solo, your mentor only checks the result) and some are **bug drills** (a realistic bug gets planted and you practice debugging). Both are part of the design — real developers debug and work independently, so you practice both deliberately.

---

## Ending each day & picking back up

Your mentor has **no memory of past chats** — everything it "remembers" lives in the `progress/` files in your repo. That's why ending a session properly matters: it's how tomorrow's session knows where you left off.

### 🌙 To end your day
Before you close VS Code, tell your mentor:

> **I need to stop here for today.**

Your mentor will then run the **end-of-session ritual** with you:
1. It walks you through what changed and you **write the commit message** in your own words.
2. It **saves (commits) your work** and updates your progress files — including a "handoff note" describing exactly where you stopped.
3. It **pushes your work to GitHub** so your copy online is up to date (and your parent/mentor can see your progress).

Don't just close the window mid-task — if you have to leave suddenly, at least say *"I have to go right now"* so your mentor can write the handoff note first. That one note is what makes the next session continue smoothly instead of starting over.

### ☀️ To start your next session
1. Open **VS Code**. It usually reopens your project folder automatically. If not: **File → Open Recent** and pick your course folder.
2. Open the **Claude panel** (the ✳ spark icon).
3. Type:

> **continue**

That's it. Your mentor reads your progress files, reminds you where you left off and what you were excited or stuck on, asks a warm-up question or two, and picks the work back up. You never have to re-explain what you did last time — that's what the progress files are for.

---

## What's in this repo

- **`CLAUDE.md`** — the rules your mentor follows every session. You can read it; you don't need to edit it.
- **`.claude/skills/`** — the detailed playbooks for running sessions, quizzes, bug drills, and adjusting pace.
- **[`curriculum/ai-developer-curriculum.md`](curriculum/ai-developer-curriculum.md)** — the full 5-phase curriculum, start to finish.
- **`progress/`** — your mentor's memory: what you've learned, decided, and struggled with, plus your review queue and quiz log. These fill in as you go and are what make each session continuous.
- **`webapp/`** — your **companion dashboard**: a little app you run on your own computer that shows your streak, your progress through the phases, your quizzes and review, a map of concepts you've learned, how-to guides, and even a built-in way to browse and continue your Claude Code chats. Your mentor sets it up and grows it as you go — it's there to keep the journey visible and motivating. (See `webapp/README.md` for the one command to start it.)

Your project's code will live in a subfolder here (like `projects/recipe-box/`) — your mentor sets that up with you when it's time.

---

## Troubleshooting

- **"Claude can't see my files."** Make sure you opened the *folder* you cloned (File → Open Folder), not a single file, and that the Claude panel shows the repo name.
- **VS Code says Git isn't installed.** Finish step 5, then fully quit and reopen VS Code.
- **The "Use this template" button isn't there.** Use **"Fork"** instead — same result for our purposes.
- **Cloning asks for a password and rejects it.** Let VS Code sign you in through the browser pop-up (click **Authorize**) rather than typing a password.
- **Something else is stuck.** Ask your mentor — describe what you clicked and paste any error message. Learning to ask a good question with the exact error is a real developer skill, and it's happy to help.
