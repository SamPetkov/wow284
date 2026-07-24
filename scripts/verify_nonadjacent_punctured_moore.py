#!/usr/bin/env python3
"""Exact verification of the nonadjacent-pair punctured Moore spectrum."""
from __future__ import annotations

from collections import deque
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def p(i: int, j: int) -> int:
        return 5 * (i % 5) + (j % 5)

    def q(k: int, ell: int) -> int:
        return 25 + 5 * (k % 5) + (ell % 5)

    def add(u: int, v: int) -> None:
        assert u != v
        rows[u].add(v)
        rows[v].add(u)

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(5):
                add(p(i, j), q(k, i * k + j))
    graph = tuple(frozenset(row) for row in rows)
    assert all(len(row) == 7 for row in graph)
    return graph


def induced(graph: Graph, deleted: set[int]) -> tuple[Graph, tuple[int, ...]]:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    index = {old: new for new, old in enumerate(keep)}
    return (
        tuple(frozenset(index[w] for w in graph[v] if w in index) for v in keep),
        keep,
    )


def distance_matrix(graph: Graph) -> sp.Matrix:
    rows: list[list[int]] = []
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
        rows.append(dist)
    return sp.Matrix(rows)


def verify_symbolic_factorization() -> dict[str, str]:
    k, x = sp.symbols("k x")
    delta = sp.symbols("Delta", positive=True)
    a = k - 1
    c = k - 2
    e = (k - 1) * (k - 2)
    sizes = [1, a, a, c, e]

    adjacency_quotient = sp.Matrix(
        [
            [0, 0, 0, c, 0],
            [0, 0, 1, 0, c],
            [0, 1, 0, 0, c],
            [1, 0, 0, 0, a],
            [0, 1, 1, 1, k - 3],
        ]
    )
    increase_quotient = sp.Matrix(
        [
            [0, a, a, 0, 0],
            [1, a - 1, 0, 0, 0],
            [1, 0, a - 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    distance_quotient = sp.Matrix(
        5,
        5,
        lambda i, j: sp.expand(
            2 * sizes[j]
            - 2 * int(i == j)
            - adjacency_quotient[i, j]
            + increase_quotient[i, j]
        ),
    )

    quartic = (
        x**4
        + (10 - 2 * k**2) * x**3
        + (2 * k**3 - 17 * k**2 - 2 * k + 36) * x**2
        + (12 * k**3 - 49 * k**2 - 4 * k + 53) * x
        - 2 * k**4
        + 17 * k**3
        - 38 * k**2
        + 5 * k
        + 20
    )
    assert sp.expand(
        distance_quotient.charpoly(x).as_expr() - (x - (k - 3)) * quartic
    ) == 0

    symmetric_module = sp.Matrix([[-4, -(k - 3)], [-1, 0]])
    antisymmetric_module = sp.Matrix([[-2, -(k - 1)], [-1, -2]])
    common_neighbor_module = sp.Matrix([[-2, -(k - 1)], [-1, -1]])
    assert sp.expand(
        symmetric_module.charpoly(x).as_expr() - (x**2 + 4 * x - (k - 3))
    ) == 0
    assert sp.expand(
        antisymmetric_module.charpoly(x).as_expr() - (x**2 + 4 * x - (k - 5))
    ) == 0
    assert sp.expand(
        common_neighbor_module.charpoly(x).as_expr()
        - (x**2 + 3 * x + 3 - k)
    ) == 0

    kernel_positive = (k - 2) * (k + (k - 4) * delta) / (2 * delta)
    kernel_negative = (k - 2) * ((k - 4) * delta - k) / (2 * delta)
    negative_multiplicity = sp.simplify(kernel_positive + k - 3)
    positive_multiplicity = sp.simplify(kernel_negative + k - 3)
    expected_negative = (
        k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    expected_positive = (
        -k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    assert sp.simplify(negative_multiplicity - expected_negative) == 0
    assert sp.simplify(positive_multiplicity - expected_positive) == 0
    assert sp.simplify(
        negative_multiplicity + positive_multiplicity - (k**2 - 4 * k + 2)
    ) == 0
    assert sp.simplify(
        5
        + 4 * (k - 2)
        + negative_multiplicity
        + positive_multiplicity
        - (k**2 - 1)
    ) == 0

    return {
        "distance_quotient_characteristic_polynomial": str(
            sp.factor(distance_quotient.charpoly(x).as_expr())
        ),
        "quartic_factor": str(quartic),
        "symmetric_module_factor": str(
            sp.factor(symmetric_module.charpoly(x).as_expr())
        ),
        "antisymmetric_module_factor": str(
            sp.factor(antisymmetric_module.charpoly(x).as_expr())
        ),
        "negative_moore_distance_multiplicity": str(expected_negative),
        "positive_moore_distance_multiplicity": str(expected_positive),
    }


def verify_hoffman_singleton_specialization() -> dict[str, str]:
    full = hoffman_singleton()
    u, v = 0, 2
    assert v not in full[u]
    common = full[u] & full[v]
    assert len(common) == 1
    w = next(iter(common))
    cell_a = set(full[u]) - {w}
    cell_b = set(full[v]) - {w}
    cell_c = set(full[w]) - {u, v}
    cell_z = set(range(50)) - {u, v, w} - cell_a - cell_b - cell_c
    assert [len(cell) for cell in ({w}, cell_a, cell_b, cell_c, cell_z)] == [
        1,
        6,
        6,
        5,
        30,
    ]

    graph, keep = induced(full, {u, v})
    old_to_new = {old: new for new, old in enumerate(keep)}
    cells = [
        [old_to_new[z] for z in cell]
        for cell in ({w}, cell_a, cell_b, cell_c, cell_z)
    ]
    distance = distance_matrix(graph)

    k = sp.Integer(7)
    sizes = [1, k - 1, k - 1, k - 2, (k - 1) * (k - 2)]
    adjacency_quotient = sp.Matrix(
        [
            [0, 0, 0, k - 2, 0],
            [0, 0, 1, 0, k - 2],
            [0, 1, 0, 0, k - 2],
            [1, 0, 0, 0, k - 1],
            [0, 1, 1, 1, k - 3],
        ]
    )
    increase_quotient = sp.Matrix(
        [
            [0, k - 1, k - 1, 0, 0],
            [1, k - 2, 0, 0, 0],
            [1, 0, k - 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    quotient = sp.Matrix(
        5,
        5,
        lambda i, j: 2 * sizes[j]
        - 2 * int(i == j)
        - adjacency_quotient[i, j]
        + increase_quotient[i, j],
    )
    for i, source_cell in enumerate(cells):
        for j, target_cell in enumerate(cells):
            row_sums = {
                sum(distance[source, target] for target in target_cell)
                for source in source_cell
            }
            assert row_sums == {int(quotient[i, j])}

    quartic = X**4 - 88 * X**3 - 125 * X**2 + 1740 * X - 778
    expected = (
        (X - 4)
        * quartic
        * (X**2 + 4 * X - 4) ** 5
        * (X**2 + 4 * X - 2) ** 5
        * (X + 4) ** 15
        * (X - 1) ** 8
    )
    characteristic = sp.factor(distance.charpoly(X).as_expr())
    assert sp.Poly(characteristic - expected, X).is_zero
    return {
        "deleted_vertices": "P_(0,0), P_(0,2)",
        "cell_sizes": "1,6,6,5,30",
        "distance_characteristic_polynomial": str(characteristic),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "generic_symbolic_factorization": verify_symbolic_factorization(),
        "hoffman_singleton_specialization": verify_hoffman_singleton_specialization(),
    }
    print("nonadjacent punctured Moore verification: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
