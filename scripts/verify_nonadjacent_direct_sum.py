#!/usr/bin/env python3
"""Exact direct-sum audit for the nonadjacent Moore puncture theorem."""
from __future__ import annotations

from collections import deque
import json
import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def hoffman_singleton() -> Graph:
    rows = [set() for _ in range(50)]
    p = lambda i, j: 5 * (i % 5) + (j % 5)
    q = lambda k, e: 25 + 5 * (k % 5) + (e % 5)

    def add(u: int, v: int) -> None:
        assert u != v
        rows[u].add(v)
        rows[v].add(u)

    for i in range(5):
        for j in range(5):
            add(p(i, j), p(i, j + 1))
            add(q(i, j), q(i, j + 2))
            for h in range(5):
                add(p(i, j), q(h, i * h + j))
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


def distances(graph: Graph) -> sp.Matrix:
    rows = []
    for source in range(len(graph)):
        row = [-1] * len(graph)
        row[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if row[v] == -1:
                    row[v] = row[u] + 1
                    queue.append(v)
        assert -1 not in row
        rows.append(row)
    return sp.Matrix(rows)


def generic_accounting() -> dict[str, str]:
    k, delta = sp.symbols("k Delta", positive=True)
    norm_plus = 2 * (k - 3)
    norm_minus = 2 * (k - 1)
    z_kernel = sp.expand((k - 1) * (k - 2) - (1 + 2 * (k - 2) + k - 3))
    assert sp.expand(z_kernel - (k - 2) * (k - 4)) == 0
    trace_kernel = 2 * (k - 2)
    r = (-1 + delta) / 2
    s = (-1 - delta) / 2
    mult_r = (k - 2) * (k + (k - 4) * delta) / (2 * delta)
    mult_s = (k - 2) * ((k - 4) * delta - k) / (2 * delta)
    assert sp.simplify(mult_r + mult_s - z_kernel) == 0
    assert sp.simplify(r * mult_r + s * mult_s - trace_kernel) == 0
    total_minus = sp.simplify(mult_r + k - 3)
    total_plus = sp.simplify(mult_s + k - 3)
    expected_minus = (
        k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    expected_plus = (
        -k * (k - 2) + (k**2 - 4 * k + 2) * delta
    ) / (2 * delta)
    assert sp.simplify(total_minus - expected_minus) == 0
    assert sp.simplify(total_plus - expected_plus) == 0
    total = sp.expand(5 + 4 * (k - 2) + 2 * (k - 3) + z_kernel)
    assert total == k**2 - 1
    return {
        "matched_plus_norm_squared_factor": str(norm_plus),
        "matched_minus_norm_squared_factor": str(norm_minus),
        "Z_kernel_dimension": str(z_kernel),
        "Z_kernel_trace": str(trace_kernel),
        "residual_positive_T_multiplicity": str(mult_r),
        "residual_negative_T_multiplicity": str(mult_s),
        "full_distance_negative_multiplicity": str(total_minus),
        "full_distance_positive_multiplicity": str(total_plus),
        "complete_dimension_sum": str(total),
    }


def vector(index: dict[int, int], n: int, values: dict[int, sp.Expr]) -> sp.Matrix:
    out = sp.zeros(n, 1)
    for old, value in values.items():
        out[index[old], 0] = value
    return out


def representation(matrix: sp.Matrix, basis: sp.Matrix) -> sp.Matrix:
    gram = basis.T * basis
    assert gram.det() != 0
    action = sp.simplify(gram.inv() * basis.T * matrix * basis)
    assert matrix * basis == basis * action
    return action


def k7_direct_sum() -> dict[str, str]:
    full = hoffman_singleton()
    u, v = 0, 2
    assert v not in full[u]
    common = full[u] & full[v]
    assert len(common) == 1
    w = next(iter(common))
    cell_a = sorted(set(full[u]) - {w})
    raw_b = set(full[v]) - {w}
    matching = {a: next(iter(set(full[a]) & raw_b)) for a in cell_a}
    assert len(set(matching.values())) == 6
    cell_b = [matching[a] for a in cell_a]
    cell_c = sorted(set(full[w]) - {u, v})
    cell_z = sorted(set(range(50)) - {u, v, w} - set(cell_a) - set(cell_b) - set(cell_c))
    assert [1, len(cell_a), len(cell_b), len(cell_c), len(cell_z)] == [1, 6, 6, 5, 30]

    graph, keep = induced(full, {u, v})
    old_to_new = {old: new for new, old in enumerate(keep)}
    d = distances(graph)
    assert d.shape == (48, 48)

    def incidence(vertices: list[int]) -> sp.Matrix:
        return sp.Matrix([[int(z in full[a]) for z in cell_z] for a in vertices])

    ra, rb, rc = incidence(cell_a), incidence(cell_b), incidence(cell_c)
    assert ra * ra.T == 5 * sp.eye(6)
    assert rb * rb.T == 5 * sp.eye(6)
    assert rc * rc.T == 6 * sp.eye(5)
    assert ra * rb.T == sp.ones(6) - sp.eye(6)
    assert ra * rc.T == sp.ones(6, 5)
    assert rb * rc.T == sp.ones(6, 5)

    cells = [[w], cell_a, cell_b, cell_c, cell_z]
    quotient = sp.Matrix.hstack(
        *[vector(old_to_new, 48, {old: 1 for old in cell}) for cell in cells]
    )

    zero_a = []
    for i in range(5):
        x = sp.zeros(6, 1)
        x[i], x[-1] = 1, -1
        zero_a.append(x)

    symmetric, antisymmetric = [], []
    for x in zero_a:
        p, q = ra.T * x, rb.T * x
        symmetric.extend([
            vector(old_to_new, 48, {
                **{a: x[i] for i, a in enumerate(cell_a)},
                **{b: x[i] for i, b in enumerate(cell_b)},
            }),
            vector(old_to_new, 48, {z: (p + q)[i] for i, z in enumerate(cell_z)}),
        ])
        antisymmetric.extend([
            vector(old_to_new, 48, {
                **{a: x[i] for i, a in enumerate(cell_a)},
                **{b: -x[i] for i, b in enumerate(cell_b)},
            }),
            vector(old_to_new, 48, {z: (p - q)[i] for i, z in enumerate(cell_z)}),
        ])
    symmetric_basis = sp.Matrix.hstack(*symmetric)
    antisymmetric_basis = sp.Matrix.hstack(*antisymmetric)

    common_columns = []
    for i in range(4):
        y = sp.zeros(5, 1)
        y[i], y[-1] = 1, -1
        image = rc.T * y
        common_columns.extend([
            vector(old_to_new, 48, {c: y[j] for j, c in enumerate(cell_c)}),
            vector(old_to_new, 48, {z: image[j] for j, z in enumerate(cell_z)}),
        ])
    common_basis = sp.Matrix.hstack(*common_columns)

    kernel_vectors = ra.col_join(rb).col_join(rc).nullspace()
    assert len(kernel_vectors) == 15
    kernel_basis = sp.Matrix.hstack(*[
        vector(old_to_new, 48, {z: x[i] for i, z in enumerate(cell_z)})
        for x in kernel_vectors
    ])

    blocks = [quotient, symmetric_basis, antisymmetric_basis, common_basis, kernel_basis]
    dims = [5, 10, 10, 8, 15]
    assert [block.cols for block in blocks] == dims
    for i, left in enumerate(blocks):
        for right in blocks[i + 1:]:
            assert left.T * right == sp.zeros(left.cols, right.cols)
    complete = sp.Matrix.hstack(*blocks)
    assert complete.shape == (48, 48)
    assert complete.rank() == 48

    qrep = representation(d, quotient)
    srep = representation(d, symmetric_basis)
    arep = representation(d, antisymmetric_basis)
    crep = representation(d, common_basis)
    krep = representation(d, kernel_basis)
    assert srep == sp.diag(*([sp.Matrix([[-4, -4], [-1, 0]])] * 5))
    assert arep == sp.diag(*([sp.Matrix([[-2, -6], [-1, -2]])] * 5))
    assert crep == sp.diag(*([sp.Matrix([[-2, -6], [-1, -1]])] * 4))
    assert sp.factor(krep.charpoly(X).as_expr()) == (X - 1) ** 4 * (X + 4) ** 11

    quotient_factor = (X - 4) * (
        X**4 - 88 * X**3 - 125 * X**2 + 1740 * X - 778
    )
    assert sp.Poly(qrep.charpoly(X).as_expr() - quotient_factor, X).is_zero
    expected = (
        quotient_factor
        * (X**2 + 4 * X - 4) ** 5
        * (X**2 + 4 * X - 2) ** 5
        * (X + 4) ** 15
        * (X - 1) ** 8
    )
    assert sp.Poly(d.charpoly(X).as_expr() - expected, X).is_zero
    return {
        "cell_sizes": "1,6,6,5,30",
        "module_dimensions": str(dims),
        "complete_basis_rank": str(complete.rank()),
        "quotient_factor": str(sp.factor(quotient_factor)),
        "kernel_factor": str(sp.factor(krep.charpoly(X).as_expr())),
        "distance_characteristic_polynomial": str(sp.factor(expected)),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "generic_symbolic_accounting": generic_accounting(),
        "k7_exact_direct_sum": k7_direct_sum(),
    }
    print("nonadjacent puncture direct-sum audit: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
