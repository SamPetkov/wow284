# Refinement: the value \(r=29\) is impossible

This note strengthens the two-path table in
`ORDER50_LOCAL_FEASIBILITY.md`.  The determinant calculation there is correct,
but determinant nonnegativity alone permits an equality case that the full
positive-semidefinite operator excludes.

Let

\[
 f(x)=(x+2)^2(x^2+2x-9).
\]

For a strict degree-six WOW counterexample, all nonprincipal adjacency
eigenvalues lie in

\[
 (-1-\sqrt{10},-1+\sqrt{10}).
\]

Hence

\[
 -f(x)=(x+2)^2\bigl(10-(x+1)^2\bigr)\ge0
\]

on the nonprincipal spectrum, with equality inside the open interval only at
\(x=-2\).  The centered matrix

\[
 M=-f(A)+\frac{2496}{50}J
\]

is positive semidefinite and, on \(\mathbf1^\perp\), its kernel is precisely the
adjacency \(-2\) eigenspace.

For vertices \(u,w\) at distance two, the matrix scaled by 25 has

\[
 25M_{uu}=25M_{ww}=48,
\]

and

\[
 25M_{uw}=773-25r_{uvw}.
\]

If \(r_{uvw}=29\), then

\[
 M_{uw}=M_{uu}=M_{ww}.
\]

Thus

\[
 (e_u-e_w)^{\mathsf T}M(e_u-e_w)=0.
\]

Positive semidefiniteness gives

\[
 M(e_u-e_w)=0.
\]

Since \(e_u-e_w\perp\mathbf1\), it follows that

\[
 A(e_u-e_w)=-2(e_u-e_w).
\]

This is impossible at coordinate \(u\): because \(u,w\) are nonadjacent,

\[
 (A(e_u-e_w))_u=A_{uu}-A_{uw}=0,
\]

whereas the right side has coordinate \(-2\).

Therefore

\[
 \boxed{r_{uvw}\ne29.}
\]

Combining this with the determinant table gives the refined possibilities

\[
\begin{array}{c|c}
\text{incident edge types}&\text{allowed }r\\
\hline
\text{low--low}&30,31,32\\
\text{mixed}&30,31,32\\
\text{high--high}&30,31.
\end{array}
\]

In particular every one of the 750 two-edge paths satisfies \(r\ge30\).  Since

\[
 \sum r=10800+6m+6N_6,
\]

we obtain the sharper global inequality

\[
 \boxed{N_6\ge1950-m.}
\]

The exact integer re-enumeration still leaves the same 266 coarse
\((n_0,n_2,n_4)\) profiles.  Thus the refinement is a genuine local theorem and
a stronger search filter, but it does not by itself eliminate order 50.
