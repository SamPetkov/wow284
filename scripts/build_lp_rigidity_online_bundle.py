#!/usr/bin/env python3
"""Build the complete dependency-ordered source bundle for hosted LP checks."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
OUTPUT = LEAN / "tmp" / "LPFullOnlineBundle.lean"
MODULES = [
    LEAN / "Wow284" / "LPDefinitions.lean",
    LEAN / "Wow284" / "LPRecurrence.lean",
    LEAN / "Wow284" / "LPPrimal.lean",
    LEAN / "Wow284" / "LPDualFinite.lean",
    LEAN / "Wow284" / "LPChebyshevTail.lean",
    LEAN / "Wow284" / "LPWeakDuality.lean",
    LEAN / "Wow284" / "LPRigidity.lean",
    LEAN / "Wow284" / "LPCeiling.lean",
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
    pieces.append(
        "-- AXIOM AUDIT\n"
        "#print axioms Wow284.LP.extremalCoefficients_admissible\n"
        "#print axioms Wow284.LP.extremalCoefficients_attains\n"
        "#print axioms Wow284.LP.twoSidedLP_equality_iff\n"
        "#print axioms Wow284.LP.twoSidedLP_coefficient_equality_iff\n"
        "#print axioms Wow284.LP.twoSidedLP_positive_ray_equality_iff\n"
        "#print axioms Wow284.LP.twoSidedLP_optimal_and_rigid\n"
        "#print axioms "
        "Wow284.LP.twoSidedLP_exact_optimum_and_coefficient_rigidity\n"
        "#print axioms Wow284.LP.polynomial_eq_extremal_of_objective_eq\n"
        "#print axioms Wow284.LP.high_coeff_eq_zero_of_slack_sum_eq\n"
        "#print axioms Wow284.LP.eq_leadingCoeff_mul_rootQuartic"
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n\n".join(pieces) + "\n", encoding="utf-8", newline="\n")
    print(OUTPUT)


if __name__ == "__main__":
    main()
