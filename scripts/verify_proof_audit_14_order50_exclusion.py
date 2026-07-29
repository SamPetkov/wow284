#!/usr/bin/env python3
"""Independent replay of Proof Audit 14B: exclusion of degree-six order 50.

This script does not import the primary order-50 verifier.  The signed-root
classification is an external theorem; all project-derived algebra and finite
arithmetic are recomputed here.
"""
from __future__ import annotations

import itertools

import sympy as sp

x = sp.symbols("x")


def recurrence_basis() -> list[sp.Expr]:
    values = [sp.Integer(1), x, x**2 - 6]
    while len(values) <= 8:
        values.append(sp.expand(x * values[-1] - 5 * values[-2]))
    return values


def parity_replay() -> None:
    g = (x + 2) ** 2 * ((x + 1) ** 2 - 10)
    basis = recurrence_basis()
    target = sp.Poly(sp.expand((g + 2) ** 2), x)
    matrix = sp.zeros(9)
    rhs = sp.Matrix(target.all_coeffs())

    # Solve in the power basis independently from the hard-coded expansion.
    for column, polynomial in enumerate(basis):
        coefficients = sp.Poly(polynomial, x).all_coeffs()
        padded = [0] * (9 - len(coefficients)) + coefficients
        matrix[:, column] = sp.Matrix(padded)
    solution = list(matrix.LUsolve(rhs))
    if solution != [28144, 18220, 8838, 3576, 1233, 352, 78, 12, 1]:
        raise AssertionError(f"independent recurrence solution changed: {solution}")

    n5, n6, n7, n8 = sp.symbols("n5 n6 n7 n8", integer=True)
    trace = (
        4
        + 50 * solution[0]
        + 10 * solution[5] * n5
        + 12 * solution[6] * n6
        + 14 * solution[7] * n7
        + 16 * solution[8] * n8
        - (sp.expand(g).subs(x, 6) + 2) ** 2
    )
    coefficients = sp.Poly(trace, n5, n6, n7, n8).coeffs()
    if any(int(value) % 8 for value in coefficients):
        raise AssertionError("trace square is not coefficientwise divisible by eight")


def root_level_replay() -> None:
    # Family B: levels 2 and 6 only.
    possibilities = []
    for n2 in range(51):
        for n6 in range(51 - n2):
            vertex_count = n2 + n6
            if 4 * n2 + 36 * n6 == 200 and 30 <= vertex_count <= 51:
                possibilities.append((n2, n6, vertex_count))
    if possibilities != [(32, 2, 34), (41, 1, 42), (50, 0, 50)]:
        raise AssertionError(f"independent family-B enumeration changed: {possibilities}")

    t = sp.symbols("t", integer=True, nonnegative=True)
    weight = 16 * t * (t + 1)
    if sp.expand((4 * t + 1) ** 2 - 3 - weight + 2 * (4 * t + 1)) != 0:
        raise AssertionError("wrong odd-chain identity for levels 1 mod 4")
    if sp.expand((4 * t + 3) ** 2 - 3 - weight - 2 * (4 * t + 3)) != 0:
        raise AssertionError("wrong odd-chain identity for levels 3 mod 4")
    if any((200 - 3 * v) >= 0 and (200 - 3 * v) % 32 == 0 for v in range(30, 52)):
        raise AssertionError("an odd-level support size survived")


def quotient_replay() -> None:
    # q_ij=n_j/5 off the diagonal and q_ii=n_i/5-4.
    partitions = []
    for count in range(2, 4):
        for parts in itertools.product(range(20, 51, 5), repeat=count):
            if tuple(sorted(parts)) != parts:
                continue
            if sum(parts) == 50:
                partitions.append(parts)
    if partitions != [(20, 30), (25, 25)]:
        raise AssertionError(f"wrong equitable component sizes: {partitions}")
    internal_degrees = {
        parts: tuple(part // 5 - 4 for part in parts) for parts in partitions
    }
    if internal_degrees[(20, 30)] != (0, 2):
        raise AssertionError("wrong 20+30 quotient")
    if internal_degrees[(25, 25)] != (1, 1):
        raise AssertionError("wrong 25+25 quotient")
    if 25 * 1 % 2 == 0:
        raise AssertionError("odd 1-regular part was not excluded")


def incidence_replay() -> None:
    p = sp.zeros(20)
    for index in range(10):
        left = 2 * index
        right = left + 1
        p[left, right] = p[right, left] = 1
    gram = 5 * sp.eye(20) + sp.ones(20) - p

    # Verify the three invariant spaces directly.
    one = sp.ones(20, 1)
    if gram * one != 24 * one:
        raise AssertionError("wrong constant incidence eigenvalue")
    for index in range(10):
        vector = sp.zeros(20, 1)
        vector[2 * index] = 1
        vector[2 * index + 1] = -1
        if gram * vector != 6 * vector:
            raise AssertionError("wrong matching-antisymmetric incidence eigenvalue")
    for index in range(1, 10):
        vector = sp.zeros(20, 1)
        vector[0] = vector[1] = -1
        vector[2 * index] = vector[2 * index + 1] = 1
        if gram * vector != 4 * vector:
            raise AssertionError("wrong matching-symmetric incidence eigenvalue")

    if sp.trace(gram) != 120 or sp.trace(gram**2) != 1080:
        raise AssertionError("incidence traces changed")


def block_replay() -> None:
    # Use symbolic entries rather than the numerical test in the first verifier.
    c00, c01, c02, c10, c11, c12 = sp.symbols("c00 c01 c02 c10 c11 c12")
    r01, r02, r12 = sp.symbols("r01 r02 r12")
    c = sp.Matrix([[c00, c01, c02], [c10, c11, c12]])
    r = sp.Matrix([[0, r01, r02], [r01, 0, r12], [r02, r12, 0]])
    adjacency = sp.BlockMatrix([[sp.zeros(2), c], [c.T, r]]).as_explicit()
    polynomial = adjacency**4 + 6 * adjacency**3 + 3 * adjacency**2 - 28 * adjacency
    b = c.T * c
    proposed = c * (b * r + r * b + r**3 + 6 * b + 6 * r**2 + 3 * r - 28 * sp.eye(3))
    difference = polynomial[:2, 2:] - proposed
    if any(sp.expand(entry) != 0 for entry in difference):
        raise AssertionError("symbolic off-block identity failed")

    # The trace equation is 2(960-2T)+U=1440 with 0<=T<=120 and U>=0.
    feasible = []
    for total in range(121):
        residual = 1440 - 2 * (960 - 2 * total)
        if residual >= 0:
            feasible.append((total, residual))
    if feasible != [(120, 0)]:
        raise AssertionError(f"independent trace squeeze changed: {feasible}")


def main() -> None:
    parity_replay()
    root_level_replay()
    quotient_replay()
    incidence_replay()
    block_replay()
    print("independent Proof Audit 14B order-50 exclusion: PASS")


if __name__ == "__main__":
    main()
