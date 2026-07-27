import Wow284.Basic

/-!
# The explicit 42-vertex WOW-284 counterexample

The graph is an induced subgraph of a previously verified coordinate graph.
Simplicity and exclusion of triangles and 4-cycles are inherited. Generated
finite certificates prove the degree data, diameter three, and semantic BFS
distance matrix; denominator-cleared integer LDL data prove the strict spectral
inequality.
-/
namespace Wow284.Induced42
open scoped BigOperators
abbrev Vertex := Fin 42

/-- Old Hoffman--Singleton labels retained after deleting `P_(0,0)`
and its seven neighbours: `0, 1, 4, 25, 30, 35, 40, 45`. -/
def embed : Vertex → Wow284.Vertex :=
  ![2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]

set_option maxRecDepth 10000 in
lemma embed_injective : Function.Injective embed := by
  decide

lemma embed_ne {u v : Vertex} (h : u ≠ v) : embed u ≠ embed v :=
  fun huv => h (embed_injective huv)

def Adjacent (u v : Vertex) : Prop := Wow284.Adjacent (embed u) (embed v)
instance (u v : Vertex) : Decidable (Adjacent u v) := by unfold Adjacent; infer_instance
lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using Wow284.adjacent_symm (embed u) (embed v)
lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using Wow284.adjacent_irrefl (embed v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card
def neighborDegreeSum (v : Vertex) : Nat := ∑ u ∈ neighbors v, degree u
def dualDegree (v : Vertex) : ℚ :=
  (neighborDegreeSum v : ℚ) / (degree v : ℚ)

def coordVertex (r : Fin 7) (c : Fin 6) : Vertex :=
  ⟨6 * r.val + c.val, by omega⟩
lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 6, by omega⟩
      ⟨v.val % 6, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext; simp [coordVertex]; omega

theorem no_triangle : ∀ a b c : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro u v w h
  rcases h with ⟨huv, huw, hvw, euv, evw, ewu⟩
  apply Wow284.no_triangle (embed u) (embed v) (embed w)
  exact ⟨embed_ne huv, embed_ne huw, embed_ne hvw, euv, evw, ewu⟩

theorem no_four_cycle : ∀ a b c d : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro u v w z h
  rcases h with ⟨huv, huw, huz, hvw, hvz, hwz, euv, evw, ewz, ezu⟩
  apply Wow284.no_four_cycle (embed u) (embed v) (embed w) (embed z)
  exact ⟨embed_ne huv, embed_ne huw, embed_ne huz, embed_ne hvw, embed_ne hvz, embed_ne hwz,
    euv, evw, ewz, ezu⟩

theorem explicit_five_cycle :
    Adjacent (2 : Vertex) 3 ∧ Adjacent (3 : Vertex) 4 ∧
    Adjacent (4 : Vertex) 5 ∧ Adjacent (5 : Vertex) 6 ∧
    Adjacent (6 : Vertex) 2 := by decide

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
end Wow284.Induced42
