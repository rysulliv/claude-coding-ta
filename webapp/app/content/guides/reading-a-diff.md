# Reading a diff

A **diff** is a before-and-after picture of a change. Your mentor proposes every code change as a diff, and reading it is *the* core skill of grounded vibe coding — it's how you stay the author of code the AI typed.

## The anatomy

- **Green / `+` lines** were added.
- **Red / `-` lines** were removed.
- A line with no colour is unchanged, shown for context.
- The header (like `@@ -12,7 +12,9 @@`) tells you *where* in the file the change is: old line 12, new line 12.

## How to actually read one (don't just click accept)

1. **Read the removed lines first.** What behaviour is going away?
2. **Read the added lines.** What's replacing it? Say it out loud in one sentence.
3. **Ask "what could this break?"** — the empty case, a null, a wrong type, a missing `await`.
4. **Only then accept.** If you can't explain what a chunk does, that's the signal to ask your mentor *before* accepting — never after.

> The rule of this whole course: **ship nothing you can't explain.** A diff you accepted without reading is exactly that.

## Keep auto-accept OFF

Reading every diff is half of how you become a real developer. If auto-accept ever turns on, turn it back off.
