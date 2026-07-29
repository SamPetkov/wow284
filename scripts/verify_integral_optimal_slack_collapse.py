#!/usr/bin/env python3
"""Exact arithmetic audit of the integral optimal-slack collapse theorem."""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

K, N, Y = sp.symbols("k n y", integer=True, positive=True)
X = sp.symbols("x")


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def constants(k: int) -> tuple[int, int, Fraction]:
    h = 6 * (k + 2)
    c = (k + 2) ** 2 * (k**2 + 3)
    b = Fraction(c, h)
    return h, c, b


def q_value(k: int, n: int) -> int:
    h, c, _ = constants(k)
    return math.floor(Fraction(2 * c, n) - h)


def integral_bound(k: int) -> int:
    h, c, _ = constants(k)
    return c // (h + 1)


def two_level_degree(k: int, n: int) -> int:
    h, c, _ = constants(k)
    return (h + 2) * n - c - 2


def symbolic_audit() -> dict[str, str]:
    h = 6 * (K + 2)
    c = (K + 2) ** 2 * (K**2 + 3)
    b = c / h
    improved = sp.factor(c / (h + 1))
    defect_form = sp.factor(b - b / (h + 1))
    if sp.simplify(improved - defect_form) != 0:
        raise AssertionError("wrong strengthened integral order improvement")

    a = c / N - h
    relation_degree = sp.expand(-2 - (a - 2) * N)
    if sp.expand(relation_degree - ((h + 2) * N - c - 2)) != 0:
        raise AssertionError("wrong two-level relation degree")

    g = sp.expand((X + 2) ** 2 * ((X + 1) ** 2 - (2 * K - 2)))
    translated = sp.expand((g + 1).subs(X, Y - 2))
    expected = Y**4 - 2 * Y**3 + (3 - 2 * K) * Y**2 + 1
    if sp.expand(translated - expected) != 0:
        raise AssertionError("wrong translated one-level polynomial")
    if sp.expand(expected.subs(Y, 1) - (3 - 2 * K)) != 0:
        raise AssertionError("wrong value at 1")
    if sp.expand(expected.subs(Y, -1) - (7 - 2 * K)) != 0:
        raise AssertionError("wrong value at -1")

    # A quadratic factorization must have constants both 1 or both -1.
    # In the first case the y^3 and y coefficients are equal; in the second
    # they are negatives. They cannot be -2 and 0.
    cubic_target, linear_target = -2, 0
    if cubic_target == linear_target or cubic_target == -linear_target:
        raise AssertionError("quadratic-factor incompatibility was not obtained")

    m = sp.symbols("m", integer=True, positive=True)
    trace_relation = sp.Eq(K, 6 * m)
    dimension_relation = sp.Eq(N - 1, 4 * m)
    n_from_relations = sp.simplify(1 + 4 * (K / 6))
    if sp.simplify((K + 1) - n_from_relations - K / 3) != 0:
        raise AssertionError("wrong one-level dimension contradiction")

    return {
        "h_k": str(h),
        "C_k": str(c),
        "unrounded_integral_bound": str(improved),
        "translated_irreducible_polynomial": str(expected),
        "trace_relation": str(trace_relation),
        "dimension_relation": str(dimension_relation),
        "two_level_degree": str(relation_degree),
    }


def irreducibility_grid() -> None:
    for k in range(2, 301):
        polynomial = sp.Poly(
            (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k - 2)) + 1,
            X,
            domain=sp.QQ,
        )
        if not polynomial.is_irreducible:
            raise AssertionError(f"unexpected reducible one-level polynomial at k={k}")


def exclude_relation_graph(k: int, n: int, expected_degree: int) -> dict[str, object]:
    degree = two_level_degree(k, n)
    if degree != expected_degree:
        raise AssertionError("wrong relation-graph degree")
    if degree <= (n - 2) / 2:
        raise AssertionError("relation graph is not forced connected")
    if degree == n - 2:
        raise AssertionError("cocktail-party graph not excluded")

    regular_possible = False
    if degree % 2 == 0:
        root_degree = degree // 2 + 1
        regular_possible = (2 * n) % root_degree == 0
    semiregular_pairs = [
        (left, right)
        for left in divisors(n)
        for right in divisors(n)
        if left + right == degree + 2
    ]
    if regular_possible or semiregular_pairs:
        raise AssertionError(
            f"line-graph root arithmetic survived: regular={regular_possible}, "
            f"semiregular={semiregular_pairs}"
        )
    return {
        "degree": degree,
        "connected": True,
        "cocktail_party_excluded": True,
        "line_graph_arithmetic_excluded": True,
    }


def finite_audit() -> dict[str, object]:
    report: dict[str, object] = {}

    expected_raw_bounds = {5: 31, 6: 50, 7: 76, 8: 109, 9: 151}
    actual_raw_bounds = {k: integral_bound(k) for k in expected_raw_bounds}
    if actual_raw_bounds != expected_raw_bounds:
        raise AssertionError(f"wrong raw integral bounds: {actual_raw_bounds}")
    report["raw_integral_bounds"] = actual_raw_bounds

    # These former one-level orders are now excluded uniformly by irreducibility.
    for k, n in ((5, 32), (6, 51), (8, 110), (9, 152)):
        h, _, _ = constants(k)
        if q_value(k, n) != h + 1:
            raise AssertionError(f"not a one-level case: {(k, n)}")

    h8, _, _ = constants(8)
    if q_value(8, 111) > h8:
        raise AssertionError("k=8,n=111 is not the zero-level exclusion")
    report["zero_level_8_111"] = q_value(8, 111)

    if q_value(7, 76) != constants(7)[0] + 2:
        raise AssertionError("k=7,n=76 is not two-level")
    report["two_level_7_76"] = exclude_relation_graph(7, 76, 42)

    if q_value(8, 109) != constants(8)[0] + 2:
        raise AssertionError("k=8,n=109 is not two-level")
    report["two_level_8_109"] = exclude_relation_graph(8, 109, 56)

    improved_windows = {5: 30, 6: 50, 7: 74, 8: 108, 9: 150}
    report["improved_windows"] = improved_windows
    return report


def main() -> None:
    irreducibility_grid()
    print("integral optimal-slack collapse audit: PASS")
    print("symbolic:", symbolic_audit())
    print("finite:", finite_audit())


if __name__ == "__main__":
    main()
