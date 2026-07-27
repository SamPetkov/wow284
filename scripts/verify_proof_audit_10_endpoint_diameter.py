#!/usr/bin/env python3
"""Independent exact audit of the endpoint-neighborhood diameter obstruction.

The script does not import the original diameter-extension verifier. It checks
the symbolic 2x2 reduction, the positive least eigenvector, the minimum-degree
radical identity, the integer rounding, and exact finite graph controls. No
floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def graph_from_edges(order: int, edges: list[tuple[int, int]]) -> Graph:
    rows = [set() for _ in range(order)]
    for u, v in edges:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)
    return tuple(frozenset(row) for row in rows)


def path_graph(order: int) -> Graph:
    return graph_from_edges(order, [(i, i + 1) for i in range(order - 1)])


def cycle_graph(order: int) -> Graph:
    return graph_from_edges(order, [(i, (i + 1) % order) for i in range(order)])


def c5_with_tail() -> Graph:
    edges = [(i, (i + 1) % 5) for i in range(5)]
    edges.extend([(0, 5), (5, 6), (6, 7), (7, 8)])
    return graph_from_edges(9, edges)


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
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
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, distance[u] + distance[v] + 1)
    return best


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def symbolic_audit() -> dict[str, str]:
    p, q, t = sp.symbols("p q t", positive=True)
    delta = sp.symbols("delta", positive=True)
    alpha, beta = sp.symbols("alpha beta", nonnegative=True)
    lam = sp.symbols("lambda")

    a_entry = 2 * (p - 1)
    b_entry = 2 * (q - 1)
    c_entry = t * sp.sqrt(p * q)
    matrix = sp.Matrix([[a_entry, -c_entry], [-c_entry, b_entry]])
    expected_charpoly = (
        lam**2
        - (a_entry + b_entry) * lam
        + a_entry * b_entry
        - c_entry**2
    )
    if sp.expand(matrix.charpoly(lam).as_expr() - expected_charpoly) != 0:
        raise AssertionError("wrong comparison-matrix characteristic polynomial")

    discriminant = sp.simplify((a_entry - b_entry) ** 2 + 4 * c_entry**2)
    least = sp.simplify((a_entry + b_entry - sp.sqrt(discriminant)) / 2)
    expected_least = p + q - 2 - sp.sqrt((p - q) ** 2 + p * q * t**2)
    if sp.simplify(least - expected_least) != 0:
        raise AssertionError("wrong least eigenvalue")

    vector = sp.Matrix([c_entry, a_entry - least])
    if sp.simplify(matrix * vector - least * vector) != sp.zeros(2, 1):
        raise AssertionError("explicit least eigenvector failed")

    p_sub = delta + alpha
    q_sub = delta + beta
    radicand = (p_sub - q_sub) ** 2 + p_sub * q_sub * t**2
    target = p_sub + q_sub + delta * (t - 2)
    identity = sp.expand(radicand - target**2)
    expected_identity = sp.expand(
        (t - 2)
        * (delta * t * (alpha + beta) + (t + 2) * alpha * beta)
    )
    if sp.expand(identity - expected_identity) != 0:
        raise AssertionError("wrong minimum-degree radical identity")

    k = sp.symbols("k", integer=True, positive=True)
    d = sp.symbols("d", integer=True, positive=True)
    score_bound = sp.expand(k + (-k * (d - 4) - 2))
    if score_bound != k * (5 - d) - 2:
        raise AssertionError("wrong regular score bound")
    moore_bound = sp.expand(1 + k * sum((k - 1) ** i for i in range(4)))
    if moore_bound != k**4 - 2 * k**3 + 2 * k**2 + 1:
        raise AssertionError("wrong diameter-four Moore bound")

    # Exact finite audit of the strict integer-rounding implication.
    for minimum in range(1, 21):
        for maximum in range(minimum, 61):
            for diameter in range(5, 61):
                if maximum > minimum * (diameter - 4) + 2:
                    ceiling = (maximum - 2 + minimum - 1) // minimum
                    if diameter > 3 + ceiling:
                        raise AssertionError("integer diameter rounding failed")

    return {
        "comparison_matrix": str(matrix),
        "least_eigenvalue": str(least),
        "positive_eigenvector": str(vector),
        "radical_difference": str(sp.factor(identity)),
        "regular_score_bound": str(score_bound),
        "diameter_four_Moore_bound": str(moore_bound),
    }


def control_audit(name: str, graph: Graph) -> dict[str, object]:
    distances = distance_rows(graph)
    diameter = max(max(row) for row in distances)
    if diameter < 5:
        raise AssertionError("control diameter is below five")
    degrees = [len(row) for row in graph]
    delta, maximum = min(degrees), max(degrees)
    if delta <= 0:
        raise AssertionError("control has an isolated vertex")

    pairs = [
        (u, v)
        for u in range(len(graph))
        for v in range(u + 1, len(graph))
        if distances[u][v] == diameter
    ]
    if not pairs:
        raise AssertionError("no diametral pair")
    u, v = pairs[0]
    neighborhood_u = sorted(graph[u])
    neighborhood_v = sorted(graph[v])
    if set(neighborhood_u) & set(neighborhood_v):
        raise AssertionError("diametral endpoint neighborhoods overlap")
    p, q = len(neighborhood_u), len(neighborhood_v)
    t = diameter - 2

    distance_matrix = sp.Matrix(distances)
    indicator_u = sp.zeros(len(graph), 1)
    indicator_v = sp.zeros(len(graph), 1)
    for vertex in neighborhood_u:
        indicator_u[vertex] = 1 / sp.sqrt(p)
    for vertex in neighborhood_v:
        indicator_v[vertex] = -1 / sp.sqrt(q)
    basis = sp.Matrix.hstack(indicator_u, indicator_v)
    actual = sp.simplify(basis.T * distance_matrix * basis)

    comparison = sp.Matrix(
        [
            [2 * (p - 1), -t * sp.sqrt(p * q)],
            [-t * sp.sqrt(p * q), 2 * (q - 1)],
        ]
    )
    if sp.ask(sp.Q.nonnegative(comparison[0, 0] - actual[0, 0])) is not True:
        raise AssertionError("wrong first within-neighborhood direction")
    if sp.ask(sp.Q.nonnegative(comparison[1, 1] - actual[1, 1])) is not True:
        raise AssertionError("wrong second within-neighborhood direction")
    if sp.ask(sp.Q.nonnegative(comparison[0, 1] - actual[0, 1])) is not True:
        raise AssertionError("wrong cross-distance direction")

    discriminant = (p - q) ** 2 + p * q * t**2
    endpoint_bound = sp.Integer(p + q - 2) - sp.sqrt(discriminant)
    a_entry = sp.Integer(2 * (p - 1))
    c_entry = sp.Integer(t) * sp.sqrt(p * q)
    vector = sp.Matrix([c_entry, a_entry - endpoint_bound])
    if sp.ask(sp.Q.positive(vector[0])) is not True:
        raise AssertionError("first minimizing coordinate is not positive")
    if sp.ask(sp.Q.positive(vector[1])) is not True:
        raise AssertionError("second minimizing coordinate is not positive")
    if sp.simplify(comparison * vector - endpoint_bound * vector) != sp.zeros(2, 1):
        raise AssertionError("finite least eigenvector failed")

    actual_quotient = sp.simplify(
        (vector.T * actual * vector)[0] / (vector.T * vector)[0]
    )
    difference = sp.simplify(endpoint_bound - actual_quotient)
    if sp.ask(sp.Q.nonnegative(difference)) is not True:
        raise AssertionError("actual Rayleigh quotient exceeds endpoint bound")

    full_vector = sp.simplify(basis * vector)
    full_quotient = sp.simplify(
        (full_vector.T * distance_matrix * full_vector)[0]
        / (full_vector.T * full_vector)[0]
    )
    if sp.simplify(full_quotient - actual_quotient) != 0:
        raise AssertionError("compressed and full Rayleigh quotients disagree")

    uniform_bound = -delta * (diameter - 4) - 2
    if sp.ask(sp.Q.nonnegative(endpoint_bound - uniform_bound)) is not True:
        raise AssertionError("endpoint bound does not imply uniform bound")

    # When the uniform bound is not itself a root, independently confirm that
    # the exact distance polynomial has a root below it.
    charpoly = distance_matrix.charpoly(X).as_poly()
    root_certificate = "Rayleigh"
    if charpoly.eval(uniform_bound) != 0:
        if charpoly.count_roots(-sp.oo, uniform_bound) < 1:
            raise AssertionError("exact root certificate failed")
        root_certificate = "Rayleigh + Sturm"

    return {
        "order": len(graph),
        "girth": exact_girth(graph),
        "diameter": diameter,
        "minimum_degree": delta,
        "maximum_degree": maximum,
        "endpoint_degrees": [p, q],
        "endpoint_bound": str(endpoint_bound),
        "uniform_bound": uniform_bound,
        "actual_test_quotient": str(actual_quotient),
        "certificate": root_certificate,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    controls = {
        "path_P6": path_graph(6),
        "cycle_C10": cycle_graph(10),
        "C5_with_length4_tail": c5_with_tail(),
    }
    result = {
        "symbolic_audit": symbolic_audit(),
        "finite_controls": {
            name: control_audit(name, graph) for name, graph in controls.items()
        },
    }
    print("Proof Audit 10 (endpoint-neighborhood diameter obstruction): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
