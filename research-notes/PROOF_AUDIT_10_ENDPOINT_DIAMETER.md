# Proof Audit 10: endpoint-neighborhood diameter obstruction

**Audited result:** Theorem 1 and Corollary 2 of
`DIAMETER_PUNCTURE_EXTENSIONS.md`.
**Verdict:** `pass_with_strengthening`.
**Main correction:** the proof does not use the girth assumption. The theorem
holds for every connected finite simple graph of diameter at least five.

## 1. Strengthened theorem

Let \(G\) be a connected finite simple graph. Choose vertices \(u,v\) at
distance

\[
 d=d_G(u,v)\ge5,
\]

and put

\[
 p=d(u),\qquad q=d(v).
\]

Then

\[
\boxed{
\lambda_{\min}(D(G))
\le
p+q-2-
\sqrt{(p-q)^2+pq(d-2)^2}.
}
\tag{1}
\]

If \(\delta\) is the minimum degree, then

\[
\boxed{
\lambda_{\min}(D(G))\le-\delta(d-4)-2.
}
\tag{2}
\]

Consequently, if \(u,v\) are diametral, so
\(d=\operatorname{diam}(G)\ge5\), and \(G\) is a strict WOW-284
counterexample with maximum degree \(\Delta\), then

\[
\boxed{
\Delta>\delta(d-4)+2,
}
\]

and

\[
\boxed{
\operatorname{diam}(G)
\le3+\left\lceil\frac{\Delta-2}{\delta}\right\rceil.
}
\]

The WOW consequence retains the conjecture's girth hypothesis, but the spectral
inequality itself does not require it. The displayed diameter corollary is
explicitly scoped to the diameter-at-least-five regime; the regular argument
below separately rules out that regime for a regular strict counterexample.

## 2. Corrections and strengthening found

The original argument is mathematically sound in its stated girth-five setting.
The audit found two hidden points and one unnecessary assumption.

1. The within-neighborhood contribution only needs
   \(d_G(r,r')\le2\), supplied by the path through the endpoint. It does not need
   equality, so triangle-freeness and the full girth assumption are unnecessary.
2. The test vector was introduced with positive coefficients \(a,b\), but the
   proof then used the least eigenvalue of a \(2\times2\) matrix without proving
   that its least eigenvector has the required sign pattern. The audit supplies
   an explicit positive least eigenvector.
3. The final ceiling formula is an integer-rounding step from a strict
   inequality; that step is now written explicitly.

No constant changes. The endpoint-degree inequality (1), which is stronger than
(2), is promoted to the theorem statement rather than left inside the proof.

## 3. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| connectedness | distances are finite and diametral endpoints exist |
| simplicity | standard graph distance and open neighborhoods; no loop terms |
| \(d\ge5\) | makes \(N(u)\) and \(N(v)\) disjoint and gives \(d-2>0\) |
| minimum degree \(\delta\) | replaces the endpoint degrees \(p,q\) by a uniform bound |
| maximum degree \(\Delta\) | uses \(\delta^*(G)\le\Delta\) for the WOW corollary |
| girth at least five | not used in the spectral theorem; needed only to place the corollary inside WOW-284's domain |

## 4. The two-neighborhood test space

The sets \(N(u)\) and \(N(v)\) are disjoint: a common vertex would give a path
of length two between \(u\) and \(v\).

For \(a,b>0\), define

\[
 x_w=
 \begin{cases}
 a,&w\in N(u),\\
 -b,&w\in N(v),\\
 0,&\text{otherwise}.
 \end{cases}
\]

Two vertices in \(N(u)\) are at distance at most two through \(u\); the same
holds in \(N(v)\). For \(r\in N(u)\), \(s\in N(v)\), the triangle inequality
gives

\[
 d_G(r,s)\ge d-2.
\]

The within-block coordinate products are positive, so an upper bound on their
distances gives an upper bound on the quadratic form. The cross products are
negative, so a lower bound on their distances also gives an upper bound. Hence

\[
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
\le
\frac{
2p(p-1)a^2+2q(q-1)b^2-2pq(d-2)ab
}{pa^2+qb^2}.
\tag{3}
\]

This sign reversal in the cross term is the critical inequality direction.

## 5. The sign of the minimizing eigenvector

Put

\[
 y_1=\sqrt p\,a,\qquad y_2=\sqrt q\,b,
\]

and

\[
 A=2(p-1),\qquad B=2(q-1),\qquad
 C=(d-2)\sqrt{pq}>0.
\]

The right side of (3) is the Rayleigh quotient of

\[
 M=\begin{pmatrix}A&-C\\-C&B\end{pmatrix}.
\]

Its least eigenvalue is

\[
 \lambda_-=
 \frac{A+B-\sqrt{(A-B)^2+4C^2}}2.
\]

Because \(C>0\),

\[
 \sqrt{(A-B)^2+4C^2}>|A-B|,
\]

so \(\lambda_-<\min(A,B)\). Therefore

\[
 y=\begin{pmatrix}C\\A-\lambda_-\end{pmatrix}
\]

has two strictly positive coordinates. The characteristic equation

\[
 (A-\lambda_-)(B-\lambda_-)=C^2
\]

shows directly that \(My=\lambda_-y\). Thus the minimizing Rayleigh vector is
admissible with \(a,b>0\), and (3) yields

\[
\lambda_{\min}(D(G))\le\lambda_-.
\]

Substituting \(A,B,C\) gives exactly (1).

## 6. Uniform minimum-degree bound

Write

\[
 p=\delta+\alpha,\qquad
 q=\delta+\beta,\qquad
 t=d-2,
\]

with \(\alpha,\beta\ge0\) and \(t\ge3\). The exact identity

\[
\begin{aligned}
&(p-q)^2+pqt^2-
\bigl(p+q+\delta(t-2)\bigr)^2\\
&\quad=(t-2)
\left[
\delta t(\alpha+\beta)+(t+2)\alpha\beta
\right]
\ge0
\end{aligned}
\]

implies

\[
\sqrt{(p-q)^2+pqt^2}
\ge p+q+\delta(t-2).
\]

All quantities on the right are nonnegative, so no unrecorded sign choice is
made before taking square roots. Inserting this into (1) gives

\[
\lambda_{\min}(D(G))
\le-2-\delta(t-2)
=-2-\delta(d-4).
\]

## 7. WOW and integer-rounding consequences

For this consequence, take \(u,v\) diametral and assume
\(d=\operatorname{diam}(G)\ge5\).

For every graph,

\[
 \delta^*(G)\le\Delta.
\]

If \(G\) is a strict counterexample, then

\[
 \Delta\ge\delta^*(G)>-\lambda_{\min}(D(G))
 \ge\delta(d-4)+2.
\]

Thus

\[
 d-4<\frac{\Delta-2}{\delta}.
\]

Since \(d-4\) is an integer,

\[
 d-4\le
 \left\lceil\frac{\Delta-2}{\delta}\right\rceil-1,
\]

which is the stated diameter bound.

If \(G\) is \(k\)-regular and \(d\ge5\), then

\[
 \Phi(G)\le k-k(d-4)-2=k(5-d)-2<0.
\]

Therefore every regular strict counterexample has diameter at most four. For
fixed \(k\), the ordinary degree-diameter bound gives

\[
 |V(G)|\le1+k\sum_{i=0}^{3}(k-1)^i
 =k^4-2k^3+2k^2+1.
\]

## 8. Independent exact verification

Run

```text
python scripts/verify_proof_audit_10_endpoint_diameter.py
```

The verifier does not import the original diameter-extension script. It checks:

- the \(2\times2\) characteristic polynomial and least root;
- the explicit positive least eigenvector;
- the endpoint-degree radical identity;
- the strict integer-rounding implication;
- the regular score and Moore-bound formulas;
- exact neighborhood-compression inequalities on a path, a cycle, and an
  irregular girth-five graph with unequal endpoint degrees;
- exact characteristic-polynomial root certificates for the rational-bound
  controls.

No floating-point arithmetic or numerical eigensolver is used.

## 9. Claim boundary

This result is a universal distance-matrix obstruction, not a classification of
WOW-284 counterexamples. It does not settle the remaining diameter-four regular
case and makes no literature-priority claim pending a dedicated search.
