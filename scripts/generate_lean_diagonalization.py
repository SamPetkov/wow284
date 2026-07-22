#!/usr/bin/env python3
"""Generate the exact Lean diagonalization data for the WOW-284 graph."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from wow284_graph import adjacency_matrix, adjacency_list, all_pairs_distances  # noqa: E402

LEAN_DIR = ROOT / "lean" / "Wow284"
TARGET = LEAN_DIR / "DiagonalizationData.lean"


def lean_rat(value: sp.Rational) -> str:
    value = sp.Rational(value)
    numerator = int(value.p)
    denominator = int(value.q)
    if denominator == 1:
        return str(numerator)
    return f"(({numerator} : ℚ) / {denominator})"


def lean_matrix(name: str, matrix: sp.Matrix) -> str:
    rows = []
    for i in range(matrix.rows):
        rows.append(", ".join(lean_rat(matrix[i, j]) for j in range(matrix.cols)))
    body = ";\n    ".join(rows)
    return f"def {name} : Matrix Vertex Vertex ℚ := !![\n    {body}\n  ]\n"


def lean_int_matrix(name: str, matrix: sp.Matrix) -> str:
    rows = []
    for i in range(matrix.rows):
        entries = []
        for j in range(matrix.cols):
            value = sp.Rational(matrix[i, j])
            if value.q != 1:
                raise AssertionError(f"{name} has a non-integral entry")
            entries.append(str(int(value)))
        rows.append(", ".join(entries))
    body = ";\n    ".join(rows)
    return f"def {name} : Matrix Vertex Vertex ℤ := !![\n    {body}\n  ]\n"


def lean_certificate_shard(name: str, lhs: str, rhs: str, r: int) -> str:
    """Render the ten 5x5 checks for one coordinate row."""
    lines: list[str] = []
    for s in range(10):
        lines.extend(
            [
                "set_option maxRecDepth 10000 in",
                f"lemma {name}_rows_{r}_{s} : ∀ c d : Fin 5,",
                f"    ({lhs}) (coordVertex {r} c) (coordVertex {s} d) =",
                f"      ({rhs}) (coordVertex {r} c) (coordVertex {s} d) := by",
                "  decide",
                "",
            ]
        )
    lines.extend(
        [
            f"lemma {name}_row_{r} (s : Fin 10) (c d : Fin 5) :",
            f"    ({lhs}) (coordVertex {r} c) (coordVertex s d) =",
            f"      ({rhs}) (coordVertex {r} c) (coordVertex s d) := by",
            "  fin_cases s",
        ]
    )
    for s in range(10):
        lines.append(f"  · exact {name}_rows_{r}_{s} c d")
    lines.append("")
    return "\n".join(lines)


def lean_certificate_assembly(name: str, lhs: str, rhs: str) -> str:
    """Reassemble 100 imported 5x5 checks into a matrix equality.

    The rational identities are first cleared of denominators.  Integer
    reduction is much cheaper, but the full 2,500-entry check still exceeds
    the strict checker's memory budget.  The generated checks are sharded so
    each Lean process retains at most ten computational proof terms.
    """
    lines = [
        f"private lemma {name}_coord (r s : Fin 10) (c d : Fin 5) :",
        f"    ({lhs}) (coordVertex r c) (coordVertex s d) =",
        f"      ({rhs}) (coordVertex r c) (coordVertex s d) := by",
        "  fin_cases r",
    ]
    for r in range(10):
        lines.append(f"  · exact {name}_row_{r} s c d")

    lines.extend(
        [
            "",
            f"theorem {name} :",
            f"    {lhs} = {rhs} := by",
            "  ext i j",
            "  rw [← coordVertex_surj i, ← coordVertex_surj j]",
            f"  exact {name}_coord _ _ _ _",
            "",
        ]
    )
    return "\n".join(lines)


def render() -> dict[Path, str]:
    graph = adjacency_list()
    adjacency = sp.Matrix(adjacency_matrix(graph))
    distance = sp.Matrix(all_pairs_distances(graph))
    identity = sp.eye(50)
    ones_matrix = sp.ones(50)

    # Twenty-eight columns spanning the adjacency-2 / distance-(-4) space.
    projector_minus_four_scaled = 15 * identity + 5 * adjacency - ones_matrix
    minus_four_space = (
        DomainMatrix.from_Matrix(projector_minus_four_scaled)
        .to_field()
        .columnspace()
        .to_Matrix()
    )

    # Twenty-one columns spanning the adjacency-(-3) / distance-1 space.
    projector_one_scaled = 20 * identity - 10 * adjacency + ones_matrix
    one_space = (
        DomainMatrix.from_Matrix(projector_one_scaled)
        .to_field()
        .columnspace()
        .to_Matrix()
    )

    if minus_four_space.cols != 28 or one_space.cols != 21:
        raise AssertionError("unexpected eigenspace dimensions")

    constant = sp.ones(50, 1)
    basis = sp.Matrix.hstack(constant, minus_four_space, one_space)
    # DomainMatrix arithmetic is dramatically faster and more predictable here
    # than generic dense Gaussian elimination.
    inverse = DomainMatrix.from_Matrix(basis).to_field().inv().to_Matrix()
    inverse_numerator = 250 * inverse
    diagonal = sp.diag(91, *([-4] * 28), *([1] * 21))

    if inverse * basis != identity or basis * inverse != identity:
        raise AssertionError("basis inverse check failed")
    if distance * basis != basis * diagonal:
        raise AssertionError("distance diagonalization check failed")
    if any(value.q != 1 for value in inverse_numerator):
        raise AssertionError("inverse denominator does not divide 250")

    left_name = "eigenbasis_left_inverse_scaled"
    left_lhs = "eigenbasisInvNumerator * eigenbasisInt"
    left_rhs = "scaledIdentityInt"
    diagonal_name = "distance_diagonalization_int"
    diagonal_lhs = "D * eigenbasisInt"
    diagonal_rhs = "eigenbasisInt * distanceDiagonalInt"

    definitions = f'''import Wow284.Basic

/-!
This file is generated by `scripts/generate_lean_diagonalization.py`.
It contains the exact integer data underlying the rational diagonalization.
-/

namespace Wow284

open Matrix

{lean_int_matrix("eigenbasisInt", basis)}
{lean_int_matrix("eigenbasisInvNumerator", inverse_numerator)}
def castMatrix (M : Matrix Vertex Vertex ℤ) : Matrix Vertex Vertex ℚ :=
  M.map (Int.castRingHom ℚ)

lemma castMatrix_mul (M N : Matrix Vertex Vertex ℤ) :
    castMatrix (M * N) = castMatrix M * castMatrix N := by
  exact Matrix.map_mul

def eigenbasis : Matrix Vertex Vertex ℚ := castMatrix eigenbasisInt

def eigenbasisInv : Matrix Vertex Vertex ℚ :=
  ((1 : ℚ) / 250) • castMatrix eigenbasisInvNumerator

def scaledIdentityInt : Matrix Vertex Vertex ℤ :=
  fun i j => if i = j then 250 else 0

def distanceDiagonalEntryInt (j : Vertex) : ℤ :=
  if j.val = 0 then 91 else if j.val < 29 then -4 else 1

def distanceDiagonalInt : Matrix Vertex Vertex ℤ :=
  diagonal distanceDiagonalEntryInt

def distanceDiagonalEntry (j : Vertex) : ℚ := distanceDiagonalEntryInt j

def distanceDiagonal : Matrix Vertex Vertex ℚ := castMatrix distanceDiagonalInt

def Dq : Matrix Vertex Vertex ℚ := castMatrix D

end Wow284
'''

    outputs: dict[Path, str] = {
        LEAN_DIR / "DiagonalizationDefinitions.lean": definitions,
    }
    for kind, name, lhs, rhs in (
        ("Left", left_name, left_lhs, left_rhs),
        ("Distance", diagonal_name, diagonal_lhs, diagonal_rhs),
    ):
        for r in range(10):
            module = f"Diagonalization{kind}{r}"
            outputs[LEAN_DIR / f"{module}.lean"] = f'''import Wow284.DiagonalizationDefinitions

/-! Generated bounded certificate shard; do not edit by hand. -/

namespace Wow284

{lean_certificate_shard(name, lhs, rhs, r)}
end Wow284
'''

    left_imports = chr(10).join(f"import Wow284.DiagonalizationLeft{r}" for r in range(10))
    outputs[LEAN_DIR / "DiagonalizationLeft.lean"] = f'''{left_imports}

/-!
Generated assembly of the bounded left-inverse certificate.
-/

namespace Wow284

open Matrix

{lean_certificate_assembly(left_name, left_lhs, left_rhs)}

theorem eigenbasis_left_inverse :
    eigenbasisInv * eigenbasis = (1 : Matrix Vertex Vertex ℚ) := by
  change (((1 : ℚ) / 250) • castMatrix eigenbasisInvNumerator) *
    castMatrix eigenbasisInt = 1
  rw [Matrix.smul_mul, ← castMatrix_mul, eigenbasis_left_inverse_scaled]
  ext i j
  by_cases h : i = j
  · subst j
    simp [castMatrix, scaledIdentityInt]
  · simp [castMatrix, scaledIdentityInt, h]

theorem eigenbasis_right_inverse :
    eigenbasis * eigenbasisInv = (1 : Matrix Vertex Vertex ℚ) := by
  exact mul_eq_one_comm.mp eigenbasis_left_inverse

end Wow284
'''

    distance_imports = chr(10).join(f"import Wow284.DiagonalizationDistance{r}" for r in range(10))
    outputs[LEAN_DIR / "DiagonalizationDistance.lean"] = f'''{distance_imports}

/-!
Generated assembly of the bounded distance-diagonalization certificate.
-/

namespace Wow284

open Matrix

{lean_certificate_assembly(diagonal_name, diagonal_lhs, diagonal_rhs)}

theorem distance_diagonalization :
    Dq * eigenbasis = eigenbasis * distanceDiagonal := by
  change castMatrix D * castMatrix eigenbasisInt =
    castMatrix eigenbasisInt * castMatrix distanceDiagonalInt
  simpa only [← castMatrix_mul] using congrArg castMatrix distance_diagonalization_int

end Wow284
'''

    assembler = '''import Wow284.DiagonalizationLeft
import Wow284.DiagonalizationDistance

/-!
This file is generated by `scripts/generate_lean_diagonalization.py`.
It exposes the exact rational diagonalization used by the WOW-284
formalization and checks its eigenvalue multiplicities.
-/

namespace Wow284

theorem distance_diagonal_counts :
    (Finset.univ.filter fun j : Vertex => distanceDiagonalEntry j = -4).card = 28 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalEntry j = 1).card = 21 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalEntry j = 91).card = 1 := by
  decide

end Wow284
'''
    outputs[TARGET] = assembler
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without writing")
    args = parser.parse_args()
    outputs = render()
    if args.check:
        stale = [
            path.relative_to(ROOT)
            for path, content in outputs.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        if stale:
            raise SystemExit("stale generated Lean files: " + ", ".join(map(str, stale)))
        print(f"Lean diagonalization data check: PASS ({len(outputs)} files)")
        return
    LEAN_DIR.mkdir(parents=True, exist_ok=True)
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
