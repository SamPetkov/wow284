#!/usr/bin/env python3
"""Exact trace audit excluding an unsigned order-50 signed complement."""
from __future__ import annotations

import sympy as sp

X = sp.symbols("x")
G6 = (X + 2) ** 2 * ((X + 1) ** 2 - 10)


def polynomial_key(poly: sp.Poly) -> tuple[sp.Rational, ...]:
    return tuple(poly.monic().all_coeffs())


def cycle_factor_inventory() -> tuple[
    dict[int, list[tuple[tuple[sp.Rational, ...], int]]],
    dict[tuple[sp.Rational, ...], sp.Poly],
]:
    inventory: dict[int, list[tuple[tuple[sp.Rational, ...], int]]] = {}
    factors: dict[tuple[sp.Rational, ...], sp.Poly] = {}

    for length in range(3, 51):
        characteristic = sp.Poly(
            sp.expand(2 * sp.chebyshevt(length, X / 2) - 2),
            X,
            domain=sp.QQ,
        )
        if characteristic.degree() != length or characteristic.LC() != 1:
            raise AssertionError(f"wrong cycle polynomial at length {length}")

        reconstructed = sp.Integer(1)
        entries: list[tuple[tuple[sp.Rational, ...], int]] = []
        for expression, exponent in sp.factor_list(characteristic.as_expr())[1]:
            factor = sp.Poly(expression, X, domain=sp.QQ).monic()
            identifier = polynomial_key(factor)
            factors[identifier] = factor
            entries.append((identifier, exponent))
            reconstructed *= factor.as_expr() ** exponent
        if sp.expand(reconstructed - characteristic.as_expr()) != 0:
            raise AssertionError(f"cycle factor reconstruction failed at {length}")
        inventory[length] = entries

    return inventory, factors


def non_special_primary_audit(
    inventory: dict[int, list[tuple[tuple[sp.Rational, ...], int]]],
    factors: dict[tuple[sp.Rational, ...], sp.Poly],
) -> dict[str, object]:
    plus = polynomial_key(sp.Poly(X - 2, X, domain=sp.QQ))
    minus = polynomial_key(sp.Poly(X + 2, X, domain=sp.QQ))

    checked = 0
    degree_trace_map: dict[int, tuple[int, int]] = {}
    occurrence_count = 0

    for length, entries in inventory.items():
        for identifier, exponent in entries:
            if identifier in {plus, minus}:
                continue
            occurrence_count += 1
            factor = factors[identifier]
            composed = sp.Poly(
                sp.expand(factor.as_expr().subs(X, -2 - G6)),
                X,
                domain=sp.QQ,
            )
            factorization = sp.factor_list(composed.as_expr())[1]
            if len(factorization) != 1 or factorization[0][1] != 1:
                raise AssertionError(
                    f"reducible composed factor at cycle length {length}: "
                    f"{factor.as_expr()}"
                )

            monic = composed.monic()
            expected_degree = 4 * factor.degree()
            if monic.degree() != expected_degree:
                raise AssertionError("wrong composed degree")
            root_sum = -monic.all_coeffs()[1]
            expected_root_sum = -6 * factor.degree()
            if root_sum != expected_root_sum:
                raise AssertionError(
                    f"wrong composed root sum for {factor.as_expr()}: {root_sum}"
                )
            degree_trace_map[factor.degree()] = (expected_degree, int(root_sum))
            checked += 1

    if checked == 0 or occurrence_count == 0:
        raise AssertionError("no non-special cycle factors checked")

    return {
        "cycle_lengths": len(inventory),
        "distinct_cycle_factors": len(factors),
        "non_special_occurrences_checked": checked,
        "degree_trace_map": degree_trace_map,
    }


def special_factor_audit() -> dict[str, object]:
    factorization = sp.factor(G6 + 4)
    expected = (X + 4) * (X**3 + 2 * X**2 - 8 * X - 4)
    if sp.expand(factorization - expected) != 0:
        raise AssertionError(f"wrong factorization of g_6+4: {factorization}")

    cubic = sp.Poly(X**3 + 2 * X**2 - 8 * X - 4, X, domain=sp.QQ)
    cubic_factors = sp.factor_list(cubic.as_expr())[1]
    if len(cubic_factors) != 1 or cubic_factors[0][0].as_poly(X).degree() != 3:
        raise AssertionError("residual cubic is reducible")
    root_sum = -cubic.all_coeffs()[1]
    if root_sum != -2:
        raise AssertionError("wrong residual cubic root sum")

    zeros = [
        -2,
        -1 - sp.sqrt(10),
        -1 + sp.sqrt(10),
    ]
    if any(sp.simplify(G6.subs(X, value)) != 0 for value in zeros):
        raise AssertionError("wrong zeros of g_6")

    return {
        "factorization": str(factorization),
        "cubic_irreducible": True,
        "cubic_root_sum": int(root_sum),
        "open_window_zero": -2,
    }


def trace_contradiction_audit() -> dict[str, str]:
    a, b, c, m = sp.symbols("a b c m", integer=True, nonnegative=True)

    trace = sp.expand(
        6
        - 2 * m
        - 4 * a
        - 2 * b
        - sp.Rational(3, 2) * (50 - c - m)
    )
    doubled = sp.expand(2 * trace)
    expected_doubled = -138 - m - 8 * a - 4 * b + 3 * c
    if doubled != expected_doubled:
        raise AssertionError("wrong global adjacency trace identity")

    substituted = sp.expand(
        expected_doubled.subs(c, a + 3 * b + 1)
    )
    expected_substituted = -135 - m - 5 * a + 5 * b
    if substituted != expected_substituted:
        raise AssertionError("wrong special-primary substitution")

    solved_m = sp.solve(sp.Eq(expected_substituted, 0), m)
    if solved_m != [-5 * a + 5 * b - 135]:
        raise AssertionError(f"wrong multiplicity relation: {solved_m}")

    # m>=0 forces b>=a+27; then c=a+3b+1>=4a+82>50.
    lower_c = sp.expand((a + 3 * b + 1).subs(b, a + 27))
    if lower_c != 4 * a + 82:
        raise AssertionError("wrong cycle-component lower bound")
    if int(lower_c.subs(a, 0)) <= 50:
        raise AssertionError("dimension contradiction disappeared")

    return {
        "twice_trace": str(doubled),
        "multiplicity_relation": "m=5(b-a-27)",
        "minimum_cycle_components": str(lower_c),
    }


def order50_bridge_audit() -> dict[str, int]:
    k, n = 6, 50
    c_value = (k + 2) ** 2 * (k**2 + 3)
    r_value = 2 * c_value - (12 * k + 27) * n
    signed_degree = (n - r_value - 4) // 2
    coefficient = 6 * (k + 2) + 2
    if (c_value, r_value, signed_degree, coefficient) != (2496, 42, 2, 50):
        raise AssertionError("wrong order-50 signed-complement specialization")
    return {
        "C_6": c_value,
        "excess_parameter": r_value,
        "signed_degree": signed_degree,
        "J_coefficient": coefficient,
    }


def main() -> None:
    inventory, factors = cycle_factor_inventory()
    report = {
        "order50": order50_bridge_audit(),
        "non_special_primary": non_special_primary_audit(inventory, factors),
        "special_factors": special_factor_audit(),
        "trace_contradiction": trace_contradiction_audit(),
    }
    print("order-50 unsigned-complement trace audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
