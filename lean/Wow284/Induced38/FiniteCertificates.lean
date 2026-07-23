import Wow284.Induced38.Finite0
import Wow284.Induced38.Finite1
import Wow284.Induced38.Finite2
import Wow284.Induced38.Finite3
import Wow284.Induced38.Finite4
import Wow284.Induced38.Finite5
import Wow284.Induced38.Finite6
import Wow284.Induced38.Finite7
import Wow284.Induced38.Finite8
import Wow284.Induced38.Finite9
import Wow284.Induced38.Finite10
import Wow284.Induced38.Finite11
import Wow284.Induced38.Finite12
import Wow284.Induced38.Finite13
import Wow284.Induced38.Finite14
import Wow284.Induced38.Finite15
import Wow284.Induced38.Finite16
import Wow284.Induced38.Finite17
import Wow284.Induced38.Finite18

/-! Assembly of exact finite certificates for the 38-vertex graph. -/
namespace Wow284.Induced38

private lemma degree_range_coord (r : Fin 19) (c : Fin 2) :
    degree (coordVertex r c) = 5 ∨ degree (coordVertex r c) = 6 := by
  fin_cases r
  · exact degree_range_row_0 c
  · exact degree_range_row_1 c
  · exact degree_range_row_2 c
  · exact degree_range_row_3 c
  · exact degree_range_row_4 c
  · exact degree_range_row_5 c
  · exact degree_range_row_6 c
  · exact degree_range_row_7 c
  · exact degree_range_row_8 c
  · exact degree_range_row_9 c
  · exact degree_range_row_10 c
  · exact degree_range_row_11 c
  · exact degree_range_row_12 c
  · exact degree_range_row_13 c
  · exact degree_range_row_14 c
  · exact degree_range_row_15 c
  · exact degree_range_row_16 c
  · exact degree_range_row_17 c
  · exact degree_range_row_18 c

theorem degree_five_or_six (v : Vertex) : degree v = 5 ∨ degree v = 6 := by
  rw [← coordVertex_surj v]
  exact degree_range_coord _ _

theorem degree_profile :
    (Finset.univ.filter fun v : Vertex => degree v = 5).card = 10 ∧
    (Finset.univ.filter fun v : Vertex => degree v = 6).card = 28 := by
  decide

private lemma dual_cross_bound_coord (r : Fin 19) (c : Fin 2) :
    17 * degree (coordVertex r c) ≤
      3 * neighborDegreeSum (coordVertex r c) := by
  fin_cases r
  · exact dual_cross_bound_row_0 c
  · exact dual_cross_bound_row_1 c
  · exact dual_cross_bound_row_2 c
  · exact dual_cross_bound_row_3 c
  · exact dual_cross_bound_row_4 c
  · exact dual_cross_bound_row_5 c
  · exact dual_cross_bound_row_6 c
  · exact dual_cross_bound_row_7 c
  · exact dual_cross_bound_row_8 c
  · exact dual_cross_bound_row_9 c
  · exact dual_cross_bound_row_10 c
  · exact dual_cross_bound_row_11 c
  · exact dual_cross_bound_row_12 c
  · exact dual_cross_bound_row_13 c
  · exact dual_cross_bound_row_14 c
  · exact dual_cross_bound_row_15 c
  · exact dual_cross_bound_row_16 c
  · exact dual_cross_bound_row_17 c
  · exact dual_cross_bound_row_18 c

private theorem dual_cross_bound (v : Vertex) :
    17 * degree v ≤ 3 * neighborDegreeSum v := by
  rw [← coordVertex_surj v]
  exact dual_cross_bound_coord _ _

private theorem degree_positive (v : Vertex) : 0 < degree v := by
  rcases degree_five_or_six v with h | h <;> omega

theorem dual_degree_lower_bound (v : Vertex) :
    (17 : ℚ) / 3 ≤ dualDegree v := by
  rw [dualDegree]
  apply (div_le_div_iff₀ (by norm_num) (by exact_mod_cast degree_positive v)).2
  have h :
      (17 : ℚ) * degree v ≤
        3 * (neighborDegreeSum v : ℚ) := by
    exact_mod_cast dual_cross_bound v
  simpa [mul_comm] using h

theorem dual_degree_attained :
    ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3 := by
  refine ⟨1, ?_⟩
  have hd : degree (1 : Vertex) = 6 := by decide
  have hs : neighborDegreeSum (1 : Vertex) = 34 := by decide
  norm_num [dualDegree, hd, hs]

private lemma diameter_row_0 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_0_0 c d
  · exact diameter_rows_0_1 c d
  · exact diameter_rows_0_2 c d
  · exact diameter_rows_0_3 c d
  · exact diameter_rows_0_4 c d
  · exact diameter_rows_0_5 c d
  · exact diameter_rows_0_6 c d
  · exact diameter_rows_0_7 c d
  · exact diameter_rows_0_8 c d
  · exact diameter_rows_0_9 c d
  · exact diameter_rows_0_10 c d
  · exact diameter_rows_0_11 c d
  · exact diameter_rows_0_12 c d
  · exact diameter_rows_0_13 c d
  · exact diameter_rows_0_14 c d
  · exact diameter_rows_0_15 c d
  · exact diameter_rows_0_16 c d
  · exact diameter_rows_0_17 c d
  · exact diameter_rows_0_18 c d
private lemma semantic_distance_row_0 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 0 c) (coordVertex s d) =
      Dcert (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_0_0 c d
  · exact semantic_distance_rows_0_1 c d
  · exact semantic_distance_rows_0_2 c d
  · exact semantic_distance_rows_0_3 c d
  · exact semantic_distance_rows_0_4 c d
  · exact semantic_distance_rows_0_5 c d
  · exact semantic_distance_rows_0_6 c d
  · exact semantic_distance_rows_0_7 c d
  · exact semantic_distance_rows_0_8 c d
  · exact semantic_distance_rows_0_9 c d
  · exact semantic_distance_rows_0_10 c d
  · exact semantic_distance_rows_0_11 c d
  · exact semantic_distance_rows_0_12 c d
  · exact semantic_distance_rows_0_13 c d
  · exact semantic_distance_rows_0_14 c d
  · exact semantic_distance_rows_0_15 c d
  · exact semantic_distance_rows_0_16 c d
  · exact semantic_distance_rows_0_17 c d
  · exact semantic_distance_rows_0_18 c d
private lemma diameter_row_1 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_1_0 c d
  · exact diameter_rows_1_1 c d
  · exact diameter_rows_1_2 c d
  · exact diameter_rows_1_3 c d
  · exact diameter_rows_1_4 c d
  · exact diameter_rows_1_5 c d
  · exact diameter_rows_1_6 c d
  · exact diameter_rows_1_7 c d
  · exact diameter_rows_1_8 c d
  · exact diameter_rows_1_9 c d
  · exact diameter_rows_1_10 c d
  · exact diameter_rows_1_11 c d
  · exact diameter_rows_1_12 c d
  · exact diameter_rows_1_13 c d
  · exact diameter_rows_1_14 c d
  · exact diameter_rows_1_15 c d
  · exact diameter_rows_1_16 c d
  · exact diameter_rows_1_17 c d
  · exact diameter_rows_1_18 c d
private lemma semantic_distance_row_1 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 1 c) (coordVertex s d) =
      Dcert (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_1_0 c d
  · exact semantic_distance_rows_1_1 c d
  · exact semantic_distance_rows_1_2 c d
  · exact semantic_distance_rows_1_3 c d
  · exact semantic_distance_rows_1_4 c d
  · exact semantic_distance_rows_1_5 c d
  · exact semantic_distance_rows_1_6 c d
  · exact semantic_distance_rows_1_7 c d
  · exact semantic_distance_rows_1_8 c d
  · exact semantic_distance_rows_1_9 c d
  · exact semantic_distance_rows_1_10 c d
  · exact semantic_distance_rows_1_11 c d
  · exact semantic_distance_rows_1_12 c d
  · exact semantic_distance_rows_1_13 c d
  · exact semantic_distance_rows_1_14 c d
  · exact semantic_distance_rows_1_15 c d
  · exact semantic_distance_rows_1_16 c d
  · exact semantic_distance_rows_1_17 c d
  · exact semantic_distance_rows_1_18 c d
private lemma diameter_row_2 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_2_0 c d
  · exact diameter_rows_2_1 c d
  · exact diameter_rows_2_2 c d
  · exact diameter_rows_2_3 c d
  · exact diameter_rows_2_4 c d
  · exact diameter_rows_2_5 c d
  · exact diameter_rows_2_6 c d
  · exact diameter_rows_2_7 c d
  · exact diameter_rows_2_8 c d
  · exact diameter_rows_2_9 c d
  · exact diameter_rows_2_10 c d
  · exact diameter_rows_2_11 c d
  · exact diameter_rows_2_12 c d
  · exact diameter_rows_2_13 c d
  · exact diameter_rows_2_14 c d
  · exact diameter_rows_2_15 c d
  · exact diameter_rows_2_16 c d
  · exact diameter_rows_2_17 c d
  · exact diameter_rows_2_18 c d
private lemma semantic_distance_row_2 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 2 c) (coordVertex s d) =
      Dcert (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_2_0 c d
  · exact semantic_distance_rows_2_1 c d
  · exact semantic_distance_rows_2_2 c d
  · exact semantic_distance_rows_2_3 c d
  · exact semantic_distance_rows_2_4 c d
  · exact semantic_distance_rows_2_5 c d
  · exact semantic_distance_rows_2_6 c d
  · exact semantic_distance_rows_2_7 c d
  · exact semantic_distance_rows_2_8 c d
  · exact semantic_distance_rows_2_9 c d
  · exact semantic_distance_rows_2_10 c d
  · exact semantic_distance_rows_2_11 c d
  · exact semantic_distance_rows_2_12 c d
  · exact semantic_distance_rows_2_13 c d
  · exact semantic_distance_rows_2_14 c d
  · exact semantic_distance_rows_2_15 c d
  · exact semantic_distance_rows_2_16 c d
  · exact semantic_distance_rows_2_17 c d
  · exact semantic_distance_rows_2_18 c d
private lemma diameter_row_3 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_3_0 c d
  · exact diameter_rows_3_1 c d
  · exact diameter_rows_3_2 c d
  · exact diameter_rows_3_3 c d
  · exact diameter_rows_3_4 c d
  · exact diameter_rows_3_5 c d
  · exact diameter_rows_3_6 c d
  · exact diameter_rows_3_7 c d
  · exact diameter_rows_3_8 c d
  · exact diameter_rows_3_9 c d
  · exact diameter_rows_3_10 c d
  · exact diameter_rows_3_11 c d
  · exact diameter_rows_3_12 c d
  · exact diameter_rows_3_13 c d
  · exact diameter_rows_3_14 c d
  · exact diameter_rows_3_15 c d
  · exact diameter_rows_3_16 c d
  · exact diameter_rows_3_17 c d
  · exact diameter_rows_3_18 c d
private lemma semantic_distance_row_3 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 3 c) (coordVertex s d) =
      Dcert (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_3_0 c d
  · exact semantic_distance_rows_3_1 c d
  · exact semantic_distance_rows_3_2 c d
  · exact semantic_distance_rows_3_3 c d
  · exact semantic_distance_rows_3_4 c d
  · exact semantic_distance_rows_3_5 c d
  · exact semantic_distance_rows_3_6 c d
  · exact semantic_distance_rows_3_7 c d
  · exact semantic_distance_rows_3_8 c d
  · exact semantic_distance_rows_3_9 c d
  · exact semantic_distance_rows_3_10 c d
  · exact semantic_distance_rows_3_11 c d
  · exact semantic_distance_rows_3_12 c d
  · exact semantic_distance_rows_3_13 c d
  · exact semantic_distance_rows_3_14 c d
  · exact semantic_distance_rows_3_15 c d
  · exact semantic_distance_rows_3_16 c d
  · exact semantic_distance_rows_3_17 c d
  · exact semantic_distance_rows_3_18 c d
private lemma diameter_row_4 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_4_0 c d
  · exact diameter_rows_4_1 c d
  · exact diameter_rows_4_2 c d
  · exact diameter_rows_4_3 c d
  · exact diameter_rows_4_4 c d
  · exact diameter_rows_4_5 c d
  · exact diameter_rows_4_6 c d
  · exact diameter_rows_4_7 c d
  · exact diameter_rows_4_8 c d
  · exact diameter_rows_4_9 c d
  · exact diameter_rows_4_10 c d
  · exact diameter_rows_4_11 c d
  · exact diameter_rows_4_12 c d
  · exact diameter_rows_4_13 c d
  · exact diameter_rows_4_14 c d
  · exact diameter_rows_4_15 c d
  · exact diameter_rows_4_16 c d
  · exact diameter_rows_4_17 c d
  · exact diameter_rows_4_18 c d
private lemma semantic_distance_row_4 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 4 c) (coordVertex s d) =
      Dcert (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_4_0 c d
  · exact semantic_distance_rows_4_1 c d
  · exact semantic_distance_rows_4_2 c d
  · exact semantic_distance_rows_4_3 c d
  · exact semantic_distance_rows_4_4 c d
  · exact semantic_distance_rows_4_5 c d
  · exact semantic_distance_rows_4_6 c d
  · exact semantic_distance_rows_4_7 c d
  · exact semantic_distance_rows_4_8 c d
  · exact semantic_distance_rows_4_9 c d
  · exact semantic_distance_rows_4_10 c d
  · exact semantic_distance_rows_4_11 c d
  · exact semantic_distance_rows_4_12 c d
  · exact semantic_distance_rows_4_13 c d
  · exact semantic_distance_rows_4_14 c d
  · exact semantic_distance_rows_4_15 c d
  · exact semantic_distance_rows_4_16 c d
  · exact semantic_distance_rows_4_17 c d
  · exact semantic_distance_rows_4_18 c d
private lemma diameter_row_5 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_5_0 c d
  · exact diameter_rows_5_1 c d
  · exact diameter_rows_5_2 c d
  · exact diameter_rows_5_3 c d
  · exact diameter_rows_5_4 c d
  · exact diameter_rows_5_5 c d
  · exact diameter_rows_5_6 c d
  · exact diameter_rows_5_7 c d
  · exact diameter_rows_5_8 c d
  · exact diameter_rows_5_9 c d
  · exact diameter_rows_5_10 c d
  · exact diameter_rows_5_11 c d
  · exact diameter_rows_5_12 c d
  · exact diameter_rows_5_13 c d
  · exact diameter_rows_5_14 c d
  · exact diameter_rows_5_15 c d
  · exact diameter_rows_5_16 c d
  · exact diameter_rows_5_17 c d
  · exact diameter_rows_5_18 c d
private lemma semantic_distance_row_5 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 5 c) (coordVertex s d) =
      Dcert (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_5_0 c d
  · exact semantic_distance_rows_5_1 c d
  · exact semantic_distance_rows_5_2 c d
  · exact semantic_distance_rows_5_3 c d
  · exact semantic_distance_rows_5_4 c d
  · exact semantic_distance_rows_5_5 c d
  · exact semantic_distance_rows_5_6 c d
  · exact semantic_distance_rows_5_7 c d
  · exact semantic_distance_rows_5_8 c d
  · exact semantic_distance_rows_5_9 c d
  · exact semantic_distance_rows_5_10 c d
  · exact semantic_distance_rows_5_11 c d
  · exact semantic_distance_rows_5_12 c d
  · exact semantic_distance_rows_5_13 c d
  · exact semantic_distance_rows_5_14 c d
  · exact semantic_distance_rows_5_15 c d
  · exact semantic_distance_rows_5_16 c d
  · exact semantic_distance_rows_5_17 c d
  · exact semantic_distance_rows_5_18 c d
private lemma diameter_row_6 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_6_0 c d
  · exact diameter_rows_6_1 c d
  · exact diameter_rows_6_2 c d
  · exact diameter_rows_6_3 c d
  · exact diameter_rows_6_4 c d
  · exact diameter_rows_6_5 c d
  · exact diameter_rows_6_6 c d
  · exact diameter_rows_6_7 c d
  · exact diameter_rows_6_8 c d
  · exact diameter_rows_6_9 c d
  · exact diameter_rows_6_10 c d
  · exact diameter_rows_6_11 c d
  · exact diameter_rows_6_12 c d
  · exact diameter_rows_6_13 c d
  · exact diameter_rows_6_14 c d
  · exact diameter_rows_6_15 c d
  · exact diameter_rows_6_16 c d
  · exact diameter_rows_6_17 c d
  · exact diameter_rows_6_18 c d
private lemma semantic_distance_row_6 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 6 c) (coordVertex s d) =
      Dcert (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_6_0 c d
  · exact semantic_distance_rows_6_1 c d
  · exact semantic_distance_rows_6_2 c d
  · exact semantic_distance_rows_6_3 c d
  · exact semantic_distance_rows_6_4 c d
  · exact semantic_distance_rows_6_5 c d
  · exact semantic_distance_rows_6_6 c d
  · exact semantic_distance_rows_6_7 c d
  · exact semantic_distance_rows_6_8 c d
  · exact semantic_distance_rows_6_9 c d
  · exact semantic_distance_rows_6_10 c d
  · exact semantic_distance_rows_6_11 c d
  · exact semantic_distance_rows_6_12 c d
  · exact semantic_distance_rows_6_13 c d
  · exact semantic_distance_rows_6_14 c d
  · exact semantic_distance_rows_6_15 c d
  · exact semantic_distance_rows_6_16 c d
  · exact semantic_distance_rows_6_17 c d
  · exact semantic_distance_rows_6_18 c d
private lemma diameter_row_7 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_7_0 c d
  · exact diameter_rows_7_1 c d
  · exact diameter_rows_7_2 c d
  · exact diameter_rows_7_3 c d
  · exact diameter_rows_7_4 c d
  · exact diameter_rows_7_5 c d
  · exact diameter_rows_7_6 c d
  · exact diameter_rows_7_7 c d
  · exact diameter_rows_7_8 c d
  · exact diameter_rows_7_9 c d
  · exact diameter_rows_7_10 c d
  · exact diameter_rows_7_11 c d
  · exact diameter_rows_7_12 c d
  · exact diameter_rows_7_13 c d
  · exact diameter_rows_7_14 c d
  · exact diameter_rows_7_15 c d
  · exact diameter_rows_7_16 c d
  · exact diameter_rows_7_17 c d
  · exact diameter_rows_7_18 c d
private lemma semantic_distance_row_7 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 7 c) (coordVertex s d) =
      Dcert (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_7_0 c d
  · exact semantic_distance_rows_7_1 c d
  · exact semantic_distance_rows_7_2 c d
  · exact semantic_distance_rows_7_3 c d
  · exact semantic_distance_rows_7_4 c d
  · exact semantic_distance_rows_7_5 c d
  · exact semantic_distance_rows_7_6 c d
  · exact semantic_distance_rows_7_7 c d
  · exact semantic_distance_rows_7_8 c d
  · exact semantic_distance_rows_7_9 c d
  · exact semantic_distance_rows_7_10 c d
  · exact semantic_distance_rows_7_11 c d
  · exact semantic_distance_rows_7_12 c d
  · exact semantic_distance_rows_7_13 c d
  · exact semantic_distance_rows_7_14 c d
  · exact semantic_distance_rows_7_15 c d
  · exact semantic_distance_rows_7_16 c d
  · exact semantic_distance_rows_7_17 c d
  · exact semantic_distance_rows_7_18 c d
private lemma diameter_row_8 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 8 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_8_0 c d
  · exact diameter_rows_8_1 c d
  · exact diameter_rows_8_2 c d
  · exact diameter_rows_8_3 c d
  · exact diameter_rows_8_4 c d
  · exact diameter_rows_8_5 c d
  · exact diameter_rows_8_6 c d
  · exact diameter_rows_8_7 c d
  · exact diameter_rows_8_8 c d
  · exact diameter_rows_8_9 c d
  · exact diameter_rows_8_10 c d
  · exact diameter_rows_8_11 c d
  · exact diameter_rows_8_12 c d
  · exact diameter_rows_8_13 c d
  · exact diameter_rows_8_14 c d
  · exact diameter_rows_8_15 c d
  · exact diameter_rows_8_16 c d
  · exact diameter_rows_8_17 c d
  · exact diameter_rows_8_18 c d
private lemma semantic_distance_row_8 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 8 c) (coordVertex s d) =
      Dcert (coordVertex 8 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_8_0 c d
  · exact semantic_distance_rows_8_1 c d
  · exact semantic_distance_rows_8_2 c d
  · exact semantic_distance_rows_8_3 c d
  · exact semantic_distance_rows_8_4 c d
  · exact semantic_distance_rows_8_5 c d
  · exact semantic_distance_rows_8_6 c d
  · exact semantic_distance_rows_8_7 c d
  · exact semantic_distance_rows_8_8 c d
  · exact semantic_distance_rows_8_9 c d
  · exact semantic_distance_rows_8_10 c d
  · exact semantic_distance_rows_8_11 c d
  · exact semantic_distance_rows_8_12 c d
  · exact semantic_distance_rows_8_13 c d
  · exact semantic_distance_rows_8_14 c d
  · exact semantic_distance_rows_8_15 c d
  · exact semantic_distance_rows_8_16 c d
  · exact semantic_distance_rows_8_17 c d
  · exact semantic_distance_rows_8_18 c d
private lemma diameter_row_9 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 9 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_9_0 c d
  · exact diameter_rows_9_1 c d
  · exact diameter_rows_9_2 c d
  · exact diameter_rows_9_3 c d
  · exact diameter_rows_9_4 c d
  · exact diameter_rows_9_5 c d
  · exact diameter_rows_9_6 c d
  · exact diameter_rows_9_7 c d
  · exact diameter_rows_9_8 c d
  · exact diameter_rows_9_9 c d
  · exact diameter_rows_9_10 c d
  · exact diameter_rows_9_11 c d
  · exact diameter_rows_9_12 c d
  · exact diameter_rows_9_13 c d
  · exact diameter_rows_9_14 c d
  · exact diameter_rows_9_15 c d
  · exact diameter_rows_9_16 c d
  · exact diameter_rows_9_17 c d
  · exact diameter_rows_9_18 c d
private lemma semantic_distance_row_9 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 9 c) (coordVertex s d) =
      Dcert (coordVertex 9 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_9_0 c d
  · exact semantic_distance_rows_9_1 c d
  · exact semantic_distance_rows_9_2 c d
  · exact semantic_distance_rows_9_3 c d
  · exact semantic_distance_rows_9_4 c d
  · exact semantic_distance_rows_9_5 c d
  · exact semantic_distance_rows_9_6 c d
  · exact semantic_distance_rows_9_7 c d
  · exact semantic_distance_rows_9_8 c d
  · exact semantic_distance_rows_9_9 c d
  · exact semantic_distance_rows_9_10 c d
  · exact semantic_distance_rows_9_11 c d
  · exact semantic_distance_rows_9_12 c d
  · exact semantic_distance_rows_9_13 c d
  · exact semantic_distance_rows_9_14 c d
  · exact semantic_distance_rows_9_15 c d
  · exact semantic_distance_rows_9_16 c d
  · exact semantic_distance_rows_9_17 c d
  · exact semantic_distance_rows_9_18 c d
private lemma diameter_row_10 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 10 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_10_0 c d
  · exact diameter_rows_10_1 c d
  · exact diameter_rows_10_2 c d
  · exact diameter_rows_10_3 c d
  · exact diameter_rows_10_4 c d
  · exact diameter_rows_10_5 c d
  · exact diameter_rows_10_6 c d
  · exact diameter_rows_10_7 c d
  · exact diameter_rows_10_8 c d
  · exact diameter_rows_10_9 c d
  · exact diameter_rows_10_10 c d
  · exact diameter_rows_10_11 c d
  · exact diameter_rows_10_12 c d
  · exact diameter_rows_10_13 c d
  · exact diameter_rows_10_14 c d
  · exact diameter_rows_10_15 c d
  · exact diameter_rows_10_16 c d
  · exact diameter_rows_10_17 c d
  · exact diameter_rows_10_18 c d
private lemma semantic_distance_row_10 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 10 c) (coordVertex s d) =
      Dcert (coordVertex 10 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_10_0 c d
  · exact semantic_distance_rows_10_1 c d
  · exact semantic_distance_rows_10_2 c d
  · exact semantic_distance_rows_10_3 c d
  · exact semantic_distance_rows_10_4 c d
  · exact semantic_distance_rows_10_5 c d
  · exact semantic_distance_rows_10_6 c d
  · exact semantic_distance_rows_10_7 c d
  · exact semantic_distance_rows_10_8 c d
  · exact semantic_distance_rows_10_9 c d
  · exact semantic_distance_rows_10_10 c d
  · exact semantic_distance_rows_10_11 c d
  · exact semantic_distance_rows_10_12 c d
  · exact semantic_distance_rows_10_13 c d
  · exact semantic_distance_rows_10_14 c d
  · exact semantic_distance_rows_10_15 c d
  · exact semantic_distance_rows_10_16 c d
  · exact semantic_distance_rows_10_17 c d
  · exact semantic_distance_rows_10_18 c d
private lemma diameter_row_11 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 11 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_11_0 c d
  · exact diameter_rows_11_1 c d
  · exact diameter_rows_11_2 c d
  · exact diameter_rows_11_3 c d
  · exact diameter_rows_11_4 c d
  · exact diameter_rows_11_5 c d
  · exact diameter_rows_11_6 c d
  · exact diameter_rows_11_7 c d
  · exact diameter_rows_11_8 c d
  · exact diameter_rows_11_9 c d
  · exact diameter_rows_11_10 c d
  · exact diameter_rows_11_11 c d
  · exact diameter_rows_11_12 c d
  · exact diameter_rows_11_13 c d
  · exact diameter_rows_11_14 c d
  · exact diameter_rows_11_15 c d
  · exact diameter_rows_11_16 c d
  · exact diameter_rows_11_17 c d
  · exact diameter_rows_11_18 c d
private lemma semantic_distance_row_11 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 11 c) (coordVertex s d) =
      Dcert (coordVertex 11 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_11_0 c d
  · exact semantic_distance_rows_11_1 c d
  · exact semantic_distance_rows_11_2 c d
  · exact semantic_distance_rows_11_3 c d
  · exact semantic_distance_rows_11_4 c d
  · exact semantic_distance_rows_11_5 c d
  · exact semantic_distance_rows_11_6 c d
  · exact semantic_distance_rows_11_7 c d
  · exact semantic_distance_rows_11_8 c d
  · exact semantic_distance_rows_11_9 c d
  · exact semantic_distance_rows_11_10 c d
  · exact semantic_distance_rows_11_11 c d
  · exact semantic_distance_rows_11_12 c d
  · exact semantic_distance_rows_11_13 c d
  · exact semantic_distance_rows_11_14 c d
  · exact semantic_distance_rows_11_15 c d
  · exact semantic_distance_rows_11_16 c d
  · exact semantic_distance_rows_11_17 c d
  · exact semantic_distance_rows_11_18 c d
private lemma diameter_row_12 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 12 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_12_0 c d
  · exact diameter_rows_12_1 c d
  · exact diameter_rows_12_2 c d
  · exact diameter_rows_12_3 c d
  · exact diameter_rows_12_4 c d
  · exact diameter_rows_12_5 c d
  · exact diameter_rows_12_6 c d
  · exact diameter_rows_12_7 c d
  · exact diameter_rows_12_8 c d
  · exact diameter_rows_12_9 c d
  · exact diameter_rows_12_10 c d
  · exact diameter_rows_12_11 c d
  · exact diameter_rows_12_12 c d
  · exact diameter_rows_12_13 c d
  · exact diameter_rows_12_14 c d
  · exact diameter_rows_12_15 c d
  · exact diameter_rows_12_16 c d
  · exact diameter_rows_12_17 c d
  · exact diameter_rows_12_18 c d
private lemma semantic_distance_row_12 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 12 c) (coordVertex s d) =
      Dcert (coordVertex 12 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_12_0 c d
  · exact semantic_distance_rows_12_1 c d
  · exact semantic_distance_rows_12_2 c d
  · exact semantic_distance_rows_12_3 c d
  · exact semantic_distance_rows_12_4 c d
  · exact semantic_distance_rows_12_5 c d
  · exact semantic_distance_rows_12_6 c d
  · exact semantic_distance_rows_12_7 c d
  · exact semantic_distance_rows_12_8 c d
  · exact semantic_distance_rows_12_9 c d
  · exact semantic_distance_rows_12_10 c d
  · exact semantic_distance_rows_12_11 c d
  · exact semantic_distance_rows_12_12 c d
  · exact semantic_distance_rows_12_13 c d
  · exact semantic_distance_rows_12_14 c d
  · exact semantic_distance_rows_12_15 c d
  · exact semantic_distance_rows_12_16 c d
  · exact semantic_distance_rows_12_17 c d
  · exact semantic_distance_rows_12_18 c d
private lemma diameter_row_13 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 13 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_13_0 c d
  · exact diameter_rows_13_1 c d
  · exact diameter_rows_13_2 c d
  · exact diameter_rows_13_3 c d
  · exact diameter_rows_13_4 c d
  · exact diameter_rows_13_5 c d
  · exact diameter_rows_13_6 c d
  · exact diameter_rows_13_7 c d
  · exact diameter_rows_13_8 c d
  · exact diameter_rows_13_9 c d
  · exact diameter_rows_13_10 c d
  · exact diameter_rows_13_11 c d
  · exact diameter_rows_13_12 c d
  · exact diameter_rows_13_13 c d
  · exact diameter_rows_13_14 c d
  · exact diameter_rows_13_15 c d
  · exact diameter_rows_13_16 c d
  · exact diameter_rows_13_17 c d
  · exact diameter_rows_13_18 c d
private lemma semantic_distance_row_13 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 13 c) (coordVertex s d) =
      Dcert (coordVertex 13 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_13_0 c d
  · exact semantic_distance_rows_13_1 c d
  · exact semantic_distance_rows_13_2 c d
  · exact semantic_distance_rows_13_3 c d
  · exact semantic_distance_rows_13_4 c d
  · exact semantic_distance_rows_13_5 c d
  · exact semantic_distance_rows_13_6 c d
  · exact semantic_distance_rows_13_7 c d
  · exact semantic_distance_rows_13_8 c d
  · exact semantic_distance_rows_13_9 c d
  · exact semantic_distance_rows_13_10 c d
  · exact semantic_distance_rows_13_11 c d
  · exact semantic_distance_rows_13_12 c d
  · exact semantic_distance_rows_13_13 c d
  · exact semantic_distance_rows_13_14 c d
  · exact semantic_distance_rows_13_15 c d
  · exact semantic_distance_rows_13_16 c d
  · exact semantic_distance_rows_13_17 c d
  · exact semantic_distance_rows_13_18 c d
private lemma diameter_row_14 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 14 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_14_0 c d
  · exact diameter_rows_14_1 c d
  · exact diameter_rows_14_2 c d
  · exact diameter_rows_14_3 c d
  · exact diameter_rows_14_4 c d
  · exact diameter_rows_14_5 c d
  · exact diameter_rows_14_6 c d
  · exact diameter_rows_14_7 c d
  · exact diameter_rows_14_8 c d
  · exact diameter_rows_14_9 c d
  · exact diameter_rows_14_10 c d
  · exact diameter_rows_14_11 c d
  · exact diameter_rows_14_12 c d
  · exact diameter_rows_14_13 c d
  · exact diameter_rows_14_14 c d
  · exact diameter_rows_14_15 c d
  · exact diameter_rows_14_16 c d
  · exact diameter_rows_14_17 c d
  · exact diameter_rows_14_18 c d
private lemma semantic_distance_row_14 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 14 c) (coordVertex s d) =
      Dcert (coordVertex 14 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_14_0 c d
  · exact semantic_distance_rows_14_1 c d
  · exact semantic_distance_rows_14_2 c d
  · exact semantic_distance_rows_14_3 c d
  · exact semantic_distance_rows_14_4 c d
  · exact semantic_distance_rows_14_5 c d
  · exact semantic_distance_rows_14_6 c d
  · exact semantic_distance_rows_14_7 c d
  · exact semantic_distance_rows_14_8 c d
  · exact semantic_distance_rows_14_9 c d
  · exact semantic_distance_rows_14_10 c d
  · exact semantic_distance_rows_14_11 c d
  · exact semantic_distance_rows_14_12 c d
  · exact semantic_distance_rows_14_13 c d
  · exact semantic_distance_rows_14_14 c d
  · exact semantic_distance_rows_14_15 c d
  · exact semantic_distance_rows_14_16 c d
  · exact semantic_distance_rows_14_17 c d
  · exact semantic_distance_rows_14_18 c d
private lemma diameter_row_15 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 15 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_15_0 c d
  · exact diameter_rows_15_1 c d
  · exact diameter_rows_15_2 c d
  · exact diameter_rows_15_3 c d
  · exact diameter_rows_15_4 c d
  · exact diameter_rows_15_5 c d
  · exact diameter_rows_15_6 c d
  · exact diameter_rows_15_7 c d
  · exact diameter_rows_15_8 c d
  · exact diameter_rows_15_9 c d
  · exact diameter_rows_15_10 c d
  · exact diameter_rows_15_11 c d
  · exact diameter_rows_15_12 c d
  · exact diameter_rows_15_13 c d
  · exact diameter_rows_15_14 c d
  · exact diameter_rows_15_15 c d
  · exact diameter_rows_15_16 c d
  · exact diameter_rows_15_17 c d
  · exact diameter_rows_15_18 c d
private lemma semantic_distance_row_15 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 15 c) (coordVertex s d) =
      Dcert (coordVertex 15 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_15_0 c d
  · exact semantic_distance_rows_15_1 c d
  · exact semantic_distance_rows_15_2 c d
  · exact semantic_distance_rows_15_3 c d
  · exact semantic_distance_rows_15_4 c d
  · exact semantic_distance_rows_15_5 c d
  · exact semantic_distance_rows_15_6 c d
  · exact semantic_distance_rows_15_7 c d
  · exact semantic_distance_rows_15_8 c d
  · exact semantic_distance_rows_15_9 c d
  · exact semantic_distance_rows_15_10 c d
  · exact semantic_distance_rows_15_11 c d
  · exact semantic_distance_rows_15_12 c d
  · exact semantic_distance_rows_15_13 c d
  · exact semantic_distance_rows_15_14 c d
  · exact semantic_distance_rows_15_15 c d
  · exact semantic_distance_rows_15_16 c d
  · exact semantic_distance_rows_15_17 c d
  · exact semantic_distance_rows_15_18 c d
private lemma diameter_row_16 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 16 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_16_0 c d
  · exact diameter_rows_16_1 c d
  · exact diameter_rows_16_2 c d
  · exact diameter_rows_16_3 c d
  · exact diameter_rows_16_4 c d
  · exact diameter_rows_16_5 c d
  · exact diameter_rows_16_6 c d
  · exact diameter_rows_16_7 c d
  · exact diameter_rows_16_8 c d
  · exact diameter_rows_16_9 c d
  · exact diameter_rows_16_10 c d
  · exact diameter_rows_16_11 c d
  · exact diameter_rows_16_12 c d
  · exact diameter_rows_16_13 c d
  · exact diameter_rows_16_14 c d
  · exact diameter_rows_16_15 c d
  · exact diameter_rows_16_16 c d
  · exact diameter_rows_16_17 c d
  · exact diameter_rows_16_18 c d
private lemma semantic_distance_row_16 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 16 c) (coordVertex s d) =
      Dcert (coordVertex 16 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_16_0 c d
  · exact semantic_distance_rows_16_1 c d
  · exact semantic_distance_rows_16_2 c d
  · exact semantic_distance_rows_16_3 c d
  · exact semantic_distance_rows_16_4 c d
  · exact semantic_distance_rows_16_5 c d
  · exact semantic_distance_rows_16_6 c d
  · exact semantic_distance_rows_16_7 c d
  · exact semantic_distance_rows_16_8 c d
  · exact semantic_distance_rows_16_9 c d
  · exact semantic_distance_rows_16_10 c d
  · exact semantic_distance_rows_16_11 c d
  · exact semantic_distance_rows_16_12 c d
  · exact semantic_distance_rows_16_13 c d
  · exact semantic_distance_rows_16_14 c d
  · exact semantic_distance_rows_16_15 c d
  · exact semantic_distance_rows_16_16 c d
  · exact semantic_distance_rows_16_17 c d
  · exact semantic_distance_rows_16_18 c d
private lemma diameter_row_17 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 17 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_17_0 c d
  · exact diameter_rows_17_1 c d
  · exact diameter_rows_17_2 c d
  · exact diameter_rows_17_3 c d
  · exact diameter_rows_17_4 c d
  · exact diameter_rows_17_5 c d
  · exact diameter_rows_17_6 c d
  · exact diameter_rows_17_7 c d
  · exact diameter_rows_17_8 c d
  · exact diameter_rows_17_9 c d
  · exact diameter_rows_17_10 c d
  · exact diameter_rows_17_11 c d
  · exact diameter_rows_17_12 c d
  · exact diameter_rows_17_13 c d
  · exact diameter_rows_17_14 c d
  · exact diameter_rows_17_15 c d
  · exact diameter_rows_17_16 c d
  · exact diameter_rows_17_17 c d
  · exact diameter_rows_17_18 c d
private lemma semantic_distance_row_17 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 17 c) (coordVertex s d) =
      Dcert (coordVertex 17 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_17_0 c d
  · exact semantic_distance_rows_17_1 c d
  · exact semantic_distance_rows_17_2 c d
  · exact semantic_distance_rows_17_3 c d
  · exact semantic_distance_rows_17_4 c d
  · exact semantic_distance_rows_17_5 c d
  · exact semantic_distance_rows_17_6 c d
  · exact semantic_distance_rows_17_7 c d
  · exact semantic_distance_rows_17_8 c d
  · exact semantic_distance_rows_17_9 c d
  · exact semantic_distance_rows_17_10 c d
  · exact semantic_distance_rows_17_11 c d
  · exact semantic_distance_rows_17_12 c d
  · exact semantic_distance_rows_17_13 c d
  · exact semantic_distance_rows_17_14 c d
  · exact semantic_distance_rows_17_15 c d
  · exact semantic_distance_rows_17_16 c d
  · exact semantic_distance_rows_17_17 c d
  · exact semantic_distance_rows_17_18 c d
private lemma diameter_row_18 (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex 18 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_18_0 c d
  · exact diameter_rows_18_1 c d
  · exact diameter_rows_18_2 c d
  · exact diameter_rows_18_3 c d
  · exact diameter_rows_18_4 c d
  · exact diameter_rows_18_5 c d
  · exact diameter_rows_18_6 c d
  · exact diameter_rows_18_7 c d
  · exact diameter_rows_18_8 c d
  · exact diameter_rows_18_9 c d
  · exact diameter_rows_18_10 c d
  · exact diameter_rows_18_11 c d
  · exact diameter_rows_18_12 c d
  · exact diameter_rows_18_13 c d
  · exact diameter_rows_18_14 c d
  · exact diameter_rows_18_15 c d
  · exact diameter_rows_18_16 c d
  · exact diameter_rows_18_17 c d
  · exact diameter_rows_18_18 c d
private lemma semantic_distance_row_18 (s : Fin 19) (c d : Fin 2) :
    D (coordVertex 18 c) (coordVertex s d) =
      Dcert (coordVertex 18 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_18_0 c d
  · exact semantic_distance_rows_18_1 c d
  · exact semantic_distance_rows_18_2 c d
  · exact semantic_distance_rows_18_3 c d
  · exact semantic_distance_rows_18_4 c d
  · exact semantic_distance_rows_18_5 c d
  · exact semantic_distance_rows_18_6 c d
  · exact semantic_distance_rows_18_7 c d
  · exact semantic_distance_rows_18_8 c d
  · exact semantic_distance_rows_18_9 c d
  · exact semantic_distance_rows_18_10 c d
  · exact semantic_distance_rows_18_11 c d
  · exact semantic_distance_rows_18_12 c d
  · exact semantic_distance_rows_18_13 c d
  · exact semantic_distance_rows_18_14 c d
  · exact semantic_distance_rows_18_15 c d
  · exact semantic_distance_rows_18_16 c d
  · exact semantic_distance_rows_18_17 c d
  · exact semantic_distance_rows_18_18 c d

private lemma diameter_coord (r s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact diameter_row_0 s c d
  · exact diameter_row_1 s c d
  · exact diameter_row_2 s c d
  · exact diameter_row_3 s c d
  · exact diameter_row_4 s c d
  · exact diameter_row_5 s c d
  · exact diameter_row_6 s c d
  · exact diameter_row_7 s c d
  · exact diameter_row_8 s c d
  · exact diameter_row_9 s c d
  · exact diameter_row_10 s c d
  · exact diameter_row_11 s c d
  · exact diameter_row_12 s c d
  · exact diameter_row_13 s c d
  · exact diameter_row_14 s c d
  · exact diameter_row_15 s c d
  · exact diameter_row_16 s c d
  · exact diameter_row_17 s c d
  · exact diameter_row_18 s c d

theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v
  rw [← coordVertex_surj u, ← coordVertex_surj v]
  exact diameter_coord _ _ _ _

theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 5 ∧ HasPathAtMostThree (0 : Vertex) 5 := by
  set_option maxRecDepth 10000 in
    decide

private lemma semantic_distance_coord (r s : Fin 19) (c d : Fin 2) :
    D (coordVertex r c) (coordVertex s d) =
      Dcert (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact semantic_distance_row_0 s c d
  · exact semantic_distance_row_1 s c d
  · exact semantic_distance_row_2 s c d
  · exact semantic_distance_row_3 s c d
  · exact semantic_distance_row_4 s c d
  · exact semantic_distance_row_5 s c d
  · exact semantic_distance_row_6 s c d
  · exact semantic_distance_row_7 s c d
  · exact semantic_distance_row_8 s c d
  · exact semantic_distance_row_9 s c d
  · exact semantic_distance_row_10 s c d
  · exact semantic_distance_row_11 s c d
  · exact semantic_distance_row_12 s c d
  · exact semantic_distance_row_13 s c d
  · exact semantic_distance_row_14 s c d
  · exact semantic_distance_row_15 s c d
  · exact semantic_distance_row_16 s c d
  · exact semantic_distance_row_17 s c d
  · exact semantic_distance_row_18 s c d

theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact semantic_distance_coord _ _ _ _

end Wow284.Induced38
