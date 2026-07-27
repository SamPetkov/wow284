#!/usr/bin/env python3
"""Exact score calculus for regular girth-five graphs of diameter two or three.

The script is intentionally independent of graph reconstruction.  It checks the
spectral transfer formulas on the exact adjacency spectra used in the manuscript
and verifies the Moore threshold by integer arithmetic only.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class RegularCase:
    name: str
    order: int
    degree: int
    diameter: int
    adjacency_spectrum: tuple[tuple[int, int], ...]
    expected_distance_spectrum: tuple[tuple[int, int], ...]
    expected_score: int


def canonical_spectrum(
    entries: Counter[int] | dict[int, int],
) -> tuple[tuple[int, int], ...]:
    return tuple(
        sorted(
            (
                (value, multiplicity)
                for value, multiplicity in entries.items()
                if multiplicity
            ),
            reverse=True,
        )
    )


def verify_adjacency_data(case: RegularCase) -> None:
    if sum(multiplicity for _, multiplicity in case.adjacency_spectrum) != case.order:
        raise AssertionError(
            f"{case.name}: adjacency multiplicities do not sum to the order"
        )
    if sum(
        value * multiplicity for value, multiplicity in case.adjacency_spectrum
    ) != 0:
        raise AssertionError(f"{case.name}: adjacency trace is not zero")
    principal = [
        (value, multiplicity)
        for value, multiplicity in case.adjacency_spectrum
        if value == case.degree
    ]
    if principal != [(case.degree, 1)]:
        raise AssertionError(
            f"{case.name}: principal adjacency eigenvalue is not simple"
        )


def transfer_distance_spectrum(
    case: RegularCase,
) -> tuple[tuple[int, int], ...]:
    """Apply the exact distance polynomial to an integral adjacency spectrum."""
    verify_adjacency_data(case)
    n, k = case.order, case.degree
    distance: Counter[int] = Counter()

    if case.diameter == 2:
        # Girth at least five and diameter two force the Moore bound with equality.
        distance[2 * n - 2 - k] += 1
        for theta, multiplicity in case.adjacency_spectrum:
            if theta != k:
                distance[-2 - theta] += multiplicity
    elif case.diameter == 3:
        distance[3 * n - k * k - k - 3] += 1
        for theta, multiplicity in case.adjacency_spectrum:
            if theta != k:
                distance[k - 2 - (theta + 1) ** 2] += multiplicity
    else:
        raise AssertionError(f"{case.name}: unsupported diameter {case.diameter}")

    result = canonical_spectrum(distance)
    if sum(multiplicity for _, multiplicity in result) != n:
        raise AssertionError(
            f"{case.name}: distance multiplicities do not sum to the order"
        )
    return result


def verify_case(case: RegularCase) -> dict[str, object]:
    actual = transfer_distance_spectrum(case)
    expected = tuple(sorted(case.expected_distance_spectrum, reverse=True))
    if actual != expected:
        raise AssertionError(
            f"{case.name}: distance spectrum mismatch\n"
            f"actual={actual}\nexpected={expected}"
        )

    least = min(value for value, _ in actual)
    score = case.degree + least
    if score != case.expected_score:
        raise AssertionError(f"{case.name}: wrong WOW score")

    nonprincipal = [
        value for value, _ in case.adjacency_spectrum if value != case.degree
    ]
    if case.diameter == 2:
        lambda_two = max(nonprincipal)
        score_from_scalar_test = case.degree - 2 - lambda_two
        scalar_parameter = {"lambda_2": lambda_two}
    else:
        shifted_radius_squared = max((value + 1) ** 2 for value in nonprincipal)
        score_from_scalar_test = 2 * case.degree - 2 - shifted_radius_squared
        scalar_parameter = {
            "shifted_adjacency_radius_squared": shifted_radius_squared
        }
    if score_from_scalar_test != score:
        raise AssertionError(f"{case.name}: scalar score identity failed")

    return {
        "name": case.name,
        "order": case.order,
        "degree": case.degree,
        "diameter": case.diameter,
        "adjacency_spectrum": list(case.adjacency_spectrum),
        "distance_spectrum": list(actual),
        "least_distance_eigenvalue": least,
        "WOW_score": score,
        **scalar_parameter,
    }


def verify_moore_threshold(limit: int = 10_000) -> dict[str, int]:
    """Verify the sign reduction by the exact squared-difference identity."""
    if limit < 3:
        raise ValueError("limit must be at least three")

    negative = zero = positive = 0
    for k in range(2, limit + 1):
        squared_difference = (2 * k - 3) ** 2 - (4 * k - 3)
        if squared_difference != 4 * (k - 1) * (k - 3):
            raise AssertionError("Moore threshold identity failed")
        if k == 2:
            # 2k-3 = 1 < sqrt(5), hence the score is negative.
            if squared_difference >= 0:
                raise AssertionError("degree-two sign check failed")
            negative += 1
        elif k == 3:
            if squared_difference != 0:
                raise AssertionError("Petersen equality check failed")
            zero += 1
        else:
            if squared_difference <= 0 or 2 * k - 3 <= 0:
                raise AssertionError("strict Moore violation check failed")
            positive += 1
    return {
        "checked_degrees": limit - 1,
        "negative_scores": negative,
        "zero_scores": zero,
        "positive_scores": positive,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    cases = (
        RegularCase(
            name="Petersen graph",
            order=10,
            degree=3,
            diameter=2,
            adjacency_spectrum=((3, 1), (1, 5), (-2, 4)),
            expected_distance_spectrum=((15, 1), (0, 4), (-3, 5)),
            expected_score=0,
        ),
        RegularCase(
            name="Hoffman--Singleton graph",
            order=50,
            degree=7,
            diameter=2,
            adjacency_spectrum=((7, 1), (2, 28), (-3, 21)),
            expected_distance_spectrum=((91, 1), (1, 21), (-4, 28)),
            expected_score=3,
        ),
        RegularCase(
            name="O'Keefe--Wong graph",
            order=40,
            degree=6,
            diameter=3,
            adjacency_spectrum=((6, 1), (2, 18), (1, 4), (-2, 5), (-3, 12)),
            expected_distance_spectrum=((75, 1), (3, 5), (0, 16), (-5, 18)),
            expected_score=1,
        ),
        RegularCase(
            name="Hoffman--Singleton second subconstituent",
            order=42,
            degree=6,
            diameter=3,
            adjacency_spectrum=((6, 1), (2, 21), (-1, 6), (-3, 14)),
            expected_distance_spectrum=((81, 1), (4, 6), (0, 14), (-5, 21)),
            expected_score=1,
        ),
    )

    result = {
        "regular_cases": [verify_case(case) for case in cases],
        "moore_threshold": verify_moore_threshold(),
    }
    print("regular WOW-score calculus: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
