#!/usr/bin/env python3
"""Direct exact check of the order-43 equality case (Proposition B.8).

E43 = HS - {P_(0,0), P_(0,2), P_(1,0), P_(1,2), P_(2,1), P_(4,1), Q_(1,4)},
with HS the paper's coordinate Hoffman--Singleton graph.  Pure Python,
fractions only; it does not use small_order_core.

The script checks, for E43 and for the stored orbit representative
data/hs_induced_classification/order43_equality.graph6:

  * the deleted set is independent in HS (E43 only);
  * order 43, 126 edges, degree counts 5^21 6^7 7^15, connected, girth five,
    diameter three, and delta* = 6 exactly;
  * M = D + 6I is positive semidefinite of rank 41, by an explicit
    certificate: a set P of 41 indices whose principal submatrix M[P,P] has
    an exact rational LDL^T factorization with all pivots positive
    (so M[P,P] is positive definite), and, for each of the two remaining
    indices r, a rational vector x_r = e_r - y with y supported on P and
    M x_r = 0 checked entry by entry.  Then M is congruent to
    M[P,P] (+) 0, hence positive semidefinite of rank exactly 41.

Consequently lambda_min(D) = -6 with multiplicity 2 and
Phi = delta* + lambda_min(D) = 0.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recertify_order40 import bfs_all, check_reconstruction, girth, hs, induced, ldl  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DELETED = [("P", 0, 0), ("P", 0, 2), ("P", 1, 0), ("P", 1, 2), ("P", 2, 1), ("P", 4, 1), ("Q", 1, 4)]
GRAPH6 = os.path.join(ROOT, "data", "hs_induced_classification", "order43_equality.graph6")


def graph6_decode(text):
    data = [ord(c) - 63 for c in text.strip()]
    n = data[0]
    assert 0 <= n < 63
    bits = []
    for byte in data[1:]:
        bits.extend((byte >> s) & 1 for s in range(5, -1, -1))
    g = [set() for _ in range(n)]
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                g[i].add(j)
                g[j].add(i)
            k += 1
    return g


def pivot_set(m):
    """Greedy symmetric elimination with diagonal pivoting.  Returns the
    pivot indices in order; used only to choose P, which is then certified
    independently below."""
    a = [row[:] for row in m]
    active = list(range(len(m)))
    order = []
    while active:
        k = max(active, key=lambda i: a[i][i])
        p = a[k][k]
        if p <= 0:
            break
        order.append(k)
        active.remove(k)
        for i in active:
            f = a[i][k] / p
            if f:
                for j in active:
                    a[i][j] -= f * a[k][j]
    return order


def solve(mat, rhs):
    """Exact Gauss-Jordan solve of a nonsingular rational system."""
    n = len(mat)
    a = [mat[i][:] + [rhs[i]] for i in range(n)]
    for c in range(n):
        r = next(i for i in range(c, n) if a[i][c] != 0)
        a[c], a[r] = a[r], a[c]
        inv = 1 / a[c][c]
        a[c] = [v * inv for v in a[c]]
        for i in range(n):
            if i != c and a[i][c] != 0:
                f = a[i][c]
                a[i] = [vi - f * vc for vi, vc in zip(a[i], a[c])]
    return [a[i][n] for i in range(n)]


def certify(name, g):
    n = len(g)
    dist = bfs_all(g)
    connected = all(x >= 0 for row in dist for x in row)
    deg = [len(nb) for nb in g]
    duals = [Fraction(sum(deg[w] for w in g[v]), deg[v]) for v in range(n)]
    dstar = min(duals)
    m = [[Fraction(dist[i][j] + (6 if i == j else 0)) for j in range(n)] for i in range(n)]

    pivots = pivot_set(m)
    rest = [i for i in range(n) if i not in pivots]
    sub = [[m[i][j] for j in pivots] for i in pivots]
    L, piv, nonsingular = ldl(sub)
    sub_pd = nonsingular and all(p > 0 for p in piv) and check_reconstruction(L, piv, sub)
    kernel_ok = True
    for r in rest:
        y = solve(sub, [m[i][r] for i in pivots])
        x = [Fraction(0)] * n
        x[r] = Fraction(1)
        for i, yi in zip(pivots, y):
            x[i] = -yi
        kernel_ok &= all(sum(m[i][j] * x[j] for j in range(n)) == 0 for i in range(n))

    rec = {
        "graph": name, "order": n, "edges": sum(deg) // 2, "connected": connected,
        "girth": girth(g), "diameter": max(max(row) for row in dist),
        "degree_counts": {str(d): deg.count(d) for d in sorted(set(deg))},
        "delta_star": str(dstar),
        "positive_definite_block_size": len(pivots), "kernel_vectors": len(rest),
        "block_ldl_all_pivots_positive": sub_pd, "kernel_vectors_verified": kernel_ok,
    }
    rec["psd_rank_41"] = bool(sub_pd and kernel_ok and len(pivots) == 41 and len(rest) == 2)
    rec["phi_zero"] = bool(rec["psd_rank_41"] and dstar == 6)
    print(json.dumps(rec), flush=True)
    assert connected and rec["order"] == 43 and rec["edges"] == 126
    assert rec["degree_counts"] == {"5": 21, "6": 7, "7": 15}
    assert rec["girth"] == 5 and rec["diameter"] == 3 and dstar == 6
    assert rec["phi_zero"], rec
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--output", help="optional JSON output path")
    args = ap.parse_args()

    labels, adj = hs()
    index = {lab: v for v, lab in enumerate(labels)}
    deleted = [index[lab] for lab in DELETED]
    assert all(b not in adj[a] for a in deleted for b in deleted), "deleted set is not independent"
    g, _ = induced(labels, adj, set(DELETED))
    out = [certify("E43 = HS - {P00, P02, P10, P12, P21, P41, Q14}", g)]
    with open(GRAPH6, encoding="ascii") as fh:
        out.append(certify("data/hs_induced_classification/order43_equality.graph6",
                           graph6_decode(fh.readline())))
    if args.output:
        with open(args.output, "w", newline="\n") as fh:
            json.dump(out, fh, indent=1)
            fh.write("\n")
    print("ORDER43_EQUALITY=PASS")


if __name__ == "__main__":
    main()
