import Wow284.Induced40.Structural
import Wow284.Induced40.DiagonalizationData
import Wow284.Induced40.Gap

/-!
# Public spectral endpoint for the induced 40-vertex graph

This module packages the finite structural and matrix certificates into a
short public interface.  The exact diagonal form is for the cast of the
semantic graph-distance matrix, and the displayed diagonal multiplicities
therefore give its complete distance spectrum.
-/

namespace Wow284.Induced40

open Matrix
open scoped BigOperators

/-- Average degree of the neighbours of `v`. -/
def dualDegree (v : Vertex) : ℚ :=
  ((∑ u ∈ neighbors v, degree u : ℕ) : ℚ) / (degree v : ℚ)

/-- Regularity makes the dual degree identically six. -/
theorem dual_degree_six (v : Vertex) : dualDegree v = 6 := by
  have hdeg : degree v = 6 := degree_six v
  have hsum : (∑ u ∈ neighbors v, degree u : ℕ) = 36 := by
    calc
      (∑ u ∈ neighbors v, degree u : ℕ) =
          ∑ _u ∈ neighbors v, 6 := by
            apply Finset.sum_congr rfl
            intro u _hu
            exact degree_six u
      _ = (neighbors v).card * 6 := by simp
      _ = 36 := by simpa [degree] using congrArg (fun n : ℕ => n * 6) hdeg
  simp [dualDegree, hdeg, hsum]

/-- The matrix diagonalized by the finite certificate is the cast of the
semantic distance matrix, rather than merely an unrelated data matrix. -/
theorem semantic_distance_cast_eq_Dq : castMatrix D = Dq := by
  rw [semantic_distance_eq_Dcert]
  rfl

/-- Exact similarity of the rational semantic distance matrix to the
certificate's diagonal matrix. -/
theorem semantic_distance_exact_diagonal_form :
    eigenbasisInv * castMatrix D * eigenbasis = distanceDiagonal := by
  rw [semantic_distance_cast_eq_Dq]
  calc
    eigenbasisInv * Dq * eigenbasis =
        eigenbasisInv * (Dq * eigenbasis) := by rw [Matrix.mul_assoc]
    _ = eigenbasisInv * (eigenbasis * distanceDiagonal) := by
      rw [distance_diagonalization]
    _ = (eigenbasisInv * eigenbasis) * distanceDiagonal := by
      rw [Matrix.mul_assoc]
    _ = distanceDiagonal := by rw [eigenbasis_left_inverse, one_mul]

/-- Concise end-to-end certificate for the order-40 example.

The four diagonal counts sum to 40.  Together with the invertible change of
basis above, they state that the semantic distance spectrum is
`{-5^18, 0^16, 3^5, 75^1}`.  Hence the least distance eigenvalue is `-5`,
while the minimum dual degree is `6`, leaving the positive strict gap `1`.
-/
theorem counterexample_spectral_endpoint :
    (∀ v : Vertex, degree v = 6 ∧ dualDegree v = 6) ∧
    eigenbasisInv * castMatrix D * eigenbasis = distanceDiagonal ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = -5).card = 18 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 3).card = 5 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 0).card = 16 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 75).card = 1 ∧
    (0 : ℚ) < (6 : ℚ) + (-5) := by
  refine ⟨?_, semantic_distance_exact_diagonal_form, ?_⟩
  · intro v
    exact ⟨degree_six v, dual_degree_six v⟩
  · exact ⟨distance_diagonal_counts.1,
      distance_diagonal_counts.2.1,
      distance_diagonal_counts.2.2.1,
      distance_diagonal_counts.2.2.2,
      exact_wow_gap_positive⟩

end Wow284.Induced40
