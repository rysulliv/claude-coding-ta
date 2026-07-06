# Prompting your AI pair

Vibe coding is only as good as your prompts. A lazy prompt gives you slop; a sharp one gives you senior-quality code. This is a *skill*, and it's graded — here are the levers.

## The six levers of a strong build-prompt

1. **Goal & context** — what you're building and where it fits. *"This endpoint feeds the standings page we built earlier."*
2. **Constraints** — the stack and existing patterns. *"Match the style of the other files in `services/`. No new dependencies."*
3. **Output shape** — the signature, return type, and file. *"One function, ~20 lines, in `services/scores.py`."*
4. **Edge cases up front** — *"Handle the empty list and the duplicate-name case."* Naming these is what separates a senior prompt from a slop-generating one.
5. **What NOT to do** — *"Don't add auth yet. Don't refactor the router. Don't swallow exceptions."*
6. **Ask for reasoning when it matters** — *"Explain the trade-off before you write it."*

## The loop: PROMPT → READ → STEER

1. **Prompt** — write the request before the AI builds.
2. **Read** — judge the result against what you *meant*, not just "did it run."
3. **Steer** — if it's weak, figure out *which lever was missing* and re-prompt. Don't accept slop; don't silently let it get fixed for you.

## Spotting slop

- Over-engineering (abstractions the task didn't need)
- Silent failures (`except:` that hides errors, no input validation)
- Invented behaviour (assumes a column/field that doesn't exist)
- Confident-but-wrong (plausible code that doesn't do what you asked — only *reading* catches this)

> If you can't explain why each part is there, it doesn't get committed. Re-prompt or cut it.
