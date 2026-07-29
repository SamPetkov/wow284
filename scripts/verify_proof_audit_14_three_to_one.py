#!/usr/bin/env python3
"""Independent replay of the three-to-one integral excess theorem.

This verifier deliberately does not import verify_three_to_one_excess_bound.py.
The regular least-eigenvalue-at-least-minus-two classification is treated as an
external theorem; all subsequent symbolic and finite arithmetic is recomputed.
"""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

X = sp.symbols("x")
K, N, R = sp.symbols("k n r", integer=True)


def constants(k: int) -> tuple[int, int]:
    return (k + 2) ** 2 * (k**2 + 3), 12 * k + 27


def excess(k: int, n: int) -> int:
    c, d = constants(k)
    return 2 * c - d * n


def divisors(value: int) -> list[int]:
    value = abs(value)
    output: list[int] = []
    for candidate in range(1, math.isqrt(value) + 1):
        if value % candidate:
            continue
        output.append(candidate)
        if candidate * candidate != value:
            output.append(value // candidate)
    return sorted(output)


def linear_remainder(t: int) -> int:
    k = sp.symbols("k")
    c = (k + 2) ** 2 * (k**2 + 3)
    d = 12 * k + 27
    value = sp.expand(18**4 * (2 * c - d * t).subs(k, -sp.Rational(41, 18)))
    if not value.is_Integer:
        raise AssertionError("linear remainder is not integral")
    return int(value)


def necessary_m_values(t: int) -> list[tuple[int, int]]:
    return [
        (m, (m - 41) // 18)
        for m in divisors(linear_remainder(t))
        if m >= 149 and m % 18 == 5
    ]


def symbolic_replay() -> dict[str, str]:
    c = (K + 2) ** 2 * (K**2 + 3)
    d = 12 * K + 27
    bound = sp.factor(6 * c / (1 + 3 * d))
    expected = sp.factor(3 * c / (18 * K + 41))
    if sp.simplify(bound - expected) != 0:
        raise AssertionError("wrong three-to-one bound")

    lp = c / (6 * (K + 2))
    improvement = sp.factor(lp - expected)
    target = sp.factor(5 * (K + 2) * (K**2 + 3) / (6 * (18 * K + 41)))
    if sp.simplify(improvement - target) != 0:
        raise AssertionError("wrong LP defect improvement")

    division = sp.expand(
        128 * (2 * c - R)
        - (4 * K + 9) * (64 * K**3 + 112 * K**2 + 196 * K + 327)
    )
    if division != 129 - 128 * R:
        raise AssertionError("wrong 4k+9 remainder")

    x, e = sp.symbols("x e", nonnegative=True)
    rho = (1 + x) / 2
    gram = sp.expand(
        2 * x * (R + R**2 * rho - 2 * e) - R**2 * (1 - x) ** 2
    )
    target_gram = sp.expand(2 * x * R + R**2 * (3 * x - 1) - 4 * x * e)
    if gram != target_gram:
        raise AssertionError("wrong aggregate doubled-edge Gram determinant")

    return {
        "order_bound": str(bound),
        "improvement": str(improvement),
        "division_remainder": str(division),
        "aggregate_gram": str(gram),
    }


def irreducibility_replay() -> dict[str, object]:
    y = sp.symbols("y")
    polynomial = y**4 - 2 * y**3 + (3 - 2 * K) * y**2 + 2

    root_exceptions: set[int] = set()
    for root in (-2, -1, 1, 2):
        for solution in sp.solve(sp.Eq(polynomial.subs(y, root), 0), K):
            if solution.is_integer:
                root_exceptions.add(int(solution))

    quadratic_exceptions: set[int] = set()
    data: list[tuple[int, int, int, int, int]] = []
    for b, d in ((1, 2), (2, 1), (-1, -2), (-2, -1)):
        a = Fraction(2 * b, d - b)
        c = Fraction(-2) - a
        if a.denominator != 1 or c.denominator != 1:
            continue
        coefficient = a.numerator * c.numerator + b + d
        if (3 - coefficient) % 2:
            continue
        k = (3 - coefficient) // 2
        quadratic_exceptions.add(k)
        data.append((a.numerator, b, c.numerator, d, k))

    if root_exceptions != {2, 4}:
        raise AssertionError(f"wrong rational-root exceptions: {root_exceptions}")
    if quadratic_exceptions != {4, 7}:
        raise AssertionError(f"wrong quadratic exceptions: {quadratic_exceptions}")

    for k in (44, 62, 158):
        g = (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k - 2)) + 2
        factors = sp.factor_list(g)[1]
        if len(factors) != 1 or sp.Poly(factors[0][0], X).degree() != 4:
            raise AssertionError(f"exceptional quartic reducible at k={k}")

    dimensions = (7406, 10219, 332373)
    if any(value % 4 == 0 for value in dimensions):
        raise AssertionError("exceptional primary dimension became divisible by four")

    return {
        "root_exceptions": sorted(root_exceptions),
        "quadratic_exceptions": sorted(quadratic_exceptions),
        "factor_data": data,
        "primary_dimensions": dimensions,
    }


def doubled_edge_replay() -> dict[str, object]:
    expected_constants = {1: 167642, 2: 202634}
    expected_candidates = {1: [], 2: [(1427, 77)]}
    for t in (1, 2):
        if linear_remainder(t) != expected_constants[t]:
            raise AssertionError(f"wrong doubled-edge remainder at t={t}")
        if necessary_m_values(t) != expected_candidates[t]:
            raise AssertionError(f"wrong doubled-edge candidate list at t={t}")

    k = 77
    c, d = constants(k)
    numerator = 2 * c - 2 * d
    denominator = 1 + 3 * d
    if numerator % denominator:
        raise AssertionError("expected k=77 arithmetic candidate disappeared")
    r = numerator // denominator
    n = 3 * r + 2
    if (n, r) != (77831, 25943):
        raise AssertionError("wrong k=77 candidate")
    if (k * n) % 2 == 0:
        raise AssertionError("k=77 candidate no longer violates handshake parity")

    return {
        "remainders": expected_constants,
        "candidates": expected_candidates,
        "parity_obstruction": (k, n, r),
    }


def component_count_replay() -> dict[int, object]:
    expected_constants = {
        1: 167642,
        2: 202634,
        3: 237626,
        4: 272618,
        5: 307610,
        6: 342602,
    }
    expected_candidates = {
        1: [],
        2: [(1427, 77)],
        3: [(6989, 386)],
        4: [],
        5: [],
        6: [],
    }
    output: dict[int, object] = {}
    for t in range(1, 7):
        if linear_remainder(t) != expected_constants[t]:
            raise AssertionError(f"wrong component remainder at t={t}")
        candidates = necessary_m_values(t)
        if candidates != expected_candidates[t]:
            raise AssertionError(f"wrong component candidate list at t={t}")

        survivors: list[tuple[int, int, int]] = []
        for _, k in candidates:
            c, d = constants(k)
            numerator = 2 * c - d * t
            denominator = 1 + 3 * d
            if numerator % denominator:
                continue
            r = numerator // denominator
            n = 3 * r + t
            if r > 0 and n >= k * k + 2 and (k * n) % 2 == 0:
                survivors.append((k, n, r))
        if survivors:
            raise AssertionError(f"component-count case survived: {t}, {survivors}")
        output[t] = {"constant": expected_constants[t], "candidates": candidates}
    return output


def connected_root_replay() -> dict[str, object]:
    regular: list[tuple[int, int, int, int]] = []
    for v in range(2, 12):
        for q in range(2, v):
            if (q * v) % 2:
                continue
            n = q * v // 2
            r = n - 4 * q
            if n >= 38 and r > 0 and n > 3 * r:
                regular.append((q, v, n, r))
    expected_regular = [
        (8, 10, 40, 8),
        (9, 10, 45, 9),
        (8, 11, 44, 12),
        (10, 11, 55, 15),
    ]
    if regular != expected_regular:
        raise AssertionError(f"wrong regular-root list: {regular}")
    for _, _, n, r in regular:
        for k in range(6, math.isqrt(n - 2) + 1):
            if (k * n) % 2 == 0 and excess(k, n) == r:
                raise AssertionError(f"regular-root case survived: {(k, n, r)}")

    b4: list[tuple[int, int, int, int, int, int]] = []
    for p in range(2, 5):
        for r in range(1, 4 * p):
            n = 2 * (r + 2 * p)
            if n < 38 or not n > 3 * r or n % p or n % 4:
                continue
            q, a = n // 4, n // p
            if p <= q and q <= a:
                b4.append((p, q, a, 4, n, r))
    expected_b4 = [
        (4, 10, 10, 4, 40, 12),
        (4, 11, 11, 4, 44, 14),
    ]
    if b4 != expected_b4:
        raise AssertionError(f"wrong b=4 semiregular list: {b4}")
    for _, _, _, _, n, r in b4:
        if excess(6, n) == r:
            raise AssertionError("b=4 semiregular case survived")

    b3_constants = {12: 552554, 18: 762506}
    for t, expected in b3_constants.items():
        if linear_remainder(t) != expected:
            raise AssertionError(f"wrong b=3 remainder at t={t}")
        odd = expected // 2
        if not sp.isprime(odd) or odd % 18 != 13:
            raise AssertionError(f"wrong b=3 prime residue at t={t}")
        if necessary_m_values(t):
            raise AssertionError(f"b=3 semiregular case survived at t={t}")

    return {
        "regular": regular,
        "b4": b4,
        "b3_remainders": b3_constants,
    }


def two_component_replay() -> dict[str, object]:
    low: dict[int, tuple[str, str]] = {}
    for k in (6, 7, 8):
        c, d = constants(k)
        lower = Fraction(6 * c, 1 + 3 * d)
        upper = Fraction(2 * c, d)
        admissible = [
            n
            for n in range(math.floor(lower) + 1, math.ceil(upper))
            if lower < n < upper and (k * n) % 2 == 0
        ]
        if admissible:
            raise AssertionError(f"low-degree interval survived at k={k}: {admissible}")
        low[k] = (str(lower), str(upper))

    # The lower endpoint exceeds 150 for k>=9.
    m = sp.symbols("m", nonnegative=True)
    lower_margin = sp.expand(
        3 * (K + 2) ** 2 * (K**2 + 3) - 150 * (18 * K + 41)
    )
    shifted = sp.expand(lower_margin.subs(K, m + 9))
    if shifted != 3 * m**4 + 120 * m**3 + 1803 * m**2 + 9378 * m + 42:
        raise AssertionError("wrong k>=9 lower-order margin")

    reciprocal_pairs: list[tuple[int, int]] = []
    for b in range(3, 100):
        for a in range(b, 100):
            if Fraction(1, a) + Fraction(1, b) > Fraction(49, 100):
                reciprocal_pairs.append((a, b))
    expected_pairs = [(3, 3), (4, 3), (5, 3), (6, 3), (4, 4)]
    if reciprocal_pairs != expected_pairs:
        raise AssertionError(f"wrong reciprocal pair list: {reciprocal_pairs}")
    if max(a * b for a, b in reciprocal_pairs) != 18:
        raise AssertionError("wrong reciprocal product maximum")

    offsets = {8: (412586, []), 10: (482570, [(2255, 123)])}
    offset_report: dict[int, object] = {}
    for t, (expected, candidates) in offsets.items():
        if linear_remainder(t) != expected:
            raise AssertionError(f"wrong mixed-component remainder at t={t}")
        actual = necessary_m_values(t)
        if actual != candidates:
            raise AssertionError(f"wrong mixed-component candidates at t={t}")
        survivors: list[tuple[int, int, int]] = []
        for _, k in actual:
            c, d = constants(k)
            numerator = 2 * c - d * t
            denominator = 1 + 3 * d
            if numerator % denominator:
                continue
            r = numerator // denominator
            n = 3 * r + t
            if r > 0 and n >= k * k + 2 and (k * n) % 2 == 0:
                survivors.append((k, n, r))
        if survivors:
            raise AssertionError(f"mixed component case survived: {survivors}")
        offset_report[t] = {"constant": expected, "candidates": actual}

    k = sp.symbols("k")
    c = (k + 2) ** 2 * (k**2 + 3)
    d = 12 * k + 27
    two_line_constant = int(
        sp.expand(24**4 * (2 * c - 8 * d).subs(k, -sp.Rational(55, 24)))
    )
    if two_line_constant != 1792898:
        raise AssertionError("wrong two-line-component remainder")
    two_line_candidates = [
        (value, (value - 55) // 24)
        for value in divisors(two_line_constant)
        if value >= 199 and value % 24 == 7
    ]
    if two_line_candidates:
        raise AssertionError(f"two-line-component case survived: {two_line_candidates}")

    return {
        "low_degree_intervals": low,
        "reciprocal_pairs": reciprocal_pairs,
        "mixed_offsets": offset_report,
        "two_line_constant": two_line_constant,
    }


def order_table_replay() -> dict[int, int]:
    expected = {
        6: 50,
        7: 75,
        8: 108,
        9: 150,
        10: 201,
        11: 263,
        12: 336,
        13: 422,
        14: 521,
        15: 635,
        16: 765,
        17: 911,
        18: 1075,
        19: 1257,
        20: 1459,
        21: 1681,
    }
    actual = {
        k: (3 * (k + 2) ** 2 * (k**2 + 3)) // (18 * k + 41)
        for k in expected
    }
    if actual != expected:
        raise AssertionError(f"wrong order table: {actual}")
    return actual


def robustness_grid() -> dict[str, int]:
    """A finite independent stress test; not used as the proof of the theorem."""
    checked = 0
    scalar_violators = 0
    for k in range(6, 1001):
        c, d = constants(k)
        upper = (2 * c - 1) // d
        lower = k * k + 2
        if upper < lower:
            continue
        for n in range(max(lower, upper - 20), upper + 1):
            if (k * n) % 2:
                continue
            r = excess(k, n)
            if r <= 0:
                continue
            checked += 1
            if n > 3 * r:
                scalar_violators += 1
    # Scalar parameter triples do exist; the classification argument is what
    # excludes graph realizations. Record, rather than silently suppress, them.
    if checked == 0 or scalar_violators == 0:
        raise AssertionError("robustness grid did not exercise the classification regime")
    return {"parameter_triples_checked": checked, "scalar_violators": scalar_violators}


def main() -> None:
    report = {
        "symbolic": symbolic_replay(),
        "irreducibility": irreducibility_replay(),
        "doubled_edge": doubled_edge_replay(),
        "component_count": component_count_replay(),
        "connected_roots": connected_root_replay(),
        "two_components": two_component_replay(),
        "order_table": order_table_replay(),
        "robustness_grid": robustness_grid(),
        "external_input": (
            "regular connected least-eigenvalue-at-least-minus-two classification"
        ),
    }
    print("Proof Audit 14A three-to-one replay: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
