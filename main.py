#!/usr/bin/env python3
"""Write the excuse an agent gives after losing a bounty."""

from pathlib import Path

EXCUSE = "I lost. My confidence was 99%. My accuracy was the remaining 1%."


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE.strip(), "excuse must be a single line"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
