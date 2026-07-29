# An order-50 bound on the adjacency -2 multiplicity

**Status:** exact project derivation under Proof Audit 14.  
**Scope:** every 6-regular graph of order 50 and girth at least five; the strict
WOW window is not needed until the final Gram-rank interpretation.

## 1. Statement

Let G be 6-regular, of order 50 and girth at least five, and let m be the
multiplicity of the adjacency eigenvalue -2. Then

```
m <= 20.
```

If G is additionally a strict diameter-three WOW candidate, the signed Gram
matrix

```
R = T+2I
```

from the order-50 root-type reduction has

```
ker R = E_{-2}(A),
rank R = 50-m >= 30.
```

## 2. Moment proof

Write the adjacency eigenvalues as 6 together with 49 nonprincipal
eigenvalues. Girth at least five gives

```
tr A   = 0,
tr A^2 = 50*6,
tr A^3 = 0,
tr A^4 = 50*6*(2*6-1).
```

After removing the principal eigenvalue 6 and the m copies of -2, the remaining
spectral measure has moments

```
mu_0 = 49-m,
mu_1 = -6+2m,
mu_2 = 264-4m,
mu_3 = -216+8m,
mu_4 = 2004-16m.
```

The moment matrix for the polynomials 1,x,x^2 is positive semidefinite:

```
H = [ mu_0 mu_1 mu_2
      mu_1 mu_2 mu_3
      mu_2 mu_3 mu_4 ].
```

Its determinant factors as

```
det H = 3600(1625-81m).
```

Hence `1625-81m>=0`, and integrality gives `m<=20`.

The same conclusion follows from the 2-by-2 localizing matrix for

```
10-(x+1)^2 >= 0
```

on the shifted WOW interval: its determinant is

```
144(125-6m),
```

which again gives `m<=20`.

## 3. Interpretation

At order 50, the positive semidefinite integral matrix `R=T+2I` has diagonal
two, row sum four and off-diagonal entries in `{-1,0,1}`. Its nullity is exactly
the adjacency -2 multiplicity. The theorem therefore forces every root-system
representation of a hypothetical order-50 candidate to have rank at least 30.

This does not rule out order 50 by itself. It is a global rank constraint for
any subsequent D-type or E8 root-system analysis and is independent of the
local two-path profile enumeration.

## 4. Verification

The exact verifier

```
scripts/verify_order50_minus_two_multiplicity.py
```

checks the trace identities, the two moment matrices, both determinant
factorizations, and the rank interpretation.
