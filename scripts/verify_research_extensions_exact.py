#!/usr/bin/env python3
"""Exact entrypoint for the WOW-284 structural extension certificates.

This wrapper deliberately does not call the legacy
``verify_research_extensions.verify_operator_identity`` helper, whose historical
reporting path used floating-point ordering of algebraic eigenvalues. The
operator certificate below checks exact characteristic polynomials instead.
"""
from __future__ import annotations

import json
import sympy as sp
import verify_research_extensions as legacy

X = sp.symbols("x")


def verify_operator_identity_exact(graph: legacy.Graph) -> dict[str, object]:
    degrees = {len(row) for row in graph}
    assert degrees == {6}
    k = 6
    assert legacy.girth(graph) >= 5
    d = legacy.distance_matrix(graph)
    assert max(d) == 3
    a = legacy.adjacency_matrix(graph)
    n = len(graph)
    identity, ones = sp.eye(n), sp.ones(n)
    assert d == 3 * ones + (k - 3) * identity - 2 * a - a * a
    assert d + k * identity == (
        3 * ones + (2 * k - 2) * identity - (a + identity) ** 2
    )

    if n == 40:
        expected_a = (
            (X - 6) * (X - 2) ** 18 * (X - 1) ** 4
            * (X + 2) ** 5 * (X + 3) ** 12
        )
        expected_d = (X - 75) * (X - 3) ** 5 * X**16 * (X + 5) ** 18
        nonprincipal = (2, 1, -2, -3)
        principal_distance = 75
    elif n == 42:
        expected_a = (X - 6) * (X - 2) ** 21 * (X + 1) ** 6 * (X + 3) ** 14
        expected_d = (X - 81) * (X - 4) ** 6 * X**14 * (X + 5) ** 21
        nonprincipal = (2, -1, -3)
        principal_distance = 81
    else:
        raise AssertionError(f"unexpected operator-certificate order: {n}")

    assert sp.Poly(a.charpoly(X).as_expr() - expected_a, X).is_zero
    assert sp.Poly(d.charpoly(X).as_expr() - expected_d, X).is_zero
    radius_sq = max((theta + 1) ** 2 for theta in nonprincipal)
    assert radius_sq == 9
    least = sp.Integer(k - 2 - radius_sq)
    score = sp.Integer(k) + least
    assert least == -5
    assert score == 1
    assert expected_d.subs(X, least) == 0
    assert principal_distance > least
    return {
        "order": n,
        "degree": k,
        "least_distance_eigenvalue": str(least),
        "score": str(score),
        "shifted_adjacency_radius_squared": str(radius_sq),
        "adjacency_characteristic_polynomial": str(sp.factor(expected_a)),
        "distance_characteristic_polynomial": str(sp.factor(expected_d)),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    full = legacy.hoffman_singleton()
    g40 = legacy.graph40(full)
    g42 = legacy.graph42(full)
    for graph in (
        full,
        g40,
        g42,
        legacy.induced(full, {0})[0],
        legacy.induced(full, {0, 1})[0],
    ):
        assert legacy.girth(graph) >= 5
        legacy.verify_radius_two_identity(graph)

    result = {
        "radius_two_dual_degree_identity": "PASS on five independent finite representatives",
        "diameter_three_operator_identity": {
            "order_40": verify_operator_identity_exact(g40),
            "order_42": verify_operator_identity_exact(g42),
        },
        "concrete_punctures": legacy.verify_concrete_punctures(full),
        "symbolic_punctured_moore": legacy.verify_symbolic_punctured_moore(),
        "deletion_stability_symbolics": legacy.verify_deletion_stability_symbolics(),
        "moment_and_layer_bounds": legacy.verify_moment_and_layer_bounds(),
        "higher_diameter_polynomials": legacy.verify_higher_diameter_polynomials(),
    }
    print("verified research extensions (exact entrypoint): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
