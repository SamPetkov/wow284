#!/usr/bin/env python3
"""Read-only compatibility entry point for the retired third revision pass.

The manuscript is now maintained in ``main.tex`` and mirrored by
``sync_manuscript_artifacts.py``.  Retaining a mutating historical rewrite
would risk reintroducing superseded language, so this legacy command now
performs the two fail-closed checks relevant to the final source.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(script: str, *args: str) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), *args],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    run("audit_v22_manuscript.py")
    run("sync_manuscript_artifacts.py", "--check")
    print("retired third-pass compatibility audit: PASS")


if __name__ == "__main__":
    main()
