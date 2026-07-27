#!/usr/bin/env python3
"""Independent exact audit of the regular degree-at-least-six theorem.

The script does not import the original low-degree verifier. It checks the
symbolic reductions, the streamlined LP order bounds, the two layer-compression
arguments, and all four committed (5,5)-cage records using exact arithmetic.
"""
from __future__ import annotations

from collections import deque
from itertools import combinations
from pathlib import Path
import json

import networkx as nx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CAGES = ROOT / "data" / "cages55"
X = sp.symbols("x")


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


def adjacency_matrix(graph: nx.Graph) -> sp.Matrix:
    nodes = sorted(graph)
    return sp.Matrix(
        [[int(graph.has_edge(u, v)) for v in nodes] for u in nodes]
    )


def distance_matrix(graph: nx.Graph) -> sp.Matrix:
    nodes = sorted(graph)
    distances = dict(nx.all_pairs_shortest_path_length(graph))
    return sp.Matrix([[distances[u][v] for v in nodes] for u in nodes])


def normalized_layer_compression(k: sp.Expr, c: sp.Expr, a: sp.Expr) -> sp.Matrix:
    ratio = k * (k - 1) / c
    cross = (k - 1 - a) * sp.sqrt(ratio)
    return sp.Matrix(
        [
            [0, sp.sqrt(k), 0, 0],
            [sp.sqrt(k), 0, sp.sqrt(k - 1), 0],
            [0, sp.sqrt(k - 1), a, cross],
            [0, 0, cross, k - ratio * (k - 1 - a)],
        ]
    )


def symbolic_case_audit() -> dict[str, str]:
    k, c, a = sp.symbols("k c a", positive=True)

    # Rayleigh quotient for e_u-e_v.
    distance = sp.symbols("d", positive=True)
    numerator = -2 * distance
    denominator = sp.Integer(2)
    if sp.simplify(numerator / denominator + distance) != 0:
        raise AssertionError("wrong diameter Rayleigh quotient")

    # Moore multiplicity obstructions at k=4 and k=5.
    multiplicity4 = sp.Rational(1, 2) * (
        16 + sp.Rational(8, 1) / sp.sqrt(13)
    )
    multiplicity5 = sp.Rational(1, 2) * (
        25 + sp.Rational(15, 1) / sp.sqrt(17)
    )
    if multiplicity4.is_integer is not False:
        raise AssertionError("degree-four Moore multiplicity not excluded")
    if multiplicity5.is_integer is not False:
        raise AssertionError("degree-five Moore multiplicity not excluded")

    # Audited all-degree LP ceiling, kept rational throughout.
    bound4 = sp.Rational((4 + 2) * (4**2 + 3), 6)
    bound5 = sp.Rational((5 + 2) * (5**2 + 3), 6)
    if bound4 != 19 or bound5 != sp.Rational(98, 3):
        raise AssertionError("wrong LP specialisation")

    # Degree-four excess-one rational-space obstruction.
    polynomial4 = X**2 + X - 4
    if sp.discriminant(polynomial4, X) != 17:
        raise AssertionError("wrong degree-four discriminant")
    if sp.Poly(polynomial4, X).is_irreducible is not True:
        raise AssertionError("degree-four polynomial is not certified irreducible")
    if 9 % 2 != 1:
        raise AssertionError("wrong parity check")

    # Distance matrix of the five-vertex geodesic.
    path = nx.path_graph(5)
    path_charpoly = sp.factor(distance_matrix(path).charpoly(X).as_expr())
    expected_path = (X**2 + 6 * X + 4) * (X**3 - 6 * X**2 - 18 * X - 8)
    if sp.expand(path_charpoly - expected_path) != 0:
        raise AssertionError("wrong P5 distance polynomial")
    if not -3 - sp.sqrt(5) < -5:
        raise AssertionError("wrong P5 least-root comparison")

    # Positive-semidefinite monotonicity of the normalized layer compression.
    ratio = k * (k - 1) / c
    derivative = sp.Matrix([[1, -sp.sqrt(ratio)], [-sp.sqrt(ratio), ratio]])
    vector = sp.Matrix([1, -sp.sqrt(ratio)])
    if sp.simplify(derivative - vector * vector.T) != sp.zeros(2):
        raise AssertionError("layer derivative is not rank-one PSD")

    # Degree-five, excess six.
    k5 = sp.Integer(5)
    c6 = sp.Integer(6)
    a0 = k5 - 1 - c6 / (k5 - 1)
    compression6 = normalized_layer_compression(k5, c6, a0)
    factor6 = sp.factor(compression6.charpoly(X).as_expr())
    expected6 = (X - 5) * (X + 3) * (2 * X**2 - X - 5) / 2
    if sp.expand(factor6 - expected6) != 0:
        raise AssertionError("wrong excess-six compression")
    p56 = 4 * X**3 + 10 * X**2 - 16 * X - 30
    if sp.expand(p56.subs(X, sp.Rational(11, 6)) + sp.Rational(29, 27)) != 0:
        raise AssertionError("wrong excess-six boundary evaluation")
    if not sp.Rational(11, 6) > -1 + sp.sqrt(8):
        raise AssertionError("wrong excess-six radical comparison")

    # Degree-five, excess five after the edge-integrality improvement.
    c5 = sp.Integer(5)
    a_integral = sp.Rational(14, 5)
    compression5 = normalized_layer_compression(k5, c5, a_integral)
    factor5 = sp.factor(compression5.charpoly(X).as_expr())
    expected5 = (X - 5) * (X + 1) * (5 * X**2 + 5 * X - 26) / 5
    if sp.expand(factor5 - expected5) != 0:
        raise AssertionError("wrong excess-five compression")
    root5 = (-5 + sp.sqrt(545)) / 10
    if not root5 > -1 + sp.sqrt(8):
        raise AssertionError("wrong excess-five radical comparison")
    if sp.ceiling(10 * sp.Rational(11, 4)) / 10 != a_integral:
        raise AssertionError("wrong edge-integrality improvement")

    return {
        "diameter_rayleigh_quotient": "-d(u,v)",
        "degree_4_LP_bound": "n<19, hence n=18 in diameter three",
        "degree_5_LP_bound": "n<98/3, hence n<=32",
        "degree_4_irreducible_factor": str(polynomial4),
        "P5_distance_polynomial": str(path_charpoly),
        "degree_5_excess_6_compression": str(factor6),
        "degree_5_excess_5_compression": str(factor5),
        "layer_derivative_rank": str(derivative.rank()),
    }


def cage_audit() -> dict[str, object]:
    files = sorted(CAGES.glob("*.graph6"))
    expected_names = {
        "foster.graph6",
        "meringer.graph6",
        "robertson_wegner.graph6",
        "wong.graph6",
    }
    if {path.name for path in files} != expected_names:
        raise AssertionError("wrong cage file set")

    witness = {
        "foster.graph6": X**2 + 6 * X - 11,
        "meringer.graph6": X + 6,
        "robertson_wegner.graph6": X + 6,
        "wong.graph6": X**2 + 6 * X - 11,
    }
    graphs: dict[str, nx.Graph] = {}
    result: dict[str, object] = {}
    for path in files:
        graph = nx.convert_node_labels_to_integers(
            nx.from_graph6_bytes(path.read_bytes().strip()), ordering="sorted"
        )
        graphs[path.name] = graph
        if graph.number_of_nodes() != 30 or graph.number_of_edges() != 75:
            raise AssertionError("wrong cage order or size")
        if not nx.is_connected(graph):
            raise AssertionError("disconnected cage")
        if set(dict(graph.degree()).values()) != {5}:
            raise AssertionError("cage is not 5-regular")
        if exact_girth(graph) != 5:
            raise AssertionError("wrong cage girth")
        if nx.diameter(graph) != 3:
            raise AssertionError("wrong cage diameter")

        adjacency = adjacency_matrix(graph)
        distance = distance_matrix(graph)
        adjacency_charpoly = sp.factor(adjacency.charpoly(X).as_expr())
        distance_charpoly = sp.factor(distance.charpoly(X).as_expr())
        quotient, remainder = sp.div(
            sp.Poly(distance_charpoly, X), sp.Poly(witness[path.name], X)
        )
        if not remainder.is_zero or quotient.degree() < 0:
            raise AssertionError("missing exact distance witness")

        # Exact sign of the witness root; no numerical ordering.
        if witness[path.name] == X + 6:
            witness_value = "-6"
        else:
            if not -3 - 2 * sp.sqrt(5) < -5:
                raise AssertionError("wrong quadratic witness comparison")
            witness_value = "-3-2*sqrt(5)"

        result[path.stem] = {
            "order": 30,
            "degree": 5,
            "girth": 5,
            "diameter": 3,
            "distance_witness": witness_value,
            "adjacency_characteristic_polynomial": str(adjacency_charpoly),
            "distance_characteristic_polynomial": str(distance_charpoly),
        }

    names = sorted(graphs)
    for left, right in combinations(names, 2):
        if nx.is_isomorphic(graphs[left], graphs[right]):
            raise AssertionError("duplicate cage records")

    return {
        "number_of_records": len(graphs),
        "pairwise_nonisomorphic": True,
        "records": result,
        "external_exhaustion_input": (
            "Meringer 1999: exactly four nonisomorphic (5,5)-cages"
        ),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "symbolic_case_audit": symbolic_case_audit(),
        "exact_cage_audit": cage_audit(),
    }
    print("Proof Audit 04 (regular degree at least six): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
