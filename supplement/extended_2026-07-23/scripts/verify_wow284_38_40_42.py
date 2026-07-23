#!/usr/bin/env python3
"""Exact independent audit of several WOW-284 counterexamples.

Requires Python 3.11+ and SymPy 1.14.

The script constructs the Hoffman--Singleton coordinate graph directly over
Z/5Z, then verifies:

* the proposed 40-vertex graph obtained by deleting P_(0,*) and Q_(0,*);
* a 42-vertex graph obtained as the second subconstituent of one vertex;
* a 39-vertex graph obtained by deleting one vertex from the 40-vertex graph;
* a 38-vertex graph obtained by deleting the adjacent pair P_(1,0), P_(1,1)
  from the 40-vertex graph.

All matrix identities, characteristic polynomials, dual degrees, and LDL^T
certificates are computed over the integers or rationals. Floating point is
not used for any proof assertion.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations

import sympy as sp

Q = 5
X = sp.symbols("x")

Vertex = tuple[str, int, int]
Graph = tuple[frozenset[int], ...]


def vertices_hs() -> tuple[Vertex, ...]:
    return tuple(
        [("P", i, j) for i in range(Q) for j in range(Q)]
        + [("Q", k, ell) for k in range(Q) for ell in range(Q)]
    )


def hoffman_singleton() -> tuple[Graph, tuple[Vertex, ...]]:
    labels = vertices_hs()
    index = {label: i for i, label in enumerate(labels)}
    mutable = [set() for _ in labels]

    def add(a: Vertex, b: Vertex) -> None:
        u, v = index[a], index[b]
        if u == v:
            raise AssertionError(f"loop at {a}")
        mutable[u].add(v)
        mutable[v].add(u)

    for i in range(Q):
        for j in range(Q):
            add(("P", i, j), ("P", i, (j + 1) % Q))
    for k in range(Q):
        for ell in range(Q):
            add(("Q", k, ell), ("Q", k, (ell + 2) % Q))
    for i in range(Q):
        for j in range(Q):
            for k in range(Q):
                add(("P", i, j), ("Q", k, (i * k + j) % Q))

    return tuple(frozenset(row) for row in mutable), labels


def induced(graph: Graph, labels: tuple[Vertex, ...], deleted: set[Vertex]) -> tuple[Graph, tuple[Vertex, ...]]:
    keep_old = [i for i, label in enumerate(labels) if label not in deleted]
    old_to_new = {old: new for new, old in enumerate(keep_old)}
    new_graph = tuple(
        frozenset(old_to_new[v] for v in graph[u] if v in old_to_new)
        for u in keep_old
    )
    new_labels = tuple(labels[u] for u in keep_old)
    return new_graph, new_labels


def bfs_distances(graph: Graph) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        distance[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        if -1 in distance:
            raise AssertionError(f"disconnected from source {source}")
        rows.append(tuple(distance))
    return tuple(rows)


def girth(graph: Graph) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        parent = [-1] * len(graph)
        distance[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, distance[u] + distance[v] + 1)
    if best == len(graph) + 1:
        raise AssertionError("acyclic graph")
    return best


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    n = len(graph)
    return sp.Matrix([[int(j in graph[i]) for j in range(n)] for i in range(n)])


def dual_degrees(graph: Graph) -> tuple[Fraction, ...]:
    degree = tuple(len(row) for row in graph)
    return tuple(
        Fraction(sum(degree[u] for u in graph[v]), degree[v])
        for v in range(len(graph))
    )


def basic_checks(graph: Graph) -> tuple[tuple[int, ...], sp.Matrix, sp.Matrix]:
    n = len(graph)
    for u, row in enumerate(graph):
        assert u not in row
        for v in row:
            assert u in graph[v]
    distance_rows = bfs_distances(graph)
    a = adjacency_matrix(graph)
    d = sp.Matrix(distance_rows)
    assert d == d.T
    assert a == a.T
    assert all(d[i, i] == 0 for i in range(n))
    return tuple(map(len, graph)), a, d


def exact_ldl_positive(matrix: sp.Matrix) -> tuple[sp.Rational, ...]:
    lower, diagonal = matrix.LDLdecomposition(hermitian=True)
    assert lower * diagonal * lower.T == matrix
    pivots = tuple(sp.factor(diagonal[i, i]) for i in range(matrix.rows))
    assert all(bool(pivot > 0) for pivot in pivots)
    return pivots


def verify_40(full: Graph, full_labels: tuple[Vertex, ...]) -> tuple[Graph, tuple[Vertex, ...], sp.Matrix, sp.Matrix]:
    deleted = {("P", 0, j) for j in range(Q)} | {("Q", 0, j) for j in range(Q)}
    graph, labels = induced(full, full_labels, deleted)
    degrees, b, d = basic_checks(graph)

    assert len(graph) == 40
    assert sum(degrees) // 2 == 120
    assert set(degrees) == {6}
    assert girth(graph) == 5
    assert max(max(row) for row in d.tolist()) == 3
    assert set(dual_degrees(graph)) == {Fraction(6)}

    expected_b = (X - 6) * (X - 2) ** 18 * (X - 1) ** 4 * (X + 2) ** 5 * (X + 3) ** 12
    expected_d = (X - 75) * (X - 3) ** 5 * X**16 * (X + 5) ** 18
    assert sp.Poly(b.charpoly(X).as_expr() - expected_b, X).is_zero
    assert sp.Poly(d.charpoly(X).as_expr() - expected_d, X).is_zero
    assert d == 3 * sp.ones(40) + 3 * sp.eye(40) - 2 * b - b * b

    # Independent block identities inside the 50-vertex Moore graph.
    keep_positions = [full_labels.index(label) for label in labels]
    removed_positions = sorted(i for i, label in enumerate(full_labels) if label in deleted)
    a_full = adjacency_matrix(full)
    c = a_full.extract(keep_positions, removed_positions)
    p = a_full.extract(removed_positions, removed_positions)
    assert c.T * c == 4 * sp.eye(10)
    assert b * c == c * (sp.ones(10) - sp.eye(10) - p)
    expected_p = (X - 3) * (X - 1) ** 5 * (X + 2) ** 4
    assert sp.Poly(p.charpoly(X).as_expr() - expected_p, X).is_zero

    pivots = exact_ldl_positive(d + 6 * sp.eye(40))
    assert min(pivots) > 0

    print("40 vertices: PASS")
    print("  size=120, degree=6, girth=5, diameter=3")
    print("  chi_A=(x-6)(x-2)^18(x-1)^4(x+2)^5(x+3)^12")
    print("  chi_D=(x-75)(x-3)^5*x^16*(x+5)^18")
    print("  delta*=6, lambda_min(D)=-5, gap=1")
    return graph, labels, b, d


def verify_42(full: Graph, full_labels: tuple[Vertex, ...]) -> None:
    root = full_labels.index(("P", 0, 0))
    deleted_positions = {root} | set(full[root])
    deleted = {full_labels[i] for i in deleted_positions}
    graph, _ = induced(full, full_labels, deleted)
    degrees, b, d = basic_checks(graph)

    assert len(graph) == 42
    assert sum(degrees) // 2 == 126
    assert set(degrees) == {6}
    assert girth(graph) == 5
    assert max(max(row) for row in d.tolist()) == 3
    assert set(dual_degrees(graph)) == {Fraction(6)}

    expected_b = (X - 6) * (X - 2) ** 21 * (X + 1) ** 6 * (X + 3) ** 14
    expected_d = (X - 81) * (X - 4) ** 6 * X**14 * (X + 5) ** 21
    assert sp.Poly(b.charpoly(X).as_expr() - expected_b, X).is_zero
    assert sp.Poly(d.charpoly(X).as_expr() - expected_d, X).is_zero
    assert d == 3 * sp.ones(42) + 3 * sp.eye(42) - 2 * b - b * b

    pivots = exact_ldl_positive(d + 6 * sp.eye(42))
    assert min(pivots) > 0

    print("42 vertices: PASS")
    print("  size=126, degree=6, girth=5, diameter=3")
    print("  chi_A=(x-6)(x-2)^21(x+1)^6(x+3)^14")
    print("  chi_D=(x-81)(x-4)^6*x^14*(x+5)^21")
    print("  delta*=6, lambda_min(D)=-5, gap=1")


def verify_39(graph40: Graph, labels40: tuple[Vertex, ...]) -> None:
    graph, _ = induced(graph40, labels40, {("P", 1, 0)})
    degrees, _, d = basic_checks(graph)
    duals = dual_degrees(graph)

    assert len(graph) == 39
    assert sum(degrees) // 2 == 114
    assert Counter(degrees) == Counter({6: 33, 5: 6})
    assert girth(graph) == 5
    assert max(max(row) for row in d.tolist()) == 3
    assert min(duals) == Fraction(35, 6)

    expected_d = (
        X**9
        * (X + 5) ** 12
        * (X**2 + 6 * X + 3)
        * (X**3 + 3 * X**2 - 15 * X - 7) ** 2
        * (X**3 + 3 * X**2 - 15 * X - 3) ** 2
        * (X**4 - 78 * X**3 + 303 * X**2 - 70 * X - 450)
    )
    assert sp.Poly(d.charpoly(X).as_expr() - expected_d, X).is_zero
    pivots = exact_ldl_positive(6 * d + 35 * sp.eye(39))

    print("39 vertices: PASS")
    print("  size=114, degrees 6^33 and 5^6, girth=5, diameter=3")
    print("  delta*=35/6 and 6D+35I has 39 positive rational LDL pivots")
    print(f"  smallest pivot in this ordering: {min(pivots, key=lambda z: float(z))}")


def verify_38(graph40: Graph, labels40: tuple[Vertex, ...]) -> None:
    # P_(1,0) and P_(1,1) are adjacent in the 40-vertex graph.
    deleted = {("P", 1, 0), ("P", 1, 1)}
    graph, _ = induced(graph40, labels40, deleted)
    degrees, _, d = basic_checks(graph)
    duals = dual_degrees(graph)

    assert len(graph) == 38
    assert sum(degrees) // 2 == 109
    assert Counter(degrees) == Counter({6: 28, 5: 10})
    assert girth(graph) == 5
    assert max(max(row) for row in d.tolist()) == 3
    assert min(duals) == Fraction(17, 3)

    expected_d = (
        X**4
        * (X - 2)
        * (X + 5) ** 8
        * (X**2 + 6 * X + 2) ** 2
        * (X**3 + 3 * X**2 - 15 * X - 3)
        * (X**4 + 5 * X**3 - 7 * X**2 - 23 * X - 6)
        * (X**5 + 9 * X**4 + 7 * X**3 - 77 * X**2 - 54 * X - 4)
        * (
            X**9
            - 67 * X**8
            - 404 * X**7
            + 1772 * X**6
            + 7205 * X**5
            - 18489 * X**4
            - 17018 * X**3
            + 20288 * X**2
            + 16824 * X
            + 1680
        )
    )
    characteristic = sp.Poly(d.charpoly(X).as_expr(), X)
    assert sp.Poly(characteristic.as_expr() - expected_d, X).is_zero

    # The factor x^2+6x+2 gives the candidate least root -3-sqrt(7).
    # Exact Sturm counting shows that it is the unique distinct root below -28/5.
    assert characteristic.count_roots(-sp.oo, sp.Rational(-28, 5)) == 1
    assert sp.Rational(7) > sp.Rational(13, 5) ** 2  # sqrt(7) > 13/5
    # Hence -3-sqrt(7) < -28/5 and no other root is smaller.

    # Independent rational positive-definiteness certificate for the strict sign.
    pivots = exact_ldl_positive(3 * d + 17 * sp.eye(38))
    smallest_pivot = min(pivots, key=lambda z: float(z))
    assert sp.Rational(8, 3) ** 2 > 7  # 17/3 > 3+sqrt(7)

    print("38 vertices: PASS")
    print("  delete P_(1,0), P_(1,1) from the 40-vertex graph")
    print("  size=109, degrees 6^28 and 5^10, girth=5, diameter=3")
    print("  delta*=17/3")
    print("  lambda_min(D)=-3-sqrt(7), certified by factorization and Sturm count")
    print("  exact gap=8/3-sqrt(7)>0 because 64>63")
    print(f"  3D+17I: 38 positive rational LDL pivots; smallest={smallest_pivot}")


def verify_pair_counts(graph: Graph) -> None:
    # A direct adversarial check for hidden triangles and 4-cycles.
    for u, v in combinations(range(len(graph)), 2):
        common = len(graph[u] & graph[v])
        if v in graph[u]:
            assert common == 0
        else:
            assert common <= 1


def main() -> None:
    full, labels = hoffman_singleton()
    degrees, a_full, _ = basic_checks(full)
    assert len(full) == 50
    assert sum(degrees) // 2 == 175
    assert set(degrees) == {7}
    verify_pair_counts(full)
    assert a_full * a_full == 6 * sp.eye(50) - a_full + sp.ones(50)

    graph40, labels40, _, _ = verify_40(full, labels)
    verify_pair_counts(graph40)
    verify_42(full, labels)
    verify_39(graph40, labels40)
    verify_38(graph40, labels40)

    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
