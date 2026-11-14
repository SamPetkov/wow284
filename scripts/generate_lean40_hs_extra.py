#!/usr/bin/env python3
"""Generate Lean certificates for new irregular order-40 strict counterexamples
inside the Hoffman--Singleton graph, found by the exact Aut(HS)-orbit
enumeration of scripts/small_order_hs_orbits.py (all strict induced
subgraphs of order 40 other than the (6,5)-cage R).

Reuses, unchanged, the order-39/42 renderers (lean3942_common, lean3942_finite,
lean3942_ldl): an induced subgraph of the coordinate HS graph, embedded into
`Wow284.Vertex`; finite `decide` certificates for degrees, dual degrees,
diameter three and the semantic distance matrix; and a column-scaled integer
LDL certificate of positive definiteness of qD + pI, where p/q is the exact
minimum dual degree.

  python scripts/generate_lean40_hs_extra.py            # write files
  python scripts/generate_lean40_hs_extra.py --check    # compare
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path

from common_graphs import hoffman_singleton, induced, distance_matrix, dual_degrees
from lean3942_common import ROOT, Spec, verify_spec, basic, bridge, counterexample
from lean3942_finite import finite_outputs
from lean3942_ldl import ldl_outputs

# Deleted HS vertices (paper coordinates) for each new graph.
GRAPHS = {
    # X42 minus the endpoints of the edge P_(0,2) P_(0,3): HS - {P_(0,*), Q_(*,0)}.
    "Induced40X": [("P", 0, j) for j in range(5)] + [("Q", k, 0) for k in range(5)],
    # Two irregular orbits with minimum dual degree 39/7 (degrees 5, 6, 7).
    "Induced40Y": [("P", 0, j) for j in range(5)]
    + [("P", 1, 0), ("Q", 0, 0), ("Q", 0, 2), ("Q", 2, 2), ("Q", 4, 4)],
    "Induced40Z": [("P", 0, j) for j in range(5)]
    + [("P", 1, 0), ("Q", 0, 0), ("Q", 0, 2), ("Q", 1, 1), ("Q", 1, 4)],
}


def five_cycle(graph):
    n = len(graph)
    for a in range(n):
        for b in sorted(graph[a]):
            for c in sorted(graph[b] - {a}):
                for d in sorted(graph[c] - {a, b}):
                    for e in sorted(graph[d] - {a, b, c}):
                        if a in graph[e]:
                            return (a, b, c, d, e)
    raise AssertionError("no five-cycle")


def make_spec(namespace: str, deleted) -> Spec:
    full, labels = hoffman_singleton()
    graph, kept_labels = induced(full, labels, deleted)
    index = {label: i for i, label in enumerate(labels)}
    old = [index[label] for label in kept_labels]
    assert old == sorted(old) and len(graph) == 40
    duals = dual_degrees(graph)
    dstar = min(duals)
    p, q = dstar.numerator, dstar.denominator
    attained = duals.index(dstar)
    degrees = tuple(len(row) for row in graph)
    values = tuple(sorted(set(degrees)))
    profile = tuple((d, degrees.count(d)) for d in values)
    dist = distance_matrix(graph)
    pair = next((u, v) for u in range(40) for v in range(40) if dist[u, v] == 3)
    deleted_text = ", ".join("%s_(%d,%d)" % lab for lab in deleted)
    embed = '''/-- Hoffman--Singleton labels retained after deleting ''' + deleted_text + '''. -/
def embed : Vertex → Wow284.Vertex :=
  ![''' + ", ".join(map(str, old)) + ''']

set_option maxRecDepth 10000 in
lemma embed_injective : Function.Injective embed := by
  decide

lemma embed_ne {u v : Vertex} (h : u ≠ v) : embed u ≠ embed v :=
  fun huv => h (embed_injective huv)
'''
    return Spec(40, namespace, graph, kept_labels, 8, 5, q, p, 40, 8,
                values, profile, p, q, attained, pair, five_cycle(graph),
                "Wow284.Basic", embed, "Wow284")


def render() -> dict[Path, str]:
    outputs = {}
    for ns, deleted in GRAPHS.items():
        spec = make_spec(ns, deleted)
        verify_spec(spec)
        relative = {f"lean/Wow284/{ns}/Basic.lean": basic(spec),
                    f"lean/Wow284/{ns}/SpectralBridge.lean": bridge(spec),
                    f"lean/Wow284/{ns}/Counterexample.lean": counterexample(spec)}
        relative.update(finite_outputs(spec))
        relative.update(ldl_outputs(spec))
        outputs.update({ROOT / path: text for path, text in relative.items()})
    return outputs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    outputs = render()
    if args.check:
        stale = [x.relative_to(ROOT) for x, c in outputs.items()
                 if not x.exists() or x.read_text(encoding="utf-8") != c]
        if stale:
            raise SystemExit("stale generated order-40 Lean files: " + ", ".join(map(str, stale)))
        print(f"order-40 HS-extra Lean certificates: PASS ({len(outputs)} files)")
        return
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
