#!/usr/bin/env python3
"""Export reproducible graph representations for the verified examples."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from verify_wow284_38_40_42 import hoffman_singleton, induced  # noqa: E402

OUT = ROOT / "data" / "graphs"


def edge_list(graph):
    return [(u, v) for u in range(len(graph)) for v in graph[u] if u < v]


def graph6(graph) -> str:
    g = nx.Graph()
    g.add_nodes_from(range(len(graph)))
    g.add_edges_from(edge_list(graph))
    return nx.to_graph6_bytes(g, header=False).decode("ascii").strip()


def adjacency_lines(graph):
    return [f"{u}: {' '.join(map(str, sorted(graph[u])))}" for u in range(len(graph))]


def export(name, graph, labels, description):
    OUT.mkdir(parents=True, exist_ok=True)
    edges = edge_list(graph)
    (OUT / f"{name}.graph6").write_text(graph6(graph) + "\n", encoding="ascii")
    (OUT / f"{name}_adjacency.txt").write_text("\n".join(adjacency_lines(graph)) + "\n", encoding="utf-8")
    with (OUT / f"{name}_edges.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
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


def main():
    full, labels = hoffman_singleton()
    items = []
    items.append(export("G50", full, labels, "Hoffman-Singleton coordinate graph"))

    deleted40 = {("P", 0, j) for j in range(5)} | {("Q", 0, j) for j in range(5)}
    g40, l40 = induced(full, labels, deleted40)
    items.append(export("G40", g40, l40, "delete P_(0,*) and Q_(0,*) from G50"))

    g39, l39 = induced(g40, l40, {("P", 1, 0)})
    items.append(export("G39", g39, l39, "delete P_(1,0) from G40"))

    g38, l38 = induced(g40, l40, {("P", 1, 0), ("P", 1, 1)})
    items.append(export("G38", g38, l38, "delete adjacent P_(1,0), P_(1,1) from G40"))

    root = labels.index(("P", 0, 0))
    deleted42 = {labels[root]} | {labels[v] for v in full[root]}
    g42, l42 = induced(full, labels, deleted42)
    items.append(export("G42", g42, l42, "second subconstituent of P_(0,0) in G50"))

    (OUT / "summary.json").write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")
    print(f"exported {len(items)} graphs to {OUT}")
    for item in items:
        print(item["name"], item["order"], item["size"], item["graph6"])


if __name__ == "__main__":
    main()
