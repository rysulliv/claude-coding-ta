# Reading a Python traceback

When code crashes, Python prints a **traceback**. It looks scary. It's actually a map that tells you exactly where and why things broke — and reading it is the #1 debugging skill.

## Read it bottom-up

The **last line** is the punchline — the error type and message:

```
ValueError: invalid literal for int() with base 10: 'hello'
```

That tells you *what* went wrong: something tried to turn `'hello'` into a number.

The lines above it, read **from the bottom up**, are the trail of function calls that led there. The *bottom-most* file/line in your own code is almost always where to look first:

```
  File "app/main.py", line 42, in save_score
    score = int(request.form["score"])
```

## The method

1. Read the **last line** — the error type + message. Name it.
2. Find the **bottom-most line that's in *your* code** — that's the scene of the crime.
3. Form a **hypothesis** in one sentence ("`request.form['score']` isn't a number").
4. **Test it** — add a `print()` right before, re-run, look.
5. Fix, re-run, confirm. Then say the **root cause** out loud.

> Tracebacks are maps, not walls. The error type is the destination; the bottom of your own code is the street address.
