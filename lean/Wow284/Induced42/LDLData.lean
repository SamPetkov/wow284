import Wow284.Induced42.LDLIdentity
import Wow284.Induced42.LDLLeft

namespace Wow284.Induced42
open Matrix

theorem ldl_identity : Lpad * DeltaPad * Lpad.transpose = Mpad := by
  rw [DeltaPad_eq_scaled_cast, Matrix.mul_smul, Matrix.smul_mul]
  change ((1 : ℚ) / 36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000) •
      (castPadMatrix BpadInt * castPadMatrix WpadInt *
        (castPadMatrix BpadInt).transpose) =
    castPadMatrix MpadInt
  rw [← castPadMatrix_transpose, ← castPadMatrix_mul, ← castPadMatrix_mul,
    ldl_scaled_identity_int]
  rw [MscaledPadInt, castPadMatrix_smul, smul_smul, one_div]
  change (((((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ)⁻¹ *
      ((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ)) • castPadMatrix MpadInt) =
    castPadMatrix MpadInt)
  have hscaleZ : (36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) ≠ 0 := by positivity
  have hscaleQ : ((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ) ≠ 0 := by
    exact_mod_cast hscaleZ
  rw [inv_mul_cancel₀ hscaleQ, one_smul]

theorem lpad_left_inverse : LpadInv * Lpad =
    (1 : Matrix PadVertex PadVertex ℚ) := by
  change (((1 : ℚ) / 36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000) •
      castPadMatrix BpadInvNumeratorInt) * castPadMatrix BpadInt = 1
  rw [Matrix.smul_mul, ← castPadMatrix_mul, lpad_left_inverse_scaled_int]
  rw [scaledIdentityInt, castPadMatrix_smul, castPadMatrix_one,
    smul_smul, one_div]
  change (((((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ)⁻¹ *
      ((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ)) •
      (1 : Matrix PadVertex PadVertex ℚ)) =
    (1 : Matrix PadVertex PadVertex ℚ))
  have hscaleZ : (36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) ≠ 0 := by positivity
  have hscaleQ : ((36733151369006981105181629103776678622592255692327838191443173928745646808621768799123295546014730080000 : ℤ) : ℚ) ≠ 0 := by
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

end Wow284.Induced42
