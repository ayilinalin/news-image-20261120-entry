#!/usr/bin/env python3
"""news-image-20261120 entry point.

Copies the front-page image baked into this repository
(``entry.png``: a newspaper front page summing up the world news of
Friday 20 November 2026) to ``$MAKEFUN_OUTPUT_DIR/entry.png``.

Python 3.13, standard library only, no network, no randomness, no
timestamps anywhere in the output: two runs write byte-identical
output. The image itself is a fixed file in this repository, so the
program is deterministic by construction.
"""

import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576  # 1 MiB cap from the competition rules.
MAX_DIMENSION = 1024  # 1024x1024 cap from the competition rules.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2

    data = src.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(
            f"error: entry.png is {len(data)} bytes, over the "
            f"{MAX_BYTES}-byte cap",
            file=sys.stderr,
        )
        return 1
    # PNG layout: 8-byte magic, then the IHDR chunk (4-byte length,
    # 4-byte type "IHDR", 4-byte width, 4-byte height, big-endian).
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"error: entry.png is {width}x{height}, over the "
            f"{MAX_DIMENSION}x{MAX_DIMENSION} cap",
            file=sys.stderr,
        )
        return 1

    out_path = Path(out_dir) / "entry.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    os.chmod(out_path, 0o644)
    print(f"wrote {out_path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
