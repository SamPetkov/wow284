import Wow284.Induced40.Basic

/-!
# The 38-vertex edge-deletion counterexample

Delete vertices 0 and 1 (the adjacent pair `P_(1,0),P_(1,1)`) from the
40-vertex graph.  The exact finite degree, distance, and dual-degree
certificates are generated separately.
-/

namespace Wow284.Induced38

abbrev Vertex := Fin 38

def embed40 (v : Vertex) : Wow284.Induced40.Vertex := ⟨v.val + 2, by omega⟩

lemma embed40_injective : Function.Injective embed40 := by
  intro u v h
  apply Fin.ext
  simpa [embed40] using congrArg Fin.val h

lemma embed40_ne {u v : Vertex} (h : u ≠ v) : embed40 u ≠ embed40 v :=
  fun huv => h (embed40_injective huv)

def Adjacent (u v : Vertex) : Prop :=
  Wow284.Induced40.Adjacent (embed40 u) (embed40 v)

instance (u v : Vertex) : Decidable (Adjacent u v) := by
  unfold Adjacent
  infer_instance

lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using Wow284.Induced40.adjacent_symm (embed40 u) (embed40 v)

lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using Wow284.Induced40.adjacent_irrefl (embed40 v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card

def dualDegree (v : Vertex) : ℚ :=
  ((∑ u in neighbors v, degree u : ℕ) : ℚ) / (degree v : ℚ)

/-- Nineteen rows of two vertices, used by generated bounded certificates. -/
def coordVertex (r : Fin 19) (c : Fin 2) : Vertex :=
  ⟨2 * r.val + c.val, by omega⟩

lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 2, by omega⟩
      ⟨v.val % 2, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext
  simp [coordVertex]
  omega

/-- Induced subgraphs inherit the triangle exclusion. -/
theorem no_triangle :
    ∀ a b c : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro a b c h
  rcases h with ⟨hab, hac, hbc, eab, ebc, eca⟩
  apply Wow284.Induced40.no_triangle (embed40 a) (embed40 b) (embed40 c)
  exact ⟨embed40_ne hab, embed40_ne hac, embed40_ne hbc, eab, ebc, eca⟩

/-- Induced subgraphs inherit the four-cycle exclusion. -/
theorem no_four_cycle :
    ∀ a b c d : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro a b c d h
  rcases h with ⟨hab, hac, had, hbc, hbd, hcd, eab, ebc, ecd, eda⟩
  apply Wow284.Induced40.no_four_cycle
    (embed40 a) (embed40 b) (embed40 c) (embed40 d)
  exact ⟨embed40_ne hab, embed40_ne hac, embed40_ne had, embed40_ne hbc,
    embed40_ne hbd, embed40_ne hcd, eab, ebc, ecd, eda⟩

/-- Vertices 3,...,7 are the surviving `P_(2,*)` five-cycle. -/
theorem explicit_five_cycle :
    Adjacent (3 : Vertex) 4 ∧ Adjacent (4 : Vertex) 5 ∧
    Adjacent (5 : Vertex) 6 ∧ Adjacent (6 : Vertex) 7 ∧
    Adjacent (7 : Vertex) 3 := by
  decide

def HasPathAtMostTwo (u v : Vertex) : Prop :=
  u = v ∨ Adjacent u v ∨ ∃ w, Adjacent u w ∧ Adjacent w v

def HasPathAtMostThree (u v : Vertex) : Prop :=
  HasPathAtMostTwo u v ∨
    ∃ w z, Adjacent u w ∧ Adjacent w z ∧ Adjacent z v

instance (u v : Vertex) : Decidable (HasPathAtMostTwo u v) := by
  unfold HasPathAtMostTwo
  infer_instance

instance (u v : Vertex) : Decidable (HasPathAtMostThree u v) := by
  unfold HasPathAtMostThree
  infer_instance

open Matrix

def D : Matrix Vertex Vertex ℤ := fun u v =>
  if u = v then 0
  else if Adjacent u v then 1
  else if ∃ w, Adjacent u w ∧ Adjacent w v then 2
  else 3

end Wow284.Induced38
