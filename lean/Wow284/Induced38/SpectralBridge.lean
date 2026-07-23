import Wow284.Induced38.FiniteCertificates
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
