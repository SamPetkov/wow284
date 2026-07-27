#!/usr/bin/env python3
"""Independent exact audit of Hoffman--Singleton deletion robustness radius five."""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from sympy.combinatorics import Permutation, PermutationGroup

MODULUS = 5
ORDER = 50
Graph = tuple[frozenset[int], ...]
PermutationTuple = tuple[int, ...]
Subset = tuple[int, ...]


def p(i: int, j: int) -> int:
    return 5 * (i % MODULUS) + (j % MODULUS)


def q(k: int, ell: int) -> int:
    return 25 + 5 * (k % MODULUS) + (ell % MODULUS)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(ORDER)]

    def add(u: int, v: int) -> None:
        if u == v:
            raise AssertionError("loop")
        rows[u].add(v)
        rows[v].add(u)

    for i in range(MODULUS):
        for j in range(MODULUS):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for k in range(MODULUS):
                add(p(i, j), q(k, i * k + j))
    graph = tuple(frozenset(row) for row in rows)
    if set(map(len, graph)) != {7}:
        raise AssertionError("bad degree")
    return graph


FULL = hoffman_singleton()
FULL_EDGES = frozenset(
    (u, v) for u in range(ORDER) for v in FULL[u] if u < v
)


def permutation_from_cycles(
    cycles: tuple[tuple[int, ...], ...]
) -> PermutationTuple:
    image = list(range(ORDER))
    for cycle_one_based in cycles:
        cycle = tuple(value - 1 for value in cycle_one_based)
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            image[source] = target
    if sorted(image) != list(range(ORDER)):
        raise AssertionError("invalid permutation")
    return tuple(image)


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
STANDARD_TO_COORDINATE: PermutationTuple = (
    0, 39, 44, 3, 34, 49, 42, 48, 36, 30,
    5, 8, 43, 32, 15, 18, 46, 35, 20, 45,
    33, 41, 23, 37, 40, 10, 31, 38, 47, 13,
    21, 6, 1, 16, 11, 28, 25, 7, 22, 2,
    12, 17, 4, 9, 19, 24, 14, 26, 27, 29,
)


def inverse(permutation: PermutationTuple) -> PermutationTuple:
    output = [0] * ORDER
    for source, target in enumerate(permutation):
        output[target] = source
    return tuple(output)


def apply_pair(
    permutation: PermutationTuple, pair: tuple[int, int]
) -> tuple[int, int]:
    return tuple(sorted((permutation[pair[0]], permutation[pair[1]])))


def pair_orbit(
    seed: tuple[int, int], generators: tuple[PermutationTuple, ...]
) -> set[tuple[int, int]]:
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


def conjugate_to_coordinates(
    permutation: PermutationTuple,
) -> PermutationTuple:
    relabel_inverse = inverse(STANDARD_TO_COORDINATE)
    return tuple(
        STANDARD_TO_COORDINATE[permutation[relabel_inverse[x]]]
        for x in range(ORDER)
    )


def verified_generators() -> tuple[PermutationTuple, ...]:
    standard = (
        STANDARD_G1,
        STANDARD_G2,
        inverse(STANDARD_G1),
        inverse(STANDARD_G2),
    )
    standard_edges = pair_orbit((0, 9), standard)
    if len(standard_edges) != 175:
        raise AssertionError("standard edge orbit does not have 175 edges")
    relabelled = frozenset(
        tuple(sorted((STANDARD_TO_COORDINATE[u], STANDARD_TO_COORDINATE[v])))
        for u, v in standard_edges
    )
    if relabelled != FULL_EDGES:
        raise AssertionError("fixed relabeling does not recover the coordinate graph")
    generators = tuple(conjugate_to_coordinates(item) for item in standard)
    for generator in generators:
        image_edges = frozenset(
            tuple(sorted((generator[u], generator[v])))
            for u, v in FULL_EDGES
        )
        if image_edges != FULL_EDGES:
            raise AssertionError("generator is not a graph automorphism")
    group = PermutationGroup(
        Permutation(list(generators[0])),
        Permutation(list(generators[1])),
    )
    if group.order() != 252000:
        raise AssertionError("unexpected generated group order")
    return generators


GENERATORS = verified_generators()


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
    total = comb(ORDER, size)
    visited = bytearray(total)
    representatives: list[Subset] = []
    orbit_sizes: list[int] = []
    for subset in combinations(range(ORDER), size):
        rank = rank_colex(subset)
        if visited[rank]:
            continue
        orbit = subset_orbit(subset)
        representatives.append(subset)
        orbit_sizes.append(len(orbit))
        for image in orbit:
            visited[rank_colex(image)] = 1
    if sum(orbit_sizes) != total or not all(visited):
        raise AssertionError("subset orbit exhaustion failed")
    return representatives, orbit_sizes


def induced_graph(deleted: Subset) -> tuple[Graph, tuple[int, ...]]:
    deleted_set = set(deleted)
    surviving = tuple(v for v in range(ORDER) if v not in deleted_set)
    index = {v: i for i, v in enumerate(surviving)}
    graph = tuple(
        frozenset(index[w] for w in FULL[v] if w not in deleted_set)
        for v in surviving
    )
    return graph, surviving


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
            raise AssertionError("punctured graph is disconnected")
        output.append(tuple(distance))
    return tuple(output)


def minimum_dual_degree(graph: Graph) -> Fraction:
    degrees = tuple(map(len, graph))
    return min(
        Fraction(sum(degrees[w] for w in graph[v]), degrees[v])
        for v in range(len(graph))
    )


def verify_distance_normal_form(
    deleted: Subset,
    surviving: tuple[int, ...],
    graph: Graph,
    distances: tuple[tuple[int, ...], ...],
) -> None:
    deleted_set = set(deleted)
    for i, x in enumerate(surviving):
        for j, y in enumerate(surviving):
            if i == j:
                expected = 0
            elif y in FULL[x]:
                expected = 1
            else:
                expected = 2 + len((FULL[x] & FULL[y]) & deleted_set)
            if distances[i][j] != expected:
                raise AssertionError("small-puncture normal form failed")


def fraction_ldl(
    matrix: list[list[int]],
) -> tuple[list[list[Fraction]], list[Fraction]]:
    order = len(matrix)
    lower = [[Fraction(0) for _ in range(order)] for _ in range(order)]
    diagonal = [Fraction(0) for _ in range(order)]
    for i in range(order):
        lower[i][i] = Fraction(1)
    for j in range(order):
        pivot = Fraction(matrix[j][j])
        for r in range(j):
            pivot -= lower[j][r] * lower[j][r] * diagonal[r]
        if pivot == 0:
            raise AssertionError(f"zero LDL pivot at {j}")
        diagonal[j] = pivot
        for i in range(j + 1, order):
            value = Fraction(matrix[i][j])
            for r in range(j):
                value -= lower[i][r] * lower[j][r] * diagonal[r]
            lower[i][j] = value / pivot

    for i in range(order):
        for j in range(order):
            reconstructed = Fraction(0)
            for r in range(min(i, j) + 1):
                reconstructed += lower[i][r] * diagonal[r] * lower[j][r]
            if reconstructed != matrix[i][j]:
                raise AssertionError("Fraction LDL reconstruction failed")
    return lower, diagonal


def audit_representative(
    deleted: Subset, *, positive: bool
) -> dict[str, object]:
    graph, surviving = induced_graph(deleted)
    distances = distance_rows(graph)
    size = len(deleted)
    if max(map(max, distances)) > 3:
        raise AssertionError("small puncture has diameter above three")
    expected_dual = Fraction(49 - size, 7)
    if minimum_dual_degree(graph) != expected_dual:
        raise AssertionError("minimum dual degree mismatch")
    verify_distance_normal_form(deleted, surviving, graph, distances)

    order = len(graph)
    shifted = [
        [
            7 * distances[i][j] + ((49 - size) if i == j else 0)
            for j in range(order)
        ]
        for i in range(order)
    ]
    _, pivots = fraction_ldl(shifted)
    negative = sum(pivot < 0 for pivot in pivots)
    if positive:
        if negative or any(pivot <= 0 for pivot in pivots):
            raise AssertionError("expected positive-definite shifted matrix")
    elif negative != 1:
        raise AssertionError("six-deletion witness needs exactly one negative pivot")
    return {
        "deleted": list(deleted),
        "order": order,
        "minimum_dual_degree": str(expected_dual),
        "negative_pivots": negative,
        "zero_pivots": sum(pivot == 0 for pivot in pivots),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    expected_counts = {0: 1, 1: 1, 2: 2, 3: 4, 4: 11, 5: 33}
    observed: dict[int, int] = {}
    checked = 0
    audit_representative((), positive=True)
    observed[0] = 1
    checked += 1
    for size in range(1, 6):
        representatives, orbit_sizes = orbit_representatives(size)
        if len(representatives) != expected_counts[size]:
            raise AssertionError("unexpected orbit count")
        if sum(orbit_sizes) != comb(ORDER, size):
            raise AssertionError("orbit sizes do not cover all labelled subsets")
        observed[size] = len(representatives)
        for deleted in representatives:
            audit_representative(deleted, positive=True)
            checked += 1

    witness = tuple(sorted((
        p(2, 4), p(3, 1), p(3, 4), q(2, 1), q(3, 4), q(4, 4)
    )))
    witness_result = audit_representative(witness, positive=False)
    result = {
        "generated_automorphism_group_order": 252000,
        "orbit_counts": observed,
        "positive_representatives_checked": checked,
        "six_vertex_failure": witness_result,
        "universal_robustness_radius": 5,
    }
    print("Proof Audit 13 (Hoffman--Singleton robustness radius): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
