#!/usr/bin/env python3
"""Generate padded exact rational LDL^T data for the 38-vertex graph.

The 38x38 certificate is padded by a 2x2 identity block.  This lets the Lean
proof reuse the existing 5x5 sharding strategy on `Fin 40`; positive
definiteness of the original matrix is then obtained by a principal submatrix.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import distance_matrix, graph38  # noqa: E402

LEAN_DIR = ROOT / "lean" / "Wow284" / "Induced38"


def lean_rat(value: sp.Expr) -> str:
    value = sp.Rational(value)
    if value.q == 1:
        return str(int(value.p))
    return f"(({int(value.p)} : ℚ) / {int(value.q)})"


def lean_rat_matrix(name: str, matrix: sp.Matrix) -> str:
    rows = [", ".join(lean_rat(matrix[i, j]) for j in range(matrix.cols)) for i in range(matrix.rows)]
    return f"def {name} : Matrix PadVertex PadVertex ℚ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def lean_rat_matrix38(name: str, matrix: sp.Matrix) -> str:
    rows = [", ".join(lean_rat(matrix[i, j]) for j in range(matrix.cols)) for i in range(matrix.rows)]
    return f"def {name} : Matrix Vertex Vertex ℚ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def shard(name: str, lhs: str, rhs: str, r: int) -> str:
    lines: list[str] = []
    for s in range(8):
        lines += [
            "set_option maxRecDepth 20000 in",
            f"lemma {name}_rows_{r}_{s} : ∀ c d : Fin 5,",
            f"    ({lhs}) (coordPad {r} c) (coordPad {s} d) =",
            f"      ({rhs}) (coordPad {r} c) (coordPad {s} d) := by",
            "  decide",
            "",
        ]
    lines += [
        f"lemma {name}_row_{r} (s : Fin 8) (c d : Fin 5) :",
        f"    ({lhs}) (coordPad {r} c) (coordPad s d) =",
        f"      ({rhs}) (coordPad {r} c) (coordPad s d) := by",
        "  fin_cases s",
    ]
    lines += [f"  · exact {name}_rows_{r}_{s} c d" for s in range(8)]
    lines.append("")
    return "\n".join(lines)


def assembly(name: str, lhs: str, rhs: str) -> str:
    lines = [
        f"private lemma {name}_coord (r s : Fin 8) (c d : Fin 5) :",
        f"    ({lhs}) (coordPad r c) (coordPad s d) =",
        f"      ({rhs}) (coordPad r c) (coordPad s d) := by",
        "  fin_cases r",
    ]
    lines += [f"  · exact {name}_row_{r} s c d" for r in range(8)]
    lines += [
        "",
        f"theorem {name} : {lhs} = {rhs} := by",
        "  ext i j",
        "  rw [← coordPad_surj i, ← coordPad_surj j]",
        f"  exact {name}_coord _ _ _ _",
        "",
    ]
    return "\n".join(lines)


def pad38(matrix: sp.Matrix, last_diag: int = 1) -> sp.Matrix:
    result = sp.zeros(40)
    result[:38, :38] = matrix
    result[38, 38] = last_diag
    result[39, 39] = last_diag
    return result


def render() -> dict[Path, str]:
    graph, _ = graph38()
    d = distance_matrix(graph)
    m38 = 3 * d + 17 * sp.eye(38)
    lower, delta = m38.LDLdecomposition(hermitian=True)
    if lower * delta * lower.T != m38:
        raise AssertionError("LDL reconstruction failed")
    pivots38 = [sp.factor(delta[i, i]) for i in range(38)]
    if not all(bool(p > 0) for p in pivots38):
        raise AssertionError("nonpositive pivot")
    lower_inv = lower.inv()

    mpad = pad38(m38)
    lpad = pad38(lower)
    dpad = pad38(delta)
    invpad = pad38(lower_inv)
    if lpad * dpad * lpad.T != mpad:
        raise AssertionError("padded LDL reconstruction failed")
    if invpad * lpad != sp.eye(40) or lpad * invpad != sp.eye(40):
        raise AssertionError("padded inverse failed")

    pivot_entries = pivots38 + [sp.Integer(1), sp.Integer(1)]
    pivot_vector = ", ".join(lean_rat(p) for p in pivot_entries)

    definitions = f'''import Wow284.Induced38.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef

/-!
Generated exact rational data for the positive-definiteness certificate
`3 D + 17 I`.  The last two coordinates form an auxiliary identity block.
-/

namespace Wow284.Induced38

open Matrix

abbrev PadVertex := Fin 40

def coordPad (r : Fin 8) (c : Fin 5) : PadVertex :=
  ⟨5 * r.val + c.val, by omega⟩

lemma coordPad_surj (v : PadVertex) :
    coordPad ⟨v.val / 5, by omega⟩ ⟨v.val % 5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext
  simp [coordPad]
  omega

{lean_rat_matrix38("M38q", m38)}
{lean_rat_matrix("Mpad", mpad)}
{lean_rat_matrix("Lpad", lpad)}
{lean_rat_matrix("LpadInv", invpad)}

def pivotPad : PadVertex → ℚ := ![{pivot_vector}]
def DeltaPad : Matrix PadVertex PadVertex ℚ := diagonal pivotPad

end Wow284.Induced38
'''

    outputs: dict[Path, str] = {LEAN_DIR / "LDLDefinitions.lean": definitions}
    identities = [
        ("Identity", "ldl_identity", "Lpad * DeltaPad * Lpad.transpose", "Mpad"),
        ("Left", "lpad_left_inverse", "LpadInv * Lpad", "(1 : Matrix PadVertex PadVertex ℚ)"),
        ("Right", "lpad_right_inverse", "Lpad * LpadInv", "(1 : Matrix PadVertex PadVertex ℚ)"),
    ]
    for kind, name, lhs, rhs in identities:
        for r in range(8):
            outputs[LEAN_DIR / f"LDL{kind}{r}.lean"] = f'''import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 rational certificate shard. -/
namespace Wow284.Induced38

{shard(name, lhs, rhs, r)}
end Wow284.Induced38
'''
        imports = "\n".join(f"import Wow284.Induced38.LDL{kind}{r}" for r in range(8))
        outputs[LEAN_DIR / f"LDL{kind}.lean"] = f'''{imports}

namespace Wow284.Induced38

{assembly(name, lhs, rhs)}
end Wow284.Induced38
'''

    outputs[LEAN_DIR / "LDLData.lean"] = '''import Wow284.Induced38.LDLIdentity
import Wow284.Induced38.LDLLeft
import Wow284.Induced38.LDLRight

namespace Wow284.Induced38

open Matrix

/-- All forty padded pivots are strictly positive. -/
theorem pivotPad_positive : ∀ i : PadVertex, 0 < pivotPad i := by
  decide

/-- The first 38 coordinates of the padded matrix are exactly `M38q`. -/
def embedPad (v : Vertex) : PadVertex := ⟨v.val, by omega⟩

lemma embedPad_injective : Function.Injective embedPad := by
  intro u v h
  apply Fin.ext
  simpa [embedPad] using congrArg Fin.val h

lemma Mpad_submatrix : Mpad.submatrix embedPad embedPad = M38q := by
  ext i j
  decide

end Wow284.Induced38
'''

    outputs[LEAN_DIR / "LDLPositiveDefinite.lean.template"] = '''import Wow284.Induced38.LDLData

/-!
NON-IMPORTED SKELETON.

The large exact identities are complete generated targets.  The remaining
wrapper should use Mathlib's positive-definite congruence and submatrix API:

1. `pivotPad_positive` implies `DeltaPad.PosDef`;
2. `lpad_left_inverse` and `lpad_right_inverse` make `Lpad` invertible;
3. `ldl_identity` gives positive definiteness of `Mpad` by congruence;
4. `Mpad_submatrix` and `embedPad_injective` transfer it to `M38q`;
5. the semantic-distance equality then proves `3D+17I` positive definite.
-/

namespace Wow284.Induced38

-- theorem shifted_positive_definite : M38q.PosDef := by
--   ...

end Wow284.Induced38
'''
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = render()
    if args.check:
        stale = [p for p, c in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != c]
        if stale:
            raise SystemExit("stale files: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        print(f"38-vertex Lean LDL data: PASS ({len(outputs)} files)")
        return
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
