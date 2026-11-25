"""The Excuse That Almost Works entry.

Writes one original line, the excuse a gamer texts the boss to skip work
on GTA 6 launch week, to /output/entry.txt: UTF-8 text, 1 to 140
characters, at most 20 words, no trailing newline so the file holds the
line and nothing else.
"""

import os

LINE = "Boss, the building's fire alarm test locked me in the stairwell with no signal, and facilities says it'll be hours."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts characters and words, so refuse to ship a line over
    # either cap: 1-140 characters, at most 20 words.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert len(LINE.split()) <= 20, "line must be at most 20 words"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
