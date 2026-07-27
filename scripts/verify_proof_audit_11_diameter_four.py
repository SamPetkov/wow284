#!/usr/bin/env python3
"""Independent exact audit of the regular diameter-four obstruction.

This verifier does not import the original extension verifier. It checks the
symbolic comparison, every diametral pair in two independent finite controls,
and exact characteristic polynomials. No floating-point arithmetic or numerical
eigensolver is used.
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


def cycle_graph(order: int) -> Graph:
    return graph_from_edges(order, [(i, (i + 1) % order) for i in range(order)])


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
    graph = tuple(frozenset(row) for row in rows)
    if set(map(len, graph)) != {7}:
        raise AssertionError("bad Hoffman--Singleton degree")
    return graph


def affine_matching_deletion() -> Graph:
    modulus = 5
    p = lambda i, j: 5 * (i % modulus) + (j % modulus)
    q = lambda k, ell: 25 + 5 * (k % modulus) + (ell % modulus)
    rows = [set(row) for row in hoffman_singleton()]
    for i in range(modulus):
        for j in range(modulus):
            u, v = p(i, j), q(i, i * i + j)
            if v not in rows[u]:
                raise AssertionError("deleted pair is not an edge")
            rows[u].remove(v)
            rows[v].remove(u)
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


def symbolic_audit() -> dict[str, str]:
    k = sp.symbols("k", integer=True, positive=True)
    lam = sp.symbols("lambda")
    matrix = sp.Matrix([[-4, -2 * sp.sqrt(k)], [-2 * sp.sqrt(k), -3]])
    expected = lam**2 + 7 * lam + 12 - 4 * k
    if sp.expand(matrix.charpoly(lam).as_expr() - expected) != 0:
        raise AssertionError("wrong comparison characteristic polynomial")

    mu = -(7 + sp.sqrt(16 * k + 1)) / 2
    vector = sp.Matrix([2 * sp.sqrt(k), -4 - mu])
    if sp.simplify(matrix * vector - mu * vector) != sp.zeros(2, 1):
        raise AssertionError("least-eigenvector identity failed")
    positive_coordinate = (sp.sqrt(16 * k + 1) - 1) / 2
    if sp.simplify((-4 - mu) - positive_coordinate) != 0:
        raise AssertionError("least-eigenvector coordinate identity failed")

    excluded = []
    for degree in range(2, 10):
        if sp.simplify(mu.subs(k, degree) + degree) >= 0:
            raise AssertionError(f"degree {degree} was not excluded")
        excluded.append(degree)
    if sp.simplify(mu.subs(k, 10) + 10) <= 0:
        raise AssertionError("the method was incorrectly claimed to exclude degree ten")

    return {
        "comparison_matrix": str(matrix),
        "least_eigenvalue": str(mu),
        "positive_eigenvector": str(vector),
        "excluded_degrees": str(excluded),
        "degree_ten_method_margin": str(sp.simplify(mu.subs(k, 10) + 10)),
    }


def audit_control(graph: Graph, expected_charpoly: sp.Expr) -> dict[str, object]:
    degrees = tuple(map(len, graph))
    if len(set(degrees)) != 1:
        raise AssertionError("control is not regular")
    k = degrees[0]
    if exact_girth(graph) < 5:
        raise AssertionError("control girth below five")
    distances = distance_rows(graph)
    if max(map(max, distances)) != 4:
        raise AssertionError("control diameter is not four")
    distance = sp.Matrix(distances)
    charpoly = sp.factor(distance.charpoly(X).as_expr())
    if not sp.Poly(charpoly - expected_charpoly, X).is_zero:
        raise AssertionError("control characteristic polynomial mismatch")

    mu = -(7 + sp.sqrt(16 * k + 1)) / 2
    pair_count = 0
    r_values: set[int] = set()
    sum_values: set[int] = set()
    margins: set[str] = set()

    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if distances[u][v] != 4:
                continue
            pair_count += 1
            first, second = graph[u], graph[v]
            if not first.isdisjoint(second):
                raise AssertionError("diametral endpoint neighborhoods overlap")
            if any(b in graph[a] for a in first for b in second):
                raise AssertionError("cross-neighborhood edge shortens the diameter")

            count = 0
            total_distance = 0
            for a in first:
                used_common: set[int] = set()
                for b in second:
                    total_distance += distances[a][b]
                    if distances[a][b] == 2:
                        common = graph[a] & graph[b]
                        if len(common) != 1:
                            raise AssertionError("distance-two pair lacks a unique common neighbor")
                        witness = next(iter(common))
                        if witness in {u, v} or witness in used_common:
                            raise AssertionError("cross-neighborhood injection failed")
                        used_common.add(witness)
                        count += 1
                if len(used_common) > k - 1:
                    raise AssertionError("too many distance-two partners")
            if count > k * (k - 1):
                raise AssertionError("global cross-neighborhood bound failed")
            if total_distance < 2 * k * k + k:
                raise AssertionError("cross-neighborhood distance-sum bound failed")

            alpha = 2 * sp.sqrt(k)
            beta = (-4 - mu) / sp.sqrt(k)
            vector = sp.zeros(len(graph), 1)
            vector[u], vector[v] = alpha, -alpha
            for a in first:
                vector[a] = beta
            for b in second:
                vector[b] = -beta
            quotient = sp.simplify(
                (vector.T * distance * vector)[0] / (vector.T * vector)[0]
            )
            margin = sp.simplify(mu - quotient)
            if sp.ask(sp.Q.nonnegative(margin)) is not True:
                raise AssertionError("finite Rayleigh control exceeds the theorem bound")
            r_values.add(count)
            sum_values.add(total_distance)
            margins.add(str(margin))

    if pair_count == 0:
        raise AssertionError("no diametral pair was audited")
    return {
        "order": len(graph),
        "degree": k,
        "girth": exact_girth(graph),
        "diameter": 4,
        "diametral_pairs": pair_count,
        "distance_two_cross_counts": sorted(r_values),
        "cross_distance_sums": sorted(sum_values),
        "Rayleigh_margins": sorted(margins),
        "distance_characteristic_polynomial": str(charpoly),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    c8_polynomial = X**3 * (X - 16) * (X**2 + 8 * X + 8)**2
    affine_polynomial = (
        (X - 106)
        * (X - 2)
        * (X - 1) ** 4
        * (X + 13) ** 4
        * (X**2 + X - 1) ** 8
        * (X**2 + 3 * X - 9) ** 8
        * (X**4 + 14 * X**3 + 13 * X**2 - 92 * X - 16) ** 2
    )
    result = {
        "symbolic": symbolic_audit(),
        "controls": {
            "C8": audit_control(cycle_graph(8), c8_polynomial),
            "HS_affine_matching_deletion": audit_control(
                affine_matching_deletion(), affine_polynomial
            ),
        },
    }
    print("Proof Audit 11 (diameter-four obstruction): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
