# Order-50 signed-component route: corrected status

**Status:** disconnection proved; quotient reduction still conditional.  
**Scope:** a hypothetical connected \(6\)-regular order-\(50\), girth-five,
diameter-three strict WOW candidate.

## Stable input

Put

\[
g_6(x)=(x+2)^2((x+1)^2-10)
\]

and

\[
S=50J-g_6(A)-2I.
\]

The signed-complement bridge proves

\[
S\mathbf 1=2\mathbf 1,\qquad S+2I\succeq0,
\qquad S_{uv}\in\{-1,0,1\}\quad(u\ne v).
\]

The exact moment bound gives

\[
m_{-2}(A)\le20,\qquad \operatorname{rank}(S+2I)\ge30.
\]

The polynomial needed on the \(S\)-eigenvalue-\(2\) space factors as

\[
\boxed{
g_6(x)+4=(x+4)(x^3+2x^2-5x-8).
}
\]

The three roots of the cubic lie inside the open shifted WOW window.
Consequently the cubic primary cannot be discarded.

## The remaining proof gate

The previously proposed five-case quotient reduction is not unconditional.
Theorem `thm:order50-disconnected` now proves that the underlying signed graph
of \(S\) is disconnected, using the corrected tailed-nonbacktracking trace
identity and the connected signed-root representation theorem.

The unresolved assertion is **component-space invariance**. Commutation of
\(A\) and \(S\) shows only that \(A\) preserves the full eigenspace
\(E_2(S)\). It does not by itself show that \(A\) preserves the smaller span
of the signed-component indicators. Equivalently, equitability of the
signed-component partition has not been proved. It would follow, for example,
from a proof that eigenvalue \(2\) is simple on every connected signed
component.

This implication fails in general even when \(A\) is the adjacency matrix of a
connected regular simple graph. The exact counterexample in
`scripts/verify_component_indicator_noninvariance.py` constructs matrices
\(A,S\) with
\[
AS=SA,\qquad S\mathbf1=2\mathbf1,\qquad S+2I\succeq0,
\]
whose signed components have connected support, while the signed-component
partition is not \(A\)-equitable. Thus a theorem specific to the order-\(50\)
WOW setting is genuinely required.

## Conditional quotient reduction

Assume additionally that the component-indicator space of \(S\) is
\(A\)-invariant. Let \(c\) be the number of components and let \(Q\) be the
resulting adjacency quotient. On its nonprincipal subspace,

\[
(Q+4I)(Q^3+2Q^2-5Q-8I)=0.
\]

If \(a\) is the multiplicity of \(-4\) and \(b\) is the number of rational
cubic blocks, then

\[
c=1+a+3b,\qquad
\operatorname{tr}Q=6-4a-2b.
\]

Since the diagonal entries of \(Q\) are nonnegative internal degrees,
\(2a+b\le3\). Under the disconnection assumption this leaves

\[
(a,b,c)\in
\{(1,0,2),(0,1,4),(1,1,5),(0,2,7),(0,3,10)\}.
\]

The cubic-free branch \((a,b,c)=(1,0,2)\) reduces to the old \(20+30\) or
\(25+25\) alternatives. The odd \(25+25\) branch is impossible, and the
\(20+30\) branch reaches the incidence-block contradiction. Thus, subject to
the remaining invariance gate above, a surviving quotient must contain a
cubic block.

For the cubic cases the conditional quotient data satisfy

\[
Q\ge0,\qquad Q\mathbf1=6\mathbf1,\qquad
n_iq_{ij}=n_jq_{ji},\qquad \sum_i n_i=50,
\]

\[
\chi_Q(x)
=(x-6)(x+4)^a(x^3+2x^2-5x-8)^b,
\]

\[
g_6(Q)+4I=50\,\mathbf1(n_1,\ldots,n_c),
\]

and the radius-two inequalities

\[
(Q^2)_{ij}-6\delta_{ij}
\le n_j-\delta_{ij}-q_{ij}.
\]

These constraints are a possible future enumeration target. They are not a
proof that order \(50\) is impossible, and no \(n\le49\) claim is made.
