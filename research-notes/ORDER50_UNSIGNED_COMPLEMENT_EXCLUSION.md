# The order-50 signed complement is genuinely signed

**Status:** exact finite algebraic derivation under Proof Audit 14.  
**Scope:** a hypothetical 6-regular order-50 strict diameter-three WOW
counterexample.

## 1. Statement

Let

```
S=50J-g_6(A)-2I,
g_6(x)=(x+2)^2((x+1)^2-10).
```

The signed-complement bridge gives

```
S 1=2 1,
S+2I is positive semidefinite,
S_uv is in {-1,0,1} for u!=v.
```

Then S has at least one negative off-diagonal entry. Equivalently, the canonical
order-50 signed complement is not an ordinary unsigned graph.

## 2. Reduction to cycles

If every off-diagonal entry of S were nonnegative, S would be the adjacency
matrix of a simple 2-regular graph on 50 vertices. Hence

```
S = A(C_{l_1}) direct-sum ... direct-sum A(C_{l_c}),
```

where every `l_i>=3` and the lengths sum to 50.

The matrices A and S commute. On the rational primary space belonging to an
irreducible factor q of the characteristic polynomial of S, the relation

```
S=-2I-g_6(A)
```

shows that A is annihilated by

```
Q_q(x)=q(-2-g_6(x)).
```

## 3. Nonprincipal cycle factors

For every cycle length `3<=l<=50`, the exact cycle polynomial

```
chi_l(x)=2 T_l(x/2)-2
```

has a non-special irreducible factor q_l that does not occur for any shorter
cycle. It occurs in `chi_l` with exponent two. Here non-special means
`q_l` is neither `x-2` nor `x+2`.

For every irreducible non-special factor occurring in a cycle of length at most
50, the composed polynomial

```
q(-2-g_6(x))
```

is irreducible over the rationals and has degree `4 deg q`.

Consequently, if q occurs in the characteristic polynomial of S with exponent
e, then the corresponding rational invariant space has dimension `(deg q)e`
and is a module over a degree-`4 deg q` field. Therefore

```
e is divisible by 4.
```

Let L be the largest cycle length present. Since q_L first appears at length L,
its total exponent is twice the number of L-cycles. That number is therefore
even. Removing all L-cycles and descending inductively shows that every cycle
length occurs an even number of times. Hence the total number c of cycles is
even.

## 4. The eigenvalue-two contradiction

The eigenvalue 2 of S has multiplicity c. One copy is the global all-ones line,
on which A has eigenvalue 6. The remaining rational space has dimension c-1,
is orthogonal to the all-ones vector, and satisfies

```
g_6(A)+4I=0.
```

But

```
g_6(x)+4=(x^2+4x+2)(x^2+2x-4),
```

where both quadratic factors are irreducible over the rationals. Thus `c-1`
must be even, so c is odd.

This contradicts the conclusion that c is even. Therefore S must contain a
negative edge.

## 5. Interpretation

The simplest norm-two Gram configuration—an unsigned union of cycle root
systems—is impossible once compatibility with the original adjacency matrix is
imposed. Any order-50 candidate must use genuinely signed root data.

This result does not rule out order 50. It removes the entire switching-trivial
unsigned branch from a future signed-root classification.

## 6. Verification

The exact verifier

```
scripts/verify_order50_unsigned_complement_exclusion.py
```

checks all cycle characteristic polynomials from lengths 3 through 50, their
irreducible factors and exponents, every composed irreducibility claim, the
first-appearance property used in the descending induction, and the quadratic
factorization on the residual eigenvalue-two space. No floating-point
factorization is used.
