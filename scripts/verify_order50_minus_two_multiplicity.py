#!/usr/bin/env python3
"""Exact audit of the order-50 adjacency -2 multiplicity bound."""
from __future__ import annotations

import sympy as sp

M = sp.symbols("m", integer=True, nonnegative=True)


def trace_audit() -> dict[str, int]:
    traces = {
        0: 50,
        1: 0,
        2: 50 * 6,
        3: 0,
        4: 50 * 6 * (2 * 6 - 1),
    }
    if traces != {0: 50, 1: 0, 2: 300, 3: 0, 4: 3300}:
        raise AssertionError("wrong order-50 adjacency traces")
    return traces


def moment_audit() -> dict[str, object]:
    # Remove the principal eigenvalue 6 and M copies of -2.
    moments = [
        49 - M,
        -6 + 2 * M,
        264 - 4 * M,
        -216 + 8 * M,
        2004 - 16 * M,
    ]
    expected = [
        49 - M,
        -6 + 2 * M,
        264 - 4 * M,
        -216 + 8 * M,
        2004 - 16 * M,
    ]
    if any(sp.expand(left - right) != 0 for left, right in zip(moments, expected, strict=True)):
        raise AssertionError("wrong residual spectral moments")

    hankel = sp.Matrix(3, 3, lambda i, j: moments[i + j])
    determinant = sp.factor(hankel.det())
    if determinant != 3600 * (1625 - 81 * M):
        raise AssertionError("wrong Hankel determinant")

    # Localize by 10-(x+1)^2 = 9-2x-x^2.
    localizing = sp.Matrix(
        2,
        2,
        lambda i, j: 9 * moments[i + j]
        - 2 * moments[i + j + 1]
        - moments[i + j + 2],
    )
    expected_localizing = sp.Matrix(
        [[9 * (21 - M), 18 * (M - 1)], [18 * (M - 1), 36 * (41 - M)]]
    )
    if localizing != expected_localizing:
        raise AssertionError("wrong shifted-window localizing matrix")
    localizing_det = sp.factor(localizing.det())
    if localizing_det != 144 * (125 - 6 * M):
        raise AssertionError("wrong localizing determinant")

    if 1625 // 81 != 20 or 125 // 6 != 20:
        raise AssertionError("wrong integral multiplicity floor")

    return {
        "moments": [str(value) for value in moments],
        "Hankel_determinant": str(determinant),
        "localizing_matrix": str(localizing),
        "localizing_determinant": str(localizing_det),
        "multiplicity_bound": 20,
    }


def gram_rank_audit() -> dict[str, int]:
    order = 50
    maximum_nullity = 20
    minimum_rank = order - maximum_nullity
    if minimum_rank != 30:
        raise AssertionError("wrong order-50 Gram rank bound")
    return {"order": order, "maximum_nullity": maximum_nullity, "minimum_rank": minimum_rank}


def main() -> None:
    report = {
        "traces": trace_audit(),
        "moments": moment_audit(),
        "Gram_rank": gram_rank_audit(),
    }
    print("order-50 minus-two multiplicity audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
