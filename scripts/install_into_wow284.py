#!/usr/bin/env python3
"""Install the extension into a local checkout of SamPetkov/wow284.

The script copies source and generator files but does not commit, push, or
claim that Lean compilation has succeeded.  Non-imported `.lean.template`
files are copied for reference and are not added to `Wow284.lean`.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil

EXTENSION = Path(__file__).resolve().parents[1]
IMPORTS = [
    "import Wow284.Induced40.Structural",
    "import Wow284.Induced40.DiagonalizationData",
    "import Wow284.Induced40.Gap",
    "import Wow284.Induced38.FiniteCertificates",
    "import Wow284.Induced38.LDLData",
    "import Wow284.Induced38.Gap",
    "import Wow284.DiameterThreeScalar",
    "import Wow284.MooreSecondThreshold",
    "import Wow284.PuncturedMooreThreshold",
]


def copy_file(source: Path, target: Path, force: bool) -> None:
    if target.exists() and target.read_bytes() != source.read_bytes() and not force:
        raise SystemExit(f"refusing to overwrite modified file: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path, help="path to local wow284 checkout")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    lean_root = repo / "lean"
    if not (lean_root / "Wow284" / "Basic.lean").exists():
        raise SystemExit("not a compatible wow284 checkout: lean/Wow284/Basic.lean missing")

    source_root = EXTENSION / "lean" / "Wow284"
    for source in source_root.rglob("*"):
        if source.is_file() and (source.suffix == ".lean" or source.name.endswith(".lean.template")):
            copy_file(source, lean_root / "Wow284" / source.relative_to(source_root), args.force)
    copy_file(EXTENSION / "lean" / "Wow284Extended.lean", lean_root / "Wow284Extended.lean", args.force)

    for source in (EXTENSION / "scripts").glob("*.py"):
        copy_file(source, repo / "scripts" / source.name, args.force)

    root_module = lean_root / "Wow284.lean"
    text = root_module.read_text(encoding="utf-8")
    missing = [line for line in IMPORTS if line not in text]
    if missing:
        root_module.write_text(text.rstrip() + "\n" + "\n".join(missing) + "\n", encoding="utf-8")

    print("extension installed")
    print("run the Python generator checks from the repository root")
    print("then: cd lean && lake env lean Wow284Extended.lean")


if __name__ == "__main__":
    main()
