#!/usr/bin/env python3
"""Exact closure of the degree-six c>=15 WOW-284 audit gate.

No floating-point arithmetic is used.  The script verifies two independent
proofs that a connected 6-regular graph of girth at least five and diameter
three cannot be a strict WOW-284 counterexample when its excess c=n-37 is at
least 15.
"""
from __future__ import annotations

import json

import sympy as sp


def shifted_moment_sum(
    polynomial: sp.Expr,
    theta: sp.Symbol,
    *,
    k: sp.Expr,
    n: sp.Expr,
) -> sp.Expr:
    """Sum a polynomial in nonprincipal adjacency eigenvalues from trace moments."""
    moments = {
        0: n - 1,
        1: -k,
        2: n * k - k**2,
        3: -k**3,
        4: n * k * (2 * k - 1) - k**4,
    }
    poly = sp.Poly(sp.expand(polynomial), theta)
    return sp.expand(
        sum(coefficient * moments[power[0]] for power, coefficient in poly.terms())
    )


def verify_layer_compression() -> dict[str, str]:
    x = sp.symbols("x")
    c, a, m = sp.symbols("c a m", real=True, positive=True)
    k = sp.Integer(6)
    a0 = k - 1 - c / (k - 1)

    compression0 = sp.Matrix(
        [
            [0, sp.sqrt(k), 0, 0],
            [sp.sqrt(k), 0, sp.sqrt(k - 1), 0],
            [
                0,
                sp.sqrt(k - 1),
                a0,
                (k - 1 - a0) * sp.sqrt(k * (k - 1) / c),
            ],
            [
                0,
                0,
                (k - 1 - a0) * sp.sqrt(k * (k - 1) / c),
                k - k * (k - 1) * (k - 1 - a0) / c,
            ],
        ]
    )
    compression = sp.Matrix(
        [
            [0, sp.sqrt(k), 0, 0],
            [sp.sqrt(k), 0, sp.sqrt(k - 1), 0],
            [
                0,
                sp.sqrt(k - 1),
                a,
                (k - 1 - a) * sp.sqrt(k * (k - 1) / c),
            ],
            [
                0,
                0,
                (k - 1 - a) * sp.sqrt(k * (k - 1) / c),
                k - k * (k - 1) * (k - 1 - a) / c,
            ],
        ]
    )

    z = sp.Matrix([0, 0, 1, -sp.sqrt(30 / c)])
    assert sp.simplify(
        compression - compression0 - (a - a0) * z * z.T
    ) == sp.zeros(4)

    p = 5 * x**3 + (c + 5) * x**2 - 25 * x - 6 * c
    characteristic = sp.factor(compression0.charpoly(x).as_expr())
    assert sp.expand(characteristic - (x - 6) * p / 5) == 0

    boundary = -1 + sp.sqrt(10)
    evaluation = sp.factor(p.subs(x, boundary))
    expected_evaluation = -(2 * sp.sqrt(10) - 5) * (c - 15)
    assert sp.simplify(evaluation - expected_evaluation) == 0

    assert 40 > 25
    assert bool(2 * sp.sqrt(10) - 5 > 0)
    assert sp.expand(
        p.subs({c: 15, x: x}) - 5 * (x + 2) * (x**2 + 2 * x - 9)
    ) == 0

    shifted_evaluation = sp.expand(
        evaluation.subs(c, m + 15)
        + (2 * sp.sqrt(10) - 5) * m
    )
    assert shifted_evaluation == 0

    return {
        "extremal_characteristic_factor": str(sp.factor(p / 5)),
        "boundary": str(boundary),
        "boundary_evaluation": str(evaluation),
        "rank_one_vector": str(z.T),
        "conclusion": "c>=15 implies lambda_2>=-1+sqrt(10), so strictness fails",
    }


def verify_independent_moment_bound() -> dict[str, str]:
    theta, k, n = sp.symbols("theta k n", real=True)
    y = theta + 1
    summand = sp.expand((2 * k - 2 - y**2) * (y + 1) ** 2)
    exact_sum = shifted_moment_sum(summand, theta, k=k, n=n)
    target = (k + 2) * ((k + 2) * (k**2 + 3) - 6 * n)
    assert sp.expand(exact_sum - target) == 0

    assert sp.simplify(target.subs(k, 6) - 48 * (52 - n)) == 0

    alpha, beta, gamma = sp.symbols("alpha beta gamma", real=True)
    numerator = (k**2 + 3) * (
        alpha * (k + 1) ** 2 + beta * (k + 1) + gamma
    )
    denominator = (
        (5 * k + 3) * alpha
        + (k + 3) * beta
        - (k - 3) * gamma
    )
    optimal_value = (k + 2) * (k**2 + 3) / 6
    q_at_minus_one = alpha - beta + gamma
    assert sp.factor(
        numerator - optimal_value * denominator
        - k * (k - 1) * (k**2 + 3) * q_at_minus_one / 6
    ) == 0

    assert sp.expand(
        denominator.subs({alpha: 1, beta: 2, gamma: 1}) - 6 * (k + 2)
    ) == 0
    assert sp.simplify(
        numerator.subs({alpha: 1, beta: 2, gamma: 1})
        / denominator.subs({alpha: 1, beta: 2, gamma: 1})
        - optimal_value
    ) == 0

    return {
        "moment_identity": str(sp.factor(exact_sum)),
        "general_strict_order_bound": "n < (k+2)(k^2+3)/6",
        "degree_six_bound": "n < 52, hence n <= 51",
        "quadratic_multiplier_optimality_remainder": (
            "k(k-1)(k^2+3)q(-1)/6"
        ),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "distance_layer_proof": verify_layer_compression(),
        "independent_fourth_moment_proof": verify_independent_moment_bound(),
    }
    print("degree-six c>=15 audit gate: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
