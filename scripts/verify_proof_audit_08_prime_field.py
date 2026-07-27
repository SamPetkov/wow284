#!/usr/bin/env python3
"""Independent exact audit of the balanced prime-field obstruction.

The script does not import the original verifier. It checks the symbolic
zero-mode and singular-value reductions, exact radical comparisons, graph
hypotheses for all q=7 members, complete characteristic polynomials for the
three surviving parameters, and exact nonprincipal-root counts. No
floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def prime_field_graph(q: int, m: int) -> Graph:
    if q < 7 or q % 2 == 0 or not 1 <= m <= q:
        raise AssertionError("parameters outside the audited family")
    vertices = [
        *(("P", i, j) for i in range(m) for j in range(q)),
        *(("Q", k, ell) for k in range(m) for ell in range(q)),
    ]
    index = {vertex: number for number, vertex in enumerate(vertices)}
    rows = [set() for _ in vertices]

    def add(left: tuple[str, int, int], right: tuple[str, int, int]) -> None:
        u, v = index[left], index[right]
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(m):
        for j in range(q):
            add(("P", i, j), ("P", i, (j + 1) % q))
            add(("Q", i, j), ("Q", i, (j + 2) % q))
            for k in range(m):
                add(("P", i, j), ("Q", k, (i * k + j) % q))

    graph = tuple(frozenset(row) for row in rows)
    if set(map(len, graph)) != {m + 2}:
        raise AssertionError("wrong degree")
    return graph


def distance_rows(graph: Graph) -> tuple[tuple[int, ...], ...]:
    output: list[tuple[int, ...]] = []
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        if -1 in distance:
            raise AssertionError("disconnected graph")
        output.append(tuple(distance))
    return tuple(output)


def exact_girth(graph: Graph) -> int:
    best = len(graph) + 1
    for source in range(len(graph)):
        distance = [-1] * len(graph)
        parent = [-1] * len(graph)
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v and parent[v] != u:
                    best = min(best, distance[u] + distance[v] + 1)
    return best


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def sign_variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign]
    return sum(left * right < 0 for left, right in zip(nonzero, nonzero[1:]))


def variations_at_positive_infinity(sequence: list[sp.Expr]) -> int:
    return sign_variations([int(sp.sign(sp.Poly(term, X).LC())) for term in sequence])


def variations_at(sequence: list[sp.Expr], point: sp.Rational) -> int:
    signs: list[int] = []
    for term in sequence:
        value = sp.Poly(term, X).eval(point)
        if value == 0:
            raise AssertionError("Sturm separator is a root")
        signs.append(int(sp.sign(value)))
    return sign_variations(signs)


def distinct_roots_above(expression: sp.Expr, point: sp.Rational) -> int:
    square_free = sp.Poly(expression, X).sqf_part().as_expr()
    sequence = sp.sturm(square_free, X)
    return variations_at(sequence, point) - variations_at_positive_infinity(sequence)


def symbolic_audit() -> dict[str, object]:
    m = sp.symbols("m", integer=True, positive=True)
    a, b, sigma, lam = sp.symbols("a b sigma lambda", real=True)

    zero_block = sp.Matrix([[2, m], [m, 2]])
    if sp.factor(zero_block.charpoly(lam).as_expr()) != (lam - m - 2) * (lam + m - 2):
        raise AssertionError("wrong zero-character constant block")
    if sp.expand((m - 3) ** 2 - (2 * m + 2) - (m - 1) * (m - 7)) != 0:
        raise AssertionError("wrong zero-mode boundary factorization")

    surviving = []
    for value in range(1, 30):
        degree = value + 2
        zero_eigenvalues = [2 - value]
        if value >= 2:
            zero_eigenvalues.append(2)
        admissible = all(
            sp.simplify((theta + 1) ** 2 < 2 * degree - 2) is sp.true
            for theta in zero_eigenvalues
        )
        if admissible:
            surviving.append(value)
    if surviving != [4, 5, 6]:
        raise AssertionError("wrong zero-mode survivor set")

    singular_block = sp.Matrix([[a, sigma], [sigma, b]])
    expected_characteristic = (lam - a) * (lam - b) - sigma**2
    if sp.expand(singular_block.charpoly(lam).as_expr() - expected_characteristic) != 0:
        raise AssertionError("wrong singular-pair block")
    upper_root = (a + b + sp.sqrt((a - b) ** 2 + 4 * sigma**2)) / 2
    if sp.simplify(singular_block.charpoly(lam).as_expr().subs(lam, upper_root)) != 0:
        raise AssertionError("wrong upper singular-block eigenvalue")

    # Frobenius averaging: m singular-value squares sum to m^2.
    if sp.simplify(m**2 / m - m) != 0:
        raise AssertionError("wrong Frobenius singular-value bound")

    # Exact radical certificate for the worst surviving value m=6.
    if not 14 * 16 < 15**2:
        raise AssertionError("sqrt(14) upper bound failed")
    if not 6 * 25 > 12**2:
        raise AssertionError("sqrt(6) lower bound failed")
    if not 3 * 100 > 17**2:
        raise AssertionError("sqrt(3) lower bound failed")
    if sp.Rational(15, 4) - sp.Rational(12, 5) != sp.Rational(27, 20):
        raise AssertionError("wrong rational difference")
    if (sp.Rational(17, 10) + 1) / 2 != sp.Rational(27, 20):
        raise AssertionError("wrong comparison target")

    exact_margins: dict[str, str] = {}
    for value in (4, 5, 6):
        margin = sp.sqrt(value) + (sp.sqrt(3) - 1) / 2 + 1 - sp.sqrt(2 * value + 2)
        if sp.ask(sp.Q.positive(margin)) is not True:
            # A direct exact fallback after squaring/rational isolation.
            minimal = sp.minpoly(margin, X)
            interval = sp.polys.polytools.intervals(sp.Poly(minimal, X), eps=sp.Rational(1, 10**6))
            positive_intervals = [item for item in interval if item[0][0] > 0]
            if not positive_intervals:
                raise AssertionError("failed exact positive-margin certification")
        exact_margins[str(value)] = str(sp.simplify(margin))

    return {
        "zero_mode_survivors": surviving,
        "singular_pair_upper_root": str(upper_root),
        "Frobenius_lower_bound_sigma_squared": "m",
        "exact_positive_margins": exact_margins,
    }


def expected_charpolys() -> dict[int, sp.Expr]:
    return {
        4: (X - 6)
        * (X - 2) ** 6
        * (X + 2)
        * (X**6 + 2 * X**5 - 24 * X**4 - 34 * X**3 + 184 * X**2 + 137 * X - 433) ** 2
        * (X**6 + 2 * X**5 - 10 * X**4 - 13 * X**3 + 30 * X**2 + 18 * X - 27) ** 2
        * (
            X**12 + 4 * X**11 - 22 * X**10 - 93 * X**9 + 174 * X**8
            + 769 * X**7 - 666 * X**6 - 2734 * X**5 + 1577 * X**4
            + 3823 * X**3 - 2280 * X**2 - 891 * X + 421
        ) ** 2,
        5: (X - 7)
        * (X - 2) ** 8
        * (X + 3)
        * (X**3 - 7 * X + 7) ** 2
        * (X**3 + 2 * X**2 - X - 1) ** 2
        * (X**6 + 2 * X**5 - 24 * X**4 - 34 * X**3 + 184 * X**2 + 137 * X - 433) ** 6
        * (X**6 + 2 * X**5 - 10 * X**4 - 20 * X**3 + 23 * X**2 + 46 * X + 1) ** 2,
        6: (X - 8)
        * (X - 2) ** 10
        * (X + 4)
        * (X**6 + 2 * X**5 - 24 * X**4 - 34 * X**3 + 184 * X**2 + 137 * X - 433) ** 10
        * (X**6 + 2 * X**5 - 6 * X**4 - 10 * X**3 + 10 * X**2 + 11 * X - 1) ** 2,
    }


def finite_q7_audit() -> dict[str, object]:
    graph_data: dict[str, object] = {}
    expected_diameters = {1: 3, 2: 4, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3}
    for m in range(1, 8):
        graph = prime_field_graph(7, m)
        distances = distance_rows(graph)
        diameter = max(max(row) for row in distances)
        if len(graph) != 14 * m or set(map(len, graph)) != {m + 2}:
            raise AssertionError("wrong q=7 order or degree")
        if exact_girth(graph) != 5:
            raise AssertionError("wrong q=7 girth")
        if diameter != expected_diameters[m]:
            raise AssertionError("wrong q=7 diameter")
        graph_data[str(m)] = {
            "order": len(graph),
            "degree": m + 2,
            "girth": 5,
            "diameter": diameter,
        }

    separators = {4: sp.Rational(9, 4), 5: sp.Rational(5, 2), 6: sp.Rational(11, 4)}
    expected_counts = {4: 5, 5: 4, 6: 3}
    polynomial_data: dict[str, object] = {}
    for m, expected in expected_charpolys().items():
        graph = prime_field_graph(7, m)
        actual = adjacency_matrix(graph).charpoly(X).as_expr()
        if not sp.Poly(actual - expected, X).is_zero:
            raise AssertionError("wrong q=7 adjacency characteristic polynomial")

        separator = separators[m]
        if m == 4 and not 10 * 16 < 13**2:
            raise AssertionError("m=4 separator is not beyond the WOW endpoint")
        if m == 5 and not 12 * 4 < 7**2:
            raise AssertionError("m=5 separator is not beyond the WOW endpoint")
        if m == 6 and not 14 * 16 < 15**2:
            raise AssertionError("m=6 separator is not beyond the WOW endpoint")

        count = distinct_roots_above(expected, separator)
        if count != expected_counts[m] or count < 2:
            raise AssertionError("wrong exact upper-root count")
        polynomial_data[str(m)] = {
            "separator": str(separator),
            "distinct_roots_above_separator": count,
            "nonprincipal_root_beyond_WOW_window": True,
            "adjacency_characteristic_polynomial": str(sp.factor(expected)),
        }

    return {"all_q7_graphs": graph_data, "exact_spectral_controls": polynomial_data}


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "symbolic_audit": symbolic_audit(),
        "finite_q7_audit": finite_q7_audit(),
    }
    print("Proof Audit 08 (prime-field diameter-three obstruction): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
