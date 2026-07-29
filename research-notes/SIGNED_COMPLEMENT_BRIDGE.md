# Signed-complement bridge for the optimal excess matrix

**Status:** exact algebraic consequence of Proof Audit 14.  
**Purpose:** identify the order-50 signed-root matrix as the specialization of a
general signed graph naturally attached to every near-ceiling strict candidate.

## 1. Definition

Under the hypotheses and notation of the three-to-one excess theorem, let

```
E = g_k(A)-(6k+13)J+I,
r = 2(k+2)^2(k^2+3)-(12k+27)n.
```

Assume in addition that

```
0<r<n.
```

Define the signed complement

```
S = J-I-E
  = (6k+14)J-2I-g_k(A).
```

The two-by-two principal minors of the optimal slack matrix give

```
0<=E_uv<=2
```

for distinct vertices when r<n. Therefore S has zero diagonal and
off-diagonal entries in {-1,0,1}; it is the adjacency matrix of a signed graph.

## 2. Spectrum and regularity

The row sum of E is

```
epsilon=(n+r+2)/2.
```

Hence S has constant signed row sum

```
d = n-1-epsilon
  = (n-r-4)/2.
```

Let

```
M=-g_k(A)+(C_k/n)J
```

be the optimal slack matrix. Since

```
M=I-E+((n+r)/(2n))J,
```

one has

```
S+2I
 = M + ((n-r)/(2n))J.
```

Both summands on the right are positive semidefinite. Thus

```
lambda_min(S)>=-2.
```

Moreover S is a polynomial in A and J, so A and S commute and are
simultaneously diagonalizable. On a nonprincipal adjacency eigenvector of
eigenvalue theta,

```
S has eigenvalue -2-g_k(theta).
```

In the open shifted WOW interval, the only zero of g_k is theta=-2. Therefore

```
E_{-2}(S)=E_{-2}(A).
```

This identifies the same -2 module in the original adjacency spectrum, the
optimal slack kernel, and the signed-complement root representation.

## 3. Order 50

At k=6 and n=50, the excess parameter is r=42. The signed degree is

```
d=(50-42-4)/2=2.
```

The signed complement becomes

```
S=50J-g_6(A)-2I,
```

which is exactly the matrix previously denoted T in the order-50 signed-root
reduction. Consequently

```
S 1 = 2 1,
S+2I is positive semidefinite,
```

and every off-diagonal entry belongs to {-1,0,1} after the audited local
integer squeezes.

Thus the order-50 root-type Gram matrix is the degree-two member of a general
family of regular signed graphs with smallest eigenvalue at least -2.

## 4. Structural interpretation

The obstruction hierarchy can now be expressed as follows.

1. The optimal slack matrix M controls the spectral and local inequalities.
2. Its integral excess E records the discrete failure of the one-level LP
   equality pattern.
3. The signed complement S packages entries 0,1,2 of E as positive, absent,
   and negative signed edges.
4. The identity S+2I>=0 places near-ceiling candidates inside the classical
   root-system theory of signed graphs with smallest eigenvalue at least -2.
5. At order 50, this is precisely the integral norm-two Gram system already
   obtained from the local cycle constraints.

The signed-graph classification is not required for the algebraic statement
above. Any later use of a D-type or E8 root representation must cite and audit
the corresponding external classification theorem separately.

## 5. Verification

The exact verifier

```
scripts/verify_signed_complement_bridge.py
```

checks all matrix identities, eigenvalue maps, row sums, the order-50
specialization, and the relation between the three -2 eigenspaces.
