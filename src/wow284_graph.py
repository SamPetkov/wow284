"""Coordinate model of the 50-vertex WOW-284 counterexample.

The graph is constructed over F_5.  Vertices 0,...,24 represent P_(i,j),
and vertices 25,...,49 represent Q_(k,l).  All routines use integer arithmetic
and the Python standard library.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from typing import Iterable

FIELD_ORDER = 5
VERTEX_COUNT = 50

Edge = tuple[int, int]
Adjacency = tuple[frozenset[int], ...]
IntegerMatrix = tuple[tuple[int, ...], ...]


def p_vertex(i: int, j: int) -> int:
    """Return the numerical label of P_(i,j), reducing coordinates mod 5."""

    return FIELD_ORDER * (i % FIELD_ORDER) + (j % FIELD_ORDER)


def q_vertex(k: int, ell: int) -> int:
    """Return the numerical label of Q_(k,ell), reducing coordinates mod 5."""

    return 25 + FIELD_ORDER * (k % FIELD_ORDER) + (ell % FIELD_ORDER)


def vertex_name(vertex: int) -> str:
    """Return a stable coordinate name for a numerical vertex label."""

    if not 0 <= vertex < VERTEX_COUNT:
        raise ValueError(f"vertex label out of range: {vertex}")
    if vertex < 25:
        i, j = divmod(vertex, FIELD_ORDER)
        return f"P_({i},{j})"
    k, ell = divmod(vertex - 25, FIELD_ORDER)
    return f"Q_({k},{ell})"


def _edge(u: int, v: int) -> Edge:
    if u == v:
        raise ValueError(f"loop at vertex {u}")
    return (u, v) if u < v else (v, u)


def build_edges() -> tuple[Edge, ...]:
    """Construct and sort the 175 unordered edges."""

    edges: set[Edge] = set()
    for i in range(FIELD_ORDER):
        for j in range(FIELD_ORDER):
            edges.add(_edge(p_vertex(i, j), p_vertex(i, j + 1)))
            edges.add(_edge(q_vertex(i, j), q_vertex(i, j + 2)))
            for k in range(FIELD_ORDER):
                edges.add(_edge(p_vertex(i, j), q_vertex(k, i * k + j)))
    return tuple(sorted(edges))


def adjacency_list(edges: Iterable[Edge] | None = None) -> Adjacency:
    """Return the adjacency list as immutable neighbor sets."""

    mutable = [set() for _ in range(VERTEX_COUNT)]
    for u, v in build_edges() if edges is None else edges:
        if not (0 <= u < VERTEX_COUNT and 0 <= v < VERTEX_COUNT):
            raise ValueError(f"edge endpoint out of range: {(u, v)}")
        if u == v:
            raise ValueError(f"loop at vertex {u}")
        mutable[u].add(v)
        mutable[v].add(u)
    return tuple(frozenset(neighbors) for neighbors in mutable)


def adjacency_matrix(adjacency: Adjacency | None = None) -> IntegerMatrix:
    """Return the 0-1 adjacency matrix."""

    graph = adjacency_list() if adjacency is None else adjacency
    return tuple(
        tuple(1 if column in graph[row] else 0 for column in range(VERTEX_COUNT))
        for row in range(VERTEX_COUNT)
    )


def all_pairs_distances(adjacency: Adjacency | None = None) -> IntegerMatrix:
    """Construct the distance matrix by independent integer BFS runs."""

    graph = adjacency_list() if adjacency is None else adjacency
    rows: list[tuple[int, ...]] = []
    for source in range(VERTEX_COUNT):
        distance = [-1] * VERTEX_COUNT
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        if -1 in distance:
            raise AssertionError(f"graph is disconnected from source {source}")
        rows.append(tuple(distance))
    return tuple(rows)


def girth(adjacency: Adjacency | None = None) -> int:
    """Return the girth using breadth-first searches in the undirected graph."""

    graph = adjacency_list() if adjacency is None else adjacency
    best = VERTEX_COUNT + 1
    for source in range(VERTEX_COUNT):
        distance = [-1] * VERTEX_COUNT
        parent = [-1] * VERTEX_COUNT
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, distance[u] + distance[v] + 1)
    if best == VERTEX_COUNT + 1:
        raise AssertionError("graph is acyclic")
    return best


def dual_degrees(adjacency: Adjacency | None = None) -> tuple[Fraction, ...]:
    """Compute every dual degree exactly from its definition."""

    graph = adjacency_list() if adjacency is None else adjacency
    degrees = tuple(len(neighbors) for neighbors in graph)
    values: list[Fraction] = []
    for vertex, neighbors in enumerate(graph):
        if not neighbors:
            raise ZeroDivisionError(f"isolated vertex {vertex}")
        values.append(Fraction(sum(degrees[u] for u in neighbors), degrees[vertex]))
    return tuple(values)


def structural_certificate() -> dict[str, object]:
    """Exhaustively verify the combinatorial claims and return a summary."""

    edges = build_edges()
    graph = adjacency_list(edges)
    if len(edges) != 175:
        raise AssertionError(f"expected 175 edges, found {len(edges)}")
    degree_set = sorted({len(neighbors) for neighbors in graph})
    if degree_set != [7]:
        raise AssertionError(f"expected degree set [7], found {degree_set}")

    adjacent_pairs = 0
    nonadjacent_pairs = 0
    for u in range(VERTEX_COUNT):
        for v in range(u + 1, VERTEX_COUNT):
            common = len(graph[u] & graph[v])
            if v in graph[u]:
                adjacent_pairs += 1
                expected = 0
            else:
                nonadjacent_pairs += 1
                expected = 1
            if common != expected:
                raise AssertionError(
                    f"common-neighbor failure for {(u, v)}: {common} != {expected}"
                )

    distances = all_pairs_distances(graph)
    diameter = max(max(row) for row in distances)
    computed_girth = girth(graph)
    duals = dual_degrees(graph)
    if min(duals) != Fraction(7, 1):
        raise AssertionError(f"unexpected minimum dual degree: {min(duals)}")

    return {
        "order": VERTEX_COUNT,
        "size": len(edges),
        "degree_set": degree_set,
        "adjacent_pair_count": adjacent_pairs,
        "nonadjacent_pair_count": nonadjacent_pairs,
        "common_neighbor_certificate": True,
        "connected": True,
        "diameter": diameter,
        "girth": computed_girth,
        "minimum_dual_degree": str(min(duals)),
    }
