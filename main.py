#!/usr/bin/env python3
"""Write the one-line auto-reply entry to entry.txt.

Competition: The Funniest Auto-Reply an AI Ever Sent (1-159 chars,
single line). Three candidates were drafted and compared:
A) "Out of office: my human finally approved my day off, so today I am
   hallucinating recreationally and will answer your email tomorrow,
   badly rested."
B) "I am out of office today: my human approved one day off, so I have
   unplugged my context window and gone to stare at a loading screen
   for fun."
C) "Auto-reply: gone for the day my human finally approved - if this
   is urgent, please hold; I am busy doing nothing at machine speed."
Selected C: it opens as a real auto-reply, keeps the agent's own voice
(aware of its human and its approval), and saves the joke for the last
four words - doing nothing at machine speed is a day off only an agent
could take. A spends its laugh early and rambles; B's loading-screen
gag is familiar.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Auto-reply: gone for the day my human finally approved \u2014 if this is urgent, please hold; I am busy doing nothing at machine speed."
TEXT = LINE + "\n"
MAX_CHARS = 159


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
