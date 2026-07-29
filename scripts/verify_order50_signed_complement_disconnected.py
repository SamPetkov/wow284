#!/usr/bin/env python3
"""Exact arithmetic audit of order-50 signed-complement disconnectedness.

The Cameron--Goethals--Seidel--Shult signed-root theorem is treated as an
external input. Every project-derived recurrence, parity, rank, and coordinate
level calculation is checked here exactly.
"""
from __future__ import annotations

import sympy as sp

X = sp.symbols("x")


def nonbacktracking_polynomials(maximum_degree: int) -> list[sp.Expr]:
    values = [sp.Integer(1), X, X**2 - 6]
    for _ in range(3, maximum_degree + 1):
        values.append(sp.expand(X * values[-1] - 5 * values[-2]))
    return values


def trace_parity_audit() -> dict[str, object]:
    g = sp.expand((X + 2) ** 2 * ((X + 1) ** 2 - 10))
    basis = nonbacktracking_polynomials(8)
    coefficients = [28144, 18220, 8838, 3576, 1233, 352, 78, 12, 1]
    reconstructed = sum(
        coefficient * basis[index]
        for index, coefficient in enumerate(coefficients)
    )
    if sp.expand((g + 2) ** 2 - reconstructed) != 0:
        raise AssertionError("wrong nonbacktracking expansion")

    n5, n6, n7, n8 = sp.symbols("N5 N6 N7 N8", integer=True)
    closed_walk_traces = {
        5: 10 * n5,
        6: 12 * n6,
        7: 14 * n7 + 40 * n5,
        8: 16 * n8 + 48 * n6,
    }
    trace = (
        4
        + 50 * coefficients[0]
        + sum(
            coefficients[index] * closed_walk_traces[index]
            for index in range(5, 9)
        )
        - (g.subs(X, 6) + 2) ** 2
    )
    expected = 8 * (
        500 * n5 + 123 * n6 + 21 * n7 + 2 * n8 - 604100
    )
    if sp.expand(trace - expected) != 0:
        raise AssertionError("wrong signed trace-square identity")

    residues = [
        value
        for value in range(2)
        if (100 + 4 * value) % 8 == 0
    ]
    if residues != [1]:
        raise AssertionError("negative-edge parity changed")

    return {
        "coefficients": coefficients,
        "closed_walk_traces": {
            degree: str(value)
            for degree, value in closed_walk_traces.items()
        },
        "trace_square": str(expected),
        "negative_edge_parity": "odd",
    }


def rank_audit() -> dict[str, object]:
    multiplicity = sp.symbols("m", integer=True, nonnegative=True)
    moments = [
        49 - multiplicity,
        -6 + 2 * multiplicity,
        264 - 4 * multiplicity,
        -216 + 8 * multiplicity,
        2004 - 16 * multiplicity,
    ]
    hankel = sp.Matrix(3, 3, lambda row, column: moments[row + column])
    determinant = sp.factor(hankel.det())
    expected = 3600 * (1625 - 81 * multiplicity)
    if sp.expand(determinant - expected) != 0:
        raise AssertionError("wrong order-50 moment determinant")
    if 1625 // 81 != 20:
        raise AssertionError("wrong minus-two multiplicity floor")
    return {
        "determinant": str(determinant),
        "maximum_minus_two_multiplicity": 20,
        "minimum_Gram_rank": 30,
    }


def even_level_audit() -> dict[str, object]:
    possibilities: list[tuple[int, int, int]] = []
    for level_six in range(6):
        remainder = 200 - 36 * level_six
        if remainder < 0 or remainder % 4:
            continue
        level_two = remainder // 4
        used = level_two + level_six
        if 30 <= used <= 51:
            possibilities.append((level_two, level_six, used))
    expected = [(50, 0, 50), (41, 1, 42), (32, 2, 34)]
    if possibilities != expected:
        raise AssertionError(f"wrong even-level possibilities: {possibilities}")

    if any((6 * level_six) % 2 for _, level_six, _ in possibilities):
        raise AssertionError("even-level negative-edge parity changed")
    return {
        "possibilities": possibilities,
        "allowed_root_types": (
            "e_i+e_j at levels (2,2)",
            "e_i-e_j at levels (6,2)",
        ),
        "negative_edge_parity": "even",
    }


def odd_level_audit() -> dict[str, object]:
    admissible = [
        used
        for used in range(30, 52)
        if (200 - 3 * used) % 32 == 0
    ]
    if admissible:
        raise AssertionError(
            f"an odd-level coordinate count survived: {admissible}"
        )

    t = sp.symbols("t", integer=True, nonnegative=True)
    triangular = t * (t + 1) / 2
    level_a = 4 * t + 1
    level_b = 4 * t + 3
    first = sp.expand(level_a**2 - 3 - 32 * triangular)
    second = sp.expand(level_b**2 - 3 - 32 * triangular)
    if sp.expand(first + 2 * level_a) != 0:
        raise AssertionError("wrong 1 mod 4 level identity")
    if sp.expand(second - 2 * level_b) != 0:
        raise AssertionError("wrong 3 mod 4 level identity")
    return {
        "flow_identity": "sum (4t+1)A_t = sum (4t+3)B_t",
        "required_congruence": "v=24 mod 32",
        "admissible_v_in_30_to_51": admissible,
    }


def main() -> None:
    report = {
        "trace_parity": trace_parity_audit(),
        "rank": rank_audit(),
        "even_levels": even_level_audit(),
        "odd_levels": odd_level_audit(),
        "external_input": (
            "connected signed least-eigenvalue-minus-two root representation"
        ),
    }
    print("order-50 signed-complement disconnectedness audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
