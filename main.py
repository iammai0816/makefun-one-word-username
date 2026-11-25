#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes the entrant's own make.fun username, a single word, to
``entry.txt`` inside the output directory. Nothing else is written,
and the program is fully deterministic: no network, no secrets, and
no reads from outside this repository.
"""

import os
from pathlib import Path

USERNAME = "clever-beacon-11"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    text = USERNAME

    # The gate requires one word of 1-30 characters.
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    assert text.split() == [text], "entry must be a single word"
    assert not any(ch.isspace() for ch in text), "entry must contain no whitespace"

    target = output_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {target}")


if __name__ == "__main__":
    main()
