#!/usr/bin/env python3
"""Generate sharded finite structural certificates for the 40-vertex graph.

The output mirrors the existing sharding strategy in SamPetkov/wow284.  Every
finite block goal is discharged with `decide`; the package does not claim a
kernel build until these files are copied into the Lean 4.31 repository and
`lake build` is run there.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEAN_DIR = ROOT / "lean" / "Wow284" / "Induced40"


def block_lemma(name: str, lhs: str, rhs: str, r: int, s: int) -> str:
    return f'''set_option maxRecDepth 10000 in
lemma {name}_rows_{r}_{s} : ∀ c d : Fin 5,
    ({lhs}) (coordVertex {r} c) (coordVertex {s} d) =
      ({rhs}) (coordVertex {r} c) (coordVertex {s} d) := by
  decide
'''


def path_block(r: int, s: int) -> str:
    return f'''set_option maxRecDepth 10000 in
lemma diameter_rows_{r}_{s} : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex {r} c) (coordVertex {s} d) := by
  decide
'''


def render() -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for r in range(8):
        parts = [
            "import Wow284.Induced40.DiagonalizationDefinitions\n",
            "/-! Generated bounded structural certificate shard. -/\n",
            "namespace Wow284.Induced40\n\n",
            f'''set_option maxRecDepth 10000 in
lemma degree_row_{r} : ∀ c : Fin 5, degree (coordVertex {r} c) = 6 := by
  decide
\n''',
        ]
        for s in range(8):
            parts.append(path_block(r, s))
            parts.append(
                block_lemma(
                    "semantic_distance",
                    "D",
                    "Dcert",
                    r,
                    s,
                )
            )
            parts.append(
                block_lemma(
                    "distance_polynomial_entry",
                    "D",
                    "(3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ) - (2 : ℤ) • A - A * A",
                    r,
                    s,
                )
            )
        parts.append("\nend Wow284.Induced40\n")
        outputs[LEAN_DIR / f"Structural{r}.lean"] = "\n".join(parts)

    imports = "\n".join(f"import Wow284.Induced40.Structural{r}" for r in range(8))
    degree_cases = "\n".join(f"  · exact degree_row_{r} c" for r in range(8))
    diameter_cases = "\n".join(f"  · exact diameter_row_{r} s c d" for r in range(8))
    semantic_cases = "\n".join(f"  · exact semantic_distance_row_{r} s c d" for r in range(8))
    polynomial_cases = "\n".join(f"  · exact distance_polynomial_entry_row_{r} s c d" for r in range(8))

    row_assemblers: list[str] = []
    for r in range(8):
        row_assemblers.append(
            f'''private lemma diameter_row_{r} (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''
            + "\n".join(f"  · exact diameter_rows_{r}_{s} c d" for s in range(8))
            + "\n"
        )
        row_assemblers.append(
            f'''private lemma semantic_distance_row_{r} (s : Fin 8) (c d : Fin 5) :
    D (coordVertex {r} c) (coordVertex s d) =
      Dcert (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''
            + "\n".join(f"  · exact semantic_distance_rows_{r}_{s} c d" for s in range(8))
            + "\n"
        )
        row_assemblers.append(
            f'''private lemma distance_polynomial_entry_row_{r} (s : Fin 8) (c d : Fin 5) :
    D (coordVertex {r} c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''
            + "\n".join(f"  · exact distance_polynomial_entry_rows_{r}_{s} c d" for s in range(8))
            + "\n"
        )

    outputs[LEAN_DIR / "Structural.lean"] = f'''{imports}

/-!
Assembly of the finite structural certificates for the induced 40-vertex graph.
-/

namespace Wow284.Induced40

open Matrix

private lemma degree_coord (r : Fin 8) (c : Fin 5) :
    degree (coordVertex r c) = 6 := by
  fin_cases r
{degree_cases}

theorem degree_six : ∀ v : Vertex, degree v = 6 := by
  intro v
  rw [← coordVertex_surj v]
  exact degree_coord _ _

{''.join(row_assemblers)}
private lemma diameter_coord (r s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{diameter_cases}

theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v
  rw [← coordVertex_surj u, ← coordVertex_surj v]
  exact diameter_coord _ _ _ _

set_option maxRecDepth 10000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 5 ∧ HasPathAtMostThree (0 : Vertex) 5 := by
  decide

private lemma semantic_distance_coord (r s : Fin 8) (c d : Fin 5) :
    D (coordVertex r c) (coordVertex s d) =
      Dcert (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{semantic_cases}

theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact semantic_distance_coord _ _ _ _

private lemma distance_polynomial_coord (r s : Fin 8) (c d : Fin 5) :
    D (coordVertex r c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{polynomial_cases}

theorem distance_polynomial :
    D = (3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
      - (2 : ℤ) • A - A * A := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact distance_polynomial_coord _ _ _ _

end Wow284.Induced40
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
        print(f"40-vertex structural Lean data: PASS ({len(outputs)} files)")
        return
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
