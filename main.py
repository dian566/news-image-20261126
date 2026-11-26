#!/usr/bin/env python3
"""Write the 26 November 2026 front page to the grader's output folder.

The picture itself lives in this repository as news.png: a newspaper front
page that sums up Thursday 26 November 2026 in six stories, drawn earlier
with a small script from the day's reported news. This program does exactly
one thing: it copies that file to entry.png in the output folder, so the
bytes the judge sees are the bytes in this repository. It touches no
network, keeps no state, and writes the same bytes on every run.
"""

import os
import shutil
import struct
import sys
import zlib

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def check_png(path):
    """Read the source image and confirm it is a PNG within the gate limits.

    Returns (width, height, size_bytes) or raises ValueError with the reason.
    """
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise ValueError("image is %d bytes, over the 1 MiB cap" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise ValueError("image is %dx%d, over the 1024x1024 cap"
                         % (width, height))
    # Walk every chunk and verify its CRC, so a truncated or corrupted
    # file is caught here instead of failing the gate's whole-image check.
    pos = 8
    saw_iend = False
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            raise ValueError("truncated %s chunk" % ctype.decode("ascii", "replace"))
        stored = struct.unpack(">I", data[pos + 8 + length:end])[0]
        actual = zlib.crc32(ctype + data[pos + 8:pos + 8 + length]) & 0xFFFFFFFF
        if stored != actual:
            raise ValueError("bad CRC in %s chunk" % ctype.decode("ascii", "replace"))
        if ctype == b"IEND":
            saw_iend = True
            if end != len(data):
                raise ValueError("trailing bytes after IEND")
            break
        pos = end
    if not saw_iend:
        raise ValueError("missing IEND chunk")
    return width, height, len(data)


def main():
    if not os.path.isfile(SOURCE):
        print("missing source image: " + SOURCE, file=sys.stderr)
        return 1
    try:
        width, height, size = check_png(SOURCE)
    except (OSError, ValueError) as exc:
        print("invalid source image: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # Confirm the copy is byte-identical to the source, so both grader runs
    # see exactly the bytes in this repository.
    with open(target, "rb") as fh:
        copied = fh.read()
    with open(SOURCE, "rb") as fh:
        original = fh.read()
    if copied != original:
        print("copy mismatch: entry.png differs from news.png", file=sys.stderr)
        return 1
    print("wrote %s (%dx%d, %d bytes)" % (target, width, height, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
