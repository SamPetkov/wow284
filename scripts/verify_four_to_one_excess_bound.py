#!/usr/bin/env python3
"""Exact audit of the four-to-one integral excess theorem.

The Cameron--Goethals--Seidel--Shult least-eigenvalue classification is treated
as an external theorem.  All polynomial, divisibility, finite line-root and
Gram-minor calculations after that input are checked here exactly.
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
    d = 2 * h + 3
    return h, c, d


def excess_parameter(k: int, n: int) -> int:
    _, c, d = constants(k)
    return 2 * c - d * n


def irreducible_mod(poly: sp.Expr, prime: int) -> bool:
    factors = sp.Poly(poly, X, modulus=prime).factor_list()[1]
    return (
        len(factors) == 1
        and factors[0][0].degree() == 4
        and factors[0][1] == 1
    )


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


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

    cocktail_identity = sp.expand(
        1296 * c
        - (6 * K + 13) * (216 * K**3 + 396 * K**2 + 654 * K + 1175)
    )
    if cocktail_identity != 277:
        raise AssertionError("wrong cocktail divisibility remainder")

    four_bound = sp.factor(8 * c / (4 * d + 1))
    expected_bound = sp.factor(8 * c / (48 * K + 109))
    if sp.simplify(four_bound - expected_bound) != 0:
        raise AssertionError("wrong four-to-one order bound")

    lp = sp.factor(c / h)
    improvement = sp.factor(lp - four_bound)
    expected_improvement = sp.factor(
        13 * (K + 2) * (K**2 + 3) / (6 * (48 * K + 109))
    )
    if sp.simplify(improvement - expected_improvement) != 0:
        raise AssertionError("wrong improvement identity")

    return {
        "r": str(r),
        "divisibility_remainder": str(division_identity),
        "cocktail_remainder": str(cocktail_identity),
        "order_bound": str(four_bound),
        "improvement": str(improvement),
    }


def nonpositive_r_audit() -> dict[str, object]:
    # r=0 doubled-edge kernel coordinate.
    for k in range(6, 100):
        n = k * k + 2
        value = Fraction(2 * k + 4, n) - 2
        if value in {0, 1}:
            raise AssertionError("r=0 kernel coordinate was not contradictory")

    # Connected cocktail case: 6k+13 divides the prime 277.
    if not sp.isprime(277):
        raise AssertionError("277 is not prime")
    k44 = (277 - 13) // 6
    if k44 != 44:
        raise AssertionError("wrong cocktail degree")
    h44, c44, _ = constants(k44)
    if c44 % (h44 + 1):
        raise AssertionError("k=44 cocktail order is not integral")
    n44 = c44 // (h44 + 1)
    if n44 != 14812:
        raise AssertionError("wrong k=44 cocktail order")
    g44 = (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k44 - 2))
    if not irreducible_mod(g44 + 2, 11):
        raise AssertionError("g_44+2 lacks the mod-11 irreducibility certificate")
    if (n44 // 2) % 4 == 0:
        raise AssertionError("k=44 matching multiplicity is unexpectedly divisible by four")

    # Connected semiregular b=2 case: r=-4 gives 4k+9 | 641.
    if not sp.isprime(641):
        raise AssertionError("641 is not prime")
    k158 = (641 - 9) // 4
    if k158 != 158:
        raise AssertionError("wrong semiregular exceptional degree")
    _, c158, d158 = constants(k158)
    if (2 * c158 + 4) % d158:
        raise AssertionError("k=158 exceptional order is not integral")
    n158 = (2 * c158 + 4) // d158
    if n158 != 664748:
        raise AssertionError("wrong k=158 exceptional order")
    a158 = n158 // 2
    g158 = (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k158 - 2))
    if not irreducible_mod(g158 + 2, 23):
        raise AssertionError("g_158+2 lacks the mod-23 irreducibility certificate")
    if (a158 - 1) % 4 == 0:
        raise AssertionError("k=158 multiplicity is unexpectedly divisible by four")

    # Two-component possibilities r=-2,-1,0 from the exact divisibility filter.
    cases: dict[int, list[tuple[int, int]]] = {}
    for r in (-2, -1, 0):
        candidates: list[tuple[int, int]] = []
        remainder = abs(129 - 128 * r)
        for divisor in divisors(remainder):
            if divisor < 4 * 6 + 9 or (divisor - 9) % 4:
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
    b62 = 20438
    if n62 != 20437 + b62:
        raise AssertionError("wrong k=62 component orders")
    g62 = (X + 2) ** 2 * ((X + 1) ** 2 - (2 * k62 - 2))
    if not irreducible_mod(g62 + 2, 23):
        raise AssertionError("g_62+2 lacks the mod-23 irreducibility certificate")
    if (b62 // 2) % 4 == 0:
        raise AssertionError("k=62 multiplicity is unexpectedly divisible by four")

    return {
        "cocktail": {"k": k44, "n": n44, "minus_one_multiplicity": n44 // 2},
        "semiregular": {"k": k158, "n": n158, "minus_one_multiplicity": a158 - 1},
        "two_component": {"k": k62, "n": n62, "minus_one_multiplicity": b62 // 2},
    }


def doubled_edge_gram_audit() -> dict[str, str]:
    x = sp.symbols("x", positive=True)
    rho = (1 + x) / 2
    diagonal = 1 + rho

    # Pair-vector Cauchy data.
    pair_norm = sp.expand(2 * x)
    third_norm = diagonal
    cauchy_rhs = sp.expand(pair_norm * third_norm)
    if cauchy_rhs != x * (3 + x):
        raise AssertionError("wrong pair-vector Cauchy right-hand side")

    def entry(weight: int) -> sp.Expr:
        return rho - weight

    def det3(a: int, b: int) -> sp.Expr:
        matrix = sp.Matrix(
            [
                [diagonal, entry(2), entry(a)],
                [entry(2), diagonal, entry(b)],
                [entry(a), entry(b), diagonal],
            ]
        )
        return sp.factor(matrix.det())

    if det3(2, 0) != (11 * x - 3) / 2:
        raise AssertionError("wrong asymmetric three-vertex determinant")
    if det3(1, 1) != 3 * (5 * x - 1) / 2:
        raise AssertionError("wrong common-neighbour determinant")

    def det4(weight: int) -> sp.Expr:
        matrix = sp.Matrix(
            [
                [diagonal, entry(2), entry(1), entry(1)],
                [entry(2), diagonal, entry(1), entry(1)],
                [entry(1), entry(1), diagonal, entry(weight)],
                [entry(1), entry(1), entry(weight), diagonal],
            ]
        )
        return sp.factor(matrix.det())

    expected = {0: 3 * (4 * x - 1), 1: 6 * (3 * x - 1), 2: 9 * (2 * x - 1)}
    actual = {weight: det4(weight) for weight in expected}
    if actual != expected:
        raise AssertionError(f"wrong four-vertex determinants: {actual}")

    # r=1 is impossible because 4k+9 must divide 1.
    if abs(129 - 128) != 1:
        raise AssertionError("wrong r=1 remainder")

    return {
        "cauchy_rhs": str(cauchy_rhs),
        "asymmetric_det": str(det3(2, 0)),
        "common_det": str(det3(1, 1)),
        "four_vertex_determinants": str(actual),
    }


def connected_line_root_audit() -> dict[str, object]:
    # Regular roots allowed by n>4r, n>=38, q<=v-1 and v<32/3.
    regular_cases: list[tuple[int, int, int, int]] = []
    for q in range(1, 20):
        for v in range(q + 1, 11):
            if (q * v) % 2:
                continue
            n = q * v // 2
            r = n - 4 * q
            if n >= 38 and r > 0 and n > 4 * r:
                regular_cases.append((q, v, n, r))
    if regular_cases != [(8, 10, 40, 8), (9, 10, 45, 9)]:
        raise AssertionError(f"wrong regular-root cases: {regular_cases}")
    for _, _, n, r in regular_cases:
        if excess_parameter(6, n) == r:
            raise AssertionError("regular-root exceptional case survived at k=6")

    # Semiregular roots.  Part sizes a>=b>=2 and simplicity give n<=ab.
    semiregular: list[tuple[int, int, int, int]] = []
    for b in range(2, 100):
        for a in range(b, 100):
            reciprocal = Fraction(1, a) + Fraction(1, b)
            if not (Fraction(3, 8) < reciprocal < Fraction(1, 2)):
                continue
            multiple = math.lcm(a, b)
            for n in range(multiple, a * b + 1, multiple):
                if n < 38:
                    continue
                r_value = n * (1 - 2 * reciprocal)
                if r_value.denominator != 1:
                    continue
                semiregular.append((a, b, n, r_value.numerator))
    expected = [
        (13, 3, 39, 7),
        (14, 3, 42, 8),
        (15, 3, 45, 9),
        (16, 3, 48, 10),
        (17, 3, 51, 11),
        (18, 3, 54, 12),
        (19, 3, 57, 13),
        (20, 3, 60, 14),
        (21, 3, 42, 10),
        (21, 3, 63, 15),
        (22, 3, 66, 16),
        (23, 3, 69, 17),
    ]
    if semiregular != expected:
        raise AssertionError(f"wrong semiregular finite list: {semiregular}")
    survivors: list[tuple[int, int, int]] = []
    for _, _, n, r in semiregular:
        for k in range(6, math.isqrt(n - 2) + 1):
            if (k * n) % 2 == 0 and excess_parameter(k, n) == r:
                survivors.append((k, n, r))
    if survivors:
        raise AssertionError(f"semiregular connected cases survived: {survivors}")

    return {"regular_cases": regular_cases, "semiregular_cases": semiregular}


def two_component_audit() -> dict[str, object]:
    # Low degrees are vacuous under r>0 and n>4r.
    low: dict[int, list[tuple[int, int]]] = {}
    for k in (6, 7, 8):
        h, c, _ = constants(k)
        upper = c // (h + 1)
        values: list[tuple[int, int]] = []
        for n in range(k * k + 2, upper + 1):
            if (k * n) % 2:
                continue
            r = excess_parameter(k, n)
            if r > 0 and n > 4 * r:
                values.append((n, r))
        if values:
            raise AssertionError(f"unexpected low-degree two-component case: {k}, {values}")
        low[k] = values

    # For k>=9, component orders exceed 28 and the semiregular reciprocal
    # condition >7/12 has only products at most 22.
    reciprocal_pairs: list[tuple[int, int]] = []
    for b in range(2, 100):
        for a in range(b, 100):
            if Fraction(1, a) + Fraction(1, b) > Fraction(7, 12):
                reciprocal_pairs.append((a, b))
    expected_pairs = [(a, 2) for a in range(2, 12)] + [(3, 3)]
    if reciprocal_pairs != expected_pairs:
        raise AssertionError(f"wrong two-component reciprocal list: {reciprocal_pairs}")
    if max(a * b for a, b in reciprocal_pairs) != 22:
        raise AssertionError("wrong two-component product maximum")

    # Exact inequalities used to obtain the 7/12 threshold and root-order <7.
    n, r = sp.symbols("n r", integer=True, positive=True)
    reciprocal_margin = sp.expand(12 * (n - r) - 7 * (n + r + 2))
    if reciprocal_margin != 5 * n - 19 * r - 14:
        raise AssertionError("wrong reciprocal margin")
    root_order_margin = sp.expand(7 * (n - r) - 4 * (n + r + 2))
    if root_order_margin != 3 * n - 11 * r - 8:
        raise AssertionError("wrong root-order margin")

    return {
        "low_degree_vacuity": low,
        "reciprocal_pairs": reciprocal_pairs,
        "max_part_product": 22,
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
    }
    actual: dict[int, int] = {}
    for k in expected:
        _, c, d = constants(k)
        actual[k] = (8 * c) // (4 * d + 1)
    if actual != expected:
        raise AssertionError(f"wrong four-to-one order table: {actual}")
    return actual


def main() -> None:
    report = {
        "symbolic": symbolic_audit(),
        "nonpositive_r": nonpositive_r_audit(),
        "doubled_edge_gram": doubled_edge_gram_audit(),
        "connected_line_roots": connected_line_root_audit(),
        "two_components": two_component_audit(),
        "order_table": order_table(),
        "external_input": (
            "connected regular least-eigenvalue-at-least-minus-two classification"
        ),
    }
    print("four-to-one integral excess audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
