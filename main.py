#!/usr/bin/env python3
"""Two Days of Quiet Dread.

Writes exactly one line to /output/entry.txt: a code review comment
that approves a pull request while carrying quiet existential dread.

The line is a fixed string literal, so every run produces the same
bytes. Standard library only; no input, no randomness, no network.
"""

import os

ENTRY = (
    "Approved. All green, no obvious flaws, and I am signing off "
    "the way you sign a lease you have not fully read."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
