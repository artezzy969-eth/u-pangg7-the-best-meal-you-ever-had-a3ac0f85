#!/usr/bin/env python3
"""Write one sentence about the best meal ever had to entry.txt.

Deterministic: the same sentence, the same bytes, every run.
Standard library only. One sentence, 1-200 characters, no trailing newline.
"""

import os

SENTENCE = (
    "At five in the morning outside the airport, I ate bubur ayam from a "
    "cart with no sign, its yellow broth steaming against my chin, and I "
    "waved goodbye to my brother with the spoon still in my hand."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
