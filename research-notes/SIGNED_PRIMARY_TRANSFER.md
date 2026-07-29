# Rational-primary transfer for the signed complement

**Status:** exact algebraic consequence of the optimal-slack construction.  
**Scope:** connected k-regular girth-five diameter-three graphs satisfying the
open shifted WOW window and the signed-complement hypotheses `0<r<n`.

## 1. Setup

Let

```
g_k(x)=(x+2)^2((x+1)^2-(2k-2))
```

and let

```
S=(6k+14)J-2I-g_k(A)
```

be the signed complement. On the orthogonal complement of the all-ones vector,

```
S=-2I-g_k(A).
```

The matrices A and S are rational symmetric matrices and commute.

## 2. Primary-transfer theorem

Let q be a monic irreducible polynomial in `Q[y]` of degree d. Suppose q occurs
with exponent e in the characteristic polynomial of `S` restricted to
`1^perp`. Define

```
Q_q(x)=(-1)^d q(-2-g_k(x)).
```

Assume that `Q_q` is irreducible over the rationals. Then:

1. `deg Q_q=4d`;
2. `e` is divisible by four;
3. the q-primary space of S has dimension `de`;
4. the trace of A on that space is

```
-(3/2)de.
```

## 3. Proof

Because A and S commute, the rational q-primary space W of S is invariant under
A. The relation `S=-2I-g_k(A)` gives

```
q(-2I-g_k(A))|_W=0,
```

so A is annihilated on W by the irreducible polynomial `Q_q` of degree `4d`.
Since A is symmetric, it is semisimple. Therefore W is a direct sum of copies
of the simple rational `Q[x]/(Q_q)` module. Its dimension `de` is a multiple of
`4d`, proving `4|e`.

The polynomial `g_k` is monic quartic with cubic coefficient six. If q is monic
of degree d, then the monic normalization of `q(-2-g_k(x))` has leading terms

```
x^(4d)+6d x^(4d-1)+...
```

and hence root sum `-6d`. Each simple degree-`4d` block contributes trace
`-6d`; there are `e/4` such blocks. Thus

```
tr(A|_W)=(-6d)(e/4)=-(3/2)de.
```

## 4. Special factors

The theorem is conditional on irreducibility of `Q_q`. The factors corresponding
to the signed eigenvalues `2` and `-2` must generally be treated separately:

- `S=-2` means `g_k(A)=0`; in the open interval only the root `A=-2` remains;
- `S=2` means `g_k(A)+4I=0`, whose factorization depends on k.

For every other factor, the theorem converts an exact irreducibility check into
both a multiplicity divisibility condition and a trace formula.

## 5. Applications

1. In the order-50 unsigned-complement exclusion, every non-special irreducible
   factor of a cycle characteristic polynomial has an irreducible quartic
   composition. The theorem supplies the exponent-divisibility and trace
   contributions used in the contradiction.
2. For rational signed-complement eigenvalues lambda, if

   ```
   g_k(x)+lambda+2
   ```

   is irreducible quartic, then the multiplicity of lambda on `1^perp` is
   divisible by four and the corresponding adjacency trace is `-3m/2`.
3. The result gives a systematic arithmetic filter for any future signed-root or
   line-graph classification of near-ceiling candidates.

## 6. Verification

The exact verifier

```
scripts/verify_signed_primary_transfer.py
```

checks the degree, monic normalization, root-sum coefficient, trace formula,
and the order-50 integer-eigenvalue examples. The module-theoretic divisibility
argument is proved in the text rather than delegated to computation.
