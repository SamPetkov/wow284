import Wow284.Induced40.SpectralEndpoint

/-!
# End-to-end counterexample certificate for the induced 40-vertex graph

The existing generated data give an invertible rational eigenbasis and an exact
diagonalization of the semantic distance matrix.  This module packages those
facts with a pointwise certificate that the diagonal minimum is `-5` and with
the exact dual-degree calculation.
-/

namespace Wow284.Induced40

open Matrix

/-- Every diagonal entry in the exact distance diagonalization is one of the
four displayed spectral values. -/
theorem distance_diagonal_entry_cases (j : Vertex) :
    distanceDiagonalInt j j = -5 ∨
    distanceDiagonalInt j j = 0 ∨
    distanceDiagonalInt j j = 3 ∨
    distanceDiagonalInt j j = 75 := by
  set_option maxRecDepth 10000 in
    fin_cases j <;> decide

/-- The minimum entry of the exact diagonal form is `-5`, and it is attained. -/
theorem distance_diagonal_minimum_certificate :
    (∀ j : Vertex, (-5 : ℤ) ≤ distanceDiagonalInt j j) ∧
      ∃ j : Vertex, distanceDiagonalInt j j = -5 := by
  constructor
  · intro j
    rcases distance_diagonal_entry_cases j with h | h | h | h <;> omega
  · have hcard := distance_diagonal_counts.1
    have hpos :
        0 < (Finset.univ.filter fun j : Vertex =>
          distanceDiagonalInt j j = -5).card := by
      rw [hcard]
      norm_num
    rcases Finset.card_pos.mp hpos with ⟨j, hj⟩
    exact ⟨j, (Finset.mem_filter.mp hj).2⟩

/-- Precisely scoped spectral certificate: the semantic distance matrix is
similar, through a two-sided invertible rational change of basis, to the
displayed diagonal matrix, whose least diagonal entry is the attained value
`-5`.  This theorem deliberately states the exact finite diagonalization
certificate rather than invoking a separate generic `λ_min` API. -/
theorem exact_distance_diagonalization_minimum_certificate :
    eigenbasisInv * eigenbasis = (1 : Matrix Vertex Vertex ℚ) ∧
    eigenbasis * eigenbasisInv = (1 : Matrix Vertex Vertex ℚ) ∧
    eigenbasisInv * castMatrix D * eigenbasis = distanceDiagonal ∧
    (∀ j : Vertex, (-5 : ℤ) ≤ distanceDiagonalInt j j) ∧
    ∃ j : Vertex, distanceDiagonalInt j j = -5 := by
  exact ⟨eigenbasis_left_inverse, eigenbasis_right_inverse,
    semantic_distance_exact_diagonal_form,
    distance_diagonal_minimum_certificate.1,
    distance_diagonal_minimum_certificate.2⟩

/-- Public end-to-end certificate for the order-40 counterexample.  It records
both inverse identities for the change of basis, the exact minimum of the
resulting diagonal form, and the previously assembled structural/spectral
endpoint with strict gap `6 + (-5) = 1`. -/
theorem exact_counterexample_certificate :
    eigenbasisInv * eigenbasis = (1 : Matrix Vertex Vertex ℚ) ∧
    eigenbasis * eigenbasisInv = (1 : Matrix Vertex Vertex ℚ) ∧
    (∀ j : Vertex, (-5 : ℤ) ≤ distanceDiagonalInt j j) ∧
    (∃ j : Vertex, distanceDiagonalInt j j = -5) ∧
    ((∀ v : Vertex, degree v = 6 ∧ dualDegree v = 6) ∧
      eigenbasisInv * castMatrix D * eigenbasis = distanceDiagonal ∧
      (Finset.univ.filter fun j : Vertex =>
        distanceDiagonalInt j j = -5).card = 18 ∧
      (Finset.univ.filter fun j : Vertex =>
        distanceDiagonalInt j j = 3).card = 5 ∧
      (Finset.univ.filter fun j : Vertex =>
        distanceDiagonalInt j j = 0).card = 16 ∧
      (Finset.univ.filter fun j : Vertex =>
        distanceDiagonalInt j j = 75).card = 1 ∧
      (0 : ℚ) < (6 : ℚ) + (-5)) := by
  exact ⟨eigenbasis_left_inverse, eigenbasis_right_inverse,
    distance_diagonal_minimum_certificate.1,
    distance_diagonal_minimum_certificate.2,
    counterexample_spectral_endpoint⟩

end Wow284.Induced40
