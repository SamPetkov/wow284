#!/usr/bin/env python3
"""Exact exhaustive checks inside the 40-vertex (6,5)-cage.

This script verifies every one of the 40 single-vertex deletions and every one
of the 120 edge-endpoint deletions.  It uses exact integer distance matrices,
exact rational dual degrees, exact characteristic polynomials, and exact Sturm
root counts.  The result is a finite exhaustive statement about these two
classes of induced descendants; it is not a minimality search over all graphs.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from verify_wow284_38_40_42 import (  # noqa: E402
    bfs_distances,
    dual_degrees,
    hoffman_singleton,
    induced,
)

X = sp.symbols("x")

P39 = sp.Poly(
    X**9
    * (X + 5) ** 12
    * (X**2 + 6 * X + 3)
    * (X**3 + 3 * X**2 - 15 * X - 7) ** 2
    * (X**3 + 3 * X**2 - 15 * X - 3) ** 2
    * (X**4 - 78 * X**3 + 303 * X**2 - 70 * X - 450),
    X,
)

P38 = sp.Poly(
    X**4
    * (X - 2)
    * (X + 5) ** 8
    * (X**2 + 6 * X + 2) ** 2
    * (X**3 + 3 * X**2 - 15 * X - 3)
    * (X**4 + 5 * X**3 - 7 * X**2 - 23 * X - 6)
    * (X**5 + 9 * X**4 + 7 * X**3 - 77 * X**2 - 54 * X - 4)
    * (
        X**9
        - 67 * X**8
        - 404 * X**7
        + 1772 * X**6
        + 7205 * X**5
        - 18489 * X**4
        - 17018 * X**3
        + 20288 * X**2
        + 16824 * X
        + 1680
    ),
    X,
)


def cage40():
    full, labels = hoffman_singleton()
    deleted = {("P", 0, j) for j in range(5)} | {("Q", 0, j) for j in range(5)}
    return induced(full, labels, deleted)


def delete_indices(graph, deleted: set[int]):
    keep = [v for v in range(len(graph)) if v not in deleted]
    index = {old: new for new, old in enumerate(keep)}
    return tuple(
        frozenset(index[w] for w in graph[v] if w in index)
        for v in keep
    )


def exact_charpoly(graph) -> sp.Poly:
    return sp.Poly(sp.Matrix(bfs_distances(graph)).charpoly(X).as_expr(), X)


def check_family() -> None:
    graph, labels = cage40()

    for vertex in range(40):
        descendant = delete_indices(graph, {vertex})
        assert min(dual_degrees(descendant)) == Fraction(35, 6)
        assert exact_charpoly(descendant) == P39

    # Since every distance matrix is real symmetric and has P39 as its exact
    # characteristic polynomial, this one exact Sturm count applies to all 40.
    assert P39.count_roots(-sp.oo, -sp.Rational(35, 6)) == 0
    assert P39.eval(-sp.Rational(35, 6)) != 0

    edges = [(u, v) for u in range(40) for v in graph[u] if u < v]
    assert len(edges) == 120
    for u, v in edges:
        descendant = delete_indices(graph, {u, v})
        assert min(dual_degrees(descendant)) == Fraction(17, 3)
        assert exact_charpoly(descendant) == P38

    assert P38.count_roots(-sp.oo, -sp.Rational(17, 3)) == 0
    assert P38.eval(-sp.Rational(17, 3)) != 0

    # The factor and exact comparison identify the least root of P38.
    assert sp.rem(P38, sp.Poly(X**2 + 6 * X + 2, X)).is_zero
    assert P38.count_roots(-sp.oo, -sp.Rational(28, 5)) == 1
    assert sp.Rational(8, 3) ** 2 > 7

    print("EXACT DESCENDANT-FAMILY CHECKS: PASS")
    print("40/40 single-vertex deletions:")
    print("  delta*=35/6 and identical exact distance characteristic polynomial P39")
    print("  P39 has no root <= -35/6, so all 40 are strict counterexamples")
    print("120/120 edge-endpoint deletions:")
    print("  delta*=17/3 and identical exact distance characteristic polynomial P38")
    print("  lambda_min=-3-sqrt(7), so all 120 are strict counterexamples")
    print("No isomorphism or minimality assertion is used.")


if __name__ == "__main__":
    check_family()
