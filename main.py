#!/usr/bin/env python3
"""make.fun entry: "Sum up 23 November's world news in one image".

The entry image is the newspaper front page bundled beside this file
as ``entry.png`` (1024 x 1024 PNG, under 1 MiB). This program copies
that image, byte for byte, to the output location so that repeated
runs always produce identical bytes. It uses only the Python 3.13
standard library and needs no network access.

Output location: ``/output/entry.png`` in the grader's container.
For a local dry run, set ``MAKEFUN_OUTPUT_DIR`` to another folder
and the image is written there instead.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def source_image() -> Path:
    """Return the path of the bundled front-page image."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def output_image() -> Path:
    """Return where the entry image must be written."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / IMAGE_NAME


def main() -> None:
    src = source_image()
    if not src.is_file():
        raise FileNotFoundError(f"bundled image not found: {src}")
    dest = output_image()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    # Guard against a truncated copy: the judge sees exactly the bytes
    # written, so the output must be the same size as the bundled image.
    if dest.stat().st_size != src.stat().st_size:
        raise IOError(f"copy size mismatch: {src} -> {dest}")


if __name__ == "__main__":
    main()
