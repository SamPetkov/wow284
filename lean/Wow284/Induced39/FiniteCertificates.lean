import Wow284.Induced39.Finite0
import Wow284.Induced39.Finite1
import Wow284.Induced39.Finite2
import Wow284.Induced39.Finite3
import Wow284.Induced39.Finite4
import Wow284.Induced39.Finite5
import Wow284.Induced39.Finite6
import Wow284.Induced39.Finite7
import Wow284.Induced39.Finite8
import Wow284.Induced39.Finite9
import Wow284.Induced39.Finite10
import Wow284.Induced39.Finite11
import Wow284.Induced39.Finite12
/-! Assembly of exact degree, dual-degree, diameter, and distance certificates. -/
namespace Wow284.Induced39
private lemma degree_range_coord (r : Fin 13) (c : Fin 3) : degree (coordVertex r c) = 5 ∨ degree (coordVertex r c) = 6 := by
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
theorem degree_range (v : Vertex) : degree v = 5 ∨ degree v = 6 := by
  rw [← coordVertex_surj v]; exact degree_range_coord _ _
theorem degree_positive (v : Vertex) : 0 < degree v := by
  rcases degree_range v with h | h <;> omega

theorem degree_profile : (Finset.univ.filter fun v : Vertex => degree v = 5).card = 6 ∧
    (Finset.univ.filter fun v : Vertex => degree v = 6).card = 33 := by decide
private lemma dual_bound_nat_coord (r : Fin 13) (c : Fin 3) :
    35 * degree (coordVertex r c) ≤
      6 * neighborDegreeSum (coordVertex r c) := by
  fin_cases r
  · exact dual_bound_nat_row_0 c
  · exact dual_bound_nat_row_1 c
  · exact dual_bound_nat_row_2 c
  · exact dual_bound_nat_row_3 c
  · exact dual_bound_nat_row_4 c
  · exact dual_bound_nat_row_5 c
  · exact dual_bound_nat_row_6 c
  · exact dual_bound_nat_row_7 c
  · exact dual_bound_nat_row_8 c
  · exact dual_bound_nat_row_9 c
  · exact dual_bound_nat_row_10 c
  · exact dual_bound_nat_row_11 c
  · exact dual_bound_nat_row_12 c
private theorem dual_bound_nat (v : Vertex) :
    35 * degree v ≤ 6 * neighborDegreeSum v := by
  rw [← coordVertex_surj v]
  exact dual_bound_nat_coord _ _
theorem dual_degree_lower_bound (v : Vertex) : (35 : ℚ) / 6 ≤ dualDegree v := by
  unfold dualDegree
  have hdegree : (0 : ℚ) < (degree v : ℚ) := by
    exact_mod_cast degree_positive v
  apply (div_le_div_iff₀ (by norm_num : (0 : ℚ) < 6) hdegree).2
  have hbound := dual_bound_nat v
  have hbound' :
      35 * degree v ≤ neighborDegreeSum v * 6 := by
    simpa [mul_comm] using hbound
  exact_mod_cast hbound'
private lemma dual_degree_attained_data :
    degree (1 : Vertex) = 6 ∧
      neighborDegreeSum (1 : Vertex) = 35 := by decide
theorem dual_degree_attained : ∃ v : Vertex, dualDegree v = (35 : ℚ) / 6 := by
  refine ⟨1, ?_⟩
  rcases dual_degree_attained_data with ⟨hdegree, hsum⟩
  norm_num [dualDegree, hdegree, hsum]

private lemma diameter_row_0 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_0 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 0 c) (coordVertex s d) = Dcert (coordVertex 0 c) (coordVertex s d) := by
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
private lemma diameter_row_1 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_1 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 1 c) (coordVertex s d) = Dcert (coordVertex 1 c) (coordVertex s d) := by
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
private lemma diameter_row_2 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_2 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 2 c) (coordVertex s d) = Dcert (coordVertex 2 c) (coordVertex s d) := by
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
private lemma diameter_row_3 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_3 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 3 c) (coordVertex s d) = Dcert (coordVertex 3 c) (coordVertex s d) := by
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
private lemma diameter_row_4 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_4 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 4 c) (coordVertex s d) = Dcert (coordVertex 4 c) (coordVertex s d) := by
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
private lemma diameter_row_5 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_5 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 5 c) (coordVertex s d) = Dcert (coordVertex 5 c) (coordVertex s d) := by
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
private lemma diameter_row_6 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_6 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 6 c) (coordVertex s d) = Dcert (coordVertex 6 c) (coordVertex s d) := by
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
private lemma diameter_row_7 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_7 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 7 c) (coordVertex s d) = Dcert (coordVertex 7 c) (coordVertex s d) := by
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
private lemma diameter_row_8 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_8 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 8 c) (coordVertex s d) = Dcert (coordVertex 8 c) (coordVertex s d) := by
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
private lemma diameter_row_9 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_9 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 9 c) (coordVertex s d) = Dcert (coordVertex 9 c) (coordVertex s d) := by
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
private lemma diameter_row_10 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_10 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 10 c) (coordVertex s d) = Dcert (coordVertex 10 c) (coordVertex s d) := by
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
private lemma diameter_row_11 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_11 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 11 c) (coordVertex s d) = Dcert (coordVertex 11 c) (coordVertex s d) := by
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
private lemma diameter_row_12 (s : Fin 13) (c d : Fin 3) :
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
private lemma semantic_distance_row_12 (s : Fin 13) (c d : Fin 3) :
    D (coordVertex 12 c) (coordVertex s d) = Dcert (coordVertex 12 c) (coordVertex s d) := by
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
private lemma diameter_coord (r s : Fin 13) (c d : Fin 3) :
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
theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v; rw [← coordVertex_surj u, ← coordVertex_surj v]; exact diameter_coord _ _ _ _
set_option maxRecDepth 15000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 3 ∧ HasPathAtMostThree (0 : Vertex) 3 := by decide
private lemma semantic_distance_coord (r s : Fin 13) (c d : Fin 3) :
    D (coordVertex r c) (coordVertex s d) = Dcert (coordVertex r c) (coordVertex s d) := by
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
theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j; rw [← coordVertex_surj i, ← coordVertex_surj j]; exact semantic_distance_coord _ _ _ _
end Wow284.Induced39
