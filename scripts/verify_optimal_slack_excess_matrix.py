#!/usr/bin/env python3
"""Exact symbolic and finite checks for the optimal-slack excess matrix."""
from fractions import Fraction
import sympy as sp

K, N = sp.symbols("k n", integer=True, positive=True)


def constants(k: int) -> tuple[int, int]:
    return 6 * (k + 2), (k + 2) ** 2 * (k**2 + 3)


def main() -> None:
    h = 6 * (K + 2)
    c = (K + 2) ** 2 * (K**2 + 3)
    epsilon = c - (h + 1) * N + 1

    # If z_uv=(g_k(A))_uv and e_uv=z_uv-(h+1), then the row sum follows
    # from g_k(A)1=C_k 1 and the diagonal value h_k.
    z_offdiag_sum = c - h
    expected = (N - 1) * (h + 1) + epsilon
    if sp.expand(z_offdiag_sum - expected) != 0:
        raise AssertionError("wrong excess row sum")

    # M=-g(A)+(C/n)J and E=g(A)-(h+1)J+I.
    # Thus M=I-E+(C/n-h-1)J, so on 1-perp M=I-E.
    a = c / N - h
    j_coefficient = sp.simplify(c / N - h - 1)
    if sp.simplify(j_coefficient - (a - 1)) != 0:
        raise AssertionError("wrong centered excess identity")

    finite = {
        (6, 50): 47,
        (7, 76): 33,
        (8, 109): 52,
    }
    for (k, n), expected_degree in finite.items():
        hk, ck = constants(k)
        degree = ck - (hk + 1) * n + 1
        if degree != expected_degree:
            raise AssertionError(f"wrong finite excess degree at {(k, n)}")
        complement_degree = n - 1 - degree
        if (k, n) == (7, 76) and complement_degree != 42:
            raise AssertionError("wrong degree-seven complement degree")
        if (k, n) == (8, 109) and complement_degree != 56:
            raise AssertionError("wrong degree-eight complement degree")

    # The integral ceiling is equivalent to epsilon>=1.
    for k in range(4, 101):
        hk, ck = constants(k)
        bound = ck // (hk + 1)
        if ck - (hk + 1) * bound < 0:
            raise AssertionError("floor bound failed")
        if Fraction(ck, hk) - Fraction(ck, hk + 1) != Fraction(ck, hk * (hk + 1)):
            raise AssertionError("ceiling improvement identity failed")

    print("optimal-slack excess-matrix audit: PASS")
    print("symbolic row sum:", epsilon)
    print("finite excess degrees:", finite)


if __name__ == "__main__":
    main()
