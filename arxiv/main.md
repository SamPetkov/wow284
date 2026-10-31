# Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284

**Samuil Petkov**<br>
Department of Physics, École normale supérieure, Université PSL, Paris, France<br>
<samuil.petkov@phys.ens.psl.eu><br>

> Reading copy generated on 31 October 2026 from `arxiv/main.tex` and its current bibliography.
> The [TeX source](main.tex) and [compiled PDF](main.pdf) are authoritative if this rendering differs in notation, citations, or layout.

<a id="abstract"></a>

# Abstract

The dual degree of a vertex is the average degree of its neighbours. WOW-284 conjectures that the minimum dual degree is at most minus the least eigenvalue of the distance matrix. The graph is required to be finite, simple and connected, with at least three vertices and girth at least five. We give exact counterexamples on $38,39,40,42$, and $50$ vertices, for which the inequality is strictly reversed.

For regular graphs of girth at least five and diameter three, a polynomial identity relates the distance and adjacency matrices. It turns strict failure of WOW-284 into an interval condition on adjacency eigenvalues. This condition also bounds the order without a diameter assumption. Let $G$ be finite, simple, connected and $k$-regular, with girth at least five and integer $k\ge4$. If every nonprincipal adjacency eigenvalue $\theta$ satisfies $|\theta+1|\le\sqrt{2k-2}$, then $|V(G)|<(k+2)(k^2+3)/6$. For regular counterexamples of diameter three, an integer matrix derived from the optimal polynomial gives stronger restrictions.

Deleting any set of at most five vertices from the Hoffman–Singleton graph leaves a strict counterexample. We give a six-vertex deletion for which strictness fails. If a degree-57 Moore graph of diameter two exists, deleting any set of at most $56$ vertices leaves a connected strict counterexample. The finite computations use exact arithmetic.

<a id="sec:introduction"></a>

# WOW-284 and the main results

Let $G$ be a finite simple connected graph of order $n=|V(G)|\ge2$. Let $A=A(G)$ and $D=D(G)$ be its adjacency and distance matrices, let $I$ and $J$ denote the identity and all-ones matrices of order $n$, and let $\mathbf 1$ be the all-ones vector. Write $d(v)$ for the degree of $v$, $N(v)$ for its open neighbourhood, and, for $S\subseteq V(G)$, let $G-S$ denote the subgraph induced by $V(G)\setminus S$. Define $$d^*(v)=\frac1{d(v)}\sum_{u\in N(v)}d(u),
 \qquad
 \delta^*(G)=\min_{v\in V(G)}d^*(v).$$ Here $d_G(u,v)$ is the length of a shortest path from $u$ to $v$, so $D=(d_G(u,v))_{u,v\in V(G)}$. Its eigenvalues are ordered as $$\partial_1(G)\ge\cdots\ge\partial_n(G),
 \qquad \partial_n(G)=\lambda_{\min}(D(G)).$$ Let $e_v$ denote the standard coordinate vector at $v$. For a square matrix $M$, write $\chi_M(t)=\det(tI-M)$ for its characteristic polynomial, with $I$ of the matching order. Aouchiche and Hansen record the following Graffiti conjecture as Conjecture 7.16 and attribute it to Fajtlowicz’s 1998 *Written on the Wall* report ([Fajtlowicz 1998](#ref-Fajtlowicz1998)) (see also ([Aouchiche and Hansen 2014](#ref-AouchicheHansen2014), Conjecture 7.16)).

<div class="wowconjecture">

**Conjecture (WOW-284)**. *If $G$ has order at least three and girth at least five, then $$\delta^*(G)\le-\lambda_{\min}(D(G)).$$*

</div>

For every finite simple connected graph of order at least two, put $$\Phi(G)=\delta^*(G)+\lambda_{\min}(D(G)).$$ Among graphs satisfying the conjecture’s hypotheses, $G$ is a strict counterexample precisely when $\Phi(G)>0$.

The initial disproof is short. A Moore graph of diameter two is a regular graph whose radius-two ball contains every vertex and attains the order bound imposed by its degree. A degree-$k$ Moore graph of diameter two ([Hoffman and Singleton 1960](#ref-HoffmanSingleton1960)) has $$A^2=(k-1)I-A+J,
 \qquad
 D=2J-2I-A,$$ and hence $$\delta^*(G)=k,
 \qquad
 \lambda_{\min}(D)=-\frac{3+\sqrt{4k-3}}2.$$ The conjecture holds on these graphs exactly for $k\le3$, with equality at $k=3$, and fails for every realizable $k>3$. The degree-seven Hoffman–Singleton graph therefore gives a gap of three.

The same Hoffman–Singleton counterexample is recorded in a public Capy Build transcript ([Capy Build 2026](#ref-CapyBuild2026)) and in a verification note by Wilbanks and Annie ([Wilbanks and Annie 2026](#ref-WilbanksAnnie2026)).

Howlader and Panigrahi already give the distance spectra of Moore graphs, including the Hoffman–Singleton graph ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022), Theorem 2.5(1)). The distance-polynomial framework is developed in ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022); [Fiol 2016](#ref-Fiol2016)). Nonbacktracking linear-programming bounds are due to Nozaki ([Nozaki 2015](#ref-Nozaki2015)); related spectral-Moore bounds appear in ([Cioabă et al. 2016](#ref-CioabaEtAl2016)). We use these methods to derive order restrictions from the WOW-284 spectral window and to study vertex deletion. Our examples are not claimed to exhaust all counterexamples, and the order-$38$ example is not claimed minimal. Appendix <a href="#sec:verification" data-reference-type="ref" data-reference="sec:verification">I</a> records the exact computations and the scope of the Lean verification.

For a connected regular graph, we call the adjacency eigenvalues other than its degree eigenvalue nonprincipal.

The paper follows two lines of argument. For regular graphs of diameter three, the distance-polynomial identity turns strict failure of WOW-284 into an interval condition on the nonprincipal adjacency eigenvalues (Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a>). A polynomial trace bound restricts the order. Evaluating the optimal polynomial at the adjacency matrix also gives a matrix of integer combinations of short-walk counts. Subtracting a constant all-ones term and adjusting the diagonal gives the integral excess matrix of Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a>. The excess matrix has integral entries, while the associated slack matrix has nonnegative principal minors. Together these give stronger order and cycle constraints. These lead to the three-to-one bound (Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">6.1</a>) and necessary conditions at the unresolved degree-six, order-$50$ boundary. The exact polynomial optimum is proved in Section <a href="#sec:lp" data-reference-type="ref" data-reference="sec:lp">5</a>. It is an optimum within the stated polynomial class, not a claim that the graph-order bound is best possible.

The degree and diameter restrictions narrow the search: every regular strict counterexample has degree at least six and diameter at most four, and a diameter-four example would have degree at least ten (Theorems <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">4.2</a>, <a href="#thm:endpoint-diameter" data-reference-type="ref" data-reference="thm:endpoint-diameter">4.3</a>, and <a href="#thm:diameter-four" data-reference-type="ref" data-reference="thm:diameter-four">4.4</a>). We give the detailed arithmetic and cycle restrictions where they enter the proofs.

The second argument concerns deletion. Deleting vertices can increase the distances between those left behind, so taking a principal submatrix of the old distance matrix is not enough. For small deletions from a Moore graph, we identify exactly which distances increase. This correction gives general stability bounds (Section <a href="#sec:punctures" data-reference-type="ref" data-reference="sec:punctures">7</a>); Appendix <a href="#app:small-deletion-spectra" data-reference-type="ref" data-reference="app:small-deletion-spectra">B</a> gives the exact one- and two-deletion spectra. For Hoffman–Singleton, the bounds prove strictness through three deletions; exact orbit certificates handle four and five. A six-vertex deletion shows that the universal radius is five (Theorem <a href="#thm:hs-radius" data-reference-type="ref" data-reference="thm:hs-radius">8.3</a>).

<a id="sec:examples"></a>

# Dual degree, Moore graphs, and explicit counterexamples

<a id="dual-degree-and-the-size-of-a-radius-two-ball"></a>

## Dual degree and the size of a radius-two ball

Dual degree has a simple local interpretation when triangles and four-cycles are absent: it measures the size of a radius-two ball relative to the degree of its centre. This count also explains why a regular graph of girth at least five and diameter two is a Moore graph.

For $v\in V(G)$, write $\Gamma_i(v)$ for the distance-$i$ sphere and $B_2(v)=\Gamma_0(v)\cup\Gamma_1(v)\cup\Gamma_2(v)$.

<div id="prop:radius-two" class="proposition">

**Proposition 2.1** (Second-degree identity). *If $G$ contains no triangle and no $4$-cycle, then $$|B_2(v)|=1+\sum_{u\in N(v)}d(u),
 \qquad
 d^*(v)=\frac{|B_2(v)|-1}{d(v)}.$$*

</div>

<div class="proof">

*Proof.* For distinct neighbours $u,w$ of $v$, the sets $N(u)\setminus\{v\}$ and $N(w)\setminus\{v\}$ are disjoint; an intersection would form a $4$-cycle, and a member in $N(v)$ would form a triangle. These sets partition $\Gamma_2(v)$, so $$|\Gamma_2(v)|=\sum_{u\in N(v)}(d(u)-1).$$ Adding the centre and first sphere proves the first identity, which is Backelin’s Lemma 2.1 ([Backelin 2015](#ref-Backelin2015)); division by $d(v)$ gives the normalized second identity. ◻

</div>

<a id="when-moore-graphs-violate-wow-284"></a>

## When Moore graphs violate WOW-284

<div id="thm:moore-threshold" class="theorem">

**Theorem 2.2**. *Let $M$ be a degree-$k$ Moore graph of diameter two, $k\ge2$. Then $$|V(M)|=k^2+1,
 \qquad g(M)=5,
 \qquad \delta^*(M)=k,$$ $$\lambda_{\min}(D(M))=-\frac{3+\sqrt{4k-3}}2,$$ and $$\Phi(M)=k-\frac{3+\sqrt{4k-3}}2.$$ Thus $M$ satisfies WOW-284 exactly for $k\le3$, with equality exactly at $k=3$.*

</div>

<div class="proof">

*Proof.* Attainment of the Moore bound determines every pair of vertices: adjacent vertices have no common neighbour, and nonadjacent vertices have exactly one. It also gives a five-cycle through every edge. Indeed, given an edge $uv$, choose $x\in N(u)\setminus\{v\}$ and $y\in N(v)\setminus\{u\}$. The vertices $x,y$ cannot be adjacent, since that would create a four-cycle; their unique common neighbour therefore completes a five-cycle through $uv$. The common-neighbour counts give the matrix identity $$A^2=(k-1)I-A+J.$$ On $\mathbf 1^\perp$, the nonprincipal adjacency eigenvalues are the roots $$r,s=\frac{-1\pm\sqrt{4k-3}}2.$$ If $m_r,m_s$ are their multiplicities, then $$m_r+m_s=k^2,\qquad k+m_rr+m_ss=0.$$ Consequently $$m_r=\frac{k(k\sqrt{4k-3}+k-2)}{2\sqrt{4k-3}},
 \qquad
 m_s=\frac{k(k\sqrt{4k-3}-k+2)}{2\sqrt{4k-3}},$$ and both roots occur. We can now pass from adjacency to distance eigenvalues. Every nonedge has distance two, so $D=2J-2I-A$, and the least distance eigenvalue is $-2-r=-(3+\sqrt{4k-3})/2$. Since regularity gives $\delta^*=k$, comparison with the dual degree reduces to $$(2k-3)^2-(4k-3)=4(k-1)(k-3)$$ This gives the stated threshold. The exact scalar and finite checks are independently repeated by [`scripts/verify_regular_score_calculus.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_regular_score_calculus.py). ◻

</div>

<a id="the-hoffmansingleton-graph-in-coordinates"></a>

## The Hoffman–Singleton graph in coordinates

All subscripts below lie in $\mathbb F_5=\mathbb Z/5\mathbb Z$. Let $$V(M)=\{P_{i,j}:i,j\in\mathbb F_5\}\mathbin{\dot\cup}
      \{Q_{k,\ell}:k,\ell\in\mathbb F_5\},$$ with edges $$\begin{aligned}
 P_{i,j}&\sim P_{i,j\pm1},\\
 Q_{k,\ell}&\sim Q_{k,\ell\pm2},\\
 P_{i,j}&\sim Q_{k,ik+j}.
\end{aligned}$$ This is Hafner’s affine-coordinate form of the Hoffman–Singleton graph after a minor reindexing ([Hafner 2003](#ref-Hafner2003)).

<div id="prop:hs-coordinate" class="proposition">

**Proposition 2.3**. *The coordinate construction is a simple connected $7$-regular graph on $50$ vertices. Adjacent pairs have no common neighbour and nonadjacent pairs have exactly one. Consequently it has girth five, diameter two, and $$\operatorname{Spec}D(M)=\{91^{(1)},1^{(21)},(-4)^{(28)}\}.$$ In particular, $\delta^*(M)=7$ and $\Phi(M)=3$.*

</div>

<div class="proof">

*Proof.* The neighbourhoods are $$\begin{aligned}
N(P_{i,j})&=\{P_{i,j-1},P_{i,j+1}\}
 \cup\{Q_{k,ik+j}:k\in\mathbb F_5\},\\
N(Q_{k,\ell})&=\{Q_{k,\ell-2},Q_{k,\ell+2}\}
 \cup\{P_{i,\ell-ik}:i\in\mathbb F_5\}.
\end{aligned}$$ Each neighbourhood has seven distinct entries. To check the common-neighbour rule, first take two $P$-vertices in the same layer. The $5$-cycle contributes no common neighbour for an adjacent pair and one for a nonadjacent pair; a common $Q$-neighbour would force their second coordinates to agree. For vertices in distinct $P$-layers, the equation $(i-i')k=j'-j$ determines a unique common $Q$-neighbour. The $Q$-vertices satisfy the same rule: within a layer the $5$-cycle uses steps $\pm2$, and between layers there is a unique common $P$-neighbour. Finally, for a cross pair $P_{i,j},Q_{k,\ell}$, put $r=\ell-(ik+j)$. The pair is adjacent when $r=0$; it has one common $P$-neighbour when $r\in\{\pm1\}$, and one common $Q$-neighbour when $r\in\{\pm2\}$. These cases exhaust the five residues. The claimed geometry now follows from Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2.2</a>. For degree $7$, the multiplicity equations in its proof give adjacency multiplicities $28$ at $2$ and $21$ at $-3$, and hence the displayed distance spectrum. The exhaustive pair certificate, integer distances from breadth-first search (BFS), characteristic polynomial, and exact positive-definiteness check are in [`scripts/verify_exact.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_exact.py). ◻

</div>

<a id="smaller-counterexamples-and-second-distance-spheres"></a>

## Smaller counterexamples and second distance spheres

The same coordinates give smaller counterexamples by deleting a Petersen subgraph and then one or two further vertices. A second subconstituent gives another regular example.

Let $$\mathcal P=\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}.$$ The induced graph $M[\mathcal P]$ is a Petersen graph. Put $$R=M-\mathcal P,
 \quad H_{39}=R-P_{1,0},
 \quad H_{38}=R-\{P_{1,0},P_{1,1}\},$$ and let $X_{42}$ be the second subconstituent of $P_{0,0}$, namely the graph induced by the vertices at distance two from it.

<div id="thm:explicit-examples" class="theorem">

**Theorem 2.4**. *The following are strict counterexamples. $$\begin{array}{c@{\quad}c@{\quad}c@{\quad}c}
\toprule
G&|V(G)|&\delta^*(G)&\lambda_{\min}(D(G))\\
\midrule
H_{38}&38&17/3&-3-\sqrt7\\
H_{39}&39&35/6&>-35/6\\
R&40&6&-5\\
X_{42}&42&6&-5\\
M&50&7&-4\\
\bottomrule
\end{array}$$ The entry for $H_{39}$ records an exact strict lower bound obtained from positive definiteness of $6D+35I$; it is not a decimal approximation to the least eigenvalue. Moreover, all $40$ labelled singleton deletions of $R$ and all $120$ labelled deletions of the endpoints of an edge of $R$ are strict counterexamples; within each family, the distance characteristic polynomial is constant.*

</div>

<div class="proof">

*Proof.* The regular examples can be read from known adjacency spectra. The graph $R$ is the Anstee–Robertson graph, the unique $(6,5)$-cage. O’Keefe and Wong proved minimality, and Wong proved uniqueness ([O’Keefe and Wong 1979](#ref-OKeefeWong1979); [Wong 1979](#ref-Wong1979)); its realization as a Petersen deletion of the Hoffman–Singleton graph also appears in ([Klin, Muzychuk, and Ziv-Av 2009, 262–63](#ref-KlinMuzychukZivAv2009)). Here is a direct derivation of its spectrum. Write $B$ for the adjacency matrix of the deleted Petersen graph, $A_R=A(R)$, and $C$ for the $10\times40$ incidence matrix between $\mathcal P$ and $R$. A vertex of $R$ has at most one neighbour in $\mathcal P$: two adjacent neighbours would make a triangle, while two nonadjacent Petersen vertices already have their unique common neighbour in $\mathcal P$. There are $10(7-3)=40$ edges between the two parts. Thus each vertex of $R$ has exactly one neighbour in $\mathcal P$, and $R$ is $6$-regular.

The Petersen identity $B^2=2I-B+J$ and the blocks of the Moore identity give $$CC^{\mathsf T}=4I,\qquad
 A_RC^{\mathsf T}=J_{40,10}-C^{\mathsf T}-C^{\mathsf T}B.$$ The image of $C^{\mathsf T}$ therefore has dimension ten. The Petersen eigenvalues $1^{(5)}$ and $(-2)^{(4)}$ give eigenvalues $(-2)^{(5)}$ and $1^{(4)}$ on this image; the constant vector gives the eigenvalue $6$. Its orthogonal complement is $\ker C$. On this $30$-dimensional space, the other diagonal block gives $$A_R^2+A_R-6I=0.$$ Hence its eigenvalues are $2$ and $-3$. The dimension and trace equations give multiplicities $18$ and $12$, respectively. We obtain $$\operatorname{Spec}A_R=\{6^{(1)},2^{(18)},1^{(4)},(-2)^{(5)},(-3)^{(12)}\}.$$

It remains to check the diameter before applying the distance polynomial. Let $x,y\in V(R)$ be nonadjacent. If their common neighbour in $M$ survives, they remain at distance two. Otherwise they share a deleted Petersen neighbour. Choose $a\in N_R(x)$. Girth five makes $a,y$ nonadjacent, and makes the Petersen neighbour of $a$ different from that of $y$. Their unique common neighbour therefore lies in $R$, giving a path of length three from $x$ to $y$. Each deleted vertex has four neighbours in $R$, so pairs whose common neighbour was deleted do occur. Thus $R$ is connected with diameter three. Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a> now gives $$\operatorname{Spec}D(R)=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\},
 \qquad \Phi(R)=1.$$ For the other regular example, the second-subconstituent calculation gives $$\operatorname{Spec}D(X_{42})=\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\}.$$ The classical second-subconstituent identification and adjacency spectrum are recorded in ([Dam and Haemers 2003](#ref-vanDamHaemers2003), Table 3, p. 265). The two irregular examples require separate certificates. For $H_{38}$, a direct degree count gives $\delta^*=17/3$. The factor $x^2+6x+2$ supplies the root $-3-\sqrt7$, and exact Sturm isolation certifies that it is the least root. For $H_{39}$, strictness is certified directly: the exact matrix $6D+35I$ is positive definite. All graph, girth, distance, dual-degree, Sturm, and rational $LDL^{\mathsf T}$ certificates are checked by [`scripts/verify_extended.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_extended.py). The characteristic polynomials for the two labelled deletion families are recorded in Appendix <a href="#app:small-example-certificates" data-reference-type="ref" data-reference="app:small-example-certificates">G</a>. The labelled deletion families are exhausted by [`scripts/verify_descendant_families.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_descendant_families.py). No transitivity or numerical root ordering is used. Fixed graph6, adjacency-list, and edge-list records are provided in `data/graphs/`. ◻

</div>

<a id="distance-two-spheres-in-moore-graphs"></a>

## Distance-two spheres in Moore graphs

<div id="thm:second-subconstituent" class="theorem">

**Theorem 2.5** (Moore second subconstituents). *Let $M$ be a degree-$K$ Moore graph of diameter two, $K\ge3$, and let $X$ be the graph induced by $\Gamma_2(v)$ for a fixed vertex $v$. Then $X$ has order $K(K-1)$, degree $K-1$, girth at least five, diameter three, and $$\lambda_{\min}(D(X))=-\frac{5+\sqrt{4K-3}}2.$$ Consequently $$\Phi(X)=K-1-\frac{5+\sqrt{4K-3}}2,$$ which is positive exactly for integers $K\ge6$.*

</div>

Each vertex in the second sphere loses its unique neighbour in the first sphere. This gives the order, degree, and girth assertions directly. The remaining calculation splits the adjacency operator according to their neighbours in the first sphere, then checks that the induced graph has diameter three. Appendix <a href="#app:second-sphere-proof" data-reference-type="ref" data-reference="app:second-sphere-proof">C</a> gives the complete proof and the multiplicity calculation.

<a id="sec:score-calculus"></a>

# Distance spectra from adjacency eigenvalues

Let $A_i$ have entry one on pairs of vertices at distance $i$, and zero elsewhere. For a regular graph of diameter three, the girth assumption identifies the distance-two matrix with a quadratic in the adjacency matrix. The distance-three matrix is then the remaining part of the all-ones matrix. As a result, the nonprincipal distance eigenvalues can be read directly from the adjacency eigenvalues. This is the spectral reformulation of WOW-284 that we use throughout the obstruction arguments.

<div id="thm:diameter-three-score" class="theorem">

**Theorem 3.1** (Diameter-three score formula). *Let $G$ be connected, $k$-regular, of girth at least five and diameter three, with adjacency matrix $A$ and order $n$. Then $$D=3J+(k-3)I-2A-A^2,$$ $$D+kI=3J+(2k-2)I-(A+I)^2.$$ The principal distance eigenvalue is $3n-k^2-k-3$, and a nonprincipal adjacency eigenvalue $\theta$ gives the distance eigenvalue $$\mu(\theta)=k-2-(\theta+1)^2.$$ Consequently $$\boxed{
 \Phi(G)=2k-2-\max_{\theta\ne k}(\theta+1)^2.
 }$$ Thus $G$ is a strict counterexample exactly when every nonprincipal adjacency eigenvalue $\theta$ satisfies $$|\theta+1|<\sqrt{2k-2}$$*

</div>

<div class="proof">

*Proof.* We first count pairs at distance two. Girth at least five means that distinct vertices have at most one common neighbour, and adjacent vertices have none. The diagonal of the squared adjacency matrix counts the degree, so $A_2=A^2-kI$. Because the diameter is three, the other distinct nonadjacent pairs are at distance three; thus $A_3=J-I-A-A_2$. Putting these expressions into $D=A+2A_2+3A_3$ proves both identities.

We next apply the identities to adjacency eigenvectors. The matrix identities and regularity make the constant vector an eigenvector of $D$. Its eigenvalue is positive and is the Perron root, since every off-diagonal entry of the distance matrix is positive. On $\mathbf 1^\perp$, $J$ acts as zero, so each nonprincipal adjacency eigenvalue gives the stated distance eigenvalue. Taking the least of these values and using $\delta^*=k$ gives the score formula. The spectral transfer and score calculations for the examples used below are independently checked by [`scripts/verify_regular_score_calculus.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_regular_score_calculus.py). ◻

</div>

<div id="cor:bipartite" class="corollary">

**Corollary 3.2** (Bipartite obstruction). *A connected $k$-regular bipartite graph of girth at least five and diameter three is not a strict counterexample for $k\ge3$.*

</div>

<div class="proof">

*Proof.* The nonprincipal eigenvalue $-k$ satisfies $$(-k+1)^2-(2k-2)=(k-1)(k-3)\ge0
 \qquad(k\ge3).$$ Thus the required strict inequality fails, with equality exactly at $k=3$. ◻

</div>

<div id="prop:higher-transfer" class="proposition">

**Proposition 3.3** (Higher-diameter transfer). *Let $G$ be connected and $k$-regular, with diameter $d$ and girth at least $2d-1$. Let $A_i$ denote the distance-$i$ matrix, and define $$F_0=1,
 \quad F_1=x,
 \quad F_2=x^2-k,
 \quad F_i=xF_{i-1}-(k-1)F_{i-2}\quad(i\ge3).$$ Then $A_i=F_i(A)$ for $0\le i\le d-1$, and $$D=dJ+q_d(A),
 \qquad
 q_d(x)=\sum_{i=0}^{d-1}(i-d)F_i(x).$$ In particular, $$q_3(x)=k-3-2x-x^2,$$ $$q_4(x)=-x^3-2x^2+(2k-4)x+2k-4.$$*

</div>

<div class="proof">

*Proof.* The polynomial matrices count walks with no immediate reversal of an edge at an internal step. These are the nonbacktracking walks ([Nozaki 2015](#ref-Nozaki2015), Theorem 1). The girth condition makes this count agree with distance: up to length $d-1$, a nonbacktracking walk between two vertices is unique exactly when its length is their graph distance. Thus the distance-$i$ matrices are the corresponding polynomials in $A$. In the sum $D=\sum_{i=0}^d iA_i$, the identity $A_d=F_d(A)$ need not hold. Eliminate $A_d$ using $J=\sum_{i=0}^d A_i$. This proves the formula within the established distance-polynomial framework ([Howlader and Panigrahi 2022](#ref-HowladerPanigrahi2022); [Fiol 2016](#ref-Fiol2016)). ◻

</div>

<a id="sec:obstructions"></a>

# Degree and diameter bounds for regular counterexamples

A long geodesic can force a distance eigenvalue below the threshold required by WOW-284. Small degree gives a different obstruction: the graph can have too few vertices to fit the spectral window. We begin with the geodesic bound. The low-degree argument uses the polynomial order bound proved in the next section; its proof does not depend on the reductions made here.

<div id="lem:diam-rayleigh" class="lemma">

**Lemma 4.1**. *For every connected graph, $$\lambda_{\min}(D(G))\le-\operatorname{diam}(G).$$*

</div>

<div class="proof">

*Proof.* For a diametral pair $u,v$, the Rayleigh quotient of $e_u-e_v$ is $-d_G(u,v)$. ◻

</div>

<div id="thm:regular-degree-six" class="theorem">

**Theorem 4.2**. *Every connected regular strict counterexample to WOW-284 has degree at least six.*

</div>

<div class="proof">

*Proof.* Let the degree of $G$ be $k$. We may use the linear-programming (LP) bound in Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a>, whose proof is independent of this degree reduction. Lemma <a href="#lem:diam-rayleigh" data-reference-type="ref" data-reference="lem:diam-rayleigh">4.1</a> and strictness first give $\operatorname{diam}(G)<k$. This already excludes $k\le2$: the order satisfies $|V(G)|\ge3$, and the girth hypothesis excludes completeness, so $\operatorname{diam}(G)\ge2\ge k$. For $k=3$, the radius-two lower bound and $\operatorname{diam}(G)\le2$ force equality in the Moore bound. Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2.2</a> then gives $\Phi(G)=0$, contradicting the required $\Phi(G)>0$.

For $k=4$, the two possible diameters lead to different obstructions. Diameter two would require a degree-four Moore graph, but its adjacency multiplicities are nonintegral. For diameter three, Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a> gives $n<19$. The radius-two ball has $17$ vertices, and the third layer is nonempty, so $n=18$. Every vertex then has exactly one vertex at distance three: the distance-three matrix is a perfect matching. Its $-1$-eigenspace $W=\ker(A_3+I)$ is a nine-dimensional rational subspace of $\mathbf 1^\perp$. Since $A$ commutes with $A_3$, the space $W$ is $A$-invariant, and $$A_3=J+3I-A-A^2
 \quad\Longrightarrow\quad
 (A^2+A-4I)|_W=0.$$ The polynomial $x^2+x-4$ is irreducible over $\mathbb Q$, so a rational space on which it annihilates an operator has even dimension, a contradiction.

For $k=5$, diameter two again fails the Moore multiplicity condition. Diameter four can be excluded directly: a diametral geodesic gives the principal submatrix $D(P_5)$, and its factor $x^2+6x+4$ supplies the eigenvalue $-3-\sqrt5<-5$. Cauchy interlacing therefore contradicts strictness. In diameter three, Meringer’s enumeration ([Meringer 1999, 142](#ref-Meringer1999)) and Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a> leave $n\in\{30,31,32\}$. The handshake identity $5n=2|E(G)|$ gives $n\equiv0\pmod2$, leaving $n\in\{30,32\}$. At $n=32$, compress the adjacency matrix to the distance layers about a vertex. Their sizes are $1,5,20,6$. Write $a$ for the average internal degree in the distance-two layer. Each vertex of that layer has one neighbour in the first layer, so the edges from the second to the third layer satisfy $20(4-a)\le6\cdot5$, giving $a\ge5/2$. On the normalized layer indicators, the symmetric compression is $$Q(a)=
 \begin{pmatrix}
 0&\sqrt5&0&0\\
 \sqrt5&0&2&0\\
 0&2&a&(4-a)\sqrt{10/3}\\
 0&0&(4-a)\sqrt{10/3}&5-\frac{10}{3}(4-a)
 \end{pmatrix}.$$ The derivative of its only $a$-dependent block is $$\begin{pmatrix}1&-\sqrt{10/3}\\-\sqrt{10/3}&10/3\end{pmatrix}
 =
 \begin{pmatrix}1\\-\sqrt{10/3}\end{pmatrix}
 \begin{pmatrix}1&-\sqrt{10/3}\end{pmatrix}\succeq0.$$ This positive-semidefinite derivative makes every ordered eigenvalue of $Q(a)$ nondecreasing in $a$. Write $5=\mu_1(a)\ge\mu_2(a)\ge\mu_3(a)\ge\mu_4(a)$. It is therefore enough to bound the second eigenvalue at the smallest feasible value, $$\chi_{Q(5/2)}(x)=\frac14(x-5)p_{5,6}(x),
 \qquad
 p_{5,6}(x)=4x^3+10x^2-16x-30,
 \qquad p_{5,6}(11/6)=-29/27<0.$$ Since $p_{5,6}(11/6)<0$ and $p_{5,6}(x)\to+\infty$ as $x\to+\infty$, its largest root satisfies $\mu_2(5/2)>11/6>-1+\sqrt8$. Monotonicity and Poincaré separation give $$\theta_2(A)\ge\mu_2(a)\ge\mu_2(5/2),$$ contradicting the necessary bound $\theta_2(A)<-1+\sqrt8$. At $n=30$, Meringer’s isomorph-free enumeration leaves exactly four $(5,5)$-cages ([Meringer 1999, 142](#ref-Meringer1999)); each fixed record has an exact distance eigenvalue at most $-5$. The characteristic-polynomial factors and their roots are listed in Appendix <a href="#app:small-example-certificates" data-reference-type="ref" data-reference="app:small-example-certificates">G</a>; the classification supplies exhaustion, while the factors supply the distance-spectral obstruction. The accompanying release contains an independent exact audit of the complete case split and the four fixed graph6 records. ◻

</div>

<div id="thm:endpoint-diameter" class="theorem">

**Theorem 4.3** (Endpoint-neighbourhood obstruction). *Let $G$ be any connected finite simple graph, and let $u,v$ be vertices at distance $\ell=d_G(u,v)\ge5$. Put $p=d(u)$ and $q=d(v)$. Then $$\boxed{
 \lambda_{\min}(D(G))
 \le p+q-2-\sqrt{(p-q)^2+pq(\ell-2)^2}.
 }$$ If $\delta$ is the ordinary minimum degree, then $$\boxed{
 \lambda_{\min}(D(G))\le-\delta(\ell-4)-2.
 }$$ Consequently every strict WOW-284 counterexample satisfies $$\Delta>\delta(\ell-4)+2,$$ where $\Delta$ is the ordinary maximum degree. In particular, every regular strict counterexample has diameter at most four.*

</div>

<div class="proof">

*Proof.* We use opposite signs on the two endpoint neighbourhoods. They are disjoint, so give weight $a>0$ to $N(u)$, weight $-b<0$ to $N(v)$, and zero elsewhere. Distances within a neighbourhood are at most two; distances between the neighbourhoods are at least $\ell-2$. The latter enter with negative products, so these upper and lower distance bounds both give an upper bound on the Rayleigh quotient. After normalizing the neighbourhood indicators, this is the quotient of $$\begin{pmatrix}
 2(p-1)&-(\ell-2)\sqrt{pq}\\
 -(\ell-2)\sqrt{pq}&2(q-1)
 \end{pmatrix}.$$ The least eigenvalue gives the first bound. Its eigenvector can be chosen with both coordinates positive, as required by our sign assignment. To replace the endpoint degrees by the minimum degree, write $p=\delta+\alpha$, $q=\delta+\beta$, with $\alpha,\beta\ge0$, and put $t=\ell-2$. The right-hand side of the identity $$(p-q)^2+pqt^2-(p+q+\delta(t-2))^2
 =(t-2)\{\delta t(\alpha+\beta)+(t+2)\alpha\beta\}$$ is nonnegative. Since $p+q+\delta(t-2)>0$, comparison of the nonnegative square roots gives the second bound. Finally $\delta^*(G)\le\Delta$. The sign choice, radical comparison, and integer rounding are independently audited by [`scripts/verify_proof_audit_10_endpoint_diameter.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_10_endpoint_diameter.py). ◻

</div>

<div id="thm:diameter-four" class="theorem">

**Theorem 4.4** (Diameter four). *Let $G$ be connected, $k$-regular, of girth at least five and diameter four. Then $$\boxed{
 \lambda_{\min}(D(G))\le-\frac{7+\sqrt{16k+1}}2.
 }$$ Consequently no such graph of degree $2\le k\le9$ is a strict counterexample.*

</div>

<div class="proof">

*Proof.* Choose $u,v$ at distance four and put $U=N(u)$, $V=N(v)$. For fixed $a\in U$, every $b\in V$ with $d_G(a,b)=2$ has a common neighbour in $N(a)\setminus\{u\}$. Distinct such vertices $b,b'$ require distinct common neighbours, since otherwise $b-c-b'-v-b$ is a $4$-cycle. Thus at most $k-1$ vertices of $V$ are at distance two from each $a$. No pair in $U\times V$ is adjacent, and every remaining pair has distance at least three. Therefore $$\sum_{a\in U,b\in V}d_G(a,b)\ge2k^2+k.$$ The extra cross-distance contribution improves the Rayleigh bound. For $\alpha,\beta>0$, assign weights $\alpha,\beta,-\alpha,-\beta$ to $u,U,v,V$, respectively. Count unordered pairs with these weights and double their contribution. The result is $$\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
 \le
 \frac{-4\alpha^2-4k\alpha\beta-3k\beta^2}
 {\alpha^2+k\beta^2}.$$ After setting $y_1=\alpha$ and $y_2=\sqrt{k}\,\beta$, the right-hand side is the Rayleigh quotient of $$\begin{pmatrix}-4&-2\sqrt{k}\\-2\sqrt{k}&-3\end{pmatrix},$$ whose least eigenvalue is the displayed value and has a positive-coordinate minimizer. The strict comparison with $-k$ holds for $2\le k\le9$. Every orientation factor, cross-distance sign, and endpoint comparison is independently checked by [`scripts/verify_proof_audit_11_diameter_four.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_11_diameter_four.py). ◻

</div>

<div id="cor:trichotomy" class="corollary">

**Corollary 4.5** (Regular trichotomy). *Every regular strict counterexample has one of the following forms:*

1.  *diameter two, hence a Moore graph;*

2.  *diameter three, with $\lvert\theta+1\rvert<\sqrt{2k-2}$ for every nonprincipal adjacency eigenvalue $\theta$;*

3.  *diameter four, with degree at least ten.*

*There are no regular strict counterexamples of diameter at least five.*

</div>

<a id="sec:lp"></a>

# Moment bounds and the optimal polynomial order bound

Let $G$ satisfy the hypotheses of Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a>, and write its nonprincipal adjacency eigenvalues as $\theta_i$. Put $y_i=\theta_i+1$.

<div id="prop:moment-bound" class="proposition">

**Proposition 5.1** (Fourth-moment identity). *One has $$\sum_{i=1}^{n-1}(2k-2-y_i^2)(y_i+1)^2
 =(k+2)\bigl((k+2)(k^2+3)-6n\bigr).$$ Every strict counterexample therefore satisfies $$\boxed{
 n< B_k:=\frac{(k+2)(k^2+3)}6.
 }$$*

</div>

<div class="proof">

*Proof.* The fourth moment supplies an order bound because the shifted WOW window makes every summand nonnegative. The identity follows from $$\operatorname{tr}A=\operatorname{tr}A^3=0,
 \quad \operatorname{tr}A^2=nk,
 \quad \operatorname{tr}A^4=nk(2k-1),$$ after removing the principal eigenvalue and expanding both sides. In a strict counterexample, each factor $2k-2-y_i^2$ is positive. To obtain a strict order bound, we must also exclude a zero sum: otherwise every nonprincipal adjacency eigenvalue would equal $-2$, and $\operatorname{tr}A=0$ would give $k-2(n-1)=0$, or $n=(k+2)/2$, incompatible with the elementary bound $n\ge k+1$ for a simple $k$-regular graph. The identity is checked symbolically by [`scripts/verify_degree_six_gate.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_degree_six_gate.py) and independently within [`scripts/verify_proof_audit_02_two_sided_lp.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_02_two_sided_lp.py). ◻

</div>

The fourth-moment argument uses a quartic polynomial. We now allow higher degrees and minimize the order bound over polynomials satisfying the coefficient and sign conditions below. This is the one-variable nonbacktracking linear program. We exhibit a polynomial attaining its optimum and a dual measure proving that no polynomial in this class gives a smaller bound. The same measure determines the equality cases.

<div class="definition">

**Definition 5.2**. Let $F_i=F_i^{(k)}$ be the nonbacktracking polynomials from Proposition <a href="#prop:higher-transfer" data-reference-type="ref" data-reference="prop:higher-transfer">3.3</a>, and set $$I_k=[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].$$ A finite polynomial $f=\sum_i f_iF_i$ is *admissible* if $$f_0>0,
 \qquad f_i\ge0\quad(i\ge5),
 \qquad f(x)\le0\quad(x\in I_k).$$

</div>

For a connected $k$-regular graph of girth at least five whose nonprincipal spectrum lies in $I_k$, one has $\operatorname{tr}F_i(A)=0$ for $1\le i\le4$, while $\operatorname{tr}F_i(A)\ge0$ for $i\ge5$, since these traces count closed nonbacktracking walks ([Nozaki 2015](#ref-Nozaki2015), Theorem 1 and Corollary 1). The coefficient conditions therefore give $nf_0\le\operatorname{tr}f(A)$. On the other hand, $f(\theta)\le0$ for every nonprincipal eigenvalue, so $\operatorname{tr}f(A)\le f(k)$. Thus $$nf_0\le\operatorname{tr}f(A)\le f(k),
 \qquad n\le\frac{f(k)}{f_0}.$$

<div id="thm:lp-ceiling" class="theorem">

**Theorem 5.3** (Exact LP ceiling and rigidity). *For every integer $k\ge4$ and every admissible $f$, $$\boxed{
 \frac{f(k)}{f_0}\ge B_k=\frac{(k+2)(k^2+3)}6.
 }$$ Equality holds if and only if $f$ is a positive scalar multiple of $$\boxed{
 f_*(x)=\frac{(x+2)^2(x^2+2x-(2k-3))}{6(k+2)}.
 }$$ Thus increasing the polynomial degree cannot improve this one-variable LP bound. Consequently, any connected $k$-regular graph of girth at least five whose nonprincipal spectrum lies in $I_k$ satisfies $n<B_k$.*

</div>

<div class="proof">

*Proof.* We first check that the stated quartic attains the proposed bound. Its nonbacktracking expansion is $$\begin{aligned}
6(k+2)f_*(x)={}&6(k+2)F_0(x)+2(2k+7)F_1(x)\\
&+(k+13)F_2(x)+6F_3(x)+F_4(x).
\end{aligned}$$ The constant coefficient is positive, and there are no coefficients above degree four. On $I_k$, the factor $(x+1)^2-(2k-2)$ is nonpositive, while $(x+2)^2\ge0$; hence $f_*$ is admissible and $f_*(k)=B_k$.

To prove that no admissible polynomial does better, we use a positive measure supported on the two window endpoints and the interior zero of the quartic. Put $\Delta=\sqrt{2k-2}$, $\xi_\pm=-1\pm\Delta$, and $\xi_0=-2$, and define $$\begin{aligned}
w_-&=\frac{k(k+2)(2k^2-6-3(k-1)\Delta)}{24(2k-3)},\\
w_0&=\frac{k(k-1)(k^2+3)}{6(2k-3)},\\
w_+&=\frac{k(k+2)(2k^2-6+3(k-1)\Delta)}{24(2k-3)}.
\end{aligned}$$ $w_-,w_0,w_+>0$. For the only nontrivial inequality, this follows from $$(2k^2-6)^2-18(k-1)^3
 =2(k-3)(2k-3)(k^2+3)>0.$$ The measure $\mu=w_-\delta_{\xi_-}+w_0\delta_{\xi_0}+w_+\delta_{\xi_+}$ satisfies $$\mu(1)=B_k-1,
 \qquad \mu(F_i)=-F_i(k)\quad(1\le i\le4).$$ The measure cancels the first four nonconstant basis terms. For the remaining terms, we need the slack $a_i=\mu(F_i)+F_i(k)$ to be strictly positive for $i\ge5$. Appendix <a href="#app:lp-slack-positivity" data-reference-type="ref" data-reference="app:lp-slack-positivity">D</a> verifies this positivity: the first five values follow from exact polynomial expansions, and a Chebyshev bound handles every later term. With this calculation available, the optimality and rigidity argument is short. We can now compare an arbitrary admissible polynomial with the quartic. Expansion in the nonbacktracking basis gives $$\int f\,d\mu
 =B_kf_0-f(k)+\sum_{i\ge5}f_i a_i
 \ge B_kf_0-f(k).$$ The last sum is nonnegative by the coefficient condition and the slack positivity verified in Appendix <a href="#app:lp-slack-positivity" data-reference-type="ref" data-reference="app:lp-slack-positivity">D</a>. On the other hand, $f\le0$ on $\operatorname{supp}\mu$, so $\int f\,d\mu\le0$. These inequalities prove the lower bound for every admissible polynomial. Equality must hold in both inequalities. Since every high-degree slack is strictly positive, $f_i=0$ for $i\ge5$. The measure has positive weight at each support point, so $f$ must vanish at $\xi_-,-2,\xi_+$. Its interior zero $-2$ has even multiplicity, because $f\le0$ on $I_k$. A polynomial of degree at most four with these zeros is a scalar multiple of $f_*$, and $f_0>0$ makes that scalar positive. The polynomial bound allows the endpoints of $I_k$. We now show that no graph attains this bound. Suppose $n=B_k$. Equality in the trace bound for the optimal quartic forces every nonprincipal eigenvalue to belong to $$\{-2,-1-\Delta,-1+\Delta\},\qquad \Delta=\sqrt{2k-2}.$$ Let $m_0,m_-,m_+$ be their respective multiplicities. If $\Delta$ is irrational, the trace equation $$0=k-(m_-+m_+)-2m_0+\Delta(m_+-m_-)$$ forces $m_+=m_-$. Counting the nonprincipal eigenvalues then gives $m_0=k-n+1<0$, since $$B_k-(k+1)=\frac{k(k-1)(k+3)}6>0.$$ This is impossible. Thus $\Delta$ is rational and, as the square root of an integer, must be an integer.

The second moment of $A+I$ now determines $m_0$. The principal eigenvalue contributes $(k+1)^2$. Each nonprincipal adjacency eigenvalue $-1\pm\Delta$ contributes $2k-2$ to this moment, while each copy of $-2$ contributes $1$. Hence $$(2k-2)(n-1-m_0)+m_0=n(k+1)-(k+1)^2,$$ and substituting $n=B_k$ gives $$m_0=\frac{k(k-1)(k^2+3)}{6(2k-3)}.$$ Since $m_0$ is an integer, $2k-3$ divides $k(k-1)(k^2+3)$. The identity $$16k(k-1)(k^2+3)
 =(2k-3)(8k^3+4k^2+30k+21)+63$$ therefore implies $2k-3\mid63$. With $k\ge4$, this leaves $k\in\{5,6,12,33\}$. Only $k=33$ has integral $\sqrt{2k-2}$, but then $m_0=9152/3$, again impossible. Consequently $n<B_k$ throughout the closed window. The LP certificate identities, finite slacks, tail bound, and polynomial equality calculation are independently checked by [`scripts/verify_proof_audit_02_two_sided_lp.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_02_two_sided_lp.py). ◻

</div>

<div id="thm:integral-slack" class="theorem">

**Theorem 5.4** (Integral optimal-slack bound). *Let $G$ be connected and $k$-regular with $k\ge4$, of girth at least five and diameter three, and suppose $$\lvert\theta+1\rvert<\sqrt{2k-2}
 \qquad(\theta\ne k)$$ for every adjacency eigenvalue $\theta$. Define $$g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),\quad
 C_k=(k+2)^2(k^2+3),\quad h_k=6(k+2),$$ $$\mathcal S_k=-g_k(A)+\frac{C_k}{n}J.$$ Then $$\mathcal S_k\succeq0,\qquad
 \mathcal S_k\mathbf 1=0,\qquad
 \operatorname{tr}\mathcal S_k=h_k(B_k-n).$$ Moreover, $$\mathcal E_k=g_k(A)-(h_k+1)J+I$$ is a nonzero, symmetric, entrywise nonnegative integral matrix with zero diagonal and constant row sum $$\varepsilon_{k,n}=C_k-(h_k+1)n+1.$$ On $\mathbf 1^\perp$, one has $\mathcal S_k=I-\mathcal E_k$. In particular, $$\boxed{
 n\le
 \left\lfloor
 \frac{(k+2)^2(k^2+3)}{6(k+2)+1}
 \right\rfloor.
 }$$*

</div>

<div class="proof">

*Proof.* We apply the optimal LP polynomial $g_k=6(k+2)f_*$ from Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a> to the adjacency matrix. The resulting $\mathcal S_k$ vanishes on $\langle\mathbf 1\rangle$. On a nonprincipal $\theta$-eigenspace, its eigenvalue is $$\bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2\ge0.$$ To compute the diagonal, use the nonbacktracking expansion of $g_k$, whose constant coefficient is $h_k$. Girth at least five implies $(F_i(A))_{uu}=0$ for every $u$ and $1\le i\le4$. Thus $$\operatorname{tr}\mathcal S_k=C_k-h_kn=h_k(B_k-n),
 \qquad (g_k(A))_{uu}=h_k.$$

The off-diagonal entries now supply the extra restriction. Put $z_{uv}=(g_k(A))_{uv}\in\mathbb Z$ for $u\ne v$, and set $a=C_k/n-h_k=(\mathcal S_k)_{uu}$. Positivity of the $2\times2$ principal minor on $\{u,v\}$ gives $$\left|\frac{C_k}{n}-z_{uv}\right|\le a.$$ We must exclude $C_k/n-z_{uv}=a$, equivalently $z_{uv}=h_k$. This would imply $(e_u-e_v)^{\mathsf T}\mathcal S_k(e_u-e_v)=0$, and positivity would then put $e_u-e_v\in\ker\mathcal S_k$. Write $E_{-2}(A)=\ker(A+2I)$. The strict spectral window gives $$\ker\mathcal S_k=\langle\mathbf 1\rangle\oplus E_{-2}(A).$$ Since $e_u-e_v\perp\mathbf 1$, it would be a $(-2)$-eigenvector of $A$. Yet the $u$-coordinate of $A(e_u-e_v)$ is $-1$ if $u\sim v$ and $0$ otherwise, never $-2$. Therefore $$z_{uv}\ge h_k+1.$$ This proves the stated entrywise properties of $\mathcal E_k$. Its row sum follows from $g_k(A)\mathbf 1=C_k\mathbf 1$; on $\mathbf 1^\perp$, the term $J$ vanishes and gives the claimed identity.

The remaining issue is $\mathcal E_k\ne0$. If this fails, then $$g_k(A)=(h_k+1)J-I,$$ so $p_k(A)=0$ on $\mathbf 1^\perp$, where $p_k(x)=g_k(x)+1$. After $y=x+2$, $$p_k(y-2)=y^4-2y^3+(3-2k)y^2+1.$$ There are two possible ways to factor this polynomial over $\mathbb Q$. A rational linear factor would give a root among $\pm1$, whose values are $3-2k$ and $7-2k$. For a factorization into monic integer quadratics, the constant terms would be both $1$ or both $-1$. The cubic and linear coefficients would then be equal or opposite, respectively; their actual values are $-2$ and $0$. Neither factorization is possible.

The adjacency operator on the rational zero-sum space is annihilated by this irreducible quartic. Its characteristic polynomial must therefore be a power of that quartic: $$\chi_{A|_{\mathbf 1^\perp}}(x)=p_k(x)^m,\qquad n-1=4m.$$ The four roots of $p_k$ sum to $-6$, so $\operatorname{tr}A=0$ gives $$0=k-6m.$$ Hence $n-1=4m=2k/3$, contradicting $n\ge k+1$. Thus $\mathcal E_k\ne0$. Its constant row sum is consequently a positive integer, so $\varepsilon_{k,n}\ge1$, which is equivalent to the displayed order bound. The symbolic expansion, irreducibility alternatives, and finite specializations have also been checked by independent exact audits. ◻

</div>

<a id="sec:degree-six"></a>

# Integral excess, order bounds, and local cycle counts

The trace of $\mathcal S_k$, apart from a positive factor, is the gap between the graph order and the scalar LP bound. We now use the entries as well as the trace. Its $2\times2$ principal minors constrain individual entries, and larger minors relate several entries. In the associated integral excess matrix, these constraints become arithmetic restrictions. They first give the three-to-one excess bound. Applied to individual edges, they also turn local cycle counts into obstructions that the scalar order bound does not see.

<a id="the-three-to-one-excess-bound"></a>

## The three-to-one excess bound

<div id="thm:three-to-one" class="theorem">

**Theorem 6.1** (Three-to-one excess bound). *Under the hypotheses of Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a>, assume $k\ge6$ and write $\varepsilon=\varepsilon_{k,n}$. The integral parameter $$r=2\varepsilon-n-2
   =2(k+2)^2(k^2+3)-(12k+27)n$$ satisfies $$r>0,\qquad n\le3r.$$ Consequently $$\boxed{
 n\le\left\lfloor
 \frac{3(k+2)^2(k^2+3)}{18k+41}
 \right\rfloor.
 }$$*

</div>

<div class="proof">

*Proof.* Put $E=\mathcal E_k$, $C=C_k$, $h=h_k$, and $$\rho=\frac{\varepsilon-1}{n}
      =\frac{1+r/n}{2}.$$ The optimal slack matrix has the form $$\mathcal S_k=I-E+\rho J\succeq0.$$ Replace each edge of a graph by a vertex and join two of these vertices when their edges meet. The resulting graph is its line graph. A complete graph with a perfect matching removed is called a cocktail-party graph.

The proof has two stages. We first assume $r\le0$, show that $E$ is the adjacency matrix of a simple graph, and rule out its complement using the least-eigenvalue classification and rational eigenspace dimensions. Once $r>0$ is known, we assume $n>3r$. We then exclude four cases, in order:

1.  an entry $E_{uv}=2$, which forces $n=3r+1$ or $3r+2$ and is excluded by divisibility and parity;

2.  a simple $E$ whose complement has at least three components, which forces $n\le3r+6$ and is excluded by fixed remainders;

3.  a connected complement, whose cocktail-party case contradicts $r>0$ and whose line-graph roots are excluded by size and divisibility;

4.  a complement with two components, excluded by their classified types and the remaining fixed remainders.

Here diameter three and the radius-two count give $n\ge k^2+2\ge38$. The classification therefore applies whenever the complement is connected. In the final two-component case we first exclude $k=6,7,8$; for $k\ge9$, each component has order greater than $28$. Before starting these cases, we record the arithmetic restrictions used to close them. The first comes from the identity $$128(2C-r)
 =(4k+9)(64k^3+112k^2+196k+327)+(129-128r).$$ Since $n=(2C-r)/(12k+27)$ is integral and $4k+9$ is odd, <a id="eq:r-divisibility"></a>$$\tag{1}
 4k+9\mid129-128r.$$ The second condition will be used when the order is close to the desired bound. If $n=3r+t$, the defining equation for $r$ gives $$18k+41\mid 2C-(12k+27)t.$$ Since $\gcd(18,18k+41)=1$, Euclidean division after multiplication by $18^4$ yields the necessary condition <a id="eq:fixed-remainder"></a>$$\tag{2}
 18k+41\mid 132650+34992t.$$

We first prove positivity of $r$. Suppose $r\le0$. A $2\times2$ principal minor of $\mathcal S_k$ gives $$E_{uv}\le2+\frac rn\qquad(u\ne v).$$ Thus $E$ is the adjacency matrix of a simple graph when $r<0$. If $r=0$ and $E_{uv}=2$, positivity puts $e_u+e_v$ in $\ker\mathcal S_k$. After subtracting its projection onto $\mathbf 1$, the strict spectral window gives a $(-2)$-eigenvector of $A$. Its $u$-coordinate would require $$A_{uv}=-2+\frac{2k+4}{n},$$ which is impossible because $n\ge k^2+2$ and $A_{uv}\in\{0,1\}$. Hence $E$ is simple also when $r=0$.

Let $X$ be the graph with adjacency matrix $J-I-E$. It is regular of degree $$d=n-1-\varepsilon=\frac{n-r-4}{2},$$ and $A(X)=-I-E+J$ has least eigenvalue at least $-2$. Since each component has at least $d+1$ vertices, $X$ has at most two components. The exceptional possibilities will be tested on eigenspaces of $E$. Because this matrix is a polynomial in $A$ and $J$, it commutes with $A$, so each rational eigenspace of $E$ is $A$-invariant.

The graph $X$ is now simple and regular, and its order is $n\ge38$. If it is connected, the classification of connected regular graphs of order greater than $28$ and least eigenvalue at least $-2$ makes it a line graph or a cocktail-party graph ([Cameron et al. 1976](#ref-CameronEtAl1976)); see also ([Cvetković, Rowlinson, and Simić 2004](#ref-CvetkovicEtAl2004), Theorems 4.1.1 and 4.1.5) and ([Koolen et al. 2025](#ref-KoolenEtAl2025), Introduction).

Suppose first that $X$ is connected. The complete case would give $E=0$, excluded in Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a>. In the cocktail-party case, $E$ is a perfect matching and $r=-n$. The identity $$1296C=(6k+13)(216k^3+396k^2+654k+1175)+277$$ forces $k=44$ and $n=14812$. On the $7406$-dimensional $(-1)$-eigenspace of $E$, the rational operator $A$ is annihilated by $g_{44}(x)+2$.

If $X=L(Y)$, choose a connected root $Y$. Since $X$ is $d$-regular, every edge $ab$ of $Y$ satisfies $\deg_Y(a)+\deg_Y(b)=d+2$. Degrees alternate along paths. An odd cycle forces them to coincide; otherwise $Y$ is bipartite, with a constant degree on each part. Thus $Y$ is regular or semiregular bipartite. Here semiregular means that the degree is constant within each part, though the two degrees may differ.

If $Y$ is $q$-regular, then $q\ge n/4$ and $|V(Y)|\le8$, contradicting $q\le |V(Y)|-1$ because $n\ge38$. If $Y$ is semiregular bipartite with part sizes $a\ge b\ge2$, then $$\frac1a+\frac1b=\frac{n-r}{2n}\ge\frac12,\qquad n\le ab.$$ The cases $b\ge3$ have $ab<38$. For $b=2$, connectedness forces $Y=K_{a,2}$, hence $r=-4$. Equation <a href="#eq:r-divisibility" data-reference-type="eqref" data-reference="eq:r-divisibility">(1)</a> leaves $k=158$ and $n=664748$. The resulting $(-1)$-eigenspace of $E$ has dimension $332373$.

If $X$ has two components, write their orders as $d+1+a_1$ and $d+1+a_2$. Then $$a_1+a_2=r+2,$$ so $r\in\{-2,-1,0\}$. Checking the divisors in <a href="#eq:r-divisibility" data-reference-type="eqref" data-reference="eq:r-divisibility">(1)</a>, together with $n\ge k^2+2$ and $kn$ even, leaves only $$(r,k,n)=(-1,62,40875).$$ The components then have orders $20437$ and $20438$. Their common degree is one less than the smaller order, so the smaller component is complete. In the larger component, each vertex has exactly one nonneighbour; these missing edges form a perfect matching, giving the cocktail-party graph. Thus $E$ has eigenvalue $-1$ with multiplicity $10219$.

We exclude all three exceptional cases using the eigenspaces just found. These rational spaces are orthogonal to the constant vector and invariant under the adjacency operator. On each of them the excess matrix has eigenvalue minus one, so its defining polynomial relation gives the annihilator $g_k(x)+2$. This quartic is irreducible over $\mathbb Q$ for every integer $k\ge6$, except $k=7$. To check irreducibility, substitute $y=x+2$, giving $$y^4-2y^3+(3-2k)y^2+2.$$ Gauss’s lemma reduces a quadratic factorization to monic integer quadratics whose constant terms multiply to $2$; coefficient comparison leaves only $k=4$ or $k=7$, while the rational-root alternatives give $k=2$ or $k=4$. The degrees $44,62,158$ are therefore irreducible cases, but the corresponding dimensions $7406,10219,332373$ are not divisible by four. Since an invariant rational space annihilated by an irreducible quartic is a vector space over the degree-four field $\mathbb Q[x]/(g_k(x)+2)$, its rational dimension must be divisible by four. This contradiction proves $r>0$.

We now assume, for a contradiction, that $n>3r$, and put $x=r/n\in(0,1/3)$. Before applying the graph classification again, we show that the excess matrix is simple. The $2\times2$ minors give $E_{uv}\le2$. Suppose $E_{uv}=2$, and for $w\notin\{u,v\}$ set $s_w=E_{uw}+E_{vw}$. Cauchy–Schwarz, applied to $e_u+e_v$ and $e_w$ in the Gram matrix $\mathcal S_k$, gives $$(1+x-s_w)^2\le x(3+x),$$ Thus the nonnegative integer $s_w$ belongs to $\{1,2\}$. Summing over the rows shows that exactly $r$ vertices satisfy $s_w=2$. We collect these vertices in $W$, let $y=\sum_{w\in W}e_w$, and put $$e_W=\sum_{\{w,z\}\subseteq W}E_{wz}.$$ Then $$\begin{aligned}
  (e_u+e_v)^{\mathsf T}\mathcal S_k(e_u+e_v)&=2x,\\
  (e_u+e_v)^{\mathsf T}\mathcal S_k y&=r(x-1),\\
  y^{\mathsf T}\mathcal S_k y&=r+\frac{r^2(1+x)}2-2e_W.
 \end{aligned}$$ Positivity of this $2\times2$ Gram determinant yields $$2xr+r^2(3x-1)-4xe_W\ge0.$$ Since $e_W\ge0$, this forces $n\le3r+2$. Our contrary assumption therefore leaves only $n=3r+t$ with $t\in\{1,2\}$. Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">(2)</a> reduces these two possibilities to: $$\begin{array}{c|c|c}
  t&\text{remainder}&\text{admissible }(18k+41,k)\\
  \hline
  1&167642&\text{none}\\
  2&202634&(1427,77).
 \end{array}$$ The remaining case gives $(k,n,r)=(77,77831,25943)$, but $kn$ is odd, contrary to the handshake lemma. Therefore $E$ is simple.

We may therefore again treat $X$, with adjacency matrix $J-I-E$, as a simple graph. It is $d$-regular and has least eigenvalue at least $-2$. If $X$ had three or more components, then $n\ge3(d+1)$, or $n\le3r+6$. This leaves $n=3r+t$ for $1\le t\le6$, and Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">(2)</a> gives $$\begin{array}{c|rrrrrr}
  t&1&2&3&4&5&6\\ \hline
  \text{remainder}
   &167642&202634&237626&272618&307610&342602,
 \end{array}$$ and leaves no integral graph: the $t=2$ case is excluded above, while the sole divisor candidate for $t=3$ does not make $r$ integral. Hence $X$ has at most two components.

For connected $X$, the cocktail-party case contradicts $r>0$. We are left with $X=L(Y)$, with the same regular/semiregular dichotomy as above. If $Y$ is $q$-regular on $v$ vertices, then $$q=\frac{n-r}{4}>\frac n6,\qquad v=\frac{2n}{q}<12.$$ Simplicity and $n\ge38$ leave only $$\begin{aligned}
  (q,v;n,r)\in\{&(8,10;40,8),(9,10;45,9),\\
                 &(8,11;44,12),(10,11;55,15)\}.
 \end{aligned}$$ The radius-two lower bound forces $k\le7$, and direct substitution in the defining formula for $r$ excludes all four cases.

For a semiregular bipartite root with part sizes $a\ge b\ge2$, write $p=n/a\le q=n/b$ for its two degrees. Then $$p+q=\frac{n-r}{2}>\frac n3,
  \qquad (b-2)n=b(r+2p),$$ so $b<6$. Connectedness excludes $p=1$. For $b=2$, the left side of the displayed identity is zero while the right side is positive. For $b=5$, the degree-sum inequality makes the sum of the reciprocals of the part sizes greater than one third. The larger part therefore has at most seven vertices, and the root has at most thirty-five edges, below the required line-graph order thirty-eight. The case $b=4$ leaves only $$(p,q,a,b;n,r)=(4,10,10,4;40,12),\ (4,11,11,4;44,14),$$ both excluded by the radius-two bound and the formula for $r$. For $b=3$, one has $p=2$ or $3$, giving $n=3r+12$ or $n=3r+18$. Equation <a href="#eq:fixed-remainder" data-reference-type="eqref" data-reference="eq:fixed-remainder">(2)</a> gives the remainders $552554=2\cdot276277$ and $762506=2\cdot381253$. Their odd cofactors are prime and congruent to $13\pmod {18}$, whereas $18k+41\equiv5
 \pmod {18}$. Thus $X$ cannot be connected.

Only the case of two components remains. When $k=6,7,8$, the inequalities $r>0$ and $n>3r$ leave no admissible integral order. For $k\ge9$, we have $n>150$, so both components have order greater than $28$ and the classification applies to each. Suppose a component of order $N$ is the line graph of a simple $q$-regular graph $Y$ on $v$ vertices. Its degree is $d=2q-2$, and the number of edges of the root is $N=vq/2$. Hence $$q=\frac{d+2}{2}=\frac{n-r}{4}>\frac n6>25,
 \qquad
 v=\frac{2N}{q}\le\frac{2n}{q}<12.$$ Simplicity gives $q\le v-1\le10$, a contradiction. If a component of order $N$ has a semiregular bipartite root, its part sizes satisfy $$\frac1a+\frac1b=\frac{d+2}{N}
  \ge\frac{n-r}{n+r+2}>\frac{49}{100}.$$ If $b\ge3$, the five possible pairs $(a,b)$ have $ab\le18<N$. If $b=2$, connectedness forces the root $K_{d,2}$, whose line graph has order $2d$. Thus every component is $K_{d+1}$, a cocktail-party graph of order $d+2$, or $L(K_{d,2})$. The first two types alone force $r\le0$. If exactly one component has order $2d$, then $n=3r+8$ or $n=3r+10$. If both do, then $n=2r+8$. Together with $n>3r$, this gives $r<8$, hence $n<24$, contrary to $n>150$. For the two remaining mixed cases, the divisor checks in Appendix <a href="#app:three-to-one-arithmetic" data-reference-type="ref" data-reference="app:three-to-one-arithmetic">H</a> exclude $n=3r+8$ and leave only $k=123$ for $n=3r+10$. In that case $kn$ is odd. This final contradiction proves $n\le3r$.

We have excluded every case under the contrary assumption. Substituting the definition of $r$ into the resulting three-to-one inequality gives $$(18k+41)n\le3(k+2)^2(k^2+3),$$ which is the displayed bound. The quartic factorization alternatives, aggregate Gram determinant, and divisor and line-root cases used after $r>0$ is established are checked in [`scripts/verify_proof_audit_14_three_to_one.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_14_three_to_one.py). The exceptional nonpositive-$r$ parameter cases are also checked by `nonpositive_r_audit()` in [`scripts/verify_three_to_one_excess_bound.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_three_to_one_excess_bound.py). ◻

</div>

<div id="cor:three-to-one-equality" class="corollary">

**Corollary 6.2** (Rigidity at equality). *Under the hypotheses and notation of Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">6.1</a>, equality in $n\le3r$ can occur only for $$\boxed{(k,n,r)=(103,185220,61740).}$$ This is an arithmetic parameter classification; it does not assert the existence of a graph with these parameters.*

</div>

<div class="proof">

*Proof.* Equality gives $$(18k+41)r=(k+2)^2(k^2+3)=:C_k.$$ Exact Euclidean division yields $$\begin{aligned}
18^4C_k={}&(18k+41)
 (5832k^3+10044k^2+17946k+29107)\\
&+66325,
\end{aligned}$$ where $66325=5^2\cdot7\cdot379$. Hence $18k+41\mid66325$. Since $k\ge6$, this divisor is at least $149$ and is congruent to $5$ modulo $18$. Among the positive divisors of $66325$, only $1895$ has these properties. Thus $k=103$, after which direct substitution gives $r=61740$ and $n=3r=185220$. ◻

</div>

<a id="a-signed-graph-from-the-excess-matrix"></a>

## A signed graph from the excess matrix

<div id="prop:signed-complement" class="proposition">

**Proposition 6.3** (Signed-complement bridge). *Under the hypotheses and notation of Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">6.1</a>, assume $0<r<n$ and define $$S=(6k+14)J-2I-g_k(A).$$ Then $S$ is a signed adjacency matrix: $$S_{uu}=0,\qquad S_{uv}\in\{-1,0,1\}\quad(u\ne v).$$ It has constant signed row sum $(n-r-4)/2$, and $$S+2I\succeq0,\qquad E_{-2}(S)=E_{-2}(A).$$ Here $E_\lambda(B):=\ker(B-\lambda I)$ denotes the $\lambda$-eigenspace of a square matrix $B$.*

</div>

<div class="proof">

*Proof.* Write $x=r/n\in(0,1)$, $\rho=(1+x)/2$, and $E=\mathcal E_k$. Since $$\mathcal S_k=I-E+\rho J\succeq0,$$ its $2\times2$ principal minors give $-1\le E_{uv}\le2+x$. The entries of $E$ are nonnegative integers, so $E_{uv}\in\{0,1,2\}$ for $u\ne v$, and $S=J-I-E$ has the asserted entries. The row sum follows from $\varepsilon=(n+r+2)/2$. Moreover, $$S+2I
 =\mathcal S_k+\frac{n-r}{2n}J\succeq0.$$ It remains to identify the shared eigenspace. The matrices $A$ and $S$ commute; a nonprincipal adjacency eigenvector of eigenvalue $\theta$ has, under $S$, eigenvalue $-2-g_k(\theta)$. Inside the open shifted WOW window, $g_k$ vanishes only at $\theta=-2$, since its other zeros are the excluded endpoints. The eigenvalue of $S$ on the constant vector is $(n-r-4)/2>-2$, since $r<n$. Thus the two $(-2)$-eigenspaces coincide. ◻

</div>

<a id="five-cycle-counts-through-an-edge"></a>

## Five-cycle counts through an edge

<div id="prop:edge-cycle" class="proposition">

**Proposition 6.4** (Edge-local cycle bounds). *Let $G$ be connected and $k$-regular, where $k\ge4$, of girth at least five and diameter three, and suppose $$|\theta+1|\le\sqrt{2k-2}
 \qquad(\theta\ne k)$$ for every adjacency eigenvalue $\theta$. For an edge $uv$, let $\sigma_{uv}$ be the number of $5$-cycles containing that edge. Then $$2k-2\le\sigma_{uv}\le
 \frac{2(k+2)^2(k^2+3)}n-10k-26.$$ If $n=k^2+1+c$, then also $$\sigma_{uv}\ge(k-1)^2-c.$$*

</div>

<div class="proof">

*Proof.* Recall $g_k$ and $C_k=g_k(k)$ from Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a>, and put $$M=-g_k(A)+\frac{C_k}{n}J.$$ The spectral window gives $M\succeq0$. For an edge $uv$, $$(A^3)_{uv}=\sum_{z\sim v}(A^2)_{uz}=k+(k-1)=2k-1.$$ Here $z=u$ contributes $k$, while every other neighbour of $v$ is at distance two from $u$ and has a unique length-two path from $u$. Moreover, $$(A^4)_{uv}=\sum_z(A^2)_{uz}(A^2)_{zv}=\sigma_{uv}.$$ Indeed, the nonzero summands away from the diagonal are precisely the vertices at distance two from both $u$ and $v$. Their two unique length-two paths, together with $uv$, form a five-cycle, and each five-cycle through $uv$ yields one such vertex. Since $C_k=(k+2)^2(k^2+3)$, the diagonal and edge entries of $M$ are $$a=\frac{C_k}{n}-6(k+2),
 \qquad
 b=\frac{C_k}{n}-(4k+14)-\sigma_{uv}.$$ The principal submatrix on $\{u,v\}$ is $\bigl(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\bigr)$, so $a\ge0$ and $-a\le b\le a$. The inequality $b\le a$ gives $\sigma_{uv}\ge2k-2$, while $b\ge-a$ gives the stated upper bound.

For the final bound, every radius-two ball has size $k^2+1$. The set $$\{u,v\}\cup(N(u)\setminus\{v\})\cup(N(v)\setminus\{u\})$$ contains $2k$ vertices and lies in $B_2(u)\cap B_2(v)$. Every further intersection vertex is at distance two from both endpoints and is therefore in the preceding five-cycle bijection. Hence $$|B_2(u)\cap B_2(v)|=2k+\sigma_{uv}.$$ Inclusion–exclusion and $n=k^2+1+c$ now give $\sigma_{uv}\ge(k-1)^2-c$. The complete walk classification, sign directions, and radius-two bijection have also been checked independently and exactly. ◻

</div>

If the spectral window is strict, both endpoint bounds improve to $$2k-1\le\sigma_{uv}
 <\frac{2(k+2)^2(k^2+3)}n-10k-26.$$ For the lower bound, the proof of Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a> gives $(g_k(A))_{uv}\ge h_k+1=6(k+2)+1$, whereas the edge calculation above gives $(g_k(A))_{uv}=4k+14+\sigma_{uv}$. For the upper bound, use $M,a,b$ from the proof above. Equality $b=-a$ would put $e_u+e_v$ in $\ker M$. In the strict window, $$\ker M=\langle\mathbf 1\rangle\oplus\ker(A+2I),$$ so $w=e_u+e_v-(2/n)\mathbf 1$ would satisfy $Aw=-2w$. At the $u$-coordinate, this gives $1-2k/n=-2+4/n$, hence $n=2(k+2)/3<k+1$, contradicting the order bound for a simple $k$-regular graph. Thus $b>-a$, proving the strict upper bound.

For $\ell\ge3$, let $N_\ell$ denote the number of $\ell$-cycles in $G$.

<div id="cor:edge-cycle-sieve" class="corollary">

**Corollary 6.5** (Edge–cycle divisibility sieve). *Under the hypotheses of Proposition <a href="#prop:edge-cycle" data-reference-type="ref" data-reference="prop:edge-cycle">6.4</a>, put $$L_{k,n}=\max\{2k-2,\;2k^2-2k+2-n\},
 \qquad
 U_{k,n}=\frac{2(k+2)^2(k^2+3)}{n}-10k-26.$$ Necessarily $$\boxed{\lceil L_{k,n}\rceil\le\lfloor U_{k,n}\rfloor.}$$ If both sides equal an integer $s$, then every edge of $G$ lies in exactly $s$ five-cycles and $$\boxed{5\mid \frac{skn}{2}.}$$ Under the strict spectral window, put $L^{\mathrm{str}}_{k,n}=\max\{2k-1,\;2k^2-2k+2-n\}$. Then the stronger necessary condition is $$\lceil L^{\mathrm{str}}_{k,n}\rceil
 \le\lceil U_{k,n}\rceil-1.$$ If these two integer bounds coincide at $s$, the same divisibility conclusion holds.*

</div>

<div class="proof">

*Proof.* Writing $n=k^2+1+c$, the two lower bounds in Proposition <a href="#prop:edge-cycle" data-reference-type="ref" data-reference="prop:edge-cycle">6.4</a> combine to $$\sigma_{uv}\ge
 \max\{2k-2,(k-1)^2-c\}=L_{k,n},$$ while its upper bound is $U_{k,n}$. Since $\sigma_{uv}$ is an integer, the first conclusion follows. If the two integer bounds coincide at $s$, then $\sigma_{uv}=s$ for every edge. Counting edge–five-cycle incidences gives $$5N_5=\sum_{uv\in E(G)}\sigma_{uv}
 =s|E(G)|=\frac{skn}{2},$$ which proves the divisibility condition. The strict-window version follows from the strengthened edge bounds above: for integral $\sigma_{uv}$, the inequality $\sigma_{uv}<U_{k,n}$ is equivalent to $\sigma_{uv}\le\lceil U_{k,n}\rceil-1$. ◻

</div>

<a id="order-bounds-in-degrees-six-through-nine"></a>

## Order bounds in degrees six through nine

<div id="thm:degree-six-fifty" class="theorem">

**Theorem 6.6**. *Every connected $6$-regular strict counterexample to WOW-284 has order at most $50$.*

</div>

<div class="proof">

*Proof.* To apply the order bound, we first reduce to diameter three. Theorem <a href="#thm:endpoint-diameter" data-reference-type="ref" data-reference="thm:endpoint-diameter">4.3</a> excludes diameter at least five, and Theorem <a href="#thm:diameter-four" data-reference-type="ref" data-reference="thm:diameter-four">4.4</a> excludes diameter four. Diameter two would force equality in the Moore bound, hence order $37$ and adjacency characteristic polynomial $(x-6)(x^2+x-5)^{18}$; its root sum is $-12$, contradicting $\operatorname{tr}A=0$. Diameter one is excluded by the girth hypothesis. Thus the diameter is three, and Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">6.1</a> gives $$n\le\left\lfloor\frac{3\cdot8^2\cdot39}{149}\right\rfloor=50.$$

There is also a short local obstruction to the first excluded order. If $n=51$, Corollary <a href="#cor:edge-cycle-sieve" data-reference-type="ref" data-reference="cor:edge-cycle-sieve">6.5</a> gives $\lceil L_{6,51}\rceil=\lfloor U_{6,51}\rfloor=11$, forcing $$5N_5=153\cdot11=1683,
 \qquad 5\nmid 1683,$$ which is impossible. An independent exact audit verifies the full diameter reduction and incidence calculation. ◻

</div>

<div id="cor:low-degree-windows" class="corollary">

**Corollary 6.7** (Low-degree order windows). *There is no regular strict counterexample of degree at most five. In degrees six through nine, every regular strict counterexample satisfies $$\begin{aligned}
k=6&:\quad n\le50,\\
k=7&:\quad n=50\text{ in diameter two, or }n\le74\text{ in diameter three},\\
k=8&:\quad n\le108,\\
k=9&:\quad n\le150.
\end{aligned}$$*

</div>

<div class="proof">

*Proof.* The degree exclusion is Theorem <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">4.2</a>, Theorem <a href="#thm:endpoint-diameter" data-reference-type="ref" data-reference="thm:endpoint-diameter">4.3</a> excludes diameter at least five, and Theorem <a href="#thm:diameter-four" data-reference-type="ref" data-reference="thm:diameter-four">4.4</a> removes diameter four for $k\le9$. For diameter three, Theorem <a href="#thm:three-to-one" data-reference-type="ref" data-reference="thm:three-to-one">6.1</a> gives, for $k=6,7,8,9$, respectively, $$n\le50,\ 75,\ 108,\ 150.$$ Since $7n=2|E(G)|$, the degree-seven bound improves to $74$. The diameter-two alternatives are determined by the Moore multiplicities: only the degree-seven, order-$50$ Hoffman–Singleton case survives. ◻

</div>

Appendix <a href="#app:three-to-one-arithmetic" data-reference-type="ref" data-reference="app:three-to-one-arithmetic">H</a> lists the corresponding order bounds through degree twenty, including the parity adjustment for odd degrees.

The degree-six order bound leaves the endpoint $n=50$ unresolved. Appendix <a href="#app:order50-details" data-reference-type="ref" data-reference="app:order50-details">A</a> gives further restrictions on adjacency multiplicity and cycle counts, and studies a signed graph associated with the excess matrix. These are necessary conditions; they do not establish whether a strict counterexample at this endpoint exists.

<a id="sec:punctures"></a>

# Distance spectra after vertex deletion in Moore graphs

Deleting vertices can increase the distances between those that remain. We identify these increases and use them to bound the change in the least distance eigenvalue. The full one- and two-deletion spectra are given in Appendix <a href="#app:small-deletion-spectra" data-reference-type="ref" data-reference="app:small-deletion-spectra">B</a>.

Let $M$ be a degree-$k$ Moore graph of diameter two and put $\Delta=\sqrt{4k-3}$.

<a id="changed-distances-and-a-stability-bound"></a>

## Changed distances and a stability bound

<div id="thm:small-puncture" class="theorem">

**Theorem 7.1** (Small-puncture normal form). *Let $M$ be a degree-$k$ Moore graph of diameter two, let $S\subseteq V(M)$ have size $s\le k-1$, and put $H=M-S$. Then $H$ is connected, has diameter at most three, and $$\boxed{\delta^*(H)=k-\frac{s}{k}.}$$ Let $B$ be the surviving-vertex by deleted-vertex incidence matrix, with $B_{xz}=1$ exactly when $x\sim_M z$. Then $$\boxed{
 D(H)=2(J-I)-A(H)+BB^{\mathsf T}
 -\operatorname{diag}(BB^{\mathsf T}).
 }$$*

</div>

<div class="proof">

*Proof.* The case $s=0$ is immediate, so assume $1\le s\le k-1$. Let $x,y\in V(H)$ be nonadjacent in $M$, and suppose their unique common neighbour $z$ lies in $S$. For every $a\in N_M(x)\setminus\{z\}$, the vertices $a,y$ are nonadjacent and have a unique common neighbour $b_a$. Thus $$x-a-b_a-y$$ is a length-three path. The $k-1$ paths are internally vertex-disjoint: if $b_a=b_{a'}$, there would be a four-cycle, and if $b_a=a'$, there would be a triangle through $x$. Apart from $z$, only $s-1\le k-2$ vertices have been deleted, so they cannot meet all these paths. At least one survives. Thus every destroyed length-two path is replaced by distance exactly three, giving the matrix formula.

For $x\in V(H)$, let $t_x=|N_M(x)\cap S|$. A deleted neighbour of $x$ is adjacent to no surviving neighbour of $x$, by triangle-freeness; each other deleted vertex has at most one common neighbour with $x$. Thus $$\sum_{y\in N_H(x)}t_y\le s-t_x.$$ Consequently, $$d_H^*(x)
 \ge k-\frac{s-t_x}{k-t_x}
 \ge k-\frac{s}{k},$$ where the last inequality follows from $$\left(k-\frac{s-t}{k-t}\right)-\left(k-\frac{s}{k}\right)
 =\frac{t(k-s)}{k(k-t)}\ge0.$$ The intersection bound $$\left|\bigcap_{z\in S}\Gamma_2(z)\right|
 \ge k^2+1-s(k+1)\ge2$$ provides a surviving vertex $x$ at distance two from every deleted vertex. This vertex attains the lower bound. For $z\in S$, let $y_z$ be the unique common neighbour of $x,z$. It cannot be deleted: $y_z\in S$ would, by the choice of $x$, require $d_M(x,y_z)=2$, contrary to $x\sim y_z$. All these common neighbours therefore survive, and each deleted vertex contributes once to the neighbour-degree deficit. The lower bound is consequently an equality. The replacement paths, boundary case $s=k-1$, distance formula, and attainment step are independently checked by [`scripts/verify_proof_audit_12_small_puncture.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_12_small_puncture.py). ◻

</div>

<div id="prop:deletion-stability" class="proposition">

**Proposition 7.2** (Deletion stability). *Let $G$ be connected with at least two vertices, let $S\subseteq V(G)$, and suppose $H=G-S$ is connected with at least two vertices. Put $$D_0=D(G)[V(H)],
 \qquad E_S=D(H)-D_0,$$ $$a=\delta^*(G),
 \quad b=\delta^*(H),
 \quad \gamma=\Phi(G).$$ Then $$\boxed{
 \Phi(H)\ge\gamma-(a-b)+\lambda_{\min}(E_S).
 }$$*

</div>

<div class="proof">

*Proof.* The score $\Phi(H)$ is the least eigenvalue of $D(H)+bI$. We write this matrix as $$D(H)+bI=(D_0+aI)+E_S-(a-b)I.$$ The first term is a principal submatrix of $D(G)+aI$, whose least eigenvalue is $\gamma$. Principal-submatrix interlacing ([Haemers 1995](#ref-Haemers1995), Corollary 2.2) therefore gives $\lambda_{\min}(D_0+aI)\ge\gamma$. Weyl’s inequality bounds the least eigenvalue after adding $E_S$, and subtracting $(a-b)I$ shifts every eigenvalue by $-(a-b)$. This gives the stated bound. For Moore punctures, $E_S$ is the explicit distance-increase matrix specified in Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>. ◻

</div>

<div id="cor:uniform-deletion" class="corollary">

**Corollary 7.3** (Uniform deletion stability). *Under the hypotheses of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>, put $$t_x=|N_M(x)\cap S|,
 \qquad
 \tau(S)=\max_{x\in V(M-S)}t_x.$$ Then $$\boxed{
 \Phi(M-S)\ge
 k-\frac{3+\sqrt{4k-3}}2-\frac{s}{k}-\tau(S).
 }$$ In particular, the deletion is a strict counterexample whenever the right-hand side is positive. Since $\tau(S)\le s$, every deletion of $s$ vertices is strict whenever $$\boxed{
 s\left(1+\frac 1k\right)
 <k-\frac{3+\sqrt{4k-3}}2.
 }$$ For $k>3$, equivalently, every deletion of at most $$r_k=\min\left\{
 k-1,\
 \left\lceil
 \frac{k}{k+1}\left(k-\frac{3+\sqrt{4k-3}}2\right)
 \right\rceil-1
 \right\}$$ vertices is strict. In particular, $r_7=2$; for a hypothetical degree-$57$ Moore graph, whose existence remains open ([Smith and Montemanni 2026](#ref-SmithMontemanni2026)), this estimate gives $r_{57}=47$. Proposition <a href="#prop:clique-deletion-bound" data-reference-type="ref" data-reference="prop:clique-deletion-bound">8.7</a> strengthens that guarantee to every deletion of at most $56$ vertices.*

</div>

<div class="proof">

*Proof.* By Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>, the distance-increase matrix is $$E_S=BB^{\mathsf T}-\operatorname{diag}(t_x).$$ Since $BB^{\mathsf T}\succeq0$ and $\operatorname{diag}(t_x)\preceq\tau(S)I$, one has $\lambda_{\min}(E_S)\ge-\tau(S)$. The parent Moore graph has score $$\Phi(M)=k-\frac{3+\sqrt{4k-3}}2,$$ and Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> shows that deletion lowers the minimum dual degree by $s/k$. Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">7.2</a> now gives the first bound. The second follows from $\tau(S)\le s$, and solving its strict scalar inequality for the largest integral $s$ gives $r_k$. ◻

</div>

<a id="one-and-two-vertex-deletions"></a>

## One and two vertex deletions

For one deleted vertex, and for the endpoints of an edge when $k\ge3$, the least distance eigenvalue is $-2-\sqrt{k}$. Combining this with the dual-degree formula gives, respectively, $$\Phi(M-v)=k-\frac1k-2-\sqrt{k},
 \qquad
 \Phi(M-\{u,v\})=k-\frac2k-2-\sqrt{k}\quad(uv\in E(M)).$$ Both scores are positive for every realizable integer $k\ge5$. Theorems <a href="#thm:one-puncture" data-reference-type="ref" data-reference="thm:one-puncture">B.1</a> and <a href="#thm:edge-puncture" data-reference-type="ref" data-reference="thm:edge-puncture">B.2</a> give the complete spectra in Appendix <a href="#app:small-deletion-spectra" data-reference-type="ref" data-reference="app:small-deletion-spectra">B</a>. For two nonadjacent deletions, Theorem <a href="#thm:nonadjacent-puncture" data-reference-type="ref" data-reference="thm:nonadjacent-puncture">B.3</a> also gives a full factorization and proves strictness for every realizable integer $k\ge6$. The stability bound above avoids these diagonalizations when only strictness is needed.

<a id="sec:robustness"></a>

# Uniform deletion bounds and the Hoffman–Singleton radius

The stability bound from Section <a href="#sec:punctures" data-reference-type="ref" data-reference="sec:punctures">7</a> handles many deletion sets without a new spectral calculation. We now improve it when the deleted vertices share a surviving neighbour. This proves stability through three deletions for Hoffman–Singleton. Exact orbit certificates cover sizes four and five and determine the sharp universal radius.

For a common surviving neighbour, the distance correction is a union of cliques. Its least eigenvalue gives the sharper bound below.

<div id="prop:neighbourhood-puncture" class="proposition">

**Proposition 8.1** (Neighbourhood punctures). *Let $M$ be a degree-$k$ Moore graph of diameter two, $k\ge2$. Let $w\in V(M)$, let $\varnothing\ne S\subseteq N_M(w)$, and put $s=|S|\le k-1$ and $H=M-S$. The distance-increase matrix $$E_S=D(H)-D(M)[V(H)]$$ is the adjacency matrix of $s$ copies of $K_k$ meeting only at $w$, together with $k(k-s)$ isolated vertices. In particular, $$\lambda_{\min}(E_S)
 =\frac{k-2-\sqrt{(k-2)^2+4s(k-1)}}2,$$ and $$\Phi(H)\ge
 k-\frac{3+\sqrt{4k-3}}2-\frac{s}{k}
 +\frac{k-2-\sqrt{(k-2)^2+4s(k-1)}}2.$$*

</div>

<div class="proof">

*Proof.* The deleted set is independent, since a pair of its vertices joined by an edge would form a triangle with $w$. Thus each deleted vertex has all $k$ of its neighbours in $H$. For distinct $z,z'\in S$, the Moore property gives $$N_M(z)\cap N_M(z')=\{w\}.$$ By Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>, every destroyed length-two path is replaced by a length-three path. Hence $(E_S)_{xy}=1$, for distinct surviving vertices $x,y$, precisely when they belong to $N_M(z)$ for some $z\in S$. There is at most one such $z$. These neighbourhoods therefore give the asserted cliques, with $k(k-s)$ remaining vertices.

We take the coordinate vector at the centre and the indicator vector of all noncentral clique vertices. Their span is invariant under the correction matrix. After normalizing both vectors to have length one, the matrix on this span is the normalized symmetric quotient $$\begin{pmatrix}
 0&\sqrt{s(k-1)}\\
 \sqrt{s(k-1)}&k-2
 \end{pmatrix}.$$ The other eigenvalues are $-1$ on the zero-sum space of the $k-1$ noncentral vertices of each clique, $k-2$ on the differences of their constant sums, and $0$ on the isolated vertices. These spaces have dimensions $s(k-2)$, $s-1$, and $k(k-s)$, respectively, so the decomposition is complete. The smaller quotient root is at most $-1$, because its characteristic polynomial has value $(k-1)(1-s)\le0$ at $-1$. It is therefore the least eigenvalue of $E_S$. The final inequality follows from Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">7.2</a> and $\delta^*(H)=k-s/k$. ◻

</div>

<div id="cor:analytic-three-puncture" class="corollary">

**Corollary 8.2** (Analytic three-vertex stability). *Let $M$ be the Hoffman–Singleton graph. For every $S\subseteq V(M)$ with $|S|\le3$, $$\Phi(M-S)>\frac17.$$ In particular, every such puncture is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* The graph $M$ has score $3$. If $|S|\le2$, Corollary <a href="#cor:uniform-deletion" data-reference-type="ref" data-reference="cor:uniform-deletion">7.3</a> gives $\Phi(M-S)\ge3-|S|/7-|S|\ge5/7$. Now let $|S|=3$, and put $$\tau=\max_{x\in V(M-S)}|N_M(x)\cap S|.$$ If $\tau\le2$, the same corollary gives $\Phi(M-S)\ge3-3/7-2=4/7$. If $\tau=3$, some surviving vertex $w$ is adjacent to all three deleted vertices. Proposition <a href="#prop:neighbourhood-puncture" data-reference-type="ref" data-reference="prop:neighbourhood-puncture">8.1</a> gives $$\Phi(M-S)\ge\frac{71-7\sqrt{97}}{14}>\frac17,$$ where the strict comparison follows from $49\cdot97=4753<4761=69^2$. ◻

</div>

<div id="thm:hs-radius" class="theorem">

**Theorem 8.3** (Hoffman–Singleton robustness radius). *Let $M$ be the Hoffman–Singleton graph. Every induced graph $M-S$ with $|S|\le5$ is a strict counterexample to WOW-284. This is sharp in the universal sense: there exists a six-vertex set whose deletion is not strict. Hence the universal vertex-deletion robustness radius is exactly five.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> gives $$\delta^*(M-S)=\frac{49-|S|}{7}.$$ Corollary <a href="#cor:analytic-three-puncture" data-reference-type="ref" data-reference="cor:analytic-three-puncture">8.2</a> proves strictness analytically for every set with $|S|\le3$. Only sets of sizes four and five remain to be certified. We reduce that finite check by automorphisms. Two explicitly stored permutations are verified edge by edge on the coordinate graph, and they generate a group of order $252000$. The full orbit inventory on deletion sets of sizes $0,1,2,3,4,5$ has counts $$1,1,2,4,11,33.$$ Thus the remaining sizes require $44$ representatives. For each one, exact fraction arithmetic gives $$7D(M-S)+(49-|S|)I\succ0.$$ The archived certificates for all $52$ original representatives are retained; those for the smaller sets provide redundant checks.

To show that the radius cannot be increased, delete $$\{P_{2,4},P_{3,1},P_{3,4},Q_{2,1},Q_{3,4},Q_{4,4}\}.$$ The resulting graph has $\delta^*=43/7$, while an exact $LDL^{\mathsf T}$ decomposition of $7D(M-S)+43I$ has exactly one negative and no zero pivot. Since $L$ is invertible, Sylvester’s law of inertia makes $7D(M-S)+43I$ indefinite, so the graph is not strict. Generator action, orbit exhaustion, BFS distances, the small-puncture formula, and a handwritten rational $LDL^{\mathsf T}$ implementation are independently checked by [`scripts/verify_proof_audit_13_hs_robustness.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_13_hs_robustness.py). ◻

</div>

<div class="remark">

*Remark 8.4*. The theorem asserts that every deletion through size five succeeds and that at least one deletion of size six fails. It does not assert that every six-vertex deletion fails.

</div>

<div id="prop:hs-neighbourhood-six" class="proposition">

**Proposition 8.5** (Six-neighbour punctures). *Let $M$ be the Hoffman–Singleton graph. For every $w\in V(M)$ and every $S\subseteq N_M(w)$ with $|S|=6$, the graph $M-S$ is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* Put $H=M-S$. Each vertex in $\Gamma_2(w)$ has a unique neighbour in $N_M(w)$, which we call its parent; the vertices adjacent to a given parent in the second sphere are its children. Partition $V(H)$ into $\{w\},A,B,C$, where $A=N_M(w)\setminus S$, $B$ consists of children of the deleted parents, and $C$ consists of children of the surviving parents. Their sizes are $$1,\qquad1,\qquad36,\qquad6.$$ The Moore property gives no edge between children of the same parent and exactly one neighbour in every other child class. Indeed, if $x$ has parent $p$ and $q\in N_M(w)\setminus\{p\}$, the unique common neighbour of the nonadjacent pair $x,q$ belongs to $\Gamma_2(w)$ and has parent $q$.

The distance sum from a vertex to each part depends only on its own part. For example, a vertex of $B$ has five siblings at distance three, five other vertices of $B$ at distance one, and twenty-five at distance two. Its distance sum to $B$ is therefore $5\cdot3+5\cdot1+25\cdot2=70$. Thus the partition is equitable for the distance matrix. On vectors constant on each part, the distance operator acts by the following row-sum quotient, in the order $\{w\},A,B,C$: $$Q=\begin{pmatrix}
 0&1&108&12\\
 1&0&72&6\\
 3&2&70&11\\
 2&1&66&10
 \end{pmatrix}.$$ The distances in the original Moore graph, restricted to the surviving vertices, are given by $D_0=2(J-I)-A(H)$. Proposition <a href="#prop:neighbourhood-puncture" data-reference-type="ref" data-reference="prop:neighbourhood-puncture">8.1</a> changes only the distances from $w$ to $B$ and between two children of the same deleted parent, adding one in each case.

Let $U$ be the four-dimensional space of vectors constant on each part. Its orthogonal complement $U^\perp$ consists of vectors whose coordinates sum to zero separately on each part. Both $D_0$ and the distance-increase matrix $E_S$ preserve $U$. Because they are symmetric, they also preserve $U^\perp$, so the two spaces can be checked separately.

We first bound the correction on $U^\perp$. The $w$-coordinate is zero because its part has only one vertex. For $x\in U^\perp$, $$x^{\mathsf T}E_Sx
 =\sum_{z\in S}\left(\sum_{y\in N_M(z)\setminus\{w\}}x_y\right)^2
   -\sum_{y\in B}x_y^2
 \ge-\lVert x\rVert^2.$$ The distance matrix of the original Moore graph has least eigenvalue $-4$. Taking its principal submatrix on the surviving vertices gives $D_0\succeq-4I$, and the correction estimate above gives $D(H)|_{U^\perp}\succeq-5I$. Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> gives $\delta^*(H)=43/7>5$.

It remains to check the restriction to $U$. In the basis of cell indicators, the quadratic form of $7D(H)+43I$ has symmetric matrix $$T=\operatorname{diag}(1,1,36,6)(7Q+43I)
 =\begin{pmatrix}
 43&7&756&84\\
 7&43&504&42\\
 756&504&19188&2772\\
 84&42&2772&678
 \end{pmatrix}.$$ Its leading principal minors are $$43,\qquad1800,\qquad4374000,\qquad226834992.$$ All four are positive, so Sylvester’s criterion gives $T\succ0$. The shifted distance matrix is therefore positive definite on both $U$ and $U^\perp$, proving $\Phi(H)>0$. ◻

</div>

These successful six-vertex deletions do not increase the universal radius: the deletion in Theorem <a href="#thm:hs-radius" data-reference-type="ref" data-reference="thm:hs-radius">8.3</a> still fails.

For a hypothetical degree-$57$ Moore graph, the neighbourhood calculation reaches the endpoint of the small-puncture theorem.

<div id="cor:degree57-neighbourhood" class="corollary">

**Corollary 8.6** (Degree-$57$ neighbourhood punctures). *If $M$ is a degree-$57$ Moore graph of diameter two, then for every $w\in V(M)$ and every $S\subseteq N_M(w)$ with $|S|\le56$, $$\Phi(M-S)>\frac{685}{57}.$$ In particular, every such induced graph is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2.2</a> gives the original Moore graph a score of $48$, which handles $S=\varnothing$. For nonempty $S$, put $s=|S|$. Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> applies through $s=56$: the survivor graph is connected and has minimum dual degree $57-s/57$. Its order is at least $3194$, and it inherits girth at least five. Proposition <a href="#prop:neighbourhood-puncture" data-reference-type="ref" data-reference="prop:neighbourhood-puncture">8.1</a> gives $$\lambda_{\min}(E_S)
 =\frac{55-\sqrt{55^2+224s}}2>-35,$$ since $$55^2+224s\le15569<15625=125^2.$$ The loss of minimum dual degree is exactly $s/57$, so Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">7.2</a> yields $$\Phi(M-S)\ge48-\frac{s}{57}+\lambda_{\min}(E_S)
 >48-\frac{56}{57}-35=\frac{685}{57}>0.$$ ◻

</div>

Grouping the correction cliques through one surviving vertex improves the estimate for arbitrary deletion sets.

<div id="prop:clique-deletion-bound" class="proposition">

**Proposition 8.7** (Splitting the distance correction at a vertex). *Let $M$ be a degree-$k$ Moore graph of diameter two, $k\ge2$, and let $S\subseteq V(M)$ have size $s\le k-1$. Put $H=M-S$, $$E_S=D(H)-D(M)[V(H)],
 \qquad
 \tau=\max_{x\in V(H)}|N_M(x)\cap S|,$$ and, for $0\le r\le k-1$, define $$f_k(r)=\frac{k-2-\sqrt{(k-2)^2+4r(k-1)}}2.$$ Then $$\lambda_{\min}(E_S)
 \ge \max\{-\tau,\,f_k(\tau)-s+\tau\},$$ and $$\Phi(H)\ge k-\frac{3+\sqrt{4k-3}}2-\frac{s}{k}
 +\max\{-\tau,\,f_k(\tau)-s+\tau\}.$$ In particular, if $M$ has degree $57$, then every $S\subseteq V(M)$ with $|S|\le56$ satisfies $$\Phi(M-S)\ge\frac{286}{57}>0.$$ Thus every such puncture is a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* For $s=0$, one has $\tau=0$, $f_k(0)=0$, and $E_S=0$, so the claims follow from Theorem <a href="#thm:moore-threshold" data-reference-type="ref" data-reference="thm:moore-threshold">2.2</a>. Assume $s\ge1$. For $z\in S$, let $b_z$ be the indicator vector of $N_M(z)\cap V(H)$, and put $$C_z=b_zb_z^{\mathsf T}-\operatorname{diag}(b_z).$$ The matrix $C_z$ records the distance increases caused by deleting $z$: it is the adjacency matrix of a clique on the surviving neighbours of $z$, with all other vertices isolated. Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> gives $E_S=\sum_{z\in S}C_z$. Each clique matrix has least eigenvalue at least $-1$, since $$C_z+I=b_zb_z^{\mathsf T}
       +\operatorname{diag}(\mathbf1-b_z)\succeq0.$$ The Gram-matrix estimate also gives $E_S\succeq-\tau I$.

To obtain the second bound, choose $w\in V(H)$ attaining $\tau$, and put $Z=N_M(w)\cap S$. Every deleted vertex has a surviving neighbour, since $s<k$, so $1\le|Z|=\tau\le k-1$. We group the $\tau$ clique matrices indexed by $Z$ and estimate the remaining $s-\tau$ separately. The correction matrix for deleting $Z$ alone is $$F_Z=D(M-Z)-D(M)[V(M-Z)].$$ By the small-puncture formula, its principal submatrix on $V(H)$ is exactly $\sum_{z\in Z}C_z$. Proposition <a href="#prop:neighbourhood-puncture" data-reference-type="ref" data-reference="prop:neighbourhood-puncture">8.1</a> gives $\lambda_{\min}(F_Z)=f_k(\tau)$, so interlacing bounds the least eigenvalue of this grouped sum below by $f_k(\tau)$. Each of the remaining clique matrices has least eigenvalue at least $-1$. Weyl’s inequality therefore yields $$\lambda_{\min}(E_S)
 \ge f_k(\tau)-(s-\tau).$$ Together with $E_S\succeq-\tau I$, this proves the first inequality. The score bound follows from Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">7.2</a> and $\delta^*(H)=k-s/k$.

For $k=57$, the original Moore graph has score $48$. If $\tau\le42$, the first bound gives $\lambda_{\min}(E_S)\ge-42$. If $\tau\ge43$, then $$(27+2\tau)^2-(55^2+224\tau)
 =4\bigl((\tau-43)(\tau+14)+28\bigr)>0.$$ Since $27+2\tau>0$, this implies $f_{57}(\tau)>14-\tau$, and hence $$\lambda_{\min}(E_S)>14-s\ge-42.$$ Consequently, for every $s\le56$, $$\Phi(M-S)\ge48-\frac{s}{57}-42
 \ge48-\frac{56}{57}-42=\frac{286}{57}>0.$$ ◻

</div>

<a id="sec:controls"></a>

# The equality boundary and a graph attaining it

The shifted adjacency window also identifies the equality case of WOW-284. We state the criterion and give an exact graph attaining it.

<div id="thm:equality-boundary" class="theorem">

**Theorem 9.1** (Equality boundary). *Let $G$ be connected, $k$-regular, of girth at least five and diameter three. Then $$\Phi(G)=0
 \quad\Longleftrightarrow\quad
 \max_{\theta\ne k}|\theta+1|=\sqrt{2k-2}.$$ Equivalently, $D+kI$ is positive semidefinite and singular. When $\Phi(G)=0$ and $2k-2$ is not a square, the two boundary adjacency eigenvalues occur with equal multiplicity, so the distance eigenvalue $-k$ has even multiplicity. If $2k-2$ is a square, then $k=2r^2+1$ for some integer $r$.*

</div>

<div class="proof">

*Proof.* This is immediate from Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a>. In the nonsquare case, the two boundary values are algebraic conjugates, so their multiplicities in the integral characteristic polynomial agree. In the square case, $2k-2=s^2$ forces $s$ even. The exact scalar audit is [`scripts/verify_equality_boundary.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_equality_boundary.py). ◻

</div>

Jørgensen’s $9$-regular order-$96$ graph of girth five is an exact equality case: $$\delta^*=9,
 \qquad \lambda_{\min}(D)=-9,$$ with multiplicity eight. The construction is due to Jørgensen ([Jørgensen 2005](#ref-Jorgensen2005)); the three local graph representations, handwritten graph6 decoder, characteristic polynomials, root intervals, and provenance boundary are checked by [`scripts/verify_proof_audit_09_jorgensen96.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_09_jorgensen96.py).

Appendix <a href="#app:excluded-constructions" data-reference-type="ref" data-reference="app:excluded-constructions">F</a> defines a balanced prime-field family of girth-five graphs and rules out strict counterexamples in that family when the diameter is three. It also rules out every layer-respecting perfect-matching deletion of Hoffman–Singleton considered there. These calculations test the window criterion but are not needed for the counterexamples or the deletion bounds above.

<a id="sec:scope"></a>

# Open questions on spectral constraints and stability

The necessary conditions at degree six and order $50$ do not settle existence. It remains to determine whether a graph satisfying them is a strict counterexample. The present results also do not determine the minimum order of a strict counterexample. Extending the regular-graph order bounds to irregular graphs is another direction.

<a id="disclosure-and-reproducibility."></a>

#### Disclosure and reproducibility.

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof exploration, and Lean formalization. Codex also assisted with organization and supplementary proof arguments. The author assumes full responsibility for the mathematics, attribution, and conclusions. The original source, exact certificates, and build instructions are available at [`github.com/SamPetkov/wow284`](https://github.com/SamPetkov/wow284). Release `v2.2.8` is the historical certificate baseline. The analytic additions in this v2 are given in the present source and are separate from that release.

<a id="app:order50-details"></a>

# Further restrictions at degree six and order fifty

<a id="the-adjacency-multiplicity-bound-at-order-fifty"></a>

## The adjacency multiplicity bound at order fifty

<div id="prop:order50-minus-two" class="proposition">

**Proposition A.1** (The order-$50$ $(-2)$-multiplicity bound). *Let $G$ be $6$-regular, of order $50$, and of girth at least five. The multiplicity $m_{-2}(A)$ of the adjacency eigenvalue $-2$ satisfies $$m_{-2}(A)\le20.$$*

</div>

<div class="proof">

*Proof.* We isolate the eigenvalue whose multiplicity is to be bounded. Put $m=m_{-2}(A)$, remove the principal eigenvalue $6$ and the $m$ copies of $-2$, and write $\mu_0,\ldots,\mu_4$ for the moments of the remaining eigenvalues. Girth at least five gives $$\operatorname{tr}A=0,\quad \operatorname{tr}A^2=300,\quad \operatorname{tr}A^3=0,\quad \operatorname{tr}A^4=3300,$$ and therefore $$(\mu_0,\mu_1,\mu_2,\mu_3,\mu_4)
 =(49-m,-6+2m,264-4m,-216+8m,2004-16m).$$ The moment matrix $$H=\begin{pmatrix}
 \mu_0&\mu_1&\mu_2\\
 \mu_1&\mu_2&\mu_3\\
 \mu_2&\mu_3&\mu_4
 \end{pmatrix}$$ is the Gram matrix obtained by evaluating the constant, linear, and quadratic monomials at the remaining eigenvalues, counted with multiplicity. It is therefore positive semidefinite, so its determinant is nonnegative. Expanding that determinant gives $$\det H=3600(1625-81m)\ge0.$$ Since $m$ is an integer, $m\le20$. ◻

</div>

<a id="cycle-counts-and-signed-structure-at-order-fifty"></a>

## Cycle counts and signed structure at order fifty

The order bound still allows the degree-six boundary case. We now restrict its possible cycle counts and signed Gram representation. These are necessary conditions; they do not settle existence.

<div id="thm:order50-feasibility" class="theorem">

**Theorem A.2**. *Let $G$ be a connected $6$-regular graph of order $50$ and girth at least five, and suppose $\Phi(G)>0$. Then $G$ has diameter three. For an edge $e$, let $\sigma_e$ be the number of five-cycles containing $e$. Then $\sigma_e\in\{12,13\}$. Call $e$ low or high according as $\sigma_e=12$ or $13$, respectively, and let $H$ be the spanning subgraph of high edges. Put $m=|E(H)|$, and let $\tau(v)$ be the number of five-cycles through $v$. Then $$\tau(v)\in\{36,37,38\},
 \qquad d_H(v)=2\tau(v)-72\in\{0,2,4\},$$ $$m\equiv0\pmod5,
 \qquad N_5=360+\frac m5.$$ For a two-edge path $u-v-w$, put $$R_{uvw}=6\alpha_{uvw}+\beta_{uvw},$$ where $\alpha$ and $\beta$ count the five- and six-cycles containing the path. The allowed values are $$\begin{array}{c|c}
\text{types of the two incident edges}&R_{uvw}\\
\hline
\text{low--low}&30,31,32\\
\text{mixed}&30,31,32\\
\text{high--high}&30,31.
\end{array}$$ Writing $S_2=\sum_vd_H(v)^2$, one has $$1950-m\le N_6
 \le2200-\frac{5m}{6}-\frac{S_2}{12},$$ $$\frac{43m^2-70200m+119632500}{58500}
 \le N_6
 <\frac{4220000-2200m-7m^2}{2000}.$$ Writing $$n_i=\bigl|\{v\in V(G):d_H(v)=i\}\bigr|
 \qquad(i\in\{0,2,4\}),$$ exact enumeration leaves $266$ triples $(n_0,n_2,n_4)$ such that $$n_0+n_2+n_4=50,\qquad
 m=n_2+2n_4\equiv0\pmod5,$$ and at least one integer $N_6$ satisfies all four displayed bounds, including the strict upper moment bound.*

</div>

<div class="proof">

*Proof.* The diameter reduction used in Theorem <a href="#thm:degree-six-fifty" data-reference-type="ref" data-reference="thm:degree-six-fifty">6.6</a> applies verbatim: diameter at least four gives a Rayleigh quotient at most $-8$, and diameter two gives the trace contradiction from $(x-6)(x^2+x-5)^{18}$. Hence the diameter is three. Proposition <a href="#prop:edge-cycle" data-reference-type="ref" data-reference="prop:edge-cycle">6.4</a> gives $$L_{6,50}=12,\qquad U_{6,50}=\frac{346}{25}<14.$$ Since $\sigma_e$ is integral, $\sigma_e\in\{12,13\}$ for every edge $e$. Around a fixed vertex $v$, write $\Gamma_i=\Gamma_i(v)$ for the distance layers; their sizes are $1,6,30,13$. We use the four distance layers to bound the five-cycle count. If $\tau$ is the number of five-cycles through $v$, take one indicator vector for each layer and normalize it to have length one. The adjacency quadratic form on their span has a symmetric matrix, the layer compression. This matrix is similar to the average row quotient. Its characteristic polynomial is $(x-6)q_\tau(x)$, where $$195q_\tau(x)
 =195x^3+(2250-43\tau)x^2+(105-30\tau)x+228\tau-11250.$$ In particular, $$195q_\tau(-1+\sqrt{10})
 =(-215+56\sqrt{10})\tau+7350-1860\sqrt{10}.$$ The coefficient of $\tau$ is negative because $56^2\cdot10<215^2$, and at $\tau=39$ the right-hand side is $9(-115+36\sqrt{10})<0$. Also $$195q_\tau(6)=1500(75-\tau).$$ Every vertex of $\Gamma_2$ has exactly one neighbour in $\Gamma_1$, and the edges inside $\Gamma_2$ are in bijection with the five-cycles through $v$. Hence $$e(\Gamma_2,\Gamma_3)
 =30\cdot5-2e(\Gamma_2)
 =150-2\tau>0,$$ because every vertex of the nonempty layer $\Gamma_3$ has a neighbour in $\Gamma_2$. Thus $q_\tau(6)>0$, whereas for $\tau\ge39$ its value at the upper end of the WOW window is negative. We obtain a root in $(-1+\sqrt{10},6)$, corresponding to a nonprincipal eigenvalue of the layer compression. By interlacing, the adjacency matrix then has a nonprincipal eigenvalue above the window, which is impossible. Conversely, $$150-2\tau=e(\Gamma_2,\Gamma_3)\le13\cdot6,$$ so $\tau\ge36$. Hence $\tau\in\{36,37,38\}$. Finally, $\sum_{e\ni v}\sigma_e=2\tau(v)$, so the high-edge degree is $2\tau(v)-72$; counting edge–five-cycle incidences gives $5N_5=12\cdot150+m$.

The next restrictions come from a two-path $u-v-w$. Girth at least five gives $(A^3)_{uw}=\alpha_{uvw}$ and $(A^4)_{uw}=16+\beta_{uvw}$. Let $h_e=0$ for a low edge and $h_e=1$ for a high edge. Substitution into the centered slack matrix gives $$25\mathcal S_6[\{u,v,w\}]=
 \begin{pmatrix}
 48&-2-25h_{uv}&773-25R_{uvw}\\
 -2-25h_{uv}&48&-2-25h_{vw}\\
 773-25R_{uvw}&-2-25h_{vw}&48
 \end{pmatrix}\succeq0.$$ The $2\times2$ minors give $R_{uvw}\in\{29,30,31,32\}$. At $R_{uvw}=29$, the Gram norm of $e_u-e_w$ vanishes, so this vector lies in the kernel of $\mathcal S_6$. On $\mathbf 1^\perp$, $\mathcal S_6=-g_6(A)$. The strict shifted window excludes the endpoint zeros of $g_6$, leaving only its double zero at $-2$. Thus $A(e_u-e_w)=-2(e_u-e_w)$, which is impossible: its $u$-coordinate would have to be both zero and $-2$. If both edges are high and $R_{uvw}=32$, the displayed determinant is $-33750$, also impossible. This proves the local table.

We now make the cycle count explicit. Sum over unoriented two-edge paths. Each five-cycle contains five such paths and each six-cycle contains six, so $$\sum_{u-v-w}R_{uvw}=30N_5+6N_6
                   =10800+6m+6N_6.$$ There are $50\binom62=750$ paths, of which $$\sum_v\binom{d_H(v)}2=\frac{S_2-2m}{2}$$ have two high edges. Every local value is at least $30$ and at most $32$, with upper bound $31$ for a high–high path. Hence $$22500\le10800+6m+6N_6
 \le24000-\frac{S_2-2m}{2}.$$ Rearranging gives the first pair of $N_6$ bounds. For the second pair, we evaluate polynomials on the shifted nonprincipal spectrum. A Gram matrix gives the lower bound, and a weighted Gram matrix gives the upper bound; the spectral window makes the weights positive. Appendix <a href="#app:order50-moment-bounds" data-reference-type="ref" data-reference="app:order50-moment-bounds">E</a> displays both matrices and their determinant calculations. The exact matrix calculations and enumeration are checked by [`scripts/verify_proof_audit_06_order50_feasibility.py`](https://github.com/SamPetkov/wow284/blob/ee387a20bb97c83d67f466c837e589509d6ad337/scripts/verify_proof_audit_06_order50_feasibility.py). The $266$ surviving profiles neither establish nor rule out a graph. ◻

</div>

<div id="rem:signed-root" class="remark">

*Remark A.3* (Signed-root Gram formulation). Under the hypotheses of Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">A.2</a>, put $$T=50J-g_6(A)-2I.$$ Then $$T\mathbf 1=2\mathbf 1,\qquad T+2I\succeq0,
 \qquad 25\mathcal S_6=25(T+2I)-2J.$$ This is the specialization of Proposition <a href="#prop:signed-complement" data-reference-type="ref" data-reference="prop:signed-complement">6.3</a>: the excess parameter is $r=42$, so the signed row sum is $2$. For vertices $u,z$ at distance three, put $$q_{uz}=6(A^3)_{uz}+(A^4)_{uz}.$$ The $2\times2$ estimate gives $q_{uz}\in\{48,49,50,51\}$, and the kernel argument in Theorem <a href="#thm:integral-slack" data-reference-type="ref" data-reference="thm:integral-slack">5.4</a> excludes $48$. Together with the edge and two-path intervals in Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">A.2</a>, this gives $$T_{uv}\in\{-1,0,1\}\qquad(u\ne v),\qquad T_{uu}=0.$$ Consequently $T+2I$ is the Gram matrix of $50$ vectors of norm $\sqrt2$, with inner products in $\{-1,0,1\}$ between distinct vectors. Its row sum is $4$; the signed adjacency matrix $T$ has row sum $2$. The kernel of $T+2I$ is $E_{-2}(A)$, so Proposition <a href="#prop:order50-minus-two" data-reference-type="ref" data-reference="prop:order50-minus-two">A.1</a> gives $$\operatorname{rank}(T+2I)\ge30.$$ Thus the unresolved degree-six boundary can be viewed as a root-type integral Gram problem constrained by the graph’s distance classes and local cycle data.

</div>

<a id="why-the-signed-complement-is-disconnected"></a>

## Why the signed complement is disconnected

<div id="thm:order50-disconnected" class="theorem">

**Theorem A.4** (Disconnected signed complement). *Under the hypotheses of Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">A.2</a>, the edge-signed graph with adjacency matrix $T$ from Remark <a href="#rem:signed-root" data-reference-type="ref" data-reference="rem:signed-root">A.3</a> is disconnected.*

</div>

<div class="proof">

*Proof.* Let $N_i$ denote the number of $i$-cycles in $G$. In terms of the degree-six nonbacktracking polynomials, $$\begin{aligned}
(g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
&+352F_5+78F_6+12F_7+F_8.
\end{aligned}$$ Girth at least five gives $\operatorname{tr}F_i(A)=0$ for $1\le i\le4$. For lengths five and six, every closed nonbacktracking walk is a directed cycle. At lengths seven and eight there are also the walks obtained by attaching a one-edge tail to a directed five- or six-cycle. Hence $$\begin{aligned}
\operatorname{tr}F_5(A)&=10N_5,&
\operatorname{tr}F_6(A)&=12N_6,\\
\operatorname{tr}F_7(A)&=14N_7+40N_5,&
\operatorname{tr}F_8(A)&=16N_8+48N_6.
\end{aligned}$$ These walk counts give the full trace of the squared polynomial. On the nonprincipal space, the signed matrix and the polynomial differ only by a sign, so their squares have the same trace there. We therefore subtract the principal adjacency contribution and add the square of the signed matrix’s eigenvalue $2$ on the constant vector, giving $$\operatorname{tr}T^2
=8(500N_5+123N_6+21N_7+2N_8-604100).$$ If $P_+$ and $P_-$ are the numbers of positive and negative signed edges, then the signed row sum and the zero diagonal give $$P_+-P_-=50,\qquad
\operatorname{tr}T^2=2(P_++P_-)=100+4P_-.$$ The polynomial expression for the trace is a multiple of eight. Comparing it with the signed-edge count shows that $P_-$ is odd.

We show that connectedness is incompatible with this parity. Suppose $T$ is connected. Proposition <a href="#prop:order50-minus-two" data-reference-type="ref" data-reference="prop:order50-minus-two">A.1</a> gives $\operatorname{rank}(T+2I)\ge30$. The representation theorem for connected edge-signed graphs with smallest eigenvalue at least $-2$ ([Greaves et al. 2015](#ref-GreavesEtAl2015), Theorem 2) represents $T+2I$ in a root system of type $D_\ell$ or $E_8$. The rank bound rules out $E_8$, leaving $$B^{\mathsf T}B=T+2I$$ for an integral matrix $B$ whose columns $b_u$ are roots $\pm e_i\pm e_j$. Put $s=B\mathbf 1$. Since $(T+2I)\mathbf 1=4\mathbf 1$, $$b_u\mathbin{\cdot}s=4\quad\text{for every }u,
\qquad
\lVert s\rVert^2=200.$$ Changing signs of coordinate axes if necessary, assume $s_i\ge0$. Form a multigraph with the used coordinates as vertices and one edge for each root column, joining its two nonzero coordinates. This is the coordinate-support multigraph. It is connected: otherwise the columns of $B$ would split into two families with zero inner products between them, and $T$ would be disconnected. If $v$ coordinates are used, then $$30\le v\le51:$$ the lower bound is the Gram rank, and a connected support multigraph with fifty root-edges has at most fifty-one vertices.

Every root joins two coordinate levels satisfying $\pm s_i\pm s_j=4$. Along such an edge, the levels either differ by four or sum to four. Starting from one coordinate and following the connected support multigraph, all levels must therefore lie in one of $$0,4,8,\ldots;\qquad
2,6,10,\ldots;\qquad
1,3,5,\ldots.$$ The first family would make $\lVert s\rVert^2$ divisible by $16$, contrary to $200\equiv8\pmod {16}$.

In the second family, a level at least $10$, together with the other $v-1\ge29$ levels, would contribute at least $10^2+29\cdot2^2>200$. Thus only levels $2$ and $6$ occur. If their multiplicities are $n_2,n_6$, then $$n_2+9n_6=50,\qquad
v=n_2+n_6=50-8n_6\ge30,$$ so $$(n_2,n_6)\in\{(50,0),(41,1),(32,2)\}.$$ Every root is now either $e_i+e_j$ with $s_i=s_j=2$, or $e_i-e_j$ with $s_i=6$ and $s_j=2$, after ordering the two coordinates. On a fixed support the sign pattern is unique, and duplicate columns would have inner product $2$. Distinct roots in this family therefore share at most one coordinate. At a level-two coordinate, let $p_i,m_i$ count positive and negative incidences. We have $p_i-m_i=2$. Each level-six coordinate has six incidences, all paired with negative incidences at level-two coordinates. A negative Gram product occurs when two roots meet at a level-two coordinate with opposite signs. The shared coordinate is unique, so each such product is counted once in $$P_-=\sum_{i:s_i=2}p_im_i.$$ Consequently $$P_-\equiv\sum_{i:s_i=2} p_im_i
\equiv\sum_{i:s_i=2} m_i
=6n_6
\equiv0\pmod2,$$ contradicting the parity already proved.

For the odd levels, let $a_t,c_t$ count coordinates at levels $4t+1,4t+3$, respectively. Sum the signed incidences along each of the two level chains. Difference roots cancel within a chain. The only roots joining the chains are sum roots $e_i+e_j$ between levels $1$ and $3$, and they contribute equally to the two sums. Hence $$\sum_{t\ge0}(4t+1)a_t
=\sum_{t\ge0}(4t+3)c_t.$$ To see the cancellation in the squared levels, write $$\begin{aligned}
(4t+1)^2-3&=16t(t+1)-2(4t+1),\\
(4t+3)^2-3&=16t(t+1)+2(4t+3).
\end{aligned}$$ After multiplying by $a_t$ and $c_t$ and summing, the linear terms cancel by the signed-incidence identity above. Since $\lVert s\rVert^2=200$, this gives $$\frac{200-3v}{32}
=\sum_{t\ge1}\binom{t+1}{2}(a_t+c_t).$$ The right-hand side is an integer. Hence $v\equiv24\pmod {32}$, which is impossible for $30\le v\le51$. All three level families are excluded, proving that $T$ is disconnected. ◻

</div>

<a id="app:small-deletion-spectra"></a>

# Exact spectra after one or two vertex deletions

Let $M$ be a degree-$k$ Moore graph of diameter two, and let $\Delta=\sqrt{4k-3}$.

The matrix in the following theorems is the recomputed distance matrix. Its correction is already given by Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>: a surviving nonadjacent pair moves from distance two to distance three exactly when its unique common neighbour was deleted.

<div id="thm:one-puncture" class="theorem">

**Theorem B.1** (One deleted vertex). *For $v\in V(M)$, put $H=M-v$. Then $$|V(H)|=k^2,
 \qquad \delta^*(H)=k-\frac1k,
 \qquad \lambda_{\min}(D(H))=-2-\sqrt{k}.$$ The complete distance spectrum is $$\begin{aligned}
\operatorname{Spec}D(H)={}&\{\rho_+,\rho_-\}
 \cup\{(-2+\sqrt{k})^{(k-1)},(-2-\sqrt{k})^{(k-1)}\}\\
&\cup\left\{\left(-\frac{\Delta+3}{2}\right)^{(m_+)},
\left(\frac{\Delta-3}{2}\right)^{(m_-)}\right\},
\end{aligned}$$ where $$\rho_\pm=k^2-2\pm\sqrt{k(k^3-2k^2+3k-1)},$$ $$m_\pm=\frac{k(k-2)(\Delta\pm1)}{2\Delta}.$$ Thus $$\Phi(H)=k-\frac1k-2-\sqrt{k},$$ which is positive exactly for integers $k\ge5$.*

</div>

<div id="thm:edge-puncture" class="theorem">

**Theorem B.2** (Endpoints of an edge). *Let $uv\in E(M)$ and $H=M-\{u,v\}$. For $k\ge3$, $$|V(H)|=k^2-1,
 \qquad \delta^*(H)=k-\frac2k,
 \qquad \lambda_{\min}(D(H))=-2-\sqrt{k}.$$ The complete distance spectrum is $$\begin{aligned}
\operatorname{Spec}D(H)={}&\{\sigma_+,\sigma_-,k-4\}\\
&\cup\{(-2+\sqrt{k})^{(2k-4)},(-2-\sqrt{k})^{(2k-4)}\}\\
&\cup\left\{\left(-\frac{\Delta+3}{2}\right)^{(a_+)},
\left(\frac{\Delta-3}{2}\right)^{(a_-)}\right\},
\end{aligned}$$ where $$\sigma_\pm=k^2-3\pm\sqrt{k^4-2k^3+3k^2-8k+7},$$ $$a_+=\frac{(k-2)(k+(k-2)\Delta)}{2\Delta},
 \quad
 a_-=\frac{(k-2)((k-2)\Delta-k)}{2\Delta}.$$ Thus $$\Phi(H)=k-\frac2k-2-\sqrt{k},$$ which is positive exactly for integers $k\ge5$.*

</div>

<div class="proof">

*Proof of Theorems <a href="#thm:one-puncture" data-reference-type="ref" data-reference="thm:one-puncture">B.1</a> and <a href="#thm:edge-puncture" data-reference-type="ref" data-reference="thm:edge-puncture">B.2</a>.* The metric facts stated above give the dual-degree formulas in the cases $s=1$ and $s=2$ of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>. We now write the changed-distance matrices in each case and compute their spectra.

In both cases, we separate the surviving neighbours of the deleted vertices from the vertices left over. Vectors constant on each part give the quotient matrices. On each neighbour part, choose an orthogonal basis of the vectors whose entries sum to zero. For each basis vector, form a second vector on the remaining vertices: at each vertex, sum the original entries on its neighbours. Each pair spans an invariant two-dimensional block. The vectors orthogonal to the cell-constant space and all these blocks give the Moore roots.

For one deleted vertex, put $A=N(v)$, $B=\Gamma_2(v)$, let $C$ be the $A$-by-$B$ incidence matrix, and let $B_0$ be the adjacency matrix on $B$. Only pairs inside $A$ lose their unique length-two path. By Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>, their new distance is three. All other distances are unchanged, so $$D(H)=\begin{pmatrix}3(J-I)&2J-C\\2J-C^{\mathsf T}&2(J-I)-B_0\end{pmatrix}.$$ The normalized constant quotient is $$Q_1=\begin{pmatrix}
 3(k-1)&(2k-1)\sqrt{k-1}\\
 (2k-1)\sqrt{k-1}&2k^2-3k-1
 \end{pmatrix},$$ whose eigenvalues are $\rho_\pm$. Block comparison in the Moore identity gives $$CC^{\mathsf T}=(k-1)I,\qquad
 CB_0=J-C,\qquad
 C^{\mathsf T}\mathbf 1_A=\mathbf 1_B,$$ $$B_0^2+C^{\mathsf T}C=(k-1)I-B_0+J.$$ Thus $C^{\mathsf T}$ is injective and $$\mathbb R^B=
 \langle\mathbf 1_B\rangle\perp
 C^{\mathsf T}(\mathbf 1_A^\perp)\perp K,
 \qquad K=\ker C,\qquad \dim K=k(k-2).$$ Choose an orthogonal basis $\mathcal B$ of $\mathbf 1_A^\perp$, and for $z\in\mathcal B$ put $$W_z=\operatorname{span}\{(z,0),(0,C^{\mathsf T}z)\}.$$ The quotient acts on the cell-constant space $W_{\mathrm{const}}$. The remaining directions split into the two-dimensional spaces $W_z$ for $z\in\mathcal B$ and the residual space $0\oplus K$. The identities above show that these spaces are invariant and mutually orthogonal. Put $$W_{\mathrm{inc}}=\bigoplus_{z\in\mathcal B}W_z.$$ Consequently $$\mathbb R^{V(H)}=W_{\mathrm{const}}\perp W_{\mathrm{inc}}\perp(0\oplus K),
 \qquad 2+2(k-1)+k(k-2)=k^2.$$ On a zero-sum incidence space, the action in the chosen generators is $\bigl(\begin{smallmatrix}-3&-(k-1)\\-1&-1\end{smallmatrix}\bigr)$, with eigenvalues $-2\pm\sqrt{k}$. The restriction to $K$ satisfies $B_0^2+B_0-(k-1)I=0$ and $D=-2I-B_0$, so only the two Moore roots remain. Their multiplicities are determined by the trace of $B_0$: after removing its principal eigenvalue $k-1$ and its $k-1$ copies of $-1$ on $C^{\mathsf T}(\mathbf 1_A^\perp)$, the remaining trace is zero. This trace and the residual dimension give $m_\pm$.

For an adjacent deleted pair, put $$A=N(u)\setminus\{v\},\qquad B=N(v)\setminus\{u\},\qquad
 C=V(M)\setminus\bigl(\{u,v\}\cup A\cup B\bigr).$$ Only pairs inside $A$ or inside $B$ lose a length-two path. Since $k\ge3$, Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a> applies to the two deleted vertices and makes the new distance of each such pair three. The antisymmetric constant line has eigenvalue $k-4$, and the normalized symmetric quotient is $$Q_2=\begin{pmatrix}
 5k-8&\sqrt{(k-1)(2k-3)(4k-6)}\\
 \sqrt{(k-1)(2k-3)(4k-6)}&2k^2-5k+2
 \end{pmatrix},$$ with eigenvalues $\sigma_\pm$. Let $R_A,R_B$ be the incidence matrices from $A,B$ to $C$, and let $T$ be the adjacency matrix on $C$. The Moore identity gives $$R_AR_A^{\mathsf T}=R_BR_B^{\mathsf T}=(k-1)I,\qquad
 R_AR_B^{\mathsf T}=J,$$ $$R_AT=J-R_A,\qquad R_BT=J-R_B,$$ $$R_A^{\mathsf T}R_A+R_B^{\mathsf T}R_B+T^2
 =(k-1)I-T+J.$$ The transpose maps of $R_A$ and $R_B$, restricted to their cell zero-sum spaces, are injective and have orthogonal images. Pair each zero-sum direction in its original cell with its incidence image. The resulting invariant two-dimensional spaces carry $\bigl(\begin{smallmatrix}-3&-(k-1)\\-1&-1\end{smallmatrix}\bigr)$, as in the one-vertex calculation. The residual space $$K=\ker R_A\cap\ker R_B,\qquad \dim K=(k-2)^2,$$ is invariant and satisfies $$T^2+T-(k-1)I=0,\qquad D=-2I-T.$$ These spaces and the three-dimensional cell-constant space are mutually orthogonal and complete, since $$3+2(2k-4)+(k-2)^2=k^2-1.$$ The constant direction of $T$ has eigenvalue $k-2$, while its two zero-sum incidence images contribute trace $-2(k-2)$. Since $\operatorname{tr}T=0$, one has $\operatorname{tr}(T|_K)=k-2$, and dimension and trace give $a_\pm$. The residual negative root is greater than $-2-\sqrt{k}$. For $k\ge3$, the antisymmetric constant root also satisfies $$(k-4)-(-2-\sqrt{k})=k-2+\sqrt{k}>0.$$ It remains to compare the incidence root with the smaller constant-quotient roots. We shift the quotients by the negative of the candidate root and test positive definiteness. In each case the leading diagonal entry is positive, and $$\det(Q_1+(2+\sqrt{k})I)
 =k(2k^2+2k^{3/2}-3k+2)>0,$$ $$\det(Q_2+(2+\sqrt{k})I)
 =(\sqrt{k}-1)(\sqrt{k}+1)
 (2k^2+2k^{3/2}-3k+2\sqrt{k}+6)>0.$$ The shifted symmetric quotients are therefore positive definite. The constant-quotient eigenvalues lie strictly above the incidence root, completing the comparison. Exact quotient normalization, trace-to-multiplicity equations, replacement paths, and all least-root comparisons are independently checked by [`scripts/verify_proof_audit_05_small_moore_punctures.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_05_small_moore_punctures.py). ◻

</div>

<div id="thm:nonadjacent-puncture" class="theorem">

**Theorem B.3** (Two nonadjacent deleted vertices). *Let $u,v$ be nonadjacent vertices of $M$, $k\ge5$, and put $H=M-\{u,v\}$. Define $$\begin{aligned}
R_k(x)={}&x^4+(10-2k^2)x^3+(2k^3-17k^2-2k+36)x^2\\
&+(12k^3-49k^2-4k+53)x\\
&-2k^4+17k^3-38k^2+5k+20,
\end{aligned}$$ $$M_- =\frac{k(k-2)+(k^2-4k+2)\Delta}{2\Delta},
 \quad
 M_+ =\frac{-k(k-2)+(k^2-4k+2)\Delta}{2\Delta}.$$ Then $$\begin{aligned}
\chi_{D(H)}(x)={}&(x-k+3)R_k(x)
 (x^2+4x-k+3)^{k-2}\\
&\cdot(x^2+4x-k+5)^{k-2}
 \left(x+\frac{\Delta+3}{2}\right)^{M_-}\\
&\cdot\left(x-\frac{\Delta-3}{2}\right)^{M_+}.
\end{aligned}$$ Moreover, $$\delta^*(H)=k-\frac2k,$$ and $H$ is a strict counterexample for every realizable integer $k\ge6$.*

</div>

<div class="proof">

*Proof.* The deleted vertices have a unique common neighbour $w$. With $A=N(u)\setminus\{w\}$, $B=N(v)\setminus\{w\}$, $C=N(w)\setminus\{u,v\}$, and $$Z=V(M)\setminus\bigl(\{u,v,w\}\cup A\cup B\cup C\bigr),$$ the surviving graph has cell sizes, in the order $\{w\},A,B,C,Z$, $$1,\quad k-1,\quad k-1,\quad k-2,\quad (k-1)(k-2).$$ The Moore common-neighbour rule gives a perfect matching between $A$ and $B$, and the five-cell partition is equitable. The distance rule from Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>, stated at the start of this section, applies because $2\le k-1$. If the unique length-two path between two surviving vertices passed through $u$ or $v$, a replacement path survives and their new distance is exactly three. We now restrict the distance matrix to vectors constant on each cell. The row-sum quotient is $$\begin{pmatrix}
0&3k-3&3k-3&k-2&2(k-1)(k-2)\\
3&3k-6&2k-3&2k-4&2k^2-7k+6\\
3&2k-3&3k-6&2k-4&2k^2-7k+6\\
1&2k-2&2k-2&2k-6&2k^2-7k+5\\
2&2k-3&2k-3&2k-5&2k^2-7k+5
\end{pmatrix}.$$ Its characteristic polynomial is $(x-k+3)R_k(x)$.

Identify $\mathbb R^A$ with $\mathbb R^B$ through the perfect matching, and let $R_A,R_B,R_C$ be the incidence matrices from the three nonconstant cells to $Z$. Let $T$ be the adjacency matrix on $Z$. The Moore identity gives $$\begin{gathered}
R_AR_A^{\mathsf T}=R_BR_B^{\mathsf T}=(k-2)I,\quad
R_CR_C^{\mathsf T}=(k-1)I,\\
R_AR_B^{\mathsf T}=J-I,\quad
R_AR_C^{\mathsf T}=R_BR_C^{\mathsf T}=J,\\
R_AT+R_B=J-R_A,\quad
R_BT+R_A=J-R_B,\quad
R_CT=J-R_C,\\
R_A^{\mathsf T}R_A+R_B^{\mathsf T}R_B+R_C^{\mathsf T}R_C+T^2
=(k-1)I-T+J.
\end{gathered}$$ Moreover, every vertex of $Z$ has one neighbour in each of $A,B,C$, so $$R_A^{\mathsf T}\mathbf 1_A
 =R_B^{\mathsf T}\mathbf 1_B
 =R_C^{\mathsf T}\mathbf 1_C
 =\mathbf 1_Z,
 \qquad T\mathbf 1_Z=(k-3)\mathbf 1_Z.$$

Use the coordinate order $(\{w\},A,B,C,Z)$. Choose orthogonal bases $\mathcal B_A$ of $\mathbf 1_A^\perp$ and $\mathcal B_C$ of $\mathbf 1_C^\perp$. For $\xi\in\mathcal B_A$ and $\eta\in\mathcal B_C$, put $$\begin{aligned}
u_\xi^\pm&=(0,\xi,\pm\xi,0,0),&
v_\xi^\pm&=(0,0,0,0,
 (R_A^{\mathsf T}\pm R_B^{\mathsf T})\xi),\\
u_\eta^C&=(0,0,0,\eta,0),&
v_\eta^C&=(0,0,0,0,R_C^{\mathsf T}\eta),
\end{aligned}$$ and define $$W_\xi^\pm=\operatorname{span}\{u_\xi^\pm,v_\xi^\pm\},
 \qquad
 W_\eta^C=\operatorname{span}\{u_\eta^C,v_\eta^C\}.$$ The incidence identities ensure that these generators give genuine two-dimensional spaces: the relevant maps are injective. They also show that the spaces are mutually orthogonal and orthogonal to the five-dimensional cell-constant space $W_{\mathrm{const}}$. For the residual space $$K=\ker R_A\cap\ker R_B\cap\ker R_C$$ one has $$K\subseteq\mathbf 1_Z^\perp,\qquad
 \dim K=(k-2)(k-4),\qquad T(K)\subseteq K.$$ Thus $W_{\mathrm{const}}$, the modules $W_\xi^\pm,W_\eta^C$, and $0\oplus0\oplus0\oplus0\oplus K$ form an orthogonal direct sum, since $$5+4(k-2)+2(k-3)+(k-2)(k-4)=k^2-1.$$

In the ordered generator pairs $(u_\xi^+,v_\xi^+)$, $(u_\xi^-,v_\xi^-)$, and $(u_\eta^C,v_\eta^C)$, respectively, the distance operator has matrices $$\begin{pmatrix}-4&-(k-3)\\-1&0\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-2\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-1\end{pmatrix}.$$ These give the two displayed quadratic factors and $k-3$ copies of each Moore linear factor. On $K$, the $Z$-block identity gives $$T^2+T-(k-1)I=0,
 \qquad D(H)|_K=-2I-T.$$ The constant direction of $Z$ has $T$-eigenvalue $k-3$, while the $Z$-images in the symmetric, antisymmetric, and common-neighbour modules have eigenvalues $-2,0,-1$, with dimensions $k-2,k-2,k-3$, respectively. Since $\operatorname{tr}T=0$, $$\operatorname{tr}(T|_K)=2(k-2).$$ The residual adjacency operator has just two possible eigenvalues, so its dimension and trace determine both multiplicities. We add the Moore-root copies from the common-neighbour spaces to obtain the full exponents $M_-$ and $M_+$.

This completes the spectral factorization. The value $\delta^*(H)=k-\frac2k$ again follows from the $s=2$ case of Theorem <a href="#thm:small-puncture" data-reference-type="ref" data-reference="thm:small-puncture">7.1</a>. To prove strictness, it is simpler to bound the distance correction than to locate the least root of the quartic. Put $$E_S=D(H)-D(M)[V(H)].$$ The correction $E_S$ records exactly the pairs whose distance has increased. Up to a simultaneous permutation of rows and columns, it is the adjacency matrix of two copies of $K_k$ meeting in $w$, together with $k(k-2)$ isolated vertices. Therefore $$\lambda_{\min}(E_S)=\frac{k-2-\sqrt{k^2+4k-4}}2.$$ Since the parent Moore graph has score $k-(3+\Delta)/2$ and deletion lowers the minimum dual degree by $2/k$, Proposition <a href="#prop:deletion-stability" data-reference-type="ref" data-reference="prop:deletion-stability">7.2</a> gives $$\Phi(H)\ge
 \frac{3k-5-\Delta-\sqrt{k^2+4k-4}}2-\frac2k.$$ For $k\ge7$, one has $$\sqrt{4k-3}<k-1,
 \qquad
 \sqrt{k^2+4k-4}<k+2.$$ Indeed, the corresponding differences of squares are $k(k-6)+4>0$ and $8>0$. The preceding lower bound is therefore greater than $$\frac{k-6}{2}-\frac2k
 \ge\frac12-\frac27=\frac3{14}>0.$$ For $k=6$, use $\sqrt{21}<23/5$ and $\sqrt{56}<15/2$, which follow from $529>525$ and $225>224$. The same lower bound is then greater than $$\frac{13-23/5-15/2}{2}-\frac13=\frac7{60}>0.$$ Thus $\Phi(H)>0$ for every realizable integer $k\ge6$. The direct-sum decomposition, injectivity, orthogonality, all recomputed distances, and the strict comparison are independently checked by [`scripts/verify_proof_audit_03_nonadjacent_puncture.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_03_nonadjacent_puncture.py) and [`scripts/verify_research_extensions_exact.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_research_extensions_exact.py). ◻

</div>

<a id="app:second-sphere-proof"></a>

# The distance spectrum of a Moore second sphere

This is the complete proof of Theorem <a href="#thm:second-subconstituent" data-reference-type="ref" data-reference="thm:second-subconstituent">2.5</a>. The main-text statement records the graph parameters and the resulting distance eigenvalue; here we give the incidence blocks and their multiplicities.

<div class="proof">

*Proof.* Each vertex of the second sphere loses exactly one neighbour when we pass to its induced graph. Put $m=K(K-1)$; the Moore property gives $\lvert\Gamma_2(v)\rvert=m$. Each vertex of $\Gamma_2(v)$ has its single parent in $N(v)$, while each vertex of $N(v)$ has $K-1$ neighbours in $\Gamma_2(v)$. The induced graph $X$ consequently has order $m$ and degree $(K-1)$. It contains no triangle or four-cycle, since $M$ contains neither. To obtain the distance spectrum we now calculate the adjacency spectrum and then prove that the diameter is three.

Relative to $\{v\}\sqcup N(v)\sqcup\Gamma_2(v)$, let $C\in\{0,1\}^{K\times m}$ be the incidence block from $N(v)$ to $\Gamma_2(v)$, and let $B\in\{0,1\}^{m\times m}$ be the adjacency matrix of $X$. Write $J_{a,b}$ for the $a\times b$ all-ones matrix and $J_a=J_{a,a}$. Then $$C\mathbf 1_m=(K-1)\mathbf 1_K,
 \qquad
 C^{\mathsf T}\mathbf 1_K=\mathbf 1_m.$$ The Moore identity ([Hoffman and Singleton 1960, sec. 4](#ref-HoffmanSingleton1960)), read in the corresponding blocks, gives $$CC^{\mathsf T}=(K-1)I_K,
 \qquad
 CB=J_{K,m}-C,$$ and $$C^{\mathsf T}C+B^2=(K-1)I_m-B+J_m.$$ Since $CC^{\mathsf T}=(K-1)I_K$, the map $C^{\mathsf T}$ is injective. The incidence block therefore gives the orthogonal decomposition $$\mathbb R^m
 =\langle\mathbf 1_m\rangle\perp
 C^{\mathsf T}(\mathbf 1_K^\perp)\perp\ker C.$$ The first space is the principal adjacency eigenspace, because $B\mathbf 1_m=(K-1)\mathbf 1_m$. Transposing the identity for $CB$ shows that $B$ acts as $-I$ on $C^{\mathsf T}(\mathbf 1_K^\perp)$. The same identity makes $\ker C$ invariant under $B$; moreover, $\ker C\subseteq\mathbf 1_m^\perp$. The final block identity restricts there to $$(B^2+B-(K-1)I_m)|_{\ker C}=0.$$ Thus the remaining eigenvalues are among $$r,s=\frac{-1\pm\sqrt{4K-3}}2.$$ Finally, $$\dim\ker C=m-K=K(K-2),
 \qquad
 \operatorname{tr}(B|_{\ker C})=0,$$ because the eigenvalue $K-1$ cancels the $K-1$ copies of $-1$ in $\operatorname{tr}B=0$. Hence the multiplicities $p,q$ of $r,s$ satisfy $$p+q=K(K-2),\qquad pr+qs=0,$$ so $$p=\frac{K(K-2)(1+\sqrt{4K-3})}{2\sqrt{4K-3}},
 \qquad
 q=\frac{K(K-2)(\sqrt{4K-3}-1)}{2\sqrt{4K-3}}.$$ Both roots occur. It remains to check that $X$ has diameter three. If the unique common neighbour in $M$ of nonadjacent vertices $x,y\in X$ lies in $X$, their distance in $X$ is two. The only other possibility is their common parent in $N(v)$. Choose $b\in N_X(x)$, and let $p$ be the common parent of $x,y$. The parent of $b$ is not $p$, since otherwise $p,x,b$ would form a triangle. Moreover $b\not\sim y$, and the unique common neighbour $c$ of $b,y$ belongs to $X$: it cannot be $v$, and it cannot lie in $N(v)$, since $b$ and $y$ have different parents there. Thus $x-b-c-y$ is a path in $X$. Each parent has $K-1\ge2$ children, and pairs of distinct children have no length-two path in $X$. Thus $X$ has diameter three and Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a> applies. Among the nonprincipal adjacency eigenvalues, $(-1+\sqrt{4K-3})/2$ maximizes $|\theta+1|$; substitution gives $$\lambda_{\min}(D(X))=-\frac{5+\sqrt{4K-3}}2.$$ For $K=3,4,5$, direct comparison gives a nonpositive score. For $K\ge6$, both sides of the relevant comparison are positive, and the threshold reduces to $$(2K-7)^2-(4K-3)=4(K^2-8K+13)>0$$ because $K>4+\sqrt3$. The finite $K=7$ instance is checked by [`scripts/verify_wow284_38_40_42.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_wow284_38_40_42.py). ◻

</div>

<a id="app:lp-slack-positivity"></a>

# Positivity of the dual LP slack

Use the measure, support points, and slack notation from the proof of Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a>. We verify the positivity of every slack beyond degree four, as used in its optimality and rigidity argument.

We check the first five values exactly and then bound the tail. For $5\le i\le9$, removing the common positive factor $k(k-1)(k+2)(k^2+3)/6$ leaves, respectively, $$2,\quad 5k-13,\quad 2(3k^2-17k+25),$$ $$6k^3-47k^2+139k-150,
 \quad
 2(3k^4-27k^3+106k^2-219k+194),$$ all positive for $k\ge4$; for the nontrivial residual factors this follows after writing $k=m+4$, when all coefficients are nonnegative and the constant terms are positive. For $i\ge10$, put $r=k-1\ge3$. The support lies in $[-2\sqrt r,2\sqrt r]$, because $1+\sqrt{2r}\le2\sqrt r$. For $|z|\le1$, the recurrence gives $$F_i(2\sqrt r\,z)
 =r^{i/2}U_i(z)-r^{(i-2)/2}U_{i-2}(z),$$ where $U_j$ is the Chebyshev polynomial of the second kind. Using $|U_j(z)|\le j+1$, the total mass $B_k-1$, and $F_i(k)=kr^{i-1}$, we obtain $$\begin{aligned}
 \frac{|\mu(F_i)|}{F_i(k)}
 &\le \frac{r^2+4r+6}{6}\,r^{-i/2}\bigl((i+1)r+i-1\bigr)\\
 &\le \frac{2i+1}{3}\,r^{3-i/2}
 \le \frac{2i+1}{3}\,3^{3-i/2}.
\end{aligned}$$ The last two inequalities use $r\ge3$ and $i\ge10$. At $i=10$ the right-hand side is $7/9$, and it decreases thereafter because $3(2i+1)^2-(2i+3)^2=8i^2-6>0$. Hence $$\frac{|\mu(F_i)|}{F_i(k)}<1\qquad(i\ge10).$$ The measure’s contribution has smaller absolute value than the principal contribution. Their sum, and therefore every slack in the tail, is positive.

<a id="app:order50-moment-bounds"></a>

# Six-cycle bounds from shifted spectral moments

We give the determinant calculation for the second pair of six-cycle bounds in Theorem <a href="#thm:order50-feasibility" data-reference-type="ref" data-reference="thm:order50-feasibility">A.2</a>. Work under its hypotheses. The earlier part of its proof has established diameter three and $N_5=360+m/5$, where $m$ counts the high edges. Let $\theta_1,\ldots,\theta_{49}$ be the nonprincipal adjacency eigenvalues, and put $$y_i=\theta_i+1,\qquad s_j=\sum_{i=1}^{49}y_i^j\quad(0\le j\le6).$$ Theorem <a href="#thm:diameter-three-score" data-reference-type="ref" data-reference="thm:diameter-three-score">3.1</a> gives $|y_i|<\sqrt{10}$.

Girth and regularity give $$\operatorname{tr}A=\operatorname{tr}A^3=0,\qquad \operatorname{tr}A^2=300,\qquad \operatorname{tr}A^4=3300.$$ For the degree-six nonbacktracking polynomials from Proposition <a href="#prop:higher-transfer" data-reference-type="ref" data-reference="prop:higher-transfer">3.3</a>, the recurrence gives $$F_5(x)=x^5-21x^3+85x,\qquad
 F_6(x)=x^6-26x^4+165x^2-150.$$ A closed nonbacktracking walk of length five or six is a cycle: a repeated vertex before the final return would leave a cycle of length at least five and require at least two further steps. Each cycle is counted once for every starting vertex and orientation. Thus $\operatorname{tr}F_5(A)=10N_5$ and $\operatorname{tr}F_6(A)=12N_6$, yielding $$(\operatorname{tr}A^j)_{j=0}^6
 =(50,0,300,0,3300,3600+2m,43800+12N_6).$$ The principal adjacency eigenvalue is six. Binomial expansion therefore gives $$s_j=\sum_{r=0}^j\binom jr\operatorname{tr}A^r-7^j,$$ and hence $$(s_0,\ldots,s_6)
 =(49,43,301,607,2749,6343+2m,1801+12m+12N_6).$$

For the lower bound, take the vectors $u_i=(1,y_i,y_i^2,y_i^3)^{\mathsf T}$. Their Gram sum is $$\mathsf M=\sum_{i=1}^{49}u_i u_i^{\mathsf T}
 =(s_{a+b})_{a,b=0}^3
 =
 \begin{pmatrix}
 49&43&301&607\\
 43&301&607&2749\\
 301&607&2749&6343+2m\\
 607&2749&6343+2m&1801+12m+12N_6
 \end{pmatrix}\succeq0.$$ For the upper bound, put $v_i=(1,y_i,y_i^2)^{\mathsf T}$ and weight each rank-one matrix by $10-y_i^2>0$. The resulting localizing matrix is $$\mathsf L=\sum_{i=1}^{49}(10-y_i^2)v_i v_i^{\mathsf T}
 =(10s_{a+b}-s_{a+b+2})_{a,b=0}^2
 =
 \begin{pmatrix}
 189&-177&261\\
 -177&261&-273-2m\\
 261&-273-2m&25689-12m-12N_6
 \end{pmatrix}\succ0.$$ For strict positivity, diameter three implies that $I,A,A^2,A^3$ are linearly independent: evaluate a linear relation successively at vertex pairs of distances three, two, one, and zero. Since $A$ is symmetric, it has at least four distinct eigenvalues. Connectedness makes the principal eigenvalue simple, so at least three distinct values occur among the $y_i$. A nonzero polynomial of degree at most two cannot vanish at all three. Together with $10-y_i^2>0$, this shows that the quadratic form of $\mathsf L$ is positive on every nonzero vector. This support argument does not give positive definiteness of the four-by-four matrix $\mathsf M$, whose test polynomials have degree at most three.

Expanding the determinants gives $$\begin{aligned}
 \det\mathsf M
 &=1200(58500N_6-43m^2+70200m-119632500),\\
 \det\mathsf L
 &=108(4220000-2200m-7m^2-2000N_6).
\end{aligned}$$ Thus $\det\mathsf M\ge0$ and $\det\mathsf L>0$. Dividing by the positive constants and isolating $N_6$ gives $$\frac{43m^2-70200m+119632500}{58500}
 \le N_6
 <\frac{4220000-2200m-7m^2}{2000}.$$

<a id="app:excluded-constructions"></a>

# Spectral exclusions for two construction families

The prime-field family below does not produce strict counterexamples of diameter three. None of the layer-respecting perfect-matching deletions considered in the second subsection is a strict counterexample. Their definitions and proofs are kept together so the coordinate calculations can be read independently of the principal counterexamples and deletion bounds.

<a id="the-prime-field-construction-in-diameter-three"></a>

## The prime-field construction in diameter three

For an odd prime $q\ge7$ and $1\le m\le q$, define $G(q,m)$ on vertices $P_{i,j},Q_{k,\ell}$, with $0\le i,k<m$ and $j,\ell\in\mathbb F_q$, by $$\begin{aligned}
P_{i,j}&\sim P_{i,j\pm1},\\
Q_{k,\ell}&\sim Q_{k,\ell\pm2},\\
P_{i,j}&\sim Q_{k,ik+j}.
\end{aligned}$$ This is a balanced specialization of known finite-field girth-five constructions ([Abreu et al. 2008](#ref-AbreuEtAl2008)). It is $(m+2)$-regular. A coordinate common-neighbour calculation shows that it has no triangle or $4$-cycle for $q\ge7$: for a cross pair, the possible same-side common neighbours require residues in the disjoint sets $\{\pm1\}$ and $\{\pm2\}$.

<div id="thm:prime-field" class="theorem">

**Theorem F.1**. *If $G(q,m)$ has diameter three, then it is not a strict counterexample to WOW-284.*

</div>

<div class="proof">

*Proof.* The degree restriction first excludes $m\le3$ by Theorem <a href="#thm:regular-degree-six" data-reference-type="ref" data-reference="thm:regular-degree-six">4.2</a>. For the remaining degrees, we first consider vectors that assign the same value to all vertices of a given type with a fixed first coordinate. Taking neighbour sums leaves these vectors constant on the same sets. The restricted adjacency matrix has eigenvalues $m+2$, $2-m$, and $2$ with multiplicity $2m-2$; the shifted WOW window leaves only $m\in\{4,5,6\}$.

This restriction is the zero-frequency block of the Fourier transform in the second coordinate. We now use a nonzero character to exclude the last three cases. Let $\omega=e^{2\pi\mathrm i/q}$. On the nonzero character $t=1$, the adjacency block has form $$\begin{pmatrix}aI&M\\M^*&bI\end{pmatrix},
 \qquad a=2\cos\frac{2\pi}{q},
 \quad b=2\cos\frac{4\pi}{q},
 \quad M_{ik}=\omega^{ik}.$$ If $\sigma$ is a singular value of $M$, the associated two-dimensional invariant subspace carries $\bigl(\begin{smallmatrix}a&\sigma\\\sigma&b\end{smallmatrix}\bigr)$. We need only the largest singular value, rather than the full Fourier spectrum. Since $\|M\|_F^2=m^2$, one singular value satisfies $\sigma^2\ge m$. Its two-dimensional block therefore supplies a nonprincipal eigenvalue at least $$\sqrt m+\frac{a+b}{2}
 \ge \sqrt m+\cos(\pi/7)-\frac12.$$ For $q\ge7$, both $\cos(2\pi/q)$ and $\cos(4\pi/q)$ increase with $q$, so their sum is minimized at $q=7$. The last inequality then uses $2\cos(2\pi/7)+2\cos(4\pi/7)=2\cos(\pi/7)-1$. Moreover $\cos(\pi/7)>\sqrt3/2$, and $h(m)=\sqrt{2m+2}-\sqrt m$ is increasing for $m\ge1$ and satisfies $$h(m)\le h(6)=\sqrt{14}-\sqrt6
 <\frac{27}{20}<\frac{\sqrt3+1}{2}.$$ Thus the displayed nonprincipal eigenvalue lies above $-1+\sqrt{2m+2}$ for $m=4,5,6$. The common-neighbour case split, Fourier reduction, radical comparisons, and exact $q=7$ controls are independently checked by [`scripts/verify_proof_audit_08_prime_field.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_08_prime_field.py). ◻

</div>

<a id="why-layer-respecting-edge-deletions-fail-wow-284"></a>

## Why layer-respecting edge deletions fail WOW-284

For $\pi\in S_5$, delete the perfect matching $$\mathcal M_\pi=\bigl\{\{P_{i,j},Q_{\pi(i),i\pi(i)+j}\}:i,j\in\mathbb F_5\bigr\}$$ from the Hoffman–Singleton graph.

<div id="thm:matching-deletions" class="theorem">

**Theorem F.2**. *Each deletion produces a connected simple $6$-regular graph of order $50$, girth five, and diameter four. The $120$ labelled graphs form exactly two isomorphism classes. The $20$ affine permutations have $$\lambda_{\min}(D)=-13,
 \qquad \Phi=-7,$$ and the $100$ nonaffine permutations have $$\lambda_{\min}(D)=-6-\sqrt{61},
 \qquad \Phi=-\sqrt{61}.$$ Thus none of these graphs is a counterexample.*

</div>

<div class="proof">

*Proof.* Every $P_{i,j}$ occurs once in $\mathcal M_\pi$; for a fixed $Q_{k,\ell}$, the unique incident matching edge is obtained from $i=\pi^{-1}(k)$ and $j=\ell-ik$. Thus $\mathcal M_\pi$ is a perfect matching, and its deletion leaves a simple $6$-regular graph. Deleting edges cannot create a short cycle, while the same-layer pentagons remain; exact breadth-first search gives connectedness and diameter four.

Explicit type-preserving and type-swapping coordinate automorphisms generate orbits of sizes $20$ and $100$. The representatives have different adjacency characteristic polynomials, so the orbits are distinct isomorphism classes. Exact distance characteristic polynomials and Sturm separators give the stated least roots. All $120$ matchings, $400$ coordinate maps, $48{,}000$ matching images, orbit coverage, graph hypotheses, and root certificates are checked by [`scripts/verify_proof_audit_07_layer_matchings.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_07_layer_matchings.py). ◻

</div>

<a id="app:small-example-certificates"></a>

# Finite spectral computations and deletion checks

We record the exact spectral and matrix computations used above, together with the graph data and the inequalities they establish. The graph encodings are fixed in `data/graphs/` and `data/cages55/`; the coordinate definitions of the small counterexamples are given above Theorem <a href="#thm:explicit-examples" data-reference-type="ref" data-reference="thm:explicit-examples">2.4</a>.

For the four degree-five cages, the displayed factor divides $\det(xI-D)$ over $\mathbb Z[x]$. Its negative root is an eigenvalue, which suffices for $\lambda_{\min}(D)<-5$; no assertion that it is the least eigenvalue is needed. $$\begin{array}{lcc}
\toprule
\text{fixed graph6 record}&\text{distance factor}&\text{eigenvalue}\\
\midrule
\text{Foster}&x^2+6x-11&-3-2\sqrt5\\
\text{Meringer}&x+6&-6\\
\text{Robertson--Wegner}&x+6&-6\\
\text{Wong}&x^2+6x-11&-3-2\sqrt5\\
\bottomrule
\end{array}$$ The records have order $30$, degree five, girth five and diameter three, and are pairwise nonisomorphic. Meringer’s classification ([Meringer 1999, 142](#ref-Meringer1999)) supplies completeness. The integer characteristic polynomials, graph properties and nonisomorphism checks are reproduced by [`scripts/verify_proof_audit_04_regular_low_degree.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_04_regular_low_degree.py).

For $H_{38}$, the factor $x^2+6x+2$, together with the exact Sturm count, identifies the least distance root as $-3-\sqrt7$. An independent rational $LDL^{\mathsf T}$ decomposition of $3D(H_{38})+17I$ has inertia $(38,0,0)$, where the entries count positive, negative and zero eigenvalues. For $H_{39}$, the decomposition of $6D(H_{39})+35I$ has inertia $(39,0,0)$. Thus each shift is positive definite and proves strictness. For $R$ and $X_{42}$, the exact spectra in Theorem <a href="#thm:explicit-examples" data-reference-type="ref" data-reference="thm:explicit-examples">2.4</a> identify the least eigenvalue $-5$. These graph, metric, dual-degree and matrix checks are reproduced by [`scripts/verify_wow284_38_40_42.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_wow284_38_40_42.py).

The two labelled deletion families of $R$ have the following common distance characteristic polynomials. For every $v\in V(R)$, $$\begin{aligned}
\det(xI-D(R-v))=P_{39}(x):={}&x^9(x+5)^{12}(x^2+6x+3)\\
&\cdot(x^3+3x^2-15x-7)^2(x^3+3x^2-15x-3)^2\\
&\cdot(x^4-78x^3+303x^2-70x-450),
\end{aligned}$$ whereas for every $uv\in E(R)$, $$\begin{aligned}
\det(xI-D(R-\{u,v\}))=P_{38}(x):={}&x^4(x-2)(x+5)^8(x^2+6x+2)^2\\
&\cdot(x^3+3x^2-15x-3)\\
&\cdot(x^4+5x^3-7x^2-23x-6)\\
&\cdot(x^5+9x^4+7x^3-77x^2-54x-4)\\
&\cdot(x^9-67x^8-404x^7+1772x^6+7205x^5\\
&\hspace{3em}-18489x^4-17018x^3+20288x^2+16824x+1680).
\end{aligned}$$

The $40$ singleton and $120$ edge-endpoint deletions are exhausted by [`scripts/verify_descendant_families.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_descendant_families.py); the root and positive-definiteness checks accompany the family records.

For Hoffman–Singleton, the two stored automorphisms generate a group of order $252000$. The orbit counts on deletion sets of sizes $0$ through $5$ are $1,1,2,4,11,33$, and for each size the orbit cardinalities sum to $\binom{50}{s}$. For every representative with $s=4$ or $5$, $$\operatorname{inertia}\bigl(7D(M-S)+(49-s)I\bigr)=(50-s,0,0).$$ This checks $11+33=44$ representatives; all $52$ representatives through size five are retained. The six-vertex set displayed in Theorem <a href="#thm:hs-radius" data-reference-type="ref" data-reference="thm:hs-radius">8.3</a> instead gives inertia $(43,1,0)$ for $7D(M-S)+43I$, proving failure of strictness. The verifier [`scripts/verify_proof_audit_13_hs_robustness.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_13_hs_robustness.py) checks the generator action, orbit exhaustion, BFS distances, dual degrees and exact rational congruence. The orbit classification and the matrix sign are separate checks; both are required.

<a id="app:three-to-one-arithmetic"></a>

# Order comparisons and divisor checks for the three-to-one bound

For comparison, the unadjusted diameter-three bounds in degrees $6$ through $20$ are $$\begin{array}{c|rrrrrrrrrrrrrrr}
 k&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20\\
 \hline
 n&50&75&108&150&201&263&336&422&521&635&765&911&1075&1257&1459.
\end{array}$$ When $k$ is odd, $kn=2|E(G)|$ requires $n$ to be even; in particular, the entries for $k=7,11,15,17,19$ improve to $74,262,634,910,1256$, respectively.

Only the mixed two-component cases remain after the direct inequality excludes $n=2r+8$. Write $C_k=(k+2)^2(k^2+3)$ and $d_k=12k+27$. For $n=3r+t$, the identity $r=2C_k-d_kn$ gives $$(1+3d_k)r=2C_k-d_kt.$$ In particular, $18k+41$ divides the numerator on the right. Modulo this linear divisor, multiplication by $18^4$ gives the integer remainder in the middle column below. Enumerating its positive divisors of the form $18k+41$, with $k\ge6$, gives the last column. $$\begin{array}{ccc}
\toprule
t&\text{remainder}&\text{candidate }k\\
\midrule
8&412586&\text{none}\\
10&482570&123\\
\bottomrule
\end{array}$$ For $t=10$ and $k=123$, substitution gives an odd value of $kn$, contradicting the handshake identity. These divisions and candidates are checked over the integers by [`scripts/verify_proof_audit_14_three_to_one.py`](https://github.com/SamPetkov/wow284/blob/v2.2.8/scripts/verify_proof_audit_14_three_to_one.py).

<a id="sec:verification"></a>

# Exact certificates and the scope of Lean verification

The computer-assisted arguments have three specific tasks: certify the labelled finite graphs, exhaust the stated finite orbit families, and check symbolic identities derived in the text. No theorem-level sign or eigenvalue ordering uses floating-point arithmetic. The computations use SymPy and NetworkX ([Meurer et al. 2017](#ref-MeurerEtAl2017); [Hagberg, Schult, and Swart 2008](#ref-HagbergSchultSwart2008)). The Lean results below provide a separate layer of formal verification.

The historical release `v2.2.8` archives the labelled graph data, exact rational and polynomial certificates, and finite-orbit records used for the computer-assisted steps. The analytic additions to this v2 are proved in the text.

For the explicit $50$-vertex graph, Lean 4.31 with Mathlib 4.31 ([Moura and Ullrich 2021](#ref-deMouraUllrich2021); [The mathlib Community 2020](#ref-Mathlib2020)) checks structural and exact rational matrix certificates. The development pins the toolchain and dependency revision in [`lean/lean-toolchain`](https://github.com/SamPetkov/wow284/blob/v2.2.8/lean/lean-toolchain) and [`lean/lake-manifest.json`](https://github.com/SamPetkov/wow284/blob/v2.2.8/lean/lake-manifest.json). It checks the coordinate graph, regularity, the exhaustive common-neighbour certificate, girth five, the adjacency-square identity, the algebraic formula for the case-defined $0/1/2$ matrix, and an exact rational diagonalization with multiplicities. The diameter-two certificate identifies that matrix with the actual distance matrix in the mathematical proof. Regularity and diagonalization then give $$\delta^*(G)=7,\qquad \lambda_{\min}(D(G))=-4,\qquad \Phi(G)=3.$$ In the historical certificate baseline these conclusions are assembled in the paper rather than exported as a combined graph-distance theorem.

Lean also kernel-checks finite spectral certificates attached to the explicit constructions of orders $38,39,40,42$. At orders $38,39,42$, they certify the dual-degree data and positive definiteness of the relevant shifted distance matrix. At order $40$, they certify an invertible exact diagonalization, multiplicities, an attained minimum diagonal entry of $-5$, dual degree six, and gap one. These are finite matrix certificates rather than end-to-end `SimpleGraph.dist` formalizations.

Separately, Lean formalizes the analytic optimization statement in Theorem <a href="#thm:lp-ceiling" data-reference-type="ref" data-reference="thm:lp-ceiling">5.3</a>. For every integer $k\ge4$ and every admissible finitely supported expansion $$f=\sum_i c_iF_i,
  \qquad c_0>0,
  \qquad c_i\ge0\quad(i\ge5),
  \qquad f\vert_{I_k}\le0,$$ it proves $$B_kc_0\le f(k),
  \qquad B_k=\frac{(k+2)(k^2+3)}6.$$ The formal development defines the coefficient family of the displayed quartic $f_*$, proves that it is admissible and attains equality, and proves that the equality cases are exactly the positive scalar multiples of $f_*$, both as polynomials and at coefficient level. The imported release development is sorry-free and kernel-checked by Lean 4.31.

This LP formalization is deliberately graph-independent. It does not formalize the trace interpretation of the $F_i(A)$, the girth-five vanishing and nonnegativity statements, or the passage from the LP inequality to graph-order bounds. The integral-slack consequences, signed-complement theory, puncture spectra, and deletion results lie outside this Lean development. They are proved in the text using the analytic and, where explicitly identified, exact computer-assisted components. This is the precise scope of the Lean claims in the paper.

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-AbreuEtAl2008" class="csl-entry">

Abreu, Marién, Martin Funk, Domenico Labbate, and Vito Napolitano. 2008. “A Family of Regular Graphs of Girth 5.” *Discrete Mathematics* 308 (10): 1810–15. <https://doi.org/10.1016/j.disc.2007.04.031>.

</div>

<div id="ref-AouchicheHansen2014" class="csl-entry">

Aouchiche, Mustapha, and Pierre Hansen. 2014. “Distance Spectra of Graphs: A Survey.” *Linear Algebra and Its Applications* 458: 301–86. <https://doi.org/10.1016/j.laa.2014.06.010>.

</div>

<div id="ref-Backelin2015" class="csl-entry">

Backelin, Jörgen. 2015. “Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49.” <https://arxiv.org/abs/1511.08128>.

</div>

<div id="ref-CameronEtAl1976" class="csl-entry">

Cameron, Peter J., Jean-Marie Goethals, Johan J. Seidel, and Ernest E. Shult. 1976. “Line Graphs, Root Systems, and Elliptic Geometry.” *Journal of Algebra* 43 (1): 305–27. <https://doi.org/10.1016/0021-8693(76)90162-9>.

</div>

<div id="ref-CapyBuild2026" class="csl-entry">

Capy Build. 2026. “CE10: Refuting Graffiti 284.” Public agent transcript. <https://tokiwa.space/f/more-front-minute.pdf>.

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

Fajtlowicz, Siemion. 1998. “Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti.” Technical report. University of Houston.

</div>

<div id="ref-Fiol2016" class="csl-entry">

Fiol, Miquel Àngel. 2016. “Quotient-Polynomial Graphs.” *Linear Algebra and Its Applications* 488: 363–76. <https://doi.org/10.1016/j.laa.2015.09.053>.

</div>

<div id="ref-GreavesEtAl2015" class="csl-entry">

Greaves, Gary, Jack H. Koolen, Akihiro Munemasa, Yoshio Sano, and Tetsuji Taniguchi. 2015. “Edge-Signed Graphs with Smallest Eigenvalue Greater Than -2.” *Journal of Combinatorial Theory, Series B* 110: 90–111. <https://doi.org/10.1016/j.jctb.2014.07.006>.

</div>

<div id="ref-Haemers1995" class="csl-entry">

Haemers, Willem H. 1995. “Interlacing Eigenvalues and Graphs.” *Linear Algebra and Its Applications* 226–228: 593–616. <https://doi.org/10.1016/0024-3795(95)00199-2>.

</div>

<div id="ref-Hafner2003" class="csl-entry">

Hafner, Paul R. 2003. “The Hoffman–Singleton Graph and Its Automorphisms.” *Journal of Algebraic Combinatorics* 18 (1): 7–12. <https://doi.org/10.1023/A:1025136524481>.

</div>

<div id="ref-HagbergSchultSwart2008" class="csl-entry">

Hagberg, Aric A., Daniel A. Schult, and Pieter J. Swart. 2008. “Exploring Network Structure, Dynamics, and Function Using NetworkX.” In *Proceedings of the 7th Python in Science Conference*, 11–15. <https://doi.org/10.25080/TCWV9851>.

</div>

<div id="ref-HoffmanSingleton1960" class="csl-entry">

Hoffman, Alan J., and Robert R. Singleton. 1960. “On Moore Graphs with Diameters 2 and 3.” *IBM Journal of Research and Development* 4 (5): 497–504. <https://doi.org/10.1147/rd.45.0497>.

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

Meurer, Aaron et al. 2017. “SymPy: Symbolic Computing in Python.” *PeerJ Computer Science* 3: e103. <https://doi.org/10.7717/peerj-cs.103>.

</div>

<div id="ref-deMouraUllrich2021" class="csl-entry">

Moura, Leonardo de, and Sebastian Ullrich. 2021. “The Lean 4 Theorem Prover and Programming Language.” In *Automated Deduction—CADE 28*, 12699:625–35. Lecture Notes in Computer Science. Springer. <https://doi.org/10.1007/978-3-030-79876-5_37>.

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

The mathlib Community. 2020. “The Lean Mathematical Library.” In *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 367–81. Association for Computing Machinery. <https://doi.org/10.1145/3372885.3373824>.

</div>

<div id="ref-WilbanksAnnie2026" class="csl-entry">

Wilbanks, Nathan, and Annie. 2026. “Graffiti 284 Refuted by Hoffman–Singleton: An Independent Exact Verification.” AGNT Labs verification note. <https://agnt.gg/whitepapers/graffiti-284-refutation>.

</div>

<div id="ref-Wong1979" class="csl-entry">

Wong, Pak-Ken. 1979. “On the Uniqueness of the Smallest Graph of Girth 5 and Valency 6.” *Journal of Graph Theory* 3 (4): 407–9. <https://doi.org/10.1002/jgt.3190030413>.

</div>

</div>
