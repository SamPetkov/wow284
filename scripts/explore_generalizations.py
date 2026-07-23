#!/usr/bin/env python3
"""Reproducible exploration of additional WOW-284 mechanisms.

Exact parts:
  * balanced coordinate-layer deletions for m=0,...,4 (one representative);
  * the Odd graph O_4 = KG(7,3);
  * the Heawood graph;
  * exact regular diameter-three distance-polynomial identities.

Exploratory part:
  * all 9,880 three-vertex deletions of the fixed 40-vertex cage are screened
    with NumPy eigenvalues.  This is explicitly not an exact nonexistence proof.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

import networkx as nx
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from verify_wow284_38_40_42 import (  # noqa: E402
    adjacency_matrix,
    bfs_distances,
    dual_degrees,
    girth,
    hoffman_singleton,
    induced,
)

X = sp.symbols("x")


def exact_balanced_layer_chain() -> None:
    full, labels = hoffman_singleton()
    expected = {
        0: (50, 7, 2, 3),
        1: (40, 6, 3, 1),
        2: (30, 5, 3, -1),
        3: (20, 4, 3, -3),
        4: (10, 3, 2, 0),
    }
    print("BALANCED LAYER-DELETION CHAIN (exact representatives)")
    for m in range(5):
        deleted = {
            *(('P', i, j) for i in range(m) for j in range(5)),
            *(('Q', k, ell) for k in range(m) for ell in range(5)),
        }
        graph, _ = induced(full, labels, deleted)
        distances = sp.Matrix(bfs_distances(graph))
        degree = next(iter({len(row) for row in graph}))
        delta = min(dual_degrees(graph))
        n, k, diameter, gap = expected[m]
        assert len(graph) == n and degree == k and delta == k
        assert girth(graph) == 5
        assert max(max(row) for row in distances.tolist()) == diameter
        charpoly = sp.Poly(distances.charpoly(X).as_expr(), X)
        # Exact lower endpoint and multiplicity known from the exact factors.
        least, multiplicity = {
            0: (-4, 28),
            1: (-5, 18),
            2: (-6, 8),
            3: (-7, 2),
            4: (-3, 5),
        }[m]
        factor = sp.Poly((X - least) ** multiplicity, X)
        quotient, remainder = sp.div(charpoly, factor)
        assert remainder.is_zero
        # The quotient has no root at or below the displayed candidate.
        assert quotient.count_roots(-sp.oo, sp.Rational(least)) == 0
        assert k + least == gap
        print(f"  m={m}: n={n}, k={k}, diameter={diameter}, lambda_min={least}, Phi={gap}")


def nx_distance_matrix(graph: nx.Graph) -> sp.Matrix:
    nodes = list(graph.nodes())
    return sp.Matrix(
        [[nx.shortest_path_length(graph, u, v) for v in nodes] for u in nodes]
    )


def exact_named_negative_checks() -> None:
    odd4 = nx.convert_node_labels_to_integers(nx.kneser_graph(7, 3), ordering="sorted")
    assert odd4.number_of_nodes() == 35
    assert set(dict(odd4.degree()).values()) == {4}
    assert nx.diameter(odd4) == 3
    d_odd = nx_distance_matrix(odd4)
    expected_odd = (X - 82) * (X - 2) ** 14 * (X + 2) ** 6 * (X + 7) ** 14
    assert sp.Poly(d_odd.charpoly(X).as_expr() - expected_odd, X).is_zero

    heawood = nx.convert_node_labels_to_integers(nx.heawood_graph())
    assert set(dict(heawood.degree()).values()) == {3}
    assert nx.diameter(heawood) == 3
    d_heawood = nx_distance_matrix(heawood)
    expected_heawood = (X - 27) * (X + 3) * (X**2 + 4 * X - 4) ** 6
    assert sp.Poly(d_heawood.charpoly(X).as_expr() - expected_heawood, X).is_zero

    print("STANDARD-FAMILY NEGATIVE CHECKS (exact)")
    print("  Odd graph O_4=KG(7,3): delta*=4, lambda_min=-7, so not a counterexample")
    print("  Heawood graph: delta*=3, lambda_min=-2-2*sqrt(2), so not a counterexample")
    print("  Connected regular bipartite diameter-three graphs are excluded in general")
    print("  because adjacency eigenvalue -k maps to k-2-(k-1)^2.")


def cage40():
    full, labels = hoffman_singleton()
    deleted = {("P", 0, j) for j in range(5)} | {("Q", 0, j) for j in range(5)}
    return induced(full, labels, deleted)[0]


def delete_indices(graph, deleted: set[int]):
    keep = [v for v in range(len(graph)) if v not in deleted]
    index = {old: new for new, old in enumerate(keep)}
    return tuple(
        frozenset(index[w] for w in graph[v] if w in index)
        for v in keep
    )


def numerical_three_vertex_screen() -> None:
    graph = cage40()
    best_score = -float("inf")
    best_deleted: tuple[int, int, int] | None = None
    checked = 0
    for deleted in combinations(range(40), 3):
        descendant = delete_indices(graph, set(deleted))
        try:
            distance_rows = bfs_distances(descendant)
        except AssertionError:
            continue
        delta = float(min(dual_degrees(descendant)))
        least = float(np.linalg.eigvalsh(np.asarray(distance_rows, dtype=float))[0])
        score = delta + least
        checked += 1
        if score > best_score:
            best_score = score
            best_deleted = deleted

    assert checked == 9880
    print("THREE-VERTEX DELETION SCREEN (floating-point exploration only)")
    print(f"  checked={checked}; best numerical Phi={best_score:.12f}; deleted={best_deleted}")
    print("  no positive candidate appeared, but this is not an exact theorem or a minimality proof")


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    exact_balanced_layer_chain()
    exact_named_negative_checks()
    numerical_three_vertex_screen()


if __name__ == "__main__":
    main()
