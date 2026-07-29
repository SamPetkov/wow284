#!/usr/bin/env python3
"""Independent exact audit of the three-to-one integral excess theorem.

The regular least-eigenvalue-at-least-minus-two classification is an external
input. Every polynomial identity, Gram compression, divisibility reduction,
and line-root arithmetic step after that input is checked exactly.
"""
from __future__ import annotations

from fractions import Fraction
import math

import sympy as sp

X = sp.symbols("x")
K, N, R = sp.symbols("k n r", integer=True)


def constants(k: int) -> tuple[int, int, int]:
    h = 6 * (k + 2)
    c = (k + 2) ** 2 * (k**2 + 3)
    d = 2 * h + 3  # 12k+27
    return h, c, d


def excess_parameter(k: int, n: int) -> int:
    _, c, d = constants(k)
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


def translated_irreducibility_audit() -> dict[str, object]:
    """Prove the exact exceptional set for g_k(x)+2 over Q."""
    y = sp.symbols("y")
    q = y**4 - 2 * y**3 + (3 - 2 * K) * y**2 + 2

    linear_exceptional: set[int] = set()
    for root in (-2, -1, 1, 2):
        value = sp.expand(q.subs(y, root))
        solutions = sp.solve(sp.Eq(value, 0), K)
        for item in solutions:
            if item.is_integer:
                linear_exceptional.add(int(item))

    quadratic_exceptional: set[int] = set()
    pairs = ((1, 2), (2, 1), (-1, -2), (-2, -1))
    factor_data: list[tuple[int, int, int, int, int]] = []
    for b, d in pairs:
        # c=-2-a and a*d+b*c=0.
        denominator = d - b
        if denominator == 0:
            continue
        a = Fraction(2 * b, denominator)
        c = Fraction(-2) - a
        if a.denominator != 1 or c.denominator != 1:
            continue
        a_i, c_i = a.numerator, c.numerator
        rhs = a_i * c_i + b + d
        # rhs = 3-2k
        if (3 - rhs) % 2:
            continue
        k = (3 - rhs) // 2
        quadratic_exceptional.add(k)
        factor_data.append((b, d, a_i, c_i, k))

    if linear_exceptional != {2, 4}:
        raise AssertionError(f"wrong rational-root exceptions: {linear_exceptional}")
    if quadratic_exceptional != {4, 7}:
        raise AssertionError(
            f"wrong monic-quadratic exceptions: {quadratic_exceptional}"
        )

    for k in (44, 62, 158):
        polynomial = sp.Poly(
            (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k - 2)) + 2,
            X,
            domain=sp.QQ,
        )
        factors = sp.factor_list(polynomial.as_expr())[1]
        if len(factors) != 1 or factors[0][0].as_poly(X).degree() != 4:
            raise AssertionError(f"g_{k}+2 is not irreducible")

    return {
        "linear_exceptions": sorted(linear_exceptional),
        "quadratic_exceptions": sorted(quadratic_exceptional),
        "factor_data": factor_data,
    }


def symbolic_audit() -> dict[str, str]:
    c = (K + 2) ** 2 * (K**2 + 3)
    h = 6 * (K + 2)
    d = 2 * h + 3
    r = sp.expand(2 * c - d * N)

    division_identity = sp.expand(
        128 * (2 * c - R)
        - (4 * K + 9) * (64 * K**3 + 112 * K**2 + 196 * K + 327)
    )
    if division_identity != 129 - 128 * R:
        raise AssertionError("wrong divisibility remainder")

    bound = sp.factor(3 * c / (18 * K + 41))
    derived = sp.factor(6 * c / (1 + 3 * d))
    if sp.simplify(bound - derived) != 0:
        raise AssertionError("wrong three-to-one order bound")

    lp = sp.factor(c / h)
    improvement = sp.factor(lp - bound)
    expected_improvement = sp.factor(
        5 * (K + 2) * (K**2 + 3) / (6 * (18 * K + 41))
    )
    if sp.simplify(improvement - expected_improvement) != 0:
        raise AssertionError("wrong LP improvement identity")

    x = sp.symbols("x", positive=True)
    rho = (1 + x) / 2
    pair_norm = 2 * x
    third_norm = (3 + x) / 2
    if sp.simplify(pair_norm * third_norm - x * (3 + x)) != 0:
        raise AssertionError("wrong pair-vector Cauchy product")

    e_w = sp.symbols("e_W", nonnegative=True)
    aggregate = sp.expand(
        2 * x * (R + R**2 * rho - 2 * e_w)
        - R**2 * (1 - x) ** 2
    )
    expected_aggregate = sp.expand(
        2 * x * R + R**2 * (3 * x - 1) - 4 * x * e_w
    )
    if aggregate != expected_aggregate:
        raise AssertionError("wrong doubled-edge aggregate Gram determinant")

    return {
        "r": str(r),
        "divisibility_remainder": str(division_identity),
        "order_bound": str(bound),
        "improvement": str(improvement),
        "aggregate_gram": str(aggregate),
    }


def nonpositive_r_audit() -> dict[str, object]:
    """Replay the r>0 classification arithmetic with the uniform quartic lemma."""
    if not sp.isprime(277):
        raise AssertionError("277 is not prime")
    k44 = 44
    h44, c44, _ = constants(k44)
    if 6 * k44 + 13 != 277 or c44 % (h44 + 1):
        raise AssertionError("wrong cocktail reduction")
    n44 = c44 // (h44 + 1)
    if n44 != 14812 or (n44 // 2) % 4 == 0:
        raise AssertionError("wrong cocktail multiplicity obstruction")

    if not sp.isprime(641):
        raise AssertionError("641 is not prime")
    k158 = 158
    _, c158, d158 = constants(k158)
    if 4 * k158 + 9 != 641 or (2 * c158 + 4) % d158:
        raise AssertionError("wrong semiregular exceptional reduction")
    n158 = (2 * c158 + 4) // d158
    a158 = n158 // 2
    if n158 != 664748 or (a158 - 1) % 4 == 0:
        raise AssertionError("wrong semiregular multiplicity obstruction")

    cases: dict[int, list[tuple[int, int]]] = {}
    for r in (-2, -1, 0):
        candidates: list[tuple[int, int]] = []
        for divisor in divisors(129 - 128 * r):
            if divisor < 33 or (divisor - 9) % 4:
                continue
            k = (divisor - 9) // 4
            _, c, d = constants(k)
            if (2 * c - r) % d:
                continue
            n = (2 * c - r) // d
            if n >= k * k + 2 and (k * n) % 2 == 0:
                candidates.append((k, n))
        cases[r] = candidates
    if cases != {-2: [], -1: [(62, 40875)], 0: []}:
        raise AssertionError(f"wrong nonpositive two-component cases: {cases}")

    k62, n62 = cases[-1][0]
    if n62 != 20437 + 20438 or (20438 // 2) % 4 == 0:
        raise AssertionError("wrong two-component multiplicity obstruction")

    for k in (k44, k62, k158):
        if k == 7:
            raise AssertionError("unexpected reducible exceptional degree")

    return {
        "cocktail": (k44, n44, n44 // 2),
        "semiregular": (k158, n158, a158 - 1),
        "two_component": (k62, n62, 20438 // 2),
    }


def linear_remainder_constant(t: int) -> int:
    """Return 18^4*(2C-Dt) at k=-41/18."""
    k = sp.symbols("k")
    c = (k + 2) ** 2 * (k**2 + 3)
    d = 12 * k + 27
    value = sp.expand(18**4 * (2 * c - d * t).subs(k, -sp.Rational(41, 18)))
    if not value.is_Integer:
        raise AssertionError("nonintegral linear remainder constant")
    return int(value)


def possible_linear_divisors(t: int) -> list[tuple[int, int]]:
    """Necessary (m,k) pairs from m=18k+41 dividing the fixed remainder."""
    constant = abs(linear_remainder_constant(t))
    return [
        (m, (m - 41) // 18)
        for m in divisors(constant)
        if m >= 149 and m % 18 == 5
    ]


def doubled_edge_audit() -> dict[str, object]:
    constants_expected = {1: 167642, 2: 202634}
    divisors_expected = {1: [], 2: [(1427, 77)]}
    for t, expected in constants_expected.items():
        if linear_remainder_constant(t) != expected:
            raise AssertionError(f"wrong t={t} remainder constant")
        if possible_linear_divisors(t) != divisors_expected[t]:
            raise AssertionError(f"wrong t={t} divisor candidates")

    k = 77
    _, c, d = constants(k)
    t = 2
    denominator = 1 + 3 * d
    numerator = 2 * c - d * t
    if numerator % denominator:
        raise AssertionError("k=77 is not the expected integer candidate")
    r = numerator // denominator
    n = 3 * r + t
    if (r, n) != (25943, 77831):
        raise AssertionError("wrong k=77 candidate")
    if (k * n) % 2 == 0:
        raise AssertionError("k=77 candidate does not violate handshake parity")

    return {
        "remainder_constants": constants_expected,
        "necessary_divisors": divisors_expected,
        "parity_exception": (k, n, r),
    }


def component_count_audit() -> dict[str, object]:
    expected_constants = {
        1: 167642,
        2: 202634,
        3: 237626,
        4: 272618,
        5: 307610,
        6: 342602,
    }
    expected_divisors = {
        1: [],
        2: [(1427, 77)],
        3: [(6989, 386)],
        4: [],
        5: [],
        6: [],
    }
    report: dict[int, object] = {}
    for t in range(1, 7):
        constant = linear_remainder_constant(t)
        candidates = possible_linear_divisors(t)
        if constant != expected_constants[t] or candidates != expected_divisors[t]:
            raise AssertionError(f"wrong component-count arithmetic at t={t}")

        survivors: list[tuple[int, int, int]] = []
        for _, k in candidates:
            _, c, d = constants(k)
            numerator = 2 * c - d * t
            denominator = 1 + 3 * d
            if numerator % denominator:
                continue
            r = numerator // denominator
            n = 3 * r + t
            if r > 0 and n >= k * k + 2 and (k * n) % 2 == 0:
                survivors.append((k, n, r))
        if survivors:
            raise AssertionError(f"three-component offset survived: {t}, {survivors}")
        report[t] = {"constant": constant, "candidates": candidates}
    return report


def connected_regular_root_audit() -> list[tuple[int, int, int, int]]:
    cases: list[tuple[int, int, int, int]] = []
    for v in range(2, 12):
        for q in range(2, v):
            if (q * v) % 2:
                continue
            n = q * v // 2
            r = n - 4 * q
            if n >= 38 and r > 0 and n > 3 * r:
                cases.append((q, v, n, r))
    expected = [
        (8, 10, 40, 8),
        (9, 10, 45, 9),
        (8, 11, 44, 12),
        (10, 11, 55, 15),
    ]
    if cases != expected:
        raise AssertionError(f"wrong connected regular-root cases: {cases}")

    survivors: list[tuple[int, int, int]] = []
    for _, _, n, r in cases:
        for k in range(6, math.isqrt(n - 2) + 1):
            if (k * n) % 2 == 0 and excess_parameter(k, n) == r:
                survivors.append((k, n, r))
    if survivors:
        raise AssertionError(f"connected regular-root case survived: {survivors}")
    return cases


def connected_semiregular_root_audit() -> dict[str, object]:
    b4_cases: list[tuple[int, int, int, int, int, int]] = []
    b = 4
    for p in range(2, b + 1):
        for r in range(1, 4 * p):
            numerator = b * (r + 2 * p)
            if numerator % (b - 2):
                continue
            n = numerator // (b - 2)
            if n < 38 or not n > 3 * r or n % p or n % b:
                continue
            q = n // b
            a = n // p
            if p <= q and p <= b and q <= a:
                b4_cases.append((p, q, a, b, n, r))
    expected_b4 = [
        (4, 10, 10, 4, 40, 12),
        (4, 11, 11, 4, 44, 14),
    ]
    if b4_cases != expected_b4:
        raise AssertionError(f"wrong b=4 cases: {b4_cases}")
    for _, _, _, _, n, r in b4_cases:
        if excess_parameter(6, n) == r:
            raise AssertionError("b=4 case survived at k=6")

    constants_expected = {12: 552554, 18: 762506}
    for t, constant in constants_expected.items():
        if linear_remainder_constant(t) != constant:
            raise AssertionError(f"wrong semiregular remainder at t={t}")
        if not sp.isprime(constant // 2):
            raise AssertionError(f"expected prime cofactor at t={t}")
        if (constant // 2) % 18 != 13:
            raise AssertionError(f"wrong prime residue at t={t}")
        if possible_linear_divisors(t):
            raise AssertionError(f"semiregular divisor survived at t={t}")

    return {"b4_cases": b4_cases, "b3_remainders": constants_expected}


def two_component_audit() -> dict[str, object]:
    low_intervals: dict[int, tuple[Fraction, Fraction]] = {}
    for k in (6, 7, 8):
        _, c, d = constants(k)
        lower = Fraction(6 * c, 1 + 3 * d)
        upper = Fraction(2 * c, d)
        low_intervals[k] = (lower, upper)
        integers = [
            n
            for n in range(math.floor(lower) + 1, math.ceil(upper))
            if lower < n < upper and (k * n) % 2 == 0
        ]
        if integers:
            raise AssertionError(f"low-degree order interval survived: {k}, {integers}")

    n = sp.symbols("n", integer=True, positive=True)
    if sp.expand(100 * (2 * n + 1) - 49 * (4 * n + 5)) != 4 * n - 145:
        raise AssertionError("wrong reciprocal lower-bound identity")

    reciprocal_pairs: list[tuple[int, int]] = []
    for b in range(3, 100):
        for a in range(b, 100):
            if Fraction(1, a) + Fraction(1, b) > Fraction(49, 100):
                reciprocal_pairs.append((a, b))
    expected_pairs = [(3, 3), (4, 3), (5, 3), (6, 3), (4, 4)]
    if reciprocal_pairs != expected_pairs:
        raise AssertionError(f"wrong >49/100 reciprocal list: {reciprocal_pairs}")
    if max(a * b for a, b in reciprocal_pairs) != 18:
        raise AssertionError("wrong semiregular product maximum")

    offset_expected = {8: (412586, []), 10: (482570, [(2255, 123)])}
    offset_report: dict[int, object] = {}
    for t, (constant, candidates) in offset_expected.items():
        if linear_remainder_constant(t) != constant:
            raise AssertionError(f"wrong two-component remainder at t={t}")
        actual = possible_linear_divisors(t)
        if actual != candidates:
            raise AssertionError(f"wrong two-component candidates at t={t}: {actual}")
        survivors: list[tuple[int, int, int]] = []
        for _, k in actual:
            _, c, d = constants(k)
            numerator = 2 * c - d * t
            denominator = 1 + 3 * d
            if numerator % denominator:
                continue
            r = numerator // denominator
            order = 3 * r + t
            if r > 0 and order >= k * k + 2 and (k * order) % 2 == 0:
                survivors.append((k, order, r))
        if survivors:
            raise AssertionError(f"mixed component type survived: {t}, {survivors}")
        offset_report[t] = {"constant": constant, "candidates": actual}

    k = sp.symbols("k")
    c = (k + 2) ** 2 * (k**2 + 3)
    d = 12 * k + 27
    constant_two = sp.expand(
        24**4 * (2 * c - 8 * d).subs(k, -sp.Rational(55, 24))
    )
    if int(constant_two) != 1792898:
        raise AssertionError("wrong two-line-component remainder")
    candidates_two = [
        (m, (m - 55) // 24)
        for m in divisors(int(constant_two))
        if m >= 199 and m % 24 == 7
    ]
    if candidates_two:
        raise AssertionError(f"two L(K_d,2) components survived: {candidates_two}")

    return {
        "low_intervals": {k: (str(a), str(b)) for k, (a, b) in low_intervals.items()},
        "reciprocal_pairs": reciprocal_pairs,
        "mixed_offsets": offset_report,
        "two_line_constant": int(constant_two),
    }


def order_table() -> dict[int, int]:
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
    actual: dict[int, int] = {}
    for k in expected:
        _, c, _ = constants(k)
        actual[k] = (3 * c) // (18 * k + 41)
    if actual != expected:
        raise AssertionError(f"wrong three-to-one order table: {actual}")
    return actual


def main() -> None:
    report = {
        "symbolic": symbolic_audit(),
        "uniform_irreducibility": translated_irreducibility_audit(),
        "nonpositive_r": nonpositive_r_audit(),
        "doubled_edge": doubled_edge_audit(),
        "component_count": component_count_audit(),
        "connected_regular_root": connected_regular_root_audit(),
        "connected_semiregular_root": connected_semiregular_root_audit(),
        "two_components": two_component_audit(),
        "order_table": order_table(),
        "external_input": (
            "connected regular least-eigenvalue-at-least-minus-two classification"
        ),
    }
    print("three-to-one integral excess audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
