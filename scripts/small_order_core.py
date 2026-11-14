#!/usr/bin/env python3
"""Shared tools for the 2026-11-14 search for strict WOW-284 counterexamples
of order below 38.

Floating-point routines here are SCREENING ONLY.  Every candidate is
re-checked by ``exact_certificate`` (integer BFS, exact rational dual
degrees, fraction-free Bareiss elimination of q*D + p*I where p/q is the
exact minimum dual degree).

Compatible with Python 3.7 (Procida) and later.
"""

from __future__ import annotations

import os
import random
from collections import deque
from fractions import Fraction
from itertools import combinations

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# graph6
# ---------------------------------------------------------------------------


def graph6_decode(text):
    """Decode a graph6 string into a 0/1 numpy adjacency matrix (uint8)."""
    s = text.strip()
    if s.startswith(">>graph6<<"):
        s = s[len(">>graph6<<"):]
    data = [ord(c) - 63 for c in s]
    if data[0] < 63:
        n = data[0]
        pos = 1
    elif data[1] < 63:
        n = (data[1] << 12) | (data[2] << 6) | data[3]
        pos = 4
    else:
        n = 0
        for x in data[2:8]:
            n = (n << 6) | x
        pos = 8
    bits = []
    for x in data[pos:]:
        for b in range(5, -1, -1):
            bits.append((x >> b) & 1)
    a = np.zeros((n, n), dtype=np.uint8)
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                a[i, j] = a[j, i] = 1
            k += 1
    return a


def graph6_encode(a):
    a = np.asarray(a)
    n = a.shape[0]
    if n < 63:
        out = [n + 63]
    elif n < 258048:
        out = [126, ((n >> 12) & 63) + 63, ((n >> 6) & 63) + 63, (n & 63) + 63]
    else:
        raise ValueError("too large")
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(1 if a[i, j] else 0)
    while len(bits) % 6:
        bits.append(0)
    for k in range(0, len(bits), 6):
        x = 0
        for b in bits[k:k + 6]:
            x = (x << 1) | b
        out.append(x + 63)
    return "".join(chr(c) for c in out)


# ---------------------------------------------------------------------------
# Parent graphs
# ---------------------------------------------------------------------------


def hs_index_p(i, j):
    return 5 * (i % 5) + (j % 5)


def hs_index_q(k, ell):
    return 25 + 5 * (k % 5) + (ell % 5)


def hs_label(v):
    if v < 25:
        return "P%d%d" % (v // 5, v % 5)
    v -= 25
    return "Q%d%d" % (v // 5, v % 5)


def hoffman_singleton():
    """The paper's coordinate Hoffman--Singleton graph (P_{i,j} -> 5i+j,
    Q_{k,l} -> 25+5k+l)."""
    a = np.zeros((50, 50), dtype=np.uint8)

    def add(u, v):
        a[u, v] = a[v, u] = 1

    for i in range(5):
        for j in range(5):
            add(hs_index_p(i, j), hs_index_p(i, j + 1))
            add(hs_index_q(i, j), hs_index_q(i, j + 2))
            for k in range(5):
                add(hs_index_p(i, j), hs_index_q(k, i * k + j))
    return a


def petersen_set():
    """The paper's deleted Petersen set {P_{0,j}, Q_{0,j}}."""
    return [hs_index_p(0, j) for j in range(5)] + [hs_index_q(0, j) for j in range(5)]


def induced(a, keep):
    keep = list(keep)
    return a[np.ix_(keep, keep)].copy()


def anstee_robertson_r():
    """R = HS - Petersen (order 40), vertex order = increasing HS index."""
    hs = hoffman_singleton()
    dele = set(petersen_set())
    keep = [v for v in range(50) if v not in dele]
    return induced(hs, keep), keep


def second_subconstituent_x42():
    """X42 = HS induced on the vertices at distance two from P_{0,0}."""
    hs = hoffman_singleton()
    v0 = hs_index_p(0, 0)
    nb = set(np.flatnonzero(hs[v0]).tolist())
    keep = [v for v in range(50) if v != v0 and v not in nb]
    return induced(hs, keep), keep


def load_graph6_file(path):
    with open(path) as fh:
        lines = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    return graph6_decode(lines[0])


def cages55():
    names = ["foster", "meringer", "robertson_wegner", "wong"]
    out = {}
    for nm in names:
        out["cage55_" + nm] = load_graph6_file(os.path.join(ROOT, "data", "cages55", nm + ".graph6"))
    return out


def jorgensen96():
    return load_graph6_file(os.path.join(ROOT, "data", "jorgensen96", "jorgensen96.graph6"))


def robertson_graph_by_search(seed=0, tries=2000):
    """Return a 4-regular girth-5 graph on 19 vertices (the (4,5)-cage, which
    is unique up to isomorphism, Robertson 1964).  Found by randomized
    construction; the caller should verify regularity and girth."""
    rng = random.Random(seed)
    n = 19
    for _ in range(tries):
        a = np.zeros((n, n), dtype=np.uint8)
        # Hamiltonian cycle (the Robertson graph is Hamiltonian).
        for i in range(n):
            a[i, (i + 1) % n] = a[(i + 1) % n, i] = 1
        ok = _complete_regular_girth5(a, 4, rng)
        if ok is not None:
            return ok
    raise RuntimeError("no (4,5)-cage found")


def _complete_regular_girth5(a, k, rng, budget=20000):
    n = a.shape[0]
    a = a.copy()
    steps = 0

    def candidates():
        deg = a.sum(1)
        need = [v for v in range(n) if deg[v] < k]
        if not need:
            return None, []
        d = all_distances(a)
        v = min(need, key=lambda x: (k - deg[x] == 0, sum(1 for w in need if d[x, w] >= 4 or d[x, w] < 0)))
        cands = [w for w in need if w != v and (d[v, w] >= 4 or d[v, w] < 0)]
        return v, cands

    def rec():
        nonlocal steps
        steps += 1
        if steps > budget:
            return False
        v, cands = candidates()
        if v is None:
            return True
        rng.shuffle(cands)
        for w in cands:
            a[v, w] = a[w, v] = 1
            if rec():
                return True
            a[v, w] = a[w, v] = 0
        return False

    if rec():
        return a
    return None


# ---------------------------------------------------------------------------
# Distances, girth, connectivity (integer, exact)
# ---------------------------------------------------------------------------


def all_distances(a):
    """Integer BFS distances; -1 for unreachable pairs."""
    n = a.shape[0]
    nbrs = [np.flatnonzero(a[v]).tolist() for v in range(n)]
    d = -np.ones((n, n), dtype=np.int64)
    for s in range(n):
        d[s, s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in nbrs[u]:
                if d[s, w] < 0:
                    d[s, w] = d[s, u] + 1
                    q.append(w)
    return d


def girth(a):
    """Exact girth by BFS from every vertex (inf -> returns 0 for forests)."""
    n = a.shape[0]
    nbrs = [np.flatnonzero(a[v]).tolist() for v in range(n)]
    best = None
    for s in range(n):
        dist = {s: 0}
        par = {s: -1}
        q = deque([s])
        while q:
            u = q.popleft()
            for w in nbrs[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    q.append(w)
                elif par[u] != w:
                    c = dist[u] + dist[w] + 1
                    if best is None or c < best:
                        best = c
    return best if best is not None else 0


def dual_degrees_exact(a):
    deg = a.sum(1).astype(int).tolist()
    n = len(deg)
    out = []
    for v in range(n):
        if deg[v] == 0:
            out.append(None)
            continue
        s = sum(deg[w] for w in np.flatnonzero(a[v]).tolist())
        out.append(Fraction(s, deg[v]))
    return out


# ---------------------------------------------------------------------------
# Floating-point screening (NOT a proof)
# ---------------------------------------------------------------------------


def batch_distances(adj):
    """adj: (B, n, n) 0/1 array.  Returns float64 distance array with
    np.inf for unreachable pairs."""
    b, n, _ = adj.shape
    af = adj.astype(np.float32)
    eye = np.broadcast_to(np.eye(n, dtype=bool), (b, n, n))
    reach = eye | (adj > 0)
    dist = np.full((b, n, n), np.inf)
    dist[eye] = 0.0
    dist[adj > 0] = 1.0
    d = 1
    while True:
        d += 1
        new = (np.matmul(reach.astype(np.float32), af) > 0.5) | reach
        fresh = new & ~reach
        if not fresh.any():
            break
        dist[fresh] = d
        reach = new
        if d > n:
            break
    return dist


def batch_phi(adj):
    """Return (phi, delta_star, lambda_min, diameter) arrays for a batch of
    graphs.  Disconnected graphs get phi = -inf."""
    adj = np.asarray(adj)
    if adj.ndim == 2:
        adj = adj[None]
    b, n, _ = adj.shape
    dist = batch_distances(adj)
    conn = np.isfinite(dist).all(axis=(1, 2))
    deg = adj.sum(2).astype(np.float64)
    nsum = np.matmul(adj.astype(np.float64), deg[:, :, None])[:, :, 0]
    with np.errstate(divide="ignore", invalid="ignore"):
        dstar = np.where(deg > 0, nsum / np.where(deg > 0, deg, 1), np.inf)
    ds = dstar.min(1)
    lam = np.full(b, -np.inf)
    diam = np.full(b, np.inf)
    if conn.any():
        dd = dist[conn]
        lam[conn] = np.linalg.eigvalsh(dd)[:, 0]
        diam[conn] = dd.max(axis=(1, 2))
    phi = np.where(conn, ds + lam, -np.inf)
    return phi, ds, lam, diam


def batch_phi_certified(adj, scale=4096):
    """Like batch_phi, plus an EXACT integer certificate of non-strictness.

    For each connected graph: delta* = p/q is located exactly (integer
    comparison s_v * q >= p * d_v for all v, where s_v is the neighbour-degree
    sum), x is the least-eigenvalue eigenvector rounded to integers after
    scaling, and Q = x^T (q D + p I) x is evaluated in exact integer (int64)
    arithmetic.  Q < 0 proves that D + delta* I is not positive
    semidefinite, i.e. Phi(G) < 0 (G is not a strict counterexample).

    Returns phi, ds, lam, diam (floats, screening only), cert (bool: Q < 0
    and the delta* check passed), Q (int64), p, q (int64)."""
    adj = np.asarray(adj)
    if adj.ndim == 2:
        adj = adj[None]
    b, n, _ = adj.shape
    dist = batch_distances(adj)
    conn = np.isfinite(dist).all(axis=(1, 2))
    deg = adj.sum(2).astype(np.int64)
    s = np.matmul(adj.astype(np.int64), deg[:, :, None])[:, :, 0]
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(deg > 0, s / np.where(deg > 0, deg, 1), np.inf)
    vstar = ratio.argmin(1)
    ar = np.arange(b)
    p = s[ar, vstar]
    q = deg[ar, vstar]
    minok = (s * q[:, None] >= p[:, None] * deg).all(1) & (q > 0)
    ds = ratio.min(1)
    lam = np.full(b, -np.inf)
    diam = np.full(b, np.inf)
    cert = np.zeros(b, dtype=bool)
    Q = np.zeros(b, dtype=np.int64)
    if conn.any():
        dd = dist[conn]
        w, v = np.linalg.eigh(dd)
        lam[conn] = w[:, 0]
        diam[conn] = dd.max(axis=(1, 2))
        x = np.rint(v[:, :, 0] * scale).astype(np.int64)
        dint = dd.astype(np.int64)
        assert (dint == dd).all()
        qc = q[conn]
        pc = p[conn]
        quad = np.einsum("bi,bij,bj->b", x, dint, x)
        Qc = qc * quad + pc * (x * x).sum(1)
        Q[conn] = Qc
        cert[conn] = (Qc < 0) & minok[conn] & (np.abs(x).sum(1) > 0)
    phi = np.where(conn, ds + lam, -np.inf)
    return phi, ds, lam, diam, cert, Q, p, q


def phi_float(a):
    phi, ds, lam, diam = batch_phi(a[None])
    return float(phi[0]), float(ds[0]), float(lam[0]), float(diam[0])


# ---------------------------------------------------------------------------
# Exact certificate
# ---------------------------------------------------------------------------


def bareiss_leading_minors(m):
    """Fraction-free Gaussian elimination without pivoting on an integer
    matrix.  Returns the list of leading principal minors det(M[:k,:k]),
    k=1..n, or stops early (returning the partial list) when a minor is
    <= 0.  For a symmetric integer matrix, all n minors > 0 iff positive
    definite (Sylvester)."""
    n = len(m)
    a = [list(map(int, row)) for row in m]
    minors = []
    prev = 1
    for k in range(n):
        piv = a[k][k]
        minors.append(piv)
        if piv <= 0:
            return minors
        for i in range(k + 1, n):
            aik = a[i][k]
            row_i = a[i]
            row_k = a[k]
            for j in range(k + 1, n):
                row_i[j] = (piv * row_i[j] - aik * row_k[j]) // prev
            row_i[k] = 0
        prev = piv
    return minors


def ldl_pivots_exact(m_frac):
    """Exact rational LDL^T pivots of a symmetric Fraction matrix (no
    pivoting).  Pivot k = minor_k / minor_{k-1}."""
    n = len(m_frac)
    a = [list(row) for row in m_frac]
    piv = []
    for k in range(n):
        p = a[k][k]
        piv.append(p)
        if p == 0:
            return piv
        for i in range(k + 1, n):
            f = a[i][k] / p
            if f:
                for j in range(k + 1, n):
                    a[i][j] -= f * a[k][j]
    return piv


def exact_certificate(a):
    """Exact strictness test.  Returns a dict with the exact data; the key
    'strict' is True iff D + delta* I is positive definite, i.e. iff
    Phi(G) > 0."""
    a = np.asarray(a, dtype=np.uint8)
    n = a.shape[0]
    assert (a == a.T).all() and not a.diagonal().any()
    d = all_distances(a)
    connected = bool((d >= 0).all())
    g = girth(a)
    deg = a.sum(1).astype(int).tolist()
    res = {
        "order": n,
        "size": int(a.sum() // 2),
        "connected": connected,
        "girth": g if g else "inf",
        "degrees": sorted(deg),
        "graph6": graph6_encode(a),
    }
    if not connected:
        res["strict"] = False
        return res
    duals = dual_degrees_exact(a)
    ds = min(duals)
    res["delta_star"] = str(ds)
    res["diameter"] = int(d.max())
    p, q = ds.numerator, ds.denominator
    mat = (q * d + p * np.eye(n, dtype=np.int64)).tolist()
    minors = bareiss_leading_minors(mat)
    res["strict"] = len(minors) == n and all(x > 0 for x in minors)
    res["minors_positive"] = sum(1 for x in minors if x > 0)
    res["qD_plus_pI"] = "%d*D + %d*I" % (q, p)
    return res


def is_girth_at_least5(a):
    g = girth(a)
    return g == 0 or g >= 5


def connected_components_ok(a):
    return bool((all_distances(a) >= 0).all())
