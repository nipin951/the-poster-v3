"""The Poster for a Place That Isn't There.

The poster itself is drawn by build_entry.py (Faroluna, the island the moon
visits first); this program hands the finished PNG to /output/entry.png.
"""

import os
import shutil


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
