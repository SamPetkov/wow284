import Wow284.Induced38.LDLIdentity
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
  decide

lemma M38Int_eq_shiftedCert : M38Int = shiftedCert := by
  rfl

end Wow284.Induced38
