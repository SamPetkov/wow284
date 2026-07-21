#!/usr/bin/env python3
"""Run the exact combinatorial and symbolic WOW-284 verification."""

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

from wow284_graph import (  # noqa: E402
    VERTEX_COUNT,
    adjacency_list,
    adjacency_matrix,
    all_pairs_distances,
    structural_certificate,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify() -> dict[str, object]:
    """Return a JSON-serializable exact certificate or raise on failure."""

    structure = structural_certificate()
    graph = adjacency_list()
    a = sp.Matrix(adjacency_matrix(graph))
    d = sp.Matrix(all_pairs_distances(graph))
    identity = sp.eye(VERTEX_COUNT)
    ones = sp.ones(VERTEX_COUNT)

    if a * a != 6 * identity - a + ones:
        raise AssertionError("A^2 = 6I - A + J failed")
    if d != 2 * ones - 2 * identity - a:
        raise AssertionError("D = 2J - 2I - A failed")
    if d != -14 * identity + a + 2 * a * a:
        raise AssertionError("D = -14I + A + 2A^2 failed")

    x = sp.symbols("x")
    adjacency_polynomial = sp.factor(a.charpoly(x).as_expr())
    expected_adjacency = (x - 7) * (x - 2) ** 28 * (x + 3) ** 21
    if sp.expand(adjacency_polynomial - expected_adjacency) != 0:
        raise AssertionError(f"unexpected adjacency polynomial: {adjacency_polynomial}")

    distance_polynomial = sp.factor(d.charpoly(x).as_expr())
    expected_distance = (x - 91) * (x - 1) ** 21 * (x + 4) ** 28
    if sp.expand(distance_polynomial - expected_distance) != 0:
        raise AssertionError(f"unexpected distance polynomial: {distance_polynomial}")

    shifted = d + 7 * identity
    lower, diagonal = shifted.LDLdecomposition(hermitian=True)
    if lower * diagonal * lower.T != shifted:
        raise AssertionError("exact LDL^T reconstruction failed")
    pivots = [sp.factor(diagonal[i, i]) for i in range(VERTEX_COUNT)]
    if not all(bool(pivot > 0) for pivot in pivots):
        raise AssertionError("D + 7I has a nonpositive LDL pivot")

    source_paths = [
        ROOT / "src" / "wow284_graph.py",
        ROOT / "scripts" / "verify_exact.py",
    ]
    return {
        "certificate_version": 1,
        "manuscript_version": "2026-07-19",
        "graph": structure,
        "matrix_identities": {
            "adjacency_square": "A^2 = 6I - A + J",
            "distance_from_adjacency": "D = 2J - 2I - A",
            "published_cage_formula_specialization": "D = -14I + A + 2A^2",
        },
        "spectra": {
            "adjacency_characteristic_polynomial": str(adjacency_polynomial),
            "adjacency_spectrum": {"7": 1, "2": 28, "-3": 21},
            "distance_characteristic_polynomial": str(distance_polynomial),
            "distance_spectrum": {"91": 1, "1": 21, "-4": 28},
            "least_distance_eigenvalue": -4,
        },
        "wow284": {
            "minimum_dual_degree": 7,
            "negative_least_distance_eigenvalue": 4,
            "strict_gap": 3,
            "counterexample": True,
        },
        "positive_definiteness": {
            "matrix": "D + 7I",
            "ldl_pivot_count": len(pivots),
            "minimum_ldl_pivot": str(min(pivots)),
            "all_pivots_positive": True,
        },
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
        print("WOW-284 exact verification: PASS")
        print("vertices=50 edges=175 degree=7 girth=5 diameter=2")
        print("adjacency charpoly: (x - 7)*(x - 2)^28*(x + 3)^21")
        print("distance charpoly: (x - 91)*(x - 1)^21*(x + 4)^28")
        print("minimum dual degree=7; least distance eigenvalue=-4; strict gap=3")
        print("D + 7I: 50 positive rational LDL pivots")


if __name__ == "__main__":
    main()
