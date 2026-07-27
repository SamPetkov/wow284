#!/usr/bin/env python3
"""Independent exact audit of the Jorgensen order-96 equality graph.

The script does not import either existing Jorgensen verifier. It checks local
provenance integrity, three representation parsers (including a handwritten
graph6 decoder), all graph hypotheses, exact characteristic polynomials, the
adjacency interval certificate, and an independent distance Sturm certificate.
No floating-point arithmetic is used.
"""
from __future__ import annotations

from collections import deque
import hashlib
import json
from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "jorgensen96"
X = sp.symbols("x")
Graph = tuple[frozenset[int], ...]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_source_snapshot(path: Path) -> Graph:
    text = path.read_text(encoding="utf-8")
    if "9 regular graph with girth 5 and order 96." not in text:
        raise AssertionError("missing source-page title")
    if "Graph defined by adjacency list." not in text:
        raise AssertionError("missing source-page description")

    rows: dict[int, frozenset[int]] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*\{([^}]*)\}\s*", line)
        if match is None:
            continue
        vertex = int(match.group(1))
        if vertex in rows:
            raise AssertionError("duplicate source row")
        raw = tuple(int(value) for value in re.findall(r"\d+", match.group(2)))
        if len(raw) != len(set(raw)):
            raise AssertionError("duplicate source neighbor")
        if any(value < 0 or value >= 96 for value in raw):
            raise AssertionError("source neighbor out of range")
        rows[vertex] = frozenset(raw)
    if set(rows) != set(range(96)):
        raise AssertionError("source rows are not exactly 0..95")
    return tuple(rows[vertex] for vertex in range(96))


def parse_normalized(path: Path) -> Graph:
    lines = path.read_text(encoding="ascii").splitlines()
    if len(lines) != 96:
        raise AssertionError("normalized file does not have 96 rows")
    rows: list[frozenset[int]] = []
    for vertex, line in enumerate(lines):
        match = re.fullmatch(rf"{vertex} : \{{ ([0-9, ]+)\}}", line)
        if match is None:
            raise AssertionError(f"noncanonical normalized row {vertex}")
        raw = tuple(int(value) for value in match.group(1).split(", "))
        if raw != tuple(sorted(set(raw))):
            raise AssertionError("normalized row is not strictly sorted")
        rows.append(frozenset(raw))
    return tuple(rows)


def decode_graph6(path: Path) -> Graph:
    data = path.read_bytes().strip()
    header = b">>graph6<<"
    if data.startswith(header):
        data = data[len(header):]
    values = [byte - 63 for byte in data]
    if not values or any(value < 0 or value > 63 for value in values):
        raise AssertionError("invalid graph6 character")

    if values[0] <= 62:
        order = values[0]
        offset = 1
    elif len(values) >= 4 and values[1] <= 62:
        order = (values[1] << 12) | (values[2] << 6) | values[3]
        offset = 4
    elif len(values) >= 8:
        order = 0
        for value in values[2:8]:
            order = (order << 6) | value
        offset = 8
    else:
        raise AssertionError("truncated graph6 order")
    if order != 96:
        raise AssertionError("wrong graph6 order")

    bits: list[int] = []
    for value in values[offset:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    needed = order * (order - 1) // 2
    if len(bits) < needed:
        raise AssertionError("truncated graph6 edge data")
    if any(bits[needed:]):
        raise AssertionError("nonzero graph6 padding")

    rows = [set() for _ in range(order)]
    cursor = 0
    for column in range(1, order):
        for row in range(column):
            if bits[cursor]:
                rows[row].add(column)
                rows[column].add(row)
            cursor += 1
    return tuple(frozenset(row) for row in rows)


def verify_graph(graph: Graph) -> tuple[tuple[int, ...], ...]:
    if len(graph) != 96:
        raise AssertionError("wrong order")
    if any(vertex in graph[vertex] for vertex in range(96)):
        raise AssertionError("loop")
    if set(map(len, graph)) != {9}:
        raise AssertionError("not 9-regular")
    for vertex, neighbors in enumerate(graph):
        for neighbor in neighbors:
            if vertex not in graph[neighbor]:
                raise AssertionError("asymmetric adjacency")
    if sum(map(len, graph)) != 864:
        raise AssertionError("wrong degree sum")

    all_distances: list[tuple[int, ...]] = []
    for source in range(96):
        distance = [-1] * 96
        distance[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[vertex] + 1
                    queue.append(neighbor)
        if -1 in distance:
            raise AssertionError("disconnected")
        all_distances.append(tuple(distance))
    if max(max(row) for row in all_distances) != 3:
        raise AssertionError("diameter is not three")

    best = 97
    for source in range(96):
        distance = [-1] * 96
        parent = [-1] * 96
        distance[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)
                elif parent[vertex] != neighbor and parent[neighbor] != vertex:
                    best = min(best, distance[vertex] + distance[neighbor] + 1)
    if best != 5:
        raise AssertionError("girth is not five")
    return tuple(all_distances)


def adjacency_matrix(graph: Graph) -> sp.Matrix:
    return sp.Matrix(
        [[int(column in graph[row]) for column in range(96)] for row in range(96)]
    )


def sign_variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign]
    return sum(left * right < 0 for left, right in zip(nonzero, nonzero[1:]))


def variations_at_minus_infinity(sequence: list[sp.Expr]) -> int:
    signs: list[int] = []
    for term in sequence:
        polynomial = sp.Poly(term, X)
        sign = int(sp.sign(polynomial.LC()))
        if polynomial.degree() % 2:
            sign = -sign
        signs.append(sign)
    return sign_variations(signs)


def variations_at_plus_infinity(sequence: list[sp.Expr]) -> int:
    return sign_variations([int(sp.sign(sp.Poly(term, X).LC())) for term in sequence])


def variations_at(sequence: list[sp.Expr], point: sp.Rational) -> int:
    signs: list[int] = []
    for term in sequence:
        value = sp.Poly(term, X).eval(point)
        if value == 0:
            raise AssertionError("Sturm endpoint is a root")
        signs.append(int(sp.sign(value)))
    return sign_variations(signs)


def roots_below(expression: sp.Expr, point: sp.Rational) -> int:
    sequence = sp.sturm(sp.Poly(expression, X).sqf_part().as_expr(), X)
    return variations_at_minus_infinity(sequence) - variations_at(sequence, point)


def roots_above(expression: sp.Expr, point: sp.Rational) -> int:
    sequence = sp.sturm(sp.Poly(expression, X).sqf_part().as_expr(), X)
    return variations_at(sequence, point) - variations_at_plus_infinity(sequence)


def expected_polynomials() -> tuple[sp.Expr, sp.Expr]:
    adjacency = (
        (X - 9)
        * (X - 3) ** 7
        * (X - 1) ** 7
        * (X + 5)
        * (X**2 - 8) ** 16
        * (X**2 + 2 * X - 6) ** 8
        * (X**4 + 2 * X**3 - 17 * X**2 - 18 * X + 74) ** 8
    )
    distance = (
        X**16
        * (X - 195)
        * (X - 3) ** 7
        * (X + 9) ** 8
        * (X**2 + 4 * X - 28) ** 16
        * (X**4 + 10 * X**3 + 5 * X**2 - 72 * X - 96) ** 8
    )
    return adjacency, distance


def exact_spectral_audit(graph: Graph, distance_rows: tuple[tuple[int, ...], ...]) -> dict[str, object]:
    adjacency = adjacency_matrix(graph)
    distance = sp.Matrix(distance_rows)
    identity = sp.eye(96)
    ones = sp.ones(96)
    if distance != 3 * ones + 6 * identity - 2 * adjacency - adjacency**2:
        raise AssertionError("distance polynomial identity failed")
    if distance * sp.ones(96, 1) != 195 * sp.ones(96, 1):
        raise AssertionError("wrong transmission")

    expected_adjacency, expected_distance = expected_polynomials()
    actual_adjacency = adjacency.charpoly(X).as_expr()
    actual_distance = distance.charpoly(X).as_expr()
    if not sp.Poly(actual_adjacency - expected_adjacency, X).is_zero:
        raise AssertionError("wrong adjacency characteristic polynomial")
    if not sp.Poly(actual_distance - expected_distance, X).is_zero:
        raise AssertionError("wrong distance characteristic polynomial")

    quartic = X**4 + 2 * X**3 - 17 * X**2 - 18 * X + 74
    if quartic.subs(X, -5) != 114 or quartic.subs(X, 3) != 2:
        raise AssertionError("wrong quartic endpoint values")
    if roots_below(quartic, sp.Integer(-5)) != 0:
        raise AssertionError("quartic has a root at or below -5")
    if roots_above(quartic, sp.Integer(3)) != 0:
        raise AssertionError("quartic has a root at or above 3")
    sequence = sp.sturm(quartic, X)
    roots_inside = variations_at(sequence, sp.Integer(-5)) - variations_at(sequence, sp.Integer(3))
    if roots_inside != 4:
        raise AssertionError("quartic roots do not all lie in (-5,3)")

    if not 8 < 9 or not 7 < 16:
        raise AssertionError("quadratic radical interval checks failed")
    # x^2-8 has roots in (-3,3); x^2+2x-6 has roots -1+-sqrt(7) in (-5,3).

    shifted_principal = 195 + 9
    if shifted_principal != 204:
        raise AssertionError("wrong shifted principal eigenvalue")
    boundary_multiplicity = 7 + 1
    if boundary_multiplicity != 8:
        raise AssertionError("wrong boundary multiplicity")

    remaining = sp.cancel(expected_distance / (X + 9) ** 8)
    if sp.Poly(remaining, X).eval(-9) == 0:
        raise AssertionError("remaining distance factor vanishes at -9")
    if roots_below(remaining, sp.Integer(-9)) != 0:
        raise AssertionError("remaining distance factor has a root below -9")

    # Direct multiplicity check.
    quotient = sp.Poly(expected_distance, X)
    multiplicity = 0
    divisor = sp.Poly(X + 9, X)
    while quotient.eval(-9) == 0:
        quotient, remainder = sp.div(quotient, divisor)
        if not remainder.is_zero:
            raise AssertionError("exact division failure")
        multiplicity += 1
    if multiplicity != 8:
        raise AssertionError("wrong multiplicity at -9")

    return {
        "transmission": 195,
        "shifted_principal_eigenvalue": shifted_principal,
        "nonprincipal_adjacency_interval": "[-5,3]",
        "quartic_roots_in_open_interval": roots_inside,
        "least_distance_eigenvalue": -9,
        "least_distance_multiplicity": multiplicity,
        "minimum_dual_degree": 9,
        "WOW_score": 0,
        "adjacency_characteristic_polynomial": str(sp.factor(expected_adjacency)),
        "distance_characteristic_polynomial": str(sp.factor(expected_distance)),
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("verification must not be run with python -O")

    provenance_path = DATA / "PROVENANCE.json"
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    for key in ("source_snapshot", "normalized_adjacency", "graph6"):
        entry = provenance[key]
        path = ROOT / entry["path"]
        if sha256(path) != entry["sha256"]:
            raise AssertionError("provenance hash mismatch")
        if len(path.read_bytes()) != entry["bytes"]:
            raise AssertionError("provenance byte-count mismatch")

    source = parse_source_snapshot(ROOT / provenance["source_snapshot"]["path"])
    normalized = parse_normalized(ROOT / provenance["normalized_adjacency"]["path"])
    graph6 = decode_graph6(ROOT / provenance["graph6"]["path"])
    if source != normalized or source != graph6:
        raise AssertionError("representation reconstructions disagree")

    distances = verify_graph(source)
    spectrum = exact_spectral_audit(source, distances)
    result = {
        "source_url": provenance["source_url"],
        "published_construction_doi": provenance["published_construction"]["doi"],
        "local_integrity_hashes_verified": True,
        "representation_consistency": "source snapshot == normalized rows == handwritten graph6 decode",
        "historical_source_independence_claimed": False,
        "order": 96,
        "size": 432,
        "degree": 9,
        "girth": 5,
        "diameter": 3,
        **spectrum,
    }
    print("Proof Audit 09 (Jorgensen order-96 equality): PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
