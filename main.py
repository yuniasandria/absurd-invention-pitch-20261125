#!/usr/bin/env python3
"""One-sentence absurd invention pitch: headphones that police fake listening."""
import os

PART_A = "Headphones that pause your music on the third 'uh-huh' of a call "
PART_B = "you aren't listening to, and resume only after you repeat the last sentence verbatim."

LINE = PART_A + PART_B

def main():
    assert 1 <= len(LINE) <= 220, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
