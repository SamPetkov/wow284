#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_or_verify(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="\n")
    elif new not in text:
        raise AssertionError(f"neither old nor new marker occurs in {path}")


def main() -> None:
    replace_or_verify(
        ROOT / "scripts" / "audit_v22_manuscript.py",
        "Representative axiom reports contain only",
        "The public endpoint axiom reports contain only",
    )
    print("final arXiv validator alignment: PASS")


if __name__ == "__main__":
    main()
