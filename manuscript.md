# Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284

**Samuil Petkov**<br>
Department of Physics, École normale supérieure, Université PSL, Paris, France<br>
<samuil.petkov@phys.ens.psl.eu><br>
> Reading copy generated from `main.tex`. The TeX source is authoritative if
> this rendering differs in notation, citations, or layout.

# Introduction

Let $`G`$ be a finite simple connected graph of order $`n=|V(G)|\ge2`$. Let $`A=A(G)`$ and $`D=D(G)`$ be its adjacency and distance matrices, let $`I`$ and $`J`$ denote the identity and all-ones matrices of order $`n`$, and let $`\mathbf 1`$ be the all-ones vector. Write $`d(v)`$ for the degree of $`v`$, $`N(v)`$ for its open neighbourhood, and, for $`S\subseteq V(G)`$, let $`G-S`$ denote the subgraph induced by $`V(G)\setminus S`$. Define
``` math
d^*(v)=\frac1{d(v)}\sum_{u\in N(v)}d(u),
 \qquad
 \delta^*(G)=\min_{v\in V(G)}d^*(v).
```
Thus $`D=(d_G(u,v))_{u,v\in V(G)}`$. Its eigenvalues are ordered as
``` math
\partial_1(G)\ge\cdots\ge\partial_n(G),
 \qquad \partial_n(G)=\lambda_{\min}(D(G)).
```
Aouchiche and Hansen record the following Graffiti conjecture as Conjecture 7.16 and attribute it to Fajtlowicz’s 1998 *Written on the Wall* report ([Fajtlowicz 1998](#ref-Fajtlowicz1998)) (see also ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16)).

<div class="wowconjecture">

**Conjecture (WOW-284)**. *If $`G`$ has order at least three and girth at least five, then
``` math
\delta^*(G)\le-\lambda_{\min}(D(G)).
```*

</div>

For graphs in the domain of the conjecture, put
``` math
\Phi(G)=\delta^*(G)+\lambda_{\min}(D(G)).
```
Thus $`G`$ is a strict counterexample precisely when $`\Phi(G)>0`$.

The initial disproof is short. A degree-$`k`$ Moore graph of diameter two has
``` math
A^2=(k-1)I-A+J,
 \qquad
 D=2J-2I-A,
```
and hence
``` math
\delta^*(G)=k,
 \qquad
 \lambda_{\min}(D)=-\frac{3+\sqrt{4k-3}}2.
```
The conjecture holds on these graphs exactly for $`k\le3`$, with equality at $`k=3`$, and fails for every realizable $`k>3`$. The degree-seven Hoffman–Singleton graph therefore gives a gap of three.

The purpose of this paper is not merely to list descendants of this graph. It addresses three structural questions.

1.  Which spectral mechanism governs regular counterexamples?

2.  How restrictive are the degree, diameter, and order conditions?

3.  How stable is the counterexample property under deletion?

Our main conclusions are as follows.

- In diameter three, WOW-284 is equivalent to a two-sided adjacency spectrum window centred at $`-1`$; see Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">6</a>.

- Every regular strict counterexample has degree at least six and diameter at most four. A diameter-four example, if one exists, has degree at least ten; see Theorems <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">10</a>, <a href="#thm:endpoint-diameter" data-reference-type="ref" data-reference="thm:endpoint-diameter">11</a>, and <a href="#thm:diameter-four" data-reference-type="ref" data-reference="thm:diameter-four">12</a>.

- The standard one-variable nonbacktracking linear-programming hierarchy has exact ceiling
  ``` math
  B_k=\frac{(k+2)(k^2+3)}6,
  ```
  with a unique optimizer up to positive scaling; see Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a>.

- For regular strict counterexamples of diameter three, the optimizer defines a positive-semidefinite slack matrix. Writing
  ``` math
  r=2(k+2)^2(k^2+3)-(12k+27)n,
  ```
  its integral excess satisfies $`r>0`$ and $`n\le3r`$, giving
  ``` math
  n\le\left\lfloor
   \frac{3(k+2)^2(k^2+3)}{18k+41}
   \right\rfloor;
  ```
  see Theorems <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">17</a> and <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">18</a>. Equality in the unrounded inequality is arithmetically rigid:
  ``` math
  (k,n,r)=(103,185220,61740);
  ```
  see Corollary <a href="#cor:three-to-one-equality" data-reference-type="ref" data-reference="cor:three-to-one-equality">19</a>. The same slack matrix’s $`2\times2`$ minors yield a general cycle-divisibility sieve and the local order-$`51`$ contradiction
  ``` math
  5N_5=153\cdot11=1683,
  ```
  where $`N_5`$ denotes the number of $`5`$-cycles. The global theorem gives the degree-$`7,8,9`$ order windows $`74,108,150`$; see Corollary <a href="#cor:low-degree-windows" data-reference-type="ref" data-reference="cor:low-degree-windows">24</a>.

- At the unresolved degree-six order-$`50`$ boundary, the integral signed-complement Gram matrix has rank at least $`30`$, and its underlying signed graph is disconnected; see Proposition <a href="#prop:order50-minus-two" data-reference-type="ref" data-reference="prop:order50-minus-two">25</a> and Theorem <a href="#thm:order50-disconnected" data-reference-type="ref" data-reference="thm:order50-disconnected">28</a>.

- One-vertex, adjacent-pair, and nonadjacent-pair deletions of Moore graphs admit exact invariant-subspace decompositions for their recomputed distance matrices; see Section <a href="#sec:punctures" data-reference-type="ref" data-reference="sec:punctures">7</a>.

- Every deletion of at most five vertices from the Hoffman–Singleton graph remains a strict counterexample, and this universal radius is sharp; see Theorem <a href="#thm:hs-radius" data-reference-type="ref" data-reference="thm:hs-radius">35</a>.

The proofs form two complementary hierarchies. In the obstruction direction, the distance-polynomial identity converts WOW-284 into a shifted adjacency window; scalar trace moments give the one-point LP ceiling; integrality of the optimal slack matrix strengthens the order bound; graph realizability and small Gram minors quantize the remaining excess into the three-to-one bound; edge-local $`2\times2`$ minors convert the same certificate into cycle counts; and $`3\times3`$ minors impose the two-path constraints at order fifty, where a signed-root representation forces a nontrivial component decomposition. In the stability direction, deleting vertices from a Moore graph produces an incidence-Gram correction to the distance matrix and a configuration-sensitive perturbation bound. Invariant-subspace decompositions then give exact puncture spectra, while orbitwise positive-definiteness certificates determine the sharp Hoffman–Singleton deletion radius.

The distance-polynomial viewpoint is established for minimal cages and distance-polynomial graphs ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022); [Fiol 2016](#ref-Fiol2016)). Nonbacktracking linear-programming bounds are due to Nozaki and related spectral-Moore work ([Nozaki 2015](#ref-Nozaki2015); [Cioabă et al. 2016](#ref-CioabaEtAl2016)). Our contribution is the specialization to the two-sided WOW window, the exact optimum for the admissible LP class of Section <a href="#sec:lp" data-reference-type="ref" data-reference="sec:lp">5</a>, the integral optimal-slack hierarchy, the edge-local cycle certificate, and the deletion theory developed below. We give an exact refutation of WOW-284 and a Lean 4.31 graph-level formalization of the $`50`$-vertex certificate. We do not claim that order $`38`$ is minimum or that the constructions classify all counterexamples.

The analytic arguments are proved in the text. Precisely specified finite classifications and matrix certificates are treated as computer-assisted proof components. Their exact reproducibility materials are archived with the accompanying release.

# Local growth, Moore graphs, and explicit counterexamples

## Dual degree as radius-two growth

For $`v\in V(G)`$, write $`\Gamma_i(v)`$ for the distance-$`i`$ sphere and $`B_2(v)=\Gamma_0(v)\cup\Gamma_1(v)\cup\Gamma_2(v)`$.

<div id="prop:radius-two" class="proposition">

**Proposition 1** (Second-degree identity). *If $`G`$ contains no triangle and no $`4`$-cycle, then
``` math
|B_2(v)|=1+\sum_{u\in N(v)}d(u),
 \qquad
 d^*(v)=\frac{|B_2(v)|-1}{d(v)}.
```*

</div>

<div class="proof">

*Proof.* For distinct neighbours $`u,w`$ of $`v`$, the sets $`N(u)\setminus\{v\}`$ and $`N(w)\setminus\{v\}`$ are disjoint; an intersection would form a $`4`$-cycle, and a member in $`N(v)`$ would form a triangle. These sets partition $`\Gamma_2(v)`$, so
``` math
|\Gamma_2(v)|=\sum_{u\in N(v)}(d(u)-1).
```
Adding the centre and first sphere proves the formula. This is the normalized form recorded in Backelin’s Lemma 2.1 ([Backelin 2015](#ref-Backelin2015)). ◻

</div>

## The Moore threshold

<div id="thm:moore-threshold" class="theorem">

**Theorem 2**. *Let $`M`$ be a degree-$`k`$ Moore graph of diameter two, $`k\ge2`$. Then
``` math
|V(M)|=k^2+1,
 \qquad g(M)=5,
 \qquad \delta^*(M)=k,
```
``` math
\lambda_{\min}(D(M))=-\frac{3+\sqrt{4k-3}}2,
```
and
``` math
\Phi(M)=k-\frac{3+\sqrt{4k-3}}2.
```
Thus $`M`$ satisfies WOW-284 exactly for $`k\le3`$, with equality exactly at $`k=3`$.*

</div>

<div class="proof">

*Proof.* The Moore bound is attained, so adjacent vertices have no common neighbour and nonadjacent vertices have exactly one. Given an edge $`uv`$, choose $`x\in N(u)\setminus\{v\}`$ and $`y\in N(v)\setminus\{u\}`$. The vertices $`x,y`$ are nonadjacent, since an edge would create a four-cycle, and their unique common neighbour completes a five-cycle through $`uv`$. Therefore
``` math
A^2=(k-1)I-A+J.
```
On $`\mathbf 1^\perp`$, the nonprincipal adjacency eigenvalues are the roots
``` math
r,s=\frac{-1\pm\sqrt{4k-3}}2.
```
If $`m_r,m_s`$ are their multiplicities, then
``` math
m_r+m_s=k^2,\qquad k+m_rr+m_ss=0.
```
Consequently
``` math
m_r=\frac{k(k\sqrt{4k-3}+k-2)}{2\sqrt{4k-3}},
 \qquad
 m_s=\frac{k(k\sqrt{4k-3}-k+2)}{2\sqrt{4k-3}},
```
and both roots occur. Every nonedge has distance two, hence $`D=2J-2I-A`$. The least distance eigenvalue is $`-2-r=-(3+\sqrt{4k-3})/2`$. Regularity gives $`\delta^*=k`$, and
``` math
(2k-3)^2-(4k-3)=4(k-1)(k-3)
```
gives the threshold. The exact scalar and finite checks are independently repeated by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_regular_score_calculus.py). ◻

</div>

## A coordinate Hoffman–Singleton certificate

All subscripts below lie in $`\mathbb F_5=\mathbb Z/5\mathbb Z`$. Let
``` math
V(M)=\{P_{i,j}:i,j\in\mathbb F_5\}\mathbin{\dot\cup}
      \{Q_{k,\ell}:k,\ell\in\mathbb F_5\},
```
with edges
``` math
\begin{align*}
 P_{i,j}&\sim P_{i,j\pm1},\\
 Q_{k,\ell}&\sim Q_{k,\ell\pm2},\\
 P_{i,j}&\sim Q_{k,ik+j}.
\end{align*}
```
This is Hafner’s affine-coordinate form of the Hoffman–Singleton graph after a minor reindexing ([Hafner 2003](#ref-Hafner2003)).

<div id="prop:hs-coordinate" class="proposition">

**Proposition 3**. *The coordinate construction is a simple connected $`7`$-regular graph on $`50`$ vertices. Adjacent pairs have no common neighbour and nonadjacent pairs have exactly one. Consequently it has girth five, diameter two, and
``` math
\operatorname{Spec}D(M)=\{91^{(1)},1^{(21)},(-4)^{(28)}\}.
```
In particular, $`\delta^*(M)=7`$ and $`\Phi(M)=3`$.*

</div>

<div class="proof">

*Proof.* The neighbourhoods are
``` math
\begin{align*}
N(P_{i,j})&=\{P_{i,j-1},P_{i,j+1}\}
 \cup\{Q_{k,ik+j}:k\in\mathbb F_5\},\\
N(Q_{k,\ell})&=\{Q_{k,\ell-2},Q_{k,\ell+2}\}
 \cup\{P_{i,\ell-ik}:i\in\mathbb F_5\}.
\end{align*}
```
They have seven distinct entries. For two $`P`$-vertices in the same layer, the $`5`$-cycle gives no common neighbour when they are adjacent and exactly one when they are nonadjacent; a common $`Q`$-neighbour would force their second coordinates to agree. In distinct $`P`$-layers, a common $`Q`$-neighbour is determined uniquely by $`(i-i')k=j'-j`$. The $`Q`$-cases are identical, with the same-layer $`5`$-cycle generated by steps $`\pm2`$ and, in distinct layers, a unique common $`P`$-neighbour. For a cross pair $`P_{i,j},Q_{k,\ell}`$, put $`r=\ell-(ik+j)`$. The pair is adjacent for $`r=0`$, has one common $`P`$-neighbour for $`r\in\{\pm1\}`$, and one common $`Q`$-neighbour for $`r\in\{\pm2\}`$. The five residues are exhausted. The claimed geometry now follows from Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2</a>. At $`k=7`$, the multiplicity equations in its proof give adjacency multiplicities $`28`$ at $`2`$ and $`21`$ at $`-3`$, and hence the displayed distance spectrum. The exhaustive pair certificate, integer BFS distances, characteristic polynomial, and exact positive-definiteness check are in [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_exact.py). ◻

</div>

## Smaller exact counterexamples

Let
``` math
\mathcal P=\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}.
```
The induced graph $`M[\mathcal P]`$ is a Petersen graph. Put
``` math
R=M-\mathcal P,
 \quad H_{39}=R-P_{1,0},
 \quad H_{38}=R-\{P_{1,0},P_{1,1}\},
```
and let $`X_{42}`$ be the second subconstituent of $`P_{0,0}`$, namely the graph induced by the vertices at distance two from it.

<div id="thm:explicit-examples" class="theorem">

**Theorem 4**. *The following are strict counterexamples.
``` math
\begin{array}{c@{\quad}c@{\quad}c@{\quad}c}
\toprule
G&|V(G)|&\delta^*(G)&\lambda_{\min}(D(G))\\
\midrule
H_{38}&38&17/3&-3-\sqrt7\\
H_{39}&39&35/6&>-35/6\\
R&40&6&-5\\
X_{42}&42&6&-5\\
M&50&7&-4\\
\bottomrule
\end{array}
```
The entry for $`H_{39}`$ records an exact strict lower bound obtained from positive definiteness of $`6D+35I`$; it is not a decimal approximation to the least eigenvalue. Moreover, all $`40`$ labelled singleton deletions of $`R`$, and all $`120`$ labelled deletions of the endpoints of an edge of $`R`$, are strict counterexamples with the same respective characteristic polynomials.*

</div>

<div class="proof">

*Proof.* The graph $`R`$ is the classical $`(6,5)`$-cage of O’Keefe and Wong ([O’Keefe and Wong 1979](#ref-OKeefeWong1979); [Wong 1979](#ref-Wong1979)); its realization as a Petersen deletion of the Hoffman–Singleton graph also appears in ([Klin et al. 2009, 262–63](#ref-KlinMuzychukZivAv2009)). The Moore block identity gives
``` math
\operatorname{Spec}A(R)=\{6^{(1)},2^{(18)},1^{(4)},(-2)^{(5)},(-3)^{(12)}\},
```
and Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">6</a> below maps this to
``` math
\operatorname{Spec}D(R)=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}.
```
The second-subconstituent calculation gives
``` math
\operatorname{Spec}D(X_{42})=\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\}.
```
The classical second-subconstituent identification and adjacency spectrum are recorded in ([Dam and Haemers 2003](#ref-vanDamHaemers2003), Table 3, p. 265). For $`H_{38}`$, a direct degree count gives $`\delta^*=17/3`$, while the factor $`x^2+6x+2`$, together with an exact Sturm isolation, gives the least root $`-3-\sqrt7`$. For $`H_{39}`$, the exact matrix $`6D+35I`$ is positive definite. All graph, girth, distance, dual-degree, Sturm, and rational $`LDL^{\mathsf T}`$ certificates are checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_extended.py). More explicitly, for every $`v\in V(R)`$,
``` math
\begin{align*}
\det(xI-D(R-v))=P_{39}(x):={}&x^9(x+5)^{12}(x^2+6x+3)\\
&\cdot(x^3+3x^2-15x-7)^2(x^3+3x^2-15x-3)^2\\
&\cdot(x^4-78x^3+303x^2-70x-450),
\end{align*}
```
whereas for every $`uv\in E(R)`$,
``` math
\begin{align*}
\det(xI-D(R-\{u,v\}))=P_{38}(x):={}&x^4(x-2)(x+5)^8(x^2+6x+2)^2\\
&\cdot(x^3+3x^2-15x-3)\\
&\cdot(x^4+5x^3-7x^2-23x-6)\\
&\cdot(x^5+9x^4+7x^3-77x^2-54x-4)\\
&\cdot(x^9-67x^8-404x^7+1772x^6+7205x^5\\
&\hspace{3em}-18489x^4-17018x^3+20288x^2+16824x+1680).
\end{align*}
```
The labelled deletion families are exhausted by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_descendant_families.py). No transitivity or numerical root ordering is used. Fixed graph6, adjacency-list, edge-list, and distance-matrix records are provided in `data/graphs/`. ◻

</div>

<div id="thm:second-subconstituent" class="theorem">

**Theorem 5** (Moore second subconstituents). *Let $`M`$ be a degree-$`K`$ Moore graph of diameter two, $`K\ge3`$, and let $`X`$ be the graph induced by $`\Gamma_2(v)`$ for a fixed vertex $`v`$. Then $`X`$ has order $`K(K-1)`$, degree $`K-1`$, girth at least five, diameter three, and
``` math
\lambda_{\min}(D(X))=-\frac{5+\sqrt{4K-3}}2.
```
Consequently
``` math
\Phi(X)=K-1-\frac{5+\sqrt{4K-3}}2,
```
which is positive exactly for integers $`K\ge6`$.*

</div>

<div class="proof">

*Proof.* Relative to $`\{v\}\sqcup N(v)\sqcup\Gamma_2(v)`$, write the adjacency matrix with incidence block $`C`$ and induced block $`B`$. The Moore identity gives
``` math
CC^{\mathsf T}=(K-1)I,
 \qquad CB=J-C,
```
and on $`\ker C`$,
``` math
B^2+B-(K-1)I=0.
```
Since $`CC^{\mathsf T}=(K-1)I`$, the map $`C^{\mathsf T}`$ is injective, its image is orthogonal to $`\ker C`$, and
``` math
\mathbb R^{\Gamma_2(v)}
 =\langle\mathbf 1\rangle\perp C^{\mathsf T}(\mathbf 1^\perp)\perp\ker C.
```
Thus $`B`$ has principal eigenvalue $`K-1`$, eigenvalue $`-1`$ on $`C^{\mathsf T}(\mathbf 1^\perp)`$, and the two Moore roots $`r,s=(-1\pm\sqrt{4K-3})/2`$ on $`\ker C`$. Moreover,
``` math
\dim\ker C=K(K-2),\qquad \operatorname{tr}(B|_{\ker C})=0.
```
Indeed, the principal eigenvalue $`K-1`$ cancels the $`K-1`$ copies of $`-1`$ in the trace. Hence the root multiplicities $`p,q`$ satisfy
``` math
p+q=K(K-2),\qquad pr+qs=0,
```
so
``` math
p=\frac{K(K-2)(1+\sqrt{4K-3})}{2\sqrt{4K-3}},
 \qquad
 q=\frac{K(K-2)(\sqrt{4K-3}-1)}{2\sqrt{4K-3}}.
```
Both roots therefore occur. It remains to identify the diameter of $`X`$. If the unique common neighbour in $`M`$ of two nonadjacent vertices $`x,y\in X`$ lies in $`X`$, their distance in $`X`$ is two. Otherwise it is their common parent in $`N(v)`$. Choose $`b\in N_X(x)`$. Then $`b\not\sim y`$, and the unique common neighbour $`c`$ of $`b,y`$ belongs to $`X`$: it cannot be $`v`$, and it cannot lie in $`N(v)`$, since $`b`$ and $`y`$ have different parents there. Thus $`x-b-c-y`$ is a path in $`X`$. Pairs with a common parent have no length-two path in $`X`$, so $`X`$ has diameter three and Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">6</a> applies. Among the nonprincipal adjacency eigenvalues, $`(-1+\sqrt{4K-3})/2`$ maximizes $`|\theta+1|`$; substitution gives
``` math
\lambda_{\min}(D(X))=-\frac{5+\sqrt{4K-3}}2.
```
For $`K=3,4,5`$, direct comparison gives a nonpositive score. For $`K\ge6`$, both sides of the relevant comparison are positive, and the threshold reduces to
``` math
(2K-7)^2-(4K-3)=4(K^2-8K+13)>0
```
because $`K>4+\sqrt3`$. The finite $`K=7`$ instance is checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_wow284_38_40_42.py). ◻

</div>

# The regular score calculus

<div id="thm:diameter-three-score" class="theorem">

**Theorem 6** (Diameter-three score formula). *Let $`G`$ be connected, $`k`$-regular, of girth at least five and diameter three, with adjacency matrix $`A`$ and order $`n`$. Then
``` math
D=3J+(k-3)I-2A-A^2,
```
``` math
D+kI=3J+(2k-2)I-(A+I)^2.
```
The principal distance eigenvalue is $`3n-k^2-k-3`$, and a nonprincipal adjacency eigenvalue $`\theta`$ gives the distance eigenvalue
``` math
\mu(\theta)=k-2-(\theta+1)^2.
```
Consequently
``` math
\boxed{
 \Phi(G)=2k-2-\max_{\theta\ne k}(\theta+1)^2.
 }
```
Thus $`G`$ is a strict counterexample exactly when
``` math
|\theta+1|<\sqrt{2k-2}
 \qquad(\theta\ne k).
```*

</div>

<div class="proof">

*Proof.* Girth at least five gives the distance-two matrix $`A_2=A^2-kI`$, and diameter three gives $`A_3=J-I-A-A_2`$. Substitute in $`D=A+2A_2+3A_3`$. On $`\mathbf 1^\perp`$, $`J`$ vanishes, and regularity gives $`\delta^*=k`$. The principal distance eigenvalue is positive and is the Perron root because every off-diagonal entry of $`D`$ is positive. The exact operator and score identities are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_regular_score_calculus.py). ◻

</div>

<div id="cor:bipartite" class="corollary">

**Corollary 7** (Bipartite obstruction). *A connected $`k`$-regular bipartite graph of girth at least five and diameter three is not a strict counterexample for $`k\ge3`$.*

</div>

<div class="proof">

*Proof.* The nonprincipal eigenvalue $`-k`$ satisfies
``` math
(-k+1)^2-(2k-2)=(k-1)(k-3)\ge0
 \qquad(k\ge3).
```
Thus the required strict inequality fails, with equality exactly at $`k=3`$. ◻

</div>

<div id="prop:higher-transfer" class="proposition">

**Proposition 8** (Higher-diameter transfer). *Let $`G`$ be connected and $`k`$-regular, with diameter $`d`$ and girth at least $`2d-1`$. Let $`A_i`$ denote the distance-$`i`$ matrix, and define
``` math
F_0=1,
 \quad F_1=x,
 \quad F_2=x^2-k,
 \quad F_i=xF_{i-1}-(k-1)F_{i-2}\quad(i\ge3).
```
Then $`A_i=F_i(A)`$ for $`0\le i\le d-1`$, and
``` math
D=dJ+q_d(A),
 \qquad
 q_d(x)=\sum_{i=0}^{d-1}(i-d)F_i(x).
```
In particular,
``` math
q_3(x)=k-3-2x-x^2,
```
``` math
q_4(x)=-x^3-2x^2+(2k-4)x+2k-4.
```*

</div>

<div class="proof">

*Proof.* Up to length $`d-1`$, the girth condition makes nonbacktracking walks between two vertices unique exactly when their length is the graph distance. Hence the distance-$`i`$ matrices are the nonbacktracking polynomials in $`A`$; summing $`D=\sum_{i=0}^d iA_i`$ and eliminating $`A_d`$ with $`J=\sum_{i=0}^d A_i`$ proves the formula. This lies within the established distance-polynomial framework ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022); [Fiol 2016](#ref-Fiol2016)). ◻

</div>

# Degree and diameter obstructions

<div id="lem:diam-rayleigh" class="lemma">

**Lemma 9**. *For every connected graph,
``` math
\lambda_{\min}(D(G))\le-\operatorname{diam}(G).
```*

</div>

<div class="proof">

*Proof.* For a diametral pair $`u,v`$, the Rayleigh quotient of $`e_u-e_v`$ is $`-d_G(u,v)`$. ◻

</div>

<div id="thm:regular-degree-six" class="theorem">

**Theorem 10**. *Every connected regular strict counterexample to WOW-284 has degree at least six.*

</div>

<div class="proof">

*Proof.* We use the LP ceiling proved independently in Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a>; that theorem does not depend on the present degree reduction. Let the degree be $`k`$. Lemma <a href="#lem:diam-rayleigh" data-reference-type="ref" data-reference="lem:diam-rayleigh">9</a> and strictness give $`\operatorname{diam}(G)<k`$. If $`k\le2`$, then $`|V(G)|\ge3`$ and connectedness give $`\operatorname{diam}(G)\ge2\ge k`$, a contradiction. For $`k=3`$, the radius-two lower bound and $`\operatorname{diam}(G)\le2`$ force equality in the Moore bound. Hence $`G`$ is a degree-three Moore graph, and Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2</a> gives $`\Phi(G)=0`$, not $`\Phi(G)>0`$.

For $`k=4`$, diameter two would require a degree-four Moore graph, whose adjacency multiplicities are nonintegral. In diameter three, the exact LP bound of Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a> gives $`n<19`$, whereas the radius-two ball has $`17`$ vertices and diameter three requires at least one more. Hence $`n=18`$. The distance-three matrix is then a perfect matching. Its $`-1`$-eigenspace $`W`$ is a nine-dimensional rational subspace of $`\mathbf 1^\perp`$, and
``` math
A_3=J+3I-A-A^2
 \quad\Longrightarrow\quad
 (A^2+A-4I)|_W=0.
```
The polynomial $`x^2+x-4`$ is irreducible over $`\mathbb Q`$, so a rational space on which it annihilates an operator has even dimension, a contradiction.

For $`k=5`$, diameter two again fails the Moore multiplicity condition. A diametral geodesic in diameter four yields the principal submatrix $`D(P_5)`$, whose factor $`x^2+6x+4`$ supplies the eigenvalue $`-3-\sqrt5<-5`$; Cauchy interlacing excludes this case. In diameter three, Meringer’s lower bound and Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a> leave $`n\in\{30,31,32\}`$. Since $`5n=2|E(G)|`$, one has $`n\equiv0\pmod2`$, so $`n\in\{30,32\}`$. At $`n=32`$, the distance layers about a vertex have sizes $`1,5,20,6`$. Write $`a`$ for the average internal degree of the distance-two layer. Each of its vertices has one neighbour in the first layer, so the number of edges from the second to the third layer is $`20(4-a)\le6\cdot5`$; hence $`a\ge5/2`$. On normalized layer indicators, the symmetric adjacency compression is
``` math
Q(a)=
 \begin{pmatrix}
 0&\sqrt5&0&0\\
 \sqrt5&0&2&0\\
 0&2&a&(4-a)\sqrt{10/3}\\
 0&0&(4-a)\sqrt{10/3}&5-\frac{10}{3}(4-a)
 \end{pmatrix}.
```
The derivative of its only $`a`$-dependent block is
``` math
\begin{pmatrix}1&-\sqrt{10/3}\\-\sqrt{10/3}&10/3\end{pmatrix}
 =
 \begin{pmatrix}1\\-\sqrt{10/3}\end{pmatrix}
 \begin{pmatrix}1&-\sqrt{10/3}\end{pmatrix}\succeq0.
```
Thus every ordered eigenvalue of $`Q(a)`$ is nondecreasing in $`a`$. At the smallest feasible value,
``` math
\chi_{Q(5/2)}(x)=\frac14(x-5)p_{5,6}(x),
 \qquad
 p_{5,6}(x)=4x^3+10x^2-16x-30,
 \qquad p_{5,6}(11/6)=-29/27<0.
```
Because the leading coefficient is positive, the largest root $`\mu_2`$ of the nonprincipal factor exceeds $`11/6>-1+\sqrt8`$. Cauchy interlacing gives $`\theta_2(A)\ge\mu_2`$, contradicting the necessary bound $`\theta<-1+\sqrt8`$. At $`n=30`$, Meringer’s isomorph-free enumeration leaves exactly four $`(5,5)`$-cages ([Meringer 1999, 142](#ref-Meringer1999)); each fixed record has an exact distance eigenvalue at most $`-5`$. The accompanying release contains an independent exact audit of the complete case split and the four fixed graph6 records. ◻

</div>

<div id="thm:endpoint-diameter" class="theorem">

**Theorem 11** (Endpoint-neighbourhood obstruction). *Let $`G`$ be any connected finite simple graph, and let $`u,v`$ be vertices at distance $`\ell=d_G(u,v)\ge5`$. Put $`p=d(u)`$ and $`q=d(v)`$. Then
``` math
\boxed{
 \lambda_{\min}(D(G))
 \le p+q-2-\sqrt{(p-q)^2+pq(\ell-2)^2}.
 }
```
If $`\delta`$ is the ordinary minimum degree, then
``` math
\boxed{
 \lambda_{\min}(D(G))\le-\delta(\ell-4)-2.
 }
```
Consequently every strict WOW-284 counterexample satisfies
``` math
\Delta>\delta(\ell-4)+2,
```
where $`\Delta`$ is the ordinary maximum degree. In particular, every regular strict counterexample has diameter at most four.*

</div>

<div class="proof">

*Proof.* The two endpoint neighbourhoods are disjoint. Give weight $`a>0`$ to $`N(u)`$, weight $`-b<0`$ to $`N(v)`$, and zero elsewhere. Within one neighbourhood distances are at most two; between the two neighbourhoods they are at least $`\ell-2`$. Since the cross products are negative, the Rayleigh quotient is at most that of
``` math
\begin{pmatrix}
 2(p-1)&-(\ell-2)\sqrt{pq}\\
 -(\ell-2)\sqrt{pq}&2(q-1)
 \end{pmatrix}.
```
Its least eigenvalue is the first displayed bound, and its least eigenvector can be chosen with both coordinates positive. Write $`p=\delta+\alpha`$, $`q=\delta+\beta`$, and $`t=\ell-2`$. The identity
``` math
(p-q)^2+pqt^2-(p+q+\delta(t-2))^2
 =(t-2)\{\delta t(\alpha+\beta)+(t+2)\alpha\beta\}
```
is nonnegative and gives the second bound. Finally $`\delta^*(G)\le\Delta`$. The sign choice, radical comparison, and integer rounding are independently audited by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_10_endpoint_diameter.py). ◻

</div>

<div id="thm:diameter-four" class="theorem">

**Theorem 12** (Diameter four). *Let $`G`$ be connected, $`k`$-regular, of girth at least five and diameter four. Then
``` math
\boxed{
 \lambda_{\min}(D(G))\le-\frac{7+\sqrt{16k+1}}2.
 }
```
Consequently no such graph of degree $`2\le k\le9`$ is a strict counterexample.*

</div>

<div class="proof">

*Proof.* Choose $`u,v`$ at distance four and put $`U=N(u)`$, $`V=N(v)`$. For fixed $`a\in U`$, distinct vertices $`b,b'\in V`$ at distance two from $`a`$ cannot use the same common neighbour, or a $`4`$-cycle results. Thus at most $`k(k-1)`$ pairs in $`U\times V`$ have distance two, and
``` math
\sum_{a\in U,b\in V}d_G(a,b)\ge2k^2+k.
```
Assign weights $`\alpha,\beta,-\alpha,-\beta`$ to $`u,U,v,V`$, respectively. Counting unordered pairs and then doubling gives
``` math
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
 \le
 \frac{-4\alpha^2-4k\alpha\beta-3k\beta^2}
 {\alpha^2+k\beta^2}.
```
After setting $`y_1=\alpha`$ and $`y_2=\sqrt{k}\,\beta`$, the right-hand side is the Rayleigh quotient of
``` math
\begin{pmatrix}-4&-2\sqrt{k}\\-2\sqrt{k}&-3\end{pmatrix},
```
whose least eigenvalue is the displayed value and has a positive-coordinate minimizer. The strict comparison with $`-k`$ holds for $`2\le k\le9`$. Every orientation factor, cross-distance sign, and endpoint comparison is independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_11_diameter_four.py). ◻

</div>

<div id="cor:trichotomy" class="corollary">

**Corollary 13** (Regular trichotomy). *Every regular strict counterexample has one of the following forms:*

1.  *diameter two, hence a Moore graph;*

2.  *diameter three, with $`\lvert\theta+1\rvert<\sqrt{2k-2}`$ for every nonprincipal adjacency eigenvalue $`\theta`$;*

3.  *diameter four, with degree at least ten.*

*There are no regular strict counterexamples of diameter at least five.*

</div>

# Moment bounds and the exact LP ceiling

Let $`G`$ satisfy the hypotheses of Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">6</a>, and write its nonprincipal adjacency eigenvalues as $`\theta_i`$. Put $`y_i=\theta_i+1`$.

<div id="prop:moment-bound" class="proposition">

**Proposition 14** (Fourth-moment identity). *One has
``` math
\sum_{i=1}^{n-1}(2k-2-y_i^2)(y_i+1)^2
 =(k+2)\bigl((k+2)(k^2+3)-6n\bigr).
```
Every strict counterexample therefore satisfies
``` math
\boxed{
 n< B_k:=\frac{(k+2)(k^2+3)}6.
 }
```*

</div>

<div class="proof">

*Proof.* Use
``` math
\operatorname{tr}A=\operatorname{tr}A^3=0,
 \quad \operatorname{tr}A^2=nk,
 \quad \operatorname{tr}A^4=nk(2k-1),
```
remove the principal eigenvalue, and expand both sides. In a strict counterexample, each factor $`2k-2-y_i^2`$ is positive. The sum cannot vanish: otherwise every nonprincipal adjacency eigenvalue would equal $`-2`$, and $`\operatorname{tr}A=0`$ would give $`k-2(n-1)=0`$, or $`n=(k+2)/2`$, incompatible with the elementary bound $`n\ge k+1`$ for a simple $`k`$-regular graph. The identity is checked symbolically by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_degree_six_gate.py) and independently within [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_02_two_sided_lp.py). ◻

</div>

The preceding bound is optimal within the one-variable nonbacktracking admissible class defined below.

<div class="definition">

**Definition 15**. Let $`F_i=F_i^{(k)}`$ be the nonbacktracking polynomials from Proposition <a href="#prop:higher-transfer" data-reference-type="ref" data-reference="prop:higher-transfer">8</a>, and set
``` math
I_k=[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
```
A finite polynomial $`f=\sum_i f_iF_i`$ is *admissible* if
``` math
f_0>0,
 \qquad f_i\ge0\quad(i\ge5),
 \qquad f(x)\le0\quad(x\in I_k).
```

</div>

For a $`k`$-regular graph of girth at least five whose nonprincipal spectrum lies in $`I_k`$, one has $`\operatorname{tr}F_i(A)=0`$ for $`1\le i\le4`$, while $`\operatorname{tr}F_i(A)\ge0`$ for $`i\ge5`$, since these traces count closed nonbacktracking walks. The coefficient conditions therefore give $`nf_0\le\operatorname{tr}f(A)`$. On the other hand, $`f(\theta)\le0`$ for every nonprincipal eigenvalue, so $`\operatorname{tr}f(A)\le f(k)`$. Thus
``` math
nf_0\le\operatorname{tr}f(A)\le f(k),
 \qquad n\le\frac{f(k)}{f_0}.
```

<div id="thm:lp-ceiling" class="theorem">

**Theorem 16** (Exact LP ceiling and rigidity). *For every integer $`k\ge4`$ and every admissible $`f`$,
``` math
\boxed{
 \frac{f(k)}{f_0}\ge B_k=\frac{(k+2)(k^2+3)}6.
 }
```
Equality holds if and only if $`f`$ is a positive scalar multiple of
``` math
\boxed{
 f_*(x)=\frac{(x+2)^2(x^2+2x-(2k-3))}{6(k+2)}.
 }
```
Thus increasing the polynomial degree cannot improve this one-variable LP bound. Consequently, any connected $`k`$-regular graph of girth at least five whose nonprincipal spectrum lies in the interior of $`I_k`$ satisfies $`n<B_k`$.*

</div>

<div class="proof">

*Proof.* The primal expansion is
``` math
\begin{aligned}
6(k+2)f_*(x)={}&6(k+2)F_0(x)+2(2k+7)F_1(x)\\
&+(k+13)F_2(x)+6F_3(x)+F_4(x).
\end{aligned}
```
On $`I_k`$, the factor $`(x+1)^2-(2k-2)`$ is nonpositive, while $`(x+2)^2\ge0`$; hence $`f_*`$ is admissible and $`f_*(k)=B_k`$.

For the dual certificate, put $`\Delta=\sqrt{2k-2}`$, $`\xi_\pm=-1\pm\Delta`$, and $`\xi_0=-2`$. Define
``` math
\begin{align*}
w_-&=\frac{k(k+2)(2k^2-6-3(k-1)\Delta)}{24(2k-3)},\\
w_0&=\frac{k(k-1)(k^2+3)}{6(2k-3)},\\
w_+&=\frac{k(k+2)(2k^2-6+3(k-1)\Delta)}{24(2k-3)}.
\end{align*}
```
$`w_-,w_0,w_+>0`$. For the only nontrivial inequality, this follows from
``` math
(2k^2-6)^2-18(k-1)^3
 =2(k-3)(2k-3)(k^2+3)>0.
```
The measure $`\mu=w_-\delta_{\xi_-}+w_0\delta_{\xi_0}+w_+\delta_{\xi_+}`$ satisfies
``` math
\mu(1)=B_k-1,
 \qquad \mu(F_i)=-F_i(k)\quad(1\le i\le4).
```
For $`i\ge5`$, the slack $`a_i=\mu(F_i)+F_i(k)`$ is strictly positive. For $`5\le i\le9`$, exact calculation gives, after removing the common positive factor $`k(k-1)(k+2)(k^2+3)/6`$, respectively,
``` math
2,\quad 5k-13,\quad 2(3k^2-17k+25),
```
``` math
6k^3-47k^2+139k-150,
 \quad
 2(3k^4-27k^3+106k^2-219k+194),
```
all positive for $`k\ge4`$; for the nontrivial residual factors this follows after writing $`k=m+4`$, when all coefficients are nonnegative and the constant terms are positive. For $`i\ge10`$, put $`r=k-1\ge3`$. The support lies in $`[-2\sqrt r,2\sqrt r]`$, because $`1+\sqrt{2r}\le2\sqrt r`$. For $`|z|\le1`$, the recurrence gives
``` math
F_i(2\sqrt r\,z)
 =r^{i/2}U_i(z)-r^{(i-2)/2}U_{i-2}(z),
```
where $`U_j`$ is the Chebyshev polynomial of the second kind. Using $`|U_j(z)|\le j+1`$ yields
``` math
\frac{|\mu(F_i)|}{F_i(k)}
 \le \frac{2i+1}{3}\,3^{3-i/2}.
```
At $`i=10`$ the right-hand side is $`7/9`$, and it decreases thereafter because $`3(2i+1)^2-(2i+3)^2=8i^2-6>0`$. Hence
``` math
\frac{|\mu(F_i)|}{F_i(k)}<1\qquad(i\ge10).
```
Expanding in the nonbacktracking basis gives
``` math
\int f\,d\mu
 =B_kf_0-f(k)+\sum_{i\ge5}f_i a_i
 \ge B_kf_0-f(k).
```
Since $`f\le0`$ on $`\operatorname{supp}\mu`$, $`\int f\,d\mu\le0`$, which proves weak duality. If equality holds, strict positivity of every high-degree slack forces $`f_i=0`$ for $`i\ge5`$. Equality on the positive dual support forces zeros at $`\xi_-,-2,\xi_+`$; the interior zero $`-2`$ has even multiplicity because $`f\le0`$ on $`I_k`$. Degree at most four then forces $`f`$ to be a scalar multiple of $`f_*`$, and $`f_0>0`$ makes the scalar positive. Equality in the graph bound would then force every nonprincipal adjacency eigenvalue to be $`-2`$, which contradicts the trace equation; hence the open-window bound is strict. Every symbolic identity, finite slack, tail bound, and equality-nullspace calculation is independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_02_two_sided_lp.py). ◻

</div>

<div id="thm:integral-slack" class="theorem">

**Theorem 17** (Integral optimal-slack bound). *Let $`G`$ be connected and $`k`$-regular with $`k\ge4`$, of girth at least five and diameter three, and suppose
``` math
\lvert\theta+1\rvert<\sqrt{2k-2}
 \qquad(\theta\ne k)
```
for every adjacency eigenvalue $`\theta`$. Define
``` math
g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),\quad
 C_k=(k+2)^2(k^2+3),\quad h_k=6(k+2),
```
``` math
\mathcal S_k=-g_k(A)+\frac{C_k}{n}J.
```
Then
``` math
\mathcal S_k\succeq0,\qquad
 \mathcal S_k\mathbf 1=0,\qquad
 \operatorname{tr}\mathcal S_k=h_k(B_k-n).
```
Moreover,
``` math
\mathcal E_k=g_k(A)-(h_k+1)J+I
```
is a nonzero, symmetric, entrywise nonnegative integral matrix with zero diagonal and constant row sum
``` math
\varepsilon_{k,n}=C_k-(h_k+1)n+1.
```
On $`\mathbf 1^\perp`$, one has $`\mathcal S_k=I-\mathcal E_k`$. In particular,
``` math
\boxed{
 n\le
 \left\lfloor
 \frac{(k+2)^2(k^2+3)}{6(k+2)+1}
 \right\rfloor.
 }
```*

</div>

<div class="proof">

*Proof.* The polynomial $`g_k=6(k+2)f_*`$ is the optimal LP polynomial from Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a>. Thus $`\mathcal S_k`$ vanishes on $`\langle\mathbf 1\rangle`$, while on a nonprincipal $`\theta`$-eigenspace its eigenvalue is
``` math
\bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2\ge0.
```
The nonbacktracking expansion of $`g_k`$ has constant coefficient $`h_k`$. Girth at least five gives $`(F_i(A))_{uu}=0`$ for every $`u`$ and $`1\le i\le4`$, and hence
``` math
\operatorname{tr}\mathcal S_k=C_k-h_kn=h_k(B_k-n),
 \qquad (g_k(A))_{uu}=h_k.
```

Put $`z_{uv}=(g_k(A))_{uv}\in\mathbb Z`$ for $`u\ne v`$, and set $`a=C_k/n-h_k=(\mathcal S_k)_{uu}`$. The $`2\times2`$ principal minor on $`\{u,v\}`$ gives
``` math
\left|\frac{C_k}{n}-z_{uv}\right|\le a.
```
Equality on the upper side would give $`(e_u-e_v)^{\mathsf T}\mathcal S_k(e_u-e_v)=0`$, hence $`e_u-e_v\in\ker\mathcal S_k`$. The strict spectral window gives
``` math
\ker\mathcal S_k=\langle\mathbf 1\rangle\oplus E_{-2}(A).
```
Since $`e_u-e_v\perp\mathbf 1`$, it would be a $`(-2)`$-eigenvector of $`A`$. Yet the $`u`$-coordinate of $`A(e_u-e_v)`$ is $`-1`$ if $`u\sim v`$ and $`0`$ otherwise, never $`-2`$. Therefore
``` math
z_{uv}\ge h_k+1.
```
It follows directly that $`\mathcal E_k`$ has the stated entrywise properties, and $`g_k(A)\mathbf 1=C_k\mathbf 1`$ gives its row sum. The identity on $`\mathbf 1^\perp`$ follows by eliminating $`J`$.

It remains to prove $`\mathcal E_k\ne0`$. Otherwise
``` math
g_k(A)=(h_k+1)J-I,
```
so $`p_k(A)=0`$ on $`\mathbf 1^\perp`$, where $`p_k(x)=g_k(x)+1`$. After $`y=x+2`$,
``` math
p_k(y-2)=y^4-2y^3+(3-2k)y^2+1.
```
This polynomial is irreducible over $`\mathbb Q`$. Its only possible rational roots are $`\pm1`$, whose values are $`3-2k`$ and $`7-2k`$. A factorization into monic integer quadratics would have constant terms both $`1`$ or both $`-1`$; these alternatives force the cubic and linear coefficients to be, respectively, equal or opposite, whereas they are $`-2`$ and $`0`$.

Rational canonical form now gives
``` math
\chi_{A|_{\mathbf 1^\perp}}(x)=p_k(x)^m,\qquad n-1=4m.
```
The four roots of $`p_k`$ sum to $`-6`$, so $`\operatorname{tr}A=0`$ gives
``` math
0=k-6m.
```
Hence $`n-1=4m=2k/3`$, contradicting $`n\ge k+1`$. Thus $`\mathcal E_k\ne0`$. Its constant row sum is consequently a positive integer, so $`\varepsilon_{k,n}\ge1`$, which is equivalent to the displayed order bound. The symbolic expansion, irreducibility alternatives, and finite specializations have also been checked by independent exact audits. ◻

</div>

# Optimal-slack integrality and local positivity

The trace of $`\mathcal S_k`$ is a positive scalar multiple of the one-variable LP defect. Its $`2\times2`$ principal minors give integral local restrictions, and larger principal minors form a canonical semidefinite hierarchy. We retain the edge-local argument below because it exposes the cycle-count obstruction hidden by the stronger global order bound.

<div id="thm:three-to-one" class="theorem">

**Theorem 18** (Three-to-one excess bound). *Under the hypotheses of Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">17</a>, assume $`k\ge6`$ and write $`\varepsilon=\varepsilon_{k,n}`$. The integral parameter
``` math
r=2\varepsilon-n-2
   =2(k+2)^2(k^2+3)-(12k+27)n
```
satisfies
``` math
r>0,\qquad n\le3r.
```
Consequently
``` math
\boxed{
 n\le\left\lfloor
 \frac{3(k+2)^2(k^2+3)}{18k+41}
 \right\rfloor.
 }
```*

</div>

<div class="proof">

*Proof.* Put $`E=\mathcal E_k`$, $`C=C_k`$, $`h=h_k`$, and
``` math
\rho=\frac{\varepsilon-1}{n}
      =\frac{1+r/n}{2}.
```
The optimal slack matrix has the form
``` math
\mathcal S_k=I-E+\rho J\succeq0.
```
We first record the divisibility identity
``` math
128(2C-r)
 =(4k+9)(64k^3+112k^2+196k+327)+(129-128r).
```
Since $`n=(2C-r)/(12k+27)`$ is integral and $`4k+9`$ is odd,
``` math
\begin{equation}
\label{eq:r-divisibility}
 4k+9\mid129-128r.
\end{equation}
```
We shall also use the following fixed-remainder calculation. If $`n=3r+t`$, then the defining equation for $`r`$ gives
``` math
18k+41\mid 2C-(12k+27)t.
```
Since $`\gcd(18,18k+41)=1`$, Euclidean division after multiplication by $`18^4`$ yields the necessary condition
``` math
\begin{equation}
\label{eq:fixed-remainder}
 18k+41\mid 132650+34992t.
\end{equation}
```

*Positivity of $`r`$.* Suppose $`r\le0`$. A $`2\times2`$ principal minor of $`\mathcal S_k`$ gives
``` math
E_{uv}\le2+\frac rn\qquad(u\ne v).
```
Thus $`E`$ is the adjacency matrix of a simple graph when $`r<0`$. If $`r=0`$ and $`E_{uv}=2`$, positivity puts $`e_u+e_v`$ in $`\ker\mathcal S_k`$. After subtracting its projection onto $`\mathbf 1`$, the strict spectral window gives a $`(-2)`$-eigenvector of $`A`$. Its $`u`$-coordinate would require
``` math
A_{uv}=-2+\frac{2k+4}{n},
```
which is impossible because $`n\ge k^2+2`$ and $`A_{uv}\in\{0,1\}`$. Hence $`E`$ is simple also when $`r=0`$.

Let $`X`$ be the graph with adjacency matrix $`J-I-E`$. It is regular of degree
``` math
d=n-1-\varepsilon=\frac{n-r-4}{2},
```
and $`A(X)=-I-E+J`$ has least eigenvalue at least $`-2`$. Every component has at least $`d+1`$ vertices, so $`X`$ has at most two components. We use the fact that $`E`$, being a polynomial in $`A`$ and $`J`$, commutes with $`A`$; hence every rational eigenspace of $`E`$ is $`A`$-invariant. We use the classification of connected regular graphs of order greater than $`28`$ and least eigenvalue at least $`-2`$: such a graph is a line graph or a cocktail-party graph ([Cameron et al. 1976](#ref-CameronEtAl1976)); see also ([Cvetković et al. 2004](#ref-CvetkovicEtAl2004), Theorems 4.1.1 and 4.1.5) and ([Koolen et al. 2025](#ref-KoolenEtAl2025), Introduction).

Suppose first that $`X`$ is connected. The complete case would give $`E=0`$, excluded in Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">17</a>. In the cocktail-party case, $`E`$ is a perfect matching and $`r=-n`$. The identity
``` math
1296C=(6k+13)(216k^3+396k^2+654k+1175)+277
```
forces $`k=44`$ and $`n=14812`$. On the $`7406`$-dimensional $`(-1)`$-eigenspace of $`E`$, the rational operator $`A`$ is annihilated by $`g_{44}(x)+2`$.

If $`X=L(Y)`$ and $`Y`$ is $`q`$-regular, then $`q\ge n/4`$ and $`|V(Y)|\le8`$, contradicting $`q\le |V(Y)|-1`$ because $`n\ge38`$. If $`Y`$ is semiregular bipartite with part sizes $`a\ge b\ge2`$, then
``` math
\frac1a+\frac1b=\frac{n-r}{2n}\ge\frac12,\qquad n\le ab.
```
The cases $`b\ge3`$ have $`ab<38`$. For $`b=2`$, connectedness forces $`Y=K_{a,2}`$, hence $`r=-4`$. Equation <a href="#eq:r-divisibility" data-reference-type="eqref" data-reference="eq:r-divisibility">[eq:r-divisibility]</a> leaves $`k=158`$ and $`n=664748`$. The resulting $`(-1)`$-eigenspace of $`E`$ has dimension $`332373`$.

If $`X`$ has two components, write their orders as $`d+1+a_1`$ and $`d+1+a_2`$. Then
``` math
a_1+a_2=r+2,
```
so $`r\in\{-2,-1,0\}`$. Checking the divisors in <a href="#eq:r-divisibility" data-reference-type="eqref" data-reference="eq:r-divisibility">[eq:r-divisibility]</a>, together with $`n\ge k^2+2`$ and $`kn`$ even, leaves only
``` math
(r,k,n)=(-1,62,40875).
```
The components then have orders $`20437`$ and $`20438`$; one is complete and the other cocktail-party. Thus $`E`$ has eigenvalue $`-1`$ with multiplicity $`10219`$.

In all three exceptional cases the rational primary space is annihilated by $`g_k(x)+2`$. This quartic is irreducible over $`\mathbb Q`$ for every integer $`k\ge6`$, except $`k=7`$. Indeed, after $`y=x+2`$ it becomes
``` math
y^4-2y^3+(3-2k)y^2+2.
```
Gauss’s lemma reduces a quadratic factorization to monic integer quadratics whose constant terms multiply to $`2`$; coefficient comparison leaves only $`k=4`$ or $`k=7`$, while the rational-root alternatives give $`k=2`$ or $`k=4`$. The degrees $`44,62,158`$ are therefore irreducible cases, but the corresponding dimensions $`7406,10219,332373`$ are not divisible by four. Since an invariant rational space annihilated by an irreducible quartic is a vector space over the degree-four field $`\mathbb Q[x]/(g_k(x)+2)`$, its rational dimension must be divisible by four. This contradiction proves $`r>0`$.

*Simplicity above the putative boundary.* Assume for contradiction that $`n>3r`$, and put $`x=r/n\in(0,1/3)`$. The $`2\times2`$ minors give $`E_{uv}\le2`$. Suppose $`E_{uv}=2`$, and for $`w\notin\{u,v\}`$ set $`s_w=E_{uw}+E_{vw}`$. Cauchy–Schwarz for $`e_u+e_v`$ and $`e_w`$ in the Gram matrix $`\mathcal S_k`$ gives
``` math
(1+x-s_w)^2\le x(3+x),
```
so the nonnegative integer $`s_w`$ belongs to $`\{1,2\}`$. The row sums show that exactly $`r`$ vertices have $`s_w=2`$. Let $`W`$ be their set, let $`y=\sum_{w\in W}e_w`$, and put
``` math
e_W=\sum_{\{w,z\}\subseteq W}E_{wz}.
```
Then
``` math
\begin{aligned}
  (e_u+e_v)^{\mathsf T}\mathcal S_k(e_u+e_v)&=2x,\\
  (e_u+e_v)^{\mathsf T}\mathcal S_k y&=r(x-1),\\
  y^{\mathsf T}\mathcal S_k y&=r+\frac{r^2(1+x)}2-2e_W.
 \end{aligned}
```
Positivity of this $`2\times2`$ Gram determinant yields
``` math
2xr+r^2(3x-1)-4xe_W\ge0.
```
Since $`e_W\ge0`$, it follows that $`n\le3r+2`$. Hence $`n=3r+t`$ with $`t\in\{1,2\}`$. Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">[eq:fixed-remainder]</a> gives:
``` math
\begin{array}{c|c|c}
  t&\text{remainder}&\text{admissible }(18k+41,k)\\
  \hline
  1&167642&\text{none}\\
  2&202634&(1427,77).
 \end{array}
```
The remaining case gives $`(k,n,r)=(77,77831,25943)`$, but $`kn`$ is odd, contrary to the handshake lemma. Therefore $`E`$ is simple.

Again let $`X`$ be the graph with adjacency matrix $`J-I-E`$. It is $`d`$-regular with least eigenvalue at least $`-2`$. If $`X`$ had at least three components, then $`n\ge3(d+1)`$, or $`n\le3r+6`$. Thus $`n=3r+t`$ for $`1\le t\le6`$. Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">[eq:fixed-remainder]</a> gives
``` math
\begin{array}{c|rrrrrr}
  t&1&2&3&4&5&6\\ \hline
  \text{remainder}
   &167642&202634&237626&272618&307610&342602,
 \end{array}
```
and leaves no integral graph: the $`t=2`$ case is excluded above, while the sole divisor candidate for $`t=3`$ does not make $`r`$ integral. Hence $`X`$ has at most two components.

Suppose first that $`X`$ is connected. The cocktail-party case contradicts $`r>0`$, so $`X=L(Y)`$. If $`Y`$ is $`q`$-regular on $`v`$ vertices, then
``` math
q=\frac{n-r}{4}>\frac n6,\qquad v=\frac{2n}{q}<12.
```
Simplicity and $`n\ge38`$ leave only
``` math
\begin{aligned}
  (q,v;n,r)\in\{&(8,10;40,8),(9,10;45,9),\\
                 &(8,11;44,12),(10,11;55,15)\}.
 \end{aligned}
```
The radius-two lower bound forces $`k\le7`$, and direct substitution in the defining formula for $`r`$ excludes all four cases.

For a semiregular bipartite root with part sizes $`a\ge b\ge2`$, write $`p=n/a\le q=n/b`$ for its two degrees. Then
``` math
p+q=\frac{n-r}{2}>\frac n3,
  \qquad (b-2)n=b(r+2p),
```
so $`b<6`$. Connectedness excludes $`p=1`$. The cases $`b=2`$ and $`b=5`$ are immediate; $`b=4`$ leaves only
``` math
(p,q,a,b;n,r)=(4,10,10,4;40,12),\ (4,11,11,4;44,14),
```
both excluded by the radius-two bound and the formula for $`r`$. For $`b=3`$, one has $`p=2`$ or $`3`$, giving $`n=3r+12`$ or $`n=3r+18`$. Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">[eq:fixed-remainder]</a> gives the remainders $`552554=2\cdot276277`$ and $`762506=2\cdot381253`$. Their odd cofactors are prime and congruent to $`13\pmod {18}`$, whereas $`18k+41\equiv5
 \pmod {18}`$. Thus $`X`$ cannot be connected.

It remains to consider two components. For $`k=6,7,8`$, the inequalities $`r>0`$ and $`n>3r`$ contain no admissible integral order. For $`k\ge9`$, one has $`n>150`$, and both components have order greater than $`28`$. A regular line-graph root is too small. For a semiregular bipartite root of a component of order $`N`$, the part sizes satisfy
``` math
\frac1a+\frac1b=\frac{d+2}{N}
  \ge\frac{n-r}{n+r+2}>\frac{49}{100}.
```
If $`b\ge3`$, the five possible pairs $`(a,b)`$ have $`ab\le18<N`$. If $`b=2`$, connectedness forces the root $`K_{d,2}`$, whose line graph has order $`2d`$. Thus every component is $`K_{d+1}`$, a cocktail-party graph of order $`d+2`$, or $`L(K_{d,2})`$. The first two types alone force $`r\le0`$. If exactly one component has order $`2d`$, then $`n=3r+8`$ or $`n=3r+10`$; if both do, then $`n=2r+8`$. The respective fixed remainders are
``` math
412586,\qquad482570,\qquad1792898.
```
The first and third have no admissible divisor of the required linear form. The second leaves only $`k=123`$, for which $`kn`$ is odd. This final contradiction proves $`n\le3r`$.

Substituting the definition of $`r`$ gives
``` math
(18k+41)n\le3(k+2)^2(k^2+3),
```
which is the displayed bound. All polynomial divisions, irreducibility alternatives, fixed-remainder cases, line-root reductions, and Gram determinants in this argument have been replayed independently in exact arithmetic. ◻

</div>

<div id="cor:three-to-one-equality" class="corollary">

**Corollary 19** (Rigidity at equality). *Under the hypotheses and notation of Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">18</a>, equality in $`n\le3r`$ can occur only for
``` math
\boxed{(k,n,r)=(103,185220,61740).}
```
This is an arithmetic parameter classification; it does not assert the existence of a graph with these parameters.*

</div>

<div class="proof">

*Proof.* Equality gives
``` math
(18k+41)r=(k+2)^2(k^2+3)=:C_k.
```
Exact Euclidean division yields
``` math
\begin{aligned}
18^4C_k={}&(18k+41)
 (5832k^3+10044k^2+17946k+29107)\\
&+66325,
\end{aligned}
```
where $`66325=5^2\cdot7\cdot379`$. Hence $`18k+41\mid66325`$. Since $`k\ge6`$, this divisor is at least $`149`$ and is congruent to $`5`$ modulo $`18`$. Among the positive divisors of $`66325`$, only $`1895`$ has these properties. Thus $`k=103`$, after which direct substitution gives $`r=61740`$ and $`n=3r=185220`$. ◻

</div>

<div id="prop:signed-complement" class="proposition">

**Proposition 20** (Signed-complement bridge). *Under the hypotheses and notation of Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">18</a>, assume $`0<r<n`$ and define
``` math
S=(6k+14)J-2I-g_k(A).
```
Then $`S`$ is a signed adjacency matrix:
``` math
S_{uu}=0,\qquad S_{uv}\in\{-1,0,1\}\quad(u\ne v).
```
It has constant signed row sum $`(n-r-4)/2`$, and
``` math
S+2I\succeq0,\qquad E_{-2}(S)=E_{-2}(A).
```*

</div>

<div class="proof">

*Proof.* Write $`x=r/n\in(0,1)`$, $`\rho=(1+x)/2`$, and $`E=\mathcal E_k`$. Since
``` math
\mathcal S_k=I-E+\rho J\succeq0,
```
its $`2\times2`$ principal minors give $`-1\le E_{uv}\le2+x`$. The entries of $`E`$ are nonnegative integers, so $`E_{uv}\in\{0,1,2\}`$ for $`u\ne v`$, and $`S=J-I-E`$ has the asserted entries. The row sum follows from $`\varepsilon=(n+r+2)/2`$. Moreover,
``` math
S+2I
 =\mathcal S_k+\frac{n-r}{2n}J\succeq0.
```
The matrices $`A`$ and $`S`$ commute. On a nonprincipal adjacency eigenvector with eigenvalue $`\theta`$, the corresponding eigenvalue of $`S`$ is $`-2-g_k(\theta)`$. The only zero of $`g_k`$ in the open shifted WOW window is $`\theta=-2`$; the other two zeros are its excluded endpoints. The principal eigenvalue of $`S`$ is not $`-2`$ because $`r<n`$. Hence the two $`(-2)`$-eigenspaces coincide. ◻

</div>

<div id="prop:edge-cycle" class="proposition">

**Proposition 21** (Edge-local cycle bounds). *Let $`G`$ be connected and $`k`$-regular, where $`k\ge4`$, of girth at least five and diameter three, and suppose
``` math
|\theta+1|\le\sqrt{2k-2}
 \qquad(\theta\ne k)
```
for every adjacency eigenvalue $`\theta`$. For an edge $`uv`$, let $`\sigma_{uv}`$ be the number of $`5`$-cycles containing that edge. Then
``` math
2k-2\le\sigma_{uv}\le
 \frac{2(k+2)^2(k^2+3)}n-10k-26.
```
If $`n=k^2+1+c`$, then also
``` math
\sigma_{uv}\ge(k-1)^2-c.
```*

</div>

<div class="proof">

*Proof.* Recall $`g_k`$ and $`C_k=g_k(k)`$ from Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">17</a>, and put
``` math
M=-g_k(A)+\frac{C_k}{n}J.
```
The spectral window gives $`M\succeq0`$. For an edge $`uv`$,
``` math
(A^3)_{uv}=\sum_{z\sim v}(A^2)_{uz}=k+(k-1)=2k-1.
```
Here $`z=u`$ contributes $`k`$, while every other neighbour of $`v`$ is at distance two from $`u`$ and has a unique length-two path from $`u`$. Moreover,
``` math
(A^4)_{uv}=\sum_z(A^2)_{uz}(A^2)_{zv}=\sigma_{uv}.
```
Indeed, the nonzero summands away from the diagonal are precisely the vertices at distance two from both $`u`$ and $`v`$. Their two unique length-two paths, together with $`uv`$, form a five-cycle, and each five-cycle through $`uv`$ yields one such vertex. Since $`C_k=(k+2)^2(k^2+3)`$, the diagonal and edge entries of $`M`$ are
``` math
a=\frac{C_k}{n}-6(k+2),
 \qquad
 b=\frac{C_k}{n}-(4k+14)-\sigma_{uv}.
```
The principal submatrix on $`\{u,v\}`$ is $`\bigl(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\bigr)`$, so $`a\ge0`$ and $`-a\le b\le a`$. The inequality $`b\le a`$ gives $`\sigma_{uv}\ge2k-2`$, while $`b\ge-a`$ gives the stated upper bound.

For the final bound, every radius-two ball has size $`k^2+1`$. The set
``` math
\{u,v\}\cup(N(u)\setminus\{v\})\cup(N(v)\setminus\{u\})
```
contains $`2k`$ vertices and lies in $`B_2(u)\cap B_2(v)`$. Every further intersection vertex is at distance two from both endpoints and is therefore in the preceding five-cycle bijection. Hence
``` math
|B_2(u)\cap B_2(v)|=2k+\sigma_{uv}.
```
Inclusion–exclusion and $`n=k^2+1+c`$ now give $`\sigma_{uv}\ge(k-1)^2-c`$. The complete walk classification, sign directions, and radius-two bijection have also been checked independently and exactly. ◻

</div>

For $`\ell\ge3`$, let $`N_\ell`$ denote the number of $`\ell`$-cycles in $`G`$.

<div id="cor:edge-cycle-sieve" class="corollary">

**Corollary 22** (Edge–cycle divisibility sieve). *Under the hypotheses of Proposition <a href="#prop:edge-cycle" data-reference-type="ref" data-reference="prop:edge-cycle">21</a>, put
``` math
L_{k,n}=\max\{2k-2,\;2k^2-2k+2-n\},
 \qquad
 U_{k,n}=\frac{2(k+2)^2(k^2+3)}{n}-10k-26.
```
Necessarily
``` math
\boxed{\lceil L_{k,n}\rceil\le\lfloor U_{k,n}\rfloor.}
```
If both sides equal an integer $`s`$, then every edge of $`G`$ lies in exactly $`s`$ five-cycles and
``` math
\boxed{5\mid \frac{skn}{2}.}
```*

</div>

<div class="proof">

*Proof.* Writing $`n=k^2+1+c`$, the two lower bounds in Proposition <a href="#prop:edge-cycle" data-reference-type="ref" data-reference="prop:edge-cycle">21</a> combine to
``` math
\sigma_{uv}\ge
 \max\{2k-2,(k-1)^2-c\}=L_{k,n},
```
while its upper bound is $`U_{k,n}`$. Since $`\sigma_{uv}`$ is an integer, the first conclusion follows. If the two integer bounds coincide at $`s`$, then $`\sigma_{uv}=s`$ for every edge. Counting edge–five-cycle incidences gives
``` math
5N_5=\sum_{uv\in E(G)}\sigma_{uv}
 =s|E(G)|=\frac{skn}{2},
```
which proves the divisibility condition. ◻

</div>

<div id="thm:degree-six-fifty" class="theorem">

**Theorem 23**. *Every connected $`6`$-regular strict counterexample to WOW-284 has order at most $`50`$.*

</div>

<div class="proof">

*Proof.* A separate Rayleigh and trace argument shows that any degree-six strict counterexample has diameter three. For vertices at distance $`d\ge4`$, the vector with weights $`3,1,-3,-1`$ on the two endpoints and their respective neighbourhoods has Rayleigh quotient at most
``` math
\frac{204-81d}{15}\le-8,
```
contradicting $`\delta^*=6`$. Diameter two would force equality in the Moore bound, hence order $`37`$ and adjacency characteristic polynomial $`(x-6)(x^2+x-5)^{18}`$; its root sum is $`-12`$, contradicting $`\operatorname{tr}A=0`$. Thus the diameter is three, and Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">18</a> gives
``` math
n\le\left\lfloor\frac{3\cdot8^2\cdot39}{149}\right\rfloor=50.
```

For an independent local explanation of the excluded boundary, assume $`n=51`$. Corollary <a href="#cor:edge-cycle-sieve" data-reference-type="ref" data-reference="cor:edge-cycle-sieve">22</a> has $`\lceil L_{6,51}\rceil=\lfloor U_{6,51}\rfloor=11`$, and hence requires
``` math
5N_5=153\cdot11=1683,
 \qquad 5\nmid 1683,
```
which is impossible. An independent exact audit verifies the full diameter reduction and incidence calculation. ◻

</div>

<div id="cor:low-degree-windows" class="corollary">

**Corollary 24** (Low-degree order windows). *There is no regular strict counterexample of degree at most five. In degrees six through nine, every regular strict counterexample satisfies
``` math
\begin{align*}
k=6&:\quad n\le50,\\
k=7&:\quad n=50\text{ in diameter two, or }n\le74\text{ in diameter three},\\
k=8&:\quad n\le108,\\
k=9&:\quad n\le150.
\end{align*}
```*

</div>

<div class="proof">

*Proof.* The degree exclusion is Theorem <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">10</a>, and Theorem <a href="#thm:diameter-four" data-reference-type="ref" data-reference="thm:diameter-four">12</a> removes diameter four for $`k\le9`$. For diameter three, Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">18</a> gives, for $`k=6,7,8,9`$, respectively,
``` math
n\le50,\ 75,\ 108,\ 150.
```
Since $`7n=2|E(G)|`$, the degree-seven bound improves to $`74`$. The diameter-two alternatives are determined by the Moore multiplicities: only the degree-seven, order-$`50`$ Hoffman–Singleton case survives. ◻

</div>

For comparison, the unadjusted diameter-three bounds in degrees $`6`$ through $`20`$ are
``` math
\begin{array}{c|rrrrrrrrrrrrrrr}
 k&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20\\
 \hline
 n&50&75&108&150&201&263&336&422&521&635&765&911&1075&1257&1459.
\end{array}
```
When $`k`$ is odd, $`kn=2|E(G)|`$ requires $`n`$ to be even; in particular, the entries for $`k=7,11,15,17,19`$ improve to $`74,262,634,910,1256`$, respectively.

<div id="prop:order50-minus-two" class="proposition">

**Proposition 25** (The order-$`50`$ $`(-2)`$-multiplicity bound). *Let $`G`$ be $`6`$-regular, of order $`50`$, and of girth at least five. The multiplicity $`m_{-2}(A)`$ of the adjacency eigenvalue $`-2`$ satisfies
``` math
m_{-2}(A)\le20.
```*

</div>

<div class="proof">

*Proof.* Put $`m=m_{-2}(A)`$, remove the principal eigenvalue $`6`$ and the $`m`$ copies of $`-2`$, and denote the remaining spectral moments by $`\mu_0,\ldots,\mu_4`$. Girth at least five gives
``` math
\operatorname{tr}A=0,\quad \operatorname{tr}A^2=300,\quad \operatorname{tr}A^3=0,\quad \operatorname{tr}A^4=3300,
```
and therefore
``` math
(\mu_0,\mu_1,\mu_2,\mu_3,\mu_4)
 =(49-m,-6+2m,264-4m,-216+8m,2004-16m).
```
The moment matrix
``` math
H=\begin{pmatrix}
 \mu_0&\mu_1&\mu_2\\
 \mu_1&\mu_2&\mu_3\\
 \mu_2&\mu_3&\mu_4
 \end{pmatrix}
```
is positive semidefinite. Exact expansion gives
``` math
\det H=3600(1625-81m)\ge0.
```
Since $`m`$ is an integer, $`m\le20`$. ◻

</div>

## Necessary structure at order fifty

The remaining degree-six boundary is highly constrained, although not yet eliminated.

<div id="thm:order50-feasibility" class="theorem">

**Theorem 26**. *Let $`G`$ be a connected $`6`$-regular graph of order $`50`$ and girth at least five, and suppose $`\Phi(G)>0`$. Then $`G`$ has diameter three. Every edge lies in $`12`$ or $`13`$ five-cycles. Let $`H`$ be the spanning subgraph of edges that lie in $`13`$ five-cycles, let $`m=|E(H)|`$, and let $`\tau(v)`$ be the number of five-cycles through $`v`$. Then
``` math
\tau(v)\in\{36,37,38\},
 \qquad d_H(v)=2\tau(v)-72\in\{0,2,4\},
```
``` math
m\equiv0\pmod5,
 \qquad N_5=360+\frac m5.
```
For a two-edge path $`u-v-w`$, put
``` math
R_{uvw}=6\alpha_{uvw}+\beta_{uvw},
```
where $`\alpha`$ and $`\beta`$ count the five- and six-cycles containing the path. The allowed values are
``` math
\begin{array}{c|c}
\text{types of the two incident edges}&R_{uvw}\\
\hline
\text{low--low}&30,31,32\\
\text{mixed}&30,31,32\\
\text{high--high}&30,31.
\end{array}
```
Writing $`S_2=\sum_vd_H(v)^2`$, one has
``` math
1950-m\le N_6
 \le2200-\frac{5m}{6}-\frac{S_2}{12},
```
``` math
\frac{43m^2-70200m+119632500}{58500}
 \le N_6
 \le\frac{4220000-2200m-7m^2}{2000}.
```
Exact enumeration of the resulting coarse degree profiles leaves $`266`$ possibilities.*

</div>

<div class="proof">

*Proof.* The diameter reduction used in Theorem <a href="#thm:degree-six-fifty" data-reference-type="ref" data-reference="thm:degree-six-fifty">23</a> applies verbatim: diameter at least four gives a Rayleigh quotient at most $`-8`$, and diameter two gives the trace contradiction from $`(x-6)(x^2+x-5)^{18}`$. Hence the diameter is three. Around a fixed vertex the distance layers have sizes $`1,6,30,13`$. If $`\tau`$ is the number of five-cycles through the centre, the average row quotient is similar to the symmetric compression on normalized layer indicators. Its nonprincipal factor $`q_\tau`$ satisfies
``` math
195q_\tau(-1+\sqrt{10})
 =(-215+56\sqrt{10})\tau+7350-1860\sqrt{10}.
```
The coefficient of $`\tau`$ is negative because $`56^2\cdot10<215^2`$, and at $`\tau=39`$ the right-hand side is $`9(-115+36\sqrt{10})<0`$. Also
``` math
195q_\tau(6)=1500(75-\tau)>0.
```
The last inequality is strict: the third layer is nonempty and connected to the second, while their edge count is $`150-2\tau`$. Thus $`\tau\ge39`$ would place a nonprincipal compression eigenvalue in $`(-1+\sqrt{10},6)`$, contradicting interlacing and the open WOW window. Conversely, $`150-2\tau\le13\cdot6`$, so $`\tau\ge36`$. Hence $`\tau\in\{36,37,38\}`$. Finally, $`\sum_{e\ni v}\sigma_e=2\tau(v)`$, so the high-edge degree is $`2\tau(v)-72`$; counting edge–five-cycle incidences gives $`5N_5=12\cdot150+m`$.

For a two-path $`u-v-w`$, girth at least five gives $`(A^3)_{uw}=\alpha_{uvw}`$ and $`(A^4)_{uw}=16+\beta_{uvw}`$. The corresponding $`3\times3`$ principal minor of the centered positive-semidefinite matrix yields the displayed finite sets for $`R_{uvw}`$, except for an apparent equality value $`R_{uvw}=29`$. At equality, the Gram norm of $`e_u-e_w`$ vanishes, so this vector lies in the kernel of the centered matrix. On $`\mathbf 1^\perp`$, that matrix is $`-g_6(A)`$. The strict shifted window excludes the two endpoint zeros of $`g_6`$, leaving only its double zero at $`-2`$; hence the kernel there is exactly the adjacency $`-2`$-eigenspace. However, the $`u`$-coordinate of $`A(e_u-e_w)`$ is zero because $`u\not\sim w`$, whereas the $`u`$-coordinate of $`-2(e_u-e_w)`$ is $`-2`$. This excludes $`R_{uvw}=29`$. Summing the local inequalities gives the first pair of $`N_6`$ bounds; shifted moment and localizing matrices give the second. The complete symbolic determinants, Schur complements, kernel argument, and integer enumeration have also been checked independently and exactly. The surviving $`266`$ profiles are exact pruning data, not an existence or nonexistence claim. ◻

</div>

<div id="rem:signed-root" class="remark">

*Remark 27* (Signed-root Gram formulation). Under the hypotheses of Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">26</a>, put
``` math
T=50J-g_6(A)-2I.
```
Then
``` math
T\mathbf 1=2\mathbf 1,\qquad T+2I\succeq0,
 \qquad 25\mathcal S_6=25(T+2I)-2J.
```
This is the specialization of Proposition <a href="#prop:signed-complement" data-reference-type="ref" data-reference="prop:signed-complement">20</a>: the excess parameter is $`r=42`$, so the signed row sum is $`2`$. For vertices $`u,z`$ at distance three, put
``` math
q_{uz}=6(A^3)_{uz}+(A^4)_{uz}.
```
The $`2\times2`$ estimate gives $`q_{uz}\in\{48,49,50,51\}`$, and the kernel argument in Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">17</a> excludes $`48`$. Together with the edge and two-path intervals in Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">26</a>, this gives
``` math
T_{uv}\in\{-1,0,1\}\qquad(u\ne v),\qquad T_{uu}=0.
```
Consequently $`T+2I`$ is the Gram matrix of $`50`$ vectors of norm $`\sqrt2`$ with pairwise inner products in $`\{-1,0,1\}`$ and constant signed row sum $`2`$. Its kernel is $`E_{-2}(A)`$, so Proposition <a href="#prop:order50-minus-two" data-reference-type="ref" data-reference="prop:order50-minus-two">25</a> gives
``` math
\operatorname{rank}(T+2I)\ge30.
```
Thus the unresolved degree-six boundary can therefore be viewed as a root-type integral Gram problem constrained by the graph’s distance classes and local cycle data.

</div>

<div id="thm:order50-disconnected" class="theorem">

**Theorem 28** (Disconnected signed complement). *Under the hypotheses of Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">26</a>, the underlying signed graph of the matrix $`T`$ in Remark <a href="#rem:signed-root" data-reference-type="ref" data-reference="rem:signed-root">27</a> is disconnected.*

</div>

<div class="proof">

*Proof.* Let $`N_i`$ denote the number of $`i`$-cycles. In terms of the degree-six nonbacktracking polynomials,
``` math
\begin{aligned}
(g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
&+352F_5+78F_6+12F_7+F_8.
\end{aligned}
```
Girth at least five gives $`\operatorname{tr}F_i(A)=0`$ for $`1\le i\le4`$. For lengths five and six, every closed nonbacktracking walk is a directed cycle. At lengths seven and eight there are also the walks obtained by attaching a one-edge tail to a directed five- or six-cycle. Hence
``` math
\begin{aligned}
\operatorname{tr}F_5(A)&=10N_5,&
\operatorname{tr}F_6(A)&=12N_6,\\
\operatorname{tr}F_7(A)&=14N_7+40N_5,&
\operatorname{tr}F_8(A)&=16N_8+48N_6.
\end{aligned}
```
Removing the principal adjacency contribution and restoring the principal signed eigenvalue $`2`$ now gives
``` math
\operatorname{tr}T^2
=8(500N_5+123N_6+21N_7+2N_8-604100).
```
If $`P_+`$ and $`P_-`$ are the numbers of positive and negative signed edges, then the signed row sum and the zero diagonal give
``` math
P_+-P_-=50,\qquad
\operatorname{tr}T^2=2(P_++P_-)=100+4P_-.
```
It follows that $`P_-`$ is odd.

Suppose that $`T`$ were connected. By Proposition <a href="#prop:order50-minus-two" data-reference-type="ref" data-reference="prop:order50-minus-two">25</a>, $`\operatorname{rank}(T+2I)\ge30`$. The root-system representation theorem for connected edge-signed graphs with smallest eigenvalue at least $`-2`$ ([Greaves et al. 2015](#ref-GreavesEtAl2015), Theorem 2) represents $`T+2I`$ in a root system of type $`D_\ell`$ or $`E_8`$. The rank bound excludes $`E_8`$. Thus
``` math
B^{\mathsf T}B=T+2I
```
for an integral matrix $`B`$ whose columns $`b_u`$ are roots $`\pm e_i\pm e_j`$. Put $`s=B\mathbf 1`$. Since $`(T+2I)\mathbf 1=4\mathbf 1`$,
``` math
b_u\mathbin{\cdot}s=4\quad\text{for every }u,
\qquad
\lVert s\rVert^2=200.
```
Changing signs of coordinate axes if necessary, assume $`s_i\ge0`$. The coordinate-support multigraph is connected, since otherwise its columns would split into two Gram-orthogonal families and $`T`$ would be disconnected. If $`v`$ coordinates are used, then
``` math
30\le v\le51:
```
the lower bound is the Gram rank, and a connected support multigraph with fifty root-edges has at most fifty-one vertices.

For every root, two coordinate levels satisfy $`\pm s_i\pm s_j=4`$. Connectivity therefore places all levels in one of
``` math
0,4,8,\ldots;\qquad
2,6,10,\ldots;\qquad
1,3,5,\ldots.
```
The first family would make $`\lVert s\rVert^2`$ divisible by $`16`$, contrary to $`200\equiv8\pmod {16}`$.

In the second family, a level at least $`10`$, together with the other $`v-1\ge29`$ levels, would contribute at least $`10^2+29\cdot2^2>200`$. Thus only levels $`2`$ and $`6`$ occur. If their multiplicities are $`n_2,n_6`$, then
``` math
n_2+9n_6=50,\qquad
v=n_2+n_6=50-8n_6\ge30,
```
so
``` math
(n_2,n_6)\in\{(50,0),(41,1),(32,2)\}.
```
Every root is now either $`e_i+e_j`$ with $`s_i=s_j=2`$, or $`e_i-e_j`$ with $`s_i=6`$ and $`s_j=2`$, after ordering the two coordinates. Its sign pattern is unique on a fixed support, while duplicate columns would have inner product $`2`$; hence distinct roots share at most one coordinate in this restricted family. At a level-two coordinate let $`p_i,m_i`$ be its positive and negative incidence counts. Then $`p_i-m_i=2`$, and every level-six coordinate has six incidences, all negative at level two. A negative Gram product occurs precisely when two roots meet at one level-two coordinate with opposite incidence signs, so it is counted exactly once in
``` math
P_-=\sum_{i:s_i=2}p_im_i.
```
Consequently
``` math
P_-\equiv\sum_{i:s_i=2} p_im_i
\equiv\sum_i m_i
=6n_6
\equiv0\pmod2,
```
contradicting the parity already proved.

It remains to exclude odd levels. Let $`a_t,b_t`$ count coordinates at levels $`4t+1,4t+3`$, respectively. Flow balance along the two level chains gives the following identity. Difference roots cancel within their chain when signed incidences are summed, while the positive roots between levels $`1`$ and $`3`$, the only cross-chain type, contribute equally to both sides:
``` math
\sum_{t\ge0}(4t+1)a_t
=\sum_{t\ge0}(4t+3)b_t.
```
Using this identity with $`\lVert s\rVert^2=200`$ yields
``` math
\frac{200-3v}{32}
=\sum_{t\ge1}\binom{t+1}{2}(a_t+b_t).
```
Thus $`v\equiv24\pmod {32}`$, which is impossible for $`30\le v\le51`$. All three level families are excluded, proving that $`T`$ is disconnected. ◻

</div>

# Distance spectra of punctured Moore graphs

Let $`M`$ be a degree-$`k`$ Moore graph of diameter two and put $`\Delta=\sqrt{4k-3}`$.

<div id="thm:one-puncture" class="theorem">

**Theorem 29** (One deleted vertex). *For $`v\in V(M)`$, put $`H=M-v`$. Then
``` math
|V(H)|=k^2,
 \qquad \delta^*(H)=k-\frac1k,
 \qquad \lambda_{\min}(D(H))=-2-\sqrt{k}.
```
The complete distance spectrum is
``` math
\begin{align*}
\operatorname{Spec}D(H)={}&\{\rho_+,\rho_-\}
 \cup\{(-2+\sqrt{k})^{(k-1)},(-2-\sqrt{k})^{(k-1)}\}\\
&\cup\left\{\left(-\frac{\Delta+3}{2}\right)^{(m_+)},
\left(\frac{\Delta-3}{2}\right)^{(m_-)}\right\},
\end{align*}
```
where
``` math
\rho_\pm=k^2-2\pm\sqrt{k(k^3-2k^2+3k-1)},
```
``` math
m_\pm=\frac{k(k-2)(\Delta\pm1)}{2\Delta}.
```
Thus
``` math
\Phi(H)=k-\frac1k-2-\sqrt{k},
```
which is positive exactly for integers $`k\ge5`$.*

</div>

<div id="thm:edge-puncture" class="theorem">

**Theorem 30** (Endpoints of an edge). *Let $`uv\in E(M)`$ and $`H=M-\{u,v\}`$. For $`k\ge3`$,
``` math
|V(H)|=k^2-1,
 \qquad \delta^*(H)=k-\frac2k,
 \qquad \lambda_{\min}(D(H))=-2-\sqrt{k}.
```
The complete distance spectrum is
``` math
\begin{align*}
\operatorname{Spec}D(H)={}&\{\sigma_+,\sigma_-,k-4\}\\
&\cup\{(-2+\sqrt{k})^{(2k-4)},(-2-\sqrt{k})^{(2k-4)}\}\\
&\cup\left\{\left(-\frac{\Delta+3}{2}\right)^{(a_+)},
\left(\frac{\Delta-3}{2}\right)^{(a_-)}\right\},
\end{align*}
```
where
``` math
\sigma_\pm=k^2-3\pm\sqrt{k^4-2k^3+3k^2-8k+7},
```
``` math
a_+=\frac{(k-2)(k+(k-2)\Delta)}{2\Delta},
 \quad
 a_-=\frac{(k-2)((k-2)\Delta-k)}{2\Delta}.
```
Thus
``` math
\Phi(H)=k-\frac2k-2-\sqrt{k},
```
which is positive exactly for integers $`k\ge5`$.*

</div>

<div class="proof">

*Proof architecture for Theorems <a href="#thm:one-puncture" data-reference-type="ref" data-reference="thm:one-puncture">29</a> and <a href="#thm:edge-puncture" data-reference-type="ref" data-reference="thm:edge-puncture">30</a>.* The displayed dual-degree formulas are the cases $`s=1`$ and $`s=2`$ of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a>; its proof below is independent of the spectral decompositions. For one deleted vertex, put $`A=N(v)`$, $`B=\Gamma_2(v)`$, let $`C`$ be the $`A`$-by-$`B`$ incidence matrix, and let $`B_0`$ be the adjacency matrix on $`B`$. Only pairs inside $`A`$ lose their unique length-two path. For distinct $`a,a'\in A`$, choose a neighbour $`b\in B`$ of $`a`$. The vertices $`b,a'`$ are nonadjacent, and their unique common neighbour $`c`$ lies in $`B`$: it is not $`v`$, since $`b\not\sim v`$, and it is not in $`A`$, since an edge inside $`A`$ would form a triangle through $`v`$. Hence $`a-b-c-a'`$ is a surviving path, and therefore
``` math
D(H)=\begin{pmatrix}3(J-I)&2J-C\\2J-C^{\mathsf T}&2(J-I)-B_0\end{pmatrix}.
```
The normalized constant quotient is
``` math
Q_1=\begin{pmatrix}
 3(k-1)&(2k-1)\sqrt{k-1}\\
 (2k-1)\sqrt{k-1}&2k^2-3k-1
 \end{pmatrix},
```
whose eigenvalues are $`\rho_\pm`$. Block comparison in the Moore identity gives
``` math
CC^{\mathsf T}=(k-1)I,\qquad
 CB_0=J-C,\qquad
 C^{\mathsf T}\mathbf 1_A=\mathbf 1_B,
```
``` math
B_0^2+C^{\mathsf T}C=(k-1)I-B_0+J.
```
Thus $`C^{\mathsf T}`$ is injective and
``` math
\mathbb R^B=
 \langle\mathbf 1_B\rangle\perp
 C^{\mathsf T}(\mathbf 1_A^\perp)\perp K,
 \qquad K=\ker C,\qquad \dim K=k(k-2).
```
The cell-constant space, the two-dimensional spaces generated by $`(z,0)`$ and $`(0,C^{\mathsf T}z)`$ for $`z\in\mathbf 1_A^\perp`$, and $`0\oplus K`$ are mutually orthogonal and invariant. Denote the first space by $`W_{\mathrm{const}}`$ and the sum of the incidence spaces by $`W_{\mathrm{inc}}`$. Consequently
``` math
\mathbb R^{V(H)}=W_{\mathrm{const}}\perp W_{\mathrm{inc}}\perp(0\oplus K),
 \qquad 2+2(k-1)+k(k-2)=k^2.
```
On each zero-sum incidence module the action matrix in these generators is $`\bigl(\begin{smallmatrix}-3&-(k-1)\\-1&-1\end{smallmatrix}\bigr)`$, giving $`-2\pm\sqrt{k}`$. On $`K`$, $`B_0^2+B_0-(k-1)I=0`$, $`D=-2I-B_0`$, and the trace of $`B_0`$ is zero after removing the principal eigenvalue $`k-1`$ and the $`k-1`$ copies of $`-1`$ on $`C^{\mathsf T}(\mathbf 1_A^\perp)`$. Dimension and trace therefore give $`m_\pm`$.

For an adjacent deleted pair, put
``` math
A=N(u)\setminus\{v\},\qquad B=N(v)\setminus\{u\},\qquad
 C=V(M)\setminus\bigl(\{u,v\}\cup A\cup B\bigr).
```
Only pairs inside $`A`$ or inside $`B`$ lose a length-two path. For distinct $`a,a'\in A`$, choose a residual neighbour $`c`$ of $`a`$. The vertices $`c,a'`$ are nonadjacent, and their unique common neighbour is also residual: it cannot be one of the deleted endpoints, cannot lie in $`A`$ by triangle-freeness, and cannot lie in $`B`$ because no edge joins $`A`$ to $`B`$. This gives a surviving length-three path; the argument for $`B`$ is symmetric. The antisymmetric constant line has eigenvalue $`k-4`$, and the normalized symmetric quotient is
``` math
Q_2=\begin{pmatrix}
 5k-8&\sqrt{(k-1)(2k-3)(4k-6)}\\
 \sqrt{(k-1)(2k-3)(4k-6)}&2k^2-5k+2
 \end{pmatrix},
```
with eigenvalues $`\sigma_\pm`$. Let $`R_A,R_B`$ be the incidence matrices from $`A,B`$ to $`C`$, and let $`T`$ be the adjacency matrix on $`C`$. The Moore identity gives
``` math
R_AR_A^{\mathsf T}=R_BR_B^{\mathsf T}=(k-1)I,\qquad
 R_AR_B^{\mathsf T}=J,
```
``` math
R_AT=J-R_A,\qquad R_BT=J-R_B,
```
``` math
R_A^{\mathsf T}R_A+R_B^{\mathsf T}R_B+T^2
 =(k-1)I-T+J.
```
The zero-sum row images of $`R_A`$ and $`R_B`$ are injective and orthogonal. Each combines with its cell zero-sum space to form an invariant module carrying $`\bigl(\begin{smallmatrix}-3&-(k-1)\\-1&-1\end{smallmatrix}\bigr)`$. The residual space
``` math
K=\ker R_A\cap\ker R_B,\qquad \dim K=(k-2)^2,
```
is invariant and satisfies
``` math
T^2+T-(k-1)I=0,\qquad D=-2I-T.
```
These spaces and the three-dimensional cell-constant space are mutually orthogonal and complete, since
``` math
3+2(2k-4)+(k-2)^2=k^2-1.
```
The constant direction of $`T`$ has eigenvalue $`k-2`$, while its two zero-sum incidence images contribute trace $`-2(k-2)`$. Since $`\operatorname{tr}T=0`$, one has $`\operatorname{tr}(T|_K)=k-2`$, and dimension and trace give $`a_\pm`$. The residual negative root is greater than $`-2-\sqrt{k}`$. The same is true of the smaller constant-quotient roots: in each case the leading diagonal entry of the shifted quotient is positive, and
``` math
\det(Q_1+(2+\sqrt{k})I)
 =k(2k^2+2k^{3/2}-3k+2)>0,
```
``` math
\det(Q_2+(2+\sqrt{k})I)
 =(\sqrt{k}-1)(\sqrt{k}+1)
 (2k^2+2k^{3/2}-3k+2\sqrt{k}+6)>0.
```
Exact quotient normalization, trace-to-multiplicity equations, replacement paths, and all least-root comparisons are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_05_small_moore_punctures.py). ◻

</div>

<div id="thm:nonadjacent-puncture" class="theorem">

**Theorem 31** (Two nonadjacent deleted vertices). *Let $`u,v`$ be nonadjacent vertices of $`M`$, $`k\ge5`$, and put $`H=M-\{u,v\}`$. Define
``` math
\begin{align*}
R_k(x)={}&x^4+(10-2k^2)x^3+(2k^3-17k^2-2k+36)x^2\\
&+(12k^3-49k^2-4k+53)x\\
&-2k^4+17k^3-38k^2+5k+20,
\end{align*}
```
``` math
M_- =\frac{k(k-2)+(k^2-4k+2)\Delta}{2\Delta},
 \quad
 M_+ =\frac{-k(k-2)+(k^2-4k+2)\Delta}{2\Delta}.
```
Then
``` math
\begin{align*}
\chi_{D(H)}(x)={}&(x-k+3)R_k(x)
 (x^2+4x-k+3)^{k-2}\\
&\cdot(x^2+4x-k+5)^{k-2}
 \left(x+\frac{\Delta+3}{2}\right)^{M_-}\\
&\cdot\left(x-\frac{\Delta-3}{2}\right)^{M_+}.
\end{align*}
```
Moreover,
``` math
\delta^*(H)=k-\frac2k,
```
and $`H`$ is a strict counterexample for every realizable integer $`k\ge6`$.*

</div>

<div class="proof">

*Proof.* The deleted vertices have a unique common neighbour $`w`$. With $`A=N(u)\setminus\{w\}`$, $`B=N(v)\setminus\{w\}`$, $`C=N(w)\setminus\{u,v\}`$, and residual cell $`Z`$, the surviving graph has cell sizes
``` math
1,\quad k-1,\quad k-1,\quad k-2,\quad (k-1)(k-2).
```
The Moore common-neighbour rule makes the $`A`$–$`B`$ edges a perfect matching and the five-cell partition equitable. It also supplies a length-three replacement path for every pair whose unique length-two path used $`u`$ or $`v`$; hence every such new distance is exactly three. On the cell-constant space, the row-sum distance quotient is
``` math
\begin{pmatrix}
0&3k-3&3k-3&k-2&2(k-1)(k-2)\\
3&3k-6&2k-3&2k-4&2k^2-7k+6\\
3&2k-3&3k-6&2k-4&2k^2-7k+6\\
1&2k-2&2k-2&2k-6&2k^2-7k+5\\
2&2k-3&2k-3&2k-5&2k^2-7k+5
\end{pmatrix}.
```
Its characteristic polynomial is $`(x-k+3)R_k(x)`$.

Let $`R_A,R_B,R_C`$ be the incidence matrices from the three nonconstant cells to $`Z`$, and let $`T`$ be the adjacency matrix on $`Z`$. The Moore identity gives
``` math
\begin{gathered}
R_AR_A^{\mathsf T}=R_BR_B^{\mathsf T}=(k-2)I,\quad
R_CR_C^{\mathsf T}=(k-1)I,\\
R_AR_B^{\mathsf T}=J-I,\quad
R_AR_C^{\mathsf T}=R_BR_C^{\mathsf T}=J,\\
R_AT+R_B=J-R_A,\quad R_BT+R_A=J-R_B,\quad R_CT=J-R_C.
\end{gathered}
```
Identify $`\mathbb R^A`$ with $`\mathbb R^B`$ through the perfect matching. For $`x\in\mathbf 1_A^\perp`$, the maps $`x\mapsto(R_A^{\mathsf T}\pm R_B^{\mathsf T})x`$, and for $`y\in\mathbf 1_C^\perp`$, the map $`y\mapsto R_C^{\mathsf T}y`$, are injective with mutually orthogonal images. Together with the cell-constant space and
``` math
K=\ker R_A\cap\ker R_B\cap\ker R_C,
```
they form an orthogonal direct sum. The distance operator has matrices
``` math
\begin{pmatrix}-4&-(k-3)\\-1&0\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-2\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-1\end{pmatrix}
```
on the matched symmetric, antisymmetric, and common-neighbour modules, respectively. These give the two displayed quadratic factors and $`k-3`$ copies of each Moore linear factor. On $`K`$,
``` math
T^2+T-(k-1)I=0,
 \qquad D=-2I-T.
```
The constant direction of $`Z`$ has $`T`$-eigenvalue $`k-3`$, the symmetric, antisymmetric, and common-neighbour images have eigenvalues $`-2,0,-1`$ with dimensions $`k-2,k-2,k-3`$. Since $`T`$ has zero diagonal, its total trace is zero, and therefore $`\operatorname{tr}(T|_K)=2(k-2)`$. Dimension and trace now give the residual multiplicities; after adding the common-neighbour copies they are precisely $`M_-`$ and $`M_+`$. The full dimension count is
``` math
5+4(k-2)+2(k-3)+(k-2)(k-4)=k^2-1.
```

The value $`\delta^*(H)=k-\frac2k`$ is again the $`s=2`$ case of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a>. For strictness, the distance-increase matrix is the adjacency matrix of two copies of $`K_k`$ meeting in $`w`$, and hence has least eigenvalue
``` math
\lambda_{\min}(E_S)=\frac{k-2-\sqrt{k^2+4k-4}}2.
```
Since the parent Moore graph has score $`k-(3+\Delta)/2`$ and deletion lowers the minimum dual degree by $`2/k`$, Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">32</a> gives
``` math
\Phi(H)\ge
 \frac{3k-5-\Delta-\sqrt{k^2+4k-4}}2-\frac2k.
```
For $`k\ge6`$,
``` math
\Delta<2\sqrt{k}-\frac{3}{4\sqrt{k}},
\qquad
\sqrt{k^2+4k-4}<k+2-\frac4{k+2}.
```
The lower bound is therefore greater than
``` math
f(k)=k-\frac72-\sqrt{k}+\frac{3}{8\sqrt{k}}
       +\frac2{k+2}-\frac2k.
```
Now $`f(6)=29/12-15\sqrt6/16>0`$, since $`116^2>6\cdot45^2`$. Moreover $`f'(x)>0`$ for $`x\ge6`$: the three negative terms in $`f'(x)`$ have sum less than $`1/4+1/64+1/32<1`$, while $`2/x^2>0`$. Thus $`\Phi(H)>0`$. The direct-sum decomposition, injectivity, orthogonality, all recomputed distances, and the strict comparison are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_03_nonadjacent_puncture.py) and [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_research_extensions_exact.py). ◻

</div>

<div id="prop:deletion-stability" class="proposition">

**Proposition 32** (Deletion stability). *Let $`G`$ be connected with at least two vertices, let $`S\subseteq V(G)`$, and suppose $`H=G-S`$ is connected with at least two vertices. Put
``` math
D_0=D(G)[V(H)],
 \qquad E_S=D(H)-D_0,
```
``` math
a=\delta^*(G),
 \quad b=\delta^*(H),
 \quad \gamma=\Phi(G).
```
Then
``` math
\boxed{
 \Phi(H)\ge\gamma-(a-b)+\lambda_{\min}(E_S).
 }
```*

</div>

<div class="proof">

*Proof.* One has
``` math
D(H)+bI=(D_0+aI)+E_S-(a-b)I.
```
Principal-submatrix interlacing gives $`\lambda_{\min}(D_0+aI)\ge\gamma`$, and Weyl’s inequality gives the result. For Moore punctures, $`E_S`$ is an explicit distance-increase graph; the exact specializations are checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_research_extensions_exact.py). ◻

</div>

# Small punctures and exact Hoffman–Singleton robustness

<div id="thm:small-puncture" class="theorem">

**Theorem 33** (Small-puncture normal form). *Let $`M`$ be a degree-$`k`$ Moore graph of diameter two, let $`S\subseteq V(M)`$ have size $`s\le k-1`$, and put $`H=M-S`$. Then $`H`$ is connected, has diameter at most three, and
``` math
\boxed{\delta^*(H)=k-\frac{s}{k}.}
```
Let $`B`$ be the surviving-vertex by deleted-vertex incidence matrix, with $`B_{xz}=1`$ exactly when $`x\sim_M z`$. Then
``` math
\boxed{
 D(H)=2(J-I)-A(H)+BB^{\mathsf T}
 -\operatorname{diag}(BB^{\mathsf T}).
 }
```*

</div>

<div class="proof">

*Proof.* The case $`s=0`$ is immediate, so assume $`1\le s\le k-1`$. Let $`x,y\in V(H)`$ be nonadjacent in $`M`$, and suppose their unique common neighbour $`z`$ lies in $`S`$. For every $`a\in N_M(x)\setminus\{z\}`$, the vertices $`a,y`$ are nonadjacent and have a unique common neighbour $`b_a`$. Thus
``` math
x-a-b_a-y
```
is a length-three path. These $`k-1`$ paths are internally vertex-disjoint: a shared vertex $`b_a=b_{a'}`$ would give a four-cycle, while $`b_a=a'`$ would give a triangle through $`x`$. Besides $`z`$, at most $`s-1\le k-2`$ vertices are deleted, so one path survives. Hence a destroyed length-two path becomes distance exactly three, which proves the matrix formula.

For $`x\in V(H)`$, let $`t_x=|N_M(x)\cap S|`$. A deleted neighbour of $`x`$ is adjacent to no surviving neighbour of $`x`$, by triangle-freeness; each other deleted vertex has at most one common neighbour with $`x`$. Thus
``` math
\sum_{y\in N_H(x)}t_y\le s-t_x.
```
Consequently,
``` math
d_H^*(x)
 \ge k-\frac{s-t_x}{k-t_x}
 \ge k-\frac{s}{k},
```
where the last inequality follows from
``` math
\left(k-\frac{s-t}{k-t}\right)-\left(k-\frac{s}{k}\right)
 =\frac{t(k-s)}{k(k-t)}\ge0.
```
The intersection bound
``` math
\left|\bigcap_{z\in S}\Gamma_2(z)\right|
 \ge k^2+1-s(k+1)\ge2
```
provides a surviving vertex $`x`$ at distance two from every deleted vertex. For $`z\in S`$, let $`y_z`$ be the unique common neighbour of $`x,z`$. If $`y_z\in S`$, then the choice of $`x`$ would require $`d_M(x,y_z)=2`$, contradicting $`x\sim y_z`$. Thus all witnesses survive, each deleted vertex contributes exactly once to the neighbour-degree deficit, and equality is attained. The replacement paths, boundary case $`s=k-1`$, distance formula, and attainment step are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_12_small_puncture.py). ◻

</div>

<div id="cor:uniform-deletion" class="corollary">

**Corollary 34** (Uniform deletion stability). *Under the hypotheses of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a>, put
``` math
t_x=|N_M(x)\cap S|,
 \qquad
 \tau(S)=\max_{x\in V(M-S)}t_x.
```
Then
``` math
\boxed{
 \Phi(M-S)\ge
 k-\frac{3+\sqrt{4k-3}}2-\frac{s}{k}-\tau(S).
 }
```
In particular, the deletion is a strict counterexample whenever the right-hand side is positive. Since $`\tau(S)\le s`$, every deletion of $`s`$ vertices is strict whenever
``` math
\boxed{
 s\left(1+\frac 1k\right)
 <k-\frac{3+\sqrt{4k-3}}2.
 }
```
For $`k>3`$, equivalently, every deletion of at most
``` math
r_k=\min\left\{
 k-1,\
 \left\lceil
 \frac{k}{k+1}\left(k-\frac{3+\sqrt{4k-3}}2\right)
 \right\rceil-1
 \right\}
```
vertices is strict. In particular, $`r_7=2`$; for a hypothetical degree-$`57`$ Moore graph, whose existence remains open ([Smith and Montemanni 2026](#ref-SmithMontemanni2026)), one would have $`r_{57}=47`$.*

</div>

<div class="proof">

*Proof.* By Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a>, the distance-increase matrix is
``` math
E_S=BB^{\mathsf T}-\operatorname{diag}(t_x).
```
Since $`BB^{\mathsf T}\succeq0`$ and $`\operatorname{diag}(t_x)\preceq\tau(S)I`$, one has $`\lambda_{\min}(E_S)\ge-\tau(S)`$. The parent Moore graph has score
``` math
\Phi(M)=k-\frac{3+\sqrt{4k-3}}2,
```
and Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a> shows that deletion lowers the minimum dual degree by $`s/k`$. Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">32</a> now gives the first bound. The second follows from $`\tau(S)\le s`$, and solving its strict scalar inequality for the largest integral $`s`$ gives $`r_k`$. ◻

</div>

<div id="thm:hs-radius" class="theorem">

**Theorem 35** (Hoffman–Singleton robustness radius). *Let $`M`$ be the Hoffman–Singleton graph. Every induced graph $`M-S`$ with $`|S|\le5`$ is a strict counterexample to WOW-284. This is sharp in the universal sense: there exists a six-vertex set whose deletion is not strict. Hence the universal vertex-deletion robustness radius is exactly five.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">33</a> gives
``` math
\delta^*(M-S)=\frac{49-|S|}{7}.
```
Corollary <a href="#cor:uniform-deletion" data-reference-type="ref" data-reference="cor:uniform-deletion">34</a> already proves strictness uniformly for $`|S|\le2`$. To obtain the sharp universal radius, two explicitly stored permutations are verified edge-by-edge as automorphisms of the coordinate graph; the group they generate has order $`252000`$. Their orbits on deletion sets of sizes $`0,1,2,3,4,5`$ have counts
``` math
1,1,2,4,11,33.
```
For every one of the $`52`$ representatives, exact fraction arithmetic gives
``` math
7D(M-S)+(49-|S|)I\succ0.
```
Orbit-size sums equal $`\binom{50}{s}`$, so every labelled set is covered.

For sharpness, delete
``` math
\{P_{2,4},P_{3,1},P_{3,4},Q_{2,1},Q_{3,4},Q_{4,4}\}.
```
The resulting graph has $`\delta^*=43/7`$, while an exact $`LDL^{\mathsf T}`$ decomposition of $`7D+43I`$ has exactly one negative and no zero pivot. Thus it is not strict. Generator action, orbit exhaustion, BFS distances, the small-puncture formula, and a handwritten rational $`LDL^{\mathsf T}`$ implementation are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_13_hs_robustness.py). ◻

</div>

<div class="remark">

*Remark 36*. The theorem asserts that every deletion through size five succeeds and that at least one deletion of size six fails. It does not assert that every six-vertex deletion fails.

</div>

# Equality and obstructions to natural construction families

<div id="thm:equality-boundary" class="theorem">

**Theorem 37** (Equality boundary). *Let $`G`$ be connected, $`k`$-regular, of girth at least five and diameter three. Then
``` math
\Phi(G)=0
 \quad\Longleftrightarrow\quad
 \max_{\theta\ne k}|\theta+1|=\sqrt{2k-2}.
```
Equivalently, $`D+kI`$ is positive semidefinite and singular. If $`2k-2`$ is not a square, the two boundary adjacency eigenvalues occur with equal multiplicity, so the distance eigenvalue $`-k`$ has even multiplicity. If $`2k-2`$ is a square, then $`k=2r^2+1`$ for some integer $`r`$.*

</div>

<div class="proof">

*Proof.* This is immediate from Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">6</a>. In the nonsquare case, the two boundary values are algebraic conjugates, so their multiplicities in the integral characteristic polynomial agree. In the square case, $`2k-2=s^2`$ forces $`s`$ even. The exact scalar audit is [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_equality_boundary.py). ◻

</div>

Jørgensen’s $`9`$-regular order-$`96`$ graph of girth five is an exact equality case:
``` math
\delta^*=9,
 \qquad \lambda_{\min}(D)=-9,
```
with multiplicity eight. The construction is due to Jørgensen ([Jørgensen 2005](#ref-Jorgensen2005)); the three local graph representations, handwritten graph6 decoder, characteristic polynomials, root intervals, and provenance boundary are checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_09_jorgensen96.py).

## A prime-field obstruction

For an odd prime $`q\ge7`$ and $`1\le m\le q`$, define $`G(q,m)`$ on vertices $`P_{i,j},Q_{k,\ell}`$, with $`0\le i,k<m`$ and $`j,\ell\in\mathbb F_q`$, by
``` math
\begin{align*}
P_{i,j}&\sim P_{i,j\pm1},\\
Q_{k,\ell}&\sim Q_{k,\ell\pm2},\\
P_{i,j}&\sim Q_{k,ik+j}.
\end{align*}
```
This is a balanced specialization of known finite-field girth-five constructions ([Abreu et al. 2008](#ref-AbreuEtAl2008)). It is $`(m+2)`$-regular. A coordinate common-neighbour calculation shows that it has no triangle or $`4`$-cycle for $`q\ge7`$: for a cross pair, the possible same-side common neighbours require residues in the disjoint sets $`\{\pm1\}`$ and $`\{\pm2\}`$.

<div id="thm:prime-field" class="theorem">

**Theorem 38**. *If $`G(q,m)`$ has diameter three, then it is not a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">10</a> excludes $`m\le3`$. The zero Fourier block has eigenvalues $`m+2`$, $`2-m`$, and $`2`$ with multiplicity $`2m-2`$; the shifted WOW window leaves only $`m\in\{4,5,6\}`$. Let $`\omega=e^{2\pi\mathrm i/q}`$. On the nonzero character $`t=1`$, the adjacency block has form
``` math
\begin{pmatrix}aI&M\\M^*&bI\end{pmatrix},
 \qquad a=2\cos\frac{2\pi}{q},
 \quad b=2\cos\frac{4\pi}{q},
 \quad M_{ik}=\omega^{ik}.
```
If $`\sigma`$ is a singular value of $`M`$, the associated two-dimensional invariant subspace carries $`\bigl(\begin{smallmatrix}a&\sigma\\\sigma&b\end{smallmatrix}\bigr)`$. Since $`\|M\|_F^2=m^2`$, one singular value satisfies $`\sigma^2\ge m`$, and the block has a nonprincipal eigenvalue at least
``` math
\sqrt m+\frac{a+b}{2}
 \ge \sqrt m+\cos(\pi/7)-\frac12.
```
For $`q\ge7`$, both $`\cos(2\pi/q)`$ and $`\cos(4\pi/q)`$ increase with $`q`$, so their sum is minimized at $`q=7`$. The last inequality then uses $`2\cos(2\pi/7)+2\cos(4\pi/7)=2\cos(\pi/7)-1`$. Moreover $`\cos(\pi/7)>\sqrt3/2`$, and the increasing function $`h(m)=\sqrt{2m+2}-\sqrt m`$ satisfies
``` math
h(m)\le h(6)=\sqrt{14}-\sqrt6
 <\frac{27}{20}<\frac{\sqrt3+1}{2}.
```
Thus the displayed nonprincipal eigenvalue lies above $`-1+\sqrt{2m+2}`$ for $`m=4,5,6`$. The common-neighbour case split, Fourier reduction, radical comparisons, and exact $`q=7`$ controls are independently checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_08_prime_field.py). ◻

</div>

## Layer-respecting matching deletions

For $`\pi\in S_5`$, delete the perfect matching
``` math
\mathcal M_\pi=\bigl\{\{P_{i,j},Q_{\pi(i),i\pi(i)+j}\}:i,j\in\mathbb F_5\bigr\}
```
from the Hoffman–Singleton graph.

<div id="thm:matching-deletions" class="theorem">

**Theorem 39**. *Each deletion produces a connected simple $`6`$-regular graph of order $`50`$, girth five, and diameter four. The $`120`$ labelled graphs form exactly two isomorphism classes. The $`20`$ affine permutations have
``` math
\lambda_{\min}(D)=-13,
 \qquad \Phi=-7,
```
and the $`100`$ nonaffine permutations have
``` math
\lambda_{\min}(D)=-6-\sqrt{61},
 \qquad \Phi=-\sqrt{61}.
```
Thus none of these graphs is a counterexample.*

</div>

<div class="proof">

*Proof.* Every $`P_{i,j}`$ occurs once in $`\mathcal M_\pi`$; for a fixed $`Q_{k,\ell}`$, the unique incident matching edge is obtained from $`i=\pi^{-1}(k)`$ and $`j=\ell-ik`$. Thus $`\mathcal M_\pi`$ is a perfect matching, and its deletion leaves a simple $`6`$-regular graph. Deleting edges cannot create a short cycle, while the same-layer pentagons remain; exact breadth-first search gives connectedness and diameter four.

Explicit type-preserving and type-swapping coordinate automorphisms generate orbits of sizes $`20`$ and $`100`$. The representatives have different adjacency characteristic polynomials, so the orbits are distinct isomorphism classes. Exact distance characteristic polynomials and Sturm separators give the stated least roots. All $`120`$ matchings, $`400`$ coordinate maps, $`48{,}000`$ matching images, orbit coverage, graph hypotheses, and root certificates are checked by [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/scripts/verify_proof_audit_07_layer_matchings.py). ◻

</div>

# Exact computation and formal verification

The analytic arguments above are primary. Exact computation is used in three roles: to certify explicitly labelled finite graphs, to exhaust precisely specified finite orbit families, and to check symbolic identities whose derivations are supplied. No theorem-level sign or eigenvalue ordering uses floating-point arithmetic. The exact computations use SymPy and NetworkX ([<span class="nocase">Meurer et al.</span> 2017](#ref-MeurerEtAl2017); [Hagberg et al. 2008](#ref-HagbergSchultSwart2008)).

The accompanying release archives the labelled graph data, exact rational and polynomial certificates, and finite-orbit records used here, so the computer-assisted steps are reproducible without a file-by-file index in the paper.

The explicit $`50`$-vertex counterexample is fully formalized in Lean 4.31 with Mathlib 4.31 ([Moura and Ullrich 2021](#ref-deMouraUllrich2021); [The mathlib Community 2020](#ref-Mathlib2020)). The development pins the exact toolchain and dependency revision in [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/lean/lean-toolchain) and [`#1`](https://github.com/SamPetkov/wow284/blob/v2.2.6/lean/lake-manifest.json). It checks the coordinate graph, regularity, the exhaustive common-neighbour certificate, girth five, the adjacency-square and distance-matrix identities, and an exact rational diagonalization with multiplicities. Thus the result is verified at graph level, including its least distance eigenvalue and strict WOW-284 gap.

Lean also kernel-checks finite spectral certificates attached to the explicit constructions of orders $`38,39,40,42`$. At orders $`38,39,42`$, they certify the dual-degree data and positive definiteness of the relevant shifted distance matrix. At order $`40`$, they certify an invertible exact diagonalization, multiplicities, least eigenvalue $`-5`$, dual degree six, and gap one. These are finite matrix certificates rather than end-to-end `SimpleGraph.dist` formalizations.

Separately, Lean formalizes the analytic optimization statement in Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">16</a>. For every integer $`k\ge4`$ and every admissible finitely supported expansion
``` math
f=\sum_i c_iF_i,
  \qquad c_0>0,
  \qquad c_i\ge0\quad(i\ge5),
  \qquad f\vert_{I_k}\le0,
```
it proves
``` math
B_kc_0\le f(k),
  \qquad B_k=\frac{(k+2)(k^2+3)}6.
```
The formal development defines the coefficient family of the displayed quartic $`f_*`$, proves that it is admissible and attains equality, and proves that every equality case is its unique positive scalar multiple, both as a polynomial and at coefficient level. The public Lean development is sorry-free and kernel-checked by Lean 4.31.

This LP formalization is deliberately graph-independent. It does not formalize the trace interpretation of the $`F_i(A)`$, the girth-five vanishing and nonnegativity statements, or the passage from the LP inequality to graph-order bounds. The integral-slack consequences, signed-complement theory, puncture spectra, and deletion results lie outside this Lean development. They are proved in the text using the analytic and, where explicitly identified, exact computer-assisted components. This is the precise scope of the Lean claims in the paper.

# Broader mathematical questions

The mechanisms in this paper point beyond the conjecture that motivated them. They connect extremal polynomial certificates, local positive-semidefinite constraints, perturbations of metric operators, exact computation, and formal proof. At that methodological level, they suggest the following questions.

1.  Given an optimal polynomial or semidefinite certificate for a global spectral inequality, when do the principal minors of its slack operator form a complete hierarchy of local constraints? Can rank or flat-extension conditions force finite convergence and reconstruct the extremal discrete objects?

2.  Is there a general stability theory for spectral inequalities in which a small global defect forces proximity to a structured algebraic model, and local perturbations distinguish sporadic objects from finite shadows of infinite families?

3.  Which one-variable spectral arguments survive when homogeneity or commutativity is lost? Can degree-weighted operators, nonbacktracking operators, or matrix-valued orthogonal polynomials provide comparably sharp certificates for irregular or multitype systems?

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof exploration, and Lean formalization. The author assumes full responsibility for the mathematics, attribution, and conclusions. The source, exact certificates, and build instructions are available at [`github.com/SamPetkov/wow284`](https://github.com/SamPetkov/wow284) and correspond to release `v2.2.6`.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AbreuEtAl2008" class="csl-entry">

Abreu, Marién, Martin Funk, Domenico Labbate, and Vito Napolitano. 2008. “A Family of Regular Graphs of Girth 5.” *Discrete Mathematics* 308 (10): 1810–15. <https://doi.org/10.1016/j.disc.2007.04.031>.

</div>

<div id="ref-AouchicheHansen2014" class="csl-entry">

Aouchiche, Mustapha, and Pierre Hansen. 2014. “Distance Spectra of Graphs: A Survey.” *Linear Algebra and Its Applications* 458: 301–86. <https://doi.org/10.1016/j.laa.2014.06.010>.

</div>

<div id="ref-Backelin2015" class="csl-entry">

Backelin, Jörgen. 2015. *Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49*. <https://arxiv.org/abs/1511.08128>.

</div>

<div id="ref-CameronEtAl1976" class="csl-entry">

Cameron, Peter J., Jean-Marie Goethals, Johan J. Seidel, and Ernest E. Shult. 1976. “Line Graphs, Root Systems, and Elliptic Geometry.” *Journal of Algebra* 43 (1): 305–27. <https://doi.org/10.1016/0021-8693(76)90162-9>.

</div>

<div id="ref-CioabaEtAl2016" class="csl-entry">

Cioabă, Sebastian M., Jack H. Koolen, Hiroshi Nozaki, and Jason R. Vermette. 2016. “Maximizing the Order of a Regular Graph of Given Valency and Second Eigenvalue.” *SIAM Journal on Discrete Mathematics* 30 (3): 1509–25. <https://doi.org/10.1137/15M1030935>.

</div>

<div id="ref-CvetkovicEtAl2004" class="csl-entry">

Cvetković, Dragoš, Peter Rowlinson, and Slobodan Simić. 2004. *Spectral Generalizations of Line Graphs: On Graphs with Least Eigenvalue -2*. Cambridge University Press. <https://doi.org/10.1017/CBO9780511751752>.

</div>

<div id="ref-vanDamHaemers2003" class="csl-entry">

Dam, Edwin R. van, and Willem H. Haemers. 2003. “Which Graphs Are Determined by Their Spectrum?” *Linear Algebra and Its Applications* 373: 241–72. <https://doi.org/10.1016/S0024-3795(03)00483-X>.

</div>

<div id="ref-Fajtlowicz1998" class="csl-entry">

Fajtlowicz, Siemion. 1998. *Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti*. Technical report. University of Houston.

</div>

<div id="ref-Fiol2016" class="csl-entry">

Fiol, Miquel Àngel. 2016. “Quotient-Polynomial Graphs.” *Linear Algebra and Its Applications* 488: 363–76. <https://doi.org/10.1016/j.laa.2015.09.053>.

</div>

<div id="ref-GreavesEtAl2015" class="csl-entry">

Greaves, Gary, Jack H. Koolen, Akihiro Munemasa, Yoshio Sano, and Tetsuji Taniguchi. 2015. “Edge-Signed Graphs with Smallest Eigenvalue Greater Than -2.” *Journal of Combinatorial Theory, Series B* 110: 90–111. <https://doi.org/10.1016/j.jctb.2014.07.006>.

</div>

<div id="ref-Hafner2003" class="csl-entry">

Hafner, Paul R. 2003. “The Hoffman–Singleton Graph and Its Automorphisms.” *Journal of Algebraic Combinatorics* 18 (1): 7–12. <https://doi.org/10.1023/A:1025136524481>.

</div>

<div id="ref-HagbergSchultSwart2008" class="csl-entry">

Hagberg, Aric A., Daniel A. Schult, and Pieter J. Swart. 2008. “Exploring Network Structure, Dynamics, and Function Using NetworkX.” *Proceedings of the 7th Python in Science Conference*, 11–15. <https://doi.org/10.25080/TCWV9851>.

</div>

<div id="ref-HowladerPanigrahi2022" class="csl-entry">

Howlader, Aditi, and Pratima Panigrahi. 2022. “On the Distance Spectrum of Minimal Cages and Associated Distance Biregular Graphs.” *Linear Algebra and Its Applications* 636: 115–33. <https://doi.org/10.1016/j.laa.2021.11.014>.

</div>

<div id="ref-Jorgensen2005" class="csl-entry">

Jørgensen, Leif K. 2005. “Girth 5 Graphs from Relative Difference Sets.” *Discrete Mathematics* 293 (1–3): 177–84. <https://doi.org/10.1016/j.disc.2004.08.029>.

</div>

<div id="ref-KlinMuzychukZivAv2009" class="csl-entry">

Klin, Mikhail, Mikhail Muzychuk, and Matan Ziv-Av. 2009. “Higmanian Rank-5 Association Schemes on 40 Points.” *Michigan Mathematical Journal* 58 (1): 255–84. <https://doi.org/10.1307/mmj/1242071692>.

</div>

<div id="ref-KoolenEtAl2025" class="csl-entry">

Koolen, Jack H., Kefan Yu, Xiaoye Liang, Harrison Choi, and Greg Markowsky. 2025. “Non-Geometric Distance-Regular Graphs of Diameter at Least 3 with Smallest Eigenvalue at Least -3.” *European Journal of Combinatorics* 126: 104118. <https://doi.org/10.1016/j.ejc.2024.104118>.

</div>

<div id="ref-Meringer1999" class="csl-entry">

Meringer, Markus. 1999. “Fast Generation of Regular Graphs and Construction of Cages.” *Journal of Graph Theory* 30 (2): 137–46. [https://doi.org/10.1002/(SICI)1097-0118(199902)30:2\<137::AID-JGT7\>3.0.CO;2-G](https://doi.org/10.1002/(SICI)1097-0118(199902)30:2<137::AID-JGT7>3.0.CO;2-G).

</div>

<div id="ref-MeurerEtAl2017" class="csl-entry">

<span class="nocase">Meurer, Aaron et al.</span> 2017. “SymPy: Symbolic Computing in Python.” *PeerJ Computer Science* 3: e103. <https://doi.org/10.7717/peerj-cs.103>.

</div>

<div id="ref-deMouraUllrich2021" class="csl-entry">

Moura, Leonardo de, and Sebastian Ullrich. 2021. “The Lean 4 Theorem Prover and Programming Language.” *Automated Deduction—CADE 28*, Lecture notes in computer science, vol. 12699: 625–35. <https://doi.org/10.1007/978-3-030-79876-5_37>.

</div>

<div id="ref-Nozaki2015" class="csl-entry">

Nozaki, Hiroshi. 2015. “Linear Programming Bounds for Regular Graphs.” *Graphs and Combinatorics* 31 (6): 1973–84. <https://doi.org/10.1007/s00373-015-1613-7>.

</div>

<div id="ref-OKeefeWong1979" class="csl-entry">

O’Keefe, M., and Pak-Ken Wong. 1979. “A Smallest Graph of Girth 5 and Valency 6.” *Journal of Combinatorial Theory, Series B* 26 (2): 145–49. <https://doi.org/10.1016/0095-8956(79)90052-2>.

</div>

<div id="ref-SmithMontemanni2026" class="csl-entry">

Smith, Derek H., and Roberto Montemanni. 2026. “The Moore Graph of Diameter 2 and Degree 57 via Cyclic Derangements.” *Axioms* 15 (5): 332. <https://doi.org/10.3390/axioms15050332>.

</div>

<div id="ref-Mathlib2020" class="csl-entry">

The mathlib Community. 2020. “The Lean Mathematical Library.” *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 367–81. <https://doi.org/10.1145/3372885.3373824>.

</div>

<div id="ref-Wong1979" class="csl-entry">

Wong, Pak-Ken. 1979. “On the Uniqueness of the Smallest Graph of Girth 5 and Valency 6.” *Journal of Graph Theory* 3 (4): 407–9. <https://doi.org/10.1002/jgt.3190030413>.

</div>

</div>
