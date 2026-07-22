import Wow284.DiagonalizationDefinitions

/-! Generated bounded certificate shard; do not edit by hand. -/

namespace Wow284

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_0 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 0 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_1 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 1 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_2 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 2 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_3 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 3 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_4 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 4 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_5 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 5 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_6 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 6 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_7 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 7 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_8 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 8 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_0_9 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex 9 d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex 9 d) := by
  decide

lemma eigenbasis_left_inverse_scaled_row_0 (s : Fin 10) (c d : Fin 5) :
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 0 c) (coordVertex s d) =
      (scaledIdentityInt) (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact eigenbasis_left_inverse_scaled_rows_0_0 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_1 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_2 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_3 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_4 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_5 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_6 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_7 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_8 c d
  · exact eigenbasis_left_inverse_scaled_rows_0_9 c d

end Wow284
