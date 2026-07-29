#!/usr/bin/env python3
"""Exact arithmetic audit of equality in the three-to-one excess bound."""
from __future__ import annotations

import sympy as sp

K = sp.symbols("k", integer=True, positive=True)


def main() -> None:
    c_value = (K + 2) ** 2 * (K**2 + 3)
    modulus = 18 * K + 41
    quotient, remainder = sp.div(sp.expand(18**4 * c_value), modulus)
    expected_quotient = (
        5832 * K**3
        + 10044 * K**2
        + 17946 * K
        + 29107
    )
    if sp.expand(quotient - expected_quotient) != 0 or remainder != 66325:
        raise AssertionError("wrong fixed remainder for equality")
    if sp.factorint(66325) != {5: 2, 7: 1, 379: 1}:
        raise AssertionError("wrong factorization of the equality remainder")

    admissible_moduli = [
        divisor
        for divisor in sp.divisors(66325)
        if divisor >= 18 * 6 + 41 and divisor % 18 == 5
    ]
    if admissible_moduli != [1895]:
        raise AssertionError(
            f"wrong admissible equality moduli: {admissible_moduli}"
        )

    degree = (admissible_moduli[0] - 41) // 18
    c_integer = int(c_value.subs(K, degree))
    excess = c_integer // admissible_moduli[0]
    order = 3 * excess
    if (degree, c_integer, excess, order) != (
        103,
        116997300,
        61740,
        185220,
    ):
        raise AssertionError("wrong equality parameter triple")
    if degree * order % 2:
        raise AssertionError(
            "the unique arithmetic equality case violates handshake parity"
        )

    r_value = 2 * c_integer - (12 * degree + 27) * order
    if r_value != excess or order != 3 * r_value:
        raise AssertionError("the equality parameters do not satisfy n=3r")

    print("three-to-one equality-rigidity audit: PASS")
    print("fixed remainder: 66325 = 5^2 * 7 * 379")
    print("unique arithmetic equality triple: (k,n,r)=(103,185220,61740)")


if __name__ == "__main__":
    main()
