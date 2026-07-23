#!/usr/bin/env python3
"""Run the exact 40-vertex induced-counterexample verification."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from wow284_graph import adjacency_matrix  # noqa: E402
from wow284_induced40 import (  # noqa: E402
    DELETED_VERTICES,
    VERTEX_COUNT_40,
    adjacency_matrix_40,
    all_pairs_distances_40,
    induced_adjacency,
    structural_certificate_40,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify() -> dict[str, object]:
    """Return a JSON-serializable exact certificate or raise on failure."""

    structure = structural_certificate_40()
    graph, remaining_labels = induced_adjacency()
    a = sp.Matrix(adjacency_matrix_40(graph))
    d = sp.Matrix(all_pairs_distances_40(graph))
    identity = sp.eye(VERTEX_COUNT_40)
    ones = sp.ones(VERTEX_COUNT_40)

    if d != 3 * ones + 3 * identity - 2 * a - a * a:
        raise AssertionError("D = 3J + 3I - 2A - A^2 failed")

    x = sp.symbols("x")
    adjacency_polynomial = sp.factor(a.charpoly(x).as_expr())
    expected_adjacency = (
        (x - 6)
        * (x - 2) ** 18
        * (x - 1) ** 4
        * (x + 2) ** 5
        * (x + 3) ** 12
    )
    if sp.expand(adjacency_polynomial - expected_adjacency) != 0:
        raise AssertionError(f"unexpected adjacency polynomial: {adjacency_polynomial}")

    distance_polynomial = sp.factor(d.charpoly(x).as_expr())
    expected_distance = (x - 75) * (x - 3) ** 5 * x**16 * (x + 5) ** 18
    if sp.expand(distance_polynomial - expected_distance) != 0:
        raise AssertionError(f"unexpected distance polynomial: {distance_polynomial}")

    full_a = sp.Matrix(adjacency_matrix())
    removed = list(DELETED_VERTICES)
    retained = list(remaining_labels)
    c = full_a.extract(retained, removed)
    petersen = full_a.extract(removed, removed)
    if c * sp.ones(10, 1) != sp.ones(40, 1):
        raise AssertionError("C*1_10 = 1_40 failed")
    if c.T * c != 4 * sp.eye(10):
        raise AssertionError("C^T*C = 4I failed")
    if a * c != c * (sp.ones(10) - sp.eye(10) - petersen):
        raise AssertionError("A*C = C*(J-I-P) failed")
    expected_petersen = (x - 3) * (x - 1) ** 5 * (x + 2) ** 4
    petersen_polynomial = sp.factor(petersen.charpoly(x).as_expr())
    if sp.expand(petersen_polynomial - expected_petersen) != 0:
        raise AssertionError(f"unexpected Petersen polynomial: {petersen_polynomial}")

    shifted = d + 6 * identity
    lower, diagonal = shifted.LDLdecomposition(hermitian=True)
    if lower * diagonal * lower.T != shifted:
        raise AssertionError("exact LDL^T reconstruction failed")
    pivots = [sp.factor(diagonal[i, i]) for i in range(VERTEX_COUNT_40)]
    if not all(bool(pivot > 0) for pivot in pivots):
        raise AssertionError("D + 6I has a nonpositive LDL pivot")

    source_paths = [
        ROOT / "src" / "wow284_graph.py",
        ROOT / "src" / "wow284_induced40.py",
        ROOT / "scripts" / "verify_40.py",
    ]
    return {
        "certificate_version": 1,
        "manuscript_version": "2026-07-23",
        "graph": structure,
        "matrix_identities": {
            "distance_from_adjacency": "D = 3J + 3I - 2A - A^2",
            "deleted_incidence_orthogonality": "C^T*C = 4I",
            "block_intertwining": "A*C = C*(J-I-P)",
        },
        "spectra": {
            "petersen_characteristic_polynomial": str(petersen_polynomial),
            "adjacency_characteristic_polynomial": str(adjacency_polynomial),
            "adjacency_spectrum": {"6": 1, "2": 18, "1": 4, "-2": 5, "-3": 12},
            "distance_characteristic_polynomial": str(distance_polynomial),
            "distance_spectrum": {"75": 1, "3": 5, "0": 16, "-5": 18},
            "least_distance_eigenvalue": -5,
        },
        "wow284": {
            "minimum_dual_degree": 6,
            "negative_least_distance_eigenvalue": 5,
            "strict_gap": 1,
            "counterexample": True,
        },
        "positive_definiteness": {
            "matrix": "D + 6I",
            "ldl_pivot_count": len(pivots),
            "minimum_ldl_pivot": str(min(pivots)),
            "all_pivots_positive": True,
        },
        "formalization_scope": "exact Python certificate; not currently Lean-formalized",
        "software": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
        },
        "source_sha256": {
            path.relative_to(ROOT).as_posix(): sha256(path) for path in source_paths
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the exact certificate as JSON")
    parser.add_argument("--quiet", action="store_true", help="suppress the human-readable summary")
    args = parser.parse_args()

    certificate = verify()
    serialized = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized, encoding="utf-8", newline="\n")
    if not args.quiet:
        print("40-vertex exact verification: PASS")
        print("vertices=40 edges=120 degree=6 girth=5 diameter=3")
        print("adjacency charpoly: (x - 6)*(x - 2)^18*(x - 1)^4*(x + 2)^5*(x + 3)^12")
        print("distance charpoly: (x - 75)*(x - 3)^5*x^16*(x + 5)^18")
        print("minimum dual degree=6; least distance eigenvalue=-5; strict gap=1")
        print("D + 6I: 40 positive rational LDL pivots")


if __name__ == "__main__":
    main()
