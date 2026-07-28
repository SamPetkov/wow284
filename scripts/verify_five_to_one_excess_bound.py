#!/usr/bin/env python3
"""Exact arithmetic audit of the five-to-one integral excess theorem.

The external Cameron--Goethals--Seidel--Shult classification is treated as an
input.  This script checks every project-derived identity and every finite
arithmetic reduction after that input.
"""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

K, N, R = sp.symbols("k n r", integer=True, positive=True)


def symbolic_audit() -> dict[str, str]:
    h = 6 * (K + 2)
    c = (K + 2) ** 2 * (K**2 + 3)
    epsilon = c - (h + 1) * N + 1
    r = sp.expand(2 * epsilon - N - 2)
    expected_r = sp.expand(2 * c - (2 * h + 3) * N)
    if sp.expand(r - expected_r) != 0:
        raise AssertionError("wrong excess-defect identity")

    rho = sp.Rational(1, 2) + R / (2 * N)
    delta = sp.expand(4 * rho - 2)
    if delta != 2 * R / N:
        raise AssertionError("wrong doubled-edge Gram norm")

    gram_rhs = sp.expand((2 * R / N) * (sp.Rational(3, 2) + R / (2 * N)))
    alternative = sp.expand((1 - R / N) ** 2)
    if sp.factor(alternative - gram_rhs) != (N - 5 * R) / N:
        raise AssertionError("wrong Cauchy--Schwarz threshold")

    d = sp.simplify(N - 1 - (N + R + 2) / 2)
    if d != (N - R - 4) / 2:
        raise AssertionError("wrong complement degree")

    order_bound = sp.factor(5 * c / (5 * h + 8))
    lp = sp.factor(c / h)
    improvement = sp.factor(lp - order_bound)
    expected_improvement = sp.factor(
        2 * (K + 2) * (K**2 + 3) / (3 * (15 * K + 34))
    )
    if sp.simplify(improvement - expected_improvement) != 0:
        raise AssertionError("wrong asymptotic improvement identity")

    return {
        "r": str(r),
        "double_edge_norm": str(delta),
        "cauchy_margin": str(alternative - gram_rhs),
        "complement_degree": str(d),
        "order_bound": str(order_bound),
        "improvement": str(improvement),
    }


def reciprocal_enumeration() -> dict[str, object]:
    connected: list[tuple[int, int]] = []
    for b in range(2, 100):
        for a in range(b, 100):
            value = Fraction(1, a) + Fraction(1, b)
            if Fraction(2, 5) < value < Fraction(1, 2):
                connected.append((a, b))
    expected_connected = [(a, 3) for a in range(7, 15)] + [(5, 4), (6, 4)]
    if connected != expected_connected:
        raise AssertionError(f"wrong connected reciprocal list: {connected}")
    large_products = [pair for pair in connected if pair[0] * pair[1] >= 38]
    if large_products != [(13, 3), (14, 3)]:
        raise AssertionError("wrong large connected part-size cases")

    component: list[tuple[int, int]] = []
    for b in range(2, 100):
        for a in range(b, 100):
            if Fraction(1, a) + Fraction(1, b) > Fraction(3, 5):
                component.append((a, b))
    expected_component = [(a, 2) for a in range(2, 10)] + [(3, 3)]
    if component != expected_component:
        raise AssertionError(f"wrong component reciprocal list: {component}")
    if max(a * b for a, b in component) != 18:
        raise AssertionError("wrong component product maximum")

    return {
        "connected_pairs": connected,
        "connected_large_pairs": large_products,
        "component_pairs": component,
        "component_product_max": 18,
    }


def low_degree_vacuity() -> dict[int, list[tuple[int, int, int]]]:
    report: dict[int, list[tuple[int, int, int]]] = {}
    for k in (6, 7, 8):
        h = 6 * (k + 2)
        c = (k + 2) ** 2 * (k**2 + 3)
        upper = math.floor(Fraction(c, h))
        surviving: list[tuple[int, int, int]] = []
        for n in range(k * k + 2, upper + 1):
            if (k * n) % 2:
                continue
            epsilon = c - (h + 1) * n + 1
            r = 2 * epsilon - n - 2
            if r > 0 and n > 5 * r:
                surviving.append((n, epsilon, r))
        if surviving:
            raise AssertionError(f"unexpected small-degree case at k={k}: {surviving}")
        report[k] = surviving
    return report


def exceptional_connected_cases() -> dict[str, int]:
    # The reciprocal enumeration leaves only (a,b)=(13,3) and (14,3).
    cases = {(13, 3): (39, 7), (14, 3): (42, 8)}
    for (a, b), (n, r) in cases.items():
        reciprocal = Fraction(1, a) + Fraction(1, b)
        if reciprocal != Fraction(n - r, 2 * n):
            raise AssertionError("wrong exceptional reciprocal identity")
        if n > a * b:
            raise AssertionError("part-size simplicity check failed")
        # n >= k^2+2 leaves only k=6; its exact r is much larger.
        possible_k = [k for k in range(6, 100) if k * k + 2 <= n]
        if possible_k != [6]:
            raise AssertionError("wrong radius-two degree reduction")
        k = 6
        h = 6 * (k + 2)
        c = (k + 2) ** 2 * (k**2 + 3)
        actual_r = 2 * c - (2 * h + 3) * n
        if actual_r == r:
            raise AssertionError("exceptional connected case survived")
    return {"n39_actual_r": 2 * 2496 - 99 * 39, "n42_actual_r": 2 * 2496 - 99 * 42}


def order_table() -> dict[int, int]:
    expected = {
        6: 50,
        7: 75,
        8: 108,
        9: 150,
        10: 201,
        11: 263,
        12: 336,
        13: 422,
        14: 521,
        15: 636,
        16: 765,
        17: 911,
        18: 1075,
        19: 1258,
        20: 1459,
    }
    actual: dict[int, int] = {}
    for k in expected:
        h = 6 * (k + 2)
        c = (k + 2) ** 2 * (k**2 + 3)
        actual[k] = (5 * c) // (5 * h + 8)
    if actual != expected:
        raise AssertionError(f"wrong five-to-one order table: {actual}")
    return actual


def main() -> None:
    report = {
        "symbolic": symbolic_audit(),
        "reciprocal_enumeration": reciprocal_enumeration(),
        "small_degree_vacuity": low_degree_vacuity(),
        "exceptional_connected_cases": exceptional_connected_cases(),
        "order_table": order_table(),
        "external_input": (
            "regular least-eigenvalue-at-least-minus-two classification: "
            "line graph, cocktail-party graph, or order at most 28"
        ),
    }
    print("five-to-one integral excess audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
