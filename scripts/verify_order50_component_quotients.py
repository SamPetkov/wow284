#!/usr/bin/env python3
"""Exact canonical audit of the corrected order-50 component quotient problem.

The script enumerates the two-, four-, and five-cell cases in pure Python and
runs two independent C++ backends for the seven- and ten-cell cases.  It uses
only integer arithmetic for the quotient constraints.  The final six-vertex
signed-component uniqueness check uses exact principal minors.
"""
from __future__ import annotations

from itertools import permutations
from math import gcd
from pathlib import Path
import subprocess
import tempfile

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def partitions(total: int, count: int, minimum: int = 1) -> list[tuple[int, ...]]:
    output: list[tuple[int, ...]] = []

    def recurse(remainder: int, parts: int, lower: int, current: list[int]) -> None:
        if parts == 0:
            if remainder == 0:
                output.append(tuple(current))
            return
        for value in range(lower, remainder // parts + 1):
            current.append(value)
            recurse(remainder - value, parts - 1, value, current)
            current.pop()

    recurse(total, count, minimum, [])
    return output


def diagonal_tuples(
    count: int,
    total: int,
    sizes: tuple[int, ...],
) -> list[tuple[int, ...]]:
    output: list[tuple[int, ...]] = []

    def recurse(index: int, remainder: int, current: list[int]) -> None:
        if index == count:
            if remainder == 0:
                output.append(tuple(current))
            return
        maximum = min(6, sizes[index] - 1, remainder)
        for value in range(maximum + 1):
            # Every internal cell is itself triangle- and four-cycle-free.
            if value == 1 and sizes[index] % 2:
                continue
            if value >= 2 and sizes[index] < value * value + 1:
                continue
            current.append(value)
            recurse(index + 1, remainder - value, current)
            current.pop()

    recurse(0, total, [])
    return output


def pair_options(
    left_size: int,
    right_size: int,
    left_remainder: int,
    right_remainder: int,
) -> list[tuple[int, int]]:
    common = gcd(left_size, right_size)
    left_unit = right_size // common
    right_unit = left_size // common
    maximum = min(
        6 // left_unit,
        6 // right_unit,
        left_remainder // left_unit,
        right_remainder // right_unit,
        right_size // left_unit,
        left_size // right_unit,
    )
    output = [(0, 0)]
    for multiplier in range(1, maximum + 1):
        left = left_unit * multiplier
        right = right_unit * multiplier
        # In a four-cycle-free biregular block, a pair of vertices on either
        # side has at most one common neighbour.
        if (
            left_size * left * (left - 1) <= right_size * (right_size - 1)
            and right_size * right * (right - 1)
            <= left_size * (left_size - 1)
        ):
            output.append((left, right))
    return output


def multiply(
    left: list[list[int]],
    right: list[list[int]],
) -> list[list[int]]:
    rows = len(left)
    columns = len(right[0])
    middle = len(right)
    return [
        [
            sum(left[row][index] * right[index][column] for index in range(middle))
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def connected(quotient: list[list[int]]) -> bool:
    count = len(quotient)
    seen = {0}
    pending = [0]
    while pending:
        left = pending.pop()
        for right in range(count):
            if left != right and quotient[left][right] > 0 and right not in seen:
                seen.add(right)
                pending.append(right)
    return len(seen) == count


def radius_two_feasible(
    quotient: list[list[int]],
    sizes: tuple[int, ...],
) -> bool:
    square = multiply(quotient, quotient)
    count = len(quotient)
    for row in range(count):
        for column in range(count):
            left = square[row][column] - (6 if row == column else 0)
            right = (
                sizes[column]
                - (1 if row == column else 0)
                - quotient[row][column]
            )
            if left > right:
                return False
    return True


def polynomial_identity(
    quotient: list[list[int]],
    sizes: tuple[int, ...],
    linear_multiplicity: int,
) -> bool:
    count = len(quotient)
    identity = [[int(row == column) for column in range(count)] for row in range(count)]
    square = multiply(quotient, quotient)
    cube = multiply(square, quotient)

    if linear_multiplicity == 0:
        # q(x)=x^3+2x^2-5x-8 and q(6)=250.
        for row in range(count):
            for column in range(count):
                value = (
                    cube[row][column]
                    + 2 * square[row][column]
                    - 5 * quotient[row][column]
                    - 8 * identity[row][column]
                )
                if value != 5 * sizes[column]:
                    return False
        return True

    fourth = multiply(cube, quotient)
    # g_6(x)+4=x^4+6x^3+3x^2-28x-32 and p(6)=2500.
    for row in range(count):
        for column in range(count):
            value = (
                fourth[row][column]
                + 6 * cube[row][column]
                + 3 * square[row][column]
                - 28 * quotient[row][column]
                - 32 * identity[row][column]
            )
            if value != 50 * sizes[column]:
                return False
    return True


def canonical_key(
    sizes: tuple[int, ...],
    quotient: tuple[tuple[int, ...], ...] | list[list[int]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    count = len(sizes)
    return min(
        (
            tuple(sizes[index] for index in permutation),
            tuple(
                quotient[row][column]
                for row in permutation
                for column in permutation
            ),
        )
        for permutation in permutations(range(count))
    )


def enumerate_small_case(
    count: int,
    linear_multiplicity: int,
    cubic_multiplicity: int,
) -> tuple[
    dict[
        tuple[tuple[int, ...], tuple[int, ...]],
        tuple[tuple[int, ...], tuple[tuple[int, ...], ...]],
    ],
    int,
    int,
]:
    trace = 6 - 4 * linear_multiplicity - 2 * cubic_multiplicity
    trace_square = 36 + 16 * linear_multiplicity + 14 * cubic_multiplicity
    solutions: dict[
        tuple[tuple[int, ...], tuple[int, ...]],
        tuple[tuple[int, ...], tuple[tuple[int, ...], ...]],
    ] = {}
    node_count = 0
    leaf_count = 0

    for sizes in partitions(50, count):
        for diagonal in diagonal_tuples(count, trace, sizes):
            remainder = [6 - value for value in diagonal]
            variables: list[tuple[int, int, list[tuple[int, int]]]] = []
            for left in range(count):
                for right in range(left + 1, count):
                    variables.append(
                        (
                            left,
                            right,
                            pair_options(
                                sizes[left],
                                sizes[right],
                                remainder[left],
                                remainder[right],
                            ),
                        )
                    )
            variables.sort(key=lambda item: (len(item[2]), -(item[0] + item[1])))
            variable_count = len(variables)

            suffix_maximum = [[0] * count for _ in range(variable_count + 1)]
            suffix_trace = [0] * (variable_count + 1)
            for position in range(variable_count - 1, -1, -1):
                suffix_maximum[position] = suffix_maximum[position + 1].copy()
                left, right, options = variables[position]
                suffix_maximum[position][left] += max(value[0] for value in options)
                suffix_maximum[position][right] += max(value[1] for value in options)
                suffix_trace[position] = suffix_trace[position + 1] + max(
                    2 * value[0] * value[1] for value in options
                )

            if any(
                suffix_maximum[0][index] < remainder[index]
                for index in range(count)
            ):
                continue

            quotient = [[0] * count for _ in range(count)]
            for index, value in enumerate(diagonal):
                quotient[index][index] = value
            initial_trace = sum(value * value for value in diagonal)

            def recurse(position: int, current_trace: int) -> None:
                nonlocal node_count, leaf_count
                node_count += 1
                if current_trace > trace_square:
                    return
                if current_trace + suffix_trace[position] < trace_square:
                    return
                if any(
                    remainder[index] < 0
                    or remainder[index] > suffix_maximum[position][index]
                    for index in range(count)
                ):
                    return
                if position == variable_count:
                    if any(remainder) or current_trace != trace_square:
                        return
                    leaf_count += 1
                    if not connected(quotient):
                        return
                    if not radius_two_feasible(quotient, sizes):
                        return
                    if not polynomial_identity(
                        quotient,
                        sizes,
                        linear_multiplicity,
                    ):
                        return
                    frozen = tuple(tuple(row) for row in quotient)
                    solutions[canonical_key(sizes, frozen)] = (sizes, frozen)
                    return

                left, right, options = variables[position]
                for left_value, right_value in options:
                    if left_value > remainder[left] or right_value > remainder[right]:
                        continue
                    quotient[left][right] = left_value
                    quotient[right][left] = right_value
                    remainder[left] -= left_value
                    remainder[right] -= right_value
                    recurse(
                        position + 1,
                        current_trace + 2 * left_value * right_value,
                    )
                    remainder[left] += left_value
                    remainder[right] += right_value
                quotient[left][right] = 0
                quotient[right][left] = 0

            recurse(0, initial_trace)

    return solutions, node_count, leaf_count


def expected_small_quotients() -> dict[int, set[tuple[tuple[int, ...], tuple[int, ...]]]]:
    examples = {
        2: [
            (
                (20, 30),
                ((0, 6), (4, 2)),
            ),
        ],
        4: [
            (
                (2, 12, 12, 24),
                (
                    (0, 6, 0, 0),
                    (1, 1, 2, 2),
                    (0, 2, 0, 4),
                    (0, 1, 2, 3),
                ),
            ),
            (
                (6, 8, 12, 24),
                (
                    (2, 0, 0, 4),
                    (0, 0, 3, 3),
                    (0, 2, 0, 4),
                    (1, 1, 2, 2),
                ),
            ),
            (
                (10, 10, 10, 20),
                (
                    (1, 0, 3, 2),
                    (0, 1, 1, 4),
                    (3, 1, 0, 2),
                    (1, 2, 1, 2),
                ),
            ),
        ],
        5: [],
    }
    return {
        count: {canonical_key(sizes, quotient) for sizes, quotient in values}
        for count, values in examples.items()
    }


def run_cpp_backend(source_name: str, expected_output: str) -> str:
    source = ROOT / "scripts" / source_name
    if not source.is_file():
        raise AssertionError(f"missing C++ backend: {source}")
    with tempfile.TemporaryDirectory(prefix="wow284-quotient-") as directory:
        executable = Path(directory) / "audit"
        subprocess.run(
            [
                "g++",
                "-std=c++17",
                "-O2",
                "-Wall",
                "-Wextra",
                "-pedantic",
                str(source),
                "-o",
                str(executable),
            ],
            check=True,
            cwd=ROOT,
        )
        completed = subprocess.run(
            [str(executable)],
            check=True,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=120,
        )
    output = completed.stdout.strip()
    if output != expected_output:
        raise AssertionError(
            f"unexpected output from {source_name}: {output!r}; "
            f"expected {expected_output!r}"
        )
    return output


def signed_six_uniqueness() -> dict[str, object]:
    order = 6
    pairs = [
        (left, right)
        for left in range(order)
        for right in range(left + 1, order)
    ]
    suffix = [[0] * order for _ in range(len(pairs) + 1)]
    for position in range(len(pairs) - 1, -1, -1):
        suffix[position] = suffix[position + 1].copy()
        left, right = pairs[position]
        suffix[position][left] += 1
        suffix[position][right] += 1

    matrix = [[0] * order for _ in range(order)]
    remainder = [2] * order
    canonical_solutions: set[tuple[int, ...]] = set()
    node_count = 0
    row_sum_leaves = 0

    def is_connected() -> bool:
        seen = {0}
        pending = [0]
        while pending:
            left = pending.pop()
            for right in range(order):
                if left != right and matrix[left][right] != 0 and right not in seen:
                    seen.add(right)
                    pending.append(right)
        return len(seen) == order

    def is_positive_semidefinite() -> bool:
        gram = sp.Matrix(
            [
                [
                    matrix[row][column] + (2 if row == column else 0)
                    for column in range(order)
                ]
                for row in range(order)
            ]
        )
        for mask in range(1, 1 << order):
            indices = [index for index in range(order) if mask & (1 << index)]
            if gram.extract(indices, indices).det(method="bareiss") < 0:
                return False
        return True

    def canonical_signed_key() -> tuple[int, ...]:
        return min(
            tuple(
                matrix[row][column]
                for row in permutation
                for column in permutation
            )
            for permutation in permutations(range(order))
        )

    def recurse(position: int) -> None:
        nonlocal node_count, row_sum_leaves
        node_count += 1
        if any(
            remainder[index] < -suffix[position][index]
            or remainder[index] > suffix[position][index]
            for index in range(order)
        ):
            return
        if position == len(pairs):
            if any(remainder):
                return
            row_sum_leaves += 1
            if not is_connected() or not is_positive_semidefinite():
                return
            canonical_solutions.add(canonical_signed_key())
            return

        left, right = pairs[position]
        for value in (-1, 0, 1):
            matrix[left][right] = value
            matrix[right][left] = value
            remainder[left] -= value
            remainder[right] -= value
            recurse(position + 1)
            remainder[left] += value
            remainder[right] += value
        matrix[left][right] = 0
        matrix[right][left] = 0

    recurse(0)
    if len(canonical_solutions) != 1:
        raise AssertionError(
            f"expected one signed six-vertex component, found {len(canonical_solutions)}"
        )
    representative = next(iter(canonical_solutions))
    unsigned_entries = {value for value in representative if value != 0}
    if unsigned_entries != {1}:
        raise AssertionError("the unique six-vertex component is not unsigned")
    return {
        "isomorphism_types": 1,
        "identification": "positive C6",
        "nodes": node_count,
        "row_sum_leaves": row_sum_leaves,
    }


def main() -> None:
    cases = {
        2: (1, 0),
        4: (0, 1),
        5: (1, 1),
    }
    expected = expected_small_quotients()
    reports: dict[int, dict[str, object]] = {}

    for count, (linear, cubic) in cases.items():
        solutions, nodes, leaves = enumerate_small_case(count, linear, cubic)
        keys = set(solutions)
        if keys != expected[count]:
            raise AssertionError(
                f"wrong canonical quotient set for c={count}: "
                f"found {len(keys)}, expected {len(expected[count])}"
            )
        reports[count] = {
            "canonical_quotients": len(keys),
            "nodes": nodes,
            "complete_row_sum_leaves": leaves,
        }

    four_cell_values = list(enumerate_small_case(4, 0, 1)[0].values())
    surviving_four_cell = [
        (sizes, quotient)
        for sizes, quotient in four_cell_values
        if 2 not in sizes
    ]
    if len(surviving_four_cell) != 2:
        raise AssertionError(
            f"expected two structurally feasible four-cell quotients, "
            f"found {len(surviving_four_cell)}"
        )

    c7_output = run_cpp_backend(
        "order50_component_quotients_c7.cpp",
        "solutions 0 nodes 13561449 leaves 5380",
    )
    c10_output = run_cpp_backend(
        "order50_component_quotients_c10.cpp",
        "solutions 0 nodes 7860789 leaves 0",
    )
    six_vertex = signed_six_uniqueness()

    print("order-50 signed-component quotient audit: PASS")
    print("small cases:", reports)
    print("surviving four-cell canonical types:")
    for sizes, quotient in sorted(surviving_four_cell):
        print(" sizes", sizes)
        for row in quotient:
            print("  ", row)
    print("seven-cell backend:", c7_output)
    print("ten-cell backend:", c10_output)
    print("six-vertex signed component:", six_vertex)


if __name__ == "__main__":
    main()
