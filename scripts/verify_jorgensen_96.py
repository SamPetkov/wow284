#!/usr/bin/env python3
"""Exact audit of Jorgensen's 96-vertex 9-regular girth-five graph.

This is an independent legacy-style parser for the normalized adjacency file.
The provenance-grade representation audit lives in
``verify_jorgensen96_provenance.py``. No floating-point ordering is used.
"""
from __future__ import annotations

from collections import deque
from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "jorgensen96" / "adjacency.txt"
X = sp.symbols("x")


def load_graph() -> tuple[frozenset[int], ...]:
    rows = [set() for _ in range(96)]
    seen = set()
    for line in DATA.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*\{([^}]*)\}\s*", line)
        if match is None:
            raise ValueError(line)
        u = int(match.group(1))
        rows[u] = {int(x) for x in re.findall(r"\d+", match.group(2))}
        seen.add(u)
    if seen != set(range(96)):
        raise AssertionError("missing vertex rows")
    graph = tuple(frozenset(row) for row in rows)
    if not all(len(row) == 9 for row in graph):
        raise AssertionError("not 9-regular")
    if not all(u in graph[v] for u in range(96) for v in graph[u]):
        raise AssertionError("asymmetric adjacency")
    if any(u in graph[u] for u in range(96)):
        raise AssertionError("loop")
    return graph


def distances(graph: tuple[frozenset[int], ...]) -> sp.Matrix:
    rows = []
    for source in range(96):
        dist = [-1] * 96
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        if -1 in dist:
            raise AssertionError("disconnected")
        rows.append(dist)
    return sp.Matrix(rows)


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    graph = load_graph()
    for u in range(96):
        for v in range(u + 1, 96):
            common = len(graph[u] & graph[v])
            if common > 1:
                raise AssertionError((u, v, common))
            if v in graph[u] and common != 0:
                raise AssertionError("triangle")

    a = sp.Matrix([[int(v in graph[u]) for v in range(96)] for u in range(96)])
    d = distances(graph)
    if max(d) != 3:
        raise AssertionError("diameter is not three")
    if d != 3 * sp.ones(96) + 6 * sp.eye(96) - 2 * a - a * a:
        raise AssertionError("diameter-three distance polynomial failed")

    expected_a = (
        (X - 9)
        * (X - 3) ** 7
        * (X - 1) ** 7
        * (X + 5)
        * (X**2 - 8) ** 16
        * (X**2 + 2 * X - 6) ** 8
        * (X**4 + 2 * X**3 - 17 * X**2 - 18 * X + 74) ** 8
    )
    expected_d = (
        X**16
        * (X - 195)
        * (X - 3) ** 7
        * (X + 9) ** 8
        * (X**2 + 4 * X - 28) ** 16
        * (X**4 + 10 * X**3 + 5 * X**2 - 72 * X - 96) ** 8
    )
    char_a = sp.factor(a.charpoly(X).as_expr())
    char_d = sp.factor(d.charpoly(X).as_expr())
    if not sp.Poly(char_a - expected_a, X).is_zero:
        raise AssertionError(char_a)
    if not sp.Poly(char_d - expected_d, X).is_zero:
        raise AssertionError(char_d)

    # Exact adjacency-interval certificate for D+9I >= 0 on 1-perp.
    quartic = X**4 + 2 * X**3 - 17 * X**2 - 18 * X + 74
    quartic_poly = sp.Poly(quartic, X)
    if quartic_poly.eval(-5) != 114 or quartic_poly.eval(3) != 2:
        raise AssertionError("wrong quartic endpoint values")
    if quartic_poly.count_roots(-sp.oo, -5) != 0:
        raise AssertionError("quartic root at or below -5")
    if quartic_poly.count_roots(3, sp.oo) != 0:
        raise AssertionError("quartic root at or above 3")
    if quartic_poly.count_roots(-5, 3) != 4:
        raise AssertionError("quartic roots are not all in (-5,3)")

    # Direct distance certificate with the boundary factor removed first, so
    # the interval endpoint convention is irrelevant.
    remaining = sp.Poly(sp.cancel(expected_d / (X + 9) ** 8), X)
    if remaining.eval(-9) == 0:
        raise AssertionError("remaining factor also vanishes at -9")
    if remaining.count_roots(-sp.oo, -9) != 0:
        raise AssertionError("remaining factor has a root below -9")

    polynomial = sp.Poly(char_d, X)
    multiplicity = 0
    divisor = sp.Poly(X + 9, X)
    while polynomial.eval(-9) == 0:
        polynomial, remainder = sp.div(polynomial, divisor)
        if not remainder.is_zero:
            raise AssertionError("failed exact division by x+9")
        multiplicity += 1
    if multiplicity != 8:
        raise AssertionError("wrong multiplicity at -9")

    print("Jorgensen order-96 exact audit: PASS")
    print("order=96 degree=9 girth=5 diameter=3 transmission=195")
    print(f"chi_A={char_a}")
    print(f"chi_D={char_d}")
    print("delta*=9; lambda_min(D)=-9 with multiplicity 8; score=0")


if __name__ == "__main__":
    main()
