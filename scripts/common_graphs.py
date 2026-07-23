#!/usr/bin/env python3
"""Exact graph constructors used by the WOW-284 Lean extension generators."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from typing import Iterable

import sympy as sp

Q = 5
VertexLabel = tuple[str, int, int]
Graph = tuple[frozenset[int], ...]


def hs_labels() -> tuple[VertexLabel, ...]:
    return tuple(
        [("P", i, j) for i in range(Q) for j in range(Q)]
        + [("Q", k, ell) for k in range(Q) for ell in range(Q)]
    )


def hoffman_singleton() -> tuple[Graph, tuple[VertexLabel, ...]]:
    labels = hs_labels()
    index = {label: i for i, label in enumerate(labels)}
    rows = [set() for _ in labels]

    def add(a: VertexLabel, b: VertexLabel) -> None:
        u, v = index[a], index[b]
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(Q):
        for j in range(Q):
            add(("P", i, j), ("P", i, (j + 1) % Q))
            add(("Q", i, j), ("Q", i, (j + 2) % Q))
            for k in range(Q):
                add(("P", i, j), ("Q", k, (i * k + j) % Q))
    return tuple(frozenset(r) for r in rows), labels


def induced(
    graph: Graph,
    labels: tuple[VertexLabel, ...],
    deleted: Iterable[VertexLabel],
) -> tuple[Graph, tuple[VertexLabel, ...]]:
    deleted_set = set(deleted)
    keep = tuple(i for i, label in enumerate(labels) if label not in deleted_set)
    relabel = {old: new for new, old in enumerate(keep)}
    new_graph = tuple(
        frozenset(relabel[v] for v in graph[u] if v in relabel) for u in keep
    )
    return new_graph, tuple(labels[u] for u in keep)



def induced_indices(graph: Graph, deleted: Iterable[int]) -> tuple[Graph, tuple[int, ...]]:
    """Return the induced graph after deleting numerical vertex indices."""
    deleted_set = set(deleted)
    keep = tuple(v for v in range(len(graph)) if v not in deleted_set)
    relabel = {old: new for new, old in enumerate(keep)}
    return (
        tuple(frozenset(relabel[w] for w in graph[v] if w in relabel) for v in keep),
        keep,
    )


def graph42() -> tuple[Graph, tuple[VertexLabel, ...]]:
    """Second subconstituent at numerical vertex 0 of the HS graph."""
    full, labels = hoffman_singleton()
    deleted_indices = {0} | set(full[0])
    graph, keep = induced_indices(full, deleted_indices)
    return graph, tuple(labels[v] for v in keep)

def graph40() -> tuple[Graph, tuple[VertexLabel, ...]]:
    full, labels = hoffman_singleton()
    deleted = {("P", 0, j) for j in range(Q)} | {("Q", 0, j) for j in range(Q)}
    return induced(full, labels, deleted)


def graph38() -> tuple[Graph, tuple[VertexLabel, ...]]:
    g40, labels40 = graph40()
    return induced(g40, labels40, {("P", 1, 0), ("P", 1, 1)})


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    n = len(graph)
    return sp.Matrix([[int(j in graph[i]) for j in range(n)] for i in range(n)])


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    out: list[tuple[int, ...]] = []
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
            raise AssertionError("disconnected graph")
        out.append(tuple(row))
    return tuple(out)


def distance_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(distance_rows(graph))


def girth(graph: Graph) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        dist = [-1] * len(graph)
        parent = [-1] * len(graph)
        dist[source] = 0
        queue = deque([source])
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


def dual_degrees(graph: Graph) -> tuple[Fraction, ...]:
    degrees = tuple(map(len, graph))
    return tuple(
        Fraction(sum(degrees[u] for u in graph[v]), degrees[v])
        for v in range(len(graph))
    )


def primitive_integer_column(column: sp.Matrix) -> sp.Matrix:
    denominators = [sp.denom(x) for x in column]
    scale = sp.ilcm(*denominators) if denominators else 1
    result = column * scale
    from math import gcd

    common = 0
    for value in result:
        common = gcd(common, abs(int(value)))
    if common > 1:
        result /= common
    assert all(sp.denom(x) == 1 for x in result)
    return result


def matrix_sha_text(matrix: sp.Matrix) -> str:
    return "\n".join(",".join(str(matrix[i, j]) for j in range(matrix.cols)) for i in range(matrix.rows)) + "\n"
