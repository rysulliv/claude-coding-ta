# Your AI Coding Mentor — "From Zero to Shipped"

This is a personal coding mentor that lives inside VS Code. It's not a course you
watch — it's a mentor you *build alongside*. You'll go from zero to a real,
deployed app that other people actually use, and by the end you'll understand
every line of it.

It works by turning Claude Code into a patient senior engineer who pairs with
you: it teaches in small steps, makes sure you understand and can read every
line before it moves on, quizzes you so things actually stick, and refuses to
just "vibe-code" the app for you. That refusal is the point — the goal is that
*you* become the developer, not that an app gets built.

## What you'll do

- Learn the terminal, Python, git, HTTP, SQL, APIs, auth, testing, and
  deployment — in the order you actually need them, building the whole time.
- Ship a real project to the internet and get a real person to use it.
- Keep a running record of what you've learned, what you decided, and what
  tripped you up — your mentor reads this every session so it always remembers
  where you are, even though each chat starts fresh.

## Day 0 — do these steps IN ORDER, before your first session

Your mentor is Claude Code — it can't help until it's running. These steps get
it talking; everything after this (git, GitHub, Python, all of it) is taught
inside the guided sessions, so don't worry about doing more than what's below.
Budget about 30 minutes. If you're under 18 or new to all of this, a parent or
mentor is welcome to sit down and do this setup with you.

1. **Claude account.** You need a paid Claude subscription (Pro or Max) —
   sign up at https://claude.ai if you don't have one. This one account
   powers the mentor; no API key needed for Claude Code itself.
2. **Install VS Code.** Download from https://code.visualstudio.com and
   install with defaults. (Windows: no WSL needed to start — the mentor will
   set up anything extra if a later phase requires it.)
3. **Put this folder somewhere sensible.** Unzip it into a folder like
   `Documents/learn-ai-dev`. Don't rename or move the hidden `.claude`
   folder or `CLAUDE.md` — they're the mentor's brain. (No git needed yet —
   you'll push this to GitHub yourself in Session 0.5, as a lesson.)
4. **Open the folder in VS Code.** File → Open Folder → select
   `learn-ai-dev`. Claude Code operates on the open folder, so this step is
   what puts the mentor "inside" the curriculum.
5. **Install the Claude Code extension.** In VS Code press Ctrl+Shift+X
   (Cmd+Shift+X on Mac), search **"Claude Code"**, and install the one
   published by **Anthropic**. If it doesn't appear after install, restart
   VS Code.
6. **Sign in.** Open the Claude panel (Spark icon), choose the Claude
   subscription sign-in option, and complete the browser authorization.
7. **Sanity check.** In the Claude panel type: *"Can you see the CLAUDE.md
   and progress folder in this repo?"* If yes, the mentor is loaded.
8. **Start.** Say: **"Let's start the curriculum."** Your mentor reads
   `progress/curriculum-state.md`, sees Session 0.1 is next, and begins with
   a full VS Code / Claude Code tour — including a walkthrough of the very
   setup you just did, so you understand it rather than having just clicked
   through it.

**One setting that matters:** leave edit auto-accept **OFF**. The whole point is
that you review every change your mentor proposes before it lands — that review
habit is half of what turns you into a real developer. If your mentor ever
notices auto-accept is on, it'll ask you to turn it back off.

## How each session runs

Every session follows the same loop, on purpose:

1. **Catch up** — your mentor reads your progress files and greets you with
   where you left off and a couple of warm-up questions.
2. **Plan** — you say today's goal in your own words and sketch the approach
   before any code gets written.
3. **Build in small steps** — never a giant wall of generated code. New
   concepts get named and explained in plain English, and your job is to
   *understand every line* — reading it back, predicting what it does, and
   modifying it (and writing more of it yourself as you go).
4. **Walk through it** — you trace how the code actually runs, out loud.
5. **Quiz** — a short quiz so today's concepts stick; the ones that don't come
   back later via spaced repetition.
6. **Commit** — you write the commit message and summarize what changed.
7. **Log** — your mentor updates the progress files so next session picks up
   exactly where you stopped.

Some sessions are **AI-free exercises** (you do it solo, your mentor only checks
the result) and some are **bug drills** (a realistic bug gets planted and you
practice debugging it). Both are part of the design — real developers debug and
work independently, so you practice both deliberately.

## Every day after Day 0

Open the folder in VS Code and say **"continue"** — your progress files handle
the rest. That's it.

## What's in this folder

- `CLAUDE.md` — the rules your mentor follows every session. You can read it;
  you don't need to edit it.
- `.claude/skills/` — the detailed playbooks for sessions, quizzes, bug drills,
  and adjusting pace.
- `curriculum/ai-developer-curriculum.md` — the full 5-phase curriculum, start
  to finish.
- `progress/` — your mentor's memory: what you've learned, decided, and
  struggled with, plus the review queue and quiz log. These fill in as you go.

Your project can live in a subfolder here (like `projects/recipe-box/`) so one
mentor governs everything. Your mentor will set that up with you when it's time.
