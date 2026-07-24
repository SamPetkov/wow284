# A spectral obstruction in the prime-field girth-five family

**Status:** proved for the balanced prime-field layer construction below. The
symbolic inequalities and the exact `q=7`, `m=4,5,6` controls are checked by
`scripts/verify_prime_field_obstruction.py`. The construction belongs to the
Murty/Abreu--Funk--Labbate--Napolitano girth-five framework; no construction
novelty is claimed.

## 1. Construction

Let `q\ge7` be an odd prime and let `1\le m\le q`. Introduce vertices

\[
 P_{i,j},\quad Q_{k,\ell},
 \qquad
 0\le i,k<m,\quad j,\ell\in\mathbb F_q.
\]

Add the edges

\[
 P_{i,j}\sim P_{i,j\pm1},
\]

\[
 Q_{k,\ell}\sim Q_{k,\ell\pm2},
\]

and

\[
 P_{i,j}\sim Q_{k,ik+j}.
\]

Call the graph `G(q,m)`.

Every vertex has two same-layer neighbors and one neighbor in each opposite
layer, so

\[
 |V(G(q,m))|=2qm,
 \qquad
 d=m+2.
\]

The graph is connected. Each `P`-layer is a `q`-cycle, each `Q`-layer is a
`q`-cycle because `2` generates the same additive subgroup as `1`, and cross
edges join every `P`-layer to every `Q`-layer.

The graph has no triangle or 4-cycle. The verification is the same coordinate
case split used for the Hoffman--Singleton graph:

- two vertices of the same `P`- or `Q`-layer have at most one same-layer
  common neighbor and no cross common neighbor;
- two vertices in distinct `P`-layers, or in distinct `Q`-layers, have at most
  one cross common neighbor because a nonzero linear equation over
  `\mathbb F_q` has at most one solution;
- for a pair `P_{i,j},Q_{k,\ell}`, put

  \[
  r=\ell-(ik+j).
  \]

  A common `P`-neighbor is possible only for `r\in\{\pm1\}`, while a common
  `Q`-neighbor is possible only for `r\in\{\pm2\}`. These sets are disjoint
  when `q\ge7`, and an adjacent pair has `r=0`.

Thus

\[
 g(G(q,m))\ge5.
\]

## 2. Zero Fourier mode

Simultaneous translation of all second coordinates is an automorphism. Over
`\mathbb C`, decompose the adjacency operator into the `q` additive-character
spaces.

On the zero character, the block is

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

Suppose that `G(q,m)` has diameter three and is a strict WOW-284
counterexample. The diameter-three criterion requires every nonprincipal
adjacency eigenvalue `\theta` to satisfy

\[
 |\theta+1|<\sqrt{2(m+2)-2}=\sqrt{2m+2}.
\]

For `m=1`, the eigenvalue `2-m=1` lies on the boundary. For `m\ge2`, the
eigenvalue `2` requires

\[
 3<\sqrt{2m+2},
\]

so `m\ge4`. The eigenvalue `2-m` requires

\[
 |3-m|<\sqrt{2m+2}.
\]

Since

\[
 (m-3)^2-(2m+2)=(m-1)(m-7),
\]

we must also have `m\le6`. Therefore only

\[
 m\in\{4,5,6\}
\]

can survive the zero-mode test.

## 3. A nontrivial Fourier block

Let

\[
 \omega=e^{2\pi i/q}.
\]

On the character `j\mapsto\omega^j`, the adjacency block has the Hermitian
form

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
\]

and

\[
 M_{ik}=\omega^{ik}.
\]

Every entry of `M` has modulus one, so

\[
 \lVert M\rVert_F^2=m^2.
\]

Hence its largest singular value satisfies

\[
 \sigma_{\max}(M)^2\ge m.
\]

The block `A_1` therefore has an eigenvalue at least

\[
 L(q,m)=
 \frac{a+b+\sqrt{(a-b)^2+4m}}2
 \ge\sqrt m+\frac{a+b}{2}.
\]

This eigenvalue belongs to a nonzero character space and is therefore
nonprincipal.

For `q\ge7`, both cosines are bounded below by their values at `q=7`. The
seventh-root identity

\[
 1+2\cos\frac{2\pi}{7}
 +2\cos\frac{4\pi}{7}
 +2\cos\frac{6\pi}{7}=0
\]

gives

\[
 2\cos\frac{2\pi}{7}+2\cos\frac{4\pi}{7}
 =2\cos\frac{\pi}{7}-1.
\]

Thus

\[
 L(q,m)
 \ge\sqrt m+\cos\frac{\pi}{7}-\frac12
 >\sqrt m+\frac{\sqrt3-1}{2},
\]

because `\pi/7<\pi/6`.

For `m=4,5,6`,

\[
 \sqrt m+\frac{\sqrt3-1}{2}
 >-1+\sqrt{2m+2}.
\]

An exact certificate for the worst case `m=6` is

\[
 \sqrt{14}-\sqrt6
 <\frac{15}{4}-\frac{12}{5}
 =\frac{27}{20}
 <\frac{\sqrt3+1}{2},
\]

using

\[
 \sqrt{14}<\frac{15}{4},
 \qquad
 \sqrt6>\frac{12}{5},
 \qquad
 \sqrt3>\frac{17}{10}.
\]

The function `\sqrt{2m+2}-\sqrt m` is increasing for `m>1`, so the same
comparison holds for `m=4,5`.

We have found a nonprincipal adjacency eigenvalue outside the strict WOW
window. This proves the theorem below.

## Theorem

Let `q\ge7` be an odd prime. If `G(q,m)` has diameter three, then it is not a
strict counterexample to WOW-284.

## 4. Exact `q=7` controls

The only zero-mode survivors are `m=4,5,6`. The verifier reconstructs all
three graphs and checks exactly that they have:

\[
 (|V|,d,g,\operatorname{diam})
 =(56,6,5,3),
 (70,7,5,3),
 (84,8,5,3),
\]

respectively. It then recomputes their complete integer adjacency
characteristic polynomials. Each fails the shifted adjacency window, in
agreement with the general Fourier proof.

## 5. Scope

This theorem excludes only the diameter-three members of this balanced
prime-field layer family. It does not prove that all higher-diameter members
satisfy WOW-284, and it does not rule out an infinite family from a different
finite-field construction.

The construction itself is part of the known Murty/Abreu family of regular
girth-five graphs. The spectral obstruction above is a specialized WOW-284
application; literature priority has not been established.
