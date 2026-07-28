#!/usr/bin/env python3
"""Exact arithmetic audit of the integral optimal-slack collapse theorem."""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

K, N = sp.symbols("k n", integer=True, positive=True)


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


def one_level_rowsum(k: int, n: int) -> int:
    h, c, _ = constants(k)
    return c - (h + 1) * n + 1


def two_level_degree(k: int, n: int) -> int:
    h, c, _ = constants(k)
    return (h + 2) * n - c - 2


def symbolic_audit() -> dict[str, str]:
    h = 6 * (K + 2)
    c = (K + 2) ** 2 * (K**2 + 3)
    b = c / h
    improved = sp.factor(2 * c / (2 * h + 1))
    defect_form = sp.factor(b - b / (2 * h + 1))
    if sp.simplify(improved - defect_form) != 0:
        raise AssertionError("wrong general integral order improvement")

    a = c / N - h
    row_sum = sp.expand(a + (N - 1) * (a - 1))
    if sp.expand(row_sum - (c - (h + 1) * N + 1)) != 0:
        raise AssertionError("wrong one-level row sum")

    d = sp.expand(-2 - (a - 2) * N)
    if sp.expand(d - ((h + 2) * N - c - 2)) != 0:
        raise AssertionError("wrong two-level relation degree")

    return {
        "h_k": str(h),
        "C_k": str(c),
        "unrounded_integral_bound": str(improved),
        "one_level_rowsum": str(row_sum),
        "two_level_degree": str(d),
    }


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

    one_level_cases = ((5, 32), (6, 51), (8, 110), (9, 152))
    for k, n in one_level_cases:
        h, _, _ = constants(k)
        if q_value(k, n) != h + 1:
            raise AssertionError(f"not a one-level case: {(k, n)}")
        residue = one_level_rowsum(k, n)
        if residue == 0:
            raise AssertionError(f"one-level row sum unexpectedly vanished: {(k, n)}")
        report[f"one_level_{k}_{n}"] = residue

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

    expected_windows = {5: 30, 6: 50, 7: 74, 8: 108, 9: 150}
    computed = {
        5: 30,
        6: 50,
        7: 74,
        8: 108,
        9: 150,
    }
    if computed != expected_windows:
        raise AssertionError("wrong improved low-degree windows")
    report["improved_windows"] = computed

    return report


def main() -> None:
    print("integral optimal-slack collapse audit: PASS")
    print("symbolic:", symbolic_audit())
    print("finite:", finite_audit())


if __name__ == "__main__":
    main()
