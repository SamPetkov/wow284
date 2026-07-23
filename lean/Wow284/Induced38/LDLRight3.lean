import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 rational certificate shard. -/
namespace Wow284.Induced38

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_0 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 0 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 0 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_1 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 1 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 1 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_2 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 2 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 2 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_3 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 3 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 3 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_4 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 4 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 4 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_5 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 5 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 5 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_6 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 6 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 6 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_right_inverse_rows_3_7 : ∀ c d : Fin 5,
    (Lpad * LpadInv) (coordPad 3 c) (coordPad 7 d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad 7 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

lemma lpad_right_inverse_row_3 (s : Fin 8) (c d : Fin 5) :
    (Lpad * LpadInv) (coordPad 3 c) (coordPad s d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad 3 c) (coordPad s d) := by
  fin_cases s
  · exact lpad_right_inverse_rows_3_0 c d
  · exact lpad_right_inverse_rows_3_1 c d
  · exact lpad_right_inverse_rows_3_2 c d
  · exact lpad_right_inverse_rows_3_3 c d
  · exact lpad_right_inverse_rows_3_4 c d
  · exact lpad_right_inverse_rows_3_5 c d
  · exact lpad_right_inverse_rows_3_6 c d
  · exact lpad_right_inverse_rows_3_7 c d

end Wow284.Induced38
