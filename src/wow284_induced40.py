"""Exact combinatorics for the 40-vertex induced WOW-284 counterexample.

Delete the vertices P_(0,j) and Q_(0,j), j in F_5, from the repository's
50-vertex Hoffman--Singleton coordinate graph.  The deleted vertices induce a
Petersen graph; the remainder is the classical 6-regular (6,5)-cage.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction

from wow284_graph import (
    Adjacency,
    IntegerMatrix,
    adjacency_list,
    p_vertex,
    q_vertex,
)

VERTEX_COUNT_40 = 40
DELETED_VERTICES = tuple(
    sorted(
        {p_vertex(0, j) for j in range(5)}
        | {q_vertex(0, j) for j in range(5)}
    )
)


def induced_adjacency() -> tuple[Adjacency, tuple[int, ...]]:
    """Return the 40-vertex adjacency list and its original-label map."""

    full = adjacency_list()
    deleted = set(DELETED_VERTICES)
    labels = tuple(vertex for vertex in range(len(full)) if vertex not in deleted)
    new_index = {old: new for new, old in enumerate(labels)}
    graph = tuple(
        frozenset(new_index[v] for v in full[u] if v in new_index) for u in labels
    )
    if len(graph) != VERTEX_COUNT_40:
        raise AssertionError(f"unexpected induced order: {len(graph)}")
    return graph, labels


def adjacency_matrix_40(adjacency: Adjacency | None = None) -> IntegerMatrix:
    """Return the 40-by-40 integer adjacency matrix."""

    graph = induced_adjacency()[0] if adjacency is None else adjacency
    order = len(graph)
    return tuple(
        tuple(1 if column in graph[row] else 0 for column in range(order))
        for row in range(order)
    )


def all_pairs_distances_40(adjacency: Adjacency | None = None) -> IntegerMatrix:
    """Construct the 40-by-40 distance matrix by independent integer BFS."""

    graph = induced_adjacency()[0] if adjacency is None else adjacency
    order = len(graph)
    rows: list[tuple[int, ...]] = []
    for source in range(order):
        distance = [-1] * order
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        if -1 in distance:
            raise AssertionError(f"induced graph is disconnected from {source}")
        rows.append(tuple(distance))
    return tuple(rows)


def girth_40(adjacency: Adjacency | None = None) -> int:
    """Return the girth by breadth-first cycle searches."""

    graph = induced_adjacency()[0] if adjacency is None else adjacency
    order = len(graph)
    best = order + 1
    for source in range(order):
        distance = [-1] * order
        parent = [-1] * order
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
    if best == order + 1:
        raise AssertionError("induced graph is acyclic")
    return best


def dual_degrees_40(adjacency: Adjacency | None = None) -> tuple[Fraction, ...]:
    """Compute every dual degree exactly from the definition."""

    graph = induced_adjacency()[0] if adjacency is None else adjacency
    degrees = tuple(len(neighbors) for neighbors in graph)
    return tuple(
        Fraction(sum(degrees[u] for u in neighbors), degrees[vertex])
        for vertex, neighbors in enumerate(graph)
    )


def structural_certificate_40() -> dict[str, object]:
    """Exhaustively verify the structural claims for the induced graph."""

    graph, labels = induced_adjacency()
    degrees = tuple(map(len, graph))
    size = sum(degrees) // 2
    if set(degrees) != {6}:
        raise AssertionError(f"unexpected degree set: {sorted(set(degrees))}")
    if size != 120:
        raise AssertionError(f"unexpected edge count: {size}")

    distances = all_pairs_distances_40(graph)
    diameter = max(map(max, distances))
    profiles = Counter(
        tuple(row.count(distance) for distance in range(diameter + 1))
        for row in distances
    )
    if profiles != {(1, 6, 30, 3): 40}:
        raise AssertionError(f"unexpected BFS profiles: {profiles}")

    duals = dual_degrees_40(graph)
    if set(duals) != {Fraction(6)}:
        raise AssertionError(f"unexpected dual degrees: {sorted(set(duals))}")

    return {
        "order": VERTEX_COUNT_40,
        "size": size,
        "degree_set": [6],
        "connected": True,
        "diameter": diameter,
        "girth": girth_40(graph),
        "distance_row_profile": [1, 6, 30, 3],
        "transmission": sum(distances[0]),
        "minimum_dual_degree": "6",
        "deleted_original_labels": list(DELETED_VERTICES),
        "remaining_original_labels": list(labels),
    }
