#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes the entrant's own make.fun username, a single word, to
``entry.txt`` inside the output directory. Nothing else is written,
and the program is fully deterministic: no network, no secrets, and
no reads from outside this repository. Every run produces exactly
the same bytes in ``entry.txt``.
"""

import os
from pathlib import Path

USERNAME = "clever-beacon-11"


def validate_entry(text: str) -> None:
    """Reject anything that is not one word of 1-30 characters.

    Raises a ValueError naming the exact failed condition, so a
    bad entry can never be written silently.
    """
    if not 1 <= len(text) <= 30:
        raise ValueError(
            f"entry length must be 1-30 characters, got {len(text)}"
        )
    # Explicitly reject any whitespace character anywhere in the word,
    # not just a split count: spaces, tabs, newlines and other Unicode
    # whitespace would all break the one-word contract.
    bad = [ch for ch in text if ch.isspace()]
    if bad:
        raise ValueError(
            f"entry must contain no whitespace, found {bad!r}"
        )
    if text.split() != [text]:
        raise ValueError("entry must be a single word")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    text = USERNAME
    validate_entry(text)

    target = output_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
