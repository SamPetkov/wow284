import Wow284.Induced38.LDLIdentity
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
