#!/usr/bin/env python3
"""Independent exact audit of one-vertex and adjacent-edge Moore punctures.

The script does not import the original extension verifier. It checks the
symbolic spectra, multiplicities, least-root comparisons and score thresholds,
then reconstructs the cycle, Petersen and Hoffman--Singleton Moore graphs and
checks the punctures directly. No floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
import json

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def add_edge(rows: list[set[int]], u: int, v: int) -> None:
    if u == v:
        raise AssertionError("loop")
    rows[u].add(v)
    rows[v].add(u)


def cycle_five() -> Graph:
    rows = [set() for _ in range(5)]
    for i in range(5):
        add_edge(rows, i, (i + 1) % 5)
    return tuple(frozenset(row) for row in rows)


def petersen() -> Graph:
    vertices = list(combinations(range(5), 2))
    rows = [set() for _ in vertices]
    for i, left in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            if set(left).isdisjoint(vertices[j]):
                add_edge(rows, i, j)
    return tuple(frozenset(row) for row in rows)


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]

    def p(i: int, j: int) -> int:
        return 5 * (i % 5) + (j % 5)

    def q(i: int, j: int) -> int:
        return 25 + 5 * (i % 5) + (j % 5)

    for i in range(5):
        for j in range(5):
            add_edge(rows, p(i, j), p(i, j + 1))
            add_edge(rows, q(i, j), q(i, j + 2))
            for h in range(5):
                add_edge(rows, p(i, j), q(h, i * h + j))
    return tuple(frozenset(row) for row in rows)


def induced(graph: Graph, deleted: set[int]) -> tuple[Graph, tuple[int, ...]]:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    index = {old: new for new, old in enumerate(keep)}
    return (
        tuple(
            frozenset(index[z] for z in graph[v] if z in index)
            for v in keep
        ),
        keep,
    )


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
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


def indicator(index: dict[int, int], order: int, vertices: list[int]) -> sp.Matrix:
    out = sp.zeros(order, 1)
    for v in vertices:
        out[index[v], 0] = 1
    return out


def embedded(
    index: dict[int, int], order: int, values: dict[int, sp.Expr]
) -> sp.Matrix:
    out = sp.zeros(order, 1)
    for vertex, value in values.items():
        out[index[vertex], 0] = value
    return out


def zero_sum_basis(size: int) -> list[sp.Matrix]:
    basis: list[sp.Matrix] = []
    for i in range(size - 1):
        vector = sp.zeros(size, 1)
        vector[i], vector[-1] = 1, -1
        basis.append(vector)
    return basis


def representation(matrix: sp.Matrix, basis: sp.Matrix) -> sp.Matrix:
    gram = basis.T * basis
    if gram.det() == 0:
        raise AssertionError("dependent basis")
    action = sp.simplify(gram.inv() * basis.T * matrix * basis)
    if matrix * basis != basis * action:
        raise AssertionError("non-invariant subspace")
    return action


def check_moore(graph: Graph, k: int) -> None:
    if len(graph) != k * k + 1:
        raise AssertionError("wrong Moore order")
    if not all(len(row) == k for row in graph):
        raise AssertionError("wrong Moore degree")
    distances = distance_matrix(graph)
    if max(distances) != 2:
        raise AssertionError("wrong Moore diameter")
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            common = len(graph[u] & graph[v])
            expected = 0 if v in graph[u] else 1
            if common != expected:
                raise AssertionError("wrong Moore common-neighbour count")


def symbolic_audit() -> dict[str, str]:
    k, delta, m, t = sp.symbols(
        "k Delta m t", positive=True
    )

    one_quotient = sp.Matrix(
        [
            [3 * (k - 1), (2 * k - 1) * sp.sqrt(k - 1)],
            [(2 * k - 1) * sp.sqrt(k - 1), 2 * k**2 - 3 * k - 1],
        ]
    )
    one_poly = sp.factor(one_quotient.charpoly(X).as_expr())
    if -sp.Poly(one_poly, X).coeff_monomial(X) != 2 * (k**2 - 2):
        raise AssertionError("wrong one-vertex quotient trace")
    one_discriminant = sp.factor(sp.discriminant(one_poly, X))
    expected_one_discriminant = 4 * k * (k**3 - 2 * k**2 + 3 * k - 1)
    if sp.expand(one_discriminant - expected_one_discriminant) != 0:
        raise AssertionError("wrong one-vertex quotient discriminant")

    edge_quotient = sp.Matrix(
        [
            [5 * k - 8, sp.sqrt((k - 1) * (2 * k - 3) * (4 * k - 6))],
            [sp.sqrt((k - 1) * (2 * k - 3) * (4 * k - 6)), 2 * k**2 - 5 * k + 2],
        ]
    )
    edge_poly = sp.factor(edge_quotient.charpoly(X).as_expr())
    if -sp.Poly(edge_poly, X).coeff_monomial(X) != 2 * (k**2 - 3):
        raise AssertionError("wrong edge quotient trace")
    edge_discriminant = sp.factor(sp.discriminant(edge_poly, X))
    expected_edge_discriminant = 4 * (
        k**4 - 2 * k**3 + 3 * k**2 - 8 * k + 7
    )
    if sp.expand(edge_discriminant - expected_edge_discriminant) != 0:
        raise AssertionError("wrong edge quotient discriminant")

    module = sp.Matrix([[-3, -(k - 1)], [-1, -1]])
    if sp.expand(module.charpoly(X).as_expr() - (X**2 + 4 * X + 4 - k)) != 0:
        raise AssertionError("wrong incidence factor")

    one_dimension = k * (k - 2)
    one_mplus = k * (k - 2) * (delta + 1) / (2 * delta)
    one_mminus = k * (k - 2) * (delta - 1) / (2 * delta)
    r = (-1 + delta) / 2
    s = (-1 - delta) / 2
    if sp.simplify(one_mplus + one_mminus - one_dimension) != 0:
        raise AssertionError("wrong one-vertex residual dimension")
    if sp.simplify(r * one_mplus + s * one_mminus) != 0:
        raise AssertionError("wrong one-vertex residual trace")
    if sp.expand(2 + 2 * (k - 1) + one_dimension - k**2) != 0:
        raise AssertionError("wrong one-vertex total dimension")

    edge_dimension = (k - 2) ** 2
    edge_aplus = (k - 2) * (k + (k - 2) * delta) / (2 * delta)
    edge_aminus = (k - 2) * ((k - 2) * delta - k) / (2 * delta)
    if sp.simplify(edge_aplus + edge_aminus - edge_dimension) != 0:
        raise AssertionError("wrong edge residual dimension")
    if sp.simplify(r * edge_aplus + s * edge_aminus - (k - 2)) != 0:
        raise AssertionError("wrong edge residual trace")
    if sp.expand(3 + 4 * (k - 2) + edge_dimension - (k**2 - 1)) != 0:
        raise AssertionError("wrong edge total dimension")

    kt = t**2
    one_shift_det = sp.factor(
        (3 * (kt - 1) + 2 + t)
        * (2 * kt**2 - 3 * kt - 1 + 2 + t)
        - (kt - 1) * (2 * kt - 1) ** 2
    )
    expected_one_shift = t**2 * (2 * t**4 + 2 * t**3 - 3 * t**2 + 2)
    if sp.expand(one_shift_det - expected_one_shift) != 0:
        raise AssertionError("wrong one-vertex quotient shift")

    edge_shift_det = sp.factor(
        (5 * kt - 8 + 2 + t)
        * (2 * kt**2 - 5 * kt + 2 + 2 + t)
        - (kt - 1) * (2 * kt - 3) * (4 * kt - 6)
    )
    expected_edge_shift = (t - 1) * (t + 1) * (
        2 * t**4 + 2 * t**3 - 3 * t**2 + 2 * t + 6
    )
    if sp.expand(edge_shift_det - expected_edge_shift) != 0:
        raise AssertionError("wrong edge quotient shift")
    if sp.expand((1 + 2 * t) ** 2 - (4 * t**2 - 3) - 4 * (t + 1)) != 0:
        raise AssertionError("wrong residual-root comparison")

    kvar = sp.symbols("kvar", integer=True, positive=True)
    one_margin = sp.expand((kvar**2 - 2 * kvar - 1) ** 2 - kvar**3)
    edge_margin = sp.expand((kvar**2 - 2 * kvar - 2) ** 2 - kvar**3)
    expected_one_shifted = m**4 + 15 * m**3 + 77 * m**2 + 149 * m + 71
    expected_edge_shifted = m**4 + 15 * m**3 + 75 * m**2 + 133 * m + 44
    if sp.expand(one_margin.subs(kvar, m + 5) - expected_one_shifted) != 0:
        raise AssertionError("wrong one-vertex score threshold")
    if sp.expand(edge_margin.subs(kvar, m + 5) - expected_edge_shifted) != 0:
        raise AssertionError("wrong edge score threshold")

    for value in (2, 3, 4):
        score = sp.Integer(value) - sp.Rational(1, value) - 2 - sp.sqrt(value)
        if not score < 0:
            raise AssertionError("wrong one-vertex low-degree sign")
    for value in (3, 4):
        score = sp.Integer(value) - sp.Rational(2, value) - 2 - sp.sqrt(value)
        if not score < 0:
            raise AssertionError("wrong edge low-degree sign")

    return {
        "one_quotient_polynomial": str(one_poly),
        "edge_quotient_polynomial": str(edge_poly),
        "incidence_factor": str(module.charpoly(X).as_expr()),
        "one_shift_determinant": str(one_shift_det),
        "edge_shift_determinant": str(edge_shift_det),
        "one_threshold_polynomial": str(one_margin),
        "edge_threshold_polynomial": str(edge_margin),
    }


def ldl_positive(matrix: sp.Matrix) -> int:
    lower, diagonal = matrix.LDLdecomposition(hermitian=True)
    if lower * diagonal * lower.T != matrix:
        raise AssertionError("LDL reconstruction failed")
    pivots = [sp.factor(diagonal[i, i]) for i in range(matrix.rows)]
    if not all(pivot.is_positive is True for pivot in pivots):
        raise AssertionError("shift is not certified positive definite")
    return len(pivots)


def one_vertex_audit(graph: Graph, k: int, deleted: int = 0) -> dict[str, object]:
    check_moore(graph, k)
    cell_a = sorted(graph[deleted])
    cell_b = sorted(set(range(len(graph))) - {deleted} - set(cell_a))
    if [len(cell_a), len(cell_b)] != [k, k * (k - 1)]:
        raise AssertionError("wrong one-vertex cells")

    child, keep = induced(graph, {deleted})
    index = {old: new for new, old in enumerate(keep)}
    order = len(child)
    distance = distance_matrix(child)
    adjacency = adjacency_matrix(child)

    correction = sp.zeros(order)
    exceptional: set[tuple[int, int]] = set()
    for a, b in combinations(cell_a, 2):
        exceptional.add((a, b))
        ia, ib = index[a], index[b]
        correction[ia, ib] = correction[ib, ia] = 1
    formula = 2 * (sp.ones(order) - sp.eye(order)) - adjacency + correction
    if distance != formula:
        raise AssertionError("one-vertex metric formula failed")

    for a, b in exceptional:
        ia, ib = index[a], index[b]
        if distance[ia, ib] != 3:
            raise AssertionError("wrong one-vertex exceptional distance")
        path_count = 0
        for x in child[ia]:
            for y in child[x]:
                if ib in child[y]:
                    path_count += 1
        if path_count == 0:
            raise AssertionError("missing one-vertex replacement path")

    incidence = sp.Matrix(
        [[int(b in graph[a]) for b in cell_b] for a in cell_a]
    )
    b0 = sp.Matrix(
        [[int(y in graph[x]) for y in cell_b] for x in cell_b]
    )
    if incidence * incidence.T != (k - 1) * sp.eye(k):
        raise AssertionError("bad one-vertex incidence norm")
    if incidence * b0 != sp.ones(k, len(cell_b)) - incidence:
        raise AssertionError("bad one-vertex incidence/T identity")
    if b0 * b0 + incidence.T * incidence != (
        (k - 1) * sp.eye(len(cell_b)) - b0 + sp.ones(len(cell_b))
    ):
        raise AssertionError("bad one-vertex bottom identity")

    quotient = sp.Matrix.hstack(
        indicator(index, order, cell_a), indicator(index, order, cell_b)
    )
    quotient_rep = representation(distance, quotient)
    expected_quotient = sp.Matrix(
        [
            [3 * (k - 1), (k - 1) * (2 * k - 1)],
            [2 * k - 1, 2 * k**2 - 3 * k - 1],
        ]
    )
    if quotient_rep != expected_quotient:
        raise AssertionError("wrong one-vertex quotient")

    module_columns: list[sp.Matrix] = []
    for z in zero_sum_basis(k):
        image = incidence.T * z
        module_columns.extend(
            [
                embedded(
                    index,
                    order,
                    {a: z[i] for i, a in enumerate(cell_a)},
                ),
                embedded(
                    index,
                    order,
                    {b: image[i] for i, b in enumerate(cell_b)},
                ),
            ]
        )
    module_basis = sp.Matrix.hstack(*module_columns)
    module_rep = representation(distance, module_basis)
    expected_module = sp.diag(
        *([sp.Matrix([[-3, -(k - 1)], [-1, -1]])] * (k - 1))
    )
    if module_rep != expected_module:
        raise AssertionError("wrong one-vertex incidence action")

    kernel_vectors = incidence.nullspace()
    expected_kernel_dim = k * (k - 2)
    if len(kernel_vectors) != expected_kernel_dim:
        raise AssertionError("wrong one-vertex kernel dimension")
    kernel_basis = None
    if kernel_vectors:
        kernel_basis = sp.Matrix.hstack(
            *[
                embedded(
                    index,
                    order,
                    {b: vector[i] for i, b in enumerate(cell_b)},
                )
                for vector in kernel_vectors
            ]
        )

    blocks = [quotient, module_basis]
    if kernel_basis is not None:
        blocks.append(kernel_basis)
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            if left.T * right != sp.zeros(left.cols, right.cols):
                raise AssertionError("one-vertex modules are not orthogonal")
    complete = sp.Matrix.hstack(*blocks)
    if complete.rank() != order:
        raise AssertionError("one-vertex modules do not span")

    if kernel_basis is not None:
        kernel_rep = representation(distance, kernel_basis)
        if kernel_rep * kernel_rep + 3 * kernel_rep + (3 - k) * sp.eye(
            kernel_rep.rows
        ) != sp.zeros(kernel_rep.rows):
            raise AssertionError("wrong one-vertex residual quadratic")

    quotient_factor = quotient_rep.charpoly(X).as_expr()
    expected_charpoly = quotient_factor * (X**2 + 4 * X + 4 - k) ** (k - 1)
    delta_squared = 4 * k - 3
    if expected_kernel_dim:
        delta_integer = sp.integer_nthroot(delta_squared, 2)
        if not delta_integer[1]:
            raise AssertionError("concrete Moore control has nonintegral Delta")
        delta = delta_integer[0]
        mplus = sp.Rational(k * (k - 2) * (delta + 1), 2 * delta)
        mminus = sp.Rational(k * (k - 2) * (delta - 1), 2 * delta)
        if mplus.q != 1 or mminus.q != 1:
            raise AssertionError("nonintegral one-vertex multiplicity")
        expected_charpoly *= (
            X + sp.Rational(delta + 3, 2)
        ) ** int(mplus) * (
            X - sp.Rational(delta - 3, 2)
        ) ** int(mminus)
    if sp.Poly(distance.charpoly(X).as_expr() - expected_charpoly, X) != sp.Poly(0, X):
        raise AssertionError("wrong one-vertex characteristic polynomial")

    degrees = tuple(len(row) for row in child)
    duals = tuple(
        Fraction(sum(degrees[z] for z in child[i]), degrees[i])
        for i in range(order)
    )
    expected_dual = Fraction(k * k - 1, k)
    if min(duals) != expected_dual:
        raise AssertionError("wrong one-vertex dual degree")

    ldl_pivots = None
    if k == 7:
        ldl_pivots = ldl_positive(7 * distance + 48 * sp.eye(order))

    return {
        "order": order,
        "exceptional_pairs": len(exceptional),
        "module_dimensions": [quotient.cols, module_basis.cols, expected_kernel_dim],
        "basis_rank": complete.rank(),
        "minimum_dual_degree": str(expected_dual),
        "positive_LDL_pivots": ldl_pivots,
        "distance_characteristic_polynomial": str(sp.factor(expected_charpoly)),
    }


def edge_audit(graph: Graph, k: int, u: int = 0) -> dict[str, object]:
    if k < 3:
        raise AssertionError("edge theorem starts at k=3")
    check_moore(graph, k)
    v = min(graph[u])
    cell_a = sorted(set(graph[u]) - {v})
    cell_b = sorted(set(graph[v]) - {u})
    cell_c = sorted(
        set(range(len(graph))) - {u, v} - set(cell_a) - set(cell_b)
    )
    if [len(cell_a), len(cell_b), len(cell_c)] != [k - 1, k - 1, (k - 1) ** 2]:
        raise AssertionError("wrong edge cells")

    child, keep = induced(graph, {u, v})
    index = {old: new for new, old in enumerate(keep)}
    order = len(child)
    distance = distance_matrix(child)
    adjacency = adjacency_matrix(child)

    correction = sp.zeros(order)
    exceptional: set[tuple[int, int]] = set()
    for cell in (cell_a, cell_b):
        for left, right in combinations(cell, 2):
            exceptional.add(tuple(sorted((left, right))))
            i, j = index[left], index[right]
            correction[i, j] = correction[j, i] = 1
    formula = 2 * (sp.ones(order) - sp.eye(order)) - adjacency + correction
    if distance != formula:
        raise AssertionError("edge-puncture metric formula failed")

    for left, right in exceptional:
        i, j = index[left], index[right]
        if distance[i, j] != 3:
            raise AssertionError("wrong edge-puncture exceptional distance")
        path_count = 0
        for x in child[i]:
            for y in child[x]:
                if j in child[y]:
                    path_count += 1
        if path_count == 0:
            raise AssertionError("missing edge-puncture replacement path")

    ra = sp.Matrix([[int(c in graph[a]) for c in cell_c] for a in cell_a])
    rb = sp.Matrix([[int(c in graph[b]) for c in cell_c] for b in cell_b])
    t_matrix = sp.Matrix(
        [[int(y in graph[x]) for y in cell_c] for x in cell_c]
    )
    if ra * ra.T != (k - 1) * sp.eye(k - 1):
        raise AssertionError("bad edge RA identity")
    if rb * rb.T != (k - 1) * sp.eye(k - 1):
        raise AssertionError("bad edge RB identity")
    if ra * rb.T != sp.ones(k - 1):
        raise AssertionError("bad edge RA/RB identity")
    if ra * t_matrix != sp.ones(k - 1, len(cell_c)) - ra:
        raise AssertionError("bad edge RA/T identity")
    if rb * t_matrix != sp.ones(k - 1, len(cell_c)) - rb:
        raise AssertionError("bad edge RB/T identity")
    if ra.T * ra + rb.T * rb + t_matrix * t_matrix != (
        (k - 1) * sp.eye(len(cell_c)) - t_matrix + sp.ones(len(cell_c))
    ):
        raise AssertionError("bad edge bottom identity")

    quotient = sp.Matrix.hstack(
        indicator(index, order, cell_a),
        indicator(index, order, cell_b),
        indicator(index, order, cell_c),
    )
    quotient_rep = representation(distance, quotient)
    expected_quotient = sp.Matrix(
        [
            [3 * (k - 2), 2 * (k - 1), (k - 1) * (2 * k - 3)],
            [2 * (k - 1), 3 * (k - 2), (k - 1) * (2 * k - 3)],
            [2 * k - 3, 2 * k - 3, (k - 2) * (2 * k - 1)],
        ]
    )
    if quotient_rep != expected_quotient:
        raise AssertionError("wrong edge-puncture quotient")

    module_blocks: list[sp.Matrix] = []
    module_matrix = sp.Matrix([[-3, -(k - 1)], [-1, -1]])
    for cell, incidence in ((cell_a, ra), (cell_b, rb)):
        columns: list[sp.Matrix] = []
        for z in zero_sum_basis(k - 1):
            image = incidence.T * z
            columns.extend(
                [
                    embedded(
                        index,
                        order,
                        {vertex: z[i] for i, vertex in enumerate(cell)},
                    ),
                    embedded(
                        index,
                        order,
                        {vertex: image[i] for i, vertex in enumerate(cell_c)},
                    ),
                ]
            )
        basis = sp.Matrix.hstack(*columns)
        action = representation(distance, basis)
        expected = sp.diag(*([module_matrix] * (k - 2)))
        if action != expected:
            raise AssertionError("wrong edge-puncture incidence action")
        module_blocks.append(basis)

    kernel_vectors = ra.col_join(rb).nullspace()
    expected_kernel_dim = (k - 2) ** 2
    if len(kernel_vectors) != expected_kernel_dim:
        raise AssertionError("wrong edge-puncture kernel dimension")
    kernel_basis = sp.Matrix.hstack(
        *[
            embedded(
                index,
                order,
                {vertex: vector[i] for i, vertex in enumerate(cell_c)},
            )
            for vector in kernel_vectors
        ]
    )

    blocks = [quotient, *module_blocks, kernel_basis]
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            if left.T * right != sp.zeros(left.cols, right.cols):
                raise AssertionError("edge-puncture modules are not orthogonal")
    complete = sp.Matrix.hstack(*blocks)
    if complete.rank() != order:
        raise AssertionError("edge-puncture modules do not span")

    kernel_rep = representation(distance, kernel_basis)
    if kernel_rep * kernel_rep + 3 * kernel_rep + (3 - k) * sp.eye(
        kernel_rep.rows
    ) != sp.zeros(kernel_rep.rows):
        raise AssertionError("wrong edge-puncture residual quadratic")

    quotient_factor = quotient_rep.charpoly(X).as_expr()
    expected_charpoly = quotient_factor * (
        X**2 + 4 * X + 4 - k
    ) ** (2 * k - 4)
    delta_integer = sp.integer_nthroot(4 * k - 3, 2)
    if not delta_integer[1]:
        raise AssertionError("concrete Moore control has nonintegral Delta")
    delta = delta_integer[0]
    aplus = sp.Rational((k - 2) * (k + (k - 2) * delta), 2 * delta)
    aminus = sp.Rational((k - 2) * ((k - 2) * delta - k), 2 * delta)
    if aplus.q != 1 or aminus.q != 1:
        raise AssertionError("nonintegral edge-puncture multiplicity")
    expected_charpoly *= (
        X + sp.Rational(delta + 3, 2)
    ) ** int(aplus) * (
        X - sp.Rational(delta - 3, 2)
    ) ** int(aminus)
    if sp.Poly(distance.charpoly(X).as_expr() - expected_charpoly, X) != sp.Poly(0, X):
        raise AssertionError("wrong edge-puncture characteristic polynomial")

    degrees = tuple(len(row) for row in child)
    duals = tuple(
        Fraction(sum(degrees[z] for z in child[i]), degrees[i])
        for i in range(order)
    )
    expected_dual = Fraction(k * k - 2, k)
    if min(duals) != expected_dual:
        raise AssertionError("wrong edge-puncture dual degree")

    ldl_pivots = None
    if k == 7:
        ldl_pivots = ldl_positive(7 * distance + 47 * sp.eye(order))

    return {
        "order": order,
        "exceptional_pairs": len(exceptional),
        "module_dimensions": [
            quotient.cols,
            module_blocks[0].cols,
            module_blocks[1].cols,
            expected_kernel_dim,
        ],
        "basis_rank": complete.rank(),
        "minimum_dual_degree": str(expected_dual),
        "positive_LDL_pivots": ldl_pivots,
        "distance_characteristic_polynomial": str(sp.factor(expected_charpoly)),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    controls = {
        "cycle_5": (cycle_five(), 2),
        "petersen": (petersen(), 3),
        "hoffman_singleton": (hoffman_singleton(), 7),
    }
    one_results = {
        name: one_vertex_audit(graph, degree)
        for name, (graph, degree) in controls.items()
    }
    edge_results = {
        name: edge_audit(graph, degree)
        for name, (graph, degree) in controls.items()
        if degree >= 3
    }
    result = {
        "symbolic_audit": symbolic_audit(),
        "one_vertex_controls": one_results,
        "edge_endpoint_controls": edge_results,
    }
    print("Proof Audit 05 (small Moore punctures): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
