import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 rational certificate shard. -/
namespace Wow284.Induced38

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_0 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 0 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 0 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_1 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 1 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 1 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_2 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 2 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 2 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_3 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 3 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 3 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_4 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 4 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 4 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_5 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 5 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 5 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_6 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 6 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 6 d) := by
  decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_5_7 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 5 c) (coordPad 7 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad 7 d) := by
  decide

lemma lpad_right_inverse_row_5 (s : Fin 8) (c d : Fin 5) :
    (Lpad * LpadInv) (coordPad 5 c) (coordPad s d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 5 c) (coordPad s d) := by
  fin_cases s
  · exact lpad_right_inverse_rows_5_0 c d
  · exact lpad_right_inverse_rows_5_1 c d
  · exact lpad_right_inverse_rows_5_2 c d
  · exact lpad_right_inverse_rows_5_3 c d
  · exact lpad_right_inverse_rows_5_4 c d
  · exact lpad_right_inverse_rows_5_5 c d
  · exact lpad_right_inverse_rows_5_6 c d
  · exact lpad_right_inverse_rows_5_7 c d

end Wow284.Induced38
