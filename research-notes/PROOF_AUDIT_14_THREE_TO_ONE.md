# Proof Audit 14A: three-to-one integral excess bound

**Audited result:** `THREE_TO_ONE_EXCESS_BOUND.md`  
**Audit mode:** independent theorem-by-theorem replay; no import from the first
three-to-one verifier.  
**Verdict:** `pass`, subject to the external least-eigenvalue-minus-two
classification stated below.

## 1. Normalized theorem

Let G be connected, k-regular, of girth at least five and diameter three, with
k at least 6. Assume that every nonprincipal adjacency eigenvalue lies in

```
(-1-sqrt(2k-2), -1+sqrt(2k-2)).
```

Set

```
g_k(x) = (x+2)^2((x+1)^2-(2k-2)),
C_k    = (k+2)^2(k^2+3),
E      = g_k(A)-(6k+13)J+I,
r      = 2C_k-(12k+27)n.
```

Then

```
r>0,
n<=3r,
```

and therefore

```
n <= floor(3(k+2)^2(k^2+3)/(18k+41)).
```

## 2. Hypothesis ledger

| Hypothesis | Use |
|---|---|
| k-regular | principal adjacency eigenspace; constant row sums |
| girth at least five | nonbacktracking expansion and integral entry formulas |
| diameter three | shifted adjacency-window equivalence for WOW-284 |
| open shifted window | positive semidefiniteness and the exact kernel |
| k at least 6 | radius-two lower bound n>=k^2+2 and exclusion of low irreducibility exceptions |
| connected | simplicity of the principal adjacency eigenspace and graph distance |

## 3. Matrix normalization

The optimal slack matrix is

```
M=-g_k(A)+(C_k/n)J.
```

On the principal adjacency eigenspace its eigenvalue is zero. On a
nonprincipal adjacency eigenvector of eigenvalue theta, its eigenvalue is

```
(2k-2-(theta+1)^2)(theta+2)^2,
```

so M is positive semidefinite. The nonbacktracking expansion shows that E is
integral and the two-by-two principal minors show that its off-diagonal entries
are nonnegative. Its row sum is

```
epsilon=C_k-(6k+13)n+1.
```

Since

```
M=I-E+((epsilon-1)/n)J,
```

putting `r=2epsilon-n-2` gives

```
M=I-E+((1+r/n)/2)J.
```

No sign reversal occurs here.

## 4. Audit of r>0

The r<=0 argument is logically independent of the later n<=3r argument.
For r<=0, the two-by-two minors make E simple, including the r=0 boundary
case after the kernel-coordinate check. Hence X=complement(E) is regular with
least eigenvalue at least -2 and has at most two components.

The only external theorem used is:

> A connected regular graph with least eigenvalue at least -2 is a line graph,
> a cocktail-party graph, or an exceptional graph represented in E8; every
> regular exceptional graph has order at most 28.

Since n>=k^2+2>=38, the exceptional case is unavailable.

The connected cocktail and semiregular line-root reductions leave degrees
44 and 158. The two-component reduction leaves degree 62. In all three cases,
the relevant rational subspace is annihilated by `g_k(x)+2` and has dimension

```
7406, 332373, 10219,
```

respectively.

A uniform Gauss-lemma calculation shows that `g_k(x)+2` is irreducible over the
rationals for every integer k>=6 except k=7. The three exceptional degrees are
therefore covered simultaneously, and none of the displayed dimensions is
divisible by four. This proves r>0 without degree-specific modular
irreducibility certificates.

## 5. Audit of the doubled-edge compression

Assume n>3r and put x=r/n. Then 0<x<1/3. If E_uv=2 and
`s_w=E_uw+E_vw`, Cauchy-Schwarz for `e_u+e_v` and `e_w` gives

```
(1+x-s_w)^2 <= x(3+x).
```

The only integral possibilities are 1 and 2. The row sums show that exactly r
vertices have value 2. If W is this set and y is its coordinate sum, then the
Gram determinant of `e_u+e_v` and y equals

```
2xr+r^2(3x-1)-4x e_W,
```

where e_W is the total E-weight inside W. Since e_W is nonnegative,

```
n<=3r+2.
```

Thus n=3r+1 or n=3r+2. The fixed linear remainders leave no admissible case:
the sole integral candidate is `(k,n,r)=(77,77831,25943)`, and the handshake
product is odd. Therefore E is simple.

This is the main proof compression. It replaces the former separate
three-vertex type split and four-vertex determinant table.

## 6. Audit of the complement classification

For X=complement(E),

```
d_X=(n-r-4)/2,
lambda_min(X)>=-2.
```

Three or more components would imply n<=3r+6. The six possible offsets are
eliminated by exact linear remainders, so X has at most two components.

### Connected X

The cocktail-party case contradicts r>0. If X=L(Y):

- a regular root has order below 12 and gives exactly four arithmetic
  possibilities, all excluded by the exact r formula;
- a bipartite semiregular root has smaller part size below 6. The cases b=2,4,5
  collapse immediately; b=3 gives two linear families whose fixed prime
  remainders have the wrong residue modulo 18.

### Two components

The interval is empty for k=6,7,8. For k>=9, both components have order above
28. Regular line roots are too small. A semiregular root with smaller part at
least 3 has part-size product at most 18, below the component order. A smaller
part of size 2 gives `L(K_{d,2})`.

The only component-size combinations reduce to

```
n=3r+8,
n=3r+10,
n=2r+8.
```

Their fixed remainders leave no admissible graph; the only necessary candidate
has odd handshake product. Hence the two-component case is impossible.

## 7. Citation audit

The external classification is supported by Cvetkovic, Rowlinson and Simic,
*Spectral Generalizations of Line Graphs*, Chapter 4, especially Theorem 4.1.1
and the classification of regular exceptional graphs. A recent primary paper
states the exact convenient corollary: a connected regular graph with smallest
eigenvalue at least -2 is either represented in E8 with order at most 28, a
cocktail-party graph, or a line graph.

No novelty or priority claim is inferred from this citation. The
least-eigenvalue classification is used as an input; the integral excess
matrix, doubled-edge compression, fixed-remainder reductions and order bound
are project-derived.

## 8. Independent executable audit

The independent verifier

```
scripts/verify_proof_audit_14_three_to_one.py
```

recomputes all symbolic identities, factorization exceptions, Gram formulas,
finite arithmetic lists, component offsets, and order tables without importing
`scripts/verify_three_to_one_excess_bound.py`.
