#!/usr/bin/env python3
"""Exact certificates for the 41- and 40-vertex descendants of the 42 graph."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import (  # noqa: E402
    distance_matrix,
    dual_degrees,
    graph42,
    induced_indices,
)


def verify_candidate(name: str, graph, expected_dual: Fraction, expected_poly: sp.Expr) -> None:
    d = distance_matrix(graph)
    x = sp.symbols("x")
    dual = min(dual_degrees(graph))
    if dual != expected_dual:
        raise AssertionError((name, dual, expected_dual))
    characteristic = sp.factor(d.charpoly(x).as_expr())
    if sp.Poly(characteristic - expected_poly, x) != sp.Poly(0, x):
        raise AssertionError((name, characteristic))
    p, q = dual.numerator, dual.denominator
    shifted = q * d + p * sp.eye(len(graph))
    lower, diagonal = shifted.LDLdecomposition(hermitian=True)
    if lower * diagonal * lower.T != shifted:
        raise AssertionError(f"{name}: LDL reconstruction")
    pivots = [diagonal[i, i] for i in range(len(graph))]
    if not all(pivot > 0 for pivot in pivots):
        raise AssertionError(f"{name}: nonpositive pivot")
    print(f"{name}: PASS")
    print(f"  order={len(graph)} delta*={dual}")
    print(f"  chi_D={characteristic}")
    print(f"  shifted={q}D+{p}I; minimum LDL pivot={min(pivots, key=float)}")


def main() -> None:
    graph, _ = graph42()
    x = sp.symbols("x")

    graph41, _ = induced_indices(graph, {0})
    expected41 = (
        x**8
        * (x + 5) ** 15
        * (x**3 - 85 * x**2 + 420 * x - 510)
        * (x**3 + 2 * x**2 - 21 * x - 6) ** 5
    )
    verify_candidate("42-minus-one (order 41)", graph41, Fraction(35, 6), expected41)

    neighbor = min(graph[0])
    graph40, _ = induced_indices(graph, {0, neighbor})
    expected40 = (
        x**4
        * (x + 5) ** 11
        * (x**2 - 4 * x + 2)
        * (x**2 + 6 * x + 2) ** 4
        * (x**3 - 83 * x**2 + 390 * x - 414)
        * (x**3 + 2 * x**2 - 20 * x - 4) ** 4
    )
    verify_candidate("42-minus-edge (order 40)", graph40, Fraction(17, 3), expected40)


if __name__ == "__main__":
    main()
