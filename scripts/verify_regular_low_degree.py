#!/usr/bin/env python3
"""Exact closure of the regular degree-at-most-five cases for WOW-284.

The four graph6 records are fixed labelled reconstructions of the four
(5,5)-cages. Every asserted spectral conclusion is checked over the integers
or exact algebraic numbers; floating point is not used for a theorem.
"""
from __future__ import annotations

from collections import deque
from pathlib import Path
import json

import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cages55"
X = sp.symbols("x")

EXPECTED = {
    "foster": {
        "house_id": 48173,
        "automorphisms": 30,
        "first_ten": [
            [2, 3, 4, 5, 6],
            [1, 14, 17, 18, 28],
            [1, 15, 21, 22, 27],
            [1, 11, 19, 23, 29],
            [1, 12, 20, 24, 30],
            [1, 13, 16, 25, 26],
            [19, 22, 25, 28, 30],
            [20, 21, 26, 28, 29],
            [18, 23, 26, 27, 30],
            [17, 24, 25, 27, 29],
        ],
        "chi_a": (X - 5)
        * (X - 2) ** 4
        * (X + 1)
        * (X**2 - 5) ** 2
        * (X**2 + 2 * X - 4) ** 2
        * (X**4 + 2 * X**3 - 6 * X**2 - 7 * X + 11) ** 4,
        "chi_d": (X - 57)
        * (X - 3)
        * (X + 2) ** 4
        * (X + 6) ** 4
        * (X**2 + 6 * X - 11) ** 2
        * (X**4 + 4 * X**3 - 4 * X**2 - 11 * X + 1) ** 4,
        "witness_factor": X**2 + 6 * X - 11,
        "witness_eigenvalue": "-3-2*sqrt(5)",
    },
    "meringer": {
        "house_id": 1227,
        "automorphisms": 96,
        "first_ten": [
            [2, 3, 4, 5, 6],
            [1, 15, 21, 24, 25],
            [1, 18, 23, 26, 30],
            [1, 17, 19, 22, 28],
            [1, 16, 20, 27, 29],
            [1, 11, 12, 13, 14],
            [8, 15, 23, 27, 28],
            [7, 19, 25, 29, 30],
            [10, 17, 20, 21, 26],
            [9, 16, 18, 22, 24],
        ],
        "chi_a": X
        * (X - 5)
        * (X - 2) ** 9
        * (X + 2) ** 3
        * (X + 3) ** 2
        * (X**2 + X - 4) ** 3
        * (X**2 + 2 * X - 2) ** 4,
        "chi_d": X**8
        * (X - 57)
        * (X - 2) ** 4
        * (X + 1) ** 2
        * (X + 6) ** 9
        * (X**2 + 3 * X - 2) ** 3,
        "witness_factor": X + 6,
        "witness_eigenvalue": "-6",
    },
    "robertson_wegner": {
        "house_id": 1290,
        "automorphisms": 20,
        "first_ten": [
            [2, 3, 4, 5, 6],
            [1, 11, 22, 23, 28],
            [1, 12, 17, 26, 30],
            [1, 13, 16, 27, 29],
            [1, 14, 19, 21, 24],
            [1, 15, 18, 20, 25],
            [16, 18, 21, 28, 30],
            [17, 19, 20, 28, 29],
            [10, 23, 24, 26, 29],
            [9, 22, 25, 27, 30],
        ],
        "chi_a": (X - 5)
        * (X - 2) ** 8
        * (X + 1)
        * (X + 3) ** 4
        * (X**4 + 2 * X**3 - 6 * X**2 - 7 * X + 11) ** 2
        * (X**4 + 2 * X**3 - 4 * X**2 - 5 * X + 5) ** 2,
        "chi_d": (X - 57)
        * (X - 3)
        * (X + 1) ** 4
        * (X + 6) ** 8
        * (X**4 - 8 * X**2 + 5 * X + 1) ** 2
        * (X**4 + 4 * X**3 - 4 * X**2 - 11 * X + 1) ** 2,
        "witness_factor": X + 6,
        "witness_eigenvalue": "-6",
    },
    "wong": {
        "house_id": 1433,
        "automorphisms": 120,
        "first_ten": [
            [2, 3, 4, 5, 6],
            [1, 11, 22, 23, 24],
            [1, 18, 28, 29, 30],
            [1, 14, 17, 19, 26],
            [1, 13, 16, 21, 25],
            [1, 12, 15, 20, 27],
            [11, 15, 16, 17, 18],
            [12, 19, 22, 25, 28],
            [13, 20, 24, 26, 30],
            [14, 21, 23, 27, 29],
        ],
        "chi_a": (X - 5)
        * (X - 1) ** 5
        * (X + 1) ** 2
        * (X**2 - 5) ** 3
        * (X**2 + X - 5) ** 8,
        "chi_d": (X - 57)
        * (X - 3) ** 2
        * (X + 1) ** 5
        * (X**2 + 5 * X + 1) ** 8
        * (X**2 + 6 * X - 11) ** 3,
        "witness_factor": X**2 + 6 * X - 11,
        "witness_eigenvalue": "-3-2*sqrt(5)",
    },
}


def load_graph(name: str) -> nx.Graph:
    raw = (DATA / f"{name}.graph6").read_bytes().strip()
    graph = nx.from_graph6_bytes(raw)
    return nx.convert_node_labels_to_integers(graph, ordering="sorted")


def exact_girth(graph: nx.Graph) -> int:
    best = graph.number_of_nodes() + 1
    for source in graph:
        dist = {source: 0}
        parent = {source: None}
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def distance_matrix(graph: nx.Graph) -> sp.Matrix:
    rows = dict(nx.all_pairs_shortest_path_length(graph))
    n = graph.number_of_nodes()
    return sp.Matrix([[rows[i][j] for j in range(n)] for i in range(n)])


def adjacency_matrix(graph: nx.Graph) -> sp.Matrix:
    n = graph.number_of_nodes()
    return sp.Matrix(
        [[int(graph.has_edge(i, j)) for j in range(n)] for i in range(n)]
    )


def verify_cages() -> dict[str, object]:
    graphs: dict[str, nx.Graph] = {}
    result: dict[str, object] = {}
    for name, expected in EXPECTED.items():
        graph = load_graph(name)
        graphs[name] = graph
        assert graph.number_of_nodes() == 30
        assert graph.number_of_edges() == 75
        assert nx.is_connected(graph)
        assert set(dict(graph.degree()).values()) == {5}
        assert exact_girth(graph) == 5
        assert nx.diameter(graph) == 3
        first_ten = [
            [v + 1 for v in sorted(graph.neighbors(u))] for u in range(10)
        ]
        assert first_ten == expected["first_ten"]

        a = adjacency_matrix(graph)
        d = distance_matrix(graph)
        chi_a = sp.factor(a.charpoly(X).as_expr())
        chi_d = sp.factor(d.charpoly(X).as_expr())
        assert sp.Poly(chi_a - expected["chi_a"], X).is_zero
        assert sp.Poly(chi_d - expected["chi_d"], X).is_zero
        quotient, remainder = sp.div(
            sp.Poly(chi_d, X), sp.Poly(expected["witness_factor"], X)
        )
        assert remainder.is_zero and quotient.degree() >= 0

        automorphisms = sum(
            1 for _ in GraphMatcher(graph, graph).isomorphisms_iter()
        )
        assert automorphisms == expected["automorphisms"]
        result[name] = {
            "house_of_graphs_id": expected["house_id"],
            "order": 30,
            "size": 75,
            "degree": 5,
            "girth": 5,
            "diameter": 3,
            "automorphism_group_order": automorphisms,
            "distance_eigenvalue_witness_at_most_minus_5": expected[
                "witness_eigenvalue"
            ],
            "adjacency_characteristic_polynomial": str(chi_a),
            "distance_characteristic_polynomial": str(chi_d),
        }

    names = list(graphs)
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            assert not nx.is_isomorphic(graphs[left], graphs[right])
    return result


def p_layer(k: sp.Expr, c: sp.Expr, z: sp.Expr) -> sp.Expr:
    return (
        (k - 1) * z**3
        + (c + k - 1) * z**2
        - (k - 1) ** 2 * z
        - c * k
    )


def verify_analytic_reduction() -> dict[str, str]:
    z, c = sp.symbols("z c")

    # A degree-4 diameter-two Moore graph would require irrational adjacency
    # multiplicities, hence cannot exist.
    delta4 = sp.sqrt(13)
    multiplicity4 = sp.Rational(1, 2) * (
        16 + sp.Rational(8, 1) / delta4
    )
    assert multiplicity4.is_rational is False

    # The fourth-moment bound gives n < 475/23, hence n <= 20 for k=4.
    bound4 = sp.Rational(25 * 19, 23)
    assert 20 < bound4 < 21
    p42 = sp.expand(p_layer(4, 2, sp.Rational(3, 2)))
    p43 = sp.expand(p_layer(4, 3, sp.Rational(3, 2)))
    assert p42 == -sp.Rational(1, 8)
    assert p43 == -sp.Rational(15, 8)
    assert sp.Rational(3, 2) > -1 + sp.sqrt(6)

    # For excess one, the forced quadratic x^2+x-4 is irreducible and would
    # have to act on a rational 9-dimensional space, impossible by conjugacy.
    assert sp.discriminant(z**2 + z - 4, z) == 17
    assert sp.sqrt(17).is_rational is False
    assert 9 % 2 == 1

    # A degree-5 diameter-two Moore graph is likewise impossible.
    delta5 = sp.sqrt(17)
    multiplicity5 = sp.Rational(1, 2) * (
        25 + sp.Rational(15, 1) / delta5
    )
    assert multiplicity5.is_rational is False

    # Diameter four is excluded by the distance matrix of a geodesic P5.
    path = nx.path_graph(5)
    path_poly = sp.factor(distance_matrix(path).charpoly(z).as_expr())
    assert path_poly == (z**2 + 6 * z + 4) * (
        z**3 - 6 * z**2 - 18 * z - 8
    )
    assert -3 - sp.sqrt(5) < -5

    # For diameter three the fourth-moment bound is the strict inequality n<36.
    bound5 = sp.Rational((5 + 1) ** 2 * (5**2 + 3), 5 * 5 + 3)
    assert bound5 == 36
    evaluation = sp.expand(p_layer(5, c, sp.Rational(11, 6)))
    assert evaluation == -(177 * c - 946) / 108
    for excess in range(6, 10):
        assert sp.expand(p_layer(5, excess, sp.Rational(11, 6))) < 0
    assert sp.Rational(11, 6) > -1 + sp.sqrt(8)

    # At excess five, integrality of the distance-two layer edge count improves
    # a >= 11/4 to a >= ceil(10*(11/4))/10 = 14/5.
    assert sp.ceiling(10 * sp.Rational(11, 4)) / 10 == sp.Rational(14, 5)
    k = sp.Integer(5)
    excess = sp.Integer(5)
    a = sp.Rational(14, 5)
    compression = sp.Matrix(
        [
            [0, sp.sqrt(k), 0, 0],
            [sp.sqrt(k), 0, sp.sqrt(k - 1), 0],
            [
                0,
                sp.sqrt(k - 1),
                a,
                (k - 1 - a) * sp.sqrt(k * (k - 1) / excess),
            ],
            [
                0,
                0,
                (k - 1 - a) * sp.sqrt(k * (k - 1) / excess),
                k - k * (k - 1) * (k - 1 - a) / excess,
            ],
        ]
    )
    compression_poly = sp.factor(compression.charpoly(z).as_expr())
    assert compression_poly == (
        (z - 5) * (z + 1) * (5 * z**2 + 5 * z - 26) / 5
    )
    root = (-5 + sp.sqrt(545)) / 10
    assert root > -1 + sp.sqrt(8)

    # The Moore score at degree three is exactly zero.
    assert sp.simplify(3 - (3 + sp.sqrt(4 * 3 - 3)) / 2) == 0

    return {
        "degree_4_moment_bound": "n < 475/23, hence n <= 20",
        "degree_4_layer_values": (
            f"p_4,2(3/2)={p42}; p_4,3(3/2)={p43}"
        ),
        "diameter_4_path_factor": str(path_poly),
        "degree_5_large_excess_evaluation": str(evaluation),
        "degree_5_excess_5_compression": str(compression_poly),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "four_5_5_cages": verify_cages(),
        "analytic_degree_at_most_five_reduction": verify_analytic_reduction(),
    }
    print("regular low-degree verification: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
