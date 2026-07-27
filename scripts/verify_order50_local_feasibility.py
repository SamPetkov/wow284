#!/usr/bin/env python3
"""Exact local and moment constraints for a hypothetical order-50 candidate.

The scope is a connected 6-regular graph of girth at least five, diameter three,
and strict WOW-284 violation.  The script derives necessary local 5/6-cycle
constraints and enumerates the surviving coarse integer profiles.  It does not
claim that order 50 is impossible.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math

import sympy as sp

X = sp.symbols("x")


def verify_vertex_cycle_gate() -> dict[str, str]:
    tau = sp.symbols("tau", integer=True)
    excess = sp.Integer(13)

    # Average distance-layer quotient around a vertex.  The layer sizes are
    # 1,6,30,13 and tau is the number of 5-cycles through the vertex.
    quotient = sp.Matrix(
        [
            [0, 6, 0, 0],
            [1, 0, 5, 0],
            [0, 1, tau / sp.Integer(15), 5 - tau / sp.Integer(15)],
            [
                0,
                0,
                30 * (5 - tau / sp.Integer(15)) / excess,
                6 - 30 * (5 - tau / sp.Integer(15)) / excess,
            ],
        ]
    )
    characteristic = sp.factor(quotient.charpoly(X).as_expr())
    cubic = sp.factor(characteristic / (X - 6))
    expected = (
        -excess * tau * X**2
        + 6 * excess * tau
        + 15 * excess * X**3
        - 165 * excess * X
        - 30 * tau * X**2
        - 30 * tau * X
        + 150 * tau
        + 2250 * X**2
        + 2250 * X
        - 11250
    ) / (15 * excess)
    if sp.simplify(cubic - expected) != 0:
        raise AssertionError("wrong nonprincipal layer factor")

    upper_boundary = -1 + sp.sqrt(10)
    boundary_value = sp.factor(
        sp.radsimp((15 * excess * cubic).subs(X, upper_boundary))
    )
    expected_boundary = (
        -215 * tau
        + 56 * sp.sqrt(10) * tau
        - 1860 * sp.sqrt(10)
        + 7350
    )
    if sp.expand(boundary_value - expected_boundary) != 0:
        raise AssertionError("wrong boundary evaluation")
    if sp.expand(
        boundary_value.subs(tau, 39) - 9 * (-115 + 36 * sp.sqrt(10))
    ) != 0:
        raise AssertionError("wrong tau=39 boundary value")
    if not 36**2 * 10 < 115**2:
        raise AssertionError("failed exact negativity at tau=39")
    if not 56**2 * 10 < 215**2:
        raise AssertionError("failed exact monotonicity coefficient")
    if sp.expand((15 * excess * cubic).subs(X, 6) + 1500 * (tau - 75)) != 0:
        raise AssertionError("wrong value at the principal eigenvalue")

    return {
        "nonprincipal_layer_factor": str(cubic),
        "upper_boundary_evaluation": str(boundary_value),
        "conclusion": "36 <= tau(v) <= 38",
    }


def verify_two_path_gate() -> dict[str, object]:
    r = sp.symbols("r", integer=True)

    # Multiply the relevant 3x3 Gram principal submatrix by 25.  The diagonal
    # is 48; an edge entry is -2 or -27 according as that edge lies in 12 or 13
    # 5-cycles; and the endpoint entry of a 2-path is 773-25r, where
    # r=6*alpha+beta.
    diagonal = sp.Integer(48)
    low_edge = sp.Integer(-2)
    high_edge = sp.Integer(-27)
    endpoint = 773 - 25 * r

    determinants: dict[str, str] = {}
    allowed: dict[str, list[int]] = {}
    for name, left, right in (
        ("low-low", low_edge, low_edge),
        ("mixed", low_edge, high_edge),
        ("high-high", high_edge, high_edge),
    ):
        determinant = sp.factor(
            sp.Matrix(
                [
                    [diagonal, left, endpoint],
                    [left, diagonal, right],
                    [endpoint, right, diagonal],
                ]
            ).det()
        )
        determinants[name] = str(determinant)
        allowed[name] = [
            value for value in range(29, 33) if determinant.subs(r, value) >= 0
        ]

    expected_allowed = {
        "low-low": [29, 30, 31, 32],
        "mixed": [30, 31, 32],
        "high-high": [29, 30, 31],
    }
    if allowed != expected_allowed:
        raise AssertionError("wrong two-path feasibility table")

    return {
        "scaled_gram_determinants": determinants,
        "allowed_r_values": allowed,
    }


def verify_spectral_moment_gate() -> dict[str, str]:
    high_edges, six_cycles = sp.symbols(
        "m N6", integer=True, nonnegative=True
    )

    # Nonprincipal shifted adjacency moments y_i=theta_i+1.
    moments = [
        sp.Integer(49),
        sp.Integer(43),
        sp.Integer(301),
        sp.Integer(607),
        sp.Integer(2749),
        sp.Integer(6343) + 2 * high_edges,
        sp.Integer(1801) + 12 * high_edges + 12 * six_cycles,
    ]

    moment_matrix = sp.Matrix(4, 4, lambda i, j: moments[i + j])
    leading_moment = moment_matrix[:3, :3]
    final_column = moment_matrix[:3, 3]
    if sp.factor(leading_moment.det()) != 5850000:
        raise AssertionError("wrong moment determinant")
    lower_sixth_moment = sp.factor(
        (final_column.T * leading_moment.inv() * final_column)[0]
    )
    expected_lower = (
        43 * high_edges**2 - 11700 * high_edges + 128412375
    ) / 4875
    if sp.simplify(lower_sixth_moment - expected_lower) != 0:
        raise AssertionError("wrong moment lower bound")

    # Localizing matrix for 10-y^2 >= 0 on the strict WOW window.
    localizing = sp.Matrix(
        3,
        3,
        lambda i, j: 10 * moments[i + j] - moments[i + j + 2],
    )
    leading_localizing = localizing[:2, :2]
    localizing_column = localizing[:2, 2]
    if sp.factor(leading_localizing.det()) != 18000:
        raise AssertionError("wrong localizing determinant")
    upper_sixth_moment = sp.factor(
        10 * moments[4]
        - (localizing_column.T * leading_localizing.inv() * localizing_column)[0]
    )
    expected_upper = -(
        21 * high_edges**2 + 600 * high_edges - 13560500
    ) / 500
    if sp.simplify(upper_sixth_moment - expected_upper) != 0:
        raise AssertionError("wrong localizing upper bound")

    lower_six_cycles = sp.factor(
        (lower_sixth_moment - 1801 - 12 * high_edges) / 12
    )
    upper_six_cycles = sp.factor(
        (upper_sixth_moment - 1801 - 12 * high_edges) / 12
    )
    expected_cycle_lower = (
        43 * high_edges**2 - 70200 * high_edges + 119632500
    ) / 58500
    expected_cycle_upper = -(
        7 * high_edges**2 + 2200 * high_edges - 4220000
    ) / 2000
    if sp.simplify(lower_six_cycles - expected_cycle_lower) != 0:
        raise AssertionError("wrong N6 moment lower bound")
    if sp.simplify(upper_six_cycles - expected_cycle_upper) != 0:
        raise AssertionError("wrong N6 localizing upper bound")

    return {
        "moment_lower_N6": str(lower_six_cycles),
        "localizing_upper_N6": str(upper_six_cycles),
    }


def verify_global_counts() -> dict[str, str]:
    high_degree_two, high_degree_four, high_edges, degree_square_sum = sp.symbols(
        "n2 n4 m S2", integer=True, nonnegative=True
    )
    if sp.expand(
        high_edges - (high_degree_two + 2 * high_degree_four)
    ) != high_edges - high_degree_two - 2 * high_degree_four:
        raise AssertionError("bad high-edge count identity")
    if sp.expand(
        degree_square_sum - (4 * high_degree_two + 16 * high_degree_four)
    ) != degree_square_sum - 4 * high_degree_two - 16 * high_degree_four:
        raise AssertionError("bad degree-square identity")

    local_lower = sp.factor(
        (10950 + 6 * high_edges - degree_square_sum) / 6
    )
    local_upper = sp.factor(
        (26400 - 10 * high_edges - degree_square_sum) / 12
    )
    return {
        "N5": "360+m/5",
        "sum_degrees_H": "2m",
        "sum_squared_degrees_H": "4 n2+16 n4",
        "local_N6_lower": str(local_lower),
        "local_N6_upper": str(local_upper),
    }


def enumerate_integer_profiles() -> dict[str, object]:
    profiles: list[tuple[int, int, int, int, int, int]] = []
    for high_degree_two in range(51):
        for high_degree_four in range(51 - high_degree_two):
            high_degree_zero = 50 - high_degree_two - high_degree_four
            high_edges = high_degree_two + 2 * high_degree_four
            if high_edges % 5 != 0:
                continue
            degree_square_sum = 4 * high_degree_two + 16 * high_degree_four

            local_lower = Fraction(
                10950 + 6 * high_edges - degree_square_sum, 6
            )
            local_upper = Fraction(
                26400 - 10 * high_edges - degree_square_sum, 12
            )
            moment_lower = Fraction(
                43 * high_edges**2
                - 70200 * high_edges
                + 119632500,
                58500,
            )
            moment_upper = Fraction(
                4220000 - 2200 * high_edges - 7 * high_edges**2,
                2000,
            )
            lower = max(Fraction(0), local_lower, moment_lower)
            upper = min(local_upper, moment_upper)
            if math.ceil(lower) <= math.floor(upper):
                profiles.append(
                    (
                        high_degree_zero,
                        high_degree_two,
                        high_degree_four,
                        high_edges,
                        math.ceil(lower),
                        math.floor(upper),
                    )
                )

    if len(profiles) != 266:
        raise AssertionError("unexpected number of coarse profiles")
    surviving_edge_counts = sorted({profile[3] for profile in profiles})
    if surviving_edge_counts != list(range(0, 101, 5)):
        raise AssertionError("unexpected surviving high-edge counts")

    return {
        "feasible_coarse_degree_profiles": len(profiles),
        "surviving_high_edge_counts": "0,5,...,100",
        "interpretation": "necessary constraints only; order 50 is not eliminated",
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "vertex_cycle_gate": verify_vertex_cycle_gate(),
        "two_path_gate": verify_two_path_gate(),
        "global_counts": verify_global_counts(),
        "spectral_moment_gate": verify_spectral_moment_gate(),
        "integer_profile_enumeration": enumerate_integer_profiles(),
    }
    print("order-50 local feasibility verification: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
