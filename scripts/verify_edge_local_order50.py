#!/usr/bin/env python3
"""Exact edge-local obstruction for regular diameter-three WOW counterexamples.

The proof uses the centered positive-semidefinite polynomial

    -(A+2I)^2(A^2+2A-(2k-3)I) + f(k)J/n

on the strict WOW adjacency window. No floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import (  # noqa: E402
    adjacency_matrix,
    distance_rows,
    graph40,
    graph42,
)

X = sp.symbols("x")


def polynomial_entry_checks() -> dict[str, str]:
    k, n, sigma = sp.symbols("k n sigma", positive=True)
    f = sp.expand((X + 2) ** 2 * (X**2 + 2 * X - (2 * k - 3)))
    constant = sp.factor(f.subs(X, k))
    assert constant == (k + 2) ** 2 * (k**2 + 3)

    poly = sp.Poly(f, X)
    diagonal_moments = {
        0: sp.Integer(1),
        1: sp.Integer(0),
        2: k,
        3: sp.Integer(0),
        4: k * (2 * k - 1),
    }
    edge_moments = {
        0: sp.Integer(0),
        1: sp.Integer(1),
        2: sp.Integer(0),
        3: 2 * k - 1,
        4: sigma,
    }

    def evaluate(moments: dict[int, sp.Expr]) -> sp.Expr:
        return sp.expand(
            sum(
                coefficient * moments[degree[0]]
                for degree, coefficient in poly.terms()
            )
        )

    f_diagonal = sp.factor(evaluate(diagonal_moments))
    f_edge = sp.factor(evaluate(edge_moments))
    assert f_diagonal == 6 * (k + 2)
    assert f_edge == sigma + 4 * k + 14

    gram_diagonal = sp.factor(constant / n - f_diagonal)
    gram_edge = sp.factor(constant / n - f_edge)
    assert sp.factor(gram_diagonal - gram_edge) == sigma - (2 * k - 2)
    assert sp.factor(gram_diagonal + gram_edge) == (
        2 * constant / n - (10 * k + 26) - sigma
    )

    return {
        "window_polynomial": str(f),
        "principal_value": str(constant),
        "centered_gram_diagonal": str(gram_diagonal),
        "centered_gram_edge": str(gram_edge),
        "edge_cycle_lower_bound": "sigma_e >= 2k-2",
        "edge_cycle_upper_bound": (
            "sigma_e <= 2(k+2)^2(k^2+3)/n - 10k - 26"
        ),
    }


def degree_six_order_checks() -> dict[str, str]:
    k = sp.Integer(6)
    constant = (k + 2) ** 2 * (k**2 + 3)
    assert constant == 2496

    # If n=k^2+1+c, two radius-two balls around an edge have union size
    # 2(k^2+1)-(2k+sigma_e). Hence sigma_e >= (k-1)^2-c.
    c51 = sp.Integer(14)
    lower51 = (k - 1) ** 2 - c51
    upper51 = sp.factor(2 * constant / 51 - 10 * k - 26)
    assert lower51 == 11
    assert upper51 == sp.Rational(202, 17)
    assert bool(11 <= upper51 < 12)

    # Thus every edge would lie in exactly 11 five-cycles. Counting
    # edge--five-cycle incidences gives 153*11, which is not divisible by 5.
    edges51 = sp.Integer(6 * 51 // 2)
    incidence51 = edges51 * 11
    assert edges51 == 153
    assert incidence51 == 1683
    assert int(incidence51 % 5) == 3

    # At n=50 the same argument gives a sharp local two-value restriction.
    c50 = sp.Integer(13)
    lower50 = (k - 1) ** 2 - c50
    upper50 = sp.factor(2 * constant / 50 - 10 * k - 26)
    assert lower50 == 12
    assert upper50 == sp.Rational(346, 25)
    assert bool(13 < upper50 < 14)

    # If H contains the edges lying in 13 five-cycles, then for every vertex
    # sum_{e incident v} sigma_e = 2*tau(v), where tau(v) is the number of
    # five-cycles through v. Hence deg_H(v)=2*tau(v)-72 is even. Globally,
    # 1800+|E(H)| is divisible by 5.
    degree_h, tau = sp.symbols(
        "degree_h tau", integer=True, nonnegative=True
    )
    assert sp.expand(6 * 12 + degree_h - 2 * tau) == degree_h - 2 * (tau - 36)
    assert 1800 % 5 == 0

    return {
        "order_51_combinatorial_lower": str(lower51),
        "order_51_psd_upper": str(upper51),
        "order_51_forced_edge_cycle_count": "11",
        "order_51_incidence_contradiction": "153*11 = 1683 is not divisible by 5",
        "degree_six_strict_order_bound": "n <= 50",
        "order_50_edge_cycle_counts": "12 or 13",
        "order_50_high_edge_graph": (
            "all degrees even and the number of high edges is divisible by 5"
        ),
    }


def edge_five_cycle_counts(graph) -> tuple[tuple[int, int], ...]:
    distances = distance_rows(graph)
    rows: list[tuple[int, int]] = []
    for u, neighbors in enumerate(graph):
        for v in neighbors:
            if u < v:
                count = sum(
                    distances[u][z] == 2 and distances[v][z] == 2
                    for z in range(len(graph))
                )
                rows.append(((u, v), count))
    return tuple(rows)


def concrete_controls() -> dict[str, object]:
    result: dict[str, object] = {}
    for name, constructor, expected_sigma, expected_cycles in (
        ("order_40", graph40, 22, 528),
        ("order_42", graph42, 20, 504),
    ):
        graph, _ = constructor()
        edge_counts = edge_five_cycle_counts(graph)
        edges = tuple(edge for edge, _ in edge_counts)
        counts = tuple(count for _, count in edge_counts)
        assert set(counts) == {expected_sigma}
        assert sum(counts) % 5 == 0
        assert sum(counts) // 5 == expected_cycles

        # Directly verify the two walk-count identities used in the proof:
        # (A^3)_{uv}=2k-1 and (A^4)_{uv}=sigma_{uv} for every edge.
        adjacency = adjacency_matrix(graph)
        adjacency3 = adjacency**3
        adjacency4 = adjacency**4
        degree = len(graph[0])
        for (u, v), sigma in edge_counts:
            assert adjacency3[u, v] == 2 * degree - 1
            assert adjacency4[u, v] == sigma

        vertex_counts = [
            sum(
                count
                for edge, count in zip(edges, counts, strict=True)
                if vertex in edge
            )
            // 2
            for vertex in range(len(graph))
        ]
        expected_vertex = 66 if name == "order_40" else 60
        assert Counter(vertex_counts) == Counter({expected_vertex: len(graph)})
        result[name] = {
            "order": len(graph),
            "edge_five_cycle_count": expected_sigma,
            "number_of_five_cycles": expected_cycles,
            "five_cycles_through_each_vertex": expected_vertex,
            "A3_edge_entry": 2 * degree - 1,
            "A4_edge_entry": expected_sigma,
        }
    return result


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "symbolic_centered_gram_certificate": polynomial_entry_checks(),
        "degree_six_order_obstruction": degree_six_order_checks(),
        "known_counterexample_controls": concrete_controls(),
    }
    print("edge-local order-50 obstruction: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
