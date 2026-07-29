#!/usr/bin/env python3
"""Exact audit of the order-50 adjacency -2 multiplicity bound."""
from __future__ import annotations

import sympy as sp

M = sp.symbols("m", integer=True, nonnegative=True)


def main() -> None:
    traces = {
        0: 50,
        1: 0,
        2: 50 * 6,
        3: 0,
        4: 50 * 6 * (2 * 6 - 1),
    }
    expected_traces = {0: 50, 1: 0, 2: 300, 3: 0, 4: 3300}
    if traces != expected_traces:
        raise AssertionError("wrong order-50 adjacency traces")

    # Remove the principal eigenvalue 6 and M copies of -2.
    moments = [
        49 - M,
        -6 + 2 * M,
        264 - 4 * M,
        -216 + 8 * M,
        2004 - 16 * M,
    ]
    hankel = sp.Matrix(3, 3, lambda i, j: moments[i + j])
    hankel_determinant = sp.factor(hankel.det())
    expected_hankel = 3600 * (1625 - 81 * M)
    if sp.expand(hankel_determinant - expected_hankel) != 0:
        raise AssertionError("wrong Hankel determinant")

    # Localize the residual measure by 10-(x+1)^2 = 9-2x-x^2.
    localizing = sp.Matrix(
        2,
        2,
        lambda i, j: (
            9 * moments[i + j]
            - 2 * moments[i + j + 1]
            - moments[i + j + 2]
        ),
    )
    expected_localizing = sp.Matrix(
        [
            [189 - 9 * M, 18 * M - 366],
            [18 * M - 366, 804 - 36 * M],
        ]
    )
    if localizing != expected_localizing:
        raise AssertionError("wrong shifted-window localizing matrix")
    localizing_determinant = sp.factor(localizing.det())
    expected_localizing_determinant = 144 * (125 - 6 * M)
    if sp.expand(
        localizing_determinant - expected_localizing_determinant
    ) != 0:
        raise AssertionError("wrong localizing determinant")

    if 1625 // 81 != 20 or 125 // 6 != 20:
        raise AssertionError("wrong integral multiplicity floor")

    print("order-50 minus-two multiplicity audit: PASS")
    print(f"traces: {traces}")
    print(f"moments: {[str(value) for value in moments]}")
    print(f"Hankel determinant: {hankel_determinant}")
    print(f"localizing matrix: {localizing}")
    print(f"localizing determinant: {localizing_determinant}")
    print("multiplicity bound: 20")
    print("signed Gram rank bound: 30")


if __name__ == "__main__":
    main()
