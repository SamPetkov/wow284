#!/usr/bin/env python3
"""Exact verification of proposed structural extensions around WOW-284.

All asserted conclusions use integer, rational, or symbolic arithmetic. The
script deliberately separates proved identities from literature-priority
questions, which are documented elsewhere.
"""
from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def p(i: int, j: int) -> int:
        return 5 * (i % 5) + (j % 5)

    def q(k: int, ell: int) -> int:
        return 25 + 5 * (k % 5) + (ell % 5)

    def add(u: int, v: int) -> None:
        assert u != v
        rows[u].add(v)
        rows[v].add(u)

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(5):
                add(p(i, j), q(k, i * k + j))
    graph = tuple(frozenset(row) for row in rows)
    assert all(len(row) == 7 for row in graph)
    return graph


def induced(graph: Graph, deleted: set[int]) -> tuple[Graph, tuple[int, ...]]:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    index = {old: new for new, old in enumerate(keep)}
    return (
        tuple(frozenset(index[w] for w in graph[v] if w in index) for v in keep),
        keep,
    )


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    result: list[tuple[int, ...]] = []
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
        assert -1 not in dist
        result.append(tuple(dist))
    return tuple(result)


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def distance_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(distance_rows(graph))


def girth(graph: Graph) -> int:
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


def dual_degrees(graph: Graph) -> tuple[Fraction, ...]:
    degrees = tuple(map(len, graph))
    return tuple(
        Fraction(sum(degrees[u] for u in graph[v]), degrees[v])
        for v in range(len(graph))
    )


def ldl_positive(matrix: sp.Matrix) -> tuple[sp.Expr, ...]:
    lower, diagonal = matrix.LDLdecomposition(hermitian=True)
    assert lower * diagonal * lower.T == matrix
    pivots = tuple(sp.factor(diagonal[i, i]) for i in range(matrix.rows))
    assert all(bool(pivot > 0) for pivot in pivots)
    return pivots


def verify_radius_two_identity(graph: Graph) -> None:
    distances = distance_rows(graph)
    degrees = tuple(map(len, graph))
    for v in range(len(graph)):
        ball_two = sum(int(distances[v][u] <= 2) for u in range(len(graph)))
        assert Fraction(ball_two - 1, degrees[v]) == Fraction(
            sum(degrees[u] for u in graph[v]), degrees[v]
        )


def graph40(full: Graph) -> Graph:
    return induced(full, set(range(5)) | set(range(25, 30)))[0]


def graph42(full: Graph) -> Graph:
    return induced(full, {0} | set(full[0]))[0]


def verify_operator_identity(graph: Graph) -> dict[str, object]:
    degrees = {len(row) for row in graph}
    assert len(degrees) == 1
    k = next(iter(degrees))
    assert girth(graph) >= 5
    d = distance_matrix(graph)
    assert max(d) == 3
    a = adjacency_matrix(graph)
    n = len(graph)
    identity = sp.eye(n)
    ones = sp.ones(n)
    assert d == 3 * ones + (k - 3) * identity - 2 * a - a * a
    assert d + k * identity == (
        3 * ones + (2 * k - 2) * identity - (a + identity) ** 2
    )

    adjacency_values = a.eigenvals()
    nonprincipal = [
        theta
        for theta, mult in adjacency_values.items()
        for _ in range(mult)
        if theta != k
    ]
    radius_sq = max(sp.expand((theta + 1) ** 2) for theta in nonprincipal)
    least = min(d.eigenvals(), key=lambda z: float(sp.N(z)))
    score = sp.Integer(k) + least
    assert sp.simplify(score - (2 * k - 2 - radius_sq)) == 0
    return {
        "order": n,
        "degree": k,
        "least_distance_eigenvalue": str(least),
        "score": str(score),
        "shifted_adjacency_radius_squared": str(radius_sq),
    }


def verify_concrete_punctures(full: Graph) -> dict[str, object]:
    cases = {
        "one_vertex": {
            "deleted": {0},
            "dual": Fraction(48, 7),
            "charpoly": (X - 1) ** 14
            * (X + 4) ** 21
            * (X**2 - 94 * X + 354)
            * (X**2 + 4 * X - 3) ** 6,
            "shift": (7, 48),
        },
        "edge_endpoints": {
            "deleted": {0, 1},
            "dual": Fraction(47, 7),
            "charpoly": (X - 3)
            * (X - 1) ** 9
            * (X + 4) ** 16
            * (X**2 - 92 * X + 303)
            * (X**2 + 4 * X - 3) ** 10,
            "shift": (7, 47),
        },
        "nonadjacent_pair": {
            "deleted": {0, 2},
            "dual": Fraction(47, 7),
            "charpoly": (X - 4)
            * (X - 1) ** 8
            * (X + 4) ** 15
            * (X**2 + 4 * X - 4) ** 5
            * (X**2 + 4 * X - 2) ** 5
            * (X**4 - 88 * X**3 - 125 * X**2 + 1740 * X - 778),
            "shift": (7, 47),
        },
    }
    output: dict[str, object] = {}
    full_d = distance_matrix(full)
    for name, case in cases.items():
        graph, keep = induced(full, case["deleted"])
        assert girth(graph) >= 5
        assert max(distance_matrix(graph)) == 3
        assert min(dual_degrees(graph)) == case["dual"]
        d = distance_matrix(graph)
        assert sp.Poly(d.charpoly(X).as_expr() - case["charpoly"], X).is_zero
        q, p = case["shift"]
        pivots = ldl_positive(q * d + p * sp.eye(len(graph)))

        principal = full_d.extract(keep, keep)
        increase = d - principal
        if name == "one_vertex":
            expected = (X - 6) * (X + 1) ** 6 * X**42
            assert sp.Poly(increase.charpoly(X).as_expr() - expected, X).is_zero
        elif name == "edge_endpoints":
            expected = (X - 5) ** 2 * (X + 1) ** 10 * X**36
            assert sp.Poly(increase.charpoly(X).as_expr() - expected, X).is_zero
        else:
            expected = (X + 1) ** 10 * (X - 5) * (X**2 - 5 * X - 12) * X**35
            assert sp.Poly(increase.charpoly(X).as_expr() - expected, X).is_zero

        output[name] = {
            "order": len(graph),
            "size": sum(map(len, graph)) // 2,
            "degree_multiset": dict(sorted(Counter(map(len, graph)).items())),
            "minimum_dual_degree": str(case["dual"]),
            "positive_definite_shift": f"{q}D+{p}I",
            "ldl_pivots": len(pivots),
        }
    return output


def verify_symbolic_punctured_moore() -> dict[str, str]:
    k, lam = sp.symbols("k lam")

    one_const = sp.Matrix(
        [
            [3 * (k - 1), (2 * k - 1) * sp.sqrt(k - 1)],
            [(2 * k - 1) * sp.sqrt(k - 1), 2 * k**2 - 3 * k - 1],
        ]
    )
    one_inc = sp.Matrix([[-3, -(k - 1)], [-1, -1]])
    assert sp.factor(one_inc.charpoly(lam).as_expr()) == (
        lam**2 + 4 * lam + 4 - k
    )
    one_const_poly = sp.factor(one_const.charpoly(lam).as_expr())
    one_radicand = sp.expand(k * (k**3 - 2 * k**2 + 3 * k - 1))
    assert sp.expand(sp.discriminant(one_const_poly, lam) - 4 * one_radicand) == 0
    assert (
        sp.expand(
            -sp.Poly(one_const_poly, lam).coeff_monomial(lam) / 2 - (k**2 - 2)
        )
        == 0
    )

    edge_const = sp.Matrix(
        [
            [
                5 * k - 8,
                sp.sqrt((k - 1) * (2 * k - 3) * (4 * k - 6)),
            ],
            [
                sp.sqrt((k - 1) * (2 * k - 3) * (4 * k - 6)),
                2 * k**2 - 5 * k + 2,
            ],
        ]
    )
    edge_const_poly = sp.factor(edge_const.charpoly(lam).as_expr())
    edge_radicand = sp.expand(k**4 - 2 * k**3 + 3 * k**2 - 8 * k + 7)
    assert sp.expand(sp.discriminant(edge_const_poly, lam) - 4 * edge_radicand) == 0
    assert (
        sp.expand(
            -sp.Poly(edge_const_poly, lam).coeff_monomial(lam) / 2 - (k**2 - 3)
        )
        == 0
    )

    delta = sp.symbols("Delta", positive=True)
    r = (-1 + delta) / 2
    s = (-1 - delta) / 2
    n_one = k * (k - 2)
    m_r = sp.simplify(n_one * (delta + 1) / (2 * delta))
    m_s = sp.simplify(n_one * (delta - 1) / (2 * delta))
    assert sp.simplify(m_r + m_s - n_one) == 0
    assert sp.simplify(r * m_r + s * m_s) == 0

    n_edge = (k - 2) ** 2
    a_r = sp.simplify((k - 2) * (k + (k - 2) * delta) / (2 * delta))
    a_s = sp.simplify((k - 2) * ((k - 2) * delta - k) / (2 * delta))
    assert sp.simplify(a_r + a_s - n_edge) == 0
    assert sp.simplify(r * a_r + s * a_s - (k - 2)) == 0

    kvar, m = sp.symbols("kvar m", integer=True, nonnegative=True)
    one_margin = sp.expand((kvar**2 - 2 * kvar - 1) ** 2 - kvar**3)
    edge_margin = sp.expand((kvar**2 - 2 * kvar - 2) ** 2 - kvar**3)
    assert sp.expand(one_margin.subs(kvar, m + 5)) == (
        m**4 + 15 * m**3 + 77 * m**2 + 149 * m + 71
    )
    assert sp.expand(edge_margin.subs(kvar, m + 5)) == (
        m**4 + 15 * m**3 + 75 * m**2 + 133 * m + 44
    )

    t = sp.symbols("t", positive=True)
    kt = t**2
    one_shift_det = sp.factor(
        (3 * (kt - 1) + 2 + t)
        * (2 * kt**2 - 3 * kt - 1 + 2 + t)
        - (kt - 1) * (2 * kt - 1) ** 2
    )
    edge_shift_det = sp.factor(
        (5 * kt - 8 + 2 + t)
        * (2 * kt**2 - 5 * kt + 2 + 2 + t)
        - (kt - 1) * (2 * kt - 3) * (4 * kt - 6)
    )
    assert one_shift_det == t**2 * (2 * t**4 + 2 * t**3 - 3 * t**2 + 2)
    assert edge_shift_det == (t - 1) * (t + 1) * (
        2 * t**4 + 2 * t**3 - 3 * t**2 + 2 * t + 6
    )

    return {
        "one_vertex_incidence_factor": str(
            sp.factor(one_inc.charpoly(lam).as_expr())
        ),
        "one_vertex_constant_factor": str(one_const_poly),
        "edge_constant_factor": str(edge_const_poly),
        "one_vertex_threshold_square_margin": str(one_margin),
        "edge_threshold_square_margin": str(edge_margin),
    }


def verify_deletion_stability_symbolics() -> dict[str, str]:
    k, lam = sp.symbols("k lam")

    # Distance-increase graph for deleting two nonadjacent Moore vertices:
    # two copies of K_k meeting in their unique common neighbor.
    quotient = sp.Matrix(
        [
            [0, k - 1, k - 1],
            [1, k - 2, 0],
            [1, 0, k - 2],
        ]
    )
    quotient_poly = sp.factor(quotient.charpoly(lam).as_expr())
    expected = (lam - (k - 2)) * (
        lam**2 - (k - 2) * lam - 2 * (k - 1)
    )
    assert sp.expand(quotient_poly - expected) == 0

    kvar, m = sp.symbols("kvar m", integer=True, nonnegative=True)
    positivity_polynomial = (
        4 * kvar**8
        - 39 * kvar**7
        + 95 * kvar**6
        + 9 * kvar**5
        - 173 * kvar**4
        - 36 * kvar**3
        + 116 * kvar**2
        + 80 * kvar
        + 16
    )
    shifted = sp.expand(positivity_polynomial.subs(kvar, m + 6))
    expected_shifted = (
        4 * m**8
        + 153 * m**7
        + 2489 * m**6
        + 22329 * m**5
        + 119437 * m**4
        + 382236 * m**3
        + 685268 * m**2
        + 559616 * m
        + 75952
    )
    assert sp.expand(shifted - expected_shifted) == 0

    return {
        "nonadjacent_distance_increase_quotient": str(quotient_poly),
        "k_ge_6_positivity_polynomial": str(positivity_polynomial),
        "shift_at_k=m+6": str(shifted),
    }


def verify_moment_and_layer_bounds() -> dict[str, str]:
    k, n, x, c = sp.symbols("k n x c")
    sum_y2 = (k + 1) * (n - k - 1)
    sum_y4 = (2 * k**2 + 5 * k + 1) * n - (k + 1) ** 4
    phi_upper = sp.factor(2 * k - 2 - sum_y4 / sum_y2)
    expected = sp.factor(
        ((k + 1) ** 2 * (k**2 + 3) - (5 * k + 3) * n)
        / ((k + 1) * (n - k - 1))
    )
    assert sp.simplify(phi_upper - expected) == 0

    a0 = k - 1 - c / (k - 1)
    q0 = sp.Matrix(
        [
            [0, k, 0, 0],
            [1, 0, k - 1, 0],
            [0, 1, a0, c / (k - 1)],
            [0, 0, k, 0],
        ]
    )
    char = sp.factor(q0.charpoly(x).as_expr())
    p = (
        (k - 1) * x**3
        + (c + k - 1) * x**2
        - (k - 1) ** 2 * x
        - c * k
    )
    assert sp.simplify(char / (x - k) - p / (k - 1)) == 0
    assert (
        sp.expand(
            p.subs({k: 6, c: 15}) - 5 * (x + 2) * (x**2 + 2 * x - 9)
        )
        == 0
    )

    # Rank-one monotonicity of the normalized layer compression.
    r = k * (k - 1) / c
    derivative = sp.Matrix([[1, -sp.sqrt(r)], [-sp.sqrt(r), r]])
    z = sp.Matrix([1, -sp.sqrt(r)])
    assert sp.simplify(derivative - z * z.T) == sp.zeros(2)

    return {
        "sum_shifted_squares": str(sum_y2),
        "sum_shifted_fourth_powers": str(sum_y4),
        "score_upper_bound": str(expected),
        "layer_nonprincipal_factor": str(sp.factor(p / (k - 1))),
    }


def verify_higher_diameter_polynomials() -> dict[str, str]:
    k, x = sp.symbols("k x")
    f0 = sp.Integer(1)
    f1 = x
    f2 = x**2 - k
    f3 = sp.expand(x * f2 - (k - 1) * f1)
    assert sp.expand(f3 - (x**3 - (2 * k - 1) * x)) == 0
    q3 = sp.expand(sum((i - 3) * f for i, f in enumerate([f0, f1, f2])))
    q4 = sp.expand(sum((i - 4) * f for i, f in enumerate([f0, f1, f2, f3])))
    assert sp.expand(q3 - (-x**2 - 2 * x + k - 3)) == 0
    assert (
        sp.expand(q4 - (-x**3 - 2 * x**2 + (2 * k - 4) * x + 2 * k - 4))
        == 0
    )
    return {"q3": str(q3), "q4": str(q4)}


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    full = hoffman_singleton()
    g40 = graph40(full)
    g42 = graph42(full)
    for graph in (
        full,
        g40,
        g42,
        induced(full, {0})[0],
        induced(full, {0, 1})[0],
    ):
        assert girth(graph) >= 5
        verify_radius_two_identity(graph)

    result = {
        "radius_two_dual_degree_identity": (
            "PASS on five independent finite representatives"
        ),
        "diameter_three_operator_identity": {
            "order_40": verify_operator_identity(g40),
            "order_42": verify_operator_identity(g42),
        },
        "concrete_punctures": verify_concrete_punctures(full),
        "symbolic_punctured_moore": verify_symbolic_punctured_moore(),
        "deletion_stability_symbolics": verify_deletion_stability_symbolics(),
        "moment_and_layer_bounds": verify_moment_and_layer_bounds(),
        "higher_diameter_polynomials": verify_higher_diameter_polynomials(),
    }
    print("verified research extensions: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
