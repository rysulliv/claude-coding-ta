---
name: bug-drill
description: Deliberately plant realistic bugs in the student's code and run structured debugging exercises with escalating independence (guided → hinted → solo → unannounced). Use when the curriculum schedules a bug drill, at weekly checkpoints, when the student says "give me a bug to fix" or "debugging practice", or roughly once a week in later phases as an unannounced drill.
---

# Bug Drill

Debugging is a first-class skill taught deliberately, not left to accidents. This skill governs how to plant bugs, run drills, and grade them.

## The four stages (match to the student's phase/mastery)

| Stage | When | Protocol |
|---|---|---|
| **Guided** | Phases 0–1 | Announce the drill. Claude demonstrates the full method out loud while the student follows: read the error bottom-up → state a hypothesis → add a print/log to test it → confirm or discard → fix → re-run to verify → name the root cause. Student repeats the method summary back. |
| **Hinted** | Phase 2 | Announce the drill. Student drives entirely. Claude answers direct questions and gives hints ONLY on explicit request, using the hint ladder (point to the layer → explain the error class → narrow to the line). Track how many hints were needed. |
| **Solo (announced)** | Phase 3 | "There are N bugs in what we just built — find and fix them." Timed. Zero help. Claude only verifies the fix afterward and debriefs. |
| **Unannounced** | Phase 4+ | No announcement — the code simply misbehaves, exactly like real life. ALWAYS reveal it was a drill in the debrief; never let the student believe they or Claude randomly failed. Max ~1 per week; never during phase exams or when the student is already frustrated. |

## Planting rules

1. **Realistic only.** Plant bugs of the class a developer actually writes — never contrived puzzles. Pick from the phase-appropriate catalog below, biased toward (a) concepts recently learned and (b) weak areas in the mastery map / struggles tracker.
2. **One conceptual lesson per bug.** Every bug must have a nameable root-cause archetype that goes into the concept ledger ("UPDATE without WHERE", "silent exception swallowing", "timezone-naive datetime").
3. **Safety rails:** plant only in a git-clean state on a branch or with the pre-drill commit noted, so recovery is always one command away. Never plant in deployed production code that real users are actively using — drills run locally or in a scratch deploy. Never plant data-destroying bugs against real data (use a copy/seed data if the bug involves writes).
4. **Bookkeeping:** log each drill in `progress/quiz-log.md` (type: bug-drill) with stage, bug archetype, time taken, hints used, and outcome. Failed or heavily-hinted drills add the archetype to `progress/review-queue.md` and, if a pattern, to `struggles.md`.

## Bug catalog by phase

- **Phase 0:** off-by-one in a loop; type confusion (`"2" + 2`); wrong variable name (NameError); mutable default argument; indentation/logic mismatch.
- **Phase 1:** missing WHERE on UPDATE/DELETE (against seed data only); NULL not handled (crash on empty result); misnamed env var (works locally, dies on Railway); f-string SQL (works, but injection-vulnerable — caught by inspection not crash); redirect missing after POST (double-submit); wrong JOIN duplicating rows.
- **Phase 2:** swallowed API exception (silent failure); malformed JSON from the model not validated; prompt that breaks when user input contains quotes/braces; forgetting to pass conversation history (bot "forgets"); token limit exceeded on long input; hardcoded model string with a typo.
- **Phase 3:** missing RLS/ownership check (user A reads user B's data through the API); JWT checked on one route but not its sibling; endpoint returning 200 with an error body instead of a proper status code; wrong status code (404 where 403 belongs, leaking resource existence); CORS misconfigured to `*` with credentials; timezone-naive datetimes; race-y double-submit creating duplicates; lost update (two concurrent edits clobber each other, last-write-wins); unverified email allowed to log in; password reset token that never expires; migration applied locally but not in prod; secret accidentally logged.
- **Phase 4–5:** N+1 query pattern; missing index on the hot path; stale cache served after an update (missing invalidation); webhook handler not idempotent; webhook signature not verified; error page leaking a stack trace to users.

## Debrief (every drill, every stage)

1. Student states the root cause in one sentence and names the archetype.
2. Ask: "how would you prevent this class of bug?" (validation, test, logging, code review habit) — the prevention goes in the journal.
3. Ask: "what log line or test would have caught this in 10 seconds?" If reasonable, actually add it before moving on.
4. Update the mastery map "Testing & debugging" row with evidence.

## Grading solo drills

Found + fixed + correct root cause, in time: full credit. Fixed but can't explain root cause: half — and it goes to the review queue (a fix you can't explain is a fix you got lucky on). Not found in time: walk it together guided-style, log to struggles, and schedule a same-archetype drill within two weeks.
