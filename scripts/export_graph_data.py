#!/usr/bin/env python3
"""Export deterministic edge, adjacency, and distance data as CSV files."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from wow284_graph import (  # noqa: E402
    VERTEX_COUNT,
    adjacency_list,
    adjacency_matrix,
    all_pairs_distances,
    build_edges,
    vertex_name,
)


def edge_type(u: int, v: int) -> str:
    if u < 25 and v < 25:
        return "P"
    if u >= 25 and v >= 25:
        return "Q"
    return "cross"


def write_matrix(path: Path, matrix: tuple[tuple[int, ...], ...]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["vertex", *range(VERTEX_COUNT)])
        for vertex, row in enumerate(matrix):
            writer.writerow([vertex, *row])


def export(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    edges = build_edges()
    graph = adjacency_list(edges)

    with (output_dir / "edges.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["u", "u_name", "v", "v_name", "edge_type"])
        for u, v in edges:
            writer.writerow([u, vertex_name(u), v, vertex_name(v), edge_type(u, v)])

    write_matrix(output_dir / "adjacency_matrix.csv", adjacency_matrix(graph))
    write_matrix(output_dir / "distance_matrix.csv", all_pairs_distances(graph))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()
    target = args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir
    export(target)
    print(f"exported exact graph data to {target}")


if __name__ == "__main__":
    main()
