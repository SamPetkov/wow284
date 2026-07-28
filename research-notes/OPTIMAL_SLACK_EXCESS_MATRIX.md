# The optimal-slack excess matrix

**Status:** exact project derivation under Proof Audit 14.

Let `G` satisfy the strict diameter-three shifted-WOW condition, and retain

\[
 g_k(x)=(x+2)^2((x+1)^2-(2k-2)),
 \quad C_k=(k+2)^2(k^2+3),
 \quad h_k=6(k+2).
\]

The optimal slack is

\[
 M=-g_k(A)+\frac{C_k}{n}J\succeq0,
 \qquad M\mathbf1=0.
\]

For distinct vertices, the `2 x 2` minors and the strict kernel argument give

\[
 (g_k(A))_{uv}\ge h_k+1.
\]

Define the **optimal-slack excess matrix**

\[
 \boxed{
 E=g_k(A)-(h_k+1)J+I.
 }
\]

Then:

1. `E` is a symmetric nonnegative integral matrix;
2. `E` has zero diagonal;
3. `E` has constant row sum
   \[
    \boxed{
    \varepsilon_{k,n}=C_k-(h_k+1)n+1;
    }
   \]
4. on `mathbf1^perp`,
   \[
    \boxed{M=I-E}.
   \]

Thus every nonprincipal eigenvalue of `E` is at most one.

## Nonvanishing and the improved order bound

If `E=0`, then

\[
 g_k(A)=(h_k+1)J-I.
\]

The irreducibility argument for `g_k(x)+1` shows that this is impossible for a
simple regular graph. Consequently `E` is nonzero. Since its row sum is a
nonnegative integer independent of the row,

\[
 \varepsilon_{k,n}\ge1.
\]

This is exactly

\[
 \boxed{
 n\le\left\lfloor\frac{C_k}{h_k+1}\right\rfloor
 =\left\lfloor
 \frac{(k+2)^2(k^2+3)}{6(k+2)+1}
 \right\rfloor.
 }
\]

The difference from the exact one-variable LP ceiling is asymptotic to
`k^2/36`.

## The simple-excess level

If every off-diagonal entry of `g_k(A)` is at most `h_k+2`, then `E` is the
adjacency matrix of a simple regular graph `Y` of degree

\[
 \varepsilon_{k,n}=C_k-(h_k+1)n+1.
\]

Its nonprincipal adjacency eigenvalues are at most one. Let `X` be its
complement. Then

\[
 A(X)=J-I-E=(h_k+2)J-2I-g_k(A),
\]

\[
 d_X=(h_k+2)n-C_k-2,
\]

and

\[
 \lambda_{\min}(A(X))\ge-2.
\]

Moreover, `A`, `E`, and `A(X)` commute. In the strict shifted window,

\[
 E_{-2}(A(X))=E_{-2}(A).
\]

Hence the low-degree near-ceiling exclusions are not isolated calculations:
they are the simple-excess level of one integral matrix hierarchy.

## Higher excess levels

In general, `E` is the adjacency matrix of a regular loopless integral weighted
graph. Its row sum measures the distance from the integral order ceiling, while
its largest nonprincipal eigenvalue is at most one. Bounding or classifying
these weighted excess matrices is a natural next step beyond the one-variable
LP and the simple relation-graph case.

For order 50 at degree six, the signed-root Gram matrix in the companion note is
a centered reformulation of this same excess data. The `2 x 2`, `3 x 3`, and
seven-vertex neighbourhood constraints are successive local positivity tests
on the same object.
