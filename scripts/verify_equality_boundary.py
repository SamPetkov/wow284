#!/usr/bin/env python3
"""Symbolic checks for equality in the regular diameter-three WOW criterion."""
from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    k, r = sp.symbols("k r", integer=True, positive=True)
    theta = sp.symbols("theta")
    distance_image = k - 2 - (theta + 1) ** 2
    boundary_plus = -1 + sp.sqrt(2 * k - 2)
    boundary_minus = -1 - sp.sqrt(2 * k - 2)
    assert sp.simplify(distance_image.subs(theta, boundary_plus) + k) == 0
    assert sp.simplify(distance_image.subs(theta, boundary_minus) + k) == 0

    boundary_polynomial = sp.expand(
        (theta - boundary_plus) * (theta - boundary_minus)
    )
    assert boundary_polynomial == theta**2 + 2 * theta - (2 * k - 3)

    # If 2k-2 is a square, its square root is even and k=2r^2+1.
    square_degree = sp.expand((2 * r) ** 2 / 2 + 1)
    assert square_degree == 2 * r**2 + 1
    for value, root in ((3, 2), (9, 4), (19, 6), (33, 8)):
        assert 2 * value - 2 == root**2
        assert value == 2 * (root // 2) ** 2 + 1

    # The order-96 control has k=9 and boundary adjacency eigenvalues 3 and -5.
    assert -1 + sp.sqrt(2 * 9 - 2) == 3
    assert -1 - sp.sqrt(2 * 9 - 2) == -5
    assert 9 - 2 - (3 + 1) ** 2 == -9
    assert 9 - 2 - (-5 + 1) ** 2 == -9

    result = {
        "boundary_polynomial": str(boundary_polynomial),
        "square_boundary_degrees": "k=2r^2+1",
        "order_96_boundary": "k=9, theta=3 or -5, distance eigenvalue=-9",
    }
    print("regular equality boundary: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
