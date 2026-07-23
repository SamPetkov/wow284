#!/usr/bin/env python3
"""Exact screen of several regular induced subgraphs inside Hoffman-Singleton.

The fixed deletion sets were found during a mixed-integer exploratory search.
This script does not use the optimizer: it reconstructs every candidate and
checks all reported spectra exactly.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import (  # noqa: E402
    adjacency_matrix,
    distance_matrix,
    dual_degrees,
    girth,
    hoffman_singleton,
    induced_indices,
)


CASES = [
    {
        "name": "degree-6/order-42",
        "deleted": [5, 6, 9, 25, 31, 37, 43, 49],
        "degree": 6,
        "girth": 5,
        "diameter": 3,
        "chi_a": lambda x: (x - 6) * (x - 2) ** 21 * (x + 1) ** 6 * (x + 3) ** 14,
        "chi_d": lambda x: x**14 * (x - 81) * (x - 4) ** 6 * (x + 5) ** 21,
        "score": Fraction(1),
    },
    {
        "name": "degree-5/order-36",
        "deleted": [20, 21, 22, 23, 26, 27, 30, 31, 35, 39, 43, 44, 47, 48],
        "degree": 5,
        "girth": 5,
        "diameter": 3,
        "chi_a": lambda x: (x - 5) * (x - 2) ** 16 * (x + 1) ** 10 * (x + 3) ** 9,
        "chi_d": lambda x: (x - 75) * (x - 3) ** 10 * (x + 1) ** 9 * (x + 6) ** 16,
        "score": Fraction(-1),
    },
    {
        "name": "degree-4/order-35",
        "deleted": [4, 8, 10, 15, 23, 26, 27, 30, 31, 37, 38, 42, 43, 45, 46],
        "degree": 4,
        "girth": 6,
        "diameter": 3,
        "chi_a": lambda x: (x - 4) * (x - 2) ** 14 * (x + 1) ** 14 * (x + 3) ** 6,
        "chi_d": lambda x: (x - 82) * (x - 2) ** 14 * (x + 2) ** 6 * (x + 7) ** 14,
        "score": Fraction(-3),
    },
    {
        "name": "degree-3/order-30",
        "deleted": [1, 4, 6, 8, 11, 13, 16, 19, 23, 24, 25, 27, 30, 31, 38, 39, 42, 43, 47, 48],
        "degree": 3,
        "girth": 8,
        "diameter": 4,
        "chi_a": lambda x: x**10 * (x - 3) * (x - 2) ** 9 * (x + 2) ** 9 * (x + 3),
        "chi_d": lambda x: (x - 83) * (x - 5) * (x - 2) ** 10 * (x + 2) ** 9 * (x + 10) ** 9,
        "score": Fraction(-7),
    },
]


def main() -> None:
    full, _ = hoffman_singleton()
    x = sp.symbols("x")
    for case in CASES:
        graph, _ = induced_indices(full, set(case["deleted"]))
        degree = case["degree"]
        if set(map(len, graph)) != {degree}:
            raise AssertionError((case["name"], set(map(len, graph))))
        if girth(graph) != case["girth"]:
            raise AssertionError((case["name"], girth(graph)))
        a = adjacency_matrix(graph)
        d = distance_matrix(graph)
        if max(d) != case["diameter"]:
            raise AssertionError((case["name"], max(d)))
        char_a = sp.factor(a.charpoly(x).as_expr())
        char_d = sp.factor(d.charpoly(x).as_expr())
        if sp.Poly(char_a - case["chi_a"](x), x) != sp.Poly(0, x):
            raise AssertionError((case["name"], char_a))
        if sp.Poly(char_d - case["chi_d"](x), x) != sp.Poly(0, x):
            raise AssertionError((case["name"], char_d))
        dual = min(dual_degrees(graph))
        least = min(d.eigenvals(), key=lambda z: float(sp.N(z)))
        score = sp.Rational(dual.numerator, dual.denominator) + least
        if score != case["score"]:
            raise AssertionError((case["name"], score))
        print(f"{case['name']}: PASS")
        print(f"  order={len(graph)} degree={degree} girth={case['girth']} diameter={case['diameter']}")
        print(f"  chi_A={char_a}")
        print(f"  chi_D={char_d}")
        print(f"  delta*={dual}; lambda_min={least}; score={score}")


if __name__ == "__main__":
    main()
