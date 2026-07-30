#!/usr/bin/env python3
"""Copy missing Paperforge template assets without overwriting WOW-284 files.

``paperforge init --force`` deliberately skips an existing top-level directory.
Because this instance commits its hand-authored ``web-assets/site`` directory,
the helper fills the remaining template assets after initialization.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def copy_missing(source: Path, target: Path) -> int:
    copied = 0
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        destination = target / relative
        if path.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        if destination.exists():
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        copied += 1
    return copied


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paperforge_tool", type=Path)
    parser.add_argument(
        "--instance",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    args = parser.parse_args()

    template = args.paperforge_tool.resolve() / "pretext-template"
    instance = args.instance.resolve()
    if not template.is_dir():
        raise FileNotFoundError(f"Paperforge template not found: {template}")

    copied = 0
    for name in ("source", "xsl", "publication", "content", "web-assets"):
        source = template / name
        if source.is_dir():
            copied += copy_missing(source, instance / name)
    project = template / "project.ptx"
    target_project = instance / "project.ptx"
    if project.is_file() and not target_project.exists():
        shutil.copy2(project, target_project)
        copied += 1

    print(f"Paperforge scaffold hydration: {copied} missing files copied")


if __name__ == "__main__":
    main()
