from __future__ import annotations

from fractions import Fraction

import sympy as sp

from wow284_induced40 import (
    VERTEX_COUNT_40,
    adjacency_matrix_40,
    all_pairs_distances_40,
    dual_degrees_40,
    girth_40,
    induced_adjacency,
    structural_certificate_40,
)


def test_induced_40_structure() -> None:
    graph, labels = induced_adjacency()
    distances = all_pairs_distances_40(graph)
    assert VERTEX_COUNT_40 == 40
    assert len(labels) == 40
    assert sum(map(len, graph)) // 2 == 120
    assert set(map(len, graph)) == {6}
    assert max(map(max, distances)) == 3
    assert {tuple(row.count(i) for i in range(4)) for row in distances} == {
        (1, 6, 30, 3)
    }
    assert girth_40(graph) == 5
    assert set(dual_degrees_40(graph)) == {Fraction(6)}


def test_induced_40_exact_spectra() -> None:
    a = sp.Matrix(adjacency_matrix_40())
    d = sp.Matrix(all_pairs_distances_40())
    x = sp.symbols("x")
    expected_a = (
        (x - 6)
        * (x - 2) ** 18
        * (x - 1) ** 4
        * (x + 2) ** 5
        * (x + 3) ** 12
    )
    expected_d = (x - 75) * (x - 3) ** 5 * x**16 * (x + 5) ** 18
    assert d == 3 * sp.ones(40) + 3 * sp.eye(40) - 2 * a - a * a
    assert sp.expand(a.charpoly(x).as_expr() - expected_a) == 0
    assert sp.expand(d.charpoly(x).as_expr() - expected_d) == 0


def test_induced_40_structural_certificate() -> None:
    certificate = structural_certificate_40()
    assert certificate["order"] == 40
    assert certificate["size"] == 120
    assert certificate["diameter"] == 3
    assert certificate["girth"] == 5
    assert certificate["transmission"] == 75
    assert certificate["minimum_dual_degree"] == "6"
