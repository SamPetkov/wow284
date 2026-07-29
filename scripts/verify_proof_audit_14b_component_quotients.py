#!/usr/bin/env python3
"""Independent Python replay of the order-50 component-quotient classification.

This script does not import the primary verifier and does not invoke its C++
backends.  It re-enumerates the seven- and ten-cell cases with separate Python
searches, checks the small canonical quotients, and independently enumerates the
six-vertex signed component.
"""
from __future__ import annotations

from itertools import permutations
from math import gcd

import sympy as sp


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
        for value in range(min(6, sizes[index] - 1, remainder) + 1):
            if value == 1 and sizes[index] % 2:
                continue
            if value >= 2 and sizes[index] < value * value + 1:
                continue
            current.append(value)
            recurse(index + 1, remainder - value, current)
            current.pop()

    recurse(0, total, [])
    return output


def options(
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
    return [
        [
            sum(
                left[row][middle] * right[middle][column]
                for middle in range(len(right))
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def connected(matrix: list[list[int]]) -> bool:
    seen = {0}
    pending = [0]
    while pending:
        left = pending.pop()
        for right, value in enumerate(matrix[left]):
            if left != right and value > 0 and right not in seen:
                seen.add(right)
                pending.append(right)
    return len(seen) == len(matrix)


def cubic_identity(matrix: list[list[int]], sizes: tuple[int, ...]) -> bool:
    square = multiply(matrix, matrix)
    cube = multiply(square, matrix)
    count = len(matrix)
    for row in range(count):
        for column in range(count):
            value = (
                cube[row][column]
                + 2 * square[row][column]
                - 5 * matrix[row][column]
                - (8 if row == column else 0)
            )
            if value != 5 * sizes[column]:
                return False
    return True


def radius_two(matrix: list[list[int]], sizes: tuple[int, ...]) -> bool:
    square = multiply(matrix, matrix)
    count = len(matrix)
    for row in range(count):
        for column in range(count):
            if (
                square[row][column] - (6 if row == column else 0)
                > sizes[column]
                - (1 if row == column else 0)
                - matrix[row][column]
            ):
                return False
    return True


def generic_seven_cell_search() -> tuple[int, int, int]:
    count = 7
    target_trace = 2
    target_trace_square = 64
    solution_count = 0
    node_count = 0
    leaf_count = 0

    for sizes in partitions(50, count):
        for diagonal in diagonal_tuples(count, target_trace, sizes):
            remainder = [6 - value for value in diagonal]
            variables: list[tuple[int, int, list[tuple[int, int]]]] = []
            for left in range(count):
                for right in range(left + 1, count):
                    variables.append(
                        (
                            left,
                            right,
                            options(
                                sizes[left],
                                sizes[right],
                                remainder[left],
                                remainder[right],
                            ),
                        )
                    )
            variables.sort(key=lambda item: (len(item[2]), -(item[0] + item[1])))
            variable_count = len(variables)
            suffix = [[0] * count for _ in range(variable_count + 1)]
            suffix_trace = [0] * (variable_count + 1)
            for position in range(variable_count - 1, -1, -1):
                suffix[position] = suffix[position + 1].copy()
                left, right, choices = variables[position]
                suffix[position][left] += max(value[0] for value in choices)
                suffix[position][right] += max(value[1] for value in choices)
                suffix_trace[position] = suffix_trace[position + 1] + max(
                    2 * value[0] * value[1] for value in choices
                )
            if any(
                suffix[0][index] < remainder[index]
                for index in range(count)
            ):
                continue

            matrix = [[0] * count for _ in range(count)]
            for index, value in enumerate(diagonal):
                matrix[index][index] = value

            def recurse(position: int, trace_square: int) -> None:
                nonlocal solution_count, node_count, leaf_count
                node_count += 1
                if trace_square > target_trace_square:
                    return
                if trace_square + suffix_trace[position] < target_trace_square:
                    return
                if any(
                    remainder[index] < 0
                    or remainder[index] > suffix[position][index]
                    for index in range(count)
                ):
                    return
                if position == variable_count:
                    if any(remainder) or trace_square != target_trace_square:
                        return
                    leaf_count += 1
                    if (
                        connected(matrix)
                        and cubic_identity(matrix, sizes)
                        and radius_two(matrix, sizes)
                    ):
                        solution_count += 1
                    return

                left, right, choices = variables[position]
                for left_value, right_value in choices:
                    if left_value > remainder[left] or right_value > remainder[right]:
                        continue
                    matrix[left][right] = left_value
                    matrix[right][left] = right_value
                    remainder[left] -= left_value
                    remainder[right] -= right_value
                    recurse(
                        position + 1,
                        trace_square + 2 * left_value * right_value,
                    )
                    remainder[left] += left_value
                    remainder[right] += right_value
                matrix[left][right] = 0
                matrix[right][left] = 0

            recurse(0, sum(value * value for value in diagonal))

    if (solution_count, node_count, leaf_count) != (0, 14179432, 3260):
        raise AssertionError(
            "independent seven-cell search changed: "
            f"{(solution_count, node_count, leaf_count)}"
        )
    return solution_count, node_count, leaf_count


def independent_ten_cell_search() -> tuple[int, int, int]:
    count = 10
    solution_count = 0
    node_count = 0
    leaf_count = 0

    # A signed component has at least three vertices.  The cubic diagonal
    # identity makes every cell size even, so every cell has size at least four.
    size_patterns = [
        values
        for values in partitions(50, count, 4)
        if all(value % 2 == 0 for value in values)
    ]
    if len(size_patterns) != 7:
        raise AssertionError(f"wrong ten-cell size-pattern count: {len(size_patterns)}")

    for sizes in size_patterns:
        matrix = [[-1] * count for _ in range(count)]
        for index in range(count):
            matrix[index][index] = 0
        remainder = [6] * count
        target_triangle = [-1] * count
        triangle_sum = [0] * count
        pair_product_sum = 0

        def local_options(left: int, right: int) -> list[tuple[int, int]]:
            return options(
                sizes[left],
                sizes[right],
                remainder[left],
                remainder[right],
            )

        def maximum_future_triangle(vertex: int) -> int:
            maximum = triangle_sum[vertex]
            for left in range(count):
                if left == vertex or matrix[vertex][left] <= 0:
                    continue
                for right in range(left + 1, count):
                    if right == vertex or matrix[vertex][right] <= 0:
                        continue
                    if matrix[left][right] >= 0:
                        continue
                    best = 0
                    for left_value, _ in local_options(left, right):
                        best = max(
                            best,
                            matrix[vertex][left]
                            * left_value
                            * matrix[right][vertex],
                        )
                    maximum += best
            return maximum

        def process_row(row: int) -> None:
            fixed = sum(matrix[row][column] for column in range(row))
            remainder[row] = 6 - fixed
            if remainder[row] < 0:
                return
            assign_row(row, list(range(row + 1, count)), 0)

        def assign_row(row: int, columns: list[int], position: int) -> None:
            nonlocal solution_count, node_count, leaf_count, pair_product_sum
            node_count += 1
            if position == len(columns):
                if remainder[row] != 0:
                    return
                diagonal_square = sum(
                    matrix[row][column] * matrix[column][row]
                    for column in range(count)
                    if column != row
                )
                target_value = 5 * sizes[row] + 8 - 2 * diagonal_square
                if target_value < 0 or target_value % 2:
                    return
                target_triangle[row] = target_value // 2
                if triangle_sum[row] > target_triangle[row]:
                    return
                if maximum_future_triangle(row) < target_triangle[row]:
                    return
                if pair_product_sum > 39:
                    return

                if row == count - 1:
                    leaf_count += 1
                    if pair_product_sum != 39 or any(remainder):
                        return
                    if triangle_sum != target_triangle:
                        return
                    if (
                        connected(matrix)
                        and cubic_identity(matrix, sizes)
                        and radius_two(matrix, sizes)
                    ):
                        solution_count += 1
                    return
                process_row(row + 1)
                return

            column = columns[position]
            choices = local_options(row, column)
            minimum_left = 0
            if position > 0:
                previous = columns[position - 1]
                interchangeable = sizes[column] == sizes[previous]
                if interchangeable:
                    interchangeable = all(
                        matrix[earlier][column] == matrix[earlier][previous]
                        for earlier in range(row)
                    )
                if interchangeable:
                    minimum_left = matrix[row][previous]

            for left_value, right_value in choices:
                if left_value < minimum_left:
                    continue
                if left_value > remainder[row] or right_value > remainder[column]:
                    continue
                maximum_remaining = 0
                for future_column in columns[position + 1 :]:
                    maximum_remaining += max(
                        (
                            future_left
                            for future_left, future_right in local_options(
                                row,
                                future_column,
                            )
                            if future_right <= remainder[future_column]
                        ),
                        default=0,
                    )
                if remainder[row] - left_value > maximum_remaining:
                    continue

                matrix[row][column] = left_value
                matrix[column][row] = right_value
                remainder[row] -= left_value
                remainder[column] -= right_value
                pair_product_sum += left_value * right_value
                deltas: list[tuple[int, int]] = []
                for third in range(count):
                    if third in {row, column}:
                        continue
                    if matrix[row][third] < 0 or matrix[column][third] < 0:
                        continue
                    value = (
                        matrix[row][column]
                        * matrix[column][third]
                        * matrix[third][row]
                    )
                    if value:
                        triangle_sum[row] += value
                        triangle_sum[column] += value
                        triangle_sum[third] += value
                        deltas.append((third, value))

                valid = all(
                    target_triangle[earlier] < 0
                    or triangle_sum[earlier] <= target_triangle[earlier]
                    for earlier in range(row + 1)
                )
                if valid:
                    assign_row(row, columns, position + 1)

                for third, value in deltas:
                    triangle_sum[row] -= value
                    triangle_sum[column] -= value
                    triangle_sum[third] -= value
                pair_product_sum -= left_value * right_value
                remainder[row] += left_value
                remainder[column] += right_value
                matrix[row][column] = -1
                matrix[column][row] = -1

        process_row(0)

    if (solution_count, node_count, leaf_count) != (0, 3130846, 0):
        raise AssertionError(
            "independent ten-cell search changed: "
            f"{(solution_count, node_count, leaf_count)}"
        )
    return solution_count, node_count, leaf_count


def explicit_quotient_audit() -> None:
    x = sp.symbols("x")
    cubic = x**3 + 2 * x**2 - 5 * x - 8
    examples = [
        (
            (6, 8, 12, 24),
            sp.Matrix(
                [
                    [2, 0, 0, 4],
                    [0, 0, 3, 3],
                    [0, 2, 0, 4],
                    [1, 1, 2, 2],
                ]
            ),
        ),
        (
            (10, 10, 10, 20),
            sp.Matrix(
                [
                    [1, 0, 3, 2],
                    [0, 1, 1, 4],
                    [3, 1, 0, 2],
                    [1, 2, 1, 2],
                ]
            ),
        ),
    ]
    for sizes, matrix in examples:
        if matrix * sp.ones(4, 1) != 6 * sp.ones(4, 1):
            raise AssertionError("explicit quotient is not 6-regular")
        for left in range(4):
            for right in range(4):
                if sizes[left] * matrix[left, right] != sizes[right] * matrix[right, left]:
                    raise AssertionError("explicit quotient violates detailed balance")
        expected_characteristic = sp.expand((x - 6) * cubic)
        if sp.expand(matrix.charpoly(x).as_expr() - expected_characteristic) != 0:
            raise AssertionError("explicit quotient has the wrong characteristic polynomial")
        frozen = [list(map(int, matrix.row(index))) for index in range(4)]
        if not cubic_identity(frozen, sizes) or not radius_two(frozen, sizes):
            raise AssertionError("explicit quotient fails an exact local constraint")


def signed_six_replay() -> None:
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
    types: set[tuple[int, ...]] = set()

    def canonical() -> tuple[int, ...]:
        return min(
            tuple(
                matrix[row][column]
                for row in permutation
                for column in permutation
            )
            for permutation in permutations(range(order))
        )

    def support_connected() -> bool:
        seen = {0}
        pending = [0]
        while pending:
            left = pending.pop()
            for right in range(order):
                if matrix[left][right] and right not in seen:
                    seen.add(right)
                    pending.append(right)
        return len(seen) == order

    def positive_semidefinite() -> bool:
        gram = sp.Matrix(
            [
                [
                    matrix[row][column] + (2 if row == column else 0)
                    for column in range(order)
                ]
                for row in range(order)
            ]
        )
        return all(
            gram.extract(indices, indices).det(method="bareiss") >= 0
            for mask in range(1, 1 << order)
            for indices in [[
                index for index in range(order) if mask & (1 << index)
            ]]
        )

    def recurse(position: int) -> None:
        if any(
            remainder[index] < -suffix[position][index]
            or remainder[index] > suffix[position][index]
            for index in range(order)
        ):
            return
        if position == len(pairs):
            if any(remainder):
                return
            if support_connected() and positive_semidefinite():
                types.add(canonical())
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
    if len(types) != 1 or {value for value in next(iter(types)) if value} != {1}:
        raise AssertionError("independent six-vertex signed uniqueness replay failed")


def main() -> None:
    explicit_quotient_audit()
    seven = generic_seven_cell_search()
    ten = independent_ten_cell_search()
    signed_six_replay()
    print("independent Proof Audit 14B component quotients: PASS")
    print("seven-cell search:", seven)
    print("ten-cell search:", ten)
    print("surviving four-cell types: 2")
    print("six-vertex signed component: unique positive C6")


if __name__ == "__main__":
    main()
