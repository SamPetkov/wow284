#!/usr/bin/env python3
"""Exact finite audit excluding an unsigned order-50 signed complement."""
from __future__ import annotations

from functools import lru_cache

import sympy as sp

X = sp.symbols("x")
G6 = (X + 2) ** 2 * ((X + 1) ** 2 - 10)


def key(poly: sp.Poly) -> tuple[sp.Rational, ...]:
    return tuple(poly.monic().all_coeffs())


@lru_cache(maxsize=None)
def cycle_polynomial(length: int) -> sp.Poly:
    expression = sp.expand(2 * sp.chebyshevt(length, X / 2) - 2)
    polynomial = sp.Poly(expression, X, domain=sp.QQ)
    if polynomial.degree() != length or polynomial.LC() != 1:
        raise AssertionError(f"wrong cycle characteristic polynomial at {length}")
    return polynomial


def factor_inventory() -> tuple[
    dict[int, list[tuple[tuple[sp.Rational, ...], int]]],
    dict[tuple[sp.Rational, ...], sp.Poly],
]:
    inventory: dict[int, list[tuple[tuple[sp.Rational, ...], int]]] = {}
    factors: dict[tuple[sp.Rational, ...], sp.Poly] = {}
    for length in range(3, 51):
        factor_list = sp.factor_list(cycle_polynomial(length).as_expr())[1]
        entries: list[tuple[tuple[sp.Rational, ...], int]] = []
        reconstructed = sp.Integer(1)
        for expression, exponent in factor_list:
            polynomial = sp.Poly(expression, X, domain=sp.QQ).monic()
            identifier = key(polynomial)
            factors[identifier] = polynomial
            entries.append((identifier, exponent))
            reconstructed *= polynomial.as_expr() ** exponent
        if sp.expand(reconstructed - cycle_polynomial(length).as_expr()) != 0:
            raise AssertionError(f"cycle factor reconstruction failed at {length}")
        inventory[length] = entries
    return inventory, factors


def composed_factor_audit(
    inventory: dict[int, list[tuple[tuple[sp.Rational, ...], int]]],
    factors: dict[tuple[sp.Rational, ...], sp.Poly],
) -> dict[str, object]:
    plus = key(sp.Poly(X - 2, X, domain=sp.QQ))
    minus = key(sp.Poly(X + 2, X, domain=sp.QQ))

    non_special_exponents: set[int] = set()
    first_appearance: dict[int, tuple[sp.Rational, ...]] = {}
    seen: set[tuple[sp.Rational, ...]] = {plus, minus}

    for length in range(3, 51):
        new_candidates: list[tuple[sp.Rational, ...]] = []
        for identifier, exponent in inventory[length]:
            if identifier in {plus, minus}:
                continue
            non_special_exponents.add(exponent)
            if identifier not in seen:
                new_candidates.append(identifier)
        if not new_candidates:
            raise AssertionError(f"no first-appearance factor at cycle length {length}")
        first_appearance[length] = new_candidates[0]
        seen.update(identifier for identifier, _ in inventory[length])

    if non_special_exponents != {2}:
        raise AssertionError(
            f"non-special cycle exponents are not uniformly two: {non_special_exponents}"
        )

    composition_degrees: dict[int, int] = {}
    checked = 0
    for identifier, polynomial in factors.items():
        if identifier in {plus, minus}:
            continue
        composed = sp.Poly(
            sp.expand(polynomial.as_expr().subs(X, -2 - G6)),
            X,
            domain=sp.QQ,
        )
        factor_list = sp.factor_list(composed.as_expr())[1]
        if len(factor_list) != 1 or factor_list[0][1] != 1:
            raise AssertionError(
                f"composed polynomial reducible for {polynomial.as_expr()}"
            )
        factor = sp.Poly(factor_list[0][0], X, domain=sp.QQ)
        expected_degree = 4 * polynomial.degree()
        if factor.degree() != expected_degree:
            raise AssertionError(
                f"wrong composed degree for {polynomial.as_expr()}: {factor.degree()}"
            )
        composition_degrees[polynomial.degree()] = expected_degree
        checked += 1

    return {
        "cycle_lengths": 48,
        "distinct_cycle_factors": len(factors),
        "non_special_factors_checked": checked,
        "non_special_exponent": 2,
        "first_appearance_lengths": len(first_appearance),
        "composition_degree_map": composition_degrees,
    }


def cycle_parity_audit(
    inventory: dict[int, list[tuple[tuple[sp.Rational, ...], int]]],
    factors: dict[tuple[sp.Rational, ...], sp.Poly],
) -> dict[str, object]:
    plus = key(sp.Poly(X - 2, X, domain=sp.QQ))
    minus = key(sp.Poly(X + 2, X, domain=sp.QQ))

    first_appearance: dict[int, tuple[sp.Rational, ...]] = {}
    seen: set[tuple[sp.Rational, ...]] = {plus, minus}
    for length in range(3, 51):
        candidates = [
            identifier
            for identifier, _ in inventory[length]
            if identifier not in {plus, minus} and identifier not in seen
        ]
        if not candidates:
            raise AssertionError(f"missing primitive factor at {length}")
        first_appearance[length] = candidates[0]
        seen.update(identifier for identifier, _ in inventory[length])

    # Exact exhaustive control: no partition of 50 into cycle lengths >=3 can
    # satisfy both the quartic-module exponent conditions and the eigenvalue-2
    # parity condition. This independently checks the descending induction.
    compatible: list[tuple[int, ...]] = []

    def inspect_partition(parts: tuple[int, ...]) -> None:
        exponents: dict[tuple[sp.Rational, ...], int] = {}
        for length in parts:
            for identifier, exponent in inventory[length]:
                exponents[identifier] = exponents.get(identifier, 0) + exponent

        cycles = len(parts)
        # The global all-ones line consumes one copy of eigenvalue 2. The
        # residual space is a sum of irreducible quadratic modules.
        if (cycles - 1) % 2:
            return

        for identifier, exponent in exponents.items():
            if identifier in {plus, minus}:
                continue
            if exponent % 4:
                return
        compatible.append(parts)

    def generate(remaining: int, minimum: int, parts: tuple[int, ...]) -> None:
        if remaining == 0:
            inspect_partition(parts)
            return
        for length in range(minimum, remaining + 1):
            if length < 3:
                continue
            generate(remaining - length, length, parts + (length,))

    generate(50, 3, ())
    if compatible:
        raise AssertionError(f"compatible unsigned cycle partitions survived: {compatible}")

    # Check the explicit eigenvalue-two annihilator.
    residual = sp.factor(G6 + 4)
    expected = (X**2 + 4 * X + 2) * (X**2 + 2 * X - 4)
    if sp.expand(residual - expected) != 0:
        raise AssertionError("wrong residual eigenvalue-two factorization")
    for factor in (X**2 + 4 * X + 2, X**2 + 2 * X - 4):
        if sp.factor(factor) != factor:
            raise AssertionError("residual quadratic is reducible")

    return {
        "partitions_checked": "all partitions of 50 with parts at least 3",
        "compatible_partitions": compatible,
        "cycle_count_requirement_from_nonprincipal_factors": "even",
        "cycle_count_requirement_from_eigenvalue_two": "odd",
    }


def order50_bridge_audit() -> dict[str, int]:
    k, n = 6, 50
    c = (k + 2) ** 2 * (k**2 + 3)
    r = 2 * c - (12 * k + 27) * n
    signed_degree = (n - r - 4) // 2
    coefficient = 6 * (k + 2) + 2
    if (c, r, signed_degree, coefficient) != (2496, 42, 2, 50):
        raise AssertionError("wrong order-50 signed-complement specialization")
    return {
        "C_6": c,
        "excess_parameter": r,
        "signed_degree": signed_degree,
        "J_coefficient": coefficient,
    }


def main() -> None:
    inventory, factors = factor_inventory()
    report = {
        "order50": order50_bridge_audit(),
        "composed_factors": composed_factor_audit(inventory, factors),
        "cycle_parity": cycle_parity_audit(inventory, factors),
    }
    print("order-50 unsigned-complement exclusion audit: PASS")
    for key_name, value in report.items():
        print(f"{key_name}: {value}")


if __name__ == "__main__":
    main()
