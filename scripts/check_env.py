#!/usr/bin/env python3
"""Check the local prerequisites for the podcast clip workflow."""

from __future__ import annotations

import importlib.util
import shutil
import sys


def main() -> int:
    ok = True
    print(f"Python: {sys.version.split()[0]}")
    if sys.version_info < (3, 11):
        print("  Python 3.11 or newer is recommended.")
        ok = False
    for command in ("ffmpeg", "ffprobe"):
        path = shutil.which(command)
        print(f"{command}: {path or 'MISSING'}")
        ok &= path is not None
    available = importlib.util.find_spec("faster_whisper") is not None
    print(f"faster-whisper: {'installed' if available else 'MISSING'}")
    ok &= available
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
