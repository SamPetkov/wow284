import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 rational certificate shard. -/
namespace Wow284.Induced38

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_0 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 0 d) =
      (Mpad) (coordPad 3 c) (coordPad 0 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_1 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 1 d) =
      (Mpad) (coordPad 3 c) (coordPad 1 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_2 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 2 d) =
      (Mpad) (coordPad 3 c) (coordPad 2 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_3 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 3 d) =
      (Mpad) (coordPad 3 c) (coordPad 3 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_4 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 4 d) =
      (Mpad) (coordPad 3 c) (coordPad 4 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_5 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 5 d) =
      (Mpad) (coordPad 3 c) (coordPad 5 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_6 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 6 d) =
      (Mpad) (coordPad 3 c) (coordPad 6 d) := by
  decide

set_option maxRecDepth 20000 in
lemma ldl_identity_rows_3_7 : ∀ c d : Fin 5,
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad 7 d) =
      (Mpad) (coordPad 3 c) (coordPad 7 d) := by
  decide

lemma ldl_identity_row_3 (s : Fin 8) (c d : Fin 5) :
    (Lpad * DeltaPad * Lpad.transpose) (coordPad 3 c) (coordPad s d) =
      (Mpad) (coordPad 3 c) (coordPad s d) := by
  fin_cases s
  · exact ldl_identity_rows_3_0 c d
  · exact ldl_identity_rows_3_1 c d
  · exact ldl_identity_rows_3_2 c d
  · exact ldl_identity_rows_3_3 c d
  · exact ldl_identity_rows_3_4 c d
  · exact ldl_identity_rows_3_5 c d
  · exact ldl_identity_rows_3_6 c d
  · exact ldl_identity_rows_3_7 c d

end Wow284.Induced38
