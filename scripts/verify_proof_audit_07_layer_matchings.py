#!/usr/bin/env python3
"""Independent exact audit of the 120 layer-respecting matching deletions.

This script does not import the original matching-deletion verifier. It checks
all perfect matchings, all displayed coordinate automorphisms, the complete
20/100 orbit exhaustion, graph hypotheses, exact characteristic polynomials,
and exact Sturm least-root certificates. No floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
from itertools import permutations
import json

import sympy as sp

MODULUS = 5
X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]
Permutation = tuple[int, ...]


def p(i: int, j: int) -> int:
    return 5 * (i % MODULUS) + (j % MODULUS)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % MODULUS) + (ell % MODULUS)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def add(u: int, v: int) -> None:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(5):
                add(p(i, j), q(k, i * k + j))

    graph = tuple(frozenset(row) for row in rows)
    if set(map(len, graph)) != {7}:
        raise AssertionError("wrong Hoffman--Singleton degree")
    return graph


FULL = hoffman_singleton()
ALL_PERMUTATIONS = tuple(permutations(range(5)))
FULL_EDGES = frozenset(
    (u, v) for u in range(50) for v in FULL[u] if u < v
)


def matching_edges(pi: Permutation) -> frozenset[tuple[int, int]]:
    edges = frozenset(
        tuple(sorted((p(i, j), q(pi[i], i * pi[i] + j))))
        for i in range(5)
        for j in range(5)
    )
    if len(edges) != 25:
        raise AssertionError("wrong matching cardinality")

    incidences = [0] * 50
    for u, v in edges:
        if v not in FULL[u]:
            raise AssertionError("proposed matching edge is not an HS edge")
        incidences[u] += 1
        incidences[v] += 1
    if incidences != [1] * 50:
        raise AssertionError("matching is not perfect")
    return edges


def delete_matching(pi: Permutation) -> Graph:
    rows = [set(row) for row in FULL]
    for u, v in matching_edges(pi):
        rows[u].remove(v)
        rows[v].remove(u)
    return tuple(frozenset(row) for row in rows)


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


def graph_girth(graph: Graph) -> int:
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


def distance_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(distance_rows(graph))


def type_preserving_map(a: int, b: int, s: int, d: int) -> dict[int, int]:
    c = s * pow(a, -1, 5) % 5
    image: dict[int, int] = {}
    for i in range(5):
        for j in range(5):
            image[p(i, j)] = p(a * i + b, s * j - a * d * i - b * d)
    for k in range(5):
        for ell in range(5):
            image[q(k, ell)] = q(c * k + d, s * ell + b * c * k)
    return image


def type_swapping_map(a: int, b: int, t: int, d: int) -> dict[int, int]:
    c = (-t) * pow(a, -1, 5) % 5
    image: dict[int, int] = {}
    for i in range(5):
        for j in range(5):
            image[p(i, j)] = q(a * i + b, t * j + d * a * i + d * b)
    for k in range(5):
        for ell in range(5):
            image[q(k, ell)] = p(c * k + d, t * ell - c * b * k)
    return image


def transform_type_preserving(
    pi: Permutation, a: int, b: int, s: int, d: int
) -> Permutation:
    c = s * pow(a, -1, 5) % 5
    output: list[int | None] = [None] * 5
    for i in range(5):
        output[(a * i + b) % 5] = (c * pi[i] + d) % 5
    if any(value is None for value in output):
        raise AssertionError("incomplete type-preserving transform")
    return tuple(int(value) for value in output)


def transform_type_swapping(
    pi: Permutation, a: int, b: int, t: int, d: int
) -> Permutation:
    c = (-t) * pow(a, -1, 5) % 5
    output: list[int | None] = [None] * 5
    for i in range(5):
        output[(c * pi[i] + d) % 5] = (a * i + b) % 5
    if any(value is None for value in output):
        raise AssertionError("incomplete type-swapping transform")
    return tuple(int(value) for value in output)


def is_affine(pi: Permutation) -> bool:
    return any(
        all(pi[i] == (a * i + b) % 5 for i in range(5))
        for a in range(1, 5)
        for b in range(5)
    )


def build_coordinate_generators() -> list[tuple[str, int, int, int, int, dict[int, int]]]:
    generators: list[tuple[str, int, int, int, int, dict[int, int]]] = []
    encodings: set[tuple[int, ...]] = set()

    for a in range(1, 5):
        for b in range(5):
            for d in range(5):
                for kind, parameter in (
                    ("preserving", 1),
                    ("preserving", 4),
                    ("swapping", 2),
                    ("swapping", 3),
                ):
                    mapping = (
                        type_preserving_map(a, b, parameter, d)
                        if kind == "preserving"
                        else type_swapping_map(a, b, parameter, d)
                    )
                    encoding = tuple(mapping[i] for i in range(50))
                    if len(set(encoding)) != 50:
                        raise AssertionError("coordinate map is not bijective")
                    image_edges = frozenset(
                        tuple(sorted((mapping[u], mapping[v])))
                        for u, v in FULL_EDGES
                    )
                    if image_edges != FULL_EDGES:
                        raise AssertionError("coordinate map is not an HS automorphism")
                    encodings.add(encoding)
                    generators.append((kind, a, b, parameter, d, mapping))

    if len(generators) != 400 or len(encodings) != 400:
        raise AssertionError("unexpected coordinate-map count")

    # Check every displayed map on every matching, not only on orbit seeds.
    for pi in ALL_PERMUTATIONS:
        source = matching_edges(pi)
        for kind, a, b, parameter, d, mapping in generators:
            transformed = (
                transform_type_preserving(pi, a, b, parameter, d)
                if kind == "preserving"
                else transform_type_swapping(pi, a, b, parameter, d)
            )
            image = frozenset(
                tuple(sorted((mapping[u], mapping[v]))) for u, v in source
            )
            if image != matching_edges(transformed):
                raise AssertionError("wrong matching image")

    return generators


def orbit(
    seed: Permutation,
    generators: list[tuple[str, int, int, int, int, dict[int, int]]],
) -> set[Permutation]:
    seen = {seed}
    stack = [seed]
    while stack:
        pi = stack.pop()
        for kind, a, b, parameter, d, _ in generators:
            transformed = (
                transform_type_preserving(pi, a, b, parameter, d)
                if kind == "preserving"
                else transform_type_swapping(pi, a, b, parameter, d)
            )
            if transformed not in seen:
                seen.add(transformed)
                stack.append(transformed)
    return seen


def sign_variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign != 0]
    return sum(left * right < 0 for left, right in zip(nonzero, nonzero[1:]))


def sturm_variations_at_minus_infinity(sequence: list[sp.Expr]) -> int:
    signs: list[int] = []
    for expression in sequence:
        polynomial = sp.Poly(expression, X)
        leading_sign = int(sp.sign(polynomial.LC()))
        signs.append(leading_sign * (-1 if polynomial.degree() % 2 else 1))
    return sign_variations(signs)


def sturm_variations_at(sequence: list[sp.Expr], endpoint: sp.Rational) -> int:
    signs: list[int] = []
    for expression in sequence:
        value = sp.sign(sp.Poly(expression, X).eval(endpoint))
        if value == 0:
            raise AssertionError("Sturm endpoint is a root")
        signs.append(int(value))
    return sign_variations(signs)


def roots_below(expression: sp.Expr, endpoint: sp.Rational) -> int:
    square_free = sp.Poly(expression, X).sqf_part().as_expr()
    sequence = sp.sturm(square_free, X)
    return sturm_variations_at_minus_infinity(sequence) - sturm_variations_at(
        sequence, endpoint
    )


def expected_characteristic_polynomials() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    adjacency_affine = (
        (X - 6)
        * (X - 3) ** 4
        * (X - 1) ** 4
        * (X + 2)
        * (X**4 + 2 * X**3 - 13 * X**2 - 14 * X + 29) ** 2
        * (X**4 + 2 * X**3 - 8 * X**2 - 9 * X + 19) ** 8
    )
    distance_affine = (
        (X - 106)
        * (X - 2)
        * (X - 1) ** 4
        * (X + 13) ** 4
        * (X**2 + X - 1) ** 8
        * (X**2 + 3 * X - 9) ** 8
        * (X**4 + 14 * X**3 + 13 * X**2 - 92 * X - 16) ** 2
    )
    adjacency_nonaffine = (
        (X - 6)
        * (X - 3) ** 4
        * (X - 1) ** 4
        * (X + 2)
        * (X**4 + 2 * X**3 - 8 * X**2 - 9 * X + 19) ** 2
        * (
            X**8
            + 4 * X**7
            - 17 * X**6
            - 65 * X**5
            + 116 * X**4
            + 345 * X**3
            - 423 * X**2
            - 607 * X
            + 701
        )
        ** 2
        * (
            X**8
            + 4 * X**7
            - 12 * X**6
            - 50 * X**5
            + 56 * X**4
            + 200 * X**3
            - 163 * X**2
            - 272 * X
            + 241
        )
        ** 2
    )
    distance_nonaffine = (
        (X - 1) ** 3
        * (X + 13) ** 3
        * (X**2 - 108 * X + 191)
        * (X**2 + X - 1) ** 2
        * (X**2 + 3 * X - 9) ** 2
        * (X**2 + 12 * X - 25)
        * (
            X**8
            + 8 * X**7
            - 18 * X**6
            - 80 * X**5
            + 111 * X**4
            + 200 * X**3
            - 162 * X**2
            - 136 * X
            - 19
        )
        ** 2
        * (
            X**8
            + 18 * X**7
            + 81 * X**6
            - 21 * X**5
            - 504 * X**4
            - 225 * X**3
            + 759 * X**2
            + 265 * X
            - 5
        )
        ** 2
    )
    return (
        adjacency_affine,
        distance_affine,
        adjacency_nonaffine,
        distance_nonaffine,
    )


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    generators = build_coordinate_generators()
    affine_orbit = orbit((0, 1, 2, 3, 4), generators)
    nonaffine_orbit = orbit((0, 1, 2, 4, 3), generators)

    if (
        len(affine_orbit),
        len(nonaffine_orbit),
        len(affine_orbit | nonaffine_orbit),
        len(affine_orbit & nonaffine_orbit),
    ) != (20, 100, 120, 0):
        raise AssertionError("wrong orbit census")
    affine_set = {pi for pi in ALL_PERMUTATIONS if is_affine(pi)}
    if affine_orbit != affine_set:
        raise AssertionError("wrong affine-orbit characterization")

    for pi in ALL_PERMUTATIONS:
        graph = delete_matching(pi)
        if set(map(len, graph)) != {6}:
            raise AssertionError("deletion graph is not 6-regular")
        distance = distance_rows(graph)
        if max(max(row) for row in distance) != 4:
            raise AssertionError("deletion graph does not have diameter four")
        if graph_girth(graph) != 5:
            raise AssertionError("deletion graph does not have girth five")

    affine_graph = delete_matching((0, 1, 2, 3, 4))
    nonaffine_graph = delete_matching((0, 1, 2, 4, 3))
    (
        adjacency_affine,
        distance_affine,
        adjacency_nonaffine,
        distance_nonaffine,
    ) = expected_characteristic_polynomials()

    for graph, expected_adjacency, expected_distance in (
        (affine_graph, adjacency_affine, distance_affine),
        (nonaffine_graph, adjacency_nonaffine, distance_nonaffine),
    ):
        actual_adjacency = adjacency_matrix(graph).charpoly(X).as_expr()
        actual_distance = distance_matrix(graph).charpoly(X).as_expr()
        if not sp.Poly(actual_adjacency - expected_adjacency, X).is_zero:
            raise AssertionError("wrong adjacency characteristic polynomial")
        if not sp.Poly(actual_distance - expected_distance, X).is_zero:
            raise AssertionError("wrong distance characteristic polynomial")

    if sp.Poly(adjacency_affine - adjacency_nonaffine, X).is_zero:
        raise AssertionError("the two orbit representatives are not spectrally separated")

    affine_remaining = sp.cancel(distance_affine / (X + 13) ** 4)
    if sp.Poly(affine_remaining, X).eval(-13) == 0:
        raise AssertionError("affine remaining factor also vanishes at -13")
    if roots_below(affine_remaining, sp.Integer(-13)) != 0:
        raise AssertionError("affine representative has a root below -13")

    separator = -sp.Rational(69, 5)
    if sp.Poly(distance_nonaffine, X).sqf_part().eval(separator) == 0:
        raise AssertionError("nonaffine separator is a root")
    if roots_below(distance_nonaffine, separator) != 1:
        raise AssertionError("wrong nonaffine Sturm count")
    algebraic_root = -6 - sp.sqrt(61)
    if sp.simplify(algebraic_root**2 + 12 * algebraic_root - 25) != 0:
        raise AssertionError("wrong nonaffine algebraic root")
    if not 61 * 25 > 39**2:
        raise AssertionError("wrong rational separator comparison")
    if not sp.sqrt(61) > 7:
        raise AssertionError("wrong comparison with -13")

    result = {
        "coordinate_automorphisms": len(generators),
        "matching_images_checked": len(generators) * len(ALL_PERMUTATIONS),
        "affine_class_size": len(affine_orbit),
        "nonaffine_class_size": len(nonaffine_orbit),
        "all_graphs": {
            "order": 50,
            "degree": 6,
            "girth": 5,
            "diameter": 4,
        },
        "affine_least_distance_eigenvalue": "-13",
        "affine_score": "-7",
        "nonaffine_least_distance_eigenvalue": "-6-sqrt(61)",
        "nonaffine_score": "-sqrt(61)",
        "two_isomorphism_classes": True,
    }
    print("Proof Audit 07 (layer-respecting matching deletions): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
