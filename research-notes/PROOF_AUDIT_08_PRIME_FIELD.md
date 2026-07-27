# Proof Audit 08: the balanced prime-field diameter-three obstruction

**Audited result:** `PRIME_FIELD_DIAMETER_THREE_OBSTRUCTION.md`.  
**Verdict:** `pass_after_correction`.  
**Scope:** the balanced prime-field construction \(G(q,m)\), with \(q\ge7\) an
odd prime and \(1\le m\le q\), under the additional hypothesis that the graph
has diameter three.

## 1. Normalized theorem

Let \(G(q,m)\) have vertices

\[
 P_{i,j},Q_{k,\ell},
 \qquad 0\le i,k<m,\quad j,\ell\in\mathbb F_q,
\]

with same-layer edges

\[
 P_{i,j}\sim P_{i,j\pm1},
 \qquad
 Q_{k,\ell}\sim Q_{k,\ell\pm2},
\]

and cross edges

\[
 P_{i,j}\sim Q_{k,ik+j}.
\]

Then \(G(q,m)\) is connected and \((m+2)\)-regular, has order \(2qm\), and has
girth at least five. If its diameter is three, then it is not a strict
counterexample to WOW-284.

## 2. Corrections found

No parameter, spectral bound, or conclusion changes. Three arguments were too
compressed in the original note.

1. The proof of girth at least five did not explicitly turn the common-neighbor
   case split into separate triangle and 4-cycle exclusions.
2. The nonzero Fourier block was stated, but the passage from a singular value
   of its cross matrix to an adjacency eigenvalue was not proved.
3. The exact \(q=7\) controls recomputed characteristic polynomials but did not
   separately certify that a **nonprincipal** root lies beyond the upper WOW
   boundary.

The audit supplies all three steps and records the result as
`pass_after_correction`.

## 3. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| \(q\ge7\) | makes the same-layer cycles have length at least seven and separates \(\{\pm1\}\) from \(\{\pm2\}\) |
| \(q\) prime | every nonzero coefficient in a linear equation over \(\mathbb F_q\) is invertible |
| \(m\le q\) | distinct layer indices represent distinct field elements |
| \(m\ge1\) | supplies both vertex types and the connected layer graph |
| diameter three | permits the adjacency-window characterization of strict WOW violation |
| regularity | gives degree \(m+2\) and identifies the principal adjacency eigenvalue |

## 4. Graph hypotheses

Each vertex has two same-layer neighbors and one neighbor in every opposite
layer. Hence

\[
 |V|=2qm,\qquad d=m+2.
\]

Each \(P\)-layer is a \(q\)-cycle. Each \(Q\)-layer is also a \(q\)-cycle because
addition by two generates the additive group of \(\mathbb F_q\). For every pair
of layer indices \(i,k\), the cross edges between the corresponding \(P\)- and
\(Q\)-layers form a perfect matching. The quotient graph on the \(2m\) layers is
connected, so \(G(q,m)\) is connected.

### 4.1 Pairs in one layer

Two distinct vertices in the same \(P\)-layer have no common cross neighbor:

\[
 Q_{k,ik+j}=Q_{k,ik+j'}\Longrightarrow j=j'.
\]

Their common neighbors inside the layer are common neighbors in a cycle of
length at least seven, so there is at most one. The same argument applies to a
\(Q\)-layer, using the step-two cycle.

### 4.2 Pairs in different layers of the same type

For \(i\ne i'\), a common \(Q\)-neighbor of \(P_{i,j}\) and \(P_{i',j'}\) must
satisfy

\[
 (i-i')k=j'-j.
\]

There is at most one solution \(k\in\mathbb F_q\), and restricting to the chosen
\(m\) layer indices cannot create another. The corresponding equation for two
distinct \(Q\)-layers is

\[
 i(k-k')=\ell-\ell',
\]

again with at most one solution.

### 4.3 Mixed pairs

For a mixed pair \(P_{i,j},Q_{k,\ell}\), put

\[
 r=\ell-(ik+j).
\]

A common neighbor of type \(P\) exists exactly when \(r\in\{\pm1\}\), and then
it is unique. A common neighbor of type \(Q\) exists exactly when
\(r\in\{\pm2\}\), and then it is unique. The two sets are disjoint for
\(q\ge7\). An adjacent mixed pair has \(r=0\), hence no common neighbor.

Thus every adjacent pair has no common neighbor, excluding triangles, and every
pair has at most one common neighbor, excluding 4-cycles. Therefore

\[
 g(G(q,m))\ge5.
\]

## 5. Fourier decomposition

Translation of every second coordinate by the same field element is an
automorphism. Let

\[
 \omega=e^{2\pi i/q}.
\]

For \(t\in\mathbb F_q\), consider vectors of the form

\[
 f(P_{i,j})=x_i\omega^{tj},
 \qquad
 f(Q_{k,\ell})=y_k\omega^{t\ell}.
\]

These \(q\) character spaces are mutually orthogonal and exhaust the complexified
vertex space.

### 5.1 Zero character

At \(t=0\), the block is

\[
 \begin{pmatrix}2I_m&J_m\\J_m&2I_m\end{pmatrix}
\]

with eigenvalues

\[
 m+2,\qquad 2-m,\qquad 2^{(2m-2)}.
\]

If the graph has diameter three and is a strict counterexample, every
nonprincipal adjacency eigenvalue must lie in

\[
 I_m=(-1-\sqrt{2m+2},-1+\sqrt{2m+2}).
\]

For \(m=1\), the eigenvalue \(2-m=1\) is on the boundary. For \(m=2,3\), the
eigenvalue \(2\) lies outside the interval. For \(m\ge4\), the condition on
\(2-m\) is

\[
 (m-3)^2<2m+2.
\]

Since

\[
 (m-3)^2-(2m+2)=(m-1)(m-7),
\]

strictness leaves only

\[
 m\in\{4,5,6\}.
\]

At \(m=7\) the lower zero-mode eigenvalue is exactly on the boundary; for
\(m>7\) it lies outside.

### 5.2 A nonzero character

Take \(t=1\). The same-layer operators contribute

\[
 a=2\cos\frac{2\pi}{q},
 \qquad
 b=2\cos\frac{4\pi}{q}.
\]

The cross matrix is

\[
 M_{ik}=\omega^{ik},
\]

so the Hermitian block is

\[
 A_1=\begin{pmatrix}aI_m&M\\M^*&bI_m\end{pmatrix}.
\]

Let \(Mv=\sigma u\) and \(M^*u=\sigma v\) be a singular-vector pair. The span
of \((u,0)\) and \((0,v)\) is invariant under \(A_1\), and the representing
matrix is

\[
 \begin{pmatrix}a&\sigma\\\sigma&b\end{pmatrix}.
\]

It has upper eigenvalue

\[
 \frac{a+b+\sqrt{(a-b)^2+4\sigma^2}}2.
\]

Since all \(m^2\) entries of \(M\) have modulus one,

\[
 \sum_{r=1}^m\sigma_r^2=\lVert M\rVert_F^2=m^2,
\]

and therefore \(\sigma_{\max}^2\ge m\). Hence \(A_1\) has an eigenvalue at least

\[
 L(q,m)=\frac{a+b+\sqrt{(a-b)^2+4m}}2
 \ge\sqrt m+\frac{a+b}{2}.
\]

Because this vector lies in a nonzero character space, the eigenvalue is
nonprincipal.

## 6. Exact lower bound beyond the WOW window

For \(q\ge7\), both angles \(2\pi/q\) and \(4\pi/q\) lie in \((0,\pi)\) and are
at most their values at \(q=7\). Since cosine decreases on \([0,\pi]\),

\[
 a+b\ge2\cos\frac{2\pi}{7}+2\cos\frac{4\pi}{7}.
\]

The seventh-root identity gives

\[
 2\cos\frac{2\pi}{7}+2\cos\frac{4\pi}{7}
 =2\cos\frac{\pi}{7}-1.
\]

As \(\pi/7<\pi/6\),

\[
 \cos\frac{\pi}{7}>\frac{\sqrt3}{2}.
\]

Consequently

\[
 L(q,m)>\sqrt m+\frac{\sqrt3-1}{2}.
\]

It remains to compare this with the upper WOW endpoint. Put

\[
 h(m)=\sqrt{2m+2}-\sqrt m.
\]

For \(m>1\),

\[
 h'(m)=\frac1{\sqrt{2m+2}}-\frac1{2\sqrt m}>0.
\]

Thus \(h(m)\le h(6)\) for \(m=4,5,6\). Exact rational bounds give

\[
 h(6)=\sqrt{14}-\sqrt6
 <\frac{15}{4}-\frac{12}{5}
 =\frac{27}{20}
 <\frac{\sqrt3+1}{2},
\]

because \(14<(15/4)^2\), \(6>(12/5)^2\), and
\(3>(17/10)^2\). Hence

\[
 \sqrt m+\frac{\sqrt3-1}{2}
 >-1+\sqrt{2m+2}
\]

for all three zero-mode survivors. The nonzero Fourier block therefore contains
a nonprincipal adjacency eigenvalue above the strict WOW interval.

## 7. Independent exact controls at \(q=7\)

The independent verifier reconstructs \(G(7,m)\) for all \(1\le m\le7\), checks
the graph hypotheses and diameters, and recomputes the complete integer
adjacency characteristic polynomials for \(m=4,5,6\).

To certify a nonprincipal root beyond the upper endpoint without floating-point
ordering, it uses rational separators

\[
 \frac94,\quad\frac52,\quad\frac{11}{4}
\]

for \(m=4,5,6\), respectively. They lie strictly above the corresponding upper
WOW endpoints. Exact Sturm counts show respectively 5, 4, and 3 distinct roots
above these separators. One is the principal root, so each graph has at least
one nonprincipal root beyond the window.

## 8. Claim boundary

The result excludes only diameter-three members of this balanced prime-field
family. It does not address higher-diameter members, different finite-field
constructions, or the existence of an unconditional infinite counterexample
family. The construction is part of the known Murty/Abreu--Funk--Labbate--
Napolitano framework; no construction-priority claim is made.