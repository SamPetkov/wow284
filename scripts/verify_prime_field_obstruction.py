#!/usr/bin/env python3
"""Exact checks for the prime-field diameter-three WOW obstruction."""
from __future__ import annotations

from collections import deque
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def prime_field_graph(q: int, m: int) -> Graph:
    assert q >= 5 and 1 <= m <= q
    vertices = [
        *(("P", i, j) for i in range(m) for j in range(q)),
        *(("Q", k, ell) for k in range(m) for ell in range(q)),
    ]
    index = {vertex: number for number, vertex in enumerate(vertices)}
    rows = [set() for _ in vertices]

    def add(left, right) -> None:
        u, v = index[left], index[right]
        assert u != v
        rows[u].add(v)
        rows[v].add(u)

    for i in range(m):
        for j in range(q):
            add(("P", i, j), ("P", i, (j + 1) % q))
            add(("Q", i, j), ("Q", i, (j + 2) % q))
            for k in range(m):
                add(("P", i, j), ("Q", k, (i * k + j) % q))
    graph = tuple(frozenset(row) for row in rows)
    assert all(len(row) == m + 2 for row in graph)
    return graph


def girth(graph: Graph) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        dist = [-1] * len(graph)
        parent = [-1] * len(graph)
        dist[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def diameter(graph: Graph) -> int:
    maximum = 0
    for source in range(len(graph)):
        dist = [-1] * len(graph)
        dist[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert -1 not in dist
        maximum = max(maximum, max(dist))
    return maximum


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def verify_symbolic_obstruction() -> dict[str, str]:
    m = sp.symbols("m", integer=True, positive=True)

    # The t=0 Fourier block is [[2I,J],[J,2I]]. Its eigenvalues are
    # m+2, 2-m, and 2 with multiplicity 2m-2.
    assert sp.expand((m - 3) ** 2 - (2 * m + 2)) == (m - 1) * (m - 7)
    for value in (1, 2, 3):
        if value == 1:
            assert abs(2 - value + 1) >= sp.sqrt(2 * value + 2)
        else:
            assert abs(2 + 1) >= sp.sqrt(2 * value + 2)
    for value in (4, 5, 6):
        assert abs(2 - value + 1) < sp.sqrt(2 * value + 2)
        assert 3 < sp.sqrt(2 * value + 2)

    # Exact comparison for the nontrivial Fourier-block lower bound.
    # cos(pi/7) > sqrt(3)/2 because pi/7 < pi/6. The remaining radical
    # comparison is verified exactly for m=4,5,6.
    lower_offset = (sp.sqrt(3) - 1) / 2
    margins = {}
    for value in (4, 5, 6):
        margin = sp.simplify(
            sp.sqrt(value) + lower_offset - (-1 + sp.sqrt(2 * value + 2))
        )
        assert bool(margin > 0)
        margins[str(value)] = str(margin)

    # A rational-only certificate for the worst case m=6:
    # sqrt(14)-sqrt(6) < 15/4-12/5 = 27/20, while
    # (sqrt(3)+1)/2 > (17/10+1)/2 = 27/20.
    assert sp.Rational(14) < sp.Rational(15, 4) ** 2
    assert sp.Rational(6) > sp.Rational(12, 5) ** 2
    assert sp.Rational(3) > sp.Rational(17, 10) ** 2
    assert sp.Rational(15, 4) - sp.Rational(12, 5) == sp.Rational(27, 20)
    assert (sp.Rational(17, 10) + 1) / 2 == sp.Rational(27, 20)

    return {
        "zero_mode_second_condition": str(
            sp.factor((m - 3) ** 2 - (2 * m + 2))
        ),
        "surviving_m_values": "4,5,6",
        "exact_positive_margins_from_cos_pi_over_7_bound": str(margins),
    }


def verify_q7_controls() -> dict[str, object]:
    expected_charpolys = {
        4: (X - 6)
        * (X - 2) ** 6
        * (X + 2)
        * (
            X**6
            + 2 * X**5
            - 24 * X**4
            - 34 * X**3
            + 184 * X**2
            + 137 * X
            - 433
        )
        ** 2
        * (
            X**6
            + 2 * X**5
            - 10 * X**4
            - 13 * X**3
            + 30 * X**2
            + 18 * X
            - 27
        )
        ** 2
        * (
            X**12
            + 4 * X**11
            - 22 * X**10
            - 93 * X**9
            + 174 * X**8
            + 769 * X**7
            - 666 * X**6
            - 2734 * X**5
            + 1577 * X**4
            + 3823 * X**3
            - 2280 * X**2
            - 891 * X
            + 421
        )
        ** 2,
        5: (X - 7)
        * (X - 2) ** 8
        * (X + 3)
        * (X**3 - 7 * X + 7) ** 2
        * (X**3 + 2 * X**2 - X - 1) ** 2
        * (
            X**6
            + 2 * X**5
            - 24 * X**4
            - 34 * X**3
            + 184 * X**2
            + 137 * X
            - 433
        )
        ** 6
        * (
            X**6
            + 2 * X**5
            - 10 * X**4
            - 20 * X**3
            + 23 * X**2
            + 46 * X
            + 1
        )
        ** 2,
        6: (X - 8)
        * (X - 2) ** 10
        * (X + 4)
        * (
            X**6
            + 2 * X**5
            - 24 * X**4
            - 34 * X**3
            + 184 * X**2
            + 137 * X
            - 433
        )
        ** 10
        * (
            X**6
            + 2 * X**5
            - 6 * X**4
            - 10 * X**3
            + 10 * X**2
            + 11 * X
            - 1
        )
        ** 2,
    }

    result: dict[str, object] = {}
    for m in (4, 5, 6):
        graph = prime_field_graph(7, m)
        assert len(graph) == 14 * m
        assert girth(graph) == 5
        assert diameter(graph) == 3
        adjacency = adjacency_matrix(graph)
        characteristic = sp.factor(adjacency.charpoly(X).as_expr())
        assert sp.Poly(characteristic - expected_charpolys[m], X).is_zero
        result[str(m)] = {
            "order": len(graph),
            "degree": m + 2,
            "girth": 5,
            "diameter": 3,
            "adjacency_characteristic_polynomial": str(characteristic),
        }
    return result


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "symbolic_obstruction": verify_symbolic_obstruction(),
        "q_equals_7_exact_controls": verify_q7_controls(),
    }
    print("prime-field diameter-three obstruction: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
