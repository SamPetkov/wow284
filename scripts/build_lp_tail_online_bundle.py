#!/usr/bin/env python3
"""Build the dependency-ordered source bundle for hosted LP-tail checks."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
OUTPUT = LEAN / "tmp" / "LPTailOnlineBundle.lean"
MODULES = [
    LEAN / "Wow284" / "LPDefinitions.lean",
    LEAN / "Wow284" / "LPRecurrence.lean",
    LEAN / "Wow284" / "LPPrimal.lean",
    LEAN / "Wow284" / "LPDualFinite.lean",
    LEAN / "Wow284" / "LPChebyshevTail.lean",
]


def strip_local_imports(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.startswith("import Wow284.")
    )


def main() -> None:
    pieces: list[str] = []
    for index, path in enumerate(MODULES):
        text = path.read_text(encoding="utf-8")
        if index:
            text = strip_local_imports(text)
        pieces.append(f"-- BEGIN {path.relative_to(ROOT).as_posix()}\n{text.rstrip()}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n\n".join(pieces) + "\n", encoding="utf-8", newline="\n")
    print(OUTPUT)


if __name__ == "__main__":
    main()
