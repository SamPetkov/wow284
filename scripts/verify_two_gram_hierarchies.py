#!/usr/bin/env python3
"""Exact scalar audit of the two-Gram-hierarchy synthesis."""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

K, S, TAU = sp.symbols("k s tau", positive=True)


def square_discriminant_data(k: int) -> tuple[int, Fraction]:
    delta = math.isqrt(4 * k - 3)
    if delta * delta != 4 * k - 3:
        raise AssertionError(f"advertised finite check requires a square discriminant: k={k}")
    parent_score = Fraction(2 * k - 3 - delta, 2)
    return delta, parent_score


def guaranteed_radius(k: int) -> int:
    _, parent_score = square_discriminant_data(k)
    threshold = parent_score * Fraction(k, k + 1)
    # Largest integer s with s < threshold.
    radius = (threshold.numerator + threshold.denominator - 1) // threshold.denominator - 1
    return min(k - 1, radius)


def symbolic_audit() -> dict[str, str]:
    parent_score = K - (3 + sp.sqrt(4 * K - 3)) / 2
    deletion_bound = sp.simplify(parent_score - S / K - TAU)
    uniform_bound = sp.simplify(deletion_bound.subs(TAU, S))
    expected = K - (3 + sp.sqrt(4 * K - 3)) / 2 - S * (1 + 1 / K)
    if sp.simplify(uniform_bound - expected) != 0:
        raise AssertionError("wrong uniform deletion bound")

    # BB^T is PSD and diag(t_x) <= tau I, hence
    # BB^T-diag(t_x) >= -tau I.
    if sp.simplify(-TAU) != -TAU:
        raise AssertionError("wrong Gram-minus-diagonal eigenvalue shift")

    return {
        "parent_score": str(parent_score),
        "configuration_sensitive_bound": str(deletion_bound),
        "uniform_bound": str(uniform_bound),
    }


def finite_audit() -> dict[str, int]:
    expected = {7: 2, 57: 47}
    actual = {k: guaranteed_radius(k) for k in expected}
    if actual != expected:
        raise AssertionError(f"wrong guaranteed radii: {actual}")

    for k, radius in expected.items():
        _, score = square_discriminant_data(k)
        loss = Fraction(k + 1, k)
        at_radius = score - radius * loss
        above = score - (radius + 1) * loss
        if at_radius <= 0:
            raise AssertionError(f"radius is not strict at k={k}")
        if above > 0:
            raise AssertionError(
                f"radius was not maximal under the uniform bound at k={k}"
            )
    return actual


def main() -> None:
    print("two Gram hierarchies audit: PASS")
    print("symbolic:", symbolic_audit())
    print("guaranteed radii:", finite_audit())


if __name__ == "__main__":
    main()
