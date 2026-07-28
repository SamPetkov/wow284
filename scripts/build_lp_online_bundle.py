#!/usr/bin/env python3
"""Build a self-contained Lean source bundle for hosted AXLE checks.

AXLE checks one source document at a time and does not receive this repository's
local module graph.  The source modules are already valid when concatenated in
dependency order because each opens and closes its own namespace.  This script
removes only local ``import Wow284...`` lines from later modules and leaves all
other source bytes and declarations in order.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
OUTPUT = LEAN / "tmp" / "LPOnlineBundle.lean"
MODULES = [
    LEAN / "Wow284" / "LPDefinitions.lean",
    LEAN / "Wow284" / "LPRecurrence.lean",
    LEAN / "Wow284" / "LPPrimal.lean",
    LEAN / "Wow284" / "LPDualFinite.lean",
]

AUDIT_COMMANDS = """
-- Representative transitive trust-surface checks for the finite dual certificate.
#print axioms Wow284.LP.weightMinus_pos
#print axioms Wow284.LP.dual_mass_eq_ceiling_sub_one
#print axioms Wow284.LP.dual_nbPoly_eq_neg_eval_of_one_le_of_le_four
#print axioms Wow284.LP.slack_pos_of_five_le_of_le_nine
""".strip()


def strip_local_imports(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.startswith("import Wow284.")
    )


def main() -> None:
    missing = [str(path) for path in MODULES if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"missing Lean module(s): {missing}")

    pieces: list[str] = []
    for index, path in enumerate(MODULES):
        text = path.read_text(encoding="utf-8")
        if index:
            text = strip_local_imports(text)
        pieces.append(f"-- BEGIN {path.relative_to(ROOT).as_posix()}\n{text.rstrip()}")

    pieces.append(AUDIT_COMMANDS)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n\n".join(pieces) + "\n", encoding="utf-8", newline="\n")
    print(OUTPUT)


if __name__ == "__main__":
    main()
