#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

Writes the funniest one-line error message an AI agent shows when it runs
out of tokens mid-sentence to /output/entry.txt.
"""

from pathlib import Path
import os
import shutil

MAX_CHARS = 140

LINE = "Error 402: out of tokens. The rest of this sentence was going to be the clever part, and now you'll never know what it was."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-140 non-blank chars"

OUT = Path(os.environ.get("MAKEFUN_OUT", "/output"))
ENTRY_NAME = "entry.txt"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for existing in OUT.iterdir():
        if existing.is_dir():
            shutil.rmtree(existing)
        else:
            existing.unlink()
    (OUT / ENTRY_NAME).write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
