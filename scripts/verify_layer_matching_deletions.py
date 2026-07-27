#!/usr/bin/env python3
"""Exact classification of 120 layer-respecting matching deletions of HS.

For every permutation pi of F_5, delete the perfect matching

    P_(i,j) -- Q_(pi(i), i*pi(i)+j).

The script proves, without floating point, that the resulting 120 graphs split
into two explicit coordinate-automorphism orbits, computes one exact adjacency
and distance characteristic polynomial per orbit, and certifies the least
distance eigenvalue in each case.
"""
from __future__ import annotations

from collections import deque
from itertools import permutations
import json

import sympy as sp

Q = 5
X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]
Permutation = tuple[int, ...]


def p(i: int, j: int) -> int:
    return 5 * (i % Q) + (j % Q)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % Q) + (ell % Q)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def add(u: int, v: int) -> None:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(Q):
        for j in range(Q):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(Q):
                add(p(i, j), q(k, i * k + j))
    graph = tuple(frozenset(row) for row in rows)
    if set(map(len, graph)) != {7}:
        raise AssertionError("bad Hoffman--Singleton degree")
    return graph


FULL = hoffman_singleton()
ALL_PERMUTATIONS = tuple(permutations(range(Q)))


def matching_edges(pi: Permutation) -> frozenset[tuple[int, int]]:
    return frozenset(
        tuple(sorted((p(i, j), q(pi[i], i * pi[i] + j))))
        for i in range(Q)
        for j in range(Q)
    )


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


def is_affine(pi: Permutation) -> bool:
    return any(
        all(pi[i] == (a * i + b) % Q for i in range(Q))
        for a in range(1, Q)
        for b in range(Q)
    )


# Type-preserving coordinate automorphisms.  Here ac=s in F_5.
def type_preserving_map(a: int, b: int, s: int, d: int) -> dict[int, int]:
    c = s * pow(a, -1, Q) % Q
    image: dict[int, int] = {}
    for i in range(Q):
        for j in range(Q):
            image[p(i, j)] = p(a * i + b, s * j - a * d * i - b * d)
    for k in range(Q):
        for ell in range(Q):
            image[q(k, ell)] = q(c * k + d, s * ell + b * c * k)
    return image


# Type-swapping coordinate automorphisms.  Here ac=-t in F_5.
def type_swapping_map(a: int, b: int, t: int, d: int) -> dict[int, int]:
    c = (-t) * pow(a, -1, Q) % Q
    image: dict[int, int] = {}
    for i in range(Q):
        for j in range(Q):
            image[p(i, j)] = q(a * i + b, t * j + d * a * i + d * b)
    for k in range(Q):
        for ell in range(Q):
            image[q(k, ell)] = p(c * k + d, t * ell - c * b * k)
    return image


def transform_type_preserving(
    pi: Permutation, a: int, b: int, s: int, d: int
) -> Permutation:
    c = s * pow(a, -1, Q) % Q
    output: list[int | None] = [None] * Q
    for i in range(Q):
        output[(a * i + b) % Q] = (c * pi[i] + d) % Q
    if any(value is None for value in output):
        raise AssertionError("incomplete transformed permutation")
    return tuple(int(value) for value in output)


def transform_type_swapping(
    pi: Permutation, a: int, b: int, t: int, d: int
) -> Permutation:
    c = (-t) * pow(a, -1, Q) % Q
    output: list[int | None] = [None] * Q
    for i in range(Q):
        output[(c * pi[i] + d) % Q] = (a * i + b) % Q
    if any(value is None for value in output):
        raise AssertionError("incomplete transformed permutation")
    return tuple(int(value) for value in output)


def verify_graph_automorphism(mapping: dict[int, int]) -> None:
    if len(set(mapping.values())) != 50:
        raise AssertionError("coordinate map is not bijective")
    original = frozenset(
        (u, v) for u in range(50) for v in FULL[u] if u < v
    )
    image = frozenset(
        tuple(sorted((mapping[u], mapping[v])))
        for u in range(50)
        for v in FULL[u]
        if u < v
    )
    if image != original:
        raise AssertionError("coordinate map does not preserve HS adjacency")


def verify_matching_image(
    pi: Permutation, mapping: dict[int, int], transformed: Permutation
) -> None:
    image = frozenset(
        tuple(sorted((mapping[u], mapping[v]))) for u, v in matching_edges(pi)
    )
    if image != matching_edges(transformed):
        raise AssertionError("matching image does not match transformed permutation")


def orbit(seed: Permutation) -> set[Permutation]:
    seen = {seed}
    pending = [seed]
    while pending:
        pi = pending.pop()
        for a in range(1, Q):
            for b in range(Q):
                for d in range(Q):
                    for s in (1, Q - 1):
                        transformed = transform_type_preserving(pi, a, b, s, d)
                        if transformed not in seen:
                            seen.add(transformed)
                            pending.append(transformed)
                    for t in (2, 3):
                        transformed = transform_type_swapping(pi, a, b, t, d)
                        if transformed not in seen:
                            seen.add(transformed)
                            pending.append(transformed)
    return seen


def verify_two_orbits() -> tuple[set[Permutation], set[Permutation]]:
    maps: list[tuple[dict[int, int], object]] = []
    for a in range(1, Q):
        for b in range(Q):
            for d in range(Q):
                for s in (1, Q - 1):
                    mapping = type_preserving_map(a, b, s, d)
                    verify_graph_automorphism(mapping)
                    maps.append(
                        (
                            mapping,
                            lambda pi, a=a, b=b, s=s, d=d: (
                                transform_type_preserving(pi, a, b, s, d)
                            ),
                        )
                    )
                for t in (2, 3):
                    mapping = type_swapping_map(a, b, t, d)
                    verify_graph_automorphism(mapping)
                    maps.append(
                        (
                            mapping,
                            lambda pi, a=a, b=b, t=t, d=d: (
                                transform_type_swapping(pi, a, b, t, d)
                            ),
                        )
                    )

    # Finite adversarial check: every displayed coordinate automorphism sends
    # every one of the 120 matchings to exactly the predicted matching.
    for pi in ALL_PERMUTATIONS:
        for mapping, transform in maps:
            verify_matching_image(pi, mapping, transform(pi))

    affine_orbit = orbit((0, 1, 2, 3, 4))
    nonaffine_orbit = orbit((0, 1, 2, 4, 3))
    if len(affine_orbit) != 20 or len(nonaffine_orbit) != 100:
        raise AssertionError("unexpected orbit sizes")
    if not affine_orbit.isdisjoint(nonaffine_orbit):
        raise AssertionError("orbits overlap")
    if affine_orbit | nonaffine_orbit != set(ALL_PERMUTATIONS):
        raise AssertionError("orbits do not exhaust S_5")
    if not all(is_affine(pi) for pi in affine_orbit):
        raise AssertionError("affine orbit contains a nonaffine permutation")
    if any(is_affine(pi) for pi in nonaffine_orbit):
        raise AssertionError("nonaffine orbit contains an affine permutation")
    return affine_orbit, nonaffine_orbit


def representative_polynomials() -> dict[str, dict[str, object]]:
    expected: dict[str, dict[str, object]] = {
        "affine": {
            "pi": (0, 1, 2, 3, 4),
            "chi_a": (X - 6)
            * (X - 3) ** 4
            * (X - 1) ** 4
            * (X + 2)
            * (X**4 + 2 * X**3 - 13 * X**2 - 14 * X + 29) ** 2
            * (X**4 + 2 * X**3 - 8 * X**2 - 9 * X + 19) ** 8,
            "chi_d": (X - 106)
            * (X - 2)
            * (X - 1) ** 4
            * (X + 13) ** 4
            * (X**2 + X - 1) ** 8
            * (X**2 + 3 * X - 9) ** 8
            * (X**4 + 14 * X**3 + 13 * X**2 - 92 * X - 16) ** 2,
            "least": "-13",
        },
        "nonaffine": {
            "pi": (0, 1, 2, 4, 3),
            "chi_a": (X - 6)
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
            ** 2,
            "chi_d": (X - 1) ** 3
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
            ** 2,
            "least": "-6-sqrt(61)",
        },
    }

    result: dict[str, dict[str, object]] = {}
    for name, data in expected.items():
        pi = data["pi"]
        if not isinstance(pi, tuple):
            raise AssertionError("bad representative")
        graph = delete_matching(pi)
        if set(map(len, graph)) != {6}:
            raise AssertionError("representative is not 6-regular")
        if graph_girth(graph) != 5:
            raise AssertionError("representative girth is not five")
        distances = distance_rows(graph)
        if max(max(row) for row in distances) != 4:
            raise AssertionError("representative diameter is not four")

        adjacency = adjacency_matrix(graph)
        distance = sp.Matrix(distances)
        chi_a = sp.factor(adjacency.charpoly(X).as_expr())
        chi_d = sp.factor(distance.charpoly(X).as_expr())
        if not sp.Poly(chi_a - data["chi_a"], X).is_zero:
            raise AssertionError(f"wrong adjacency polynomial for {name}")
        if not sp.Poly(chi_d - data["chi_d"], X).is_zero:
            raise AssertionError(f"wrong distance polynomial for {name}")

        if name == "affine":
            other = sp.cancel(chi_d / (X + 13) ** 4)
            other_poly = sp.Poly(other, X)
            if other_poly.eval(-13) == 0:
                raise AssertionError("unexpected extra -13 factor")
            if other_poly.count_roots(-sp.oo, -13) != 0:
                raise AssertionError("affine representative has a root below -13")
        else:
            separator = -sp.Rational(69, 5)
            square_free = sp.Poly(chi_d, X).sqf_part()
            if square_free.eval(separator) == 0:
                raise AssertionError("Sturm separator is a root")
            if square_free.count_roots(-sp.oo, separator) != 1:
                raise AssertionError("nonaffine least-root isolation failed")
            if not 61 > sp.Rational(39, 5) ** 2:
                raise AssertionError("bad radical comparison")
            if not -6 - sp.sqrt(61) < separator:
                raise AssertionError("candidate root is not below separator")

        result[name] = {
            "representative_permutation": list(pi),
            "order": 50,
            "degree": 6,
            "girth": 5,
            "diameter": 4,
            "minimum_dual_degree": 6,
            "least_distance_eigenvalue": data["least"],
            "adjacency_characteristic_polynomial": str(chi_a),
            "distance_characteristic_polynomial": str(chi_d),
        }
    return result


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    affine_orbit, nonaffine_orbit = verify_two_orbits()
    result = {
        "family": {
            "total_matchings": 120,
            "affine_orbit_size": len(affine_orbit),
            "nonaffine_orbit_size": len(nonaffine_orbit),
            "classification": "20 affine permutations and 100 nonaffine permutations",
        },
        "representatives": representative_polynomials(),
        "conclusion": (
            "Every graph in this explicit 120-member family is a strict negative "
            "control for WOW-284: delta*=6 and lambda_min(D)<=-13."
        ),
    }
    print("layer-respecting matching-deletion verification: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
