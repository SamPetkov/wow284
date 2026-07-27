# Proof Audit 11: the regular diameter-four obstruction

**Audited result:** Theorem 3 and Corollary 4 of
`DIAMETER_PUNCTURE_EXTENSIONS.md`.  
**Verdict:** `pass_after_proof_expansion`.  
**Standard terminology:** the \(2\times2\) matrix below is a comparison matrix
for a two-dimensional test subspace. It is not described as an equitable
quotient.

## 1. Theorem

Let \(G\) be a connected \(k\)-regular graph of girth at least five and diameter
four. Then

\[
\boxed{
\lambda_{\min}(D(G))
\le -\frac{7+\sqrt{16k+1}}2.
}
\]

Since \(\delta^*(G)=k\),

\[
\boxed{
\Phi(G)\le k-\frac{7+\sqrt{16k+1}}2.
}
\]

In particular, no such graph of degree \(2\le k\le9\) is a strict
counterexample to WOW-284.

Together with the audited diameter-at-least-five obstruction, every regular
strict counterexample has diameter two, three, or four; the diameter-four case
requires \(k\ge10\).

## 2. What required expansion

The numerical bound is correct. The original proof compressed four points.

1. For \(a\in N(u)\), a distance-two partner \(b\in N(v)\) has a unique common
   neighbor with \(a\), and that common neighbor lies in \(N(a)\setminus\{u\}\).
2. Two different \(b,b'\in N(v)\) cannot use the same common neighbor, because
   this would create a 4-cycle.
3. The quadratic-form numerator combines six classes of unordered pairs. The
   orientation factor two is written out below.
4. The test vector assumes positive parameters. The least eigenvector of the
   comparison matrix must therefore be shown to have positive coordinates.

No hypothesis, constant, strictness, or degree threshold changes.

## 3. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| connectedness | graph distances and diameter are defined |
| \(k\)-regularity | \(|N(u)|=|N(v)|=k\), counts the available common neighbors, and gives \(\delta^*=k\) |
| girth at least five | adjacent vertices have no common neighbor; arbitrary vertices have at most one common neighbor; neighbors of one vertex are pairwise nonadjacent |
| diameter four | supplies endpoints \(u,v\) at distance four and excludes edges between \(N(u)\) and \(N(v)\) |
| \(k\ge2\) | automatic for a connected regular graph of diameter four |

## 4. Cross-neighborhood incidence bound

Choose \(u,v\in V(G)\) with

\[
 d_G(u,v)=4,
\]

and put

\[
 U=N(u),
 \qquad
 V=N(v).
\]

The sets \(U\) and \(V\) are disjoint. An edge between \(a\in U\) and \(b\in V\)
would give the length-three path \(u-a-b-v\), so every pair in \(U\times V\)
has distance at least two.

Let

\[
 r=|\{(a,b)\in U\times V:d_G(a,b)=2\}|.
\]

Fix \(a\in U\). If \(d_G(a,b)=2\), then \(a,b\) have a common neighbor \(w\).
Girth at least five makes \(w\) unique. Moreover \(w\ne u\), since
\(u-b-v\) would be a path of length two from \(u\) to \(v\); similarly
\(w\ne v\).

If two distinct vertices \(b,b'\in V\) used the same \(w\), then

\[
 w-b-v-b'-w
\]

would be a 4-cycle. Hence, for fixed \(a\), the map \(b\mapsto w\) is injective
into \(N(a)\setminus\{u\}\), a set of size \(k-1\). Therefore

\[
 r\le k(k-1).
\]

Every pair not counted by \(r\) has distance at least three. It follows that

\[
\begin{aligned}
S
&:=\sum_{a\in U}\sum_{b\in V}d_G(a,b)\\
&\ge2r+3(k^2-r)\\
&=3k^2-r\\
&\ge2k^2+k.
\end{aligned}
\tag{1}
\]

## 5. Exact quadratic-form accounting

For \(\alpha,eta>0\), define \(x\in\mathbb R^{V(G)}\) by

\[
 x_u=\alpha,
 \qquad
 x_a=\beta\quad(a\in U),
\]

\[
 x_v=-\alpha,
 \qquad
 x_b=-\beta\quad(b\in V),
\]

and set all remaining coordinates to zero.

The norm is

\[
 x^{\mathsf T}x=2\alpha^2+2k\beta^2.
\]

The six contributions to \(x^{\mathsf T}Dx\), counted over unordered pairs and
then multiplied by two, are as follows.

| Pair class | Contribution |
| --- | ---: |
| \(\{u,v\}\) | \(-8\alpha^2\) |
| \(u\)--\(U\) and \(v\)--\(V\) | \(+4k\alpha\beta\) |
| \(u\)--\(V\) and \(v\)--\(U\) | at most \(-12k\alpha\beta\) |
| pairs inside \(U\) | \(+2k(k-1)\beta^2\) |
| pairs inside \(V\) | \(+2k(k-1)\beta^2\) |
| \(U\)--\(V\) | at most \(-2S\beta^2\) |

For example, \(d_G(u,b)\ge3\) for \(b\in V\), and the coordinate product is
negative, so that contribution is at most \(-6k\alpha\beta\). Neighbors of one
center have distance exactly two: the center gives a length-two path and an
edge between them would create a triangle.

Using (1),

\[
 x^{\mathsf T}D(G)x
\le
-8\alpha^2-8k\alpha\beta-6k\beta^2.
\]

Dividing numerator and denominator by two gives

\[
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
\le
\frac{-4\alpha^2-4k\alpha\beta-3k\beta^2}
{\alpha^2+k\beta^2}.
\tag{2}
\]

## 6. Comparison matrix and sign of its minimizer

Set

\[
 y_1=\alpha,
 \qquad
 y_2=\sqrt{k}\,\beta.
\]

The right side of (2) is the Rayleigh quotient of

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

and its least eigenvalue is

\[
 \mu_k=-\frac{7+\sqrt{16k+1}}2.
\]

Since the off-diagonal entry is strictly negative,

\[
 \mu_k<-4.
\]

Thus

\[
 y=
 \begin{pmatrix}
 2\sqrt{k}\\
 -4-\mu_k
 \end{pmatrix}
\]

has two positive coordinates. The characteristic equation gives

\[
 M_k y=\mu_k y.
\]

Consequently the minimizing vector is compatible with
\(\alpha,eta>0\), and Rayleigh--Ritz applied to (2) yields

\[
 \lambda_{\min}(D(G))\le\mu_k.
\]

## 7. Exact degree threshold

For \(2\le k\le9\), we need

\[
 \frac{7+\sqrt{16k+1}}2>k.
\]

If \(k\le3\), this is immediate because \(2k-7<0\). For \(4\le k\le9\), both
sides of

\[
 \sqrt{16k+1}>2k-7
\]

are nonnegative, so squaring is legitimate. The difference is

\[
 16k+1-(2k-7)^2
 =4(-k^2+11k-12),
\]

which is positive for every integer \(k=4,\ldots,9\). Hence

\[
 \mu_k<-k,
\]

and therefore

\[
 \Phi(G)=k+\lambda_{\min}(D(G))<0.
\]

At \(k=10\), this particular comparison gives

\[
 \mu_{10}>-10,
\]

so the method does not exclude degree ten. This is a limitation of the bound,
not evidence that a degree-ten counterexample exists.

## 8. Independent exact verification

Run

```text
python scripts/verify_proof_audit_11_diameter_four.py
```

The verifier does not import the original extension verifier. It checks:

- the cross-neighborhood distance-two injection for every diametral pair of the
  finite controls;
- the exact sum bound (1);
- each of the six quadratic-form contributions;
- the comparison polynomial and positive least eigenvector;
- the strict threshold for every integer \(2\le k\le9\) and failure of this
  method at \(k=10\);
- an exact distance-polynomial root certificate for \(C_8\);
- the full affine matching-deletion control obtained from the
  Hoffman--Singleton graph, including degree six, girth five, diameter four,
  and least distance eigenvalue \(-13\).

No floating-point arithmetic or numerical eigensolver is used.

## 9. Claim boundary

The theorem excludes regular diameter-four strict counterexamples only through
degree nine. It does not prove that degree-ten examples exist, and it does not
settle the diameter-four regime in general. The terms “test subspace” and
“comparison matrix” are used in their standard linear-algebraic senses; no
equitability assertion is made.