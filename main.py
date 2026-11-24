"""The Vacuum's Alibi: one line, 200 characters max.

A robot vacuum explains why it missed a spot. Writes the line to
/output/entry.txt (created if missing). Python stdlib only, deterministic.
"""

import os

LINE = (
    "I did not miss the spot. I scanned it, named it Gerald, and my "
    "warranty forbids eating anything with a name."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
