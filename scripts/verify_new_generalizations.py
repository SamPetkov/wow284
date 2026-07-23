#!/usr/bin/env python3
"""Exact checks for the additional WOW-284 generalizations.

This script does not use floating point for any asserted conclusion.  It checks
three punctures of the Hoffman--Singleton graph, a 35-vertex no-go candidate,
and the symbolic block determinants used in the generic Moore-graph theorem.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import (  # noqa: E402
    adjacency_matrix,
    distance_matrix,
    dual_degrees,
    girth,
    hoffman_singleton,
    induced,
)

X = sp.symbols("x")


def ldl_positive(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    lower, diagonal = matrix.LDLdecomposition(hermitian=True)
    assert lower * diagonal * lower.T == matrix
    pivots = tuple(sp.factor(diagonal[i, i]) for i in range(matrix.rows))
    assert all(bool(p > 0) for p in pivots)
    return pivots


def graph_summary(graph):
    degrees = tuple(map(len, graph))
    d = distance_matrix(graph)
    return {
        "order": len(graph),
        "size": sum(degrees) // 2,
        "degrees": dict(sorted(Counter(degrees).items())),
        "girth": girth(graph),
        "diameter": int(max(max(row) for row in d.tolist())),
        "minimum_dual_degree": str(min(dual_degrees(graph))),
    }, d


def verify_punctures() -> dict[str, object]:
    full, labels = hoffman_singleton()
    cases = {
        "one_vertex": {
            "deleted": {("P", 0, 0)},
            "expected_dual": Fraction(48, 7),
            "expected_charpoly":
                (X - 1) ** 14 * (X + 4) ** 21
                * (X**2 - 94 * X + 354)
                * (X**2 + 4 * X - 3) ** 6,
            "shift": (7, 48),
        },
        "edge_endpoints": {
            "deleted": {("P", 0, 0), ("P", 0, 1)},
            "expected_dual": Fraction(47, 7),
            "expected_charpoly":
                (X - 3) * (X - 1) ** 9 * (X + 4) ** 16
                * (X**2 - 92 * X + 303)
                * (X**2 + 4 * X - 3) ** 10,
            "shift": (7, 47),
        },
        "nonadjacent_pair": {
            "deleted": {("P", 0, 0), ("P", 0, 2)},
            "expected_dual": Fraction(47, 7),
            "expected_charpoly":
                (X - 4) * (X - 1) ** 8 * (X + 4) ** 15
                * (X**2 + 4 * X - 4) ** 5
                * (X**2 + 4 * X - 2) ** 5
                * (X**4 - 88 * X**3 - 125 * X**2 + 1740 * X - 778),
            "shift": (7, 47),
        },
    }

    result: dict[str, object] = {}
    for name, data in cases.items():
        graph, _ = induced(full, labels, data["deleted"])
        summary, d = graph_summary(graph)
        assert summary["girth"] >= 5
        assert summary["diameter"] == 3
        assert min(dual_degrees(graph)) == data["expected_dual"]
        charpoly = sp.factor(d.charpoly(X).as_expr())
        assert sp.Poly(charpoly - data["expected_charpoly"], X).is_zero
        q, p = data["shift"]
        pivots = ldl_positive(q * d + p * sp.eye(len(graph)))
        summary.update({
            "distance_characteristic_polynomial": str(charpoly),
            "positive_definite_shift": f"{q}D+{p}I",
            "ldl_pivot_count": len(pivots),
            "smallest_ldl_pivot_in_fixed_order": str(min(pivots, key=lambda z: float(z))),
        })
        result[name] = summary

    # The quadratic factor x^2+4x-3 gives -2-sqrt(7), and exact scalar
    # comparisons establish the strict signs in the first two cases.
    assert Fraction(48, 7) > Fraction(2, 1) + sp.sqrt(7)
    assert Fraction(47, 7) > Fraction(2, 1) + sp.sqrt(7)
    return result


def verify_coclique_no_go() -> dict[str, object]:
    full, labels = hoffman_singleton()
    deleted_indices = {0, 8, 14, 18, 20, 26, 27, 32, 33, 36, 37, 43, 44, 48, 49}
    for u in deleted_indices:
        for v in deleted_indices:
            if u < v:
                assert v not in full[u]
    deleted = {labels[i] for i in deleted_indices}
    graph, _ = induced(full, labels, deleted)
    summary, d = graph_summary(graph)
    a = adjacency_matrix(graph)
    expected_a = (X - 4) * (X - 2) ** 14 * (X + 1) ** 14 * (X + 3) ** 6
    expected_d = (X - 82) * (X - 2) ** 14 * (X + 2) ** 6 * (X + 7) ** 14
    assert sp.Poly(a.charpoly(X).as_expr() - expected_a, X).is_zero
    assert sp.Poly(d.charpoly(X).as_expr() - expected_d, X).is_zero
    assert summary["degrees"] == {4: 35}
    assert summary["girth"] == 6
    assert summary["minimum_dual_degree"] == "4"
    summary.update({
        "deleted_original_indices": sorted(deleted_indices),
        "adjacency_characteristic_polynomial": str(sp.factor(expected_a)),
        "distance_characteristic_polynomial": str(sp.factor(expected_d)),
        "least_distance_eigenvalue": -7,
        "score": -3,
        "counterexample": False,
    })
    return summary


def verify_symbolic_moore_blocks() -> dict[str, str]:
    t = sp.symbols("t", positive=True)
    k = t**2

    # One-vertex deletion: normalized two-cell quotient shifted by 2+sqrt(k).
    one_a = 3 * (k - 1)
    one_b = 2 * k**2 - 3 * k - 1
    one_off_sq = (k - 1) * (2 * k - 1) ** 2
    one_shift_det = sp.factor((one_a + 2 + t) * (one_b + 2 + t) - one_off_sq)
    assert one_shift_det == t**2 * (2 * t**4 + 2 * t**3 - 3 * t**2 + 2)

    # Edge deletion: quotient on A∪B and C.
    edge_a = 5 * k - 8
    edge_b = 2 * k**2 - 5 * k + 2
    edge_off_sq = (k - 1) * (2 * k - 3) * (4 * k - 6)
    edge_shift_det = sp.factor((edge_a + 2 + t) * (edge_b + 2 + t) - edge_off_sq)
    assert edge_shift_det == (t - 1) * (t + 1) * (
        2 * t**4 + 2 * t**3 - 3 * t**2 + 2 * t + 6
    )

    kvar = sp.symbols("k", integer=True, positive=True)
    one_square_margin = sp.expand((kvar**2 - 2 * kvar - 1) ** 2 - kvar**3)
    edge_square_margin = sp.expand((kvar**2 - 2 * kvar - 2) ** 2 - kvar**3)
    m = sp.symbols("m", integer=True, nonnegative=True)
    assert sp.expand(one_square_margin.subs(kvar, m + 5)) == (
        m**4 + 15 * m**3 + 77 * m**2 + 149 * m + 71
    )
    assert sp.expand(edge_square_margin.subs(kvar, m + 5)) == (
        m**4 + 15 * m**3 + 75 * m**2 + 133 * m + 44
    )

    # The quotient determinants are positive for t >= sqrt(2): isolate the
    # only negative term inside a manifestly positive decomposition.
    one_core = 2 * t**4 + 2 * t**3 - 3 * t**2 + 2
    edge_core = 2 * t**4 + 2 * t**3 - 3 * t**2 + 2 * t + 6
    assert sp.expand(one_core - (t**2 * (2 * t**2 - 3) + 2 * t**3 + 2)) == 0
    assert sp.expand(edge_core - (t**2 * (2 * t**2 - 3) + 2 * t**3 + 2 * t + 6)) == 0

    # Exact low-degree side of the threshold.
    for value in (2, 3, 4):
        assert bool(sp.simplify(value - sp.Rational(1, value) - 2 - sp.sqrt(value)) < 0)
        assert bool(sp.simplify(value - sp.Rational(2, value) - 2 - sp.sqrt(value)) < 0)

    return {
        "one_vertex_quotient_shift_determinant": str(one_shift_det),
        "edge_quotient_shift_determinant": str(edge_shift_det),
        "one_vertex_threshold_polynomial_at_k=m+5": str(sp.expand(one_square_margin.subs(kvar, m + 5))),
        "edge_threshold_polynomial_at_k=m+5": str(sp.expand(edge_square_margin.subs(kvar, m + 5))),
    }



def verify_low_degree_moore_cases() -> dict[str, object]:
    """Check the degree-two exception and the degree-three boundary exactly."""
    from itertools import combinations

    def induced_indices(graph, deleted):
        keep = [i for i in range(len(graph)) if i not in deleted]
        relabel = {old: new for new, old in enumerate(keep)}
        return tuple(
            frozenset(relabel[v] for v in graph[u] if v in relabel) for u in keep
        )

    # C5.
    c5 = tuple(frozenset({(i - 1) % 5, (i + 1) % 5}) for i in range(5))
    c5_one = induced_indices(c5, {0})
    c5_edge = induced_indices(c5, {0, 1})
    cp_c5_one = sp.factor(distance_matrix(c5_one).charpoly(X).as_expr())
    cp_c5_edge = sp.factor(distance_matrix(c5_edge).charpoly(X).as_expr())
    assert cp_c5_one == (X**2 - 4 * X - 6) * (X**2 + 4 * X + 2)
    assert cp_c5_edge == (X + 2) * (X**2 - 2 * X - 2)
    assert min(dual_degrees(c5_one)) == Fraction(3, 2)
    assert min(dual_degrees(c5_edge)) == Fraction(1, 1)

    # Petersen graph as KG(5,2).
    vertices = list(combinations(range(5), 2))
    rows = [set() for _ in vertices]
    for i, a in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            b = vertices[j]
            if set(a).isdisjoint(b):
                rows[i].add(j)
                rows[j].add(i)
    petersen = tuple(frozenset(r) for r in rows)
    neighbor = next(iter(petersen[0]))
    pet_one = induced_indices(petersen, {0})
    pet_edge = induced_indices(petersen, {0, neighbor})
    cp_pet_one = sp.factor(distance_matrix(pet_one).charpoly(X).as_expr())
    cp_pet_edge = sp.factor(distance_matrix(pet_edge).charpoly(X).as_expr())
    assert cp_pet_one == X * (X + 3) ** 2 * (X**2 - 14 * X - 2) * (X**2 + 4 * X + 1) ** 2
    assert cp_pet_edge == (X + 1) * (X + 3) * (X**2 - 12 * X - 1) * (X**2 + 4 * X + 1) ** 2
    assert min(dual_degrees(pet_one)) == Fraction(8, 3)
    assert min(dual_degrees(pet_edge)) == Fraction(7, 3)

    return {
        "C5_one_vertex_charpoly": str(cp_c5_one),
        "C5_edge_charpoly": str(cp_c5_edge),
        "C5_edge_exception_least": "-2",
        "Petersen_one_vertex_charpoly": str(cp_pet_one),
        "Petersen_edge_charpoly": str(cp_pet_edge),
        "Petersen_puncture_least": "-2-sqrt(3)",
    }

def main() -> None:
    result = {
        "punctured_hoffman_singleton": verify_punctures(),
        "delsarte_coclique_complement_no_go": verify_coclique_no_go(),
        "symbolic_generic_moore_checks": verify_symbolic_moore_blocks(),
        "low_degree_moore_checks": verify_low_degree_moore_cases(),
    }
    output = ROOT / "data" / "new_generalizations.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("new generalizations: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
