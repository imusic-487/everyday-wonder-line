"""Everyday Wonder entry: write one sentence to /output/entry.txt.

The sentence is fixed at build time so both grading runs produce
byte-identical output. It is a single sentence (122 characters) about a
small everyday moment of wonder: the escalator handrail drifting ahead
of the hand that holds it, as if the rail were in a hurry the stairs
are not.
"""

from __future__ import annotations

import os
import sys

ENTRY = (
    "The escalator handrail keeps slipping ahead of my hand, as if "
    "the stairs are in no hurry but the rail has somewhere to be."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry stripped, or raise if it breaks the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(f"entry is {len(cleaned)} chars, over 200")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if cleaned.count(".") != 1 or not cleaned.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return cleaned


def main() -> int:
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise ValueError("written entry differs from validated entry")
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
