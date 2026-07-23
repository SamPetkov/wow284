#!/usr/bin/env python3
"""Export reproducible graph representations for the verified examples."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys
import tempfile

import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from verify_wow284_38_40_42 import hoffman_singleton, induced  # noqa: E402

OUT = ROOT / "data" / "graphs"


def edge_list(graph):
    return [(u, v) for u in range(len(graph)) for v in sorted(graph[u]) if u < v]


def graph6(graph) -> str:
    g = nx.Graph()
    g.add_nodes_from(range(len(graph)))
    g.add_edges_from(edge_list(graph))
    return nx.to_graph6_bytes(g, header=False).decode("ascii").strip()


def adjacency_lines(graph):
    return [f"{u}: {' '.join(map(str, sorted(graph[u])))}" for u in range(len(graph))]


def export(out, name, graph, labels, description):
    out.mkdir(parents=True, exist_ok=True)
    edges = edge_list(graph)
    (out / f"{name}.graph6").write_text(
        graph6(graph) + "\n", encoding="ascii", newline="\n"
    )
    (out / f"{name}_adjacency.txt").write_text(
        "\n".join(adjacency_lines(graph)) + "\n", encoding="utf-8", newline="\n"
    )
    with (out / f"{name}_edges.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["u", "v", "u_coordinate", "v_coordinate"])
        for u, v in edges:
            writer.writerow([u, v, repr(labels[u]), repr(labels[v])])
    return {
        "name": name,
        "description": description,
        "order": len(graph),
        "size": len(edges),
        "graph6": graph6(graph),
        "labeling": "surviving ambient coordinate labels in increasing ambient order, relabeled 0,...,n-1",
    }


def build(out: Path):
    full, labels = hoffman_singleton()
    items = []
    items.append(export(out, "G50", full, labels, "Hoffman-Singleton coordinate graph"))

    deleted40 = {("P", 0, j) for j in range(5)} | {("Q", 0, j) for j in range(5)}
    g40, l40 = induced(full, labels, deleted40)
    items.append(export(out, "G40", g40, l40, "delete P_(0,*) and Q_(0,*) from G50"))

    g39, l39 = induced(g40, l40, {("P", 1, 0)})
    items.append(export(out, "G39", g39, l39, "delete P_(1,0) from G40"))

    g38, l38 = induced(g40, l40, {("P", 1, 0), ("P", 1, 1)})
    items.append(export(out, "G38", g38, l38, "delete adjacent P_(1,0), P_(1,1) from G40"))

    root = labels.index(("P", 0, 0))
    deleted42 = {labels[root]} | {labels[v] for v in full[root]}
    g42, l42 = induced(full, labels, deleted42)
    items.append(export(out, "G42", g42, l42, "second subconstituent of P_(0,0) in G50"))

    (out / "summary.json").write_text(
        json.dumps(items, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    return items


def check() -> None:
    with tempfile.TemporaryDirectory(prefix="wow284-graphs-") as temporary:
        generated = Path(temporary)
        build(generated)
        expected_names = sorted(path.name for path in OUT.iterdir() if path.is_file())
        generated_names = sorted(path.name for path in generated.iterdir() if path.is_file())
        if generated_names != expected_names:
            raise AssertionError(
                f"graph file set differs: expected {expected_names}, generated {generated_names}"
            )
        for name in expected_names:
            if (OUT / name).read_bytes() != (generated / name).read_bytes():
                raise AssertionError(f"generated graph file differs: {name}")
    print(f"all graph representations match {OUT}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare without writing")
    args = parser.parse_args()
    if args.check:
        check()
        return

    items = build(OUT)
    print(f"exported {len(items)} graphs to {OUT}")
    for item in items:
        print(item["name"], item["order"], item["size"], item["graph6"])


if __name__ == "__main__":
    main()
