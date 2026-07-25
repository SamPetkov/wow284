#!/usr/bin/env python3
"""Independent exact audit of the edge-local order-51 exclusion.

This verifier does not import the original edge-local verifier.  It checks the
missing degree-six diameter reduction, all symbolic matrix-entry identities,
the radius-two intersection bijection on two independent concrete controls,
and the final integral incidence contradiction.  No floating-point arithmetic
is used.
"""
from __future__ import annotations

from collections import deque
import json

import sympy as sp

Graph = tuple[frozenset[int], ...]
X = sp.symbols("x")


def p(i: int, j: int) -> int:
    return 5 * (i % 5) + (j % 5)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % 5) + (ell % 5)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def add(u: int, v: int) -> None:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(5):
                add(p(i, j), q(k, i * k + j))
    graph = tuple(frozenset(row) for row in rows)
    if not all(len(row) == 7 for row in graph):
        raise AssertionError("bad Hoffman-Singleton degree")
    return graph


def induced(graph: Graph, deleted: set[int]) -> Graph:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    relabel = {old: new for new, old in enumerate(keep)}
    return tuple(
        frozenset(relabel[w] for w in graph[v] if w in relabel) for v in keep
    )


def graph40() -> Graph:
    full = hoffman_singleton()
    return induced(full, set(range(5)) | set(range(25, 30)))


def graph42() -> Graph:
    full = hoffman_singleton()
    return induced(full, {0} | set(full[0]))


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
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
            raise AssertionError("disconnected control graph")
        rows.append(tuple(dist))
    return tuple(rows)


def exact_girth(graph: Graph) -> int:
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


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def five_cycles_through_edge(graph: Graph, u: int, v: int) -> int:
    """Count complementary simple four-edge paths from u to v."""
    if v not in graph[u]:
        raise AssertionError("not an edge")
    count = 0
    for a in graph[u]:
        if a == v:
            continue
        for b in graph[a]:
            if b in {u, v, a}:
                continue
            for c in graph[b]:
                if c in {u, v, a, b}:
                    continue
                if v in graph[c]:
                    count += 1
    return count


def ball_two(distances: tuple[tuple[int, ...], ...], u: int) -> set[int]:
    return {v for v, value in enumerate(distances[u]) if value <= 2}


def verify_symbolic_core() -> dict[str, str]:
    k, n, sigma, d = sp.symbols(
        "k n sigma d", integer=True, positive=True
    )
    f = sp.expand((X + 2) ** 2 * (X**2 + 2 * X - (2 * k - 3)))
    expected_f = (
        X**4
        + 6 * X**3
        + (15 - 2 * k) * X**2
        + (20 - 8 * k) * X
        + 12
        - 8 * k
    )
    if sp.expand(f - expected_f) != 0:
        raise AssertionError("wrong polynomial expansion")

    constant = sp.factor(f.subs(X, k))
    if constant != (k + 2) ** 2 * (k**2 + 3):
        raise AssertionError("wrong principal value")

    diagonal_f = sp.factor(k * (2 * k - 1) + (15 - 2 * k) * k + 12 - 8 * k)
    edge_f = sp.factor(sigma + 6 * (2 * k - 1) + 20 - 8 * k)
    if diagonal_f != 6 * (k + 2):
        raise AssertionError("wrong diagonal entry")
    if edge_f != sigma + 4 * k + 14:
        raise AssertionError("wrong edge entry")

    m_diagonal = constant / n - diagonal_f
    m_edge = constant / n - edge_f
    if sp.simplify(m_diagonal - m_edge - (sigma - (2 * k - 2))) != 0:
        raise AssertionError("wrong lower edge-cycle inequality")
    if sp.simplify(
        m_diagonal
        + m_edge
        - (2 * constant / n - 10 * k - 26 - sigma)
    ) != 0:
        raise AssertionError("wrong upper edge-cycle inequality")

    # Degree-six diameter reduction.  The unordered quadratic contribution for
    # weights 3,1,-3,-1 on two closed neighborhoods is 204-81d.
    unordered = sp.expand(
        96 - 9 * d - 36 * (d - 1) - 36 * (d - 2)
    )
    if unordered != 204 - 81 * d:
        raise AssertionError("wrong diameter Rayleigh numerator")
    rayleigh = sp.factor(unordered / 15)
    if rayleigh.subs(d, 4) != -8:
        raise AssertionError("wrong diameter-four bound")
    if sp.diff(rayleigh, d) >= 0:
        raise AssertionError("diameter bound is not decreasing")

    # Diameter two would force the stated characteristic polynomial and a
    # nonzero trace, impossible for a simple adjacency matrix.
    moore_charpoly = sp.expand((X - 6) * (X**2 + X - 5) ** 18)
    coefficient_x36 = sp.Poly(moore_charpoly, X).coeff_monomial(X**36)
    if coefficient_x36 != 12:
        raise AssertionError("wrong forced Moore trace coefficient")
    if sp.discriminant(X**2 + X - 5, X) != 21:
        raise AssertionError("wrong Moore discriminant")

    # Final order-51 arithmetic.
    k6 = sp.Integer(6)
    n51 = sp.Integer(51)
    c14 = sp.Integer(14)
    lower = (k6 - 1) ** 2 - c14
    upper = sp.factor(
        2 * (k6 + 2) ** 2 * (k6**2 + 3) / n51 - 10 * k6 - 26
    )
    if lower != 11 or upper != sp.Rational(202, 17):
        raise AssertionError("wrong order-51 bounds")
    if not lower <= upper < 12:
        raise AssertionError("order-51 integrality interval failed")
    incidences = sp.Integer(6 * 51 // 2) * lower
    if incidences != 1683 or incidences % 5 == 0:
        raise AssertionError("order-51 incidence contradiction failed")

    return {
        "expanded_polynomial": str(f),
        "principal_value": str(constant),
        "diameter_rayleigh_bound": str(rayleigh),
        "forced_diameter_two_x36_coefficient": str(coefficient_x36),
        "order_51_spectral_upper": str(upper),
        "order_51_incidence_total": str(incidences),
    }


def audit_control(name: str, graph: Graph, expected_sigma: int) -> dict[str, object]:
    n = len(graph)
    degrees = {len(row) for row in graph}
    if degrees != {6}:
        raise AssertionError(f"{name}: not 6-regular")
    if exact_girth(graph) != 5:
        raise AssertionError(f"{name}: wrong girth")
    distances = distance_rows(graph)
    if max(max(row) for row in distances) != 3:
        raise AssertionError(f"{name}: wrong diameter")

    a = adjacency_matrix(graph)
    a2 = a * a
    a3 = a2 * a
    a4 = a3 * a
    f_a = (
        a4
        + 6 * a3
        + 3 * a2
        - 28 * a
        - 36 * sp.eye(n)
    )
    # This is f_6(A): 15-2k=3, 20-8k=-28, 12-8k=-36.
    constant = sp.Integer(2496)
    m = -f_a + sp.Rational(constant, n) * sp.ones(n)

    sigma_values: list[int] = []
    for u, neighbors in enumerate(graph):
        if f_a[u, u] != 48:
            raise AssertionError(f"{name}: wrong diagonal polynomial entry")
        for v in neighbors:
            if u >= v:
                continue
            sigma = five_cycles_through_edge(graph, u, v)
            sigma_values.append(sigma)
            if a2[u, v] != 0:
                raise AssertionError(f"{name}: edge lies in a triangle")
            if a3[u, v] != 11:
                raise AssertionError(f"{name}: wrong length-three walk count")
            if a4[u, v] != sigma:
                raise AssertionError(f"{name}: length-four/5-cycle mismatch")
            if f_a[u, v] != sigma + 38:
                raise AssertionError(f"{name}: wrong edge polynomial entry")

            intersection = ball_two(distances, u) & ball_two(distances, v)
            if len(intersection) != 12 + sigma:
                raise AssertionError(f"{name}: radius-two intersection mismatch")

            diagonal = m[u, u]
            edge = m[u, v]
            if diagonal < 0 or sp.factor(diagonal**2 - edge**2) < 0:
                raise AssertionError(f"{name}: failed 2x2 PSD control")

    if set(sigma_values) != {expected_sigma}:
        raise AssertionError(f"{name}: unexpected edge cycle counts")
    total_five_cycles = sum(sigma_values) // 5
    if 5 * total_five_cycles != sum(sigma_values):
        raise AssertionError(f"{name}: edge-cycle incidence mismatch")

    return {
        "order": n,
        "edge_count": len(sigma_values),
        "edge_five_cycle_count": expected_sigma,
        "total_five_cycles": total_five_cycles,
        "all_walk_and_ball_identities": True,
        "all_edge_2x2_psd_controls": True,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "symbolic_and_arithmetic_audit": verify_symbolic_core(),
        "independent_controls": {
            "order_40": audit_control("order_40", graph40(), 22),
            "order_42": audit_control("order_42", graph42(), 20),
        },
    }
    print("Proof Audit 01 (edge-local order-51 exclusion): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
