#!/usr/bin/env python3
"""Exact dual certificate for the full-degree two-sided LP ceiling.

For every integer k>=4, this verifies the symbolic ingredients showing that
the standard nonbacktracking linear-programming method for k-regular graphs of
girth at least five cannot improve

    n < (k+2)(k^2+3)/6

under the full shifted WOW adjacency window. No floating-point arithmetic is
used.
"""
from __future__ import annotations

import json

import sympy as sp

X = sp.symbols("x")
K = sp.symbols("k", integer=True, positive=True)
M = sp.symbols("m", integer=True, nonnegative=True)
DELTA = sp.sqrt(2 * K - 2)


def nonbacktracking_polynomials(max_degree: int) -> list[sp.Expr]:
    values = [sp.Integer(1), X, X**2 - K]
    for _ in range(3, max_degree + 1):
        values.append(sp.expand(X * values[-1] - (K - 1) * values[-2]))
    return values


def verify_extremal_polynomial(polynomials: list[sp.Expr]) -> dict[str, str]:
    boundary_factor = X**2 + 2 * X - (2 * K - 3)
    numerator = sp.expand((X + 2) ** 2 * boundary_factor)
    coefficients = [
        6 * (K + 2),
        2 * (2 * K + 7),
        K + 13,
        sp.Integer(6),
        sp.Integer(1),
    ]
    assert sp.expand(
        numerator - sum(coefficients[i] * polynomials[i] for i in range(5))
    ) == 0

    normalized = sp.factor(numerator / (6 * (K + 2)))
    order_bound = sp.factor((K + 2) * (K**2 + 3) / 6)
    assert sp.simplify(normalized.subs(X, K) - order_bound) == 0

    return {
        "extremal_polynomial": str(normalized),
        "F_basis_coefficients": str(
            [sp.factor(value / (6 * (K + 2))) for value in coefficients]
        ),
        "value_at_k": str(order_bound),
        "window_sign": (
            "(x+2)^2>=0 and x^2+2x-(2k-3)<=0 on "
            "[-1-sqrt(2k-2),-1+sqrt(2k-2)]"
        ),
    }


def dual_weights() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    common = K * (K + 2) / (24 * (2 * K - 3))
    lower = sp.factor(common * (2 * K**2 - 6 - 3 * (K - 1) * DELTA))
    middle = sp.factor(K * (K - 1) * (K**2 + 3) / (6 * (2 * K - 3)))
    upper = sp.factor(common * (2 * K**2 - 6 + 3 * (K - 1) * DELTA))
    return lower, middle, upper


def verify_dual_measure(polynomials: list[sp.Expr]) -> dict[str, str]:
    lower_point = -1 - DELTA
    middle_point = sp.Integer(-2)
    upper_point = -1 + DELTA
    points = (lower_point, middle_point, upper_point)
    weights = dual_weights()

    mass = sp.factor(sum(weights))
    expected_mass = sp.factor(K * (K**2 + 2 * K + 3) / 6)
    assert sp.simplify(mass - expected_mass) == 0

    positivity_square_difference = sp.factor(
        (2 * K**2 - 6) ** 2 - 18 * (K - 1) ** 3
    )
    expected_square_difference = 2 * (K - 3) * (2 * K - 3) * (K**2 + 3)
    assert sp.expand(
        positivity_square_difference - expected_square_difference
    ) == 0

    moments: dict[int, sp.Expr] = {}
    for degree in range(1, 10):
        moment = sp.simplify(
            sum(
                weights[index] * polynomials[degree].subs(X, points[index])
                for index in range(3)
            )
        )
        moments[degree] = moment

    for degree in range(1, 5):
        assert sp.simplify(
            moments[degree] + K * (K - 1) ** (degree - 1)
        ) == 0

    high_slacks = {
        degree: sp.factor(
            sp.radsimp(moments[degree] + K * (K - 1) ** (degree - 1))
        )
        for degree in range(5, 10)
    }
    expected = {
        5: K * (K - 1) * (K + 2) * (K**2 + 3) / 3,
        6: K * (K - 1) * (K + 2) * (5 * K - 13) * (K**2 + 3) / 6,
        7: K
        * (K - 1)
        * (K + 2)
        * (K**2 + 3)
        * (3 * K**2 - 17 * K + 25)
        / 3,
        8: K
        * (K - 1)
        * (K + 2)
        * (K**2 + 3)
        * (6 * K**3 - 47 * K**2 + 139 * K - 150)
        / 6,
        9: K
        * (K - 1)
        * (K + 2)
        * (K**2 + 3)
        * (3 * K**4 - 27 * K**3 + 106 * K**2 - 219 * K + 194)
        / 3,
    }
    for degree, value in expected.items():
        assert sp.simplify(high_slacks[degree] - value) == 0

    positive_inner_shifts = {
        7: sp.expand((3 * K**2 - 17 * K + 25).subs(K, M + 4)),
        8: sp.expand(
            (6 * K**3 - 47 * K**2 + 139 * K - 150).subs(K, M + 4)
        ),
        9: sp.expand(
            (
                3 * K**4
                - 27 * K**3
                + 106 * K**2
                - 219 * K
                + 194
            ).subs(K, M + 4)
        ),
    }
    expected_shifts = {
        7: 3 * M**2 + 7 * M + 5,
        8: 6 * M**3 + 25 * M**2 + 51 * M + 38,
        9: 3 * M**4 + 21 * M**3 + 70 * M**2 + 101 * M + 54,
    }
    for degree in expected_shifts:
        assert sp.expand(
            positive_inner_shifts[degree] - expected_shifts[degree]
        ) == 0

    # Uniform Chebyshev bound for every remaining degree i>=10. Put r=k-1.
    r, i = sp.symbols("r i", integer=True, positive=True)
    assert sp.expand(
        3 * r**2 - (r**2 + 4 * r + 6) - 2 * (r - 3) * (r + 1)
    ) == 0
    assert sp.expand(
        (4 * i + 2) * r / 3
        - ((i + 1) * r + i - 1)
        - (i - 1) * (r - 3) / 3
    ) == 0
    assert (
        sp.Rational(2 * 10 + 1, 3) * 3 ** (3 - sp.Rational(10, 2))
        == sp.Rational(7, 9)
    )
    assert sp.expand(
        3 * (2 * i + 1) ** 2 - (2 * i + 3) ** 2 - (8 * i**2 - 6)
    ) == 0

    return {
        "support": str(points),
        "weights": str(weights),
        "mass": str(mass),
        "weight_positivity_square_difference": str(positivity_square_difference),
        "moments_F1_to_F4": str({degree: moments[degree] for degree in range(1, 5)}),
        "slacks_F5_to_F9": str(high_slacks),
        "Chebyshev_tail_start": "i=10",
        "Chebyshev_tail_ratio_at_i10_r3": "7/9",
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    polynomials = nonbacktracking_polynomials(10)
    for degree in range(1, 11):
        assert sp.simplify(
            polynomials[degree].subs(X, K) - K * (K - 1) ** (degree - 1)
        ) == 0
    result = {
        "extremal_primal_certificate": verify_extremal_polynomial(polynomials),
        "dual_measure_certificate": verify_dual_measure(polynomials),
        "conclusion": (
            "For every integer k>=4, every standard girth-five "
            "nonbacktracking LP certificate for the full WOW window has "
            "f(k)/f0 >= (k+2)(k^2+3)/6, and equality is attained."
        ),
    }
    print("two-sided nonbacktracking LP ceiling: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
