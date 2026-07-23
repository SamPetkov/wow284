#!/usr/bin/env python3
"""Numerical exploration of induced-subgraph deletion landscapes.

This file is explicitly exploratory.  It uses floating-point eigenvalues to
rank or classify candidates and must not be cited as an exact proof.  Exact
certificates for selected positive candidates are supplied by the other
scripts in this package.

Default screens:
* all C(40,2)=780 two-vertex deletions from the 40-vertex graph;
* all 42 one-vertex and all C(42,2)=861 two-vertex deletions from the
  42-vertex Moore second subconstituent.

Optional:
* --triples42 screens all C(42,3)=11480 triples;
* --large96 screens all 96 one-vertex and 432 edge deletions of the exact
  order-96 equality graph.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import re

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


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


def induced(graph: tuple[frozenset[int], ...], deleted: set[int]):
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    index = {old: new for new, old in enumerate(keep)}
    return tuple(frozenset(index[w] for w in graph[v] if w in index) for v in keep)


def distance_rows(graph: tuple[frozenset[int], ...]) -> list[list[int]] | None:
    rows = []
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
        if -1 in dist:
            return None
        rows.append(dist)
    return rows


def score(graph: tuple[frozenset[int], ...]) -> tuple[float, Fraction, float] | None:
    rows = distance_rows(graph)
    if rows is None:
        return None
    degrees = tuple(map(len, graph))
    if min(degrees) == 0:
        return None
    dual = min(
        Fraction(sum(degrees[u] for u in graph[v]), degrees[v])
        for v in range(len(graph))
    )
    least = float(np.linalg.eigvalsh(np.asarray(rows, dtype=float))[0])
    return float(dual) + least, dual, least


def graph40() -> tuple[frozenset[int], ...]:
    full = hoffman_singleton()
    deleted = set(range(5)) | set(range(25, 30))
    return induced(full, deleted)


def graph42() -> tuple[frozenset[int], ...]:
    full = hoffman_singleton()
    return induced(full, {0} | set(full[0]))


def graph96() -> tuple[frozenset[int], ...]:
    data = ROOT / "data" / "jorgensen96_adjacency.txt"
    graph = [set() for _ in range(96)]
    for line in data.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*\{([^}]*)\}\s*", line)
        if match is None:
            raise ValueError(line)
        graph[int(match.group(1))] = {int(x) for x in re.findall(r"\d+", match.group(2))}
    return tuple(frozenset(row) for row in graph)


def screen_40_pairs() -> None:
    graph = graph40()
    original_distances = distance_rows(graph)
    assert original_distances is not None
    groups: dict[int, list[float]] = defaultdict(list)
    positives = 0
    best = (-1e100, None, None)
    for u, v in combinations(range(40), 2):
        result = score(induced(graph, {u, v}))
        assert result is not None
        phi, dual, least = result
        groups[original_distances[u][v]].append(phi)
        positives += int(phi > 1e-9)
        if phi > best[0]:
            best = (phi, (u, v), (dual, least))
    print("40-vertex two-deletion screen")
    print(f"  tested=780 positive={positives}")
    for distance in sorted(groups):
        values = groups[distance]
        print(
            f"  original distance {distance}: count={len(values)} "
            f"min={min(values):.12f} max={max(values):.12f}"
        )
    print(f"  best={best}")


def screen_42(triples: bool) -> None:
    graph = graph42()
    singles = [score(induced(graph, {u})) for u in range(42)]
    assert all(x is not None for x in singles)
    single_values = [x[0] for x in singles if x is not None]

    positive_edges = 0
    positive_non_edges = 0
    best_pair = (-1e100, None, None)
    for u, v in combinations(range(42), 2):
        result = score(induced(graph, {u, v}))
        assert result is not None
        phi, dual, least = result
        if phi > 1e-9:
            if v in graph[u]:
                positive_edges += 1
            else:
                positive_non_edges += 1
        if phi > best_pair[0]:
            best_pair = (phi, (u, v), (dual, least))

    print("42-vertex deletion screen")
    print(
        f"  single deletions: count=42 positive={sum(v > 1e-9 for v in single_values)} "
        f"min={min(single_values):.12f} max={max(single_values):.12f}"
    )
    print(
        f"  pair deletions: edge-positive={positive_edges} "
        f"nonedge-positive={positive_non_edges}; best={best_pair}"
    )

    if triples:
        best_triple = (-1e100, None, None)
        positive = 0
        for deleted in combinations(range(42), 3):
            result = score(induced(graph, set(deleted)))
            assert result is not None
            phi, dual, least = result
            positive += int(phi > 1e-9)
            if phi > best_triple[0]:
                best_triple = (phi, deleted, (dual, least))
        print(f"  triple deletions: tested=11480 positive={positive}; best={best_triple}")


def screen_96() -> None:
    graph = graph96()
    single_results = [score(induced(graph, {u})) for u in range(96)]
    assert all(x is not None for x in single_results)
    single_values = [x[0] for x in single_results if x is not None]
    edge_results = []
    for u in range(96):
        for v in graph[u]:
            if u < v:
                result = score(induced(graph, {u, v}))
                assert result is not None
                edge_results.append(result[0])
    print("order-96 equality-graph deletion screen")
    print(
        f"  singles: count=96 positive={sum(v > 1e-9 for v in single_values)} "
        f"min={min(single_values):.12f} max={max(single_values):.12f}"
    )
    print(
        f"  edges: count={len(edge_results)} positive={sum(v > 1e-9 for v in edge_results)} "
        f"min={min(edge_results):.12f} max={max(edge_results):.12f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triples42", action="store_true")
    parser.add_argument("--large96", action="store_true")
    args = parser.parse_args()
    screen_40_pairs()
    screen_42(args.triples42)
    if args.large96:
        screen_96()


if __name__ == "__main__":
    main()
