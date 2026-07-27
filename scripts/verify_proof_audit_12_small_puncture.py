#!/usr/bin/env python3
"""Independent exact audit of the small-puncture Moore normal form."""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
import json
import sympy as sp

Graph = tuple[frozenset[int], ...]
Subset = tuple[int, ...]


def graph_from_edges(order: int, edges: list[tuple[int, int]]) -> Graph:
    rows = [set() for _ in range(order)]
    for u, v in edges:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)
    return tuple(frozenset(row) for row in rows)


def cycle_graph(order: int) -> Graph:
    return graph_from_edges(order, [(i, (i + 1) % order) for i in range(order)])


def petersen() -> Graph:
    edges: list[tuple[int, int]] = []
    for i in range(5):
        edges.append((i, (i + 1) % 5))
        edges.append((5 + i, 5 + ((i + 2) % 5)))
        edges.append((i, 5 + i))
    return graph_from_edges(10, edges)


def hoffman_singleton() -> Graph:
    modulus = 5
    p = lambda i, j: 5 * (i % modulus) + (j % modulus)
    q = lambda k, ell: 25 + 5 * (k % modulus) + (ell % modulus)
    rows = [set() for _ in range(50)]

    def add(u: int, v: int) -> None:
        rows[u].add(v)
        rows[v].add(u)

    for i in range(modulus):
        for j in range(modulus):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(modulus):
                add(p(i, j), q(k, i * k + j))
    return tuple(frozenset(row) for row in rows)


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    output: list[tuple[int, ...]] = []
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        if -1 in distance:
            raise AssertionError("disconnected graph")
        output.append(tuple(distance))
    return tuple(output)


def verify_moore(graph: Graph) -> int:
    degrees = {len(row) for row in graph}
    if len(degrees) != 1:
        raise AssertionError("not regular")
    k = next(iter(degrees))
    distances = distance_rows(graph)
    if max(map(max, distances)) != 2 or len(graph) != k * k + 1:
        raise AssertionError("not a diameter-two Moore graph")
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            expected = 0 if v in graph[u] else 1
            if len(graph[u] & graph[v]) != expected:
                raise AssertionError("Moore common-neighbor identity failed")
    return k


def induced(graph: Graph, deleted: Subset) -> tuple[Graph, tuple[int, ...]]:
    deleted_set = set(deleted)
    surviving = tuple(v for v in range(len(graph)) if v not in deleted_set)
    index = {v: i for i, v in enumerate(surviving)}
    induced_graph = tuple(
        frozenset(index[w] for w in graph[v] if w not in deleted_set)
        for v in surviving
    )
    return induced_graph, surviving


def minimum_dual_degree(graph: Graph) -> Fraction:
    degrees = tuple(len(row) for row in graph)
    return min(
        Fraction(sum(degrees[w] for w in graph[v]), degrees[v])
        for v in range(len(graph))
    )


def replacement_paths(
    graph: Graph, x: int, y: int, deleted_common: int
) -> list[tuple[int, int, int, int]]:
    paths: list[tuple[int, int, int, int]] = []
    for a in sorted(graph[x] - {deleted_common}):
        if y in graph[a]:
            raise AssertionError("second common neighbor of x,y")
        common = graph[a] & graph[y]
        if len(common) != 1:
            raise AssertionError("missing unique common neighbor for a,y")
        b = next(iter(common))
        paths.append((x, a, b, y))
    return paths


def audit_deletion(graph: Graph, deleted: Subset) -> dict[str, object]:
    k = verify_moore(graph)
    size = len(deleted)
    if size > k - 1:
        raise AssertionError("outside theorem range")
    punctured, surviving = induced(graph, deleted)
    distances = distance_rows(punctured)
    if max(map(max, distances)) > 3:
        raise AssertionError("diameter exceeds three")
    expected_dual = Fraction(k * k - size, k)
    if minimum_dual_degree(punctured) != expected_dual:
        raise AssertionError("dual-degree formula failed")

    deleted_set = set(deleted)
    old_to_new = {v: i for i, v in enumerate(surviving)}
    incidence = sp.Matrix(
        [[int(z in graph[x]) for z in deleted] for x in surviving]
    )
    gram = incidence * incidence.T
    adjacency = sp.Matrix(
        [[int(y in punctured[x]) for y in range(len(punctured))]
         for x in range(len(punctured))]
    )
    expected = 2 * (sp.ones(len(punctured)) - sp.eye(len(punctured))) - adjacency
    expected += gram - sp.diag(*[gram[i, i] for i in range(len(punctured))])
    if sp.Matrix(distances) != expected:
        raise AssertionError("distance normal form failed")

    destroyed = 0
    for index, x in enumerate(surviving):
        for y in surviving[index + 1:]:
            if y in graph[x]:
                continue
            common = next(iter(graph[x] & graph[y]))
            if common not in deleted_set:
                continue
            destroyed += 1
            paths = replacement_paths(graph, x, y, common)
            if len(paths) != k - 1:
                raise AssertionError("wrong replacement-path count")
            internal = [frozenset(path[1:3]) for path in paths]
            if any(
                internal[a] & internal[b]
                for a in range(len(internal))
                for b in range(a + 1, len(internal))
            ):
                raise AssertionError("replacement paths are not internally disjoint")
            if not any(
                path[1] not in deleted_set and path[2] not in deleted_set
                for path in paths
            ):
                raise AssertionError("no replacement path survives")
            if distances[old_to_new[x]][old_to_new[y]] != 3:
                raise AssertionError("destroyed length-two path did not become distance three")

    ambient_distances = distance_rows(graph)
    witnesses = [
        x for x in surviving
        if all(ambient_distances[x][z] == 2 for z in deleted)
    ]
    if not witnesses:
        raise AssertionError("no dual-degree attainment witness")
    witness = witnesses[0]
    if graph[witness] & deleted_set:
        raise AssertionError("attainment witness has a deleted neighbor")
    contribution = sum(
        len(graph[y] & deleted_set)
        for y in graph[witness]
        if y not in deleted_set
    )
    if contribution != size:
        raise AssertionError("deleted vertices do not contribute exactly once")

    return {
        "deleted": list(deleted),
        "order": len(punctured),
        "diameter": max(map(max, distances)),
        "minimum_dual_degree": str(expected_dual),
        "destroyed_common_neighbors": destroyed,
        "attainment_witness": witness,
    }


def symbolic_audit() -> dict[str, str]:
    k, s, t = sp.symbols("k s t", positive=True)
    difference = sp.factor((k - (s - t) / (k - t)) - (k - s / k))
    expected = sp.factor(t * (k - s) / (k * (k - t)))
    if sp.simplify(difference - expected) != 0:
        raise AssertionError("dual-degree comparison identity failed")
    boundary = sp.expand(k**2 + 1 - (k - 1) * (k + 1))
    if boundary != 2:
        raise AssertionError("boundary intersection count failed")
    return {
        "dual_degree_margin": str(difference),
        "boundary_intersection_lower_bound": str(boundary),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    controls: dict[str, object] = {}
    for name, graph in (("C5", cycle_graph(5)), ("Petersen", petersen())):
        k = verify_moore(graph)
        checked = 0
        for size in range(k):
            for deleted in combinations(range(len(graph)), size):
                audit_deletion(graph, deleted)
                checked += 1
        controls[name] = {"deletions_checked": checked, "max_s": k - 1}

    graph = hoffman_singleton()
    verify_moore(graph)
    checked = 0
    for size in range(3):
        for deleted in combinations(range(50), size):
            audit_deletion(graph, deleted)
            checked += 1
    fixed = (
        (0, 1, 2),
        (0, 1, 2, 3),
        (0, 1, 2, 3, 4),
        (0, 1, 2, 3, 4, 5),
        (0, 7, 14, 21, 28, 35),
        (0, 8, 16, 24, 32, 40),
    )
    for deleted in fixed:
        audit_deletion(graph, deleted)
        checked += 1
    controls["Hoffman--Singleton"] = {
        "deletions_checked": checked,
        "exhaustive_through_s": 2,
        "boundary_six_controls": sum(len(item) == 6 for item in fixed),
    }

    result = {"symbolic": symbolic_audit(), "controls": controls}
    print("Proof Audit 12 (small-puncture Moore normal form): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
