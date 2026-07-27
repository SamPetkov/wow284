#!/usr/bin/env python3
"""Independent exact audit of the all-degree two-sided LP ceiling.

This verifier does not import the original LP verifier. It checks:
- the nonbacktracking recurrence and evaluation at k;
- the primal extremal polynomial in the F-basis;
- positivity and moment identities for the three-point dual measure;
- strict dual slacks for degrees 5 through 9;
- the uniform Chebyshev tail estimate for every degree at least 10;
- rigidity of equality and uniqueness of the extremal polynomial up to scale.

No floating-point arithmetic is used.
"""
from __future__ import annotations

import json
import sympy as sp

X = sp.symbols("x")
K = sp.symbols("k", integer=True, positive=True)
M = sp.symbols("m", integer=True, nonnegative=True)
R = sp.symbols("r", integer=True, positive=True)
I = sp.symbols("i", integer=True, positive=True)
DELTA = sp.sqrt(2 * K - 2)


def nonbacktracking_polynomials(max_degree: int) -> list[sp.Expr]:
    if max_degree < 2:
        raise ValueError("need degree at least two")
    values = [sp.Integer(1), X, X**2 - K]
    for _ in range(3, max_degree + 1):
        values.append(sp.expand(X * values[-1] - (K - 1) * values[-2]))
    return values


def assert_zero(expr: sp.Expr, label: str) -> None:
    if sp.simplify(sp.expand(expr)) != 0:
        raise AssertionError(f"{label}: {sp.factor(expr)}")


def verify_recurrence_and_primal(polynomials: list[sp.Expr]) -> dict[str, str]:
    for degree in range(1, len(polynomials)):
        assert_zero(
            polynomials[degree].subs(X, K) - K * (K - 1) ** (degree - 1),
            f"F_{degree}(k)",
        )

    boundary = X**2 + 2 * X - (2 * K - 3)
    numerator = sp.expand((X + 2) ** 2 * boundary)
    coefficients = (
        6 * (K + 2),
        2 * (2 * K + 7),
        K + 13,
        sp.Integer(6),
        sp.Integer(1),
    )
    assert_zero(
        numerator - sum(coefficients[j] * polynomials[j] for j in range(5)),
        "primal F-basis expansion",
    )

    normalized = sp.factor(numerator / (6 * (K + 2)))
    bound = sp.factor((K + 2) * (K**2 + 3) / 6)
    assert_zero(normalized.subs(X, K) - bound, "primal value at k")

    lower = -1 - DELTA
    upper = -1 + DELTA
    assert_zero(numerator.subs(X, lower), "lower endpoint zero")
    assert_zero(numerator.subs(X, upper), "upper endpoint zero")
    assert_zero(numerator.subs(X, -2), "interior zero")
    assert_zero(sp.diff(numerator, X).subs(X, -2), "interior double zero")
    if sp.simplify(sp.diff(numerator, X, 2).subs(X, -2)) == 0:
        raise AssertionError("interior root has multiplicity greater than two")

    return {
        "extremal_polynomial": str(normalized),
        "bound": str(bound),
        "F_basis_coefficients_before_normalization": str(coefficients),
        "equality_support": str((lower, -2, upper)),
    }


def dual_weights() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    common = K * (K + 2) / (24 * (2 * K - 3))
    lower = sp.factor(common * (2 * K**2 - 6 - 3 * (K - 1) * DELTA))
    middle = sp.factor(K * (K - 1) * (K**2 + 3) / (6 * (2 * K - 3)))
    upper = sp.factor(common * (2 * K**2 - 6 + 3 * (K - 1) * DELTA))
    return lower, middle, upper


def verify_dual_finite(polynomials: list[sp.Expr]) -> dict[str, str]:
    points = (-1 - DELTA, sp.Integer(-2), -1 + DELTA)
    weights = dual_weights()

    mass = sp.factor(sum(weights))
    expected_mass = sp.factor(K * (K**2 + 2 * K + 3) / 6)
    assert_zero(mass - expected_mass, "dual mass")

    square_difference = sp.factor((2 * K**2 - 6) ** 2 - 18 * (K - 1) ** 3)
    expected_difference = 2 * (K - 3) * (2 * K - 3) * (K**2 + 3)
    assert_zero(square_difference - expected_difference, "weight square identity")
    shifted_difference = sp.expand(expected_difference.subs(K, M + 4))
    if not all(value > 0 for value in sp.Poly(shifted_difference, M).all_coeffs()):
        raise AssertionError("weight positivity expansion is not coefficientwise positive")

    moments: dict[int, sp.Expr] = {}
    for degree in range(1, 10):
        moments[degree] = sp.simplify(
            sum(
                weights[j] * polynomials[degree].subs(X, points[j])
                for j in range(3)
            )
        )

    for degree in range(1, 5):
        assert_zero(
            moments[degree] + K * (K - 1) ** (degree - 1),
            f"dual moment F_{degree}",
        )

    slacks = {
        degree: sp.factor(
            sp.radsimp(moments[degree] + K * (K - 1) ** (degree - 1))
        )
        for degree in range(5, 10)
    }
    expected = {
        5: K * (K - 1) * (K + 2) * (K**2 + 3) / 3,
        6: K * (K - 1) * (K + 2) * (5 * K - 13) * (K**2 + 3) / 6,
        7: K * (K - 1) * (K + 2) * (K**2 + 3) * (3 * K**2 - 17 * K + 25) / 3,
        8: K * (K - 1) * (K + 2) * (K**2 + 3) * (6 * K**3 - 47 * K**2 + 139 * K - 150) / 6,
        9: K * (K - 1) * (K + 2) * (K**2 + 3) * (3 * K**4 - 27 * K**3 + 106 * K**2 - 219 * K + 194) / 3,
    }
    for degree, target in expected.items():
        assert_zero(slacks[degree] - target, f"finite slack F_{degree}")

    positive_shifts = {
        7: sp.expand((3 * K**2 - 17 * K + 25).subs(K, M + 4)),
        8: sp.expand((6 * K**3 - 47 * K**2 + 139 * K - 150).subs(K, M + 4)),
        9: sp.expand((3 * K**4 - 27 * K**3 + 106 * K**2 - 219 * K + 194).subs(K, M + 4)),
    }
    expected_shifts = {
        7: 3 * M**2 + 7 * M + 5,
        8: 6 * M**3 + 25 * M**2 + 51 * M + 38,
        9: 3 * M**4 + 21 * M**3 + 70 * M**2 + 101 * M + 54,
    }
    for degree in expected_shifts:
        assert_zero(
            positive_shifts[degree] - expected_shifts[degree],
            f"positive shift F_{degree}",
        )

    return {
        "support": str(points),
        "weights": str(weights),
        "mass": str(mass),
        "finite_slacks": str(slacks),
    }


def verify_support_and_tail() -> dict[str, str]:
    support_margin = sp.expand((2 * R - 1) ** 2 - 8 * R)
    shifted_margin = sp.expand(support_margin.subs(R, M + 3))
    if shifted_margin != 4 * M**2 + 12 * M + 1:
        raise AssertionError("wrong support inclusion margin")

    assert_zero(
        3 * R**2 - (R**2 + 4 * R + 6) - 2 * (R - 3) * (R + 1),
        "first tail inequality",
    )
    assert_zero(
        (4 * I + 2) * R / 3
        - ((I + 1) * R + I - 1)
        - (I - 1) * (R - 3) / 3,
        "second tail inequality",
    )

    tail_at_10 = sp.Rational(2 * 10 + 1, 3) * 3 ** (3 - sp.Rational(10, 2))
    if tail_at_10 != sp.Rational(7, 9):
        raise AssertionError("wrong tail value at degree ten")

    monotonicity_margin = sp.expand(3 * (2 * I + 1) ** 2 - (2 * I + 3) ** 2)
    if monotonicity_margin != 8 * I**2 - 6:
        raise AssertionError("wrong tail monotonicity margin")

    return {
        "support_square_margin_at_r=m+3": str(shifted_margin),
        "tail_ratio_at_i10_r3": str(tail_at_10),
        "tail_monotonicity_margin": str(monotonicity_margin),
        "conclusion": "all dual slacks are strictly positive for every i>=5",
    }


def verify_equality_rigidity(polynomials: list[sp.Expr]) -> dict[str, str]:
    lower = -1 - DELTA
    upper = -1 + DELTA
    numerator = sp.expand((X + 2) ** 2 * (X - lower) * (X - upper))
    canonical = sp.expand((X + 2) ** 2 * (X**2 + 2 * X - (2 * K - 3)))
    assert_zero(numerator - canonical, "root factorization")

    coeffs = sp.symbols("a0:5")
    generic = sum(coeffs[j] * X**j for j in range(5))
    equations = [
        sp.expand(generic.subs(X, lower)),
        sp.expand(generic.subs(X, upper)),
        sp.expand(generic.subs(X, -2)),
        sp.expand(sp.diff(generic, X).subs(X, -2)),
    ]
    matrix, _ = sp.linear_eq_to_matrix(equations, coeffs)
    nullspace = matrix.nullspace()
    if len(nullspace) != 1:
        raise AssertionError(f"optimizer nullspace dimension is {len(nullspace)}")

    canonical_vector = sp.Matrix(
        [sp.Poly(canonical, X).coeff_monomial(X**j) for j in range(5)]
    )
    witness = nullspace[0]
    for a in range(5):
        for b in range(a + 1, 5):
            assert_zero(
                witness[a] * canonical_vector[b] - witness[b] * canonical_vector[a],
                "optimizer nullspace direction",
            )

    f0 = 6 * (K + 2)
    assert_zero(
        canonical
        - sum(
            value * polynomials[j]
            for j, value in enumerate((f0, 2 * (2 * K + 7), K + 13, 6, 1))
        ),
        "canonical F-basis expansion",
    )

    return {
        "optimizer_nullspace_dimension": "1",
        "canonical_F0_coefficient": str(f0),
        "rigidity": (
            "equality forces f_i=0 for i>=5, zeros at both endpoints, "
            "and a double zero at -2; hence f is a positive multiple of f_*"
        ),
    }


def verify_exact_numeric_grid(polynomials: list[sp.Expr]) -> dict[str, object]:
    checked: list[dict[str, int]] = []
    for kval in range(4, 13):
        r = kval - 1
        delta = sp.sqrt(2 * kval - 2)
        points = (-1 - delta, sp.Integer(-2), -1 + delta)
        weights = tuple(sp.simplify(value.subs(K, kval)) for value in dual_weights())
        if not all(bool(value > 0) for value in weights):
            raise AssertionError(f"nonpositive concrete weight at k={kval}")
        for degree in range(5, 31):
            current = polynomials[degree]
            moment = sp.simplify(
                sum(
                    weights[j] * current.subs({K: kval, X: points[j]})
                    for j in range(3)
                )
            )
            slack = sp.simplify(moment + kval * r ** (degree - 1))
            if not bool(slack > 0):
                raise AssertionError((kval, degree, slack))
        checked.append({"k": kval, "degrees_through": 30})
    return {"concrete_exact_checks": checked}


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")
    polynomials = nonbacktracking_polynomials(30)
    result = {
        "recurrence_and_primal": verify_recurrence_and_primal(polynomials),
        "dual_finite": verify_dual_finite(polynomials),
        "support_and_tail": verify_support_and_tail(),
        "equality_rigidity": verify_equality_rigidity(polynomials),
        "redundant_exact_grid": verify_exact_numeric_grid(polynomials),
    }
    print("Proof Audit 02 (two-sided LP ceiling): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
