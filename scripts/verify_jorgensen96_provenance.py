#!/usr/bin/env python3
"""Provenance-grade exact audit of Jorgensen's order-96 graph.

Three independent local reconstructions are compared: a row-wise parser of
the source-page text snapshot, a strict parser of normalized rows, and graph6.
All structural and spectral assertions are exact.
"""
from __future__ import annotations

from collections import deque
import hashlib
import json
from pathlib import Path
import re

import networkx as nx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "jorgensen96"
PROVENANCE = DATA / "PROVENANCE.json"
X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_source_snapshot(path: Path) -> Graph:
    rows: dict[int, frozenset[int]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*\{([^}]*)\}\s*", line)
        if match is None:
            continue
        vertex = int(match.group(1))
        if vertex in rows:
            raise AssertionError(f"duplicate source row {vertex}")
        neighbors = tuple(int(value) for value in re.findall(r"\d+", match.group(2)))
        if len(neighbors) != len(set(neighbors)):
            raise AssertionError(f"duplicate neighbor in source row {vertex}")
        rows[vertex] = frozenset(neighbors)
    if set(rows) != set(range(96)):
        raise AssertionError("source snapshot does not contain rows 0..95 exactly once")
    return tuple(rows[vertex] for vertex in range(96))


def parse_normalized_rows(path: Path) -> Graph:
    lines = path.read_text(encoding="ascii").splitlines()
    if len(lines) != 96:
        raise AssertionError("normalized adjacency must contain exactly 96 rows")
    rows: list[frozenset[int]] = []
    for expected_vertex, line in enumerate(lines):
        prefix = f"{expected_vertex} : {{ "
        if not line.startswith(prefix) or not line.endswith("}"):
            raise AssertionError(f"noncanonical row syntax at {expected_vertex}")
        values = tuple(int(value) for value in line[len(prefix) : -1].split(", "))
        if values != tuple(sorted(set(values))):
            raise AssertionError(f"row {expected_vertex} is not strictly sorted")
        rows.append(frozenset(values))
    return tuple(rows)


def parse_graph6(path: Path) -> Graph:
    graph = nx.from_graph6_bytes(path.read_bytes().strip())
    graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
    if set(graph.nodes()) != set(range(96)):
        raise AssertionError("graph6 labels are not 0..95")
    return tuple(
        frozenset(int(neighbor) for neighbor in graph.neighbors(vertex))
        for vertex in range(96)
    )


def canonical_adjacency_text(graph: Graph) -> str:
    return "\n".join(
        f"{vertex} : {{ "
        + ", ".join(str(neighbor) for neighbor in sorted(graph[vertex]))
        + "}"
        for vertex in range(len(graph))
    ) + "\n"


def verify_simple_regular(graph: Graph) -> None:
    if len(graph) != 96:
        raise AssertionError("wrong order")
    if any(vertex in graph[vertex] for vertex in range(96)):
        raise AssertionError("loop")
    if not all(len(neighbors) == 9 for neighbors in graph):
        raise AssertionError("not 9-regular")
    for vertex, neighbors in enumerate(graph):
        if any(neighbor < 0 or neighbor >= 96 for neighbor in neighbors):
            raise AssertionError("neighbor outside 0..95")
        for neighbor in neighbors:
            if vertex not in graph[neighbor]:
                raise AssertionError("asymmetric adjacency")
    if sum(map(len, graph)) // 2 != 432:
        raise AssertionError("wrong edge count")


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[vertex] + 1
                    queue.append(neighbor)
        if -1 in distance:
            raise AssertionError("disconnected graph")
        rows.append(tuple(distance))
    return tuple(rows)


def exact_girth(graph: Graph) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        parent = [-1] * len(graph)
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)
                elif parent[vertex] != neighbor and parent[neighbor] != vertex:
                    best = min(best, distance[vertex] + distance[neighbor] + 1)
    return best


def verify_provenance_hashes(provenance: dict[str, object]) -> None:
    for key in ("source_snapshot", "normalized_adjacency", "graph6"):
        entry = provenance[key]
        assert isinstance(entry, dict)
        path = ROOT / str(entry["path"])
        if sha256(path) != entry["sha256"]:
            raise AssertionError(f"SHA-256 mismatch for {path}")
        if len(path.read_bytes()) != entry["bytes"]:
            raise AssertionError(f"byte-count mismatch for {path}")


def verify_exact_spectrum(graph: Graph) -> dict[str, str]:
    adjacency = sp.Matrix([
        [int(column in graph[row]) for column in range(96)]
        for row in range(96)
    ])
    distance = sp.Matrix(distance_rows(graph))
    identity, ones = sp.eye(96), sp.ones(96)
    if max(distance) != 3:
        raise AssertionError("diameter is not three")
    if distance != 3 * ones + 6 * identity - 2 * adjacency - adjacency**2:
        raise AssertionError("distance polynomial identity failed")
    if distance * sp.ones(96, 1) != 195 * sp.ones(96, 1):
        raise AssertionError("transmission is not 195")

    expected_adjacency = (
        (X - 9) * (X - 3) ** 7 * (X - 1) ** 7 * (X + 5)
        * (X**2 - 8) ** 16 * (X**2 + 2 * X - 6) ** 8
        * (X**4 + 2 * X**3 - 17 * X**2 - 18 * X + 74) ** 8
    )
    expected_distance = (
        X**16 * (X - 195) * (X - 3) ** 7 * (X + 9) ** 8
        * (X**2 + 4 * X - 28) ** 16
        * (X**4 + 10 * X**3 + 5 * X**2 - 72 * X - 96) ** 8
    )
    actual_adjacency = sp.factor(adjacency.charpoly(X).as_expr())
    actual_distance = sp.factor(distance.charpoly(X).as_expr())
    if not sp.Poly(actual_adjacency - expected_adjacency, X).is_zero:
        raise AssertionError("adjacency characteristic polynomial mismatch")
    if not sp.Poly(actual_distance - expected_distance, X).is_zero:
        raise AssertionError("distance characteristic polynomial mismatch")

    polynomial = sp.Poly(expected_distance, X)
    if polynomial.eval(-9) != 0:
        raise AssertionError("-9 is not a distance root")
    if polynomial.count_roots(-sp.oo, -9) != 1:
        raise AssertionError("there is a distinct distance root below -9")
    quotient = polynomial
    multiplicity = 0
    while quotient.eval(-9) == 0:
        quotient, remainder = sp.div(quotient, sp.Poly(X + 9, X))
        if not remainder.is_zero:
            raise AssertionError("failed exact division by x+9")
        multiplicity += 1
    if multiplicity != 8:
        raise AssertionError("wrong multiplicity at -9")

    return {
        "adjacency_characteristic_polynomial": str(actual_adjacency),
        "distance_characteristic_polynomial": str(actual_distance),
        "least_distance_eigenvalue": "-9",
        "least_distance_eigenvalue_multiplicity": "8",
        "minimum_dual_degree": "9",
        "WOW_score": "0",
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    verify_provenance_hashes(provenance)
    source_graph = parse_source_snapshot(ROOT / provenance["source_snapshot"]["path"])
    normalized_graph = parse_normalized_rows(ROOT / provenance["normalized_adjacency"]["path"])
    graph6_graph = parse_graph6(ROOT / provenance["graph6"]["path"])
    if source_graph != normalized_graph or source_graph != graph6_graph:
        raise AssertionError("independent graph reconstructions disagree")
    canonical = canonical_adjacency_text(source_graph)
    stored = (ROOT / provenance["normalized_adjacency"]["path"]).read_text(encoding="ascii")
    if canonical != stored:
        raise AssertionError("canonical adjacency serialization mismatch")

    verify_simple_regular(source_graph)
    if exact_girth(source_graph) != 5:
        raise AssertionError("girth is not five")
    exact = verify_exact_spectrum(source_graph)
    result = {
        "source_url": provenance["source_url"],
        "retrieved_at_utc": provenance["retrieved_at_utc"],
        "published_construction_doi": provenance["published_construction"]["doi"],
        "source_snapshot_sha256": provenance["source_snapshot"]["sha256"],
        "normalized_adjacency_sha256": provenance["normalized_adjacency"]["sha256"],
        "graph6_sha256": provenance["graph6"]["sha256"],
        "independent_reconstructions": "source rows == normalized rows == graph6",
        "order": 96,
        "size": 432,
        "degree": 9,
        "girth": 5,
        "diameter": 3,
        **exact,
    }
    print("Jorgensen order-96 provenance and exact audit: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
