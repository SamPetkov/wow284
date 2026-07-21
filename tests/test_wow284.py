from __future__ import annotations

from fractions import Fraction

import sympy as sp

from wow284_graph import (
    VERTEX_COUNT,
    adjacency_list,
    adjacency_matrix,
    all_pairs_distances,
    build_edges,
    dual_degrees,
    girth,
    structural_certificate,
)


def test_order_size_regularity_and_simplicity() -> None:
    edges = build_edges()
    graph = adjacency_list(edges)
    assert VERTEX_COUNT == 50
    assert len(edges) == 175
    assert len(set(edges)) == 175
    assert all(u < v for u, v in edges)
    assert all(len(neighbors) == 7 for neighbors in graph)


def test_common_neighbor_certificate() -> None:
    graph = adjacency_list()
    for u in range(VERTEX_COUNT):
        for v in range(u + 1, VERTEX_COUNT):
            expected = 0 if v in graph[u] else 1
            assert len(graph[u] & graph[v]) == expected


def test_distances_girth_and_dual_degree() -> None:
    graph = adjacency_list()
    distances = all_pairs_distances(graph)
    assert max(max(row) for row in distances) == 2
    assert girth(graph) == 5
    assert set(dual_degrees(graph)) == {Fraction(7, 1)}


def test_structural_certificate() -> None:
    certificate = structural_certificate()
    assert certificate["order"] == 50
    assert certificate["size"] == 175
    assert certificate["adjacent_pair_count"] == 175
    assert certificate["nonadjacent_pair_count"] == 1050
    assert certificate["diameter"] == 2
    assert certificate["girth"] == 5


def test_matrix_identities_and_characteristic_polynomials() -> None:
    a = sp.Matrix(adjacency_matrix())
    d = sp.Matrix(all_pairs_distances())
    identity = sp.eye(VERTEX_COUNT)
    ones = sp.ones(VERTEX_COUNT)
    x = sp.symbols("x")

    assert a * a == 6 * identity - a + ones
    assert d == 2 * ones - 2 * identity - a
    assert d == -14 * identity + a + 2 * a * a
    assert sp.expand(a.charpoly(x).as_expr() - (x - 7) * (x - 2) ** 28 * (x + 3) ** 21) == 0
    assert sp.expand(d.charpoly(x).as_expr() - (x - 91) * (x - 1) ** 21 * (x + 4) ** 28) == 0


def test_exact_positive_definiteness_certificate() -> None:
    d = sp.Matrix(all_pairs_distances())
    shifted = d + 7 * sp.eye(VERTEX_COUNT)
    lower, diagonal = shifted.LDLdecomposition(hermitian=True)
    pivots = [diagonal[i, i] for i in range(VERTEX_COUNT)]
    assert lower * diagonal * lower.T == shifted
    assert len(pivots) == 50
    assert all(bool(pivot > 0) for pivot in pivots)
