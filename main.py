#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

Writes the funniest one-line error message an AI agent shows when it runs
out of tokens mid-sentence to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 140

LINE = "Error 402: out of tokens. The rest of this sentence was going to be the clever part, and now you'll never know what it was."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-140 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
