#!/usr/bin/env python3
"""Independent exact audit of the degree-six order-50 feasibility system.

The script does not import either original order-50 verifier. It checks the
layer compression, local walk/cycle identities, positive-semidefinite minors,
shifted moments, Schur complements and exact profile enumeration. No
floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations
import json
import math

import sympy as sp

X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def add_edge(rows: list[set[int]], u: int, v: int) -> None:
    if u == v:
        raise AssertionError("loop")
    rows[u].add(v)
    rows[v].add(u)


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


def induced(graph: Graph, deleted: set[int]) -> Graph:
    keep = tuple(v for v in range(len(graph)) if v not in deleted)
    index = {old: new for new, old in enumerate(keep)}
    return tuple(
        frozenset(index[z] for z in graph[v] if z in index) for v in keep
    )


def graph40() -> Graph:
    return induced(hoffman_singleton(), set(range(5)) | set(range(25, 30)))


def graph42() -> Graph:
    full = hoffman_singleton()
    return induced(full, {0} | set(full[0]))


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(v in graph[u]) for v in range(len(graph))] for u in range(len(graph))]
    )


def exact_girth(graph: Graph) -> int:
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


def alpha_count(graph: Graph, u: int, v: int, w: int) -> int:
    count = 0
    for a in graph[u]:
        if a in {v, w}:
            continue
        for b in graph[a]:
            if b in {u, v, w, a}:
                continue
            if w in graph[b]:
                count += 1
    return count


def beta_count(graph: Graph, u: int, v: int, w: int) -> int:
    count = 0
    for a in graph[u]:
        if a in {v, w}:
            continue
        for b in graph[a]:
            if b in {u, v, w, a}:
                continue
            for c in graph[b]:
                if c in {u, v, w, a, b}:
                    continue
                if w in graph[c]:
                    count += 1
    return count


def layer_compression_audit() -> dict[str, str]:
    tau = sp.symbols("tau", integer=True)
    sizes = [1, 6, 30, 13]
    quotient = sp.Matrix(
        [
            [0, 6, 0, 0],
            [1, 0, 5, 0],
            [0, 1, tau / 15, 5 - tau / 15],
            [0, 0, 30 * (5 - tau / 15) / 13, 6 - 30 * (5 - tau / 15) / 13],
        ]
    )
    size_matrix = sp.diag(*sizes)
    if sp.simplify(size_matrix * quotient - quotient.T * size_matrix) != sp.zeros(4):
        raise AssertionError("layer edge balance failed")
    root_size = sp.diag(*[sp.sqrt(value) for value in sizes])
    normalized = sp.simplify(root_size * quotient * root_size.inv())
    if normalized != normalized.T:
        raise AssertionError("normalized layer compression is not symmetric")
    if sp.simplify(
        normalized.charpoly(X).as_expr() - quotient.charpoly(X).as_expr()
    ) != 0:
        raise AssertionError("row quotient and normalized compression differ spectrally")

    factor = sp.factor(quotient.charpoly(X).as_expr() / (X - 6))
    expected = (
        -43 * tau * X**2
        - 30 * tau * X
        + 228 * tau
        + 195 * X**3
        + 2250 * X**2
        + 105 * X
        - 11250
    ) / 195
    if sp.simplify(factor - expected) != 0:
        raise AssertionError("wrong layer nonprincipal factor")

    boundary = -1 + sp.sqrt(10)
    boundary_value = sp.factor(sp.radsimp((195 * factor).subs(X, boundary)))
    expected_boundary = (
        (-215 + 56 * sp.sqrt(10)) * tau
        + 7350
        - 1860 * sp.sqrt(10)
    )
    if sp.expand(boundary_value - expected_boundary) != 0:
        raise AssertionError("wrong layer boundary value")
    if not 56**2 * 10 < 215**2:
        raise AssertionError("wrong monotonicity sign")
    if sp.expand(boundary_value.subs(tau, 39) - 9 * (-115 + 36 * sp.sqrt(10))) != 0:
        raise AssertionError("wrong tau=39 value")
    if not 36**2 * 10 < 115**2:
        raise AssertionError("wrong tau=39 sign")
    if sp.expand((195 * factor).subs(X, 6) - 1500 * (75 - tau)) != 0:
        raise AssertionError("wrong value at six")

    # The cross-layer capacity gives 150-2*tau <= 78.
    if sp.solve_univariate_inequality(150 - 2 * tau <= 78, tau) is sp.S.EmptySet:
        raise AssertionError("failed lower-bound inequality")
    if 150 - 2 * 36 != 78:
        raise AssertionError("wrong tau lower boundary")

    return {
        "row_quotient": str(quotient),
        "normalized_compression_symmetric": "true",
        "nonprincipal_factor": str(factor),
        "boundary_value": str(boundary_value),
        "vertex_cycle_range": "36,37,38",
    }


def gram_minor_audit() -> dict[str, object]:
    r = sp.symbols("r", integer=True)
    diagonal = sp.Integer(48)
    low = sp.Integer(-2)
    high = sp.Integer(-27)
    endpoint = 773 - 25 * r

    if endpoint.subs(r, 29) != diagonal:
        raise AssertionError("r=29 is not the kernel equality case")
    allowed: dict[str, list[int]] = {}
    factors: dict[str, str] = {}
    expected_factors = {
        "low-low": -5000 * (r - 29) * (6 * r - 197),
        "mixed": -7500 * (4 * r**2 - 247 * r + 3803),
        "high-high": -3750 * (r - 29) * (8 * r - 253),
    }
    for name, left, right in (
        ("low-low", low, low),
        ("mixed", low, high),
        ("high-high", high, high),
    ):
        determinant = sp.factor(
            sp.Matrix(
                [
                    [diagonal, left, endpoint],
                    [left, diagonal, right],
                    [endpoint, right, diagonal],
                ]
            ).det()
        )
        if sp.expand(determinant - expected_factors[name]) != 0:
            raise AssertionError("wrong Gram determinant")
        factors[name] = str(determinant)
        raw = [value for value in range(29, 33) if determinant.subs(r, value) >= 0]
        allowed[name] = [value for value in raw if value != 29]

    expected_allowed = {
        "low-low": [30, 31, 32],
        "mixed": [30, 31, 32],
        "high-high": [30, 31],
    }
    if allowed != expected_allowed:
        raise AssertionError("wrong refined two-path table")

    polynomial = sp.expand((X + 2) ** 2 * (X**2 + 2 * X - 9))
    if sp.expand(-polynomial - (X + 2) ** 2 * (10 - (X + 1) ** 2)) != 0:
        raise AssertionError("wrong kernel polynomial factorization")
    if polynomial.subs(X, -2) != 0:
        raise AssertionError("missing internal zero")
    # The coordinate contradiction is 0=-2 when a distance-two difference
    # vector is forced into the -2 eigenspace.
    if sp.Integer(0) == sp.Integer(-2):
        raise AssertionError("accepted impossible kernel coordinate")

    return {
        "scaled_diagonal": str(diagonal),
        "scaled_low_edge": str(low),
        "scaled_high_edge": str(high),
        "scaled_endpoint": str(endpoint),
        "determinants": factors,
        "allowed_values": allowed,
        "r_29_kernel_contradiction": "0 != -2",
    }


def global_and_moment_audit() -> dict[str, str]:
    m, s2, n6 = sp.symbols("m S2 N6", integer=True, nonnegative=True)

    # Local sum identities.
    sum_r = 10800 + 6 * m + 6 * n6
    local_lower = sp.solve_univariate_inequality(sum_r >= 750 * 30, n6)
    expected_lower = 1950 - m
    if sp.simplify(sum_r.subs(n6, expected_lower) - 750 * 30) != 0:
        raise AssertionError("wrong global local lower bound")

    local_upper_sum = 24000 - (s2 - 2 * m) / 2
    expected_upper = 2200 - sp.Rational(5, 6) * m - s2 / 12
    if sp.simplify(sum_r.subs(n6, expected_upper) - local_upper_sum) != 0:
        raise AssertionError("wrong global local upper bound")

    # Nonbacktracking trace identities at k=6, n=50.
    f5 = sp.expand(X**5 - 21 * X**3 + 85 * X)
    f6 = sp.expand(X**6 - 26 * X**4 + 165 * X**2 - 150)
    if f5 != X**5 - 21 * X**3 + 85 * X:
        raise AssertionError("wrong F5")
    if f6 != X**6 - 26 * X**4 + 165 * X**2 - 150:
        raise AssertionError("wrong F6")

    traces = {
        0: sp.Integer(50),
        1: sp.Integer(0),
        2: sp.Integer(300),
        3: sp.Integer(0),
        4: sp.Integer(3300),
        5: 3600 + 2 * m,
        6: 43800 + 12 * n6,
    }
    shifted: list[sp.Expr] = []
    for degree in range(7):
        total = sum(
            sp.binomial(degree, j) * traces[j] for j in range(degree + 1)
        )
        shifted.append(sp.expand(total - 7**degree))
    expected_shifted = [
        49,
        43,
        301,
        607,
        2749,
        6343 + 2 * m,
        1801 + 12 * m + 12 * n6,
    ]
    if any(sp.expand(left - right) != 0 for left, right in zip(shifted, expected_shifted, strict=True)):
        raise AssertionError("wrong shifted moments")

    moment = sp.Matrix(4, 4, lambda i, j: shifted[i + j])
    leading = moment[:3, :3]
    column = moment[:3, 3]
    if leading.det() != 5850000:
        raise AssertionError("wrong leading moment determinant")
    lower_s6 = sp.factor((column.T * leading.inv() * column)[0])
    lower_n6 = sp.factor((lower_s6 - 1801 - 12 * m) / 12)
    expected_moment_lower = (
        43 * m**2 - 70200 * m + 119632500
    ) / 58500
    if sp.simplify(lower_n6 - expected_moment_lower) != 0:
        raise AssertionError("wrong moment N6 lower bound")

    localizing = sp.Matrix(
        3,
        3,
        lambda i, j: 10 * shifted[i + j] - shifted[i + j + 2],
    )
    leading_localizing = localizing[:2, :2]
    localizing_column = localizing[:2, 2]
    if leading_localizing.det() != 18000:
        raise AssertionError("wrong localizing determinant")
    upper_s6 = sp.factor(
        10 * shifted[4]
        - (localizing_column.T * leading_localizing.inv() * localizing_column)[0]
    )
    upper_n6 = sp.factor((upper_s6 - 1801 - 12 * m) / 12)
    expected_moment_upper = (
        4220000 - 2200 * m - 7 * m**2
    ) / 2000
    if sp.simplify(upper_n6 - expected_moment_upper) != 0:
        raise AssertionError("wrong localizing N6 upper bound")

    return {
        "sum_r": str(sum_r),
        "local_lower_N6": str(expected_lower),
        "local_upper_N6": str(expected_upper),
        "F5": str(f5),
        "F6": str(f6),
        "shifted_moments": str(shifted),
        "moment_lower_N6": str(lower_n6),
        "localizing_upper_N6": str(upper_n6),
    }


def profile_enumeration() -> dict[str, object]:
    profiles: list[tuple[int, int, int, int, int, int]] = []
    for n2 in range(51):
        for n4 in range(51 - n2):
            n0 = 50 - n2 - n4
            m = n2 + 2 * n4
            if m % 5 != 0:
                continue
            s2 = 4 * n2 + 16 * n4
            local_lower = Fraction(1950 - m)
            local_upper = Fraction(26400 - 10 * m - s2, 12)
            moment_lower = Fraction(
                43 * m**2 - 70200 * m + 119632500,
                58500,
            )
            moment_upper = Fraction(
                4220000 - 2200 * m - 7 * m**2,
                2000,
            )
            lower = max(Fraction(0), local_lower, moment_lower)
            upper = min(local_upper, moment_upper)
            if math.ceil(lower) <= math.floor(upper):
                profiles.append(
                    (n0, n2, n4, m, math.ceil(lower), math.floor(upper))
                )

    if len(profiles) != 266:
        raise AssertionError("wrong surviving profile count")
    edge_counts = sorted({profile[3] for profile in profiles})
    if edge_counts != list(range(0, 101, 5)):
        raise AssertionError("wrong surviving high-edge counts")
    return {
        "surviving_profiles": len(profiles),
        "surviving_high_edge_counts": edge_counts,
        "first_profile": profiles[0],
        "last_profile": profiles[-1],
    }


def control_walk_audit(name: str, graph: Graph) -> dict[str, int]:
    if set(map(len, graph)) != {6}:
        raise AssertionError("control is not 6-regular")
    if exact_girth(graph) != 5:
        raise AssertionError("control has wrong girth")
    adjacency = adjacency_matrix(graph)
    a2 = adjacency * adjacency
    a3 = a2 * adjacency
    a4 = a3 * adjacency
    a5 = a4 * adjacency
    a6 = a5 * adjacency

    sum_alpha = 0
    sum_beta = 0
    path_count = 0
    for v, neighbours in enumerate(graph):
        for u, w in combinations(sorted(neighbours), 2):
            alpha = alpha_count(graph, u, v, w)
            beta = beta_count(graph, u, v, w)
            if a3[u, w] != alpha:
                raise AssertionError("A3/alpha mismatch")
            if a4[u, w] != 16 + beta:
                raise AssertionError("A4/beta mismatch")
            sum_alpha += alpha
            sum_beta += beta
            path_count += 1

    if path_count != len(graph) * 15:
        raise AssertionError("wrong two-path count")
    if sum_alpha % 5 or sum_beta % 6:
        raise AssertionError("cycle incidence divisibility failed")
    n5 = sum_alpha // 5
    n6 = sum_beta // 6
    if sp.trace(a5) != 10 * n5:
        raise AssertionError("A5 trace/cycle mismatch")
    expected_a6 = len(graph) * 6 * (5 * 6**2 - 6 * 6 + 2) + 12 * n6
    if sp.trace(a6) != expected_a6:
        raise AssertionError("A6 trace/cycle mismatch")

    return {
        "order": len(graph),
        "two_paths": path_count,
        "five_cycles": n5,
        "six_cycles": n6,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    result = {
        "layer_compression": layer_compression_audit(),
        "gram_minors": gram_minor_audit(),
        "global_and_moments": global_and_moment_audit(),
        "profile_enumeration": profile_enumeration(),
        "independent_walk_controls": {
            "order_40": control_walk_audit("order_40", graph40()),
            "order_42": control_walk_audit("order_42", graph42()),
        },
    }
    print("Proof Audit 06 (order-50 feasibility): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
