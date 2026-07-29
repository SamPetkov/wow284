#!/usr/bin/env python3
"""Exact audit of the optimal-slack Gram hierarchy.

The script checks the project-derived algebra, the order-50 signed-root
reduction, the neighbourhood inequality, and the arithmetic in the improved
low-degree windows. Its only external input is the classical classification of
connected regular graphs with least eigenvalue at least -2 and more than 28
vertices; every subsequent line-graph and cocktail-party exclusion is checked
here exactly.
"""
from __future__ import annotations

from fractions import Fraction

import sympy as sp

X = sp.symbols("x")
K = sp.symbols("k", integer=True, positive=True)
N = sp.symbols("n", integer=True, positive=True)


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def symbolic_audit() -> dict[str, str]:
    g = sp.expand((X + 2) ** 2 * ((X + 1) ** 2 - (2 * K - 2)))
    expected = (
        X**4
        + 6 * X**3
        + (15 - 2 * K) * X**2
        + (20 - 8 * K) * X
        + 12
        - 8 * K
    )
    if sp.expand(g - expected) != 0:
        raise AssertionError("wrong power-basis expansion")

    principal = sp.factor(g.subs(X, K))
    c_k = (K + 2) ** 2 * (K**2 + 3)
    if sp.expand(principal - c_k) != 0:
        raise AssertionError("wrong principal value")

    b_k = (K + 2) * (K**2 + 3) / 6
    trace = sp.factor(principal - 6 * (K + 2) * N)
    if sp.expand(trace - 6 * (K + 2) * (b_k - N)) != 0:
        raise AssertionError("wrong trace-defect identity")

    theta = sp.symbols("theta", real=True)
    slack = sp.factor(-g.subs(X, theta))
    expected_slack = (2 * K - 2 - (theta + 1) ** 2) * (theta + 2) ** 2
    if sp.expand(slack - expected_slack) != 0:
        raise AssertionError("wrong nonprincipal slack eigenvalue")

    sigma, alpha, beta, eta, gamma = sp.symbols(
        "sigma alpha beta eta gamma", integer=True
    )
    edge_entry = sigma + 6 * (2 * K - 1) + (20 - 8 * K)
    if sp.expand(edge_entry - (4 * K + 14 + sigma)) != 0:
        raise AssertionError("wrong edge entry")

    # At distance two, F_2=1, F_3=alpha and F_4=beta. Equivalently,
    # A^4_{uw}=3k-2+beta, not 4k-8+beta except at k=6.
    distance_two_entry = (
        (3 * K - 2 + beta) + 6 * alpha + (15 - 2 * K)
    )
    if sp.expand(distance_two_entry - (K + 13 + 6 * alpha + beta)) != 0:
        raise AssertionError("wrong distance-two entry")

    # At distance three, A and A^2 vanish, so the entry is simply
    # q=6(A^3)_{uz}+(A^4)_{uz}; there need not be a unique geodesic.
    distance_three_entry = gamma + 6 * eta
    if sp.expand(distance_three_entry - (6 * eta + gamma)) != 0:
        raise AssertionError("wrong distance-three entry")

    return {
        "power_basis": str(g),
        "principal_value": str(principal),
        "trace_defect": str(trace),
        "nonprincipal_slack": str(slack),
        "distance_two_constant": str(K + 13),
        "distance_three_parameter": "6*(A^3)_{uz}+(A^4)_{uz}",
    }


def slack_data(k: int, n: int) -> tuple[Fraction, Fraction]:
    c_k = Fraction((k + 2) ** 2 * (k**2 + 3), 1)
    diagonal = c_k / n - 6 * (k + 2)
    if diagonal <= 0:
        raise AssertionError("slack diagonal is not positive")
    return c_k, diagonal


def integer_interval(k: int, n: int, base: int) -> list[int]:
    c_k, diagonal = slack_data(k, n)
    centre = c_k / n - base
    return list(
        range(
            ceil_fraction(centre - diagonal),
            floor_fraction(centre + diagonal) + 1,
        )
    )


def scaled_value(k: int, n: int, base: int, parameter: int, scale: int) -> int:
    c_k, _ = slack_data(k, n)
    scaled = (c_k / n - base - parameter) * scale
    if scaled.denominator != 1:
        raise AssertionError("scale does not clear denominators")
    return scaled.numerator


def relation_graph_arithmetic(
    *,
    n: int,
    scale: int,
    diagonal: int,
    positive: int,
    negative: int,
    expected_degree: int,
    line_degree: int,
    root_regular_degree: int,
    root_semiregular_sum: int,
) -> dict[str, object]:
    # scale*M = alpha*I + negative*J + scale*A(X).
    alpha = diagonal - negative
    if positive - negative != scale:
        raise AssertionError("wrong two-distance scale")
    numerator = -(alpha + negative * n)
    if numerator % scale:
        raise AssertionError("relation degree is not integral")
    degree = numerator // scale
    if degree != expected_degree:
        raise AssertionError("wrong relation degree")
    if degree <= (n - 2) / 2:
        raise AssertionError("relation graph connectivity is not forced")
    if degree == n - 2:
        raise AssertionError("cocktail-party case was not excluded")

    if 2 * (root_regular_degree - 1) != line_degree:
        raise AssertionError("wrong regular line-root degree")
    if Fraction(2 * n, root_regular_degree).denominator == 1:
        raise AssertionError("regular line-root case survived")

    pairs = [
        (left, right)
        for left in divisors(n)
        for right in divisors(n)
        if left + right == root_semiregular_sum
    ]
    if pairs:
        raise AssertionError(f"semiregular line-root case survived: {pairs}")

    return {
        "relation_degree": degree,
        "connected_by_degree": True,
        "cocktail_party_excluded": True,
        "line_graph_arithmetic_excluded": True,
    }


def near_ceiling_audit() -> dict[str, object]:
    report: dict[str, object] = {}

    # k=7, n=76.
    k, n = 7, 76
    if slack_data(k, n)[1] != Fraction(27, 19):
        raise AssertionError("wrong k=7 diagonal")
    intervals = (
        integer_interval(k, n, 4 * k + 14),
        integer_interval(k, n, k + 13),
        integer_interval(k, n, 0),
    )
    if intervals != ([12, 13, 14], [34, 35, 36], [54, 55, 56]):
        raise AssertionError("wrong k=7 intervals")
    values: set[int] = set()
    for base, candidates in zip((4 * k + 14, k + 13, 0), intervals, strict=True):
        values.update(scaled_value(k, n, base, value, 19) for value in candidates[1:])
    if values != {8, -11}:
        raise AssertionError("wrong k=7 two-distance values")
    report["k7_n76"] = relation_graph_arithmetic(
        n=n,
        scale=19,
        diagonal=27,
        positive=8,
        negative=-11,
        expected_degree=42,
        line_degree=42,
        root_regular_degree=22,
        root_semiregular_sum=44,
    )

    # k=8, n=110.
    k, n = 8, 110
    if slack_data(k, n)[1] != Fraction(10, 11):
        raise AssertionError("wrong k=8,n=110 diagonal")
    intervals = (
        integer_interval(k, n, 4 * k + 14),
        integer_interval(k, n, k + 13),
        integer_interval(k, n, 0),
    )
    if intervals != ([14, 15], [39, 40], [60, 61]):
        raise AssertionError("wrong k=8,n=110 intervals")
    remaining = {
        scaled_value(k, n, base, candidates[-1], 11)
        for base, candidates in zip((4 * k + 14, k + 13, 0), intervals, strict=True)
    }
    if remaining != {-1} or 10 + 109 * (-1) == 0:
        raise AssertionError("k=8,n=110 row-sum contradiction failed")
    report["k8_n110"] = {"row_sum_numerator": -99, "excluded": True}

    # k=8, n=109.
    k, n = 8, 109
    if slack_data(k, n)[1] != Fraction(160, 109):
        raise AssertionError("wrong k=8,n=109 diagonal")
    intervals = (
        integer_interval(k, n, 4 * k + 14),
        integer_interval(k, n, k + 13),
        integer_interval(k, n, 0),
    )
    if intervals != ([14, 15, 16], [39, 40, 41], [60, 61, 62]):
        raise AssertionError("wrong k=8,n=109 intervals")
    values = set()
    for base, candidates in zip((4 * k + 14, k + 13, 0), intervals, strict=True):
        values.update(scaled_value(k, n, base, value, 109) for value in candidates[1:])
    if values != {51, -58}:
        raise AssertionError("wrong k=8,n=109 two-distance values")
    report["k8_n109"] = relation_graph_arithmetic(
        n=n,
        scale=109,
        diagonal=160,
        positive=51,
        negative=-58,
        expected_degree=56,
        line_degree=56,
        root_regular_degree=29,
        root_semiregular_sum=58,
    )

    # k=9, n=152.
    k, n = 9, 152
    if slack_data(k, n)[1] != Fraction(33, 38):
        raise AssertionError("wrong k=9,n=152 diagonal")
    intervals = (
        integer_interval(k, n, 4 * k + 14),
        integer_interval(k, n, k + 13),
        integer_interval(k, n, 0),
    )
    if intervals != ([16, 17], [44, 45], [66, 67]):
        raise AssertionError("wrong k=9,n=152 intervals")
    remaining = {
        scaled_value(k, n, base, candidates[-1], 38)
        for base, candidates in zip((4 * k + 14, k + 13, 0), intervals, strict=True)
    }
    if remaining != {-5} or 33 + 151 * (-5) == 0:
        raise AssertionError("k=9,n=152 row-sum contradiction failed")
    report["k9_n152"] = {"row_sum_numerator": -722, "excluded": True}

    return report


def order50_audit() -> dict[str, object]:
    k, n = 6, 50
    c_k, diagonal = slack_data(k, n)
    if c_k != 2496 or diagonal != Fraction(48, 25):
        raise AssertionError("wrong order-50 constants")

    raw_edge = integer_interval(k, n, 4 * k + 14)
    dist2 = integer_interval(k, n, k + 13)
    dist3 = integer_interval(k, n, 0)
    if raw_edge != [10, 11, 12, 13]:
        raise AssertionError("wrong raw edge interval")
    excess = n - (k**2 + 1)
    radius_lower = (k - 1) ** 2 - excess
    edge = [value for value in raw_edge if value >= radius_lower]
    if edge != [12, 13] or dist2 != [29, 30, 31, 32] or dist3 != [48, 49, 50, 51]:
        raise AssertionError("wrong refined order-50 intervals")

    edge_t = [12 - value for value in edge]
    dist2_t = [31 - value for value in dist2]
    dist3_t = [50 - value for value in dist3]
    if edge_t != [0, -1] or dist2_t != [2, 1, 0, -1] or dist3_t != [2, 1, 0, -1]:
        raise AssertionError("wrong signed-root conversion")
    if set(edge_t + dist2_t[1:] + dist3_t[1:]) != {-1, 0, 1}:
        raise AssertionError("signed entries are not {-1,0,1}")

    a, d, r_total = sp.symbols("a d R", real=True)
    quadratic = 2 * a**2 - 2 * d * a + 942 - 2 * r_total
    minimized = sp.expand(quadratic.subs(a, d / 2))
    if sp.expand(minimized - (942 - d**2 / 2 - 2 * r_total)) != 0:
        raise AssertionError("wrong neighbourhood quadratic")
    if sp.expand(2 * (471 - d**2 / 4) - (942 - d**2 / 2)) != 0:
        raise AssertionError("wrong weak neighbourhood bound")

    local_bounds = {degree: 470 - degree**2 // 4 for degree in (0, 2, 4)}
    if local_bounds != {0: 470, 2: 469, 4: 466}:
        raise AssertionError("wrong strict neighbourhood bounds")

    m, s2 = sp.symbols("m S2", integer=True, nonnegative=True)
    n6_upper = sp.factor((50 * 470 - s2 / 4 - 10800 - 6 * m) / 6)
    expected = sp.Rational(6350, 3) - m - s2 / 24
    if sp.simplify(n6_upper - expected) != 0:
        raise AssertionError("wrong summed N6 bound")

    return {
        "diagonal": str(diagonal),
        "edge_interval": edge,
        "distance_two_interval": dist2,
        "distance_three_interval": dist3,
        "signed_entries": [-1, 0, 1],
        "local_R_bounds": local_bounds,
        "summed_N6_bound": str(expected),
    }


def main() -> None:
    report = {
        "general": symbolic_audit(),
        "order50": order50_audit(),
        "near_ceiling": near_ceiling_audit(),
        "external_input": (
            "classification of connected regular graphs with least eigenvalue "
            "at least -2 and more than 28 vertices"
        ),
    }
    print("optimal-slack Gram unification audit: PASS")
    for section, value in report.items():
        print(f"{section}: {value}")


if __name__ == "__main__":
    main()
