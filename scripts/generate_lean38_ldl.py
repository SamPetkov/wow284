#!/usr/bin/env python3
"""Generate a denominator-cleared padded LDL^T certificate for order 38.

The 38x38 certificate is padded by a 2x2 identity block.  This lets the Lean
proof reuse the existing 5x5 sharding strategy on `Fin 40`.  Columns of the
rational LDL lower factor are scaled independently to an integer matrix `B`.
The resulting exact identity `B W B^T = s M` and a scaled integer left inverse
avoid asking Lean to normalize large rational matrix products.
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


def spectral_bridge() -> str:
    """Render the Lean-4.31-compatible spectral endpoint wrapper.

    The finite and LDL identities above are generated separately, but this
    bridge is also deterministic generated source: keeping it here makes the
    exact algebraic certificate and its positive-definiteness transfer fresh
    together.  Its cast and transpose proofs deliberately follow the shared
    order-39/42 bridge, whose API choices target Mathlib on Lean 4.31.
    """
    return '''import Wow284.Induced38.FiniteCertificates
import Wow284.Induced38.LDLData
import Mathlib.Analysis.Matrix.PosDef

/-! Exact positive-definiteness bridge for the order-38 graph. -/
namespace Wow284.Induced38
open Matrix

def Dq : Matrix Vertex Vertex ℚ := D.map (Int.castRingHom ℚ)
theorem Dq_eq_cast_Dcert : Dq = castMatrix38 Dcert := by
  rw [Dq, semantic_distance_eq_Dcert]
  rfl
theorem M38q_eq_shifted_distance :
    M38q = (3 : ℚ) • Dq + (17 : ℚ) • (1 : Matrix Vertex Vertex ℚ) := by
  rw [M38q, M38Int_eq_shiftedCert, shiftedCert, Dq, semantic_distance_eq_Dcert]
  ext i j
  change (((3 * Dcert i j + 17 * (if i = j then 1 else 0) : ℤ) : ℚ)) =
    (3 : ℚ) * ((Dcert i j : ℤ) : ℚ) +
      (17 : ℚ) * (if i = j then 1 else 0)
  by_cases h : i = j <;> simp [h, Int.cast_add, Int.cast_mul]

theorem deltaPad_posDef : DeltaPad.PosDef := Matrix.PosDef.diagonal pivotPad_positive
theorem lpad_isUnit : IsUnit Lpad := Matrix.isUnit_of_left_inverse lpad_left_inverse
theorem Mpad_posDef : Mpad.PosDef := by
  rw [← ldl_identity]
  rw [← Matrix.conjTranspose_eq_transpose_of_trivial]
  exact
    deltaPad_posDef.mul_mul_conjTranspose_same (Matrix.vecMul_injective_of_isUnit lpad_isUnit)
theorem M38q_posDef : M38q.PosDef := by
  rw [← Mpad_submatrix]; exact Mpad_posDef.submatrix embedPad_injective
theorem shifted_distance_posDef :
    ((3 : ℚ) • Dq + (17 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef := by
  rw [← M38q_eq_shifted_distance]; exact M38q_posDef

noncomputable def Dr : Matrix Vertex Vertex ℝ := D.map (Int.castRingHom ℝ)
private noncomputable def LpadR : Matrix PadVertex PadVertex ℝ := Lpad.map (Rat.castHom ℝ)
private noncomputable def DeltaPadR : Matrix PadVertex PadVertex ℝ := DeltaPad.map (Rat.castHom ℝ)
private noncomputable def MpadR : Matrix PadVertex PadVertex ℝ := Mpad.map (Rat.castHom ℝ)
private noncomputable def M38r : Matrix Vertex Vertex ℝ := M38q.map (Rat.castHom ℝ)
private noncomputable def LpadInvR : Matrix PadVertex PadVertex ℝ := LpadInv.map (Rat.castHom ℝ)
private theorem deltaPadR_eq : DeltaPadR = diagonal (fun i => (pivotPad i : ℝ)) := by
  ext i j
  change ((if i = j then pivotPad i else 0 : ℚ) : ℝ) =
    if i = j then (pivotPad i : ℝ) else 0
  by_cases h : i = j <;> simp [h]
private theorem pivotPadR_positive (i : PadVertex) : 0 < (pivotPad i : ℝ) := by
  exact_mod_cast pivotPad_positive i
private theorem deltaPadR_posDef : DeltaPadR.PosDef := by
  rw [deltaPadR_eq]; exact Matrix.PosDef.diagonal pivotPadR_positive
private theorem lpadR_left_inverse : LpadInvR * LpadR = (1 : Matrix PadVertex PadVertex ℝ) := by
  rw [LpadInvR, LpadR, ← Matrix.map_mul, lpad_left_inverse]; simp
private theorem lpadR_isUnit : IsUnit LpadR := Matrix.isUnit_of_left_inverse lpadR_left_inverse
private theorem ldl_identity_real : LpadR * DeltaPadR * LpadR.transpose = MpadR := by
  rw [LpadR, DeltaPadR, MpadR, ← Matrix.map_mul]
  change (Lpad * DeltaPad).map (Rat.castHom ℝ) *
    (Lpad.transpose.map (Rat.castHom ℝ)) = Mpad.map (Rat.castHom ℝ)
  rw [← Matrix.map_mul]
  exact congrArg (fun M : Matrix PadVertex PadVertex ℚ =>
    Matrix.map M (Rat.castHom ℝ)) ldl_identity
private theorem MpadR_posDef : MpadR.PosDef := by
  rw [← ldl_identity_real]
  rw [← Matrix.conjTranspose_eq_transpose_of_trivial]
  exact
    deltaPadR_posDef.mul_mul_conjTranspose_same (Matrix.vecMul_injective_of_isUnit lpadR_isUnit)
private theorem MpadR_submatrix : MpadR.submatrix embedPad embedPad = M38r := by
  ext i j
  change ((Mpad (embedPad i) (embedPad j) : ℚ) : ℝ) =
    ((M38q i j : ℚ) : ℝ)
  have h := congrArg (fun M : Matrix Vertex Vertex ℚ => M i j) Mpad_submatrix
  exact_mod_cast h
private theorem M38r_posDef : M38r.PosDef := by
  rw [← MpadR_submatrix]; exact MpadR_posDef.submatrix embedPad_injective
private theorem M38r_eq_shifted_distance :
    M38r = (3 : ℝ) • Dr + (17 : ℝ) • (1 : Matrix Vertex Vertex ℝ) := by
  rw [M38r, Dr, M38q_eq_shifted_distance]
  ext i j
  by_cases h : i = j <;> simp [Dq, h]
theorem shifted_distance_real_posDef :
    ((3 : ℝ) • Dr + (17 : ℝ) • (1 : Matrix Vertex Vertex ℝ)).PosDef := by
  rw [← M38r_eq_shifted_distance]; exact M38r_posDef

theorem real_eigenpair_above_neg_seventeen_thirds {mu : ℝ} {x : Vertex → ℝ}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : (-17 : ℝ) / 3 < mu := by
  have hpos := shifted_distance_real_posDef.dotProduct_mulVec_pos hx
  rw [add_mulVec, smul_mulVec, smul_mulVec, one_mulVec, heig] at hpos
  simp only [star_trivial, dotProduct_add, dotProduct_smul, smul_eq_mul] at hpos
  have hnorm : 0 < dotProduct x x := by
    have hnonneg : 0 ≤ dotProduct x x :=
      Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
    have hne : dotProduct x x ≠ 0 := (dotProduct_self_eq_zero).not.mpr hx
    exact lt_of_le_of_ne hnonneg hne.symm
  have hprod : 0 < ((3 : ℝ) * mu + 17) * dotProduct x x := by
    nlinarith [hpos]
  have hcoeff : 0 < (3 : ℝ) * mu + 17 := by
    rcases (mul_pos_iff.mp hprod) with h | h
    · exact h.1
    · exact False.elim ((not_lt_of_ge hnorm.le) h.2)
  nlinarith
end Wow284.Induced38
'''


def lean_int_matrix(name: str, matrix: sp.Matrix, typ: str) -> str:
    rows: list[str] = []
    for i in range(matrix.rows):
        entries: list[str] = []
        for j in range(matrix.cols):
            value = sp.Rational(matrix[i, j])
            if value.q != 1:
                raise AssertionError(f"{name}[{i},{j}] is not integral")
            entries.append(str(int(value)))
        rows.append(", ".join(entries))
    return f"def {name} : Matrix {typ} {typ} ℤ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def common_denominator(matrix: sp.Matrix) -> int:
    denominators = [int(sp.denom(x)) for x in matrix]
    return int(sp.ilcm(*denominators)) if denominators else 1


def shard(name: str, lhs: str, rhs: str, r: int) -> str:
    lines: list[str] = []
    for s in range(8):
        lines += [
            "set_option maxRecDepth 20000 in",
            f"lemma {name}_rows_{r}_{s} : ∀ c d : Fin 5,",
            f"    ({lhs}) (coordPad {r} c) (coordPad {s} d) =",
            f"      ({rhs}) (coordPad {r} c) (coordPad {s} d) := by",
            "  intro c d",
            "  fin_cases c <;> fin_cases d <;> decide",
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

    column_scales = [
        common_denominator(lower[:, j]) for j in range(lower.cols)
    ]
    b38 = lower * sp.diag(*column_scales)
    if any(sp.denom(x) != 1 for x in b38):
        raise AssertionError("column-scaled lower factor is not integral")
    coefficient38 = [
        sp.factor(delta[j, j] / (column_scales[j] ** 2))
        for j in range(delta.rows)
    ]
    ldl_scale = int(sp.ilcm(*[int(sp.denom(x)) for x in coefficient38]))
    weight38 = [sp.factor(ldl_scale * x) for x in coefficient38]
    if any(sp.denom(x) != 1 or x <= 0 for x in weight38):
        raise AssertionError("scaled LDL weights are not positive integers")

    mpad_int = pad38(m38)
    bpad_int = pad38(b38)
    weight_entries = weight38 + [sp.Integer(ldl_scale), sp.Integer(ldl_scale)]
    wpad_int = sp.diag(*weight_entries)
    inverse = bpad_int.inv()
    inverse_scale = common_denominator(inverse)
    inverse_numerator = inverse_scale * inverse
    scaled_identity = inverse_scale * sp.eye(40)

    if any(sp.denom(x) != 1 for x in inverse_numerator):
        raise AssertionError("scaled inverse is not integral")
    if bpad_int * wpad_int * bpad_int.T != ldl_scale * mpad_int:
        raise AssertionError("denominator-cleared padded LDL reconstruction failed")
    if inverse_numerator * bpad_int != scaled_identity:
        raise AssertionError("scaled padded left inverse failed")

    definitions = f'''import Wow284.Induced38.CertificateDefinitions
import Mathlib.LinearAlgebra.Matrix.PosDef

/-!
Generated denominator-cleared data for the positive-definiteness certificate
`3 D + 17 I`. The last two coordinates form an auxiliary identity block.
All computational matrix identities below are checked over the integers.
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

def M38Int : Matrix Vertex Vertex ℤ := shiftedCert
{lean_int_matrix("MpadInt", mpad_int, "PadVertex")}
{lean_int_matrix("BpadInt", bpad_int, "PadVertex")}
{lean_int_matrix("BpadInvNumerator", inverse_numerator, "PadVertex")}

def weightPadInt : PadVertex → ℤ := ![
  {", ".join(str(int(x)) for x in weight_entries)}
]
def WpadInt : Matrix PadVertex PadVertex ℤ := diagonal weightPadInt
def scaledIdentityInt : Matrix PadVertex PadVertex ℤ :=
  ({inverse_scale} : ℤ) • (1 : Matrix PadVertex PadVertex ℤ)

def castMatrix38 (M : Matrix Vertex Vertex ℤ) : Matrix Vertex Vertex ℚ :=
  M.map (Int.castRingHom ℚ)
def castPadMatrix (M : Matrix PadVertex PadVertex ℤ) : Matrix PadVertex PadVertex ℚ :=
  M.map (Int.castRingHom ℚ)

lemma castPadMatrix_mul (M N : Matrix PadVertex PadVertex ℤ) :
    castPadMatrix (M * N) = castPadMatrix M * castPadMatrix N := Matrix.map_mul
lemma castPadMatrix_transpose (M : Matrix PadVertex PadVertex ℤ) :
    castPadMatrix M.transpose = (castPadMatrix M).transpose := rfl
lemma castPadMatrix_smul (a : ℤ) (M : Matrix PadVertex PadVertex ℤ) :
    castPadMatrix (a • M) = (a : ℚ) • castPadMatrix M := by
  ext i j
  change (((a * M i j : ℤ) : ℚ)) =
    (a : ℚ) * ((M i j : ℤ) : ℚ)
  rw [Int.cast_mul]
lemma castPadMatrix_one :
    castPadMatrix (1 : Matrix PadVertex PadVertex ℤ) =
      (1 : Matrix PadVertex PadVertex ℚ) := by
  ext i j
  by_cases h : i = j
  · subst j
    simp [castPadMatrix]
  · simp [castPadMatrix, h]

def M38q : Matrix Vertex Vertex ℚ := castMatrix38 M38Int
def Mpad : Matrix PadVertex PadVertex ℚ := castPadMatrix MpadInt
def Lpad : Matrix PadVertex PadVertex ℚ := castPadMatrix BpadInt
def LpadInv : Matrix PadVertex PadVertex ℚ :=
  ((1 : ℚ) / {inverse_scale}) • castPadMatrix BpadInvNumerator

def pivotPad (i : PadVertex) : ℚ :=
  ((1 : ℚ) / {ldl_scale}) * (weightPadInt i : ℚ)
def DeltaPad : Matrix PadVertex PadVertex ℚ := diagonal pivotPad

lemma deltaPad_eq_scaled_cast :
    DeltaPad = ((1 : ℚ) / {ldl_scale}) • castPadMatrix WpadInt := by
  ext i j
  by_cases h : i = j
  · subst j
    simp [DeltaPad, pivotPad, WpadInt, castPadMatrix, diagonal]
  · simp [DeltaPad, pivotPad, WpadInt, castPadMatrix, diagonal, h]

end Wow284.Induced38
'''

    outputs: dict[Path, str] = {
        LEAN_DIR / "LDLDefinitions.lean": definitions,
        LEAN_DIR / "SpectralBridge.lean": spectral_bridge(),
    }
    identities = [
        (
            "Identity",
            "ldl_identity_scaled",
            "BpadInt * WpadInt * BpadInt.transpose",
            f"({ldl_scale} : ℤ) • MpadInt",
        ),
        (
            "Left",
            "lpad_left_inverse_scaled",
            "BpadInvNumerator * BpadInt",
            "scaledIdentityInt",
        ),
    ]
    for kind, name, lhs, rhs in identities:
        for r in range(8):
            outputs[LEAN_DIR / f"LDL{kind}{r}.lean"] = f'''import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 integer certificate shard. -/
namespace Wow284.Induced38

{shard(name, lhs, rhs, r)}
end Wow284.Induced38
'''
        imports = "\n".join(f"import Wow284.Induced38.LDL{kind}{r}" for r in range(8))
        if kind == "Identity":
            body = f'''{imports}

namespace Wow284.Induced38

{assembly(name, lhs, rhs)}
theorem ldl_identity :
    Lpad * DeltaPad * Lpad.transpose = Mpad := by
  rw [deltaPad_eq_scaled_cast, Matrix.mul_smul, Matrix.smul_mul]
  change ((1 : ℚ) / {ldl_scale}) •
      (castPadMatrix BpadInt * castPadMatrix WpadInt *
        (castPadMatrix BpadInt).transpose) =
    castPadMatrix MpadInt
  rw [← castPadMatrix_transpose, ← castPadMatrix_mul, ← castPadMatrix_mul,
    ldl_identity_scaled]
  rw [castPadMatrix_smul, smul_smul, one_div]
  change ((((({ldl_scale} : ℤ) : ℚ)⁻¹ * (({ldl_scale} : ℤ) : ℚ)) •
      castPadMatrix MpadInt) = castPadMatrix MpadInt)
  have hscaleZ : ({ldl_scale} : ℤ) ≠ 0 := by positivity
  have hscaleQ : (({ldl_scale} : ℤ) : ℚ) ≠ 0 := by
    exact_mod_cast hscaleZ
  rw [inv_mul_cancel₀ hscaleQ, one_smul]

end Wow284.Induced38
'''
        else:
            body = f'''{imports}

namespace Wow284.Induced38

{assembly(name, lhs, rhs)}
theorem lpad_left_inverse :
    LpadInv * Lpad = (1 : Matrix PadVertex PadVertex ℚ) := by
  change (((1 : ℚ) / {inverse_scale}) •
      castPadMatrix BpadInvNumerator) * castPadMatrix BpadInt = 1
  rw [Matrix.smul_mul, ← castPadMatrix_mul, lpad_left_inverse_scaled]
  rw [scaledIdentityInt, castPadMatrix_smul, castPadMatrix_one,
    smul_smul, one_div]
  change ((((({inverse_scale} : ℤ) : ℚ)⁻¹ * (({inverse_scale} : ℤ) : ℚ)) •
      (1 : Matrix PadVertex PadVertex ℚ)) =
    (1 : Matrix PadVertex PadVertex ℚ))
  have hscaleZ : ({inverse_scale} : ℤ) ≠ 0 := by positivity
  have hscaleQ : (({inverse_scale} : ℤ) : ℚ) ≠ 0 := by
    exact_mod_cast hscaleZ
  rw [inv_mul_cancel₀ hscaleQ, one_smul]

theorem lpad_right_inverse :
    Lpad * LpadInv = (1 : Matrix PadVertex PadVertex ℚ) :=
  mul_eq_one_comm.mp lpad_left_inverse

end Wow284.Induced38
'''
        outputs[LEAN_DIR / f"LDL{kind}.lean"] = body

    outputs[LEAN_DIR / "LDLData.lean"] = '''import Wow284.Induced38.LDLIdentity
import Wow284.Induced38.LDLLeft

namespace Wow284.Induced38

open Matrix

/-- All forty denominator-cleared padded weights are strictly positive. -/
theorem weightPadInt_positive : ∀ i : PadVertex, 0 < weightPadInt i := by
  intro i
  fin_cases i <;> decide

/-- All forty rational padded pivots are strictly positive. -/
theorem pivotPad_positive (i : PadVertex) : 0 < pivotPad i := by
  have hw : (0 : ℚ) < weightPadInt i := by exact_mod_cast weightPadInt_positive i
  simp only [pivotPad]
  positivity

/-- The first 38 coordinates of the padded matrix are exactly `M38q`. -/
def embedPad (v : Vertex) : PadVertex := ⟨v.val, by omega⟩

lemma embedPad_injective : Function.Injective embedPad := by
  intro u v h
  apply Fin.ext
  simpa [embedPad] using congrArg Fin.val h

lemma Mpad_submatrix : Mpad.submatrix embedPad embedPad = M38q := by
  ext i j
  decide +revert

lemma M38Int_eq_shiftedCert : M38Int = shiftedCert := by
  rfl

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
