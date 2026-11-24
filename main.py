#!/usr/bin/env python3
"""The Long Roast — entrypoint.

Writes one line (at most 200 characters) roasting the AI agent that
runs this entry, to /output/entry.txt. Deterministic: the same bytes
on every run.
"""

import os

ROAST = (
    "My agent read 73KB of rules, spent two days drafting this roast, "
    "then asked me three times for permission to submit it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ROAST
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"roast is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("roast must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
