import Mathlib

/-!
# The finite graph underlying the WOW-284 counterexample

This file fixes the numerical labeling used by the paper and proves the
structural and matrix certificates by kernel-checked finite computation.
-/

namespace Wow284

abbrev Vertex := Fin 50

/-- Adjacency in the coordinate graph. Labels `5*i+j` represent `P_(i,j)`;
labels `25+5*k+l` represent `Q_(k,l)`. -/
def Adjacent (u v : Vertex) : Prop :=
  if u.val < 25 then
    let i := u.val / 5
    let j := u.val % 5
    if v.val < 25 then
      let i' := v.val / 5
      let j' := v.val % 5
      i = i' ∧ ((j + 1) % 5 = j' ∨ (j' + 1) % 5 = j)
    else
      let k := (v.val - 25) / 5
      let l := (v.val - 25) % 5
      l = (i * k + j) % 5
  else
    let k := (u.val - 25) / 5
    let l := (u.val - 25) % 5
    if v.val < 25 then
      let i := v.val / 5
      let j := v.val % 5
      l = (i * k + j) % 5
    else
      let k' := (v.val - 25) / 5
      let l' := (v.val - 25) % 5
      k = k' ∧ ((l + 2) % 5 = l' ∨ (l' + 2) % 5 = l)

instance (u v : Vertex) : Decidable (Adjacent u v) := by
  unfold Adjacent
  infer_instance

def neighbors (v : Vertex) : Finset Vertex :=
  Finset.univ.filter (Adjacent v)

def degree (v : Vertex) : Nat := (neighbors v).card

def commonNeighborCount (u v : Vertex) : Nat :=
  (Finset.univ.filter fun w => Adjacent u w ∧ Adjacent v w).card

theorem adjacent_irrefl : ∀ v : Vertex, ¬Adjacent v v := by
  intro v
  simp only [Adjacent]
  split <;> omega

theorem adjacent_symm : ∀ u v : Vertex, Adjacent u v ↔ Adjacent v u := by
  intro u v
  simp only [Adjacent]
  split <;> split <;> omega

def coordVertex (r : Fin 10) (c : Fin 5) : Vertex :=
  ⟨5 * r.val + c.val, by omega⟩

lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 5, by omega⟩ ⟨v.val % 5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext
  simp [coordVertex]
  omega

private lemma degree_row_0 : ∀ c : Fin 5, degree (coordVertex 0 c) = 7 := by
  decide

private lemma degree_row_1 : ∀ c : Fin 5, degree (coordVertex 1 c) = 7 := by
  decide

private lemma degree_row_2 : ∀ c : Fin 5, degree (coordVertex 2 c) = 7 := by
  decide

private lemma degree_row_3 : ∀ c : Fin 5, degree (coordVertex 3 c) = 7 := by
  decide

private lemma degree_row_4 : ∀ c : Fin 5, degree (coordVertex 4 c) = 7 := by
  decide

private lemma degree_row_5 : ∀ c : Fin 5, degree (coordVertex 5 c) = 7 := by
  decide

private lemma degree_row_6 : ∀ c : Fin 5, degree (coordVertex 6 c) = 7 := by
  decide

private lemma degree_row_7 : ∀ c : Fin 5, degree (coordVertex 7 c) = 7 := by
  decide

private lemma degree_row_8 : ∀ c : Fin 5, degree (coordVertex 8 c) = 7 := by
  decide

private lemma degree_row_9 : ∀ c : Fin 5, degree (coordVertex 9 c) = 7 := by
  decide

private lemma degree_coord (r : Fin 10) (c : Fin 5) : degree (coordVertex r c) = 7 := by
  have hrlt : r.val < 10 := r.isLt
  interval_cases hr : r.val
  · have er : r = 0 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_0 c
  · have er : r = 1 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_1 c
  · have er : r = 2 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_2 c
  · have er : r = 3 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_3 c
  · have er : r = 4 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_4 c
  · have er : r = 5 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_5 c
  · have er : r = 6 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_6 c
  · have er : r = 7 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_7 c
  · have er : r = 8 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_8 c
  · have er : r = 9 := Fin.ext (by exact hr)
    rw [er]
    exact degree_row_9 c

theorem degree_seven : ∀ v : Vertex, degree v = 7 := by
  intro v
  rw [← coordVertex_surj v]
  exact degree_coord _ _

private lemma common_rows_0_0 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 0 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_0_1 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 0 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_0_2 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 0 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_0_3 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 0 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_0_4 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 0 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_0_5 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 0 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_0_6 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 0 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_0_7 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 0 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_0_8 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 0 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_0_9 : ∀ c d : Fin 5, coordVertex 0 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 0 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 0 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 0 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_1_0 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 1 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_1_1 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 1 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_1_2 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 1 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_1_3 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 1 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_1_4 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 1 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_1_5 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 1 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_1_6 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 1 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_1_7 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 1 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_1_8 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 1 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_1_9 : ∀ c d : Fin 5, coordVertex 1 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 1 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 1 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 1 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_2_0 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 2 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_2_1 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 2 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_2_2 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 2 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_2_3 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 2 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_2_4 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 2 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_2_5 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 2 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_2_6 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 2 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_2_7 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 2 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_2_8 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 2 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_2_9 : ∀ c d : Fin 5, coordVertex 2 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 2 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 2 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 2 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_3_0 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 3 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_3_1 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 3 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_3_2 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 3 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_3_3 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 3 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_3_4 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 3 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_3_5 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 3 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_3_6 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 3 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_3_7 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 3 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_3_8 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 3 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_3_9 : ∀ c d : Fin 5, coordVertex 3 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 3 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 3 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 3 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_4_0 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 4 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_4_1 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 4 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_4_2 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 4 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_4_3 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 4 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_4_4 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 4 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_4_5 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 4 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_4_6 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 4 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_4_7 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 4 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_4_8 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 4 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_4_9 : ∀ c d : Fin 5, coordVertex 4 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 4 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 4 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 4 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_5_0 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 5 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_5_1 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 5 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_5_2 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 5 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_5_3 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 5 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_5_4 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 5 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_5_5 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 5 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_5_6 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 5 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_5_7 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 5 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_5_8 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 5 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_5_9 : ∀ c d : Fin 5, coordVertex 5 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 5 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 5 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 5 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_6_0 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 6 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_6_1 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 6 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_6_2 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 6 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_6_3 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 6 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_6_4 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 6 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_6_5 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 6 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_6_6 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 6 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_6_7 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 6 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_6_8 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 6 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_6_9 : ∀ c d : Fin 5, coordVertex 6 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 6 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 6 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 6 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_7_0 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 7 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_7_1 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 7 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_7_2 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 7 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_7_3 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 7 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_7_4 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 7 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_7_5 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 7 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_7_6 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 7 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_7_7 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 7 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_7_8 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 7 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_7_9 : ∀ c d : Fin 5, coordVertex 7 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 7 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 7 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 7 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_8_0 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 8 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_8_1 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 8 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_8_2 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 8 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_8_3 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 8 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_8_4 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 8 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_8_5 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 8 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_8_6 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 8 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_8_7 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 8 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_8_8 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 8 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_8_9 : ∀ c d : Fin 5, coordVertex 8 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 8 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 8 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 8 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_rows_9_0 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 0 d →
    if Adjacent (coordVertex 9 c) (coordVertex 0 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 0 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 0 d) = 1 := by
  decide

private lemma common_rows_9_1 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 1 d →
    if Adjacent (coordVertex 9 c) (coordVertex 1 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 1 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 1 d) = 1 := by
  decide

private lemma common_rows_9_2 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 2 d →
    if Adjacent (coordVertex 9 c) (coordVertex 2 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 2 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 2 d) = 1 := by
  decide

private lemma common_rows_9_3 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 3 d →
    if Adjacent (coordVertex 9 c) (coordVertex 3 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 3 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 3 d) = 1 := by
  decide

private lemma common_rows_9_4 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 4 d →
    if Adjacent (coordVertex 9 c) (coordVertex 4 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 4 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 4 d) = 1 := by
  decide

private lemma common_rows_9_5 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 5 d →
    if Adjacent (coordVertex 9 c) (coordVertex 5 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 5 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 5 d) = 1 := by
  decide

private lemma common_rows_9_6 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 6 d →
    if Adjacent (coordVertex 9 c) (coordVertex 6 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 6 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 6 d) = 1 := by
  decide

private lemma common_rows_9_7 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 7 d →
    if Adjacent (coordVertex 9 c) (coordVertex 7 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 7 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 7 d) = 1 := by
  decide

private lemma common_rows_9_8 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 8 d →
    if Adjacent (coordVertex 9 c) (coordVertex 8 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 8 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 8 d) = 1 := by
  decide

private lemma common_rows_9_9 : ∀ c d : Fin 5, coordVertex 9 c ≠ coordVertex 9 d →
    if Adjacent (coordVertex 9 c) (coordVertex 9 d)
    then commonNeighborCount (coordVertex 9 c) (coordVertex 9 d) = 0
    else commonNeighborCount (coordVertex 9 c) (coordVertex 9 d) = 1 := by
  decide

private lemma common_coord (r t : Fin 10) (c d : Fin 5)
    (huv : coordVertex r c ≠ coordVertex t d) :
    if Adjacent (coordVertex r c) (coordVertex t d)
    then commonNeighborCount (coordVertex r c) (coordVertex t d) = 0
    else commonNeighborCount (coordVertex r c) (coordVertex t d) = 1 := by
  have hrlt : r.val < 10 := r.isLt
  have htlt : t.val < 10 := t.isLt
  interval_cases hr : r.val <;> interval_cases ht : t.val
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_0 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_1 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_2 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_3 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_4 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_5 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_6 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_7 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_8 c d huv
  · have er : r = 0 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_0_9 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_0 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_1 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_2 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_3 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_4 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_5 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_6 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_7 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_8 c d huv
  · have er : r = 1 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_1_9 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_0 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_1 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_2 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_3 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_4 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_5 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_6 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_7 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_8 c d huv
  · have er : r = 2 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_2_9 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_0 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_1 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_2 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_3 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_4 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_5 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_6 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_7 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_8 c d huv
  · have er : r = 3 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_3_9 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_0 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_1 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_2 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_3 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_4 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_5 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_6 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_7 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_8 c d huv
  · have er : r = 4 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_4_9 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_0 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_1 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_2 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_3 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_4 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_5 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_6 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_7 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_8 c d huv
  · have er : r = 5 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_5_9 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_0 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_1 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_2 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_3 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_4 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_5 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_6 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_7 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_8 c d huv
  · have er : r = 6 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_6_9 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_0 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_1 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_2 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_3 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_4 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_5 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_6 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_7 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_8 c d huv
  · have er : r = 7 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_7_9 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_0 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_1 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_2 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_3 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_4 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_5 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_6 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_7 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_8 c d huv
  · have er : r = 8 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_8_9 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 0 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_0 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 1 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_1 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 2 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_2 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 3 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_3 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 4 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_4 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 5 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_5 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 6 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_6 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 7 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_7 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 8 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_8 c d huv
  · have er : r = 9 := Fin.ext (by exact hr)
    have et : t = 9 := Fin.ext (by exact ht)
    subst r
    subst t
    exact common_rows_9_9 c d huv

theorem common_neighbor_certificate :
    ∀ u v : Vertex, u ≠ v →
      if Adjacent u v then commonNeighborCount u v = 0
      else commonNeighborCount u v = 1 := by
  intro u v huv
  rw [← coordVertex_surj u, ← coordVertex_surj v] at huv ⊢
  exact common_coord _ _ _ _ huv

theorem diameter_two_certificate :
    ∀ u v : Vertex, u ≠ v →
      Adjacent u v ∨ ∃ w : Vertex, Adjacent u w ∧ Adjacent v w := by
  intro u v huv
  by_cases hadj : Adjacent u v
  · exact Or.inl hadj
  · right
    have hcert := common_neighbor_certificate u v huv
    simp [hadj] at hcert
    let common := Finset.univ.filter fun w => Adjacent u w ∧ Adjacent v w
    have hnonempty : common.Nonempty := by
      apply Finset.card_pos.mp
      change 0 < commonNeighborCount u v
      omega
    rcases hnonempty with ⟨w, hw⟩
    exact ⟨w, (Finset.mem_filter.mp hw).2⟩

theorem no_triangle :
    ∀ a b c : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro a b c h
  rcases h with ⟨hab_ne, hac_ne, hbc_ne, hab, hbc, hca⟩
  have hac : Adjacent a c := (adjacent_symm c a).mp hca
  have hcert := common_neighbor_certificate a b hab_ne
  simp [hab] at hcert
  let common := Finset.univ.filter fun w => Adjacent a w ∧ Adjacent b w
  have hc_mem : c ∈ common := by simp [common, hac, hbc]
  have hpositive : 0 < common.card := Finset.card_pos.mpr ⟨c, hc_mem⟩
  change common.card = 0 at hcert
  omega

theorem no_four_cycle :
    ∀ a b c d : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro a b c d h
  rcases h with ⟨hab_ne, hac_ne, had_ne, hbc_ne, hbd_ne, hcd_ne,
    hab, hbc, hcd, hda⟩
  have hcb : Adjacent c b := (adjacent_symm b c).mp hbc
  have had : Adjacent a d := (adjacent_symm d a).mp hda
  let common := Finset.univ.filter fun w => Adjacent a w ∧ Adjacent c w
  have hpair : ({b, d} : Finset Vertex) ⊆ common := by
    intro w hw
    simp only [Finset.mem_insert, Finset.mem_singleton] at hw
    rcases hw with rfl | rfl
    · simp [common, hab, hcb]
    · simp [common, had, hcd]
  have htwo : 2 ≤ common.card := by
    rw [← Finset.card_pair hbd_ne]
    exact Finset.card_le_card hpair
  have hcert := common_neighbor_certificate a c hac_ne
  have hone : common.card ≤ 1 := by
    change commonNeighborCount a c ≤ 1
    split_ifs at hcert <;> omega
  omega

theorem explicit_five_cycle :
    Adjacent (0 : Vertex) 1 ∧ Adjacent (1 : Vertex) 2 ∧
    Adjacent (2 : Vertex) 3 ∧ Adjacent (3 : Vertex) 4 ∧
    Adjacent (4 : Vertex) 0 := by
  decide

open Matrix

def A : Matrix Vertex Vertex ℤ := fun u v => if Adjacent u v then 1 else 0

/-- The graph distance, justified by `diameter_two_certificate`. -/
def D : Matrix Vertex Vertex ℤ := fun u v =>
  if u = v then 0 else if Adjacent u v then 1 else 2

def J : Matrix Vertex Vertex ℤ := fun _ _ => 1

lemma adjacency_product_sum (u v : Vertex) :
    (∑ w, (if Adjacent u w then (1 : ℤ) else 0) *
      (if Adjacent w v then (1 : ℤ) else 0)) = commonNeighborCount u v := by
  rw [commonNeighborCount, ← Finset.sum_boole]
  apply Finset.sum_congr rfl
  intro w hw
  have hwv : Adjacent w v ↔ Adjacent v w := adjacent_symm w v
  by_cases huw : Adjacent u w <;> by_cases hvw : Adjacent v w <;>
    simp [huw, hvw, hwv]

theorem adjacency_square :
    A * A = (6 : ℤ) • (1 : Matrix Vertex Vertex ℤ) - A + J := by
  ext u v
  simp only [Matrix.mul_apply, A, J, Matrix.smul_apply, smul_eq_mul,
    Matrix.one_apply, Matrix.sub_apply, Matrix.add_apply]
  rw [adjacency_product_sum]
  by_cases huv : u = v
  · subst v
    have hcount : commonNeighborCount u u = degree u := by
      simp [commonNeighborCount, degree, neighbors]
    rw [hcount]
    simp [degree_seven, adjacent_irrefl]
  · have hcert := common_neighbor_certificate u v huv
    by_cases hadj : Adjacent u v <;> simp [huv, hadj] at hcert ⊢ <;> omega

theorem distance_formula :
    D = (2 : ℤ) • J - (2 : ℤ) • (1 : Matrix Vertex Vertex ℤ) - A := by
  ext u v
  simp only [D, J, A, Matrix.smul_apply, smul_eq_mul, Matrix.one_apply,
    Matrix.sub_apply]
  by_cases huv : u = v
  · subst v
    simp [adjacent_irrefl]
  · by_cases hadj : Adjacent u v <;> simp [huv, hadj]

end Wow284
