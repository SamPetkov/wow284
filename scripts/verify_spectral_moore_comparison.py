#!/usr/bin/env python3
"""Exact comparison with the published spectral-Moore bound.

This verifies the specialization of Cioaba--Koolen--Nozaki--Vermette,
Theorem 2.3, at k=6 and theta=-1+sqrt(10).  It is a literature comparison,
not a proof of the stronger two-sided WOW-specific bound.
"""
from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    x = sp.symbols("x")
    k = sp.Integer(6)
    theta = -1 + sp.sqrt(10)
    c = (16 + 2 * sp.sqrt(10)) / 3

    matrix = sp.Matrix(
        [
            [0, k, 0, 0],
            [1, 0, k - 1, 0],
            [0, 1, 0, k - 1],
            [0, 0, c, k - c],
        ]
    )
    characteristic = sp.factor(
        matrix.charpoly(x).as_expr(), extension=sp.sqrt(10)
    )
    residual_quadratic = (
        x**2
        + (sp.Rational(13, 3) + 5 * sp.sqrt(10) / 3) * x
        + sp.Rational(20, 3)
        + 10 * sp.sqrt(10) / 3
    )
    expected = (x - k) * (x - theta) * residual_quadratic
    assert sp.expand(characteristic - expected) == 0

    coefficient = sp.Rational(13, 3) + 5 * sp.sqrt(10) / 3
    discriminant = sp.factor(
        sp.discriminant(residual_quadratic, x), extension=sp.sqrt(10)
    )
    assert sp.simplify(discriminant - (179 + 10 * sp.sqrt(10)) / 9) == 0
    assert bool(discriminant > 0)
    assert sp.simplify(theta + coefficient / 2) == (
        sp.Rational(7, 6) + 11 * sp.sqrt(10) / 6
    )
    assert bool(theta + coefficient / 2 > 0)
    assert sp.simplify(
        residual_quadratic.subs(x, theta) - 2 * (15 + 2 * sp.sqrt(10))
    ) == 0
    assert bool(residual_quadratic.subs(x, theta) > 0)

    bound = sp.simplify(1 + 6 + 30 + 150 / c)
    expected_bound = sp.Rational(211, 3) - 25 * sp.sqrt(10) / 6
    assert sp.simplify(bound - expected_bound) == 0

    assert 80**2 > 25**2 * 10
    assert bool(bound > 57)
    assert 25**2 * 10 > 74**2
    assert bool(bound < 58)

    result = {
        "k": 6,
        "theta": str(theta),
        "t": 4,
        "c": str(c),
        "T_characteristic_polynomial": str(characteristic),
        "published_one_sided_bound": str(bound),
        "integer_consequence": "v(6,-1+sqrt(10)) <= 57",
        "project_two_sided_bound": "n <= 51",
    }
    print("spectral-Moore comparison: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
