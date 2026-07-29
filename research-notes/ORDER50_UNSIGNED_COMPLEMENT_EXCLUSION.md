# The order-50 signed complement is genuinely signed

**Status:** exact finite algebraic derivation under Proof Audit 14.  
**Scope:** a hypothetical 6-regular order-50 strict diameter-three WOW
counterexample.  
**Correction:** an earlier provisional proof used an incorrect factorization of
`g_6(x)+4`.  That proof was deleted.  The theorem below uses the correct
factorization and a rational-primary trace argument.

## 1. Statement

Let

```
g_6(x)=(x+2)^2((x+1)^2-10)
```

and let

```
S=50J-g_6(A)-2I
```

be the signed complement attached to a hypothetical order-50 candidate.  The
signed-complement bridge gives

```
S 1 = 2 1,
S+2I is positive semidefinite,
S_uv is in {-1,0,1} for u!=v.
```

Then S has at least one negative off-diagonal entry.  Equivalently, S is not the
adjacency matrix of an ordinary unsigned graph.

## 2. Reduction to a union of cycles

If every off-diagonal entry of S were nonnegative, then S would be the adjacency
matrix of a simple 2-regular graph on 50 vertices.  Thus

```
S=A(C_{l_1}) direct-sum ... direct-sum A(C_{l_c}),
```

where every `l_i>=3`, the lengths sum to 50, and `c` is the number of cycle
components.

The matrices A and S commute.  On the orthogonal complement of the global
all-ones vector,

```
S=-2I-g_6(A).
```

We compare the rational primary decompositions of these two commuting symmetric
matrices.

## 3. Non-special cycle factors

For `3<=l<=50`, the characteristic polynomial of the cycle is

```
chi_l(x)=2T_l(x/2)-2.
```

Let q be an irreducible factor occurring in one of these cycle polynomials,
with q different from `x-2` and `x+2`, and let `d=deg q`.  Exact rational
factorization verifies that

```
q(-2-g_6(x))
```

is irreducible over the rationals and has degree `4d` for every such q.

Suppose q occurs with total exponent e in the characteristic polynomial of S.
Its q-primary space has dimension `de` and is invariant under A.  Since A is
annihilated there by the irreducible polynomial `q(-2-g_6(x))`, the dimension is
a multiple of `4d`.  Hence

```
e is divisible by 4.
```

After normalizing `q(-2-g_6(x))` to be monic, the sum of its roots is `-6d`.
Therefore each degree-`4d` A-primary block has trace `-6d`, and the whole
q-primary space contributes

```
-(3/2)de
```

to `tr A`.

Consequently, if `m` is the multiplicity of the S-eigenvalue `-2`, then all
S-primary spaces except the eigenvalues `2` and `-2` have total dimension

```
50-c-m
```

and contribute

```
-(3/2)(50-c-m)
```

to the adjacency trace.

## 4. The special eigenvalues

In the open shifted WOW window, `S=-2` implies `g_6(A)=0`, and the endpoint
zeros of `g_6` are unavailable.  Hence A acts as `-2` on this entire m-dimensional
space, contributing `-2m` to the trace.

The S-eigenvalue `2` has multiplicity c, one copy for each cycle component.
One dimension is the global all-ones line, on which A has eigenvalue 6.  On the
remaining `(c-1)`-dimensional rational space,

```
g_6(A)+4I=0.
```

The correct factorization is

```
g_6(x)+4=(x+4)(x^3+2x^2-8x-4),
```

and the cubic is irreducible over the rationals.  Write

```
a = multiplicity of the linear factor,
b = number of cubic primary blocks.
```

Then

```
a+3b=c-1,
```

and this residual S-eigenvalue-2 space contributes

```
-4a-2b
```

to `tr A`, because the cubic roots sum to `-2`.

## 5. Trace contradiction

Adding the principal line, the `-2` space, the residual `2` space and all
non-special primary spaces gives

```
0=tr A
 =6-2m-4a-2b-(3/2)(50-c-m).
```

Equivalently,

```
3c=138+m+8a+4b.
```

Using `c=a+3b+1` yields

```
m=5(b-a-27).
```

Since `m>=0`, one has `b>=a+27`, and therefore

```
c=a+3b+1 >= 4a+82 > 50,
```

contradicting the fact that a graph on 50 vertices has at most 50 cycle
components.  Thus S must have a negative edge.

## 6. Interpretation

The simplest norm-two Gram configuration—an ordinary disjoint union of cycle
root systems—is incompatible with the original adjacency trace.  Any order-50
candidate must therefore use genuinely signed root data.

This theorem does not rule out order 50.  It removes the switching-trivial
unsigned branch from a future signed-root analysis.

## 7. Verification

The exact verifier

```
scripts/verify_order50_unsigned_complement_exclusion.py
```

checks:

1. all cycle characteristic polynomials from lengths 3 through 50;
2. every irreducible cycle factor and every composed irreducibility claim;
3. the degree and root-sum formula for each composed polynomial;
4. the correct factorization of `g_6(x)+4` and irreducibility of its cubic;
5. the complete trace identity and final dimension contradiction.

No floating-point factorization is used.
