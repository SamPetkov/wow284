#!/usr/bin/env python3
"""Second, independent exact certification of the three new order-40 strict
WOW-284 counterexamples inside the Hoffman--Singleton graph.

Self-contained on purpose: it does not import small_order_core (whose
Bareiss routine produced the first certificate).  Pure Python 3.7+,
fractions only.

For each graph G = HS - S (paper coordinates P_{i,j}, Q_{k,l}):
  * HS is rebuilt from the paper's edge rules and checked: 50 vertices,
    7-regular, 175 edges;
  * integer BFS distances; connectivity; diameter;
  * girth by BFS from every vertex;
  * degrees, exact dual degrees d*(v) = s(v)/d(v) as Fractions, delta*;
  * exact rational LDL^T of M = D + delta* I without pivoting: every pivot
    is printed and must be > 0, and L * diag(pivots) * L^T == M is checked
    entry by entry.  All pivots positive <=> M positive definite (Sylvester)
    <=> lambda_min(D) > -delta* <=> Phi(G) > 0.
"""

from __future__ import annotations

import json
import sys
from collections import deque
from fractions import Fraction


def hs():
    labels = [("P", i, j) for i in range(5) for j in range(5)] + \
             [("Q", k, l) for k in range(5) for l in range(5)]
    index = {lab: n for n, lab in enumerate(labels)}
    adj = [set() for _ in labels]

    def add(a, b):
        u, v = index[a], index[b]
        assert u != v
        adj[u].add(v)
        adj[v].add(u)

    for i in range(5):
        for j in range(5):
            add(("P", i, j), ("P", i, (j + 1) % 5))
            add(("Q", i, j), ("Q", i, (j + 2) % 5))
            for k in range(5):
                add(("P", i, j), ("Q", k, (i * k + j) % 5))
    assert len(adj) == 50 and all(len(a) == 7 for a in adj)
    assert sum(len(a) for a in adj) == 2 * 175
    return labels, adj


def induced(labels, adj, deleted):
    keep = [n for n, lab in enumerate(labels) if lab not in deleted]
    pos = {old: new for new, old in enumerate(keep)}
    g = [set(pos[w] for w in adj[v] if w in pos) for v in keep]
    return g, [labels[v] for v in keep]


def bfs_all(g):
    n = len(g)
    dist = []
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in g[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1
                    q.append(w)
        dist.append(d)
    return dist


def girth(g):
    best = None
    for s in range(len(g)):
        dist = {s: 0}
        parent = {s: -1}
        q = deque([s])
        while q:
            u = q.popleft()
            for w in g[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    parent[w] = u
                    q.append(w)
                elif parent[u] != w:
                    c = dist[u] + dist[w] + 1
                    best = c if best is None else min(best, c)
    return best


def ldl(m):
    n = len(m)
    L = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    piv = [Fraction(0)] * n
    for j in range(n):
        s = m[j][j] - sum(L[j][k] * L[j][k] * piv[k] for k in range(j))
        piv[j] = s
        if s == 0:
            return L, piv, False
        for i in range(j + 1, n):
            t = m[i][j] - sum(L[i][k] * L[j][k] * piv[k] for k in range(j))
            L[i][j] = t / s
    return L, piv, True


def check_reconstruction(L, piv, m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1):
            v = sum(L[i][k] * piv[k] * L[j][k] for k in range(j + 1))
            if v != m[i][j]:
                return False
    return True


GRAPHS = {
    "X40 = X42 - edge = HS - {P_(0,*), Q_(*,0)}":
        [("P", 0, j) for j in range(5)] + [("Q", k, 0) for k in range(5)],
    "HS - {P_(0,*), P_(1,0), Q_(0,0), Q_(0,2), Q_(2,2), Q_(4,4)}":
        [("P", 0, j) for j in range(5)] + [("P", 1, 0), ("Q", 0, 0), ("Q", 0, 2), ("Q", 2, 2), ("Q", 4, 4)],
    "HS - {P_(0,*), P_(1,0), Q_(0,0), Q_(0,2), Q_(1,1), Q_(1,4)}":
        [("P", 0, j) for j in range(5)] + [("P", 1, 0), ("Q", 0, 0), ("Q", 0, 2), ("Q", 1, 1), ("Q", 1, 4)],
}


def main():
    labels, adj = hs()
    out = []
    for name, deleted in GRAPHS.items():
        g, kept = induced(labels, adj, set(deleted))
        n = len(g)
        dist = bfs_all(g)
        connected = all(x >= 0 for row in dist for x in row)
        diam = max(max(row) for row in dist)
        deg = [len(a) for a in g]
        duals = [Fraction(sum(deg[w] for w in g[v]), deg[v]) for v in range(n)]
        dstar = min(duals)
        m = [[Fraction(dist[i][j]) + (dstar if i == j else 0) for j in range(n)] for i in range(n)]
        L, piv, nonsingular = ldl(m)
        positive = nonsingular and all(p > 0 for p in piv)
        recon = nonsingular and check_reconstruction(L, piv, m)
        rec = {
            "graph": name, "order": n, "edges": sum(deg) // 2, "connected": connected,
            "diameter": diam, "girth": girth(g),
            "degree_counts": {str(d): deg.count(d) for d in sorted(set(deg))},
            "delta_star": str(dstar),
            "delta_star_attained_at": [kept[v] for v in range(n) if duals[v] == dstar][:3],
            "ldl_all_pivots_positive": positive, "ldl_reconstruction_exact": recon,
            "min_pivot": str(min(piv)), "pivots": [str(p) for p in piv],
            "strict": bool(connected and positive and recon),
        }
        out.append(rec)
        print("%s: n=%d edges=%d connected=%s diameter=%d girth=%s degrees=%s delta*=%s "
              "LDL pivots all > 0: %s, L D L^T == D + delta* I: %s, min pivot = %s -> strict: %s" % (
                  name, n, rec["edges"], connected, diam, rec["girth"], rec["degree_counts"], dstar,
                  positive, recon, float(min(piv)), rec["strict"]), flush=True)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as fh:
            json.dump(out, fh, indent=1)
    assert all(r["strict"] for r in out)
    print("RECERTIFY_ORDER40=PASS")


if __name__ == "__main__":
    main()
