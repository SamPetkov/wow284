import Wow284.Induced42.FiniteCertificates
import Wow284.Induced42.LDLData
import Mathlib.Analysis.Matrix.PosDef

/-! Exact positive-definiteness bridge for the order-42 graph. -/
namespace Wow284.Induced42
open Matrix
def Dq : Matrix Vertex Vertex ℚ := D.map (Int.castRingHom ℚ)
theorem Mcore_eq_shifted_distance :
    Mcore = (1 : ℚ) • Dq + (6 : ℚ) • (1 : Matrix Vertex Vertex ℚ) := by
  rw [Mcore, Dq, semantic_distance_eq_Dcert]
  ext i j
  change (((1 * Dcert i j + 6 * (if i = j then 1 else 0) : ℤ) : ℚ)) =
    (1 : ℚ) * ((Dcert i j : ℤ) : ℚ) +
      (6 : ℚ) * (if i = j then 1 else 0)
  by_cases h : i = j <;> simp [h, Int.cast_add]

theorem deltaPad_posDef : DeltaPad.PosDef := Matrix.PosDef.diagonal pivotPad_positive
theorem lpad_isUnit : IsUnit Lpad :=
  IsUnit.of_mul_eq_one_right LpadInv lpad_left_inverse
theorem Mpad_posDef : Mpad.PosDef := by
  rw [← ldl_identity]
  rw [← Matrix.conjTranspose_eq_transpose_of_trivial]
  exact
    deltaPad_posDef.mul_mul_conjTranspose_same (Matrix.vecMul_injective_of_isUnit lpad_isUnit)
theorem Mcore_posDef : Mcore.PosDef := by
  rw [← Mpad_submatrix]; exact Mpad_posDef.submatrix embedPad_injective
theorem shifted_distance_posDef :
    ((1 : ℚ) • Dq + (6 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef := by
  rw [← Mcore_eq_shifted_distance]; exact Mcore_posDef

noncomputable def Dr : Matrix Vertex Vertex ℝ := D.map (Int.castRingHom ℝ)
private noncomputable def LpadR : Matrix PadVertex PadVertex ℝ := Lpad.map (Rat.castHom ℝ)
private noncomputable def DeltaPadR : Matrix PadVertex PadVertex ℝ := DeltaPad.map (Rat.castHom ℝ)
private noncomputable def MpadR : Matrix PadVertex PadVertex ℝ := Mpad.map (Rat.castHom ℝ)
private noncomputable def McoreR : Matrix Vertex Vertex ℝ := Mcore.map (Rat.castHom ℝ)
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
private theorem lpadR_isUnit : IsUnit LpadR :=
  IsUnit.of_mul_eq_one_right LpadInvR lpadR_left_inverse
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
private theorem MpadR_submatrix : MpadR.submatrix embedPad embedPad = McoreR := by
  ext i j
  change ((Mpad (embedPad i) (embedPad j) : ℚ) : ℝ) =
    ((Mcore i j : ℚ) : ℝ)
  have h := congrArg (fun M : Matrix Vertex Vertex ℚ => M i j) Mpad_submatrix
  exact_mod_cast h
private theorem McoreR_posDef : McoreR.PosDef := by
  rw [← MpadR_submatrix]; exact MpadR_posDef.submatrix embedPad_injective
private theorem McoreR_eq_shifted_distance :
    McoreR = (1 : ℝ) • Dr + (6 : ℝ) • (1 : Matrix Vertex Vertex ℝ) := by
  rw [McoreR, Dr, Mcore_eq_shifted_distance]
  ext i j
  by_cases h : i = j <;> simp [Dq, h]
theorem shifted_distance_real_posDef :
    ((1 : ℝ) • Dr + (6 : ℝ) • (1 : Matrix Vertex Vertex ℝ)).PosDef := by
  rw [← McoreR_eq_shifted_distance]; exact McoreR_posDef

theorem real_eigenpair_above_shift {mu : ℝ} {x : Vertex → ℝ}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : (-6 : ℝ) / 1 < mu := by
  have hpos := shifted_distance_real_posDef.dotProduct_mulVec_pos hx
  rw [add_mulVec, smul_mulVec, smul_mulVec, one_mulVec, heig] at hpos
  simp only [star_trivial, dotProduct_add, dotProduct_smul, smul_eq_mul] at hpos
  have hnorm : 0 < dotProduct x x := by
    have hnonneg : 0 ≤ dotProduct x x :=
      Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
    have hne : dotProduct x x ≠ 0 := (dotProduct_self_eq_zero).not.mpr hx
    exact lt_of_le_of_ne hnonneg hne.symm
  have hprod : 0 < ((1 : ℝ) * mu + 6) * dotProduct x x := by
    nlinarith [hpos]
  have hcoeff : 0 < (1 : ℝ) * mu + 6 := by
    rcases (mul_pos_iff.mp hprod) with h | h
    · exact h.1
    · exact False.elim ((not_lt_of_ge hnorm.le) h.2)
  nlinarith
end Wow284.Induced42
