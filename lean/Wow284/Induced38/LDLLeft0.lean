import Wow284.Induced38.LDLDefinitions

/-! Generated bounded 5x5 integer certificate shard. -/
namespace Wow284.Induced38

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_0 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 0 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 0 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_1 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 1 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 1 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_2 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 2 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 2 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_3 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 3 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 3 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_4 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 4 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 4 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_5 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 5 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 5 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_6 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 6 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 6 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 20000 in
lemma lpad_left_inverse_scaled_rows_0_7 : ∀ c d : Fin 5,
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad 7 d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad 7 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

lemma lpad_left_inverse_scaled_row_0 (s : Fin 8) (c d : Fin 5) :
    (BpadInvNumerator * BpadInt) (coordPad 0 c) (coordPad s d) =
      (scaledIdentityInt) (coordPad 0 c) (coordPad s d) := by
  fin_cases s
  · exact lpad_left_inverse_scaled_rows_0_0 c d
  · exact lpad_left_inverse_scaled_rows_0_1 c d
  · exact lpad_left_inverse_scaled_rows_0_2 c d
  · exact lpad_left_inverse_scaled_rows_0_3 c d
  · exact lpad_left_inverse_scaled_rows_0_4 c d
  · exact lpad_left_inverse_scaled_rows_0_5 c d
  · exact lpad_left_inverse_scaled_rows_0_6 c d
  · exact lpad_left_inverse_scaled_rows_0_7 c d

end Wow284.Induced38
