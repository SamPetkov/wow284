#!/usr/bin/env python3
"""Exact arithmetic checks for the degree-seven, eight, and nine corollaries.

These checks combine the all-degree LP ceiling, regular-graph parity, the
standard Moore multiplicity obstruction, and the edge-local five-cycle bound.
No graph enumeration or floating-point eigenvalue computation is used.
"""
from __future__ import annotations

from fractions import Fraction
from math import isqrt


def lp_ceiling(k: int) -> Fraction:
    return Fraction((k + 2) * (k * k + 3), 6)


def integer_strict_upper(bound: Fraction) -> int:
    """Largest integer n satisfying n < bound."""

    return (bound.numerator - 1) // bound.denominator


def even_upper(bound: Fraction) -> int:
    """Largest even integer n satisfying n < bound."""

    upper = integer_strict_upper(bound)
    return upper if upper % 2 == 0 else upper - 1


def moore_multiplicity_obstruction(k: int) -> bool:
    """Return whether the standard Moore multiplicities are nonintegral.

    For a diameter-two degree-k Moore graph, the nonprincipal roots are
    (-1 +/- sqrt(4k-3))/2 and their multiplicities contain the nonzero term
    k(k-2)/sqrt(4k-3).  If 4k-3 is not a square, integrality is impossible.
    """

    discriminant = 4 * k - 3
    return isqrt(discriminant) ** 2 != discriminant and k * (k - 2) != 0


def verify_degree_seven() -> None:
    bound = lp_ceiling(7)
    if bound != 78:
        raise AssertionError(bound)
    if even_upper(bound) != 76:
        raise AssertionError("degree-seven parity bound failed")
    if moore_multiplicity_obstruction(7):
        raise AssertionError("degree seven should not be multiplicity-obstructed")


def verify_degree_eight() -> None:
    k = 8
    bound = lp_ceiling(k)
    if bound != Fraction(335, 3):
        raise AssertionError(bound)
    if integer_strict_upper(bound) != 111:
        raise AssertionError("degree-eight LP integer bound failed")
    if not moore_multiplicity_obstruction(k):
        raise AssertionError("degree-eight Moore obstruction failed")

    n = 111
    spectral_lower = 2 * k - 2
    spectral_upper = (
        Fraction(2 * (k + 2) ** 2 * (k * k + 3), n) - 10 * k - 26
    )
    if not (spectral_lower <= spectral_upper < spectral_lower + 1):
        raise AssertionError((spectral_lower, spectral_upper))

    sigma = spectral_lower
    edges = k * n // 2
    incidences = sigma * edges
    if incidences != 6216:
        raise AssertionError(incidences)
    if incidences % 5 == 0:
        raise AssertionError("degree-eight edge-cycle contradiction disappeared")


def verify_degree_nine() -> None:
    bound = lp_ceiling(9)
    if bound != 154:
        raise AssertionError(bound)
    if even_upper(bound) != 152:
        raise AssertionError("degree-nine parity bound failed")
    if not moore_multiplicity_obstruction(9):
        raise AssertionError("degree-nine Moore obstruction failed")


def main() -> None:
    verify_degree_seven()
    verify_degree_eight()
    verify_degree_nine()
    print("low-degree regular-window verification: PASS")
    print("degree 7: diameter-three order <= 76; diameter-two order = 50")
    print("degree 8: global order <= 110")
    print("degree 9: global order <= 152")


if __name__ == "__main__":
    main()
