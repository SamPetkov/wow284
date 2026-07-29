#!/usr/bin/env python3
"""Exact exhaustive audit excluding both order-50 quotient lifts.

All spectral decisions are exact.  The Type-A search uses rational affine
solution spaces and exact Schur-complement PSD tests.  The Type-B search uses
an exact plus/minus decomposition, exact principal-minor filters, and exact
full PSD verification of every surviving completion.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import itertools
import json
import math
from typing import Iterable, Sequence

import networkx as nx
import numpy as np
import sympy as sp

TERNARY = np.array([-1, 0, 1], dtype=np.int64)


def exact_psd(matrix: np.ndarray) -> bool:
    """Exact rational Schur-complement test for a symmetric matrix."""
    a = [[Fraction(int(matrix[i, j])) for j in range(matrix.shape[1])]
         for i in range(matrix.shape[0])]
    while a:
        n = len(a)
        keep: list[int] = []
        for i in range(n):
            if a[i][i] < 0:
                return False
            if a[i][i] == 0:
                if any(a[i][j] != 0 for j in range(n)):
                    return False
            else:
                keep.append(i)
        if not keep:
            return True
        if len(keep) < n:
            a = [[a[i][j] for j in keep] for i in keep]
            n = len(a)
        pivot = a[0][0]
        column = [a[i][0] for i in range(1, n)]
        a = [
            [a[i + 1][j + 1] - column[i] * column[j] / pivot
             for j in range(n - 1)]
            for i in range(n - 1)
        ]
    return True


def permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


DET_PERMS = {
    size: [
        (permutation, permutation_sign(permutation))
        for permutation in itertools.permutations(range(size))
    ]
    for size in range(1, 6)
}


def determinant_batch(matrices: np.ndarray) -> np.ndarray:
    """Exact int64 determinants for a batch of matrices of order at most five."""
    batch, size, _ = matrices.shape
    result = np.zeros(batch, dtype=np.int64)
    rows = np.arange(size)
    for permutation, sign in DET_PERMS[size]:
        result += sign * np.prod(
            matrices[:, rows, permutation], axis=1, dtype=np.int64
        )
    return result


def principal_minor_filter(
    matrices: np.ndarray, maximum_order: int
) -> np.ndarray:
    """Return candidates whose principal minors through maximum_order are >=0."""
    active = np.ones(len(matrices), dtype=bool)
    order = matrices.shape[1]
    for size in range(1, min(maximum_order, order) + 1):
        for indices in itertools.combinations(range(order), size):
            active_indices = np.flatnonzero(active)
            if not len(active_indices):
                return active
            selection = np.array(indices)
            minors = matrices[active_indices][:, selection[:, None], selection]
            determinants = determinant_batch(minors)
            active[active_indices[determinants < 0]] = False
    return active



def determinant_exact_small(matrix: np.ndarray) -> int:
    """Fraction-free exact determinant for a small integer matrix."""
    work = [[int(value) for value in row] for row in matrix.tolist()]
    order = len(work)
    if order == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(order - 1):
        pivot_row = next(
            (row for row in range(pivot_index, order) if work[row][pivot_index] != 0),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_row], work[pivot_index] = work[pivot_index], work[pivot_row]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, order):
            for column in range(pivot_index + 1, order):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                if pivot_index:
                    assert numerator % previous == 0
                    numerator //= previous
                work[row][column] = numerator
        previous = pivot
    return sign * work[-1][-1]


def certified_minor_filter(
    matrices: np.ndarray, maximum_order: int
) -> np.ndarray:
    """Exact rejection by small negative principal minors, with numerical triage.

    Floating point is used only to nominate candidates for an exact integer
    determinant check.  A candidate is rejected only after an exact negative
    principal minor has been computed.  All unrejected candidates are later
    subjected to the full exact PSD test.
    """
    active = np.ones(len(matrices), dtype=bool)
    order = matrices.shape[1]
    for size in range(1, min(maximum_order, order) + 1):
        for indices in itertools.combinations(range(order), size):
            active_indices = np.flatnonzero(active)
            if not len(active_indices):
                return active
            selection = np.array(indices)
            minors = matrices[active_indices][:, selection[:, None], selection]
            approximate = np.linalg.det(minors.astype(float))
            suspects = np.flatnonzero(approximate < -0.25)
            for local_index in suspects:
                determinant = determinant_exact_small(minors[local_index])
                if determinant < 0:
                    active[active_indices[local_index]] = False
    return active

def upper_tuple_to_matrix(values: Sequence[int], order: int) -> np.ndarray:
    result = np.zeros((order, order), dtype=np.int8)
    position = 0
    for row in range(order):
        for column in range(row + 1, order):
            result[row, column] = result[column, row] = int(values[position])
            position += 1
    assert position == len(values)
    return result


def affine_integer_data(
    expressions: Sequence[sp.Expr], parameters: Sequence[sp.Symbol]
) -> tuple[np.ndarray, np.ndarray, int]:
    zero = {parameter: 0 for parameter in parameters}
    coefficients = [
        [sp.Rational(expression.coeff(parameter)) for parameter in parameters]
        for expression in expressions
    ]
    constants = [sp.Rational(expression.subs(zero)) for expression in expressions]
    denominators = [value.q for row in coefficients for value in row]
    denominators.extend(value.q for value in constants)
    denominator = int(sp.ilcm(*denominators)) if denominators else 1
    matrix = np.array(
        [[int(value * denominator) for value in row] for row in coefficients],
        dtype=np.int64,
    )
    vector = np.array(
        [int(value * denominator) for value in constants], dtype=np.int64
    )
    return matrix, vector, denominator


def enumerate_affine_signed(
    order: int,
    expressions: Sequence[sp.Expr],
    parameters: Sequence[sp.Symbol],
    *,
    connected_support: bool,
    chunk_size: int = 300_000,
) -> list[np.ndarray]:
    coefficient, constant, denominator = affine_integer_data(expressions, parameters)
    dimension = len(parameters)
    total = 3 ** dimension
    candidate_rows: list[np.ndarray] = []
    for start in range(0, total, chunk_size):
        stop = min(total, start + chunk_size)
        indices = np.arange(start, stop, dtype=np.int64)
        assignments = np.empty((stop - start, dimension), dtype=np.int64)
        work = indices.copy()
        for column in range(dimension):
            assignments[:, column] = TERNARY[work % 3]
            work //= 3
        numerators = assignments @ coefficient.T + constant
        admissible = np.all(
            (numerators == -denominator)
            | (numerators == 0)
            | (numerators == denominator),
            axis=1,
        )
        if np.any(admissible):
            candidate_rows.append(numerators[admissible])
    if not candidate_rows:
        return []
    rows = np.concatenate(candidate_rows, axis=0)
    signed_matrices = np.stack([
        upper_tuple_to_matrix((row // denominator).astype(int), order).astype(int)
        for row in rows
    ])
    grams = signed_matrices + 2 * np.eye(order, dtype=int)[None, :, :]
    cutoff = 4 if order <= 12 else 5
    minor_admissible = principal_minor_filter(grams, cutoff)
    output: list[np.ndarray] = []
    for signed, gram in zip(signed_matrices[minor_admissible], grams[minor_admissible]):
        if connected_support and not nx.is_connected(
            nx.from_numpy_array((signed != 0).astype(int))
        ):
            continue
        if exact_psd(gram):
            output.append(signed.astype(np.int8))
    return output

def generate_cubic_graphs_order_eight() -> list[nx.Graph]:
    """Generate all isomorphism classes of simple cubic graphs on eight vertices."""
    order, degree = 8, 3
    adjacency = [0] * order
    degrees = [0] * order
    edges: list[tuple[int, int]] = []
    representatives: list[nx.Graph] = []
    buckets: dict[str, list[int]] = defaultdict(list)

    def recurse() -> None:
        deficient = [vertex for vertex in range(order) if degrees[vertex] < degree]
        if not deficient:
            graph = nx.Graph()
            graph.add_nodes_from(range(order))
            graph.add_edges_from(edges)
            fingerprint = nx.weisfeiler_lehman_graph_hash(graph)
            if any(
                nx.is_isomorphic(graph, representatives[index])
                for index in buckets[fingerprint]
            ):
                return
            buckets[fingerprint].append(len(representatives))
            representatives.append(graph.copy())
            return

        vertex = deficient[0]
        need = degree - degrees[vertex]
        candidates = [
            other
            for other in range(vertex + 1, order)
            if degrees[other] < degree and not (adjacency[vertex] >> other) & 1
        ]
        if len(candidates) < need:
            return
        for chosen in itertools.combinations(candidates, need):
            for other in chosen:
                degrees[vertex] += 1
                degrees[other] += 1
                adjacency[vertex] |= 1 << other
                adjacency[other] |= 1 << vertex
                edges.append((vertex, other))
            feasible = True
            for current in range(vertex + 1, order):
                remaining = degree - degrees[current]
                available = sum(
                    1
                    for other in range(vertex + 1, order)
                    if other != current
                    and degrees[other] < degree
                    and not (adjacency[current] >> other) & 1
                )
                if remaining > available:
                    feasible = False
                    break
            if feasible:
                recurse()
            for other in reversed(chosen):
                edges.pop()
                adjacency[vertex] &= ~(1 << other)
                adjacency[other] &= ~(1 << vertex)
                degrees[vertex] -= 1
                degrees[other] -= 1

    recurse()
    assert len(representatives) == 6
    return representatives


def automorphisms(graph: nx.Graph) -> list[tuple[int, ...]]:
    matcher = nx.algorithms.isomorphism.GraphMatcher(graph, graph)
    return [
        tuple(mapping[vertex] for vertex in range(graph.number_of_nodes()))
        for mapping in matcher.isomorphisms_iter()
    ]


def signed_key(matrix: np.ndarray, permutation: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        int(matrix[permutation[row], permutation[column]])
        for row in range(len(permutation))
        for column in range(row + 1, len(permutation))
    )


def incidence_matrix(graph: nx.Graph) -> tuple[np.ndarray, list[tuple[int, int]]]:
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    result = np.zeros((graph.number_of_nodes(), len(edges)), dtype=int)
    for column, (left, right) in enumerate(edges):
        result[left, column] = result[right, column] = 1
    return result, edges


def induced_edge_permutation(
    edges: Sequence[tuple[int, int]], permutation: Sequence[int]
) -> tuple[int, ...]:
    lookup = {edge: index for index, edge in enumerate(edges)}
    return tuple(
        lookup[tuple(sorted((permutation[left], permutation[right])))]
        for left, right in edges
    )


def signed_commutant_affine(adjacency: np.ndarray) -> tuple[list[sp.Expr], list[sp.Symbol]]:
    order = adjacency.shape[0]
    variables: list[sp.Symbol] = []
    signed = sp.zeros(order)
    for row in range(order):
        for column in range(row + 1, order):
            variable = sp.symbols(f"s_{row}_{column}")
            variables.append(variable)
            signed[row, column] = signed[column, row] = variable
    adj = sp.Matrix(adjacency.tolist())
    equations = list(signed * adj - adj * signed)
    equations.extend(
        sum(signed[row, column] for column in range(order)) - 2
        for row in range(order)
    )
    coefficient, target = sp.linear_eq_to_matrix(equations, variables)
    expressions = next(iter(sp.linsolve((coefficient, target), variables)))
    parameters = sorted(
        set().union(*(expression.free_symbols for expression in expressions)), key=str
    )
    assert set(parameters).issubset(set(variables))
    return list(expressions), parameters


def edge_component_affine(
    incidence: np.ndarray, signed_vertices: np.ndarray
) -> tuple[list[sp.Expr], list[sp.Symbol]]:
    order = incidence.shape[1]
    variables: list[sp.Symbol] = []
    signed_edges = sp.zeros(order)
    for row in range(order):
        for column in range(row + 1, order):
            variable = sp.symbols(f"t_{row}_{column}")
            variables.append(variable)
            signed_edges[row, column] = signed_edges[column, row] = variable
    c = sp.Matrix(incidence.tolist())
    equations = list(c * signed_edges - sp.Matrix(signed_vertices.tolist()) * c)
    equations.extend(
        sum(signed_edges[row, column] for column in range(order)) - 2
        for row in range(order)
    )
    coefficient, target = sp.linear_eq_to_matrix(equations, variables)
    solution = sp.linsolve((coefficient, target), variables)
    if solution == sp.EmptySet:
        return [], []
    expressions = next(iter(solution))
    parameters = sorted(
        set().union(*(expression.free_symbols for expression in expressions)), key=str
    )
    assert set(parameters).issubset(set(variables))
    return list(expressions), parameters


def canonical_signed_representatives(
    matrices: Sequence[np.ndarray], permutations: Sequence[Sequence[int]]
) -> list[np.ndarray]:
    representatives: dict[tuple[int, ...], np.ndarray] = {}
    for matrix in matrices:
        keys = [signed_key(matrix, permutation) for permutation in permutations]
        canonical = min(keys)
        if canonical not in representatives:
            permutation = permutations[keys.index(canonical)]
            representatives[canonical] = matrix[np.ix_(permutation, permutation)].copy()
    return list(representatives.values())


def canonical_pair_key(
    signed_vertices: np.ndarray,
    signed_edges: np.ndarray,
    vertex_permutations: Sequence[Sequence[int]],
    edges: Sequence[tuple[int, int]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    keys = []
    for permutation in vertex_permutations:
        edge_permutation = induced_edge_permutation(edges, permutation)
        keys.append(
            (
                signed_key(signed_vertices, permutation),
                signed_key(signed_edges, edge_permutation),
            )
        )
    return min(keys)


def binary_intertwiner_count(signed_twelve: np.ndarray) -> tuple[int, int]:
    cycle = np.zeros((6, 6), dtype=int)
    for vertex in range(6):
        cycle[vertex, (vertex + 1) % 6] = 1
        cycle[(vertex + 1) % 6, vertex] = 1
    variables = sp.symbols("m0:72")
    matrix = sp.Matrix(6, 12, variables)
    equations = list(
        sp.Matrix(cycle.tolist()) * matrix
        - matrix * sp.Matrix(signed_twelve.tolist())
    )
    equations.extend(
        sum(matrix[row, column] for column in range(12)) - 8
        for row in range(6)
    )
    equations.extend(
        sum(matrix[row, column] for row in range(6)) - 4
        for column in range(12)
    )
    coefficient, target = sp.linear_eq_to_matrix(equations, variables)
    expressions = next(iter(sp.linsolve((coefficient, target), variables)))
    parameters = sorted(
        set().union(*(expression.free_symbols for expression in expressions)), key=str
    )
    assert set(parameters).issubset(set(variables))
    count = 0
    for values in itertools.product((0, 1), repeat=len(parameters)):
        substitution = dict(zip(parameters, values))
        entries = [sp.simplify(expression.subs(substitution)) for expression in expressions]
        if all(entry in (0, 1) for entry in entries):
            count += 1
    return len(parameters), count


def audit_type_a() -> dict[str, object]:
    graphs = generate_cubic_graphs_order_eight()
    signed_orbit_counts: list[int] = []
    pair_orbit_counts: list[int] = []
    surviving_pairs: list[tuple[nx.Graph, np.ndarray, np.ndarray]] = []

    for graph in graphs:
        adjacency = nx.to_numpy_array(graph, dtype=int)
        expressions, parameters = signed_commutant_affine(adjacency)
        signed_vertices = enumerate_affine_signed(
            8, expressions, parameters, connected_support=True
        )
        vertex_permutations = automorphisms(graph)
        signed_representatives = canonical_signed_representatives(
            signed_vertices, vertex_permutations
        )
        signed_orbit_counts.append(len(signed_representatives))

        incidence, edges = incidence_matrix(graph)
        pair_representatives: dict[
            tuple[tuple[int, ...], tuple[int, ...]], tuple[np.ndarray, np.ndarray]
        ] = {}
        for signed_eight in signed_representatives:
            edge_expressions, edge_parameters = edge_component_affine(
                incidence, signed_eight
            )
            if not edge_expressions:
                continue
            signed_twelve_list = enumerate_affine_signed(
                12,
                edge_expressions,
                edge_parameters,
                connected_support=True,
                chunk_size=100_000,
            )
            for signed_twelve in signed_twelve_list:
                key = canonical_pair_key(
                    signed_eight,
                    signed_twelve,
                    vertex_permutations,
                    edges,
                )
                pair_representatives.setdefault(key, (signed_eight, signed_twelve))
        pair_orbit_counts.append(len(pair_representatives))
        surviving_pairs.extend(
            (graph, signed_eight, signed_twelve)
            for signed_eight, signed_twelve in pair_representatives.values()
        )

    assert sorted(signed_orbit_counts) == [0, 2, 7, 15, 18, 31]
    assert pair_orbit_counts.count(1) == 1
    assert sum(pair_orbit_counts) == 1
    graph, _, signed_twelve = surviving_pairs[0]
    assert not nx.is_connected(graph)
    assert sorted(len(component) for component in nx.connected_components(graph)) == [4, 4]
    affine_dimension, binary_count = binary_intertwiner_count(signed_twelve)
    assert affine_dimension == 6
    assert binary_count == 0
    return {
        "cubic_graph_classes": 6,
        "signed_eight_orbit_counts": signed_orbit_counts,
        "signed_pair_orbit_counts": pair_orbit_counts,
        "sole_pair_cubic_graph": "K4 disjoint union K4",
        "final_binary_affine_dimension": affine_dimension,
        "final_binary_solutions": binary_count,
    }


PAIR_EDGES = [(left, right) for left in range(5) for right in range(left + 1, 5)]
PAIR_INCIDENCE = [
    [index for index, edge in enumerate(PAIR_EDGES) if vertex in edge]
    for vertex in range(5)
]


def generate_plus_labels() -> list[tuple[int, ...]]:
    labels = [0] * len(PAIR_EDGES)
    sums = [0] * 5
    output: list[tuple[int, ...]] = []

    def recurse(position: int) -> None:
        if position == len(PAIR_EDGES):
            if all(1 <= value <= 3 for value in sums):
                output.append(tuple(labels))
            return
        left, right = PAIR_EDGES[position]
        for value in (-2, -1, 0, 1, 2):
            labels[position] = value
            sums[left] += value
            sums[right] += value
            feasible = True
            for vertex in (left, right):
                remaining = sum(
                    edge_index > position for edge_index in PAIR_INCIDENCE[vertex]
                )
                if sums[vertex] - 2 * remaining > 3:
                    feasible = False
                if sums[vertex] + 2 * remaining < 1:
                    feasible = False
            if feasible:
                recurse(position + 1)
            sums[left] -= value
            sums[right] -= value

    recurse(0)
    return output


def construct_matching_symmetric_signed(
    plus_labels: Sequence[int],
    minus_labels: Sequence[int],
    matching_entries: Sequence[int],
) -> np.ndarray:
    signed = np.zeros((10, 10), dtype=np.int8)
    for pair in range(5):
        signed[2 * pair, 2 * pair + 1] = matching_entries[pair]
        signed[2 * pair + 1, 2 * pair] = matching_entries[pair]
    for plus, minus, (left, right) in zip(
        plus_labels, minus_labels, PAIR_EDGES
    ):
        same = (plus + minus) // 2
        cross = (plus - minus) // 2
        signed[2 * left, 2 * right] = signed[2 * right, 2 * left] = same
        signed[2 * left + 1, 2 * right + 1] = signed[
            2 * right + 1, 2 * left + 1
        ] = same
        signed[2 * left, 2 * right + 1] = signed[
            2 * right + 1, 2 * left
        ] = cross
        signed[2 * left + 1, 2 * right] = signed[
            2 * right, 2 * left + 1
        ] = cross
    return signed


def audit_signed_ten_components() -> tuple[list[np.ndarray], dict[str, object]]:
    plus_labels = generate_plus_labels()
    plus_matrices = np.zeros((len(plus_labels), 5, 5), dtype=np.int8)
    matching_entries: list[list[int]] = []
    for index, labels in enumerate(plus_labels):
        sums = [0] * 5
        for value, (left, right) in zip(labels, PAIR_EDGES):
            plus_matrices[index, left, right] = value
            plus_matrices[index, right, left] = value
            sums[left] += value
            sums[right] += value
        entries = [2 - value for value in sums]
        matching_entries.append(entries)
        for vertex in range(5):
            plus_matrices[index, vertex, vertex] = entries[vertex] + 2
    plus_admissible = np.flatnonzero(
        principal_minor_filter(plus_matrices.astype(np.int64), 5)
    )

    signed_matrices: list[np.ndarray] = []
    minus_trials = 0
    for index in plus_admissible:
        labels = plus_labels[index]
        entries = matching_entries[index]
        options = []
        for value in labels:
            if abs(value) == 2:
                options.append((0,))
            elif abs(value) == 1:
                options.append((-1, 1))
            else:
                options.append((-2, 0, 2))
        minus_assignments = np.array(list(itertools.product(*options)), dtype=np.int8)
        minus_trials += len(minus_assignments)
        minus_matrices = np.zeros((len(minus_assignments), 5, 5), dtype=np.int8)
        for vertex in range(5):
            minus_matrices[:, vertex, vertex] = -entries[vertex] + 2
        for edge_index, (left, right) in enumerate(PAIR_EDGES):
            minus_matrices[:, left, right] = minus_assignments[:, edge_index]
            minus_matrices[:, right, left] = minus_assignments[:, edge_index]
        admissible = np.flatnonzero(
            principal_minor_filter(minus_matrices.astype(np.int64), 5)
        )
        for candidate in admissible:
            signed = construct_matching_symmetric_signed(
                labels, minus_assignments[candidate], entries
            )
            if nx.is_connected(nx.from_numpy_array((signed != 0).astype(int))):
                signed_matrices.append(signed)

    assert len(plus_labels) == 57_464
    assert len(plus_admissible) == 632
    assert minus_trials == 3_647_592
    assert len(signed_matrices) == 1_152
    assert all(np.all(matrix >= 0) for matrix in signed_matrices)
    assert all(
        all(np.count_nonzero(matrix[vertex]) == 2 for vertex in range(10))
        for matrix in signed_matrices
    )

    intersection_classes = Counter(
        sum(matrix[2 * pair, 2 * pair + 1] == 1 for pair in range(5))
        for matrix in signed_matrices
    )
    assert intersection_classes == {0: 192, 2: 960}
    return signed_matrices, {
        "plus_labelings": len(plus_labels),
        "plus_psd_labelings": len(plus_admissible),
        "minus_labelings_tested": minus_trials,
        "signed_ten_labelings": len(signed_matrices),
        "matching_intersection_classes": {int(key): int(value) for key, value in intersection_classes.items()},
        "relative_orbits": 2,
        "underlying_signed_graph": "positive C10 in both orbits",
    }


def cycle_adjacency(order: int) -> np.ndarray:
    adjacency = np.zeros((order, order), dtype=int)
    for vertex in range(order):
        adjacency[vertex, (vertex + 1) % order] = 1
        adjacency[(vertex + 1) % order, vertex] = 1
    return adjacency


def binary_cycle_intertwiners() -> list[np.ndarray]:
    order = 10
    cycle = sp.Matrix(cycle_adjacency(order).tolist())
    variables = sp.symbols("x0:100")
    matrix = sp.Matrix(order, order, variables)
    equations = list(cycle * matrix - matrix * cycle)
    equations.extend(
        sum(matrix[row, column] for column in range(order)) - 2
        for row in range(order)
    )
    equations.extend(
        sum(matrix[row, column] for row in range(order)) - 2
        for column in range(order)
    )
    coefficient, target = sp.linear_eq_to_matrix(equations, variables)
    expressions = next(iter(sp.linsolve((coefficient, target), variables)))
    parameters = sorted(
        set().union(*(expression.free_symbols for expression in expressions)), key=str
    )
    assert len(parameters) == 17
    integer_coefficient, integer_constant, denominator = affine_integer_data(
        expressions, parameters
    )
    total = 1 << len(parameters)
    indices = np.arange(total, dtype=np.int64)
    assignments = np.empty((total, len(parameters)), dtype=np.int64)
    for column in range(len(parameters)):
        assignments[:, column] = (indices >> column) & 1
    numerators = assignments @ integer_coefficient.T + integer_constant
    admissible = np.all(
        (numerators == 0) | (numerators == denominator), axis=1
    )
    return [
        (numerator // denominator).astype(np.int8).reshape(order, order)
        for numerator in numerators[admissible]
    ]


def dihedral_permutations(order: int) -> list[tuple[int, ...]]:
    output = []
    for shift in range(order):
        output.append(tuple((vertex + shift) % order for vertex in range(order)))
        output.append(tuple((shift - vertex) % order for vertex in range(order)))
    return list(dict.fromkeys(output))


def rectangular_binary_key(
    matrix: np.ndarray,
    row_permutation: Sequence[int],
    column_permutation: Sequence[int],
) -> bytes:
    return bytes(
        int(matrix[row_permutation[row], column_permutation[column]])
        for row in range(matrix.shape[0])
        for column in range(matrix.shape[1])
    )


def canonical_cycle_intertwiners(
    matrices: Sequence[np.ndarray],
) -> list[np.ndarray]:
    permutations = dihedral_permutations(10)
    representatives: dict[bytes, np.ndarray] = {}
    for matrix in matrices:
        canonical = min(
            rectangular_binary_key(matrix, left, right)
            for left in permutations
            for right in permutations
        )
        representatives.setdefault(canonical, matrix)
    return list(representatives.values())


def completion_affine(
    left_incidence: np.ndarray, right_incidence: np.ndarray
) -> tuple[list[sp.Expr], list[sp.Symbol]]:
    order = 20
    variables: list[sp.Symbol] = []
    signed = sp.zeros(order)
    for row in range(order):
        for column in range(row + 1, order):
            variable = sp.symbols(f"u_{row}_{column}")
            variables.append(variable)
            signed[row, column] = signed[column, row] = variable
    cycle = sp.Matrix(cycle_adjacency(10).tolist())
    left = sp.Matrix(left_incidence.tolist())
    right = sp.Matrix(right_incidence.tolist())
    equations = list(left * signed - cycle * left)
    equations.extend(list(right * signed - cycle * right))
    equations.extend(
        sum(signed[row, column] for column in range(order)) - 2
        for row in range(order)
    )
    coefficient, target = sp.linear_eq_to_matrix(equations, variables)
    expressions = next(iter(sp.linsolve((coefficient, target), variables)))
    parameters = sorted(
        set().union(*(expression.free_symbols for expression in expressions)), key=str
    )
    assert set(parameters).issubset(set(variables))
    return list(expressions), parameters


def enumerate_twenty_completions(
    expressions: Sequence[sp.Expr], parameters: Sequence[sp.Symbol]
) -> tuple[int, int, list[np.ndarray]]:
    coefficient, constant, denominator = affine_integer_data(expressions, parameters)
    dimension = len(parameters)
    total = 3 ** dimension
    indices = np.arange(total, dtype=np.int64)
    assignments = np.empty((total, dimension), dtype=np.int64)
    work = indices.copy()
    for column in range(dimension):
        assignments[:, column] = TERNARY[work % 3]
        work //= 3
    numerators = assignments @ coefficient.T + constant
    entry_admissible = np.all(
        (numerators == -denominator)
        | (numerators == 0)
        | (numerators == denominator),
        axis=1,
    )
    candidate_rows = numerators[entry_admissible]
    candidates = np.stack(
        [
            upper_tuple_to_matrix((row // denominator).astype(int), 20).astype(int)
            + 2 * np.eye(20, dtype=int)
            for row in candidate_rows
        ]
    )
    minor_admissible = certified_minor_filter(candidates, 5)
    survivors: list[np.ndarray] = []
    for gram in candidates[minor_admissible]:
        if exact_psd(gram):
            survivors.append((gram - 2 * np.eye(20, dtype=int)).astype(np.int8))
    return len(candidate_rows), int(np.count_nonzero(minor_admissible)), survivors


def audit_type_b() -> dict[str, object]:
    _, signed_report = audit_signed_ten_components()
    matrices = binary_cycle_intertwiners()
    assert len(matrices) == 140
    representatives = canonical_cycle_intertwiners(matrices)
    assert len(representatives) == 6

    component_distribution = Counter()
    completion_report = []
    for matrix in representatives:
        support = nx.Graph()
        support.add_nodes_from(range(20))
        support.add_edges_from(
            (left, 10 + right)
            for left in range(10)
            for right in range(10)
            if matrix[left, right]
        )
        components = nx.number_connected_components(support)
        component_distribution[components] += 1

        edges = [
            (left, right)
            for left in range(10)
            for right in range(10)
            if matrix[left, right]
        ]
        assert len(edges) == 20
        left_incidence = np.zeros((10, 20), dtype=int)
        right_incidence = np.zeros((10, 20), dtype=int)
        for column, (left, right) in enumerate(edges):
            left_incidence[left, column] = 1
            right_incidence[right, column] = 1

        expressions, parameters = completion_affine(left_incidence, right_incidence)
        entry_count, small_minor_count, completions = enumerate_twenty_completions(
            expressions, parameters
        )
        assert len(completions) == 1
        completion = completions[0]
        assert np.all(completion >= 0)
        completion_support = nx.from_numpy_array((completion != 0).astype(int))
        sizes = sorted(
            len(component) for component in nx.connected_components(completion_support)
        )
        assert sizes == [10, 10]
        assert all(
            completion_support.degree(vertex) == 2
            for vertex in completion_support.nodes()
        )
        completion_report.append(
            {
                "bipartite_support_components": components,
                "affine_dimension": len(parameters),
                "entry_admissible": entry_count,
                "survive_minors_through_order_5": small_minor_count,
                "exact_psd_completions": len(completions),
                "completion_support": sizes,
            }
        )

    assert component_distribution == {1: 2, 2: 2, 5: 2}
    assert sorted(item["affine_dimension"] for item in completion_report) == [
        0, 0, 1, 1, 10, 10
    ]
    return {
        "signed_ten_components": signed_report,
        "binary_cycle_intertwiners": len(matrices),
        "dihedral_orbits": len(representatives),
        "support_component_distribution": dict(component_distribution),
        "completion_audits": completion_report,
        "conclusion": "every exact PSD completion is positive C10 disjoint union C10",
    }


def main() -> None:
    import sys

    if len(sys.argv) == 2 and sys.argv[1] in {"--type-a", "--type-b"}:
        report = audit_type_a() if sys.argv[1] == "--type-a" else audit_type_b()
        label = "Type A" if sys.argv[1] == "--type-a" else "Type B"
        print(f"order-50 lift exclusion {label}: PASS")
        print("RESULT_JSON=" + json.dumps(report, sort_keys=True))
        return

    raise SystemExit(
        "usage: verify_order50_lift_exclusion.py --type-a | --type-b"
    )


if __name__ == "__main__":
    main()
