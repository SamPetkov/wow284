import Wow284.Induced38.FiniteCertificates
import Wow284.Induced38.LDLData
import Mathlib.Analysis.Matrix.PosDef

/-!
# Semantic and spectral endpoint for the 38-vertex construction

This file turns the generated exact LDL certificate into a positive-definiteness
theorem for the semantic shifted distance matrix.  It then records the resulting
strict lower bound for every real eigenpair of the distance matrix.
-/

namespace Wow284.Induced38

open Matrix

/-- The semantic distance matrix, regarded over the rationals. -/
def Dq : Matrix Vertex Vertex ℚ := D.map (Int.castRingHom ℚ)

/-- The semantic distance cast agrees with the generated integer certificate. -/
lemma Dq_eq_cast_Dcert : Dq = castMatrix38 Dcert := by
  rw [Dq, semantic_distance_eq_Dcert]
  rfl

/-- The generated rational matrix is exactly `3 D + 17 I`. -/
theorem M38q_eq_shifted_distance :
    M38q = (3 : ℚ) • Dq + (17 : ℚ) • (1 : Matrix Vertex Vertex ℚ) := by
  rw [M38q, M38Int_eq_shiftedCert, shiftedCert, Dq_eq_cast_Dcert]
  ext i j
  simp [castMatrix38]

theorem deltaPad_posDef : DeltaPad.PosDef :=
  Matrix.PosDef.diagonal pivotPad_positive

theorem lpad_isUnit : IsUnit Lpad :=
  Matrix.isUnit_of_left_inverse lpad_left_inverse

theorem Mpad_posDef : Mpad.PosDef := by
  rw [← ldl_identity]
  simpa only [conjTranspose_eq_transpose] using
    deltaPad_posDef.mul_mul_conjTranspose_same
      (Matrix.vecMul_injective_of_isUnit lpad_isUnit)

theorem M38q_posDef : M38q.PosDef := by
  rw [← Mpad_submatrix]
  exact Mpad_posDef.submatrix embedPad_injective

theorem shifted_distance_posDef :
    ((3 : ℚ) • Dq + (17 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef := by
  rw [← M38q_eq_shifted_distance]
  exact M38q_posDef

/-- The semantic distance matrix, regarded over the reals. -/
def Dr : Matrix Vertex Vertex ℝ := D.map (Int.castRingHom ℝ)

private def LpadR : Matrix PadVertex PadVertex ℝ := Lpad.map (Rat.castHom ℝ)
private def DeltaPadR : Matrix PadVertex PadVertex ℝ := DeltaPad.map (Rat.castHom ℝ)
private def MpadR : Matrix PadVertex PadVertex ℝ := Mpad.map (Rat.castHom ℝ)
private def M38r : Matrix Vertex Vertex ℝ := M38q.map (Rat.castHom ℝ)
private def LpadInvR : Matrix PadVertex PadVertex ℝ := LpadInv.map (Rat.castHom ℝ)

private theorem deltaPadR_eq :
    DeltaPadR = diagonal (fun i => (pivotPad i : ℝ)) := by
  ext i j
  simp [DeltaPadR, DeltaPad, diagonal]

private theorem pivotPadR_positive (i : PadVertex) : 0 < (pivotPad i : ℝ) := by
  exact_mod_cast pivotPad_positive i

private theorem deltaPadR_posDef : DeltaPadR.PosDef := by
  rw [deltaPadR_eq]
  exact Matrix.PosDef.diagonal pivotPadR_positive

private theorem lpadR_left_inverse :
    LpadInvR * LpadR = (1 : Matrix PadVertex PadVertex ℝ) := by
  rw [LpadInvR, LpadR, ← Matrix.map_mul, lpad_left_inverse]
  simp

private theorem lpadR_isUnit : IsUnit LpadR :=
  Matrix.isUnit_of_left_inverse lpadR_left_inverse

private theorem ldl_identity_real :
    LpadR * DeltaPadR * LpadR.transpose = MpadR := by
  rw [LpadR, DeltaPadR, MpadR, ← Matrix.map_mul, ← Matrix.map_mul]
  simpa only [Matrix.map_transpose] using congrArg (Matrix.map (Rat.castHom ℝ)) ldl_identity

private theorem MpadR_posDef : MpadR.PosDef := by
  rw [← ldl_identity_real]
  simpa only [conjTranspose_eq_transpose] using
    deltaPadR_posDef.mul_mul_conjTranspose_same
      (Matrix.vecMul_injective_of_isUnit lpadR_isUnit)

private theorem MpadR_submatrix : MpadR.submatrix embedPad embedPad = M38r := by
  rw [MpadR, M38r, ← Matrix.map_submatrix, Mpad_submatrix]

private theorem M38r_posDef : M38r.PosDef := by
  rw [← MpadR_submatrix]
  exact MpadR_posDef.submatrix embedPad_injective

private theorem M38r_eq_shifted_distance :
    M38r = (3 : ℝ) • Dr + (17 : ℝ) • (1 : Matrix Vertex Vertex ℝ) := by
  rw [M38r, Dr, M38q_eq_shifted_distance]
  ext i j
  simp [Dq]

/-- The real shifted semantic distance matrix `3 D + 17 I` is positive definite. -/
theorem shifted_distance_real_posDef :
    ((3 : ℝ) • Dr + (17 : ℝ) • (1 : Matrix Vertex Vertex ℝ)).PosDef := by
  rw [← M38r_eq_shifted_distance]
  exact M38r_posDef

/-- Every real eigenvalue of the semantic distance matrix is strictly above `-17/3`. -/
theorem real_eigenpair_above_neg_seventeen_thirds
    {mu : ℝ} {x : Vertex → ℝ} (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) :
    (-17 : ℝ) / 3 < mu := by
  have hpos := shifted_distance_real_posDef.dotProduct_mulVec_pos hx
  rw [add_mulVec, smul_mulVec, smul_mulVec, one_mulVec, heig] at hpos
  simp only [star_trivial, dotProduct_smul] at hpos
  have hnorm : 0 < x ⋝ᵥ x := dotProduct_self_pos.mpr hx
  nlinarith

end Wow284.Induced38
