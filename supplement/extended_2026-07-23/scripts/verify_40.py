#!/usr/bin/env python3
"""Standalone exact audit of the proposed 40-vertex counterexample."""

from __future__ import annotations

from collections import deque
from fractions import Fraction

import sympy as sp


def p(i: int, j: int) -> int:
    return 5 * (i % 5) + (j % 5)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % 5) + (ell % 5)


def hoffman_singleton() -> tuple[frozenset[int], ...]:
    edges: set[tuple[int, int]] = set()

    def add(u: int, v: int) -> None:
        edges.add((u, v) if u < v else (v, u))

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(5):
                add(p(i, j), q(k, i * k + j))
    graph = [set() for _ in range(50)]
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return tuple(frozenset(row) for row in graph)


def induced(
    graph: tuple[frozenset[int], ...], deleted: set[int]
) -> tuple[tuple[frozenset[int], ...], tuple[int, ...]]:
    labels = tuple(v for v in range(50) if v not in deleted)
    index = {old: new for new, old in enumerate(labels)}
    return (
        tuple(frozenset(index[v] for v in graph[u] if v in index) for u in labels),
        labels,
    )


def distances(graph: tuple[frozenset[int], ...]) -> tuple[tuple[int, ...], ...]:
    rows = []
    for source in range(len(graph)):
        row = [-1] * len(graph)
        row[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if row[v] == -1:
                    row[v] = row[u] + 1
                    queue.append(v)
        if -1 in row:
            raise AssertionError("graph is disconnected")
        rows.append(tuple(row))
    return tuple(rows)


def girth(graph: tuple[frozenset[int], ...]) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        parent = [-1] * len(graph)
        distance[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, distance[u] + distance[v] + 1)
    return best


def matrix(graph: tuple[frozenset[int], ...]) -> sp.Matrix:
    return sp.Matrix(
        [[int(j in graph[i]) for j in range(len(graph))] for i in range(len(graph))]
    )


def main() -> None:
    full_graph = hoffman_singleton()
    deleted = {p(0, j) for j in range(5)} | {q(0, j) for j in range(5)}
    graph, labels = induced(full_graph, deleted)
    distance_rows = distances(graph)

    degrees = tuple(map(len, graph))
    assert len(graph) == 40
    assert sum(degrees) // 2 == 120
    assert set(degrees) == {6}
    assert girth(graph) == 5
    assert max(map(max, distance_rows)) == 3
    duals = tuple(
        Fraction(sum(degrees[u] for u in graph[v]), degrees[v]) for v in range(40)
    )
    assert set(duals) == {Fraction(6)}

    b = matrix(graph)
    d = sp.Matrix(distance_rows)
    x = sp.symbols("x")
    expected_b = (x - 6) * (x - 2) ** 18 * (x - 1) ** 4 * (x + 2) ** 5 * (x + 3) ** 12
    expected_d = (x - 75) * (x - 3) ** 5 * x**16 * (x + 5) ** 18
    assert sp.Poly(b.charpoly(x).as_expr() - expected_b, x).is_zero
    assert sp.Poly(d.charpoly(x).as_expr() - expected_d, x).is_zero
    assert d == 3 * sp.ones(40) + 3 * sp.eye(40) - 2 * b - b * b

    full_a = matrix(full_graph)
    removed = sorted(deleted)
    c = full_a.extract(list(labels), removed)
    petersen = full_a.extract(removed, removed)
    assert c.T * c == 4 * sp.eye(10)
    assert b * c == c * (sp.ones(10) - sp.eye(10) - petersen)
    expected_p = (x - 3) * (x - 1) ** 5 * (x + 2) ** 4
    assert sp.Poly(petersen.charpoly(x).as_expr() - expected_p, x).is_zero

    print("40-vertex exact audit: PASS")
    print("order=40 size=120 degree=6 girth=5 diameter=3")
    print("chi_A=(x-6)(x-2)^18(x-1)^4(x+2)^5(x+3)^12")
    print("chi_D=(x-75)(x-3)^5*x^16*(x+5)^18")
    print("delta*=6; lambda_min(D)=-5; WOW-284 gap=1")


if __name__ == "__main__":
    main()
