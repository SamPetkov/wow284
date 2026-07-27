# A spectral obstruction in the balanced prime-field family

**Status:** exact theorem for the construction below, with an independent
line-by-line audit. The construction belongs to the Murty/Abreu--Funk--Labbate--
Napolitano girth-five framework; no construction or priority claim is made.

## Theorem

Let \(q\ge7\) be an odd prime and \(1\le m\le q\). Construct \(G(q,m)\) as below.
If \(G(q,m)\) has diameter three, then it is not a strict counterexample to
WOW-284.

The theorem is conditional on diameter three. It says nothing about the
higher-diameter members of this family.

## 1. Construction and graph hypotheses

Introduce vertices

\[
 P_{i,j},\quad Q_{k,\ell},
 \qquad
 0\le i,k<m,\quad j,\ell\in\mathbb F_q,
\]

and edges

\[
 P_{i,j}\sim P_{i,j\pm1},
 \qquad
 Q_{k,\ell}\sim Q_{k,\ell\pm2},
\]

\[
 P_{i,j}\sim Q_{k,ik+j}.
\]

Each vertex has two same-layer neighbors and one neighbor in every opposite
layer. Thus

\[
 |V(G(q,m))|=2qm,
 \qquad
 d=m+2.
\]

Each \(P\)-layer is a \(q\)-cycle. Each \(Q\)-layer is also a \(q\)-cycle because
addition by two generates the additive group of \(\mathbb F_q\). Cross edges
join every \(P\)-layer to every \(Q\)-layer. Therefore the graph is connected.

We now exclude triangles and 4-cycles by checking common neighbors.

- Two distinct vertices in one \(P\)-layer have no common cross neighbor, and
  have at most one common neighbor in their cycle. The same holds in one
  \(Q\)-layer.
- If \(i\ne i'\), a common \(Q\)-neighbor of \(P_{i,j}\) and \(P_{i',j'}\) must
  solve
  \[
  (i-i')k=j'-j,
  \]
  which has at most one solution. The analogous equation for two distinct
  \(Q\)-layers also has at most one solution.
- For a mixed pair \(P_{i,j},Q_{k,\ell}\), put
  \[
  r=\ell-(ik+j).
  \]
  A common \(P\)-neighbor is possible exactly when \(r\in\{\pm1\}\), and a
  common \(Q\)-neighbor exactly when \(r\in\{\pm2\}\). Each is then unique, and
  the two alternatives are disjoint for \(q\ge7\). An adjacent mixed pair has
  \(r=0\), so it has no common neighbor.

Hence adjacent pairs have no common neighbor and arbitrary pairs have at most
one. Thus

\[
 g(G(q,m))\ge5.
\]

## 2. Character decomposition

Translation of every second coordinate by the same element of \(\mathbb F_q\)
is an automorphism. Let

\[
 \omega=e^{2\pi i/q}.
\]

For \(t\in\mathbb F_q\), the character space consists of vectors

\[
 f(P_{i,j})=x_i\omega^{tj},
 \qquad
 f(Q_{k,\ell})=y_k\omega^{t\ell}.
\]

These \(q\) spaces are mutually orthogonal and exhaust the complexified vertex
space.

### 2.1 Zero character

For \(t=0\), the adjacency block is

\[
 \begin{pmatrix}
 2I_m&J_m\\
 J_m&2I_m
 \end{pmatrix}.
\]

Its eigenvalues are

\[
 m+2,
 \qquad
 2-m,
 \qquad
 2^{(2m-2)}.
\]

Assume now that \(G(q,m)\) has diameter three and is a strict counterexample.
The regular diameter-three criterion requires every nonprincipal adjacency
eigenvalue \(\theta\) to satisfy

\[
 |\theta+1|<\sqrt{2m+2}.
\]

For \(m=1\), the eigenvalue \(2-m=1\) lies on the boundary. For \(m=2,3\), the
eigenvalue \(2\) lies outside the interval. For \(m\ge4\), the eigenvalue
\(2-m\) requires

\[
 (m-3)^2<2m+2.
\]

Since

\[
 (m-3)^2-(2m+2)=(m-1)(m-7),
\]

only

\[
 m\in\{4,5,6\}
\]

survive the zero-character test. At \(m=7\) there is equality at the boundary;
for \(m>7\) the inequality fails.

### 2.2 A nonzero character

Take \(t=1\). The adjacency block has Hermitian form

\[
 A_1=
 \begin{pmatrix}
 aI_m&M\\
 M^*&bI_m
 \end{pmatrix},
\]

where

\[
 a=2\cos\frac{2\pi}{q},
 \qquad
 b=2\cos\frac{4\pi}{q},
 \qquad
 M_{ik}=\omega^{ik}.
\]

Let \(Mv=\sigma u\) and \(M^*u=\sigma v\) be a singular-vector pair. The span
of \((u,0)\) and \((0,v)\) is invariant and carries

\[
 \begin{pmatrix}a&\sigma\\\sigma&b\end{pmatrix}.
\]

Its upper eigenvalue is

\[
 \frac{a+b+\sqrt{(a-b)^2+4\sigma^2}}2.
\]

All \(m^2\) entries of \(M\) have modulus one, so

\[
 \sum_{r=1}^m\sigma_r^2=\lVert M\rVert_F^2=m^2.
\]

Therefore \(\sigma_{\max}^2\ge m\), and \(A_1\) has an eigenvalue at least

\[
 L(q,m)=
 \frac{a+b+\sqrt{(a-b)^2+4m}}2
 \ge\sqrt m+\frac{a+b}{2}.
\]

This eigenvalue lies in a nonzero character space and is therefore
nonprincipal.

## 3. The nonzero mode crosses the WOW boundary

For \(q\ge7\), the angles \(2\pi/q\) and \(4\pi/q\) lie in \((0,\pi)\) and are no
larger than their values at \(q=7\). Hence

\[
 a+b\ge
 2\cos\frac{2\pi}{7}+2\cos\frac{4\pi}{7}.
\]

The seventh-root identity gives

\[
 2\cos\frac{2\pi}{7}+2\cos\frac{4\pi}{7}
 =2\cos\frac{\pi}{7}-1.
\]

Since \(\pi/7<\pi/6\),

\[
 \cos\frac{\pi}{7}>\frac{\sqrt3}{2},
\]

and therefore

\[
 L(q,m)>\sqrt m+\frac{\sqrt3-1}{2}.
\]

Define

\[
 h(m)=\sqrt{2m+2}-\sqrt m.
\]

For \(m>1\),

\[
 h'(m)=\frac1{\sqrt{2m+2}}-\frac1{2\sqrt m}>0.
\]

Thus \(h(m)\le h(6)\) for \(m=4,5,6\). Exact rational estimates give

\[
 h(6)=\sqrt{14}-\sqrt6
 <\frac{15}{4}-\frac{12}{5}
 =\frac{27}{20}
 <\frac{\sqrt3+1}{2},
\]

using

\[
 14<\left(\frac{15}{4}\right)^2,
 \qquad
 6>\left(\frac{12}{5}\right)^2,
 \qquad
 3>\left(\frac{17}{10}\right)^2.
\]

Consequently, for every \(m\in\{4,5,6\}\),

\[
 \sqrt m+\frac{\sqrt3-1}{2}
 >-1+\sqrt{2m+2}.
\]

The nonzero character block therefore contains a nonprincipal adjacency
eigenvalue beyond the upper endpoint of the strict WOW window. This proves the
theorem.

## 4. Exact \(q=7\) controls

The independent verifiers reconstruct \(G(7,m)\) and check the complete integer
adjacency characteristic polynomials for \(m=4,5,6\). They also certify a
nonprincipal root beyond the upper WOW endpoint by exact Sturm counts.

Use the rational separators

\[
 \frac94,
 \qquad
 \frac52,
 \qquad
 \frac{11}{4}
\]

for \(m=4,5,6\), respectively. Each lies strictly above the corresponding upper
WOW endpoint. The square-free characteristic polynomials have respectively
5, 4, and 3 distinct roots above the separator. Since only one can be the
principal eigenvalue, every graph has a nonprincipal root outside the window.

The graph data are

\[
 (|V|,d,g,\operatorname{diam})
 =(56,6,5,3),
 (70,7,5,3),
 (84,8,5,3).
\]

## 5. Verification and scope

Run

```text
python scripts/verify_prime_field_obstruction.py
python scripts/verify_proof_audit_08_prime_field.py
```

The second verifier is independent of the first. It checks the symbolic block
reductions, exact radical comparisons, all \(q=7\) graph hypotheses, the three
complete characteristic polynomials, and the exact nonprincipal-root counts.

The theorem excludes only diameter-three members of this balanced prime-field
family. It does not address higher-diameter members, other finite-field
families, or an unconditional infinite counterexample family.
