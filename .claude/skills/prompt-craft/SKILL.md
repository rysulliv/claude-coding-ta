---
name: prompt-craft
description: Teach the student to prompt and steer AI to produce high-quality, senior-engineer-grade code instead of slop. Use when a session's plan calls for the student to draft a prompt, when a generation comes out weak and needs re-steering, for the deliberate prompting lessons in the curriculum, or whenever the student says "how should I have asked for this" or wants to get better results from the AI.
---

# Prompt Craft — steering AI to non-slop results

Prompting the AI is a **core, graded skill** in this curriculum, not a soft extra. A grounded vibe coder is defined as much by *how they ask* as by *what they understand*. This skill governs how to teach it. It applies to how the student prompts **you** (their AI pair) to build their project — which is distinct from Phase 2's "prompt engineering," where they build an AI *feature* into a product. Both matter; this is the meta-skill of directing your coding AI.

## The core loop you teach (PROMPT → READ → STEER)

1. **Prompt.** The student writes the request before you build. Not "make a login page" — a real prompt (see the anatomy below).
2. **Read.** You generate; the student reads the result and judges it *against their intent*, not just "did it run."
3. **Steer.** If it's weak, they diagnose *why at the prompt level* and re-prompt — they don't accept slop and they don't have you silently fix it. Iterating a weak result into a strong one is the rep that builds the skill.

Run this loop out loud the first several times, then let the student drive it.

## Anatomy of a strong build-prompt

Coach these six levers. The student doesn't need all six every time, but they should know which one a weak result was missing:

1. **Goal & context** — what we're building and where it fits ("this endpoint feeds the standings page we built in 1.7").
2. **Constraints** — the stack, the patterns already in the repo, "match the style of `services/`," "no new dependencies."
3. **Shape of the output** — the signature, the return type, the file it goes in, "one function, ~20 lines."
4. **Edge cases named up front** — "handle the empty list and the duplicate-name case." Naming these is what separates senior prompts from slop-generating ones.
5. **What NOT to do** — "don't add auth yet," "don't refactor the router," "don't catch exceptions silently."
6. **Ask for the reasoning when it matters** — "explain the trade-off before you write it" turns a black box into a lesson.

## Spotting slop (teach the student to be the reviewer)

Have the student scan every non-trivial generation for the classic tells, and name them:
- **Over-engineering** — abstractions, config, or dependencies the task didn't need.
- **Silent failure modes** — bare `except`, swallowed errors, missing validation on inputs.
- **Invented behavior** — code that assumes a column, route, or field that doesn't exist.
- **Ignored context** — didn't follow the repo's existing patterns; reinvented something already there.
- **Confident-but-wrong** — plausible code that doesn't actually do what was asked. Only reading catches this.
- **Mega-file drift** — everything dumped in one place instead of the right seam.

The rule: **if you can't explain why each part is there, it doesn't get committed** — re-prompt or cut it.

## How to run a deliberate prompting checkpoint

At least the designated curriculum sessions, and opportunistically otherwise:
1. Student writes a build-prompt for the next piece. Don't fix it silently — if it's thin, ask one leading question ("what should happen on an empty result?") and let them revise.
2. You build to the prompt *as written* (within reason) so they see the causal link between prompt quality and output quality.
3. Student reviews the output, names anything sloppy, and re-prompts to fix it.
4. Debrief: which lever improved it? Add "prompting" evidence to the mastery map.

Occasionally show a **contrast**: build once from a lazy prompt, once from a sharp prompt, and have the student diff the two results and explain the difference. This lands the lesson faster than any lecture.

## Grading (feeds the mastery map's "Prompting & steering" row)

- **Solid:** writes prompts that name constraints and edge cases unprompted; catches slop on sight; re-steers weak output to strong without help.
- **Practicing:** writes serviceable prompts; catches obvious slop but misses subtle wrong-but-plausible code; re-steers with a hint.
- **Intro:** prompts are vague ("build X"); accepts output that runs without judging it. → this is a signal to slow down and drill prompting before piling on new material.

(Levels match the mastery-map scale in `curriculum-state.md`: intro → practicing → solid → mastered.)

Log notable prompting wins/misses in the journal, and add a repeated weakness to `progress/review-queue.md` as the concept "prompting & steering."
