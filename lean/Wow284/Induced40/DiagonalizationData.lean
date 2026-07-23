import Wow284.Induced40.DiagonalizationLeft
import Wow284.Induced40.DiagonalizationDistance

namespace Wow284.Induced40

/-- The generated diagonal contains the complete distance spectrum. -/
theorem distance_diagonal_counts :
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = -5).card = 18 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 3).card = 5 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 0).card = 16 ∧
    (Finset.univ.filter fun j : Vertex => distanceDiagonalInt j j = 75).card = 1 := by
  decide

end Wow284.Induced40
