# Complete mathematical synthesis of the post-v1 WOW-284 programme

**Scope.** This document consolidates the mathematical content developed after
the submitted v1 manuscript. It is a theorem ledger and manuscript-planning
record, not a replacement for the individual proof notes. Every result is
classified by proof status, exact-verification status, and literature boundary.
No result in this document is automatically promoted into `main.tex`.

**Notation.** For a connected graph \(G\), write

\[
D=D(G),\qquad
\lambda_D(G)=\lambda_{\min}(D(G)),\qquad
\Phi(G)=\delta^*(G)+\lambda_D(G).
\]

Thus \(G\) is a strict counterexample to WOW-284 exactly when
\(\Phi(G)>0\).

## Status legend

- **v1:** already present in the submitted manuscript.
- **proved / exact:** an analytic proof and an exact executable certificate are
  present in the stacked branch.
- **audited:** a separate one-proof-at-a-time audit has checked the statement,
  hypotheses, critical lemmas, and an independent verifier.
- **priority unresolved:** correctness is supported, but the literature search
  does not justify a novelty or first-priority claim.
- **computational classification:** all objects in a precisely defined finite
  family are covered exactly; this is not a classification outside that family.

The current stack is deliberately conservative. Search silence is never treated
as proof of novelty.

---

# Part I. The v1 core

## 1. Moore-graph disproof mechanism

Let \(M\) be a degree-\(k\) Moore graph of diameter two. Then

\[
|V(M)|=k^2+1,\qquad g(M)=5,\qquad \delta^*(M)=k,
\]

and the Moore common-neighbour identity is

\[
A^2=(k-1)I-A+J.
\]

On \(\mathbf 1^\perp\), the two nonprincipal adjacency eigenvalues are

\[
rac{-1\pm\sqrt{4k-3}}2.
\]

Since every nonedge has distance two,

\[
D=2J-2I-A.
\]

Hence

\[
oxed{
\lambda_D(M)=-rac{3+\sqrt{4k-3}}2
}
\]

and

\[
oxed{
\Phi(M)=k-rac{3+\sqrt{4k-3}}2.
}
\]

Therefore a Moore graph satisfies WOW-284 exactly for \(k\le3\), with equality
at \(k=3\), and is a strict counterexample for every realizable \(k>3\).
The degree-seven Hoffman--Singleton graph gives

\[
\delta^*=7,\qquad \lambda_D=-4,\qquad \Phi=3.
\]

**Status:** v1; complete graph-level Lean formalisation for the 50-vertex
example.

## 2. Regular diameter-three spectral criterion

Let \(G\) be connected, \(k\)-regular, of girth at least five and diameter
three. The distance-two matrix is \(A_2=A^2-kI\), so

\[
D=A+2A_2+3(J-I-A-A_2)
 =3J+(k-3)I-2A-A^2.
\]

Equivalently,

\[
oxed{
D+kI=3J+(2k-2)I-(A+I)^2.
}
\]

On \(\mathbf 1^\perp\), a nonprincipal adjacency eigenvalue \(	heta\) maps to

\[
\mu(	heta)=k-2-(	heta+1)^2.
\]

Consequently

\[
oxed{
\Phi(G)=2k-2-\max_{	heta
e k}(	heta+1)^2
}
\]

and \(G\) is a strict counterexample exactly when

\[
oxed{
|	heta+1|<\sqrt{2k-2}\quad	ext{for every nonprincipal }	heta.
}
\]

This shifted spectral window is the organising principle for the entire
post-v1 regular theory.

**Status:** v1; exact matrix checks on the regular order-40 and order-42
examples.

## 3. Explicit finite counterexamples in v1

The manuscript gives exact counterexamples of orders \(38,39,40,42,50\).
Representative parameters are

\[
egin{array}{c|c|c}
|V|&\delta^*&\lambda_D\
\hline
38&17/3&-3-\sqrt7\
39&35/6&>-35/6\
40&6&-5\
42&6&-5\
50&7&-4.
\end{array}
\]

All finite claims are reconstructed by integer BFS and exact rational or
algebraic certificates. Lean kernel-checks the complete 50-vertex theorem and
finite spectral certificates for orders \(38,39,40,42\).

---

# Part II. General structural extensions

## 4. Dual degree as radius-two growth

If \(G\) contains no triangle and no 4-cycle, then for every vertex \(v\),

\[
|\Gamma_2(v)|=\sum_{u\in N(v)}(d(u)-1).
\]

Therefore

\[
oxed{
 d^*(v)=rac{|B_2(v)|-1}{d(v)}.
}
\]

This converts the Graffiti quantity into normalised local growth. It is useful
for deletion arguments and local incidence counts, but the identity itself is
literature-established and is not claimed as new.

**Status:** proved / exact; literature-established.

## 5. Higher-diameter distance-polynomial transfer

Define the nonbacktracking polynomials

\[
F_0=1,\qquad F_1=x,\qquad F_2=x^2-k,
\]

and

\[
F_i=xF_{i-1}-(k-1)F_{i-2}\qquad(i\ge3).
\]

If \(G\) is connected and \(k\)-regular, has diameter \(d\), and girth at least
\(2d-1\), then \(A_i=F_i(A)\) for \(0\le i\le d-1\). Hence

\[
oxed{
D=dJ+q_d(A),\qquad
q_d(x)=\sum_{i=0}^{d-1}(i-d)F_i(x).
}
\]

For example,

\[
q_3(x)=k-3-2x-x^2,
\]

\[
q_4(x)=-x^3-2x^2+(2k-4)x+2k-4.
\]

**Status:** verified derivation; substantially overlaps established
minimal-cage and distance-polynomial theory, so no novelty claim is made.

---

# Part III. Diameter and degree obstructions

## 6. Regular counterexamples have degree at least six

### Theorem

If a connected regular graph of girth at least five is a strict WOW-284
counterexample, then its degree is at least six.

The first universal observation is

\[
\lambda_D(G)\le-\operatorname{diam}(G),
\]

obtained from the Rayleigh vector \(e_u-e_v\) on a diametral pair. Therefore a
\(k\)-regular strict counterexample must satisfy

\[
\operatorname{diam}(G)<k.
\]

The degrees \(2,3,4,5\) are then closed as follows.

- \(k=2\): connected graphs are cycles and fail the strict diameter condition.
- \(k=3\): the graph would be the degree-three Moore graph and lies on equality.
- \(k=4\): diameter two is excluded by nonintegral Moore multiplicities;
  diameter three is excluded by distance-layer compression and interlacing.
- \(k=5\): diameter two is excluded by Moore multiplicities; diameter four is
  excluded by interlacing the distance matrix of a diametral \(P_5\); diameter
  three is reduced to the four \((5,5)\)-cages, all of which have an exact
  distance eigenvalue at most \(-5\).

Thus

\[
oxed{k\ge6.}
\]

**Status:** proved / exact; dedicated proof audit queued.

## 7. General endpoint-neighbourhood diameter bound

Let \(G\) be connected, have girth at least five, minimum degree \(\delta\),
maximum degree \(\Delta\), and diameter \(d\ge5\). For diametral vertices \(u,v\),
put \(p=d(u)\), \(q=d(v)\), and use a vector supported with opposite signs on
\(N(u)\) and \(N(v)\). Optimisation gives

\[
\lambda_D(G)\le
p+q-2-\sqrt{(p-q)^2+pq(d-2)^2}.
\]

Writing \(p=\delta+\alpha\), \(q=\delta+eta\), \(t=d-2\), the exact identity

\[
egin{aligned}
&(p-q)^2+pqt^2-igl(p+q+\delta(t-2)igr)^2\
&\qquad=(t-2)igl[\delta t(\alpha+eta)+(t+2)\alphaetaigr]\ge0
\end{aligned}
\]

yields

\[
oxed{
\lambda_D(G)\le-\delta(d-4)-2.
}
\]

Since \(\delta^*(G)\le\Delta\), every strict counterexample must satisfy

\[
oxed{
\Delta>\delta(d-4)+2.
}
\]

In particular,

\[
oxed{
\operatorname{diam}(G)\le
3+\left\lceilrac{\Delta-2}{\delta}ightceil.
}
\]

For a \(k\)-regular graph this becomes

\[
oxed{\operatorname{diam}(G)\le4.}
\]

More quantitatively, every regular graph in the hypotheses with \(d\ge5\)
satisfies

\[
\Phi(G)\le k(5-d)-2<0.
\]

**Status:** proved / exact symbolic audit; independent proof audit and priority
search queued.

## 8. Diameter-four obstruction

Let \(G\) be connected, \(k\)-regular, of girth at least five and diameter four.
Choose diametral vertices \(u,v\), put \(U=N(u)\), \(V=N(v)\), and let \(r\) be
the number of pairs \((a,b)\in U	imes V\) at distance two. Girth at least five
gives

\[
r\le k(k-1),
\]

so

\[
\sum_{a\in U,b\in V}d(a,b)\ge2k^2+k.
\]

A four-level signed Rayleigh vector reduces to the matrix

\[
egin{pmatrix}
-4&-2\sqrt{k}\
-2\sqrt{k}&-3
\end{pmatrix}.
\]

Therefore

\[
oxed{
\lambda_D(G)\le-rac{7+\sqrt{16k+1}}2.
}
\]

and

\[
oxed{
\Phi(G)\le k-rac{7+\sqrt{16k+1}}2.
}
\]

For \(2\le k\le9\), the right-hand side is negative. Hence no regular strict
counterexample of degree at most nine has diameter four.

**Status:** proved / exact symbolic audit; independent proof audit and priority
search queued.

## 9. Regular-counterexample trichotomy

Combining the preceding results gives the following structural reduction.
Every regular strict counterexample has exactly one of the following forms.

1. **Diameter two:** a Moore graph.
2. **Diameter three:** all nonprincipal adjacency eigenvalues lie in
   \(|	heta+1|<\sqrt{2k-2}\).
3. **Diameter four:** necessarily \(k\ge10\).

There are no regular strict counterexamples of diameter at least five.

For fixed \(k\), the search is finite. In the diameter-four regime the ordinary
Moore bound gives

\[
|V(G)|\le1+k\sum_{i=0}^3(k-1)^i
=k^4-2k^3+2k^2+1.
\]

---

# Part IV. Diameter-three order bounds and method optimality

## 10. Fourth-moment score bound

For a \(k\)-regular girth-five diameter-three graph, write the nonprincipal
adjacency eigenvalues as \(	heta_i\) and put \(y_i=	heta_i+1\). Exact trace
identities give

\[
\sum y_i^2=(k+1)(n-k-1),
\]

\[
\sum y_i^4=(2k^2+5k+1)n-(k+1)^4.
\]

If \(R=\max_i|y_i|\), then \(\sum y_i^4\le R^2\sum y_i^2\), and
\(\Phi=2k-2-R^2\). Therefore

\[
oxed{
\Phi(G)\le
rac{(k+1)^2(k^2+3)-(5k+3)n}
{(k+1)(n-k-1)}.
}
\]

Every strict counterexample consequently satisfies

\[
oxed{
 n<rac{(k+1)^2(k^2+3)}{5k+3}.
}
\]

This was the first general order bound in the extension stack.

## 11. Stronger fourth-moment identity

A sharper exact identity is

\[
oxed{
\sum_{i=1}^{n-1}
(2k-2-y_i^2)(y_i+1)^2
=(k+2)igl((k+2)(k^2+3)-6nigr).
}
\]

In a strict counterexample every factor \(2k-2-y_i^2\) is positive. The sum
cannot vanish, since vanishing would force every nonprincipal adjacency
eigenvalue to equal \(-2\), contradicting the trace equation and
\(n\ge k+1\). Hence

\[
oxed{
 n<B_k:=rac{(k+2)(k^2+3)}6.
}
\]

At \(k=6\), this gives \(n<52\), hence \(n\le51\).

**Status:** proved / exact; independent audit queued.

## 12. Exact ceiling of the standard nonbacktracking LP hierarchy

Let \(F_i\) be the standard nonbacktracking polynomials. Suppose

\[
f(x)=\sum_i f_iF_i(x)
\]

satisfies

\[
f_0>0,\qquad f_i\ge0\ (i\ge5),\qquad
f(x)\le0\quad	ext{on}\quad
[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
\]

Then

\[
oxed{
rac{f(k)}{f_0}\ge B_k=rac{(k+2)(k^2+3)}6.
}
\]

Equality is attained by

\[
oxed{
 f_*(x)=
 rac{(x+2)^2igl(x^2+2x-(2k-3)igr)}{6(k+2)}.
}
\]

The lower bound is certified by a positive three-point dual measure supported
at

\[
-1-\sqrt{2k-2},\qquad -2,\qquad -1+\sqrt{2k-2},
\]

with exact moment matching for \(F_1,\ldots,F_4\), explicit positive slacks for
\(F_5,\ldots,F_9\), and a uniform Chebyshev estimate for every \(i\ge10\).

Thus no polynomial degree in this standard one-point nonbacktracking LP
hierarchy improves the bound \(n<B_k\). Any stronger theorem must use local
intersection information, multipoint semidefinite constraints, cycle
realizability, or canonical generation.

**Status:** proved / exact; proof audit and literature-priority clearance queued.

## 13. Equality boundary

A regular girth-five diameter-three graph satisfies equality in WOW-284 exactly
when

\[
oxed{
\max_{	heta
e k}|	heta+1|=\sqrt{2k-2}.
}
\]

Equivalently, \(D+kI\succeq0\) and \(D+kI\) is singular. If \(2k-2\) is not a
square, algebraic conjugacy forces the two boundary adjacency eigenvalues

\[
-1\pm\sqrt{2k-2}
\]

to have the same multiplicity, so the distance eigenvalue \(-k\) has even
multiplicity. If \(2k-2\) is a square, then \(k=2r^2+1\).

Jørgensen's 9-regular order-96 girth-five graph is an exact boundary control:

\[
\delta^*=9,\qquad \lambda_D=-9,\qquad\Phi=0,
\]

and the distance factor \((x+9)^8\) matches the contact eigenvalues \(3,-5\).

**Status:** proved / exact; graph provenance independently reconstructed.

---

# Part V. The degree-six programme

## 14. Closing the \(n\le51\) gate by distance-layer compression

Write

\[
n=37+c.
\]

For a fixed vertex the layer sizes are \(1,6,30,c\). At the smallest feasible
internal degree of the distance-two layer, the nonprincipal compression factor
is

\[
p_{6,c}(x)=5x^3+(c+5)x^2-25x-6c.
\]

At the upper WOW boundary \(r=-1+\sqrt{10}\),

\[
oxed{
 p_{6,c}(r)=-(2\sqrt{10}-5)(c-15).
}
\]

For \(c\ge15\), the largest compression root is at least the boundary; by
interlacing strict violation is impossible. Therefore

\[
oxed{c\le14,\qquad n\le51.}
\]

The stronger fourth-moment identity gives the same bound independently.

## 15. Diameter reduction at degree six

A connected 6-regular strict counterexample cannot have diameter at least four.
For vertices at distance \(d\ge4\), use the signed vector with weights

\[
3,\ 1	ext{ on }N(u),\ -3,\ -1	ext{ on }N(v).
\]

The exact estimate is

\[
rac{x^{\mathsf T}Dx}{\|x\|^2}\lerac{204-81d}{15}\le-8,
\]

contradicting \(\delta^*=6\). Diameter two would force

\[
\chi_A(x)=(x-6)(x^2+x-5)^{18},
\]

whose trace is \(-12\), contradicting \(\operatorname{tr}A=0\). Hence every
6-regular strict counterexample has diameter three.

**Status:** audited; the original scope gap was repaired explicitly in PR #19.

## 16. Edge-local spectral inequality

For general \(k\), put

\[
f_k(x)=(x+2)^2igl(x^2+2x-(2k-3)igr),
\]

\[
C_k=f_k(k)=(k+2)^2(k^2+3),
\]

and

\[
M=-f_k(A)+rac{C_k}{n}J\succeq0.
\]

If \(\sigma_{uv}\) is the number of 5-cycles through an edge \(uv\), then exact
diagonal and edge entries of \(M\), followed by the \(2	imes2\) PSD condition,
give

\[
oxed{\sigma_{uv}\ge2k-2}
\]

and

\[
oxed{
\sigma_{uv}\le
rac{2(k+2)^2(k^2+3)}n-10k-26.
}
\]

Independently, if \(n=k^2+1+c\), radius-two ball intersection gives

\[
oxed{\sigma_{uv}\ge(k-1)^2-c.}
\]

At \(k=6,n=51\), these bounds force \(\sigma_{uv}=11\) on every edge. But

\[
5N_5=153\cdot11=1683
\]

is impossible. Thus

\[
oxed{
	ext{every connected 6-regular strict counterexample has }n\le50.
}
\]

**Status:** audited after the diameter-scope correction; exact independent
verifier present.

## 17. Exact structure at order 50

For a hypothetical order-50 candidate, every edge lies in 12 or 13 five-cycles.
Let \(H\) be the spanning subgraph of the 13-cycle edges and \(m=|E(H)|\).
If \(	au(v)\) is the number of 5-cycles through \(v\), then distance-layer
compression yields

\[
oxed{	au(v)\in\{36,37,38\}}
\]

and hence

\[
oxed{d_H(v)=2	au(v)-72\in\{0,2,4\}.}
\]

Thus \(H\) is an even spanning subgraph of maximum degree four. Moreover,

\[
oxed{N_5=360+rac m5,\qquad m\equiv0\pmod5.}
\]

For a two-edge path \(u-v-w\), define

\[
\alpha=\#\{	ext{5-cycles containing }u-v-w\},
\]

\[
eta=\#\{	ext{6-cycles containing }u-v-w\},
\qquad r=6\alpha+eta.
\]

Three-vertex Gram minors and the kernel refinement give

\[
egin{array}{c|c}
	ext{incident edge types}&	ext{allowed }r\
\hline
	ext{low--low}&30,31,32\
	ext{mixed}&30,31,32\
	ext{high--high}&30,31.
\end{array}
\]

The value \(r=29\), which determinant nonnegativity alone permits in two cases,
is impossible because equality would put \(e_u-e_w\) in the adjacency
\(-2\)-eigenspace, contradicting the \(u\)-coordinate.

Writing

\[
S_2=\sum_vd_H(v)^2,
\]

the local table gives

\[
oxed{N_6\ge1950-m}
\]

and

\[
oxed{N_6\le2200-rac{5m}{6}-rac{S_2}{12}.}
\]

Independent shifted-moment and localising-matrix Schur complements give

\[
oxed{
N_6\ge
rac{43m^2-70200m+119632500}{58500}
}
\]

and

\[
oxed{
N_6\le
rac{4220000-2200m-7m^2}{2000}.
}
\]

Exact integer enumeration leaves 266 coarse degree profiles. Therefore the
present constraints are strong necessary conditions and useful canonical-search
filters, but they do not eliminate order 50.

**Status:** proved necessary conditions / exact; dedicated proof audit queued.

---

# Part VI. Moore-puncture theory

## 18. One deleted Moore vertex

Let \(M\) be a degree-\(k\) Moore graph and \(H=M-v\). Then

\[
|V(H)|=k^2,\qquad \delta^*(H)=k-rac1k,
\]

and

\[
oxed{\lambda_D(H)=-2-\sqrt{k}.}
\]

Hence

\[
oxed{
\Phi(H)=k-rac1k-2-\sqrt{k},
}
\]

which is positive exactly for integers \(k\ge5\).

The full distance spectrum is obtained by an orthogonal decomposition into the
constant quotient, a two-dimensional incidence module for each vector in
\(\mathbf1^\perp\) on the deleted neighbourhood, and the residual Moore kernel.

**Status:** proved / exact; priority unresolved; proof audit queued.

## 19. Deleting the endpoints of an edge

Let \(uv\in E(M)\) and \(H=M-\{u,v\}\). Then

\[
|V(H)|=k^2-1,\qquad \delta^*(H)=k-rac2k,
\]

and again

\[
oxed{\lambda_D(H)=-2-\sqrt{k}.}
\]

Therefore

\[
oxed{
\Phi(H)=k-rac2k-2-\sqrt{k},
}
\]

which is positive exactly for integers \(k\ge5\).

**Status:** proved / exact; priority unresolved; proof audit queued.

## 20. Deleting two nonadjacent Moore vertices

Let \(u,v\) be nonadjacent vertices of a degree-\(k\) Moore graph, \(k\ge5\), and
put \(H=M-\{u,v\}\). Then

\[
oxed{\delta^*(H)=k-rac2k.}
\]

Writing \(\Delta=\sqrt{4k-3}\), the exact distance characteristic polynomial is

\[
egin{aligned}
\chi_{D(H)}(x)={}&(x-k+3)R_k(x)\
&\cdot(x^2+4x-k+3)^{k-2}\
&\cdot(x^2+4x-k+5)^{k-2}\
&\cdot\left(x+rac{\Delta+3}{2}ight)^{M_-}\
&\cdot\left(x-rac{\Delta-3}{2}ight)^{M_+},
\end{aligned}
\]

where

\[
egin{aligned}
R_k(x)={}&x^4+(10-2k^2)x^3
 +(2k^3-17k^2-2k+36)x^2\
&+(12k^3-49k^2-4k+53)x
 -2k^4+17k^3-38k^2+5k+20,
\end{aligned}
\]

\[
M_-=rac{k(k-2)+(k^2-4k+2)\Delta}{2\Delta},\qquad
M_+=rac{-k(k-2)+(k^2-4k+2)\Delta}{2\Delta}.
\]

The factorisation follows from a five-cell equitable partition and a complete
orthogonal decomposition into constant, matched symmetric, matched
antisymmetric, common-neighbour, and residual-kernel modules.

A deletion-stability estimate proves strictness for every realizable \(k\ge6\),
even though the least root of the quartic quotient does not simplify uniformly.

**Status:** proved / exact; direct-sum audit artifact present; priority unresolved;
dedicated proof audit queued.

## 21. General deletion-stability inequality

Let \(H=G-S\) be connected, and define

\[
D_0=D(G)[V(H)],\qquad E_S=D(H)-D_0.
\]

If

\[
a=\delta^*(G),\qquad b=\delta^*(H),\qquad
\gamma=\Phi(G),
\]

then Cauchy interlacing and Weyl's inequality give

\[
oxed{
\Phi(H)\ge\gamma-(a-b)+\lambda_{\min}(E_S).
}
\]

For Moore punctures, \(E_S\) is a structured distance-increase graph. This
proves that deleting any two vertices preserves strict violation for \(k\ge6\),
while adjacent pairs already work for \(k\ge5\).

**Status:** proved / exact specialised checks; standard matrix ingredients.

## 22. Small-puncture Moore normal form

Let \(M\) be a degree-\(k\) Moore graph, let \(S\subseteq V(M)\), and write
\(s=|S|\le k-1\), \(H=M-S\). Then \(H\) is connected, has diameter at most
three, and

\[
oxed{\delta^*(H)=k-rac{s}{k}.}
\]

Let \(B\) be the surviving-vertex/deleted-vertex incidence matrix. The exact
distance matrix is

\[
oxed{
D(H)=2(J-I)-A(H)+BB^{\mathsf T}
-\operatorname{diag}(BB^{\mathsf T}).
}
\]

The connectivity proof constructs \(k-1\) internally vertex-disjoint
length-three replacement paths whenever a deleted common neighbour destroys a
length-two path. The dual-degree lower bound follows from

\[
\sum_{y\in N_H(x)}|N_M(y)\cap S|\le s-|N_M(x)\cap S|,
\]

and equality is attained using

\[
\left|igcap_{z\in S}\Gamma_2(z)ight|
\ge k^2+1-s(k+1)\ge2.
\]

This theorem unifies all small Moore punctures at the metric and dual-degree
level; the detailed spectra still depend on the deletion geometry.

**Status:** proved / exact finite specialisation; proof audit and priority search
queued.

## 23. Hoffman--Singleton deletion robustness radius

For the Hoffman--Singleton graph \(M\), every deletion of at most five vertices
remains a strict WOW-284 counterexample. The exact automorphism-orbit counts for
deleted sets of sizes \(1,2,3,4,5\) are

\[
1,\ 2,\ 4,\ 11,\ 33.
\]

For every orbit representative the verifier reconstructs the punctured graph,
checks the small-puncture distance formula and

\[
\delta^*(M-S)=rac{49-|S|}{7},
\]

and proves

\[
oxed{
7D(M-S)+(49-|S|)I\succ0.
}
\]

Thus every labelled deletion set with \(|S|\le5\) is strict.

Sharpness is witnessed by

\[
S=\{P_{2,4},P_{3,1},P_{3,4},Q_{2,1},Q_{3,4},Q_{4,4}\}.
\]

For this 44-vertex graph,

\[
\delta^*=rac{43}{7},
\]

and an exact rational \(LDL^{\mathsf T}\) decomposition of \(7D+43I\) has
exactly one negative pivot and no zero pivot. Hence it is not a strict
counterexample.

Therefore

\[
oxed{
	ext{the universal Hoffman--Singleton vertex-deletion robustness radius is }5.
}
\]

**Status:** exact finite classification inside the full labelled deletion family;
proof audit and automorphism-provenance review queued.

---

# Part VII. Construction obstructions and negative controls

## 24. Prime-field diameter-three obstruction

For an odd prime \(q\ge7\) and \(1\le m\le q\), define the balanced layer graph
\(G(q,m)\) on \(2qm\) vertices by

\[
P_{i,j}\sim P_{i,j\pm1},\qquad
Q_{k,\ell}\sim Q_{k,\ell\pm2},\qquad
P_{i,j}\sim Q_{k,ik+j}.
\]

It is \((m+2)\)-regular and has girth at least five. Fourier decomposition under
translation in the second coordinate gives zero-mode eigenvalues

\[
m+2,\qquad 2-m,\qquad 2^{(2m-2)}.
\]

The strict WOW window reduces possible \(m\) to \(4,5,6\). A nonzero Fourier
block has an eigenvalue at least

\[
\sqrt m+\cosrac{\pi}{7}-rac12,
\]

which lies above the upper WOW boundary for \(m=4,5,6\). Therefore

\[
oxed{
q\ge7	ext{ prime and }\operatorname{diam}G(q,m)=3
\Longrightarrow G(q,m)	ext{ is not strict.}
}
\]

This closes a natural attempt to turn the Hoffman--Singleton coordinates into
an unconditional diameter-three infinite family.

**Status:** proved / exact; construction literature-established; proof audit
queued.

## 25. Layer-respecting perfect-matching deletions

For \(\pi\in S_5\), delete the perfect matching

\[
M_\pi=\{P_{i,j}Q_{\pi(i),\,i\pi(i)+j}:i,j\in\mathbb F_5\}
\]

from the Hoffman--Singleton graph. The resulting 120 graphs are 6-regular,
have girth five and diameter four. Explicit coordinate automorphisms split the
family into exactly two isomorphism orbits:

\[
20	ext{ affine permutations}\quad+\quad100	ext{ nonaffine permutations}.
\]

For the affine orbit,

\[
\lambda_D=-13,\qquad\Phi=-7.
\]

For the nonaffine orbit,

\[
\lambda_D=-6-\sqrt{61},\qquad\Phi=-\sqrt{61}.
\]

Thus all 120 members are exact negative controls. A natural order-50 regular
construction obtained by deleting one cross-layer perfect matching cannot
produce a counterexample.

**Status:** exact finite classification; proof audit and priority search queued.

---

# Part VIII. Derived low-degree windows

The new diameter bounds and the LP ceiling yield concise global restrictions.

## 26. Degree six

The audited edge-local theorem gives

\[
oxed{k=6\Longrightarrow n\le50.}
\]

## 27. Degree seven

Diameter four and larger are impossible. The diameter-two case is a Moore graph
and has order 50. In diameter three,

\[
n<B_7=rac{9\cdot52}{6}=78.
\]

A 7-regular graph has even order, hence

\[
oxed{
 k=7:\quad n=50	ext{ in diameter two, or }n\le76	ext{ in diameter three.}
}
\]

## 28. Degree eight

Diameter four and larger are impossible, and a degree-eight Moore graph is
excluded by the standard multiplicity integrality condition. The LP ceiling
gives \(n\le111\). If \(n=111\), the edge-local inequalities force every edge
to lie in exactly \(14\) five-cycles. Since

\[
|E|=rac{8\cdot111}{2}=444,
\]

edge--cycle incidence would give

\[
5N_5=14\cdot444=6216,
\]

which is impossible. Therefore

\[
oxed{k=8\Longrightarrow n\le110.}
\]

## 29. Degree nine

Diameter four and larger are impossible, and the diameter-two Moore
multiplicities are nonintegral. The LP ceiling gives

\[
n<B_9=rac{11\cdot84}{6}=154.
\]

A 9-regular graph has even order, so

\[
oxed{k=9\Longrightarrow n\le152.}
\]

These are corollaries of the current stack rather than independent principal
theorems.

---

# Part IX. Dependency graph and audit state

## 30. Logical dependencies

The principal dependency chain is

\[
	ext{girth-five local geometry}
\Longrightarrow
	ext{diameter-three operator identity}
\Longrightarrow
	ext{shifted spectral window}.
\]

From the shifted window branch three programmes emerge.

### Order-bound branch

\[
	ext{trace moments}
\Longrightarrow n<B_k
\Longrightarrow
	ext{LP optimality ceiling}.
\]

At degree six,

\[
n\le51
\Longrightarrow
	ext{edge-local cycle bounds}
\Longrightarrow n\le50
\Longrightarrow
	ext{order-50 feasibility system}.
\]

### Puncture branch

\[
	ext{Moore common-neighbour identity}
\Longrightarrow
	ext{structured distance-increase matrices}
\Longrightarrow
	ext{one-/two-vertex spectra and deletion stability}.
\]

The small-puncture normal form then supplies the metric and dual-degree layer
for arbitrary \(s\le k-1\), and exact automorphism orbit exhaustion gives the
Hoffman--Singleton radius-five theorem.

### Diameter branch

\[
	ext{endpoint-neighbourhood Rayleigh vector}
\Longrightarrow d\le4	ext{ for regular strict counterexamples},
\]

followed by the sharper diameter-four Rayleigh vector, which excludes
\(k\le9\).

## 31. Current proof-audit state

The edge-local order-51 exclusion has passed a dedicated audit after one
substantive theorem-scope correction. The following remain queued for separate
audits:

1. all-degree nonbacktracking LP ceiling;
2. nonadjacent Moore-puncture direct sum and factorisation;
3. regular degree-at-least-six theorem;
4. one-vertex and adjacent-edge Moore spectra;
5. order-50 local feasibility system;
6. layer-matching deletion classification;
7. prime-field obstruction;
8. Jørgensen equality control;
9. endpoint-neighbourhood diameter theorem;
10. diameter-four theorem;
11. small-puncture Moore normal form;
12. Hoffman--Singleton robustness-radius classification.

A green exact verifier is necessary but not sufficient for manuscript
promotion.

---

# Part X. Recommended v2 selection

A coherent v2 should not simply paste every result into one manuscript. The
strongest theorem narrative is:

1. the counterexample and diameter-three spectral mechanism;
2. regular counterexamples have degree at least six;
3. every regular strict counterexample has diameter at most four, with the
   diameter-four regime beginning only at degree ten;
4. the sharp all-degree ceiling of the standard one-point LP method;
5. the audited degree-six bound \(n\le50\);
6. the Moore-puncture normal form and the Hoffman--Singleton robustness radius.

The following are better placed in appendices or a companion note:

- full quartic and high-degree characteristic-polynomial factorizations;
- all order-50 moment matrices and the 266 surviving coarse profiles;
- the 120 matching-deletion negative controls;
- full automorphism orbit tables and LDL pivot ledgers;
- Lean implementation details beyond the precise formal-scope statement.

A possible manuscript theorem hierarchy is:

- **Theorem A:** explicit counterexamples and Moore threshold;
- **Theorem B:** diameter-three shifted-spectrum criterion;
- **Theorem C:** regular counterexamples have degree at least six and diameter
  at most four;
- **Theorem D:** exact LP ceiling \(n<B_k\);
- **Theorem E:** every degree-six regular strict counterexample has \(n\le50\);
- **Theorem F:** small Moore punctures and Hoffman--Singleton robustness radius
  five.

This selection would move the paper from an isolated disproof toward a
structural study of where failure can occur and how stable the principal
counterexample is.

---

# Part XI. Exact artifacts

The principal executable certificates are:

\[
egin{array}{l|l}
	ext{Result}&	ext{Entry point}\
\hline
	ext{base exact spectra}&	exttt{scripts/verify_exact.py}\
	ext{general structural extensions}&	exttt{scripts/verify_research_extensions_exact.py}\
	ext{regular degree }\ge6&	exttt{scripts/verify_regular_low_degree.py}\
	ext{nonadjacent puncture factorisation}&	exttt{scripts/verify_nonadjacent_punctured_moore.py}\
	ext{direct-sum audit}&	exttt{scripts/verify_nonadjacent_direct_sum.py}\
	ext{prime-field obstruction}&	exttt{scripts/verify_prime_field_obstruction.py}\
	ext{equality boundary}&	exttt{scripts/verify_equality_boundary.py}\
	ext{Jørgensen control}&	exttt{scripts/verify_jorgensen96_provenance.py}\
	ext{degree-six }n\le51&	exttt{scripts/verify_degree_six_gate.py}\
	ext{LP ceiling}&	exttt{scripts/verify_two_sided_lp_ceiling.py}\
	ext{edge-local }n\le50&	exttt{scripts/verify_edge_local_order50.py}\
	ext{matching deletions}&	exttt{scripts/verify_layer_matching_deletions.py}\
	ext{order-50 feasibility}&	exttt{scripts/verify_order50_local_feasibility.py}\
	ext{\(r=29\) exclusion}&	exttt{scripts/verify_order50_r29_exclusion.py}\
	ext{proof audit 01}&	exttt{scripts/verify_proof_audit_01_edge_local.py}\
	ext{diameter and puncture robustness}&	exttt{scripts/verify_diameter_puncture_extensions.py}
\end{array}
\]

The exact workflow rejects floating-point spectral decisions on every asserted
proof path.

---

# Part XII. Deliberate nonclaims

The current stack does **not** prove any of the following.

- Order 38 is the minimum order of a counterexample.
- No degree-six order-50 counterexample exists.
- Every six-vertex deletion of Hoffman--Singleton fails.
- A regular diameter-four counterexample exists.
- Every regular diameter-four graph satisfies WOW-284.
- The punctured-Moore spectra, LP dual certificate, diameter bounds, or
  robustness theorem have established literature priority.
- An unconditional infinite family of strict counterexamples exists.
- Exact computation or Lean checking substitutes for independent mathematical
  review of theorem statements and proof architecture.

These boundaries should remain explicit in any v2 manuscript and public
announcement.
