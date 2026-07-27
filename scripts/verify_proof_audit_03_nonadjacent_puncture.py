#!/usr/bin/env python3
"""Independent exact audit of the nonadjacent Moore-puncture spectrum.

This script does not import either original puncture verifier.  It checks the
metric replacement paths, quotient, incidence identities, invariant direct sum,
full characteristic polynomial, dual degrees, and an exact positive-definite
shift for the punctured Hoffman--Singleton graph.  No floating-point arithmetic
is used.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def p(i: int, j: int) -> int:
    return 5 * (i % 5) + (j % 5)


def q(i: int, j: int) -> int:
    return 25 + 5 * (i % 5) + (j % 5)


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
            for h in range(5):
                add(p(i, j), q(h, i * h + j))
    graph = tuple(frozenset(row) for row in rows)
    if not all(len(row) == 7 for row in graph):
        raise AssertionError("bad Hoffman--Singleton degree")
    if not all(u in graph[v] for u in range(50) for v in graph[u]):
        raise AssertionError("asymmetric adjacency")
    return graph


def induced(graph: Graph, deleted: set[int]) -> tuple[Graph, tuple[int, ...]]:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    relabel = {old: new for new, old in enumerate(keep)}
    return (
        tuple(
            frozenset(relabel[z] for z in graph[v] if z in relabel)
            for v in keep
        ),
        keep,
    )


def distance_matrix(graph: Graph) -> sp.Matrix:
    rows: list[list[int]] = []
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
        if -1 in dist:
            raise AssertionError("disconnected graph")
        rows.append(dist)
    return sp.Matrix(rows)


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def indicator(index: dict[int, int], order: int, vertices: list[int]) -> sp.Matrix:
    out = sp.zeros(order, 1)
    for v in vertices:
        out[index[v], 0] = 1
    return out


def embedded_vector(
    index: dict[int, int], order: int, values: dict[int, sp.Expr]
) -> sp.Matrix:
    out = sp.zeros(order, 1)
    for v, value in values.items():
        out[index[v], 0] = value
    return out


def representation(matrix: sp.Matrix, basis: sp.Matrix) -> sp.Matrix:
    gram = basis.T * basis
    if gram.det() == 0:
        raise AssertionError("dependent basis")
    action = sp.simplify(gram.inv() * basis.T * matrix * basis)
    if matrix * basis != basis * action:
        raise AssertionError("claimed subspace is not invariant")
    return action


def generic_symbolic_audit() -> dict[str, str]:
    k, delta = sp.symbols("k Delta", positive=True)
    sizes = [1, k - 1, k - 1, k - 2, (k - 1) * (k - 2)]
    adjacency_quotient = sp.Matrix(
        [
            [0, 0, 0, k - 2, 0],
            [0, 0, 1, 0, k - 2],
            [0, 1, 0, 0, k - 2],
            [1, 0, 0, 0, k - 1],
            [0, 1, 1, 1, k - 3],
        ]
    )
    increase_quotient = sp.Matrix(
        [
            [0, k - 1, k - 1, 0, 0],
            [1, k - 2, 0, 0, 0],
            [1, 0, k - 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    distance_quotient = sp.Matrix(
        5,
        5,
        lambda i, j: sp.expand(
            2 * sizes[j]
            - 2 * int(i == j)
            - adjacency_quotient[i, j]
            + increase_quotient[i, j]
        ),
    )
    quartic = (
        X**4
        + (10 - 2 * k**2) * X**3
        + (2 * k**3 - 17 * k**2 - 2 * k + 36) * X**2
        + (12 * k**3 - 49 * k**2 - 4 * k + 53) * X
        - 2 * k**4
        + 17 * k**3
        - 38 * k**2
        + 5 * k
        + 20
    )
    if sp.expand(
        distance_quotient.charpoly(X).as_expr() - (X - k + 3) * quartic
    ) != 0:
        raise AssertionError("wrong quotient factor")

    symmetric = sp.Matrix([[-4, -(k - 3)], [-1, 0]])
    antisymmetric = sp.Matrix([[-2, -(k - 1)], [-1, -2]])
    common = sp.Matrix([[-2, -(k - 1)], [-1, -1]])
    expected_factors = (
        X**2 + 4 * X - k + 3,
        X**2 + 4 * X - k + 5,
        X**2 + 3 * X + 3 - k,
    )
    for matrix, expected in zip(
        (symmetric, antisymmetric, common), expected_factors, strict=True
    ):
        if sp.expand(matrix.charpoly(X).as_expr() - expected) != 0:
            raise AssertionError("wrong module factor")

    dim_k = (k - 2) * (k - 4)
    trace_k = 2 * (k - 2)
    r = (-1 + delta) / 2
    s = (-1 - delta) / 2
    mult_r = (k - 2) * (k + (k - 4) * delta) / (2 * delta)
    mult_s = (k - 2) * ((k - 4) * delta - k) / (2 * delta)
    if sp.simplify(mult_r + mult_s - dim_k) != 0:
        raise AssertionError("wrong residual dimension")
    if sp.simplify(r * mult_r + s * mult_s - trace_k) != 0:
        raise AssertionError("wrong residual trace")

    total_negative = sp.simplify(mult_r + k - 3)
    total_positive = sp.simplify(mult_s + k - 3)
    expected_negative = (
        k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    expected_positive = (
        -k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    if sp.simplify(total_negative - expected_negative) != 0:
        raise AssertionError("wrong negative multiplicity")
    if sp.simplify(total_positive - expected_positive) != 0:
        raise AssertionError("wrong positive multiplicity")
    total_dimension = sp.expand(
        5 + 2 * (k - 2) + 2 * (k - 2) + 2 * (k - 3) + dim_k
    )
    if total_dimension != k**2 - 1:
        raise AssertionError("incomplete direct sum")

    dual_gap = sp.factor(
        (k - sp.Rational(1, 1) / (k - 1))
        - (k - sp.Rational(2, 1) / k)
    )
    if dual_gap != (k - 2) / (k * (k - 1)):
        raise AssertionError("wrong dual-degree comparison")

    return {
        "quotient_factor": str(sp.factor((X - k + 3) * quartic)),
        "module_factors": str(expected_factors),
        "residual_dimension": str(dim_k),
        "residual_trace": str(trace_k),
        "total_dimension": str(total_dimension),
        "dual_degree_gap": str(dual_gap),
    }


def finite_k7_audit() -> dict[str, object]:
    full = hoffman_singleton()
    u, v = p(0, 0), p(0, 2)
    if v in full[u]:
        raise AssertionError("deleted vertices are adjacent")
    common_uv = full[u] & full[v]
    if len(common_uv) != 1:
        raise AssertionError("wrong common-neighbour count")
    w = next(iter(common_uv))

    cell_a = sorted(set(full[u]) - {w})
    raw_b = set(full[v]) - {w}
    matching: dict[int, int] = {}
    for a in cell_a:
        neighbours = set(full[a]) & raw_b
        if len(neighbours) != 1:
            raise AssertionError("A--B edges are not a matching")
        matching[a] = next(iter(neighbours))
    if len(set(matching.values())) != 6:
        raise AssertionError("matching is not perfect")
    cell_b = [matching[a] for a in cell_a]
    cell_c = sorted(set(full[w]) - {u, v})
    cell_z = sorted(
        set(range(50))
        - {u, v, w}
        - set(cell_a)
        - set(cell_b)
        - set(cell_c)
    )
    cells_old = [[w], cell_a, cell_b, cell_c, cell_z]
    if [len(cell) for cell in cells_old] != [1, 6, 6, 5, 30]:
        raise AssertionError("wrong cell sizes")

    expected_adjacency_counts = [
        [0, 0, 0, 5, 0],
        [0, 0, 1, 0, 5],
        [0, 1, 0, 0, 5],
        [1, 0, 0, 0, 6],
        [0, 1, 1, 1, 4],
    ]
    for i, source_cell in enumerate(cells_old):
        for source in source_cell:
            counts = [len(set(full[source]) & set(target)) for target in cells_old]
            if counts != expected_adjacency_counts[i]:
                raise AssertionError(("bad cell adjacency", source, counts))

    graph, keep = induced(full, {u, v})
    old_to_new = {old: new for new, old in enumerate(keep)}
    order = len(graph)
    if order != 48:
        raise AssertionError("wrong punctured order")
    adjacency = adjacency_matrix(graph)
    distance = distance_matrix(graph)
    if max(distance) != 3:
        raise AssertionError("wrong punctured diameter")

    f_matrix = sp.zeros(order)
    for clique in ([w] + cell_a, [w] + cell_b):
        for a, b in combinations(clique, 2):
            ia, ib = old_to_new[a], old_to_new[b]
            f_matrix[ia, ib] = 1
            f_matrix[ib, ia] = 1
    formula = 2 * (sp.ones(order) - sp.eye(order)) - adjacency + f_matrix
    if distance != formula:
        raise AssertionError("recomputed-distance formula failed")

    exceptional_pairs: set[tuple[int, int]] = set()
    for clique in ([w] + cell_a, [w] + cell_b):
        for a, b in combinations(clique, 2):
            exceptional_pairs.add(tuple(sorted((a, b))))
            ia, ib = old_to_new[a], old_to_new[b]
            if distance[ia, ib] != 3:
                raise AssertionError("exceptional pair is not at distance three")
            length_three_paths = 0
            for x in graph[ia]:
                for y in graph[x]:
                    if ib in graph[y]:
                        length_three_paths += 1
            if length_three_paths == 0:
                raise AssertionError("missing replacement path of length three")

    for a, b in combinations(keep, 2):
        ia, ib = old_to_new[a], old_to_new[b]
        if tuple(sorted((a, b))) not in exceptional_pairs:
            expected = 1 if b in full[a] else 2
            if distance[ia, ib] != expected:
                raise AssertionError("a nonexceptional distance changed")

    def incidence(vertices: list[int]) -> sp.Matrix:
        return sp.Matrix(
            [[int(z in full[a]) for z in cell_z] for a in vertices]
        )

    ra, rb, rc = incidence(cell_a), incidence(cell_b), incidence(cell_c)
    t = sp.Matrix(
        [[int(z2 in full[z1]) for z2 in cell_z] for z1 in cell_z]
    )
    if ra * ra.T != 5 * sp.eye(6):
        raise AssertionError("bad RA norm identity")
    if rb * rb.T != 5 * sp.eye(6):
        raise AssertionError("bad RB norm identity")
    if rc * rc.T != 6 * sp.eye(5):
        raise AssertionError("bad RC norm identity")
    if ra * rb.T != sp.ones(6) - sp.eye(6):
        raise AssertionError("bad RA/RB identity")
    if ra * rc.T != sp.ones(6, 5) or rb * rc.T != sp.ones(6, 5):
        raise AssertionError("bad A/B--C identity")
    if ra * t + rb != sp.ones(6, 30) - ra:
        raise AssertionError("bad RA/T identity")
    if rb * t + ra != sp.ones(6, 30) - rb:
        raise AssertionError("bad RB/T identity")
    if rc * t != sp.ones(5, 30) - rc:
        raise AssertionError("bad RC/T identity")
    bottom = ra.T * ra + rb.T * rb + rc.T * rc + t * t
    if bottom != 6 * sp.eye(30) - t + sp.ones(30):
        raise AssertionError("bad bottom-right Moore identity")

    cell_indicators = sp.Matrix.hstack(
        *[indicator(old_to_new, order, cell) for cell in cells_old]
    )
    quotient_rep = representation(distance, cell_indicators)
    expected_quotient = sp.Matrix(
        [
            [0, 18, 18, 5, 60],
            [3, 15, 11, 10, 55],
            [3, 11, 15, 10, 55],
            [1, 12, 12, 8, 54],
            [2, 11, 11, 9, 54],
        ]
    )
    if quotient_rep != expected_quotient:
        raise AssertionError("wrong distance quotient")

    zero_a: list[sp.Matrix] = []
    for i in range(5):
        x = sp.zeros(6, 1)
        x[i], x[-1] = 1, -1
        zero_a.append(x)

    symmetric_columns: list[sp.Matrix] = []
    antisymmetric_columns: list[sp.Matrix] = []
    for x in zero_a:
        image_a, image_b = ra.T * x, rb.T * x
        symmetric_columns.extend(
            [
                embedded_vector(
                    old_to_new,
                    order,
                    {
                        **{a: x[i] for i, a in enumerate(cell_a)},
                        **{b: x[i] for i, b in enumerate(cell_b)},
                    },
                ),
                embedded_vector(
                    old_to_new,
                    order,
                    {z: (image_a + image_b)[i] for i, z in enumerate(cell_z)},
                ),
            ]
        )
        antisymmetric_columns.extend(
            [
                embedded_vector(
                    old_to_new,
                    order,
                    {
                        **{a: x[i] for i, a in enumerate(cell_a)},
                        **{b: -x[i] for i, b in enumerate(cell_b)},
                    },
                ),
                embedded_vector(
                    old_to_new,
                    order,
                    {z: (image_a - image_b)[i] for i, z in enumerate(cell_z)},
                ),
            ]
        )
    symmetric_basis = sp.Matrix.hstack(*symmetric_columns)
    antisymmetric_basis = sp.Matrix.hstack(*antisymmetric_columns)

    common_columns: list[sp.Matrix] = []
    for i in range(4):
        y = sp.zeros(5, 1)
        y[i], y[-1] = 1, -1
        image = rc.T * y
        common_columns.extend(
            [
                embedded_vector(
                    old_to_new,
                    order,
                    {c: y[j] for j, c in enumerate(cell_c)},
                ),
                embedded_vector(
                    old_to_new,
                    order,
                    {z: image[j] for j, z in enumerate(cell_z)},
                ),
            ]
        )
    common_basis = sp.Matrix.hstack(*common_columns)

    kernel_vectors = ra.col_join(rb).col_join(rc).nullspace()
    if len(kernel_vectors) != 15:
        raise AssertionError("wrong residual-kernel dimension")
    kernel_basis = sp.Matrix.hstack(
        *[
            embedded_vector(
                old_to_new,
                order,
                {z: vec[i] for i, z in enumerate(cell_z)},
            )
            for vec in kernel_vectors
        ]
    )

    blocks = [
        cell_indicators,
        symmetric_basis,
        antisymmetric_basis,
        common_basis,
        kernel_basis,
    ]
    expected_dimensions = [5, 10, 10, 8, 15]
    if [block.cols for block in blocks] != expected_dimensions:
        raise AssertionError("wrong module dimensions")
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            if left.T * right != sp.zeros(left.cols, right.cols):
                raise AssertionError("modules are not orthogonal")
    complete = sp.Matrix.hstack(*blocks)
    if complete.rank() != 48:
        raise AssertionError("modules do not span the full space")

    symmetric_rep = representation(distance, symmetric_basis)
    antisymmetric_rep = representation(distance, antisymmetric_basis)
    common_rep = representation(distance, common_basis)
    kernel_rep = representation(distance, kernel_basis)
    if symmetric_rep != sp.diag(*([sp.Matrix([[-4, -4], [-1, 0]])] * 5)):
        raise AssertionError("wrong symmetric action")
    if antisymmetric_rep != sp.diag(*([sp.Matrix([[-2, -6], [-1, -2]])] * 5)):
        raise AssertionError("wrong antisymmetric action")
    if common_rep != sp.diag(*([sp.Matrix([[-2, -6], [-1, -1]])] * 4)):
        raise AssertionError("wrong common-neighbour action")
    if sp.factor(kernel_rep.charpoly(X).as_expr()) != (X - 1) ** 4 * (X + 4) ** 11:
        raise AssertionError("wrong residual-kernel factor")

    quotient_factor = (X - 4) * (
        X**4 - 88 * X**3 - 125 * X**2 + 1740 * X - 778
    )
    if sp.Poly(quotient_rep.charpoly(X).as_expr() - quotient_factor, X) != sp.Poly(0, X):
        raise AssertionError("wrong quotient characteristic polynomial")
    expected_charpoly = (
        quotient_factor
        * (X**2 + 4 * X - 4) ** 5
        * (X**2 + 4 * X - 2) ** 5
        * (X + 4) ** 15
        * (X - 1) ** 8
    )
    if sp.Poly(distance.charpoly(X).as_expr() - expected_charpoly, X) != sp.Poly(0, X):
        raise AssertionError("wrong complete distance characteristic polynomial")

    degrees = tuple(len(row) for row in graph)
    dual_degrees = tuple(
        Fraction(sum(degrees[z] for z in graph[i]), degrees[i])
        for i in range(order)
    )
    if min(dual_degrees) != Fraction(47, 7):
        raise AssertionError("wrong minimum dual degree")
    class_degrees = {
        "w": degrees[old_to_new[w]],
        "A": {degrees[old_to_new[a]] for a in cell_a},
        "B": {degrees[old_to_new[b]] for b in cell_b},
        "C": {degrees[old_to_new[c]] for c in cell_c},
        "Z": {degrees[old_to_new[z]] for z in cell_z},
    }
    if class_degrees != {"w": 5, "A": {6}, "B": {6}, "C": {7}, "Z": {7}}:
        raise AssertionError("wrong degree classes")

    shifted = 7 * distance + 47 * sp.eye(order)
    lower, diagonal = shifted.LDLdecomposition(hermitian=True)
    if lower * diagonal * lower.T != shifted:
        raise AssertionError("LDL reconstruction failed")
    pivots = [sp.factor(diagonal[i, i]) for i in range(order)]
    if not all(pivot.is_positive is True for pivot in pivots):
        raise AssertionError("shifted distance matrix is not certified positive")

    return {
        "deleted_vertices": "P_(0,0), P_(0,2)",
        "cell_sizes": [1, 6, 6, 5, 30],
        "exceptional_pairs_checked": len(exceptional_pairs),
        "module_dimensions": expected_dimensions,
        "complete_basis_rank": complete.rank(),
        "minimum_dual_degree": "47/7",
        "positive_definite_shift": "7D+47I",
        "positive_LDL_pivots": len(pivots),
        "distance_characteristic_polynomial": str(sp.factor(expected_charpoly)),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "generic_symbolic_audit": generic_symbolic_audit(),
        "independent_k7_audit": finite_k7_audit(),
    }
    print("Proof Audit 03 (nonadjacent Moore puncture): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
