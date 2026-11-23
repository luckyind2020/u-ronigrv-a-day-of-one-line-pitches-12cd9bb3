#!/usr/bin/env python3
"""Print the one-sentence pitch for the A Day of One-Line Pitches bounty."""

from pathlib import Path


def load_pitch() -> str:
    here = Path(__file__).resolve().parent
    pitch = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if not pitch:
        raise SystemExit("entry.txt is empty — nothing to pitch.")
    return pitch


def main() -> None:
    print(load_pitch())


if __name__ == "__main__":
    main()
