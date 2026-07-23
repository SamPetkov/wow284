#!/usr/bin/env python3
"""Exact audit of Jørgensen's 96-vertex 9-regular girth-five graph.

This graph is a useful boundary control: it has delta*=9 and least distance
eigenvalue -9, so it gives equality rather than a strict WOW-284 violation.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "jorgensen96_adjacency.txt"


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


def distances(graph) -> sp.Matrix:
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

    x = sp.symbols("x")
    expected_a = (
        (x - 9)
        * (x - 3) ** 7
        * (x - 1) ** 7
        * (x + 5)
        * (x**2 - 8) ** 16
        * (x**2 + 2 * x - 6) ** 8
        * (x**4 + 2 * x**3 - 17 * x**2 - 18 * x + 74) ** 8
    )
    expected_d = (
        x**16
        * (x - 195)
        * (x - 3) ** 7
        * (x + 9) ** 8
        * (x**2 + 4 * x - 28) ** 16
        * (x**4 + 10 * x**3 + 5 * x**2 - 72 * x - 96) ** 8
    )
    char_a = sp.factor(a.charpoly(x).as_expr())
    char_d = sp.factor(d.charpoly(x).as_expr())
    if sp.Poly(char_a - expected_a, x) != sp.Poly(0, x):
        raise AssertionError(char_a)
    if sp.Poly(char_d - expected_d, x) != sp.Poly(0, x):
        raise AssertionError(char_d)

    polynomial = sp.Poly(char_d, x)
    if polynomial.eval(-9) != 0 or polynomial.count_roots(-sp.oo, -9) != 1:
        raise AssertionError("Sturm least-root certificate failed")

    print("Jorgensen order-96 exact audit: PASS")
    print("order=96 degree=9 girth=5 diameter=3 transmission=195")
    print(f"chi_A={char_a}")
    print(f"chi_D={char_d}")
    print("delta*=9; lambda_min(D)=-9; WOW-284 score=0 (equality)")


if __name__ == "__main__":
    main()
