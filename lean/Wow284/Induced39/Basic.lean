import Wow284.Induced40.Basic

/-!
# The explicit 39-vertex WOW-284 counterexample

The graph is an induced subgraph of a previously verified coordinate graph.
Simplicity and exclusion of triangles and 4-cycles are inherited. Generated
finite certificates prove the degree data, diameter three, and semantic BFS
distance matrix; denominator-cleared integer LDL data prove the strict spectral
inequality.
-/
namespace Wow284.Induced39
open scoped BigOperators
abbrev Vertex := Fin 39

def embed40 (v : Vertex) : Wow284.Induced40.Vertex :=
  ⟨v.val + 1, by omega⟩

lemma embed40_injective : Function.Injective embed40 := by
  intro u v h
  apply Fin.ext
  simpa [embed40] using congrArg Fin.val h

lemma embed40_ne {u v : Vertex} (h : u ≠ v) : embed40 u ≠ embed40 v :=
  fun huv => h (embed40_injective huv)

def Adjacent (u v : Vertex) : Prop := Wow284.Induced40.Adjacent (embed40 u) (embed40 v)
instance (u v : Vertex) : Decidable (Adjacent u v) := by unfold Adjacent; infer_instance
lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using Wow284.Induced40.adjacent_symm (embed40 u) (embed40 v)
lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using Wow284.Induced40.adjacent_irrefl (embed40 v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card
def neighborDegreeSum (v : Vertex) : Nat := ∑ u ∈ neighbors v, degree u
def dualDegree (v : Vertex) : ℚ :=
  (neighborDegreeSum v : ℚ) / (degree v : ℚ)

def coordVertex (r : Fin 13) (c : Fin 3) : Vertex :=
  ⟨3 * r.val + c.val, by omega⟩
lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 3, by omega⟩
      ⟨v.val % 3, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext; simp [coordVertex]; omega

theorem no_triangle : ∀ a b c : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro u v w h
  rcases h with ⟨huv, huw, hvw, euv, evw, ewu⟩
  apply Wow284.Induced40.no_triangle (embed40 u) (embed40 v) (embed40 w)
  exact ⟨embed40_ne huv, embed40_ne huw, embed40_ne hvw, euv, evw, ewu⟩

theorem no_four_cycle : ∀ a b c d : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro u v w z h
  rcases h with ⟨huv, huw, huz, hvw, hvz, hwz, euv, evw, ewz, ezu⟩
  apply Wow284.Induced40.no_four_cycle (embed40 u) (embed40 v) (embed40 w) (embed40 z)
  exact ⟨embed40_ne huv, embed40_ne huw, embed40_ne huz, embed40_ne hvw, embed40_ne hvz, embed40_ne hwz,
    euv, evw, ewz, ezu⟩

theorem explicit_five_cycle :
    Adjacent (4 : Vertex) 5 ∧ Adjacent (5 : Vertex) 6 ∧
    Adjacent (6 : Vertex) 7 ∧ Adjacent (7 : Vertex) 8 ∧
    Adjacent (8 : Vertex) 4 := by decide

def HasPathAtMostTwo (u v : Vertex) : Prop :=
  u = v ∨ Adjacent u v ∨ ∃ w, Adjacent u w ∧ Adjacent w v
def HasPathAtMostThree (u v : Vertex) : Prop :=
  HasPathAtMostTwo u v ∨ ∃ w z, Adjacent u w ∧ Adjacent w z ∧ Adjacent z v
instance (u v : Vertex) : Decidable (HasPathAtMostTwo u v) := by unfold HasPathAtMostTwo; infer_instance
instance (u v : Vertex) : Decidable (HasPathAtMostThree u v) := by unfold HasPathAtMostThree; infer_instance

open Matrix
def D : Matrix Vertex Vertex ℤ := fun u v =>
  if u = v then 0 else if Adjacent u v then 1
  else if ∃ w, Adjacent u w ∧ Adjacent w v then 2 else 3
end Wow284.Induced39
