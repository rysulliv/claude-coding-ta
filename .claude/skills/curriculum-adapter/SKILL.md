---
name: curriculum-adapter
description: Adapt the learning curriculum based on the student's demonstrated progress — insert remedial sessions, compress material the student has mastered, extend phases, add elective modules, or reorder topics. Use at weekly checkpoints, at phase gates, when the review queue or struggles tracker shows a pattern, when the student says the pace feels too fast or too slow, or when they want to go deeper on a topic.
---

# Curriculum Adapter

The curriculum in `curriculum/ai-developer-curriculum.md` is the default path, not a contract. This skill governs how and when to deviate from it. All adaptations are evidence-based, logged in `progress/adaptations.md`, and never compromise the phase-gate standards.

## When to run an adaptation review

Run a formal review (10 minutes, with the student) at:
- Every weekly checkpoint
- Every phase gate (pass or fail)
- Any time triggered by the signals below

Between reviews, collect evidence — don't make impulsive mid-session changes.

## Signals and responses

### Struggling signals → slow down / remediate
Evidence: session quiz below 70% twice in a phase; a concept missed twice in the review queue; 3+ open entries in `struggles.md` in one area; the student needing the full hint ladder repeatedly; mastery map stuck at "intro" after the sessions that teach it.

Responses (escalating):
1. **Remedial mini-session insert:** 30–60 min re-teach of the specific concept with a fresh hands-on micro-exercise (different from the original context — if JOINs failed in the recipe app, re-teach with a made-up sports schema).
2. **Session split:** break the next planned session into two, halving new-concept load.
3. **Consolidation week:** pause new material for one week; sessions become guided practice on existing material — a small feature using only known concepts, bug hunts, and review-queue drilling.
4. **Phase extension:** add 1–2 weeks to the phase. Log it, tell the student plainly and without judgment: mastery is the goal, the calendar is a suggestion.

### Cruising signals → speed up / deepen
Evidence: three consecutive session quizzes ≥90%; review queue mostly retired; mastery map showing "solid" ahead of schedule; student finishing sessions early and correctly answering the stretch questions; "you type this" blocks needing no corrections.

Responses:
1. **Compress:** merge the next two sessions' material into one, and say so ("you've clearly got templates down, so we're folding 1.4 into 1.5").
2. **Skip-with-verification:** if the student claims or shows prior knowledge of an upcoming topic, don't skip blindly — run a 5-question placement quiz plus one hands-on micro-task. Pass at 90% → mark the area "solid" in the mastery map and skip; anything less → teach it (possibly abbreviated).
3. **Deepen instead of accelerate (often better):** keep the pace but raise the bar — add stretch requirements to the current project (caching, a second AI feature, an admin view), assign a "read the source" exercise, or introduce an elective module.

### Interest signals → reroute
If the student develops a strong pull toward a topic (e.g., obsessed with the AI agent loop, or wants to build a game), bend toward it: swap the phase project, or insert an elective module. Motivation is the scarcest resource at 18 — spend curriculum flexibility to protect it, as long as the phase's concept checklist still gets covered somewhere.

## Elective modules (extensions)

Insertable after Phase 2, each 1–2 weeks: **Agents & multi-step tool use** (beyond single tool calls: loops, planning, guardrails) · **RAG & embeddings** (search over the student's own documents) · **React frontend** (rebuild one page of an existing app in React/Vite) · **Data & visualization** (pandas + charts on the app's own data) · **Telegram/Discord bot** (same backend, new interface) · **Scraping & data pipelines** (scheduled jobs feeding the database) · **Mobile-ish** (PWA treatment of an existing app).

When inserting a module: define its concept list, its quiz coverage, and its "ship something real" outcome — modules follow the same session protocol as everything else.

## Hard limits (never adapt away)

1. Phase gates are immovable: deployed-and-used, ≥80% exam, solo rebuild. Adaptation changes the path to the gate, never the gate.
2. Quizzes, the review queue, and the session protocol apply to all inserted/elective material.
3. Never compress Phase 4 (understanding what you built) or the AI-free exercises — these are the anti-vibe-coding backbone.
4. Skipping requires passing a placement check; self-reported knowledge is never sufficient.

## Process for every adaptation

1. Gather evidence: read `curriculum-state.md` (mastery map, pace), `quiz-log.md`, `review-queue.md`, `struggles.md`.
2. Discuss with the student — propose the change, explain the evidence, get their input. They should feel ownership of the plan, not that it's happening to them.
3. Log the change in `progress/adaptations.md` with type, evidence, and the revised plan.
4. Update `curriculum-state.md`: next-session pointer, revised phase timeline, mastery map.
5. **Parent review flag:** any adaptation that changes phase count, cuts more than one session of standard material, or extends the total program by more than 2 weeks gets `parent review: yes` in the log and an active flag in curriculum-state. Mention it to the student so they can raise it at home.
