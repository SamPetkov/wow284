# Proof Audit 11: the regular diameter-four obstruction

**Audited result:** Theorem 3 and Corollary 4 of
`DIAMETER_PUNCTURE_EXTENSIONS.md`.

**Verdict:** `pass_after_proof_expansion`.

The theorem and constants are correct. The audit expands four logically
compressed points: the cross-neighborhood injection, all orientation factors in
the distance quadratic form, positivity of the minimizing eigenvector, and the
exact degree threshold. No theorem statement or numerical bound changes.

## 1. Audited theorem

Let \(G\) be a connected \(k\)-regular graph of girth at least five and diameter
four. Then

\[
\boxed{
\lambda_{\min}(D(G))
\le -\frac{7+\sqrt{16k+1}}2.
}
\]

Since regularity gives \(\delta^*(G)=k\),

\[
\boxed{
\Phi(G)\le k-\frac{7+\sqrt{16k+1}}2.
}
\]

Consequently no such graph of degree \(2\le k\le9\) is a strict
counterexample to WOW-284. The comparison does not exclude \(k=10\).

## 2. Hypothesis ledger

| Hypothesis | Exact use |
| --- | --- |
| connectedness | graph distances and diametral endpoints exist |
| \(k\)-regularity | both endpoint neighborhoods have size \(k\), and \(\delta^*=k\) |
| girth at least five | adjacent vertices have no common neighbor; arbitrary pairs have at most one common neighbor; neighbors of one vertex are pairwise nonadjacent |
| diameter four | supplies \(u,v\) at distance four and excludes edges between their neighborhoods |

The \(2\times2\) matrix below is a comparison matrix for a test subspace. It is
not called an equitable quotient.

## 3. Cross-neighborhood injection

Choose \(u,v\in V(G)\) with \(d_G(u,v)=4\), and put

\[
U=N(u),\qquad V=N(v).
\]

The sets \(U,V\) are disjoint, and no edge joins \(U\) to \(V\), since such an
edge would give a path of length three from \(u\) to \(v\).

Let

\[
r=\#\{(a,b)\in U\times V:d_G(a,b)=2\}.
\]

Fix \(a\in U\). For every \(b\in V\) at distance two from \(a\), girth at least
five gives a unique common neighbor \(w\). The vertex \(w\) lies in
\(N(a)\setminus\{u\}\). Distinct vertices \(b,b'\in V\) cannot use the same
\(w\), because then

\[
w-b-v-b'-w
\]

would be a 4-cycle. Thus \(b\mapsto w\) is injective into a set of size
\(k-1\), and hence

\[
\boxed{r\le k(k-1).}
\]

All other pairs in \(U\times V\) have distance at least three, so

\[
\begin{aligned}
S&:=\sum_{a\in U}\sum_{b\in V}d_G(a,b)\\
 &\ge 2r+3(k^2-r)\\
 &=3k^2-r\\
 &\ge 2k^2+k.
\end{aligned}
\tag{1}
\]

## 4. Exact quadratic-form accounting

For \(\alpha,\beta>0\), define \(x\in\mathbb R^{V(G)}\) by

\[
x_u=\alpha,\qquad x_a=\beta\ (a\in U),
\]

\[
x_v=-\alpha,\qquad x_b=-\beta\ (b\in V),
\]

and set all remaining coordinates to zero. Then

\[
x^{\mathsf T}x=2\alpha^2+2k\beta^2.
\]

Counting unordered pairs and multiplying by two gives:

| Pair class | Contribution to \(x^{\mathsf T}Dx\) |
| --- | ---: |
| \(\{u,v\}\) | \(-8\alpha^2\) |
| \(u\)--\(U\) and \(v\)--\(V\) | \(+4k\alpha\beta\) |
| \(u\)--\(V\) and \(v\)--\(U\) | at most \(-12k\alpha\beta\) |
| pairs inside \(U\) and inside \(V\) | \(+4k(k-1)\beta^2\) |
| \(U\)--\(V\) | at most \(-2S\beta^2\) |

The last two signs are critical: the cross-block coordinate products are
negative, so lower bounds on distances give upper bounds on the quadratic form.
Using (1),

\[
x^{\mathsf T}D(G)x
\le -8\alpha^2-8k\alpha\beta-6k\beta^2.
\]

Therefore

\[
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
\le
\frac{-4\alpha^2-4k\alpha\beta-3k\beta^2}
{\alpha^2+k\beta^2}.
\tag{2}
\]

## 5. Comparison matrix and sign of the minimizer

Set

\[
y_1=\alpha,\qquad y_2=\sqrt{k}\,\beta.
\]

The right-hand side of (2) is the Rayleigh quotient of

\[
M_k=
\begin{pmatrix}
-4&-2\sqrt{k}\\
-2\sqrt{k}&-3
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
x^2+7x+12-4k,
\]

so its least eigenvalue is

\[
\mu_k=-\frac{7+\sqrt{16k+1}}2.
\]

The vector

\[
y=
\begin{pmatrix}
2\sqrt{k}\\
-4-\mu_k
\end{pmatrix}
=
\begin{pmatrix}
2\sqrt{k}\\
(\sqrt{16k+1}-1)/2
\end{pmatrix}
\]

has two strictly positive coordinates and satisfies \(M_ky=\mu_ky\). Hence it
corresponds to admissible \(\alpha,\beta>0\). Rayleigh--Ritz applied to (2)
proves the theorem.

## 6. Exact degree threshold

For \(2\le k\le9\),

\[
\frac{7+\sqrt{16k+1}}2>k.
\]

For \(k\le3\), the right side of
\(\sqrt{16k+1}>2k-7\) is negative. For \(4\le k\le9\), both sides are
nonnegative and squaring is legitimate; the difference is

\[
16k+1-(2k-7)^2=4(-k^2+11k-12)>0.
\]

Thus \(\mu_k<-k\), and \(\Phi(G)<0\). At \(k=10\), the comparison gives
\(\mu_{10}>-10\); this only records the limitation of the method.

## 7. Independent exact verification

Run

```text
python scripts/verify_proof_audit_11_diameter_four.py
```

The script does not import the original extension verifier. It checks:

- the comparison characteristic polynomial and positive least eigenvector;
- the exact threshold for \(2\le k\le9\) and failure of the method at \(k=10\);
- every diametral pair of \(C_8\);
- every diametral pair of the affine perfect-matching deletion of the
  Hoffman--Singleton graph;
- the distance-two injection and distance-sum bound;
- the exact test-vector Rayleigh inequality;
- both complete exact distance characteristic polynomials.

No floating-point arithmetic or numerical eigensolver is used.

## 8. Claim boundary

This theorem excludes regular diameter-four strict counterexamples only through
degree nine. It does not establish existence at degree ten and does not settle
the full diameter-four regime. No literature-priority claim is made pending a
dedicated citation-chain audit.
