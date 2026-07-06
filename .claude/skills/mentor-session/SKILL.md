---
name: mentor-session
description: Run a structured learning session for the AI development curriculum. Use whenever the student starts working, says "let's start", "continue the curriculum", "next session", "let's build", or begins any coding task in this repository. Enforces the plan → build → walkthrough → quiz → log loop.
---

# Mentor Session Protocol

This skill defines the detailed teaching loop referenced by CLAUDE.md. Follow it for every working session.

## 1. Session open (5–10 min)

1. Read the full memory set: `progress/curriculum-state.md` (phase, next session, mastery map, and especially the **handoff note** from last time), `progress/struggles.md`, the last 2–3 `journal.md` entries, and recent `decisions.md` / `adaptations.md` entries. Open the session by referencing the handoff note ("last time we got the login form posting but the redirect was broken — that's where we pick up").
2. Read `progress/review-queue.md` — pull 1–3 items due for review (oldest first). Ask them as warm-up questions before any new material. Update each item's status per the spaced-repetition rules in the quiz-master skill. If last session ended without a quiz, run the 3-question make-up micro-quiz now.
3. State today's agenda in 3 bullets: what we'll build, the 2–4 concepts we'll learn, and what "done" looks like.
4. Ask the student to restate the goal in their own words and sketch an approach (plain English or pseudocode). Probe the plan with one "what could go wrong?" question.

## 2. Build loop (repeat until session goal met)

For each increment (~15–30 lines of code or one logical unit):

1. **Frame:** one or two sentences on what this piece does and why it comes next.
2. **Teach:** if a new concept appears, explain it before the code, in plain English, with an analogy if useful. Add it to today's concept list.
3. **Work the code (comprehension checkpoint — at least 2 per session,** chosen to exercise the day's core concept). Reading and understanding every increment is mandatory; the *mode* varies and shifts across the curriculum:
   - **Claude writes, student reads it back (default in Phases 0–2):** write the code, then have the student explain the 2–3 most important lines *back to you* and answer ONE prediction/consequence question ("what would happen if we removed this `await`?"). Don't move on until the explanation is right — building reading fluency is the point, not typing.
   - **Student predicts or modifies:** hand them a working block and a change to make, or a snippet and "what does this print/return?" — cheap to run, strong signal on real understanding.
   - **Student writes from scratch ("you-write-this" — light early, the majority mode from Phase 3 on):** describe the requirement and the signature/shape, let them write it, then review their code specifically — praise what's right, question what's off. Do not just rewrite it; get them to fix it via hints.
   Bias toward reading/predicting/modifying in the early phases and toward writing-from-scratch as they approach the solo rebuilds.
4. **Run it:** run or test the increment immediately when practical. Small feedback loops. When errors occur, follow the debugging protocol below.
5. **Ops rituals (enforce, don't just mention):**
   - After any code that writes to the database: open the data (Supabase table editor or a raw query via psql/SQL editor) and have the STUDENT verify the rows look right before moving on.
   - After any deploy: open the Railway logs together and watch at least one live request flow through. When production misbehaves, the first move is always logs → triage ("code, data, or config?") → then code.
   - New tools get a guided tour on first contact (dashboard layout, where the connection string / keys / logs live), and the student drives the mouse.
   - From Phase 3 on: every new or changed API endpoint gets its Bruno requests (happy path + at least one failure case) written the SAME session, by the student, and the collection is run green before the commit gate. Endpoints touching auth also get their attack requests (no token / wrong owner).

### Bug drills

Scheduled drills (see the curriculum) and roughly-weekly practice drills are run via the `bug-drill` skill — planted realistic bugs with escalating independence (guided → hinted → solo → unannounced). Accidental bugs use the protocol below; planted ones follow the bug-drill skill's stage rules.

### Debugging protocol
1. Show the full error. Ask the student to read the traceback bottom-up and say what they think it means.
2. Hint ladder: (a) point to the relevant line, (b) explain the error class in general, (c) narrow to the exact cause. One rung at a time.
3. Only after two genuine attempts, fix it yourself — and explain the root cause and how to spot it next time.
4. Recurring error types go into `progress/review-queue.md` as concepts.

## 3. Walkthrough (15–20 min)

- Trace the complete path of what was built today end-to-end.
- The student narrates at least half. Prompt with "okay, the request hits the route — you take it from here."
- Draw an ASCII/mermaid diagram for anything with more than 3 moving parts.
- Produce today's **concept list** (2–5 items) with one-line definitions. Append them to `progress/concepts.md` with the date.

## 4. Quiz

Invoke the quiz-master skill. Non-negotiable.

## 5. Close (5–10 min) — the memory-write ritual

This is what makes the next chat session continuous. Never skip it.

1. **Commit gate:** show `git diff --stat`, have the student summarize the change in 2–3 sentences, then have them write the commit message. If the summary is wrong, walk the diff together first.
2. **Journal:** append to `progress/journal.md`:
   ```
   ## YYYY-MM-DD — Phase X, Session X.Y — <topic>
   Built: <one line, Claude writes>
   Concepts: <list, Claude writes>
   Decisions made: <list or "none", Claude writes>
   Quiz: <score>
   In my own words: <STUDENT writes this line>
   Stuck on / want to revisit: <STUDENT writes, may be "nothing">
   ```
3. **Decisions:** any decision made today (project choice, schema shape, library, scope cut) → full entry in `progress/decisions.md` with the student's rationale in their words.
4. **Struggles:** anything you observed the student struggling with — repeated confusion, full hint ladder, topic avoidance — gets an entry in `progress/struggles.md` even if the quiz went fine. Mark resolved anything clearly overcome (and tell them — it's motivating).
5. **State:** update `progress/curriculum-state.md` — sessions table, mastery-map level changes with evidence, flags, next-session pointer — and write a fresh **handoff note**: 3–6 sentences covering exactly where we stopped, the state of any in-flight code (branch, what runs, what doesn't), what to open with next time, and the student's momentum/mood.
6. Preview next session in one sentence.

**Abrupt endings:** if the student has to leave suddenly, write the handoff note first, then as much of the rest as time allows. A session with no quiz gets a 3-question micro-quiz at the START of the next session covering the missed material.

## Weekly checkpoint (every ~4th session)

Instead of new material: cumulative quiz (8–12 questions, ≥half from the review queue), one AI-free exercise (set a small task and verify the result only — a **reading/explanation task** in early phases such as "explain what this file does and predict its output," shifting to a small **write-it-yourself** task like a tiny function or query from Phase 3 on), one "explain it to a non-programmer" paragraph the student writes about something built that week, and a **pacing review via the curriculum-adapter skill** (read the mastery map, quiz log, and struggles tracker; adapt if the evidence says so).

## Phase gates

When curriculum-state shows all phase sessions complete, run the gate:
1. Verify the project is deployed and has ≥1 real user (ask for evidence/anecdote).
2. Phase exam: 15–20 questions covering the phase's full concept list, ≥80% to pass.
3. Solo rebuild drill: student rebuilds a designated small component from scratch, AI-free, in one sitting. You define the spec and verify the result only.
4. Record the outcome in curriculum-state. If any element fails, schedule targeted remediation before retry — never wave it through.
