#!/usr/bin/env python3
"""Exact symbolic audit of the signed-primary transfer theorem."""
from __future__ import annotations

import sympy as sp

X, Y = sp.symbols("x y")
K = sp.symbols("k", integer=True, positive=True)


def generic_coefficient_audit() -> dict[str, str]:
    d = sp.symbols("d", integer=True, positive=True)

    # The degree and x^(4d-1) coefficient follow from the top two terms of the
    # monic quartic g_k=x^4+6x^3+....  Check the binomial expansion symbolically.
    leading_model = (X**4 + 6 * X**3) ** d
    coefficient = sp.expand(leading_model).coeff(X, 4 * d - 1)
    if sp.simplify(coefficient - 6 * d) != 0:
        raise AssertionError("wrong generic composed cubic coefficient")

    e = sp.symbols("e", integer=True, positive=True)
    trace = sp.simplify((-6 * d) * (e / 4))
    if trace != -sp.Rational(3, 2) * d * e:
        raise AssertionError("wrong primary trace formula")

    return {
        "monic_x_4d_minus_1_coefficient": str(coefficient),
        "root_sum_per_block": str(-6 * d),
        "total_trace": str(trace),
    }


def concrete_factor_audit() -> dict[str, object]:
    g = (X + 2) ** 2 * ((X + 1) ** 2 - (2 * K - 2))
    examples: dict[str, object] = {}

    for expression in (
        Y,
        Y - 1,
        Y + 1,
        Y**2 + Y - 1,
        Y**2 - 2,
    ):
        q = sp.Poly(expression, Y, domain=sp.QQ).monic()
        d = q.degree()
        composed = sp.Poly(
            sp.expand((-1) ** d * q.as_expr().subs(Y, -2 - g)),
            X,
            domain=sp.QQ.frac_field(K),
        ).monic()
        if composed.degree() != 4 * d:
            raise AssertionError("wrong composed degree")
        root_sum = -composed.all_coeffs()[1]
        if sp.simplify(root_sum + 6 * d) != 0:
            raise AssertionError(
                f"wrong composed root sum for {q.as_expr()}: {root_sum}"
            )
        examples[str(q.as_expr())] = {
            "degree": d,
            "composed_degree": composed.degree(),
            "root_sum": str(root_sum),
        }

    return examples


def order50_integer_eigenvalue_audit() -> dict[int, object]:
    k = 6
    g = sp.expand((X + 2) ** 2 * ((X + 1) ** 2 - 10))
    report: dict[int, object] = {}

    for eigenvalue in (-1, 0, 1, 2, 3):
        polynomial = sp.Poly(g + eigenvalue + 2, X, domain=sp.QQ)
        factors = sp.factor_list(polynomial.as_expr())[1]
        report[eigenvalue] = {
            "factorization": str(sp.factor(polynomial.as_expr())),
            "factor_degrees": [sp.Poly(factor, X).degree() for factor, _ in factors],
            "exponents": [exponent for _, exponent in factors],
        }

    # The generic quartic transfer applies directly at -1,0,1.
    for eigenvalue in (-1, 0, 1):
        degrees = report[eigenvalue]["factor_degrees"]
        if degrees != [4]:
            raise AssertionError(
                f"expected irreducible quartic at signed eigenvalue {eigenvalue}"
            )

    # The special signed eigenvalue 2 has the correct linear-cubic split.
    if sp.factor(g + 4) != (X + 4) * (X**3 + 2 * X**2 - 8 * X - 4):
        raise AssertionError("wrong order-50 special factorization")

    return report


def main() -> None:
    report = {
        "generic": generic_coefficient_audit(),
        "concrete_factors": concrete_factor_audit(),
        "order50_integer_eigenvalues": order50_integer_eigenvalue_audit(),
    }
    print("signed-primary transfer audit: PASS")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
