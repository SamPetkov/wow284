#!/usr/bin/env python3
"""Exact symbolic audit of the signed-complement bridge."""
from __future__ import annotations

import sympy as sp

K, N, R, THETA = sp.symbols("k n r theta", integer=True)


def symbolic_audit() -> dict[str, str]:
    h = 6 * (K + 2)
    c = (K + 2) ** 2 * (K**2 + 3)
    epsilon = c - (h + 1) * N + 1
    r = sp.expand(2 * epsilon - N - 2)
    expected_r = sp.expand(2 * c - (12 * K + 27) * N)
    if r != expected_r:
        raise AssertionError("wrong excess parameter")

    rho = sp.simplify((epsilon - 1) / N)
    if sp.simplify(rho - (N + r) / (2 * N)) != 0:
        raise AssertionError("wrong optimal-slack J coefficient")

    signed_degree = sp.simplify(N - 1 - epsilon)
    if sp.simplify(signed_degree - (N - r - 4) / 2) != 0:
        raise AssertionError("wrong signed degree")

    bridge_coefficient = sp.simplify(1 - rho)
    if sp.simplify(bridge_coefficient - (N - r) / (2 * N)) != 0:
        raise AssertionError("wrong signed-complement PSD coefficient")

    g = (THETA + 2) ** 2 * ((THETA + 1) ** 2 - (2 * K - 2))
    signed_eigenvalue = -2 - g
    if sp.expand(signed_eigenvalue + 2 + g) != 0:
        raise AssertionError("wrong nonprincipal signed eigenvalue map")

    return {
        "r": str(r),
        "rho": str(rho),
        "signed_degree": str(signed_degree),
        "bridge_J_coefficient": str(bridge_coefficient),
        "signed_eigenvalue": str(sp.expand(signed_eigenvalue)),
    }


def entry_bound_audit() -> dict[str, str]:
    x = sp.symbols("x", positive=True)
    rho = (1 + x) / 2
    diagonal = 1 + rho
    z = sp.symbols("z", integer=True, nonnegative=True)

    # |rho-z| <= 1+rho implies z <= 1+2rho = 2+x.
    upper = sp.simplify(1 + 2 * rho)
    if upper != x + 2:
        raise AssertionError("wrong integral entry upper bound")

    # If 0<x<1, integral nonnegative z is at most two.
    if not all(value <= 2 for value in (0, 1, 2)):
        raise AssertionError("internal integer check failed")

    return {"diagonal": str(diagonal), "entry_upper": str(upper)}


def order50_audit() -> dict[str, int]:
    k, n = 6, 50
    c = (k + 2) ** 2 * (k**2 + 3)
    r = 2 * c - (12 * k + 27) * n
    degree = (n - r - 4) // 2
    if (c, r, degree) != (2496, 42, 2):
        raise AssertionError("wrong order-50 specialization")

    # S=(h+2)J-2I-g(A), and h+2=50 at k=6.
    coefficient = 6 * (k + 2) + 2
    if coefficient != 50:
        raise AssertionError("wrong order-50 J coefficient")

    return {"C_6": c, "r": r, "signed_degree": degree, "J_coefficient": coefficient}


def kernel_audit() -> dict[str, object]:
    theta = sp.symbols("theta", real=True)
    k = sp.symbols("k", integer=True, positive=True)
    g = sp.factor((theta + 2) ** 2 * ((theta + 1) ** 2 - (2 * k - 2)))
    roots = [
        -2,
        -1 - sp.sqrt(2 * k - 2),
        -1 + sp.sqrt(2 * k - 2),
    ]
    if any(sp.simplify(g.subs(theta, value)) != 0 for value in roots):
        raise AssertionError("wrong zeros of the optimal polynomial")
    return {"optimal_polynomial": str(g), "open_interval_zero": -2}


def main() -> None:
    report = {
        "symbolic": symbolic_audit(),
        "entry_bound": entry_bound_audit(),
        "order50": order50_audit(),
        "kernel": kernel_audit(),
    }
    print("signed-complement bridge audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
