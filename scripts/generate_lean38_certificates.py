#!/usr/bin/env python3
"""Generate exact finite data and Lean skeleton support for the 38-vertex graph.

The generated finite structural modules use bounded `decide` goals.  The
positive-definiteness data use Sylvester's criterion: the 38 exact leading
principal determinants of 3D+17I are emitted both as JSON and as Lean data.
The remaining generic theorem connecting those determinants to positive
definiteness is intentionally left in a non-imported `.lean.template` file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import distance_matrix, graph38  # noqa: E402

LEAN_DIR = ROOT / "lean" / "Wow284" / "Induced38"
DATA_DIR = ROOT / "data"


def lean_int_matrix(name: str, matrix: sp.Matrix) -> str:
    rows: list[str] = []
    for i in range(matrix.rows):
        entries: list[str] = []
        for j in range(matrix.cols):
            value = sp.Rational(matrix[i, j])
            if value.q != 1:
                raise AssertionError(f"{name}[{i},{j}] is not integral")
            entries.append(str(int(value)))
        rows.append(", ".join(entries))
    return f"def {name} : Matrix Vertex Vertex ℤ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def render() -> dict[Path, str]:
    graph, labels = graph38()
    degrees = [len(graph[v]) for v in range(len(graph))]
    neighbor_degree_sums = [
        sum(degrees[u] for u in graph[v]) for v in range(len(graph))
    ]
    if not all(17 * degrees[v] <= 3 * neighbor_degree_sums[v] for v in range(len(graph))):
        raise AssertionError("dual-degree cross-multiplication certificate failed")
    if (degrees[1], neighbor_degree_sums[1]) != (6, 34):
        raise AssertionError("unexpected attaining-vertex data")
    d = distance_matrix(graph)
    shifted = 3 * d + 17 * sp.eye(38)
    leading = [int(shifted[:k, :k].det(method="domain-ge")) for k in range(1, 39)]
    if not all(value > 0 for value in leading):
        raise AssertionError("nonpositive leading principal determinant")

    data = {
        "order": 38,
        "shifted_matrix": "3D+17I",
        "vertex_labels": [list(label) for label in labels],
        "leading_principal_determinants": leading,
        "determinant": leading[-1],
        "all_positive": True,
    }

    definitions = f'''import Wow284.Induced38.Basic

/-!
Exact generated matrix and Sylvester-certificate data for the 38-vertex graph.
-/

namespace Wow284.Induced38

open Matrix

{lean_int_matrix("Dcert", d)}
def shiftedCert : Matrix Vertex Vertex ℤ :=
  (3 : ℤ) • Dcert + (17 : ℤ) • (1 : Matrix Vertex Vertex ℤ)

def leadingPrincipalExpected : Fin 38 → ℤ := ![
  {", ".join(str(v) for v in leading)}
]

theorem leadingPrincipalExpected_positive (i : Fin 38) :
    0 < leadingPrincipalExpected i := by
  fin_cases i <;> norm_num [leadingPrincipalExpected]

end Wow284.Induced38
'''

    outputs: dict[Path, str] = {
        DATA_DIR / "thirty_eight_sylvester.json": json.dumps(data, indent=2, sort_keys=True) + "\n",
        LEAN_DIR / "CertificateDefinitions.lean": definitions,
    }

    for r in range(19):
        parts = [
            "import Wow284.Induced38.CertificateDefinitions\n",
            "/-! Generated bounded finite certificate shard. -/\n",
            "namespace Wow284.Induced38\n\n",
            f'''set_option maxRecDepth 10000 in
lemma degree_range_row_{r} : ∀ c : Fin 2,
    degree (coordVertex {r} c) = 5 ∨ degree (coordVertex {r} c) = 6 := by
  intro c
  fin_cases c <;> decide

set_option maxRecDepth 10000 in
lemma dual_cross_bound_row_{r} : ∀ c : Fin 2,
    17 * degree (coordVertex {r} c) ≤
      3 * neighborDegreeSum (coordVertex {r} c) := by
  intro c
  fin_cases c <;> decide
''',
        ]
        for s in range(19):
            parts += [
                f'''set_option maxRecDepth 10000 in
lemma diameter_rows_{r}_{s} : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex {r} c) (coordVertex {s} d) := by
  decide
''',
                f'''set_option maxRecDepth 10000 in
lemma semantic_distance_rows_{r}_{s} : ∀ c d : Fin 2,
    D (coordVertex {r} c) (coordVertex {s} d) =
      Dcert (coordVertex {r} c) (coordVertex {s} d) := by
  decide
''',
            ]
        parts.append("\nend Wow284.Induced38\n")
        outputs[LEAN_DIR / f"Finite{r}.lean"] = "\n".join(parts)

    imports = "\n".join(f"import Wow284.Induced38.Finite{r}" for r in range(19))
    degree_cases = "\n".join(f"  · exact degree_range_row_{r} c" for r in range(19))
    dual_cases = "\n".join(f"  · exact dual_cross_bound_row_{r} c" for r in range(19))
    diameter_cases = "\n".join(f"  · exact diameter_row_{r} s c d" for r in range(19))
    semantic_cases = "\n".join(f"  · exact semantic_distance_row_{r} s c d" for r in range(19))
    row_assemblers: list[str] = []
    for r in range(19):
        row_assemblers += [
            f'''private lemma diameter_row_{r} (s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''
            + "\n".join(f"  · exact diameter_rows_{r}_{s} c d" for s in range(19))
            + "\n",
            f'''private lemma semantic_distance_row_{r} (s : Fin 19) (c d : Fin 2) :
    D (coordVertex {r} c) (coordVertex s d) =
      Dcert (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''
            + "\n".join(f"  · exact semantic_distance_rows_{r}_{s} c d" for s in range(19))
            + "\n",
        ]

    outputs[LEAN_DIR / "FiniteCertificates.lean"] = f'''{imports}

/-! Assembly of exact finite certificates for the 38-vertex graph. -/
namespace Wow284.Induced38

private lemma degree_range_coord (r : Fin 19) (c : Fin 2) :
    degree (coordVertex r c) = 5 ∨ degree (coordVertex r c) = 6 := by
  fin_cases r
{degree_cases}

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
{dual_cases}

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

{''.join(row_assemblers)}
private lemma diameter_coord (r s : Fin 19) (c d : Fin 2) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{diameter_cases}

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
{semantic_cases}

theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact semantic_distance_coord _ _ _ _

end Wow284.Induced38
'''

    outputs[LEAN_DIR / "PositiveDefiniteSkeleton.lean.template"] = '''import Wow284.Induced38.FiniteCertificates

/-!
NON-IMPORTED SKELETON.

Target: connect the generated list of 38 positive leading principal minors to
`Matrix.PosDef` (or an equivalent quadratic-form predicate) by Sylvester's
criterion.  The exact values are in `leadingPrincipalExpected`; Python checks
that each is the determinant of the corresponding leading principal submatrix
of `shiftedCert = 3D+17I`.
-/

namespace Wow284.Induced38

-- Suggested obligations:
-- 1. define the `k` by `k` leading principal submatrix of `shiftedCert`;
-- 2. prove its determinant equals `leadingPrincipalExpected ⟨k-1,...⟩`;
-- 3. apply a Sylvester-criterion lemma, or prove the criterion once;
-- 4. transfer along `semantic_distance_eq_Dcert`;
-- 5. conclude every eigenvalue of `D` is greater than `-17/3`.

-- theorem shiftedCert_posDef : Matrix.PosDef (shiftedCert.map (Int.castRingHom ℚ)) := by
--   ...

end Wow284.Induced38
'''
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = render()
    if args.check:
        stale = [p for p, c in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != c]
        if stale:
            raise SystemExit("stale files: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
        print(f"38-vertex Lean/Sylvester data: PASS ({len(outputs)} files)")
        return
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
