#!/usr/bin/env python3
"""Second independent exact audit of the 38-vertex WOW-284 graph.

This pass starts only from graph6, uses NetworkX integer BFS for distances,
and uses a handwritten Fraction-based LDL^T algorithm rather than SymPy's LDL
routine. SymPy is used only for the exact characteristic polynomial and Sturm
root count.
"""

from __future__ import annotations

from fractions import Fraction

import networkx as nx
import sympy as sp

GRAPH6 = (
    "egCGGc??G?_@?H????G?@??C?@HCP?AG_OAIaG@qGaBH?Q?HGA??c@@?HG?s_H?E_SA?"
    "@OGC?@OI??OGD??WA_O?E@@@??CCE???GKC??AKCC??EAAA??B?"
)


def fraction_ldl(matrix: list[list[int]]) -> tuple[list[list[Fraction]], list[Fraction]]:
    n = len(matrix)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    diagonal = [Fraction(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = Fraction(1)
        diagonal[i] = Fraction(matrix[i][i]) - sum(
            lower[i][k] * lower[i][k] * diagonal[k] for k in range(i)
        )
        if diagonal[i] == 0:
            raise AssertionError(f"zero pivot at {i}")
        for j in range(i + 1, n):
            lower[j][i] = (
                Fraction(matrix[j][i])
                - sum(lower[j][k] * lower[i][k] * diagonal[k] for k in range(i))
            ) / diagonal[i]
    return lower, diagonal


def main() -> None:
    if not __debug__:
        raise RuntimeError("exact verification must not be run with python -O")

    graph = nx.from_graph6_bytes(GRAPH6.encode("ascii"))
    assert graph.number_of_nodes() == 38
    assert graph.number_of_edges() == 109
    assert nx.is_connected(graph)
    assert sorted(dict(graph.degree()).values()).count(5) == 10
    assert sorted(dict(graph.degree()).values()).count(6) == 28

    # Exact integer distances, reconstructed independently from graph6.
    distances = [[0 for _ in range(38)] for _ in range(38)]
    for source, lengths in nx.all_pairs_shortest_path_length(graph):
        assert len(lengths) == 38
        for target, distance in lengths.items():
            distances[source][target] = distance
    assert max(map(max, distances)) == 3
    assert min(map(len, nx.minimum_cycle_basis(graph))) == 5

    degrees = dict(graph.degree())
    duals = []
    for v in range(38):
        duals.append(
            Fraction(sum(degrees[u] for u in graph.neighbors(v)), degrees[v])
        )
    assert min(duals) == Fraction(17, 3)

    x = sp.symbols("x")
    distance_matrix = sp.Matrix(distances)
    characteristic = sp.Poly(distance_matrix.charpoly(x).as_expr(), x)
    assert sp.rem(characteristic, sp.Poly(x**2 + 6*x + 2, x)).is_zero
    assert characteristic.sqf_part().count_roots(
        -sp.oo, sp.Rational(-28, 5)
    ) == 1
    assert sp.Rational(13, 5) ** 2 < 7

    shifted = (3 * distance_matrix + 17 * sp.eye(38)).tolist()
    shifted_int = [[int(value) for value in row] for row in shifted]
    lower, pivots = fraction_ldl(shifted_int)
    assert all(pivot > 0 for pivot in pivots)

    # Full exact reconstruction check.
    for i in range(38):
        for j in range(38):
            reconstructed = sum(
                lower[i][k] * pivots[k] * lower[j][k]
                for k in range(min(i, j) + 1)
            )
            assert reconstructed == shifted_int[i][j]

    print("independent graph6 audit: PASS")
    print("order=38 size=109 degrees=5^10,6^28 girth=5 diameter=3")
    print("delta*=17/3; lambda_min=-3-sqrt(7)")
    print("3D+17I: 38 positive exact Fraction pivots")
    print(f"smallest pivot={min(pivots, key=float)}")


if __name__ == "__main__":
    main()
