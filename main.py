#!/usr/bin/env python3
"""make.fun entry - "Sum up 23 November's world news in one image".

Writes the bundled front-page image to /output/entry.png, byte for byte,
so repeated runs always produce identical output. No network access.
"""
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
