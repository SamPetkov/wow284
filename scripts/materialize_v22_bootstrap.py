#!/usr/bin/env python3
"""Compatibility check for the retired v2.2 bootstrap materializer.

The canonical manuscript is now tracked directly.  This entry point remains
for older workflow references, but it is deliberately read-only: it verifies
that the root, arXiv, and ``v22`` mirrors are synchronized.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "sync_manuscript_artifacts.py"),
            "--check",
        ],
        cwd=ROOT,
        check=True,
    )
    print("legacy v2.2 bootstrap retired; synchronized mirror check: PASS")


if __name__ == "__main__":
    main()
