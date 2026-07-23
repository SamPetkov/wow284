#!/usr/bin/env python3
"""Render padded denominator-cleared integer LDL certificates."""
from __future__ import annotations

import sympy as sp

from lean3942_common import Spec, distance_matrix, lean_int_matrix


def pad_identity(matrix: sp.Matrix, order: int) -> sp.Matrix:
    """Pad a square matrix by an identity block."""
    result = sp.eye(order)
    result[: matrix.rows, : matrix.cols] = matrix
    return result


def pad_diagonal(entries: list[sp.Integer], order: int, extra: sp.Integer) -> list[sp.Integer]:
    return entries + [extra] * (order - len(entries))


def lcm_denominators(values) -> sp.Integer:
    denominators = [int(sp.denom(value)) for value in values]
    return sp.Integer(sp.ilcm(*denominators)) if denominators else sp.Integer(1)


def integer_shard(name: str, lhs: str, rhs: str, row: int, rows: int) -> str:
    """Emit bounded 5x5 checks for one padded coordinate row."""
    lines: list[str] = []
    for column_row in range(rows):
        lines += [
            "set_option maxRecDepth 25000 in",
            f"lemma {name}_rows_{row}_{column_row} : ∀ c d : Fin 5,",
            f"    ({lhs}) (coordPad {row} c) (coordPad {column_row} d) =",
            f"      ({rhs}) (coordPad {row} c) (coordPad {column_row} d) := by",
            "  intro c d",
            "  fin_cases c <;> fin_cases d <;> decide",
            "",
        ]
    lines += [
        f"lemma {name}_row_{row} (s : Fin {rows}) (c d : Fin 5) :",
        f"    ({lhs}) (coordPad {row} c) (coordPad s d) =",
        f"      ({rhs}) (coordPad {row} c) (coordPad s d) := by",
        "  fin_cases s",
    ]
    lines += [f"  · exact {name}_rows_{row}_{s} c d" for s in range(rows)]
    return "\n".join(lines) + "\n"


def assembly(name: str, lhs: str, rhs: str, rows: int) -> str:
    return (
        f"""private lemma {name}_coord (r s : Fin {rows}) (c d : Fin 5) :
    ({lhs}) (coordPad r c) (coordPad s d) = ({rhs}) (coordPad r c) (coordPad s d) := by
  fin_cases r
"""
        + "\n".join(f"  · exact {name}_row_{r} s c d" for r in range(rows))
        + f"""
theorem {name} : {lhs} = {rhs} := by
  ext i j
  rw [← coordPad_surj i, ← coordPad_surj j]
  exact {name}_coord _ _ _ _
"""
    )


def ldl_outputs(spec: Spec) -> dict[str, str]:
    ns = spec.namespace
    distance = distance_matrix(spec.graph)
    core = spec.shift_scale * distance + spec.shift_diag * sp.eye(spec.order)
    lower, delta = core.LDLdecomposition(hermitian=True)
    assert lower * delta * lower.T == core

    # Scale each column separately.  This keeps B small even when the common
    # denominator of all entries of L is enormous (629 digits for order 39).
    column_scales = [
        lcm_denominators(lower[i, j] for i in range(spec.order))
        for j in range(spec.order)
    ]
    b_core = lower * sp.diag(*column_scales)
    if any(sp.denom(value) != 1 for value in b_core):
        raise AssertionError("column-scaled LDL factor is not integral")

    rational_weights = [
        sp.Rational(delta[j, j]) / (column_scales[j] ** 2)
        for j in range(spec.order)
    ]
    identity_scale = lcm_denominators(rational_weights)
    weights_core = [sp.Integer(identity_scale * value) for value in rational_weights]
    if not all(value > 0 for value in weights_core):
        raise AssertionError("nonpositive denominator-cleared LDL weight")

    w_core = sp.diag(*weights_core)
    if b_core * w_core * b_core.T != identity_scale * core:
        raise AssertionError("denominator-cleared LDL identity failed")

    b_inverse = b_core.inv()
    inverse_scale = lcm_denominators(b_inverse)
    b_inverse_numerator_core = b_inverse * inverse_scale
    if any(sp.denom(value) != 1 for value in b_inverse_numerator_core):
        raise AssertionError("scaled inverse is not integral")
    if b_inverse_numerator_core * b_core != inverse_scale * sp.eye(spec.order):
        raise AssertionError("denominator-cleared left inverse failed")

    m_pad_int = pad_identity(core, spec.pad_order)
    b_pad_int = pad_identity(b_core, spec.pad_order)
    b_inverse_numerator_pad_int = sp.zeros(spec.pad_order)
    b_inverse_numerator_pad_int[: spec.order, : spec.order] = b_inverse_numerator_core
    for i in range(spec.order, spec.pad_order):
        b_inverse_numerator_pad_int[i, i] = inverse_scale

    weights_pad = pad_diagonal(weights_core, spec.pad_order, identity_scale)
    w_pad_int = sp.diag(*weights_pad)
    m_scaled_pad_int = identity_scale * m_pad_int
    scaled_identity_int = inverse_scale * sp.eye(spec.pad_order)

    assert b_pad_int * w_pad_int * b_pad_int.T == m_scaled_pad_int
    assert b_inverse_numerator_pad_int * b_pad_int == scaled_identity_int

    weight_vector = ", ".join(str(int(value)) for value in weights_pad)
    definitions = f"""import Wow284.{ns}.CertificateDefinitions
import Mathlib.Analysis.Matrix.PosDef

/-!
Generated exact denominator-cleared integer data for
`{spec.shift_scale}D+{spec.shift_diag}I`.  If `s = {identity_scale}`, the core
certificate is `B W Bᵀ = s M`; padding is an identity block.  Rational
factorization is recovered algebraically after the integer shards compile.
-/
namespace Wow284.{ns}
open Matrix

abbrev PadVertex := Fin {spec.pad_order}

def coordPad (r : Fin {spec.pad_rows}) (c : Fin 5) : PadVertex :=
  ⟨5 * r.val + c.val, by omega⟩

lemma coordPad_surj (v : PadVertex) :
    coordPad ⟨v.val / 5, by omega⟩
      ⟨v.val % 5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext
  simp [coordPad]
  omega

def McoreInt : Matrix Vertex Vertex ℤ :=
  ({spec.shift_scale} : ℤ) • Dcert +
    ({spec.shift_diag} : ℤ) • (1 : Matrix Vertex Vertex ℤ)
def MpadInt : Matrix PadVertex PadVertex ℤ := fun i j =>
  if hi : i.val < {spec.order} then
    if hj : j.val < {spec.order} then
      McoreInt ⟨i.val, hi⟩ ⟨j.val, hj⟩
    else 0
  else if i = j then 1 else 0
{lean_int_matrix("BpadInt", b_pad_int, "PadVertex")}
{lean_int_matrix("BpadInvNumeratorInt", b_inverse_numerator_pad_int, "PadVertex")}
def wPadInt : PadVertex → ℤ := ![{weight_vector}]
def WpadInt : Matrix PadVertex PadVertex ℤ := diagonal wPadInt
def MscaledPadInt : Matrix PadVertex PadVertex ℤ :=
  ({identity_scale} : ℤ) • MpadInt
def scaledIdentityInt : Matrix PadVertex PadVertex ℤ :=
  ({inverse_scale} : ℤ) • (1 : Matrix PadVertex PadVertex ℤ)

def castPadMatrix (M : Matrix PadVertex PadVertex ℤ) :
    Matrix PadVertex PadVertex ℚ := M.map (Int.castRingHom ℚ)
def castCoreMatrix (M : Matrix Vertex Vertex ℤ) :
    Matrix Vertex Vertex ℚ := M.map (Int.castRingHom ℚ)

lemma castPadMatrix_mul (M N : Matrix PadVertex PadVertex ℤ) :
    castPadMatrix (M * N) = castPadMatrix M * castPadMatrix N := by
  exact Matrix.map_mul

lemma castPadMatrix_transpose (M : Matrix PadVertex PadVertex ℤ) :
    castPadMatrix M.transpose = (castPadMatrix M).transpose := by
  rfl

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

def Mcore : Matrix Vertex Vertex ℚ := castCoreMatrix McoreInt
def Mpad : Matrix PadVertex PadVertex ℚ := castPadMatrix MpadInt
def Lpad : Matrix PadVertex PadVertex ℚ := castPadMatrix BpadInt
def LpadInv : Matrix PadVertex PadVertex ℚ :=
  ((1 : ℚ) / {inverse_scale}) • castPadMatrix BpadInvNumeratorInt
def pivotPad (i : PadVertex) : ℚ :=
  ((1 : ℚ) / {identity_scale}) * (wPadInt i : ℚ)
def DeltaPad : Matrix PadVertex PadVertex ℚ := diagonal pivotPad

lemma DeltaPad_eq_scaled_cast :
    DeltaPad = ((1 : ℚ) / {identity_scale}) • castPadMatrix WpadInt := by
  ext i j
  simp [DeltaPad, pivotPad, castPadMatrix, WpadInt, diagonal]

end Wow284.{ns}
"""

    out: dict[str, str] = {
        f"lean/Wow284/{ns}/LDLDefinitions.lean": definitions
    }
    identities = [
        (
            "Identity",
            "ldl_scaled_identity_int",
            "BpadInt * WpadInt * BpadInt.transpose",
            "MscaledPadInt",
        ),
        (
            "Left",
            "lpad_left_inverse_scaled_int",
            "BpadInvNumeratorInt * BpadInt",
            "scaledIdentityInt",
        ),
    ]
    for kind, name, lhs, rhs in identities:
        for row in range(spec.pad_rows):
            out[f"lean/Wow284/{ns}/LDL{kind}{row}.lean"] = f"""import Wow284.{ns}.LDLDefinitions
/-! Generated bounded denominator-cleared integer shard {row + 1}/{spec.pad_rows}. -/
namespace Wow284.{ns}
{integer_shard(name, lhs, rhs, row, spec.pad_rows)}
end Wow284.{ns}
"""
        imports = "\n".join(
            f"import Wow284.{ns}.LDL{kind}{row}" for row in range(spec.pad_rows)
        )
        out[f"lean/Wow284/{ns}/LDL{kind}.lean"] = f"""{imports}
namespace Wow284.{ns}
{assembly(name, lhs, rhs, spec.pad_rows)}
end Wow284.{ns}
"""

    out[f"lean/Wow284/{ns}/LDLData.lean"] = f"""import Wow284.{ns}.LDLIdentity
import Wow284.{ns}.LDLLeft

namespace Wow284.{ns}
open Matrix

theorem ldl_identity : Lpad * DeltaPad * Lpad.transpose = Mpad := by
  rw [DeltaPad_eq_scaled_cast, Matrix.mul_smul, Matrix.smul_mul]
  change ((1 : ℚ) / {identity_scale}) •
      (castPadMatrix BpadInt * castPadMatrix WpadInt *
        (castPadMatrix BpadInt).transpose) =
    castPadMatrix MpadInt
  rw [← castPadMatrix_transpose, ← castPadMatrix_mul, ← castPadMatrix_mul,
    ldl_scaled_identity_int]
  rw [MscaledPadInt, castPadMatrix_smul, smul_smul, one_div]
  change ((((({identity_scale} : ℤ) : ℚ)⁻¹ *
      (({identity_scale} : ℤ) : ℚ)) • castPadMatrix MpadInt) =
    castPadMatrix MpadInt)
  have hscaleZ : ({identity_scale} : ℤ) ≠ 0 := by positivity
  have hscaleQ : (({identity_scale} : ℤ) : ℚ) ≠ 0 := by
    exact_mod_cast hscaleZ
  rw [inv_mul_cancel₀ hscaleQ, one_smul]

theorem lpad_left_inverse : LpadInv * Lpad =
    (1 : Matrix PadVertex PadVertex ℚ) := by
  change (((1 : ℚ) / {inverse_scale}) •
      castPadMatrix BpadInvNumeratorInt) * castPadMatrix BpadInt = 1
  rw [Matrix.smul_mul, ← castPadMatrix_mul, lpad_left_inverse_scaled_int]
  rw [scaledIdentityInt, castPadMatrix_smul, castPadMatrix_one,
    smul_smul, one_div]
  change ((((({inverse_scale} : ℤ) : ℚ)⁻¹ *
      (({inverse_scale} : ℤ) : ℚ)) •
      (1 : Matrix PadVertex PadVertex ℚ)) =
    (1 : Matrix PadVertex PadVertex ℚ))
  have hscaleZ : ({inverse_scale} : ℤ) ≠ 0 := by positivity
  have hscaleQ : (({inverse_scale} : ℤ) : ℚ) ≠ 0 := by
    exact_mod_cast hscaleZ
  rw [inv_mul_cancel₀ hscaleQ, one_smul]

private theorem wPadInt_positive : ∀ i : PadVertex, 0 < wPadInt i := by decide

theorem pivotPad_positive : ∀ i : PadVertex, 0 < pivotPad i := by
  intro i
  have hweight : (0 : ℚ) < (wPadInt i : ℚ) := by
    exact_mod_cast wPadInt_positive i
  unfold pivotPad
  positivity

def embedPad (v : Vertex) : PadVertex := ⟨v.val, by omega⟩

lemma embedPad_injective : Function.Injective embedPad := by
  intro u v h
  apply Fin.ext
  simpa [embedPad] using congrArg Fin.val h

private lemma MpadInt_submatrix :
    MpadInt.submatrix embedPad embedPad = McoreInt := by
  ext i j
  simp [MpadInt, embedPad]

lemma Mpad_submatrix : Mpad.submatrix embedPad embedPad = Mcore := by
  ext i j
  change ((MpadInt (embedPad i) (embedPad j) : ℤ) : ℚ) =
    ((McoreInt i j : ℤ) : ℚ)
  have h := congrArg (fun M : Matrix Vertex Vertex ℤ => M i j)
    MpadInt_submatrix
  exact_mod_cast h

end Wow284.{ns}
"""
    return out
