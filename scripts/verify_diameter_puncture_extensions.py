#!/usr/bin/env python3
"""Exact verification of the diameter and Moore-puncture extensions.

The analytic theorems are checked symbolically.  The Hoffman--Singleton
robustness theorem is checked orbit-by-orbit under two explicit verified
50-point automorphisms.  Every asserted spectral sign uses exact rational
LDL^T decomposition; no floating-point eigenvalue ordering is used.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
from math import comb

import sympy as sp

Q = 5
N = 50
Graph = tuple[frozenset[int], ...]
Permutation = tuple[int, ...]
Subset = tuple[int, ...]


def p(i: int, j: int) -> int:
    return 5 * (i % Q) + (j % Q)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % Q) + (ell % Q)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(N)]

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
FULL_EDGES = frozenset(
    (u, v) for u in range(N) for v in FULL[u] if u < v
)


def permutation_from_cycles(cycles: tuple[tuple[int, ...], ...]) -> Permutation:
    """Return a zero-based permutation from one-based disjoint cycles."""

    image = list(range(N))
    for cycle_one_based in cycles:
        cycle = tuple(value - 1 for value in cycle_one_based)
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            image[source] = target
    if sorted(image) != list(range(N)):
        raise AssertionError("cycle data do not define a permutation")
    return tuple(image)


def inverse(permutation: Permutation) -> Permutation:
    output = [0] * N
    for source, target in enumerate(permutation):
        output[target] = source
    return tuple(output)


# Standard 50-point generators.  Correctness is not assumed from provenance:
# the verifier reconstructs their 175-edge pair orbit, checks a fixed
# relabelling to the coordinate graph above, and then checks the conjugated
# permutations edge-by-edge.
STANDARD_G1 = permutation_from_cycles((
    (1, 44, 22, 49, 17, 43, 9, 46, 40, 45),
    (2, 23, 24, 14, 18, 10, 12, 42, 38, 6),
    (3, 41, 19, 4, 15, 20, 7, 13, 37, 8),
    (5, 28, 21, 29, 16, 25, 11, 26, 39, 30),
    (27, 47),
    (31, 36, 34, 32, 35),
    (33, 50),
))
STANDARD_G2 = permutation_from_cycles((
    (1, 7, 48, 47, 41, 46, 17),
    (2, 39, 11, 4, 15, 14, 42),
    (3, 32, 28, 9, 23, 6, 43),
    (5, 22, 38, 18, 44, 36, 29),
    (8, 37, 40, 34, 26, 49, 24),
    (10, 16, 31, 27, 13, 21, 45),
    (19, 33, 25, 35, 50, 30, 20),
))

# Fixed isomorphism from the graph generated as the pair orbit of {0,9}
# under STANDARD_G1, STANDARD_G2 to the P/Q coordinate labelling.
STANDARD_TO_COORDINATE: Permutation = (
    0, 39, 44, 3, 34, 49, 42, 48, 36, 30,
    5, 8, 43, 32, 15, 18, 46, 35, 20, 45,
    33, 41, 23, 37, 40, 10, 31, 38, 47, 13,
    21, 6, 1, 16, 11, 28, 25, 7, 22, 2,
    12, 17, 4, 9, 19, 24, 14, 26, 27, 29,
)


def apply_pair(permutation: Permutation, pair: tuple[int, int]) -> tuple[int, int]:
    return tuple(sorted((permutation[pair[0]], permutation[pair[1]])))


def pair_orbit(seed: tuple[int, int], generators: tuple[Permutation, ...]) -> set[tuple[int, int]]:
    start = tuple(sorted(seed))
    seen = {start}
    pending = [start]
    while pending:
        pair = pending.pop()
        for generator in generators:
            image = apply_pair(generator, pair)
            if image not in seen:
                seen.add(image)
                pending.append(image)
    return seen


def conjugate_to_coordinates(permutation: Permutation) -> Permutation:
    relabel = STANDARD_TO_COORDINATE
    relabel_inverse = inverse(relabel)
    return tuple(relabel[permutation[relabel_inverse[x]]] for x in range(N))


def verify_generators() -> tuple[Permutation, ...]:
    standard_generators = (
        STANDARD_G1,
        STANDARD_G2,
        inverse(STANDARD_G1),
        inverse(STANDARD_G2),
    )
    standard_edges = pair_orbit((0, 9), standard_generators)
    if len(standard_edges) != 175:
        raise AssertionError("standard pair orbit does not have 175 edges")
    relabelled_edges = frozenset(
        tuple(sorted((STANDARD_TO_COORDINATE[u], STANDARD_TO_COORDINATE[v])))
        for u, v in standard_edges
    )
    if relabelled_edges != FULL_EDGES:
        raise AssertionError("fixed relabelling does not recover coordinate HS")

    generators = tuple(
        conjugate_to_coordinates(permutation)
        for permutation in standard_generators
    )
    for generator in generators:
        if sorted(generator) != list(range(N)):
            raise AssertionError("conjugated map is not bijective")
        image_edges = frozenset(
            tuple(sorted((generator[u], generator[v]))) for u, v in FULL_EDGES
        )
        if image_edges != FULL_EDGES:
            raise AssertionError("conjugated map is not an automorphism")
    return generators


GENERATORS = verify_generators()


def rank_colex(subset: Subset) -> int:
    return sum(comb(value, index + 1) for index, value in enumerate(subset))


def subset_orbit(seed: Subset) -> set[Subset]:
    seen = {seed}
    pending = [seed]
    while pending:
        subset = pending.pop()
        for generator in GENERATORS:
            image = tuple(sorted(generator[value] for value in subset))
            if image not in seen:
                seen.add(image)
                pending.append(image)
    return seen


def orbit_representatives(size: int) -> tuple[list[Subset], list[int]]:
    total = comb(N, size)
    visited = bytearray(total)
    representatives: list[Subset] = []
    orbit_sizes: list[int] = []
    for subset in combinations(range(N), size):
        rank = rank_colex(subset)
        if visited[rank]:
            continue
        orbit = subset_orbit(subset)
        representatives.append(subset)
        orbit_sizes.append(len(orbit))
        for image in orbit:
            visited[rank_colex(image)] = 1
    if sum(orbit_sizes) != total or not all(visited):
        raise AssertionError("subset orbits do not exhaust all labelled subsets")
    return representatives, orbit_sizes


def induced_graph(deleted: Subset) -> tuple[Graph, tuple[int, ...]]:
    deleted_set = set(deleted)
    surviving = tuple(vertex for vertex in range(N) if vertex not in deleted_set)
    index = {vertex: position for position, vertex in enumerate(surviving)}
    graph = tuple(
        frozenset(index[neighbor] for neighbor in FULL[vertex] if neighbor not in deleted_set)
        for vertex in surviving
    )
    return graph, surviving


def distance_matrix(graph: Graph) -> tuple[tuple[int, ...], ...]:
    rows: list[tuple[int, ...]] = []
    for source in range(len(graph)):
        distances = [-1] * len(graph)
        distances[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[vertex] + 1
                    queue.append(neighbor)
        if -1 in distances:
            raise AssertionError("punctured graph is disconnected")
        rows.append(tuple(distances))
    return tuple(rows)


def minimum_dual_degree(graph: Graph) -> Fraction:
    degrees = tuple(len(row) for row in graph)
    values = tuple(
        Fraction(sum(degrees[neighbor] for neighbor in graph[vertex]), degrees[vertex])
        for vertex in range(len(graph))
    )
    return min(values)


def verify_distance_correction(
    deleted: Subset,
    surviving: tuple[int, ...],
    graph: Graph,
    distances: tuple[tuple[int, ...], ...],
) -> None:
    order = len(graph)
    adjacency = sp.Matrix([
        [int(column in graph[row]) for column in range(order)]
        for row in range(order)
    ])
    incidence = sp.Matrix([
        [int(deleted_vertex in FULL[vertex]) for deleted_vertex in deleted]
        for vertex in surviving
    ])
    gram = incidence * incidence.T
    correction = gram - sp.diag(*[gram[i, i] for i in range(order)])
    expected = 2 * (sp.ones(order) - sp.eye(order)) - adjacency + correction
    if sp.Matrix(distances) != expected:
        raise AssertionError("small-puncture distance correction failed")


def exact_ldl_signs(matrix: sp.Matrix, *, positive: bool) -> tuple[sp.Expr, ...]:
    lower, diagonal = matrix.LDLdecomposition(hermitian=positive)
    if lower * diagonal * lower.T != matrix:
        raise AssertionError("exact LDL reconstruction failed")
    pivots = tuple(sp.factor(diagonal[i, i]) for i in range(matrix.rows))
    if positive:
        if not all(bool(pivot > 0) for pivot in pivots):
            raise AssertionError("expected a positive-definite shifted matrix")
    else:
        if any(pivot == 0 for pivot in pivots):
            raise AssertionError("indefinite witness has a zero LDL pivot")
        if not any(bool(pivot < 0) for pivot in pivots):
            raise AssertionError("expected a negative LDL pivot")
    return pivots


def verify_symbolic_diameter_bounds() -> None:
    delta, alpha, beta, t = sp.symbols(
        "delta alpha beta t", nonnegative=True
    )
    p_degree = delta + alpha
    q_degree = delta + beta
    radicand = (p_degree - q_degree) ** 2 + p_degree * q_degree * t**2
    target = p_degree + q_degree + delta * (t - 2)
    expected = (t - 2) * (
        delta * t * (alpha + beta) + (t + 2) * alpha * beta
    )
    if sp.expand(sp.factor(radicand - target**2) - expected) != 0:
        raise AssertionError("endpoint-neighborhood radical identity failed")

    k = sp.symbols("k", positive=True)
    diameter_four_matrix = sp.Matrix([
        [-4, -2 * sp.sqrt(k)],
        [-2 * sp.sqrt(k), -3],
    ])
    x = sp.symbols("x")
    if sp.expand(diameter_four_matrix.charpoly(x).as_expr() - (x**2 + 7*x + 12 - 4*k)) != 0:
        raise AssertionError("diameter-four quotient polynomial failed")
    if sp.factor(7**2 - 4 * (12 - 4*k)) != 16*k + 1:
        raise AssertionError("diameter-four discriminant failed")

    for degree in range(2, 10):
        left = 2 * degree - 7
        if left <= 0:
            continue
        if left * left >= 16 * degree + 1:
            raise AssertionError("degree-at-most-nine diameter-four exclusion failed")


def verify_hoffman_singleton_robustness() -> dict[int, int]:
    expected_orbit_counts = {1: 1, 2: 2, 3: 4, 4: 11, 5: 33}
    observed: dict[int, int] = {}
    for size in range(1, 6):
        representatives, orbit_sizes = orbit_representatives(size)
        observed[size] = len(representatives)
        if observed[size] != expected_orbit_counts[size]:
            raise AssertionError((size, observed[size], expected_orbit_counts[size]))
        if sum(orbit_sizes) != comb(N, size):
            raise AssertionError("orbit-size sum failed")

        for deleted in representatives:
            graph, surviving = induced_graph(deleted)
            distances = distance_matrix(graph)
            if max(max(row) for row in distances) > 3:
                raise AssertionError("small puncture has diameter greater than three")
            expected_dual = Fraction(49 - size, 7)
            if minimum_dual_degree(graph) != expected_dual:
                raise AssertionError("small-puncture dual-degree formula failed")
            verify_distance_correction(deleted, surviving, graph, distances)
            shifted = 7 * sp.Matrix(distances) + (49 - size) * sp.eye(N - size)
            exact_ldl_signs(shifted, positive=True)

    deleted_six = (
        p(2, 4),
        p(3, 1),
        p(3, 4),
        q(2, 1),
        q(3, 4),
        q(4, 4),
    )
    graph, surviving = induced_graph(deleted_six)
    distances = distance_matrix(graph)
    if minimum_dual_degree(graph) != Fraction(43, 7):
        raise AssertionError("six-puncture dual degree failed")
    verify_distance_correction(deleted_six, surviving, graph, distances)
    shifted = 7 * sp.Matrix(distances) + 43 * sp.eye(44)
    pivots = exact_ldl_signs(shifted, positive=False)
    if sum(bool(pivot < 0) for pivot in pivots) != 1:
        raise AssertionError("expected exactly one negative shifted eigenvalue")
    return observed


def main() -> None:
    verify_symbolic_diameter_bounds()
    orbit_counts = verify_hoffman_singleton_robustness()
    print("diameter and puncture extension verification: PASS")
    print("endpoint-neighborhood bound: symbolic identity PASS")
    print("diameter-four degree-at-most-nine exclusion: PASS")
    print(f"Hoffman--Singleton deletion orbit counts: {orbit_counts}")
    print("all deletions of at most five vertices: exact strict counterexamples")
    print("explicit six-vertex deletion: exact negative shifted LDL pivot")
    print("universal Hoffman--Singleton deletion robustness radius: 5")


if __name__ == "__main__":
    main()
