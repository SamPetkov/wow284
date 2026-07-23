#!/usr/bin/env python3
"""Cross-platform runner for the extended WOW-284 certificates."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run(script: str, *arguments: str) -> None:
    command = [sys.executable, str(ROOT / "scripts" / script), *arguments]
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-exploratory",
        action="store_true",
        help="also run the labelled floating-point three-vertex screen",
    )
    args = parser.parse_args()

    run("verify_wow284_38_40_42.py")
    run("verify_38_graph6_independent.py")
    run("verify_descendant_families.py")
    run("export_graphs.py", "--check")
    if args.include_exploratory:
        run("explore_generalizations.py")
    print("EXTENDED WOW-284 VERIFICATION: PASS")


if __name__ == "__main__":
    main()
