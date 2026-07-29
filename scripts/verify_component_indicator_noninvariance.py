#!/usr/bin/env python3
"""Exact counterexample to commutation implying component equitability."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    identity4 = sp.eye(4)
    h = sp.ones(4, 4) - 2 * identity4
    zero4 = sp.zeros(4, 4)
    t = zero4.row_join(h).col_join(h.row_join(zero4))
    if any(
        t[row, column] not in {-1, 0, 1}
        for row in range(8)
        for column in range(8)
    ) or any(t[index, index] for index in range(8)):
        raise AssertionError("T is not a signed adjacency matrix")
    if t * sp.ones(8, 1) != 2 * sp.ones(8, 1):
        raise AssertionError("the signed component has the wrong row sum")
    if t * t != 4 * sp.eye(8):
        raise AssertionError("the signed component does not square to 4I")
    if t.eigenvals().get(sp.Integer(2), 0) != 4:
        raise AssertionError("the signed component has the wrong 2-multiplicity")
    signed_seen = {0}
    signed_pending = [0]
    while signed_pending:
        left = signed_pending.pop()
        for right in range(8):
            if t[left, right] and right not in signed_seen:
                signed_seen.add(right)
                signed_pending.append(right)
    if len(signed_seen) != 8:
        raise AssertionError("the signed support is not connected")

    p = sp.Matrix(
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
    r = h * p * h / 4
    expected_r = sp.Matrix(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
    )
    if r != expected_r:
        raise AssertionError("the exact intertwiner block changed")
    x = sp.diag(p, r)
    if t * x != x * t:
        raise AssertionError("the non-equitable block does not commute")

    b = sp.Matrix(
        [
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
        ]
    )
    if b != b.transpose() or any(b[index, index] for index in range(8)):
        raise AssertionError("B is not a simple-graph adjacency matrix")
    if b * t != t * b:
        raise AssertionError("B does not commute with the signed component")

    a = b.row_join(x).col_join(x.row_join(b))
    s = t.row_join(sp.zeros(8, 8)).col_join(sp.zeros(8, 8).row_join(t))
    if (
        a != a.transpose()
        or any(a[index, index] for index in range(16))
        or any(
            a[row, column] not in {0, 1}
            for row in range(16)
            for column in range(16)
        )
    ):
        raise AssertionError("A is not a simple-graph adjacency matrix")
    if a * sp.ones(16, 1) != 3 * sp.ones(16, 1):
        raise AssertionError("A is not 3-regular")
    if a * s != s * a:
        raise AssertionError("A and S do not commute")

    cross_degrees = x * sp.ones(8, 1)
    expected_cross_degrees = sp.Matrix([2, 2, 0, 0, 0, 0, 2, 2])
    if cross_degrees != expected_cross_degrees:
        raise AssertionError("the cross-degree vector changed")
    if len(set(cross_degrees)) == 1:
        raise AssertionError("the signed-component partition became equitable")

    seen = {0}
    pending = [0]
    while pending:
        left = pending.pop()
        for right in range(16):
            if a[left, right] and right not in seen:
                seen.add(right)
                pending.append(right)
    if len(seen) != 16:
        raise AssertionError("A is not connected")

    print("component-indicator noninvariance audit: PASS")
    print("signed component: connected support, T^2=4I, dim E_2(T)=4")
    print("graph adjacency: connected, simple, 3-regular, and AS=SA")
    print("cross degrees:", list(cross_degrees))


if __name__ == "__main__":
    main()
