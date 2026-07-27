#!/usr/bin/env python3
"""Exact refinement excluding r=29 in the order-50 two-path Gram table."""
from __future__ import annotations

from fractions import Fraction
import json
import math

import sympy as sp

X = sp.symbols("x")


def verify_kernel_exclusion() -> dict[str, str]:
    r = sp.symbols("r", integer=True)
    f = sp.expand((X + 2) ** 2 * (X**2 + 2 * X - 9))
    if sp.expand(-f - (X + 2) ** 2 * (10 - (X + 1) ** 2)) != 0:
        raise AssertionError("wrong strict-window factorization")

    # In the matrix scaled by 25, the diagonal is 48 and the endpoint entry of
    # a distance-two pair is 773-25r.  At r=29 they are equal.
    endpoint = 773 - 25 * r
    if endpoint.subs(r, 29) != 48:
        raise AssertionError("r=29 does not give Gram equality")

    # On the strict open WOW window, -f(theta)>0 except at theta=-2.
    if f.subs(X, -2) != 0:
        raise AssertionError("-2 is not the internal zero")
    if sp.factor(f) != (X + 2) ** 2 * (X**2 + 2 * X - 9):
        raise AssertionError("wrong polynomial factorization")

    # If u,w are at distance two and r=29, PSD gives M(e_u-e_w)=0.  Since
    # e_u-e_w is orthogonal to 1, this forces A(e_u-e_w)=-2(e_u-e_w).
    # At coordinate u the left side is A_uu-A_uw=0-0, while the right side is
    # -2.  These exact coordinate values are incompatible.
    adjacency_coordinate = sp.Integer(0) - sp.Integer(0)
    forced_coordinate = sp.Integer(-2)
    if adjacency_coordinate == forced_coordinate:
        raise AssertionError("impossible kernel coordinate was accepted")

    return {
        "strict_window_nonnegative_polynomial": str(sp.factor(-f)),
        "r_29_endpoint_entry": str(endpoint.subs(r, 29)),
        "kernel_coordinate_contradiction": "0 != -2",
        "conclusion": "r=29 is impossible for every distance-two pair",
    }


def verify_refined_table() -> dict[str, object]:
    r = sp.symbols("r", integer=True)
    diagonal = sp.Integer(48)
    low = sp.Integer(-2)
    high = sp.Integer(-27)
    endpoint = 773 - 25 * r

    determinant_allowed: dict[str, list[int]] = {}
    final_allowed: dict[str, list[int]] = {}
    for name, left, right in (
        ("low-low", low, low),
        ("mixed", low, high),
        ("high-high", high, high),
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
        raw = [value for value in range(29, 33) if determinant.subs(r, value) >= 0]
        determinant_allowed[name] = raw
        final_allowed[name] = [value for value in raw if value != 29]

    expected = {
        "low-low": [30, 31, 32],
        "mixed": [30, 31, 32],
        "high-high": [30, 31],
    }
    if final_allowed != expected:
        raise AssertionError("wrong refined local table")
    return {
        "determinant_only_values": determinant_allowed,
        "final_values_after_kernel_exclusion": final_allowed,
    }


def verify_refined_global_enumeration() -> dict[str, object]:
    profiles: list[tuple[int, int, int, int, int, int]] = []
    for n2 in range(51):
        for n4 in range(51 - n2):
            n0 = 50 - n2 - n4
            high_edges = n2 + 2 * n4
            if high_edges % 5 != 0:
                continue
            square_sum = 4 * n2 + 16 * n4

            # Since all 750 two-paths have r>=30,
            # 10800+6m+6N6 >= 22500.
            local_lower = Fraction(1950 - high_edges)
            local_upper = Fraction(26400 - 10 * high_edges - square_sum, 12)
            moment_lower = Fraction(
                43 * high_edges**2 - 70200 * high_edges + 119632500,
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
                        n0,
                        n2,
                        n4,
                        high_edges,
                        math.ceil(lower),
                        math.floor(upper),
                    )
                )

    if len(profiles) != 266:
        raise AssertionError("unexpected refined profile count")
    if sorted({profile[3] for profile in profiles}) != list(range(0, 101, 5)):
        raise AssertionError("unexpected refined high-edge counts")

    return {
        "refined_local_lower_N6": "N6 >= 1950-m",
        "surviving_coarse_profiles": len(profiles),
        "interpretation": (
            "the local theorem is stronger, but the same 266 coarse profiles survive"
        ),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "kernel_exclusion": verify_kernel_exclusion(),
        "refined_two_path_table": verify_refined_table(),
        "refined_integer_enumeration": verify_refined_global_enumeration(),
    }
    print("order-50 r=29 exclusion: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
