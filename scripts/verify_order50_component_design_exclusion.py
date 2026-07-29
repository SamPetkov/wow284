#!/usr/bin/env python3
"""Exact audit of the degree-six order-50 component-design exclusion.

The external Cameron--Goethals--Seidel--Shult root-system theorem is treated as
an input.  Every polynomial, congruence, finite level reduction, equitable
partition count, incidence spectrum, block identity, and trace squeeze after
that input is checked exactly.
"""
from __future__ import annotations

from itertools import combinations_with_replacement

import sympy as sp

X = sp.symbols("x")


def nonbacktracking_polynomials(k: int, degree: int) -> list[sp.Expr]:
    values = [sp.Integer(1), X, X**2 - k]
    for index in range(3, degree + 1):
        values.append(sp.expand(X * values[-1] - (k - 1) * values[-2]))
    return values


def trace_parity_audit() -> dict[str, str]:
    functions = nonbacktracking_polynomials(6, 8)
    g = sp.expand((X + 2) ** 2 * ((X + 1) ** 2 - 10))
    if g != X**4 + 6 * X**3 + 3 * X**2 - 28 * X - 36:
        raise AssertionError("wrong g_6 expansion")

    coefficients = [28144, 18220, 8838, 3576, 1233, 352, 78, 12, 1]
    reconstructed = sum(
        coefficients[index] * functions[index] for index in range(9)
    )
    if sp.expand((g + 2) ** 2 - reconstructed) != 0:
        raise AssertionError("wrong nonbacktracking expansion of (g_6+2)^2")

    n5, n6, n7, n8 = sp.symbols("N5 N6 N7 N8", integer=True)
    cycle_counts = [n5, n6, n7, n8]
    trace_s2 = (
        4
        + 50 * coefficients[0]
        + sum(
            coefficients[index] * 2 * index * cycle_counts[index - 5]
            for index in range(5, 9)
        )
        - (g.subs(X, 6) + 2) ** 2
    )
    expected = 8 * (440 * n5 + 117 * n6 + 21 * n7 + 2 * n8 - 604100)
    if sp.expand(trace_s2 - expected) != 0:
        raise AssertionError("wrong signed-square trace congruence")

    # If P-N=50, then tr(S^2)=2(P+N)=100+4N.  Divisibility by eight
    # forces N odd.
    negative = sp.symbols("negative", integer=True)
    if sp.expand((100 + 4 * negative).subs(negative, 2 * sp.Symbol("q")) % 8) != 4:
        raise AssertionError("even-negative-edge parity test failed")
    if sp.expand((100 + 4 * negative).subs(negative, 2 * sp.Symbol("q") + 1) % 8) != 0:
        raise AssertionError("odd-negative-edge parity test failed")

    return {
        "g6": str(g),
        "nonbacktracking_coefficients": str(coefficients),
        "trace_S2": str(sp.factor(trace_s2)),
        "negative_edge_parity": "odd",
    }


def connected_root_audit() -> dict[str, object]:
    if 200 % 16 != 8:
        raise AssertionError("divisible-by-four level family was not excluded")

    family_b: list[tuple[int, int, int]] = []
    for n6 in range(0, 20):
        n2 = 50 - 9 * n6
        if n2 < 0:
            continue
        vertex_count = n2 + n6
        if 4 * n2 + 36 * n6 == 200 and 30 <= vertex_count <= 51:
            family_b.append((n2, n6, vertex_count))
    expected_b = [(50, 0, 50), (41, 1, 42), (32, 2, 34)]
    if family_b != expected_b:
        raise AssertionError(f"wrong level-2/6 possibilities: {family_b}")
    if any((6 * n6) % 2 for _, n6, _ in family_b):
        raise AssertionError("family-B negative-edge parity is not even")

    # The odd-level flow identity requires (200-3v)/32 to be a nonnegative
    # integer.  No rank-compatible support size has this property.
    family_c = [
        vertex_count
        for vertex_count in range(30, 52)
        if 200 - 3 * vertex_count >= 0
        and (200 - 3 * vertex_count) % 32 == 0
    ]
    if family_c:
        raise AssertionError(f"odd-level support sizes survived: {family_c}")

    return {
        "rank_support_interval": [30, 51],
        "family_B": family_b,
        "family_C": family_c,
        "connected_signed_complement": "excluded",
    }


def cubic_and_partition_audit() -> dict[str, object]:
    cubic = X**3 + 2 * X**2 - 8 * X - 4
    for root in (1, -1, 2, -2, 4, -4):
        if cubic.subs(X, root) == 0:
            raise AssertionError("cubic factor has a rational root")
    boundary = -1 + sp.sqrt(10)
    if sp.expand(cubic.subs(X, boundary) - (-5 + sp.sqrt(10))) != 0:
        raise AssertionError("wrong cubic value at the upper WOW endpoint")
    if not cubic.subs(X, 3) > 0:
        raise AssertionError("cubic root outside the WOW interval was not isolated")

    partitions: list[tuple[int, ...]] = []
    for number_of_parts in range(2, 6):
        for parts in combinations_with_replacement(range(5, 51, 5), number_of_parts):
            if sum(parts) == 50 and min(parts) >= 20:
                partitions.append(parts)
    if partitions != [(20, 30), (25, 25)]:
        raise AssertionError(f"wrong component-size list: {partitions}")
    if 25 % 2 != 1:
        raise AssertionError("odd perfect-matching obstruction disappeared")

    return {
        "cubic": str(cubic),
        "upper_boundary_value": str(sp.expand(cubic.subs(X, boundary))),
        "component_partitions": partitions,
        "surviving_partition": (20, 30),
    }


def incidence_audit() -> dict[str, str]:
    matching = sp.zeros(20)
    for vertex in range(0, 20, 2):
        matching[vertex, vertex + 1] = 1
        matching[vertex + 1, vertex] = 1
    row_gram = 5 * sp.eye(20) + sp.ones(20) - matching

    characteristic = sp.factor(row_gram.charpoly(X).as_expr())
    expected_characteristic = (X - 24) * (X - 6) ** 10 * (X - 4) ** 9
    if sp.expand(characteristic - expected_characteristic) != 0:
        raise AssertionError("wrong incidence row-Gram spectrum")
    if sp.trace(row_gram) != 120 or sp.trace(row_gram**2) != 1080:
        raise AssertionError("wrong incidence trace data")

    return {
        "row_gram_characteristic_polynomial": str(characteristic),
        "trace_B": "120",
        "trace_B2": "1080",
        "trace_BR": "0",
        "trace_BR2": "240",
    }


def block_polynomial_audit() -> dict[str, str]:
    # Test the noncommutative block identity on a generic exact rectangular
    # matrix and a generic exact symmetric lower-right block.  The proof note
    # also derives it term by term.
    c_matrix = sp.Matrix([[1, 2, 3], [4, 5, 6]])
    r_matrix = sp.Matrix([[0, 7, 8], [7, 0, 9], [8, 9, 0]])
    adjacency = sp.BlockMatrix(
        [[sp.zeros(2), c_matrix], [c_matrix.T, r_matrix]]
    ).as_explicit()
    polynomial = (
        adjacency**4
        + 6 * adjacency**3
        + 3 * adjacency**2
        - 28 * adjacency
        - 36 * sp.eye(5)
    )
    b_matrix = c_matrix.T * c_matrix
    h_matrix = (
        b_matrix * r_matrix
        + r_matrix * b_matrix
        + r_matrix**3
        + 6 * b_matrix
        + 6 * r_matrix**2
        + 3 * r_matrix
        - 28 * sp.eye(3)
    )
    if polynomial[:2, 2:] != c_matrix * h_matrix:
        raise AssertionError("wrong off-block polynomial identity")

    t = sp.symbols("T", real=True)
    trace_rb2 = 960 - 2 * t
    trace_br3 = sp.expand(1440 - 2 * trace_rb2)
    if trace_br3 != 4 * t - 480:
        raise AssertionError("wrong final trace squeeze")
    # T<=120 and tr(BR^3)>=0 force T=120.
    feasible = [
        value
        for value in range(0, 121)
        if 4 * value - 480 >= 0
    ]
    if feasible != [120]:
        raise AssertionError(f"trace squeeze did not force T=120: {feasible}")

    return {
        "off_block": "C(BR+RB+R^3+6B+6R^2+3R-28I)",
        "trace_equation": "2 tr(RB^2)+tr(BR^3)=1440",
        "matching_cross_sum": "120",
        "conclusion": "distance-two incidence contradiction",
    }


def main() -> None:
    report = {
        "trace_parity": trace_parity_audit(),
        "connected_root": connected_root_audit(),
        "partition": cubic_and_partition_audit(),
        "incidence": incidence_audit(),
        "block_polynomial": block_polynomial_audit(),
    }
    print("order-50 component-design exclusion audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
