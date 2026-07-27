#!/usr/bin/env python3
"""Apply the audited mathematical, citation, and prose corrections to v2.2.

The preserved bootstrap is immutable.  This script is therefore deliberately
fail-closed: every replacement must match exactly once, and every citation and
inline repository path is checked after the rewrite.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "v22" / "main.tex"
BIB = ROOT / "v22" / "references.bib"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def revise_tex(text: str) -> str:
    replacements: list[tuple[str, str, str]] = [
        (
            "fonts",
            r"\usepackage{newtxtext,newtxmath}",
            r"\IfFileExists{newtxtext.sty}{%" "\n"
            r"  \usepackage{newtxtext,newtxmath}%" "\n"
            r"}{%" "\n"
            r"  \usepackage{lmodern}%" "\n"
            r"}",
        ),
        (
            "abstract-diameter-scope",
            "four; the diameter-four regime starts only at degree ten.",
            "four; diameter-four counterexamples are excluded through degree nine.",
        ),
        (
            "conjecture-citation",
            "Aouchiche and Hansen record the following Graffiti conjecture and attribute it\n"
            "to Fajtlowicz's 1998 \\emph{Written on the Wall} report\n"
            "\\cite[Conjecture~7.16]{AouchicheHansen2014,Fajtlowicz1998}.",
            "Aouchiche and Hansen record the following Graffiti conjecture as\n"
            "Conjecture~7.16 and attribute it to Fajtlowicz's 1998\n"
            "\\emph{Written on the Wall} report\n"
            "\\cite{Fajtlowicz1998} (see also \\cite[Conjecture~7.16]{AouchicheHansen2014}).",
        ),
        (
            "computer-assisted-scope",
            "Every computer-assisted theorem is accompanied by a conventional proof and an\n"
            "inline reference to an independent exact verifier.  The code is part of the\n"
            "public release \\texttt{v2.2.0}; a path such as\n"
            "\\codefile{scripts/verify_proof_audit_01_edge_local.py} links to the exact file\n"
            "used for the corresponding audit.",
            "The analytic arguments are proved in the text.  Precisely specified finite\n"
            "classifications and matrix certificates are treated as computer-assisted proof\n"
            "components, each with an inline reference to an independent exact verifier.\n"
            "The code is part of release \\texttt{v2.2.0}; a path such as\n"
            "\\codefile{scripts/verify_proof_audit_01_edge_local.py} identifies the exact\n"
            "file used for the corresponding audit.",
        ),
        (
            "h39-table-note",
            "\\end{array}\n\\]\nMoreover, all \\(40\\) labelled singleton deletions of \\(R\\), and all \\(120\\)\n",
            "\\end{array}\n\\]\nThe entry for \\(H_{39}\\) records an exact strict lower bound obtained from\n"
            "positive definiteness of \\(6D+35I\\); it is not a decimal approximation to the\n"
            "least eigenvalue.  Moreover, all \\(40\\) labelled singleton deletions of \\(R\\),\n"
            "and all \\(120\\)\n",
        ),
        (
            "second-subconstituent-least-root",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots on \\(\\ker C\\).  The\n"
            "remaining vertices sharing the unique neighbour of a chosen vertex are at\n"
            "distance three, so Theorem~\\ref{thm:diameter-three-score} applies.  The threshold\n"
            "reduces to\n",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  The remaining vertices sharing\n"
            "the unique neighbour of a chosen vertex are at distance three, so\n"
            "Theorem~\\ref{thm:diameter-three-score} applies.  Among the nonprincipal\n"
            "adjacency eigenvalues, \\((-1+\\sqrt{4K-3})/2\\) maximizes\n"
            "\\(|\\theta+1|\\); substitution gives\n"
            "\\[\n"
            " \\lambda_{\\min}(D(X))=-\\frac{5+\\sqrt{4K-3}}2.\n"
            "\\]\n"
            "The threshold reduces to\n",
        ),
        (
            "regular-low-degree-proof",
            "For \\(k=4\\), diameter two would require a degree-four Moore graph, whose\n"
            "adjacency multiplicities are nonintegral.  In diameter three, the exact LP\n"
            "bound of Theorem~\\ref{thm:lp-ceiling} gives \\(n<19\\), while the radius-two\n"
            "ball and diameter give \\(n\\ge18\\).  Regularity forces \\(n=18\\).  The\n"
            "nine-dimensional rational distance-three module would be annihilated by the\n"
            "irreducible polynomial \\(x^2+x-4\\), which is impossible in odd dimension.\n"
            "\n"
            "For \\(k=5\\), diameter two again fails the Moore multiplicity condition.\n"
            "Diameter four is excluded by Cauchy interlacing with the principal distance\n"
            "matrix of a diametral \\(P_5\\), whose least eigenvalue is below \\(-5\\).\n"
            "Diameter three is reduced by the order bounds to \\(n=30,31,32\\); parity excludes\n"
            "\\(31\\), normalized layer compressions exclude \\(32\\), and Meringer's\n"
            "isomorph-free enumeration leaves exactly four \\((5,5)\\)-cages at order \\(30\\)\n"
            "\\cite{Meringer1999}.  Each has an exact distance eigenvalue at most \\(-5\\).\n",
            "For \\(k=4\\), diameter two would require a degree-four Moore graph, whose\n"
            "adjacency multiplicities are nonintegral.  In diameter three, the exact LP\n"
            "bound of Theorem~\\ref{thm:lp-ceiling} gives \\(n<19\\), whereas the\n"
            "radius-two ball has \\(17\\) vertices and diameter three requires at least one\n"
            "more.  Hence \\(n=18\\).  The distance-three matrix is then a perfect matching.\n"
            "Its \\(-1\\)-eigenspace \\(W\\) is a nine-dimensional rational subspace of\n"
            "\\(\\one^\\perp\\), and\n"
            "\\[\n"
            " A_3=J+3I-A-A^2\n"
            " \\quad\\Longrightarrow\\quad\n"
            " (A^2+A-4I)|_W=0.\n"
            "\\]\n"
            "The polynomial \\(x^2+x-4\\) is irreducible over \\(\\mathbb Q\\), so a rational\n"
            "space on which it annihilates an operator has even dimension, a contradiction.\n"
            "\n"
            "For \\(k=5\\), diameter two again fails the Moore multiplicity condition.\n"
            "A diametral geodesic in diameter four yields the principal submatrix\n"
            "\\(D(P_5)\\), whose factor \\(x^2+6x+4\\) supplies the eigenvalue\n"
            "\\(-3-\\sqrt5<-5\\); Cauchy interlacing excludes this case.  In diameter\n"
            "three, Meringer's lower bound and Theorem~\\ref{thm:lp-ceiling} leave\n"
            "\\(n\\in\\{30,31,32\\}\\), and parity removes \\(31\\).  At \\(n=32\\), the\n"
            "normalized distance-layer compression has nonprincipal factor\n"
            "\\[\n"
            " p_{5,6}(x)=4x^3+10x^2-16x-30,\n"
            " \\qquad p_{5,6}(11/6)=-29/27<0.\n"
            "\\]\n"
            "Its largest root therefore exceeds \\(11/6>-1+\\sqrt8\\), contradicting the\n"
            "open shifted window.  At \\(n=30\\), Meringer's isomorph-free enumeration\n"
            "leaves exactly four \\((5,5)\\)-cages \\cite{Meringer1999}; each fixed record has\n"
            "an exact distance eigenvalue at most \\(-5\\).\n",
        ),
        (
            "diameter-four-rayleigh",
            "Assign weights \\(\\alpha,\\beta,-\\alpha,-\\beta\\) to\n"
            "\\(u,U,v,V\\), respectively.  Exact accounting gives a Rayleigh quotient at\n"
            "most that of\n"
            "\\[\n"
            " \\begin{pmatrix}-4&-2\\sqrt{k}\\\\-2\\sqrt{k}&-3\\end{pmatrix},\n"
            "\\]\n",
            "Assign weights \\(\\alpha,\\beta,-\\alpha,-\\beta\\) to\n"
            "\\(u,U,v,V\\), respectively.  Counting unordered pairs and then doubling gives\n"
            "\\[\n"
            " \\frac{x^{\\mathsf T}D(G)x}{x^{\\mathsf T}x}\n"
            " \\le\n"
            " \\frac{-4\\alpha^2-4k\\alpha\\beta-3k\\beta^2}\n"
            " {\\alpha^2+k\\beta^2}.\n"
            "\\]\n"
            "After setting \\(y_1=\\alpha\\) and \\(y_2=\\sqrt{k}\\,\\beta\\), the\n"
            "right-hand side is the Rayleigh quotient of\n"
            "\\[\n"
            " \\begin{pmatrix}-4&-2\\sqrt{k}\\\\-2\\sqrt{k}&-3\\end{pmatrix},\n"
            "\\]\n",
        ),
        (
            "moment-strictness",
            "The sum cannot vanish,\n"
            "because that would force every nonprincipal adjacency eigenvalue to be \\(-2\\),\n"
            "contradicting the trace equation.",
            "The sum cannot vanish: otherwise every nonprincipal adjacency eigenvalue\n"
            "would equal \\(-2\\), and \\(\\tr A=0\\) would give\n"
            "\\(k-2(n-1)=0\\), or \\(n=(k+2)/2\\), incompatible with the elementary\n"
            "bound \\(n\\ge k+1\\) for a simple \\(k\\)-regular graph.",
        ),
        (
            "lp-trace-explanation",
            "For a \\(k\\)-regular graph of girth at least five whose nonprincipal spectrum\n"
            "lies in \\(I_k\\), nonbacktracking-walk counts give\n"
            "\\[\n"
            " nf_0\\le\\tr f(A)\\le f(k),\n"
            "\\]\n"
            "and hence \\(n\\le f(k)/f_0\\).",
            "For a \\(k\\)-regular graph of girth at least five whose nonprincipal spectrum\n"
            "lies in \\(I_k\\), one has \\(\\tr F_i(A)=0\\) for \\(1\\le i\\le4\\), while\n"
            "\\(\\tr F_i(A)\\ge0\\) for \\(i\\ge5\\), since these traces count closed\n"
            "nonbacktracking walks.  The coefficient conditions therefore give\n"
            "\\(nf_0\\le\\tr f(A)\\).  On the other hand, \\(f(\\theta)\\le0\\) for every\n"
            "nonprincipal eigenvalue, so \\(\\tr f(A)\\le f(k)\\).  Thus\n"
            "\\[\n"
            " nf_0\\le\\tr f(A)\\le f(k),\n"
            " \\qquad n\\le\\frac{f(k)}{f_0}.\n"
            "\\]",
        ),
        (
            "order50-statement",
            "Let \\(G\\) be a connected \\(6\\)-regular strict counterexample of order \\(50\\).\n",
            "Let \\(G\\) be a connected \\(6\\)-regular graph of order \\(50\\) and girth\n"
            "at least five, and suppose \\(\\Phi(G)>0\\).  Then \\(G\\) has diameter three.\n",
        ),
        (
            "order50-proof",
            "A normalized distance-layer compression gives the range for \\(\\tau(v)\\), and\n"
            "edge--cycle incidence gives the even high-edge subgraph.  The centered matrix\n"
            "from Proposition~\\ref{prop:edge-cycle}, restricted to three vertices of a\n"
            "two-path, gives exact Gram determinants.  A kernel argument removes the\n"
            "apparent equality value \\(r=29\\).  Summing local inequalities gives the first\n"
            "pair of \\(N_6\\) bounds; shifted moment and localizing matrices give the second.\n",
            "By Theorem~\\ref{thm:degree-six-fifty}, the diameter is three.  Around a fixed\n"
            "vertex the distance layers have sizes \\(1,6,30,13\\).  If \\(\\tau\\) is the\n"
            "number of five-cycles through the centre, the average row quotient is similar\n"
            "to the symmetric compression on normalized layer indicators.  Its\n"
            "nonprincipal factor \\(q_\\tau\\) satisfies\n"
            "\\[\n"
            " 195q_\\tau(-1+\\sqrt{10})\n"
            " =(-215+56\\sqrt{10})\\tau+7350-1860\\sqrt{10},\n"
            "\\]\n"
            "and \\(195q_\\tau(6)=1500(75-\\tau)>0\\).  Hence \\(\\tau\\ge39\\) would\n"
            "create a compression eigenvalue above the open WOW endpoint.  Conversely, the\n"
            "number \\(150-2\\tau\\) of edges from the second to the third layer is at most\n"
            "\\(13\\cdot6\\), so \\(\\tau\\ge36\\).  Thus\n"
            "\\(\\tau\\in\\{36,37,38\\}\\), and edge--cycle incidence gives the even\n"
            "high-edge subgraph and the formula for \\(N_5\\).\n"
            "\n"
            "For a two-path \\(u-v-w\\), girth at least five gives\n"
            "\\((A^3)_{uw}=\\alpha_{uvw}\\) and\n"
            "\\((A^4)_{uw}=16+\\beta_{uvw}\\).  The corresponding \\(3\\times3\\) principal\n"
            "minor of the centered positive-semidefinite matrix yields the displayed finite\n"
            "sets for \\(r_{uvw}\\), except for an apparent equality value \\(r=29\\).\n"
            "At equality, the Gram norm of \\(e_u-e_w\\) vanishes, so this vector lies in\n"
            "the kernel of the centered matrix.  On \\(\\one^\\perp\\), that kernel is the\n"
            "adjacency \\(-2\\)-eigenspace; however, the \\(u\\)-coordinate of\n"
            "\\(A(e_u-e_w)\\) is zero because \\(u\\not\\sim w\\), whereas the\n"
            "\\(u\\)-coordinate of \\(-2(e_u-e_w)\\) is \\(-2\\).  This excludes\n"
            "\\(r=29\\).  Summing the local inequalities gives the first pair of\n"
            "\\(N_6\\) bounds; shifted moment and localizing matrices give the second.\n",
        ),
        (
            "puncture-proof-architecture",
            "Partition by the deleted neighbourhoods and the residual vertices.  The Moore\n"
            "incidence identities decompose the distance matrix orthogonally into a\n"
            "constant quotient, zero-sum incidence modules, and a residual kernel carrying\n"
            "the Moore quadratic relation.  The dimensions are respectively\n"
            "\\[\n"
            " 2+2(k-1)+k(k-2)=k^2\n"
            "\\]\n"
            "and\n"
            "\\[\n"
            " 3+2(2k-4)+(k-2)^2=k^2-1.\n"
            "\\]\n"
            "Exact quotient normalization, trace-to-multiplicity equations, replacement\n"
            "paths, and least-root comparisons are independently checked by\n"
            "\\codefile{scripts/verify_proof_audit_05_small_moore_punctures.py}.",
            "For one deleted vertex, put \\(A=N(v)\\), \\(B=\\Gamma_2(v)\\), let \\(C\\) be\n"
            "the \\(A\\)-by-\\(B\\) incidence matrix, and let \\(B_0\\) be the adjacency\n"
            "matrix on \\(B\\).  Recomputed distances give\n"
            "\\[\n"
            " D(H)=\\begin{pmatrix}3(J-I)&2J-C\\\\2J-C^{\\mathsf T}&2(J-I)-B_0\\end{pmatrix}.\n"
            "\\]\n"
            "The identities \\(CC^{\\mathsf T}=(k-1)I\\), \\(CB_0=J-C\\), and the\n"
            "bottom-right block of the Moore relation yield the orthogonal decomposition\n"
            "\\[\n"
            " \\mathbb R^{V(H)}=W_{\\mathrm{const}}\\perp W_{\\mathrm{inc}}\\perp\\ker C,\n"
            " \\qquad 2+2(k-1)+k(k-2)=k^2.\n"
            "\\]\n"
            "On each zero-sum incidence module the action matrix is\n"
            "\\(\\bigl(\\begin{smallmatrix}-3&-(k-1)\\\\-1&-1\\end{smallmatrix}\\bigr)\\),\n"
            "giving \\(-2\\pm\\sqrt{k}\\); on \\(\\ker C\\),\n"
            "\\(B_0^2+B_0-(k-1)I=0\\) and \\(D=-2I-B_0\\).  The normalized constant\n"
            "quotient supplies \\(\\rho_\\pm\\).\n"
            "\n"
            "For an adjacent deleted pair, the cells\n"
            "\\(A=N(u)\\setminus\\{v\\}\\), \\(B=N(v)\\setminus\\{u\\}\\), and the residual\n"
            "cell give an antisymmetric constant line, a symmetric two-dimensional\n"
            "quotient, two zero-sum incidence modules, and a residual kernel.  Their\n"
            "dimensions add to\n"
            "\\[\n"
            " 3+2(2k-4)+(k-2)^2=k^2-1.\n"
            "\\]\n"
            "The same incidence action gives \\(-2\\pm\\sqrt{k}\\), the residual Moore\n"
            "relation gives the \\(a_\\pm\\) factors, and positive definiteness of the two\n"
            "shifted constant quotients shows that no quotient or residual root lies below\n"
            "\\(-2-\\sqrt{k}\\).  Exact quotient normalization, trace-to-multiplicity\n"
            "equations, replacement paths, and all least-root comparisons are independently\n"
            "checked by \\codefile{scripts/verify_proof_audit_05_small_moore_punctures.py}.",
        ),
        (
            "nonadjacent-proof",
            "The deleted vertices have a unique common neighbour \\(w\\).  The surviving graph\n"
            "has an equitable five-cell geometry\n"
            "\\[\n"
            " \\{w\\}\\sqcup A\\sqcup B\\sqcup C\\sqcup Z,\n"
            "\\]\n"
            "with a perfect matching between \\(A\\) and \\(B\\).  Every pair whose unique\n"
            "length-two path was deleted has an explicit surviving length-three path.  The\n"
            "distance space decomposes into the constant quotient, matched symmetric and\n"
            "antisymmetric modules, the common-neighbour module, and the residual Moore\n"
            "kernel.  Their dimensions add to\n"
            "\\[\n"
            " 5+4(k-2)+2(k-3)+(k-2)(k-4)=k^2-1.\n"
            "\\]\n"
            "The corresponding factors are exactly those displayed.  The direct sum,\n"
            "injectivity, orthogonality, trace, multiplicities, and all recomputed distances\n"
            "are independently checked by\n"
            "\\codefile{scripts/verify_proof_audit_03_nonadjacent_puncture.py}.  Strictness\n"
            "for \\(k\\ge6\\) follows from Proposition~\\ref{prop:deletion-stability} below.",
            "The deleted vertices have a unique common neighbour \\(w\\).  With\n"
            "\\(A=N(u)\\setminus\\{w\\}\\), \\(B=N(v)\\setminus\\{w\\}\\),\n"
            "\\(C=N(w)\\setminus\\{u,v\\}\\), and residual cell \\(Z\\), the surviving graph\n"
            "has an equitable five-cell geometry and a perfect matching between \\(A\\) and\n"
            "\\(B\\).  Explicit length-three paths show that every pair whose unique\n"
            "length-two path was deleted has new distance exactly three.  The five-cell\n"
            "distance quotient has characteristic polynomial \\((x-k+3)R_k(x)\\).\n"
            "\n"
            "Let \\(R_A,R_B,R_C\\) be the incidence matrices from the three nonconstant\n"
            "cells to \\(Z\\), and let \\(T\\) be the adjacency matrix on \\(Z\\).  The Moore\n"
            "identity splits the remaining space into matched symmetric and antisymmetric\n"
            "modules, a common-neighbour module, and\n"
            "\\(K=\\ker R_A\\cap\\ker R_B\\cap\\ker R_C\\).  The first three modules give\n"
            "the two displayed quadratic factors and \\(k-3\\) copies of each Moore linear\n"
            "factor.  On \\(K\\),\n"
            "\\[\n"
            " T^2+T-(k-1)I=0,\n"
            " \\qquad D=-2I-T.\n"
            "\\]\n"
            "The constant direction of \\(Z\\) has \\(T\\)-eigenvalue \\(k-3\\), the\n"
            "symmetric, antisymmetric, and common-neighbour images have eigenvalues\n"
            "\\(-2,0,-1\\) with dimensions \\(k-2,k-2,k-3\\).  Since \\(T\\) has zero\n"
            "diagonal, its total trace is zero, and therefore\n"
            "\\(\\tr(T|_K)=2(k-2)\\).  Dimension and trace now give the residual\n"
            "multiplicities; after adding the common-neighbour copies they are precisely\n"
            "\\(M_-\\) and \\(M_+\\).  The full dimension count is\n"
            "\\[\n"
            " 5+4(k-2)+2(k-3)+(k-2)(k-4)=k^2-1.\n"
            "\\]\n"
            "\n"
            "For strictness, the distance-increase matrix is the adjacency matrix of two\n"
            "copies of \\(K_k\\) meeting in \\(w\\), and hence has least eigenvalue\n"
            "\\[\n"
            " \\lambda_{\\min}(E_S)=\\frac{k-2-\\sqrt{k^2+4k-4}}2.\n"
            "\\]\n"
            "Proposition~\\ref{prop:deletion-stability} gives a positive lower bound for\n"
            "the child score for every \\(k\\ge6\\).  After the sign-preserving squarings,\n"
            "the remaining condition is \\(P(k)>0\\), where\n"
            "\\[\n"
            " P(k)=4k^8-39k^7+95k^6+9k^5-173k^4-36k^3+116k^2+80k+16.\n"
            "\\]\n"
            "Writing \\(k=m+6\\) makes every coefficient positive.  The direct sum,\n"
            "injectivity, orthogonality, all recomputed distances, and the polynomial sign\n"
            "are independently checked by\n"
            "\\codefile{scripts/verify_proof_audit_03_nonadjacent_puncture.py} and\n"
            "\\codefile{scripts/verify_research_extensions_exact.py}.",
        ),
        (
            "prime-field-omega",
            "A nonzero character block has form\n"
            "\\[\n"
            " \\begin{pmatrix}aI&M\\\\M^*&bI\\end{pmatrix},\n"
            " \\qquad M_{ik}=\\omega^{ik},\n"
            "\\]\n",
            "Let \\(\\omega=e^{2\\pi\\mathrm i/q}\\).  On the nonzero character\n"
            "\\(t=1\\), the adjacency block has form\n"
            "\\[\n"
            " \\begin{pmatrix}aI&M\\\\M^*&bI\\end{pmatrix},\n"
            " \\qquad M_{ik}=\\omega^{ik},\n"
            "\\]\n",
        ),
        (
            "matching-theorem-structure",
            "The \\(120\\) labelled graphs form exactly two isomorphism classes.  The \\(20\\)\n"
            "affine permutations have\n",
            "Each deletion produces a connected simple \\(6\\)-regular graph of order\n"
            "\\(50\\), girth five, and diameter four.  The \\(120\\) labelled graphs form\n"
            "exactly two isomorphism classes.  The \\(20\\) affine permutations have\n",
        ),
        (
            "matching-proof",
            "Explicit type-preserving and type-swapping coordinate automorphisms generate\n"
            "orbits of sizes \\(20\\) and \\(100\\).  The representatives have different\n"
            "adjacency characteristic polynomials, so the orbits are distinct isomorphism\n"
            "classes.  Exact distance characteristic polynomials and Sturm separators give\n"
            "the stated least roots.  All \\(120\\) matchings, \\(400\\) coordinate maps,\n"
            "\\(48000\\) matching images, orbit coverage, and root certificates are checked\n",
            "Every \\(P_{i,j}\\) occurs once in \\(\\mathcal M_\\pi\\); for a fixed\n"
            "\\(Q_{k,\\ell}\\), the unique incident matching edge is obtained from\n"
            "\\(i=\\pi^{-1}(k)\\) and \\(j=\\ell-ik\\).  Thus \\(\\mathcal M_\\pi\\) is a\n"
            "perfect matching, and its deletion leaves a simple \\(6\\)-regular graph.\n"
            "Deleting edges cannot create a short cycle, while the same-layer pentagons\n"
            "remain; exact breadth-first search gives connectedness and diameter four.\n"
            "\n"
            "Explicit type-preserving and type-swapping coordinate automorphisms generate\n"
            "orbits of sizes \\(20\\) and \\(100\\).  The representatives have different\n"
            "adjacency characteristic polynomials, so the orbits are distinct isomorphism\n"
            "classes.  Exact distance characteristic polynomials and Sturm separators give\n"
            "the stated least roots.  All \\(120\\) matchings, \\(400\\) coordinate maps,\n"
            "\\(48000\\) matching images, orbit coverage, graph hypotheses, and root\n"
            "certificates are checked\n",
        ),
        (
            "verification-table",
            "\\[\n"
            "\\begin{array}{p{0.43\\textwidth}p{0.49\\textwidth}}\n"
            "\\toprule\n"
            "Result&Exact verifier\\\\\n"
            "\\midrule\n",
            "\\begin{center}\n"
            "\\begin{tabular}{p{0.39\\textwidth}p{0.53\\textwidth}}\n"
            "\\toprule\n"
            "Result&Exact verifier\\\\\n"
            "\\midrule\n",
        ),
        (
            "verification-table-end",
            "Matching deletion classes&\\codefile{scripts/verify_proof_audit_07_layer_matchings.py}\\\\\n"
            "\\bottomrule\n"
            "\\end{array}\n"
            "\\]\n",
            "Matching deletion classes&\\codefile{scripts/verify_proof_audit_07_layer_matchings.py}\\\\\n"
            "\\bottomrule\n"
            "\\end{tabular}\n"
            "\\end{center}\n",
        ),
        (
            "lean-scope",
            "The non-\\(50\\) formal statements are deliberately described as finite spectral\n"
            "certificates rather than as a single Mathlib theorem bundling every graph-\n"
            "theoretic phrase.\n",
            "The non-\\(50\\) formal statements are deliberately described as finite spectral\n"
            "certificates rather than as a single Mathlib theorem bundling every\n"
            "graph-theoretic phrase.  The LP ceiling, optimizer rigidity, punctured-Moore\n"
            "spectra, and deletion-robustness theorems remain conventional analytic proofs\n"
            "with exact executable audits; they are not included in the Lean claim above.\n",
        ),
        (
            "literature-matrix-link",
            "\\codefile{research-notes/LITERATURE_AUDIT_EXTENSIONS.md} and the associated\n"
            "source matrix, did not locate direct prior statements",
            "\\codefile{research-notes/LITERATURE_AUDIT_EXTENSIONS.md} and\n"
            "\\codefile{research-notes/NEXT_DIRECTION_SOURCE_MATRIX.json}, did not locate\n"
            "direct prior statements",
        ),
    ]

    for label, old, new in replacements:
        text = replace_once(text, old, new, label)
    return text


BIB_ENTRIES = r'''

@misc{Backelin2015,
  author        = {Backelin, J{"o}rgen},
  title         = {Sizes of the Extremal Girth 5 Graphs of Orders from 40 to 49},
  year          = {2015},
  eprint        = {1511.08128},
  archiveprefix = {arXiv},
  primaryclass  = {math.CO}
}

@article{Fiol2016,
  author  = {Fiol, Miquel {\`A}ngel},
  title   = {Quotient-Polynomial Graphs},
  journal = {Linear Algebra and its Applications},
  volume  = {488},
  pages   = {363--376},
  year    = {2016},
  doi     = {10.1016/j.laa.2015.09.053}
}

@article{Nozaki2015,
  author  = {Nozaki, Hiroshi},
  title   = {Linear Programming Bounds for Regular Graphs},
  journal = {Graphs and Combinatorics},
  volume  = {31},
  number  = {6},
  pages   = {1973--1984},
  year    = {2015},
  doi     = {10.1007/s00373-015-1613-7}
}

@article{CioabaEtAl2016,
  author  = {Cioab
, Sebastian M. and Koolen, Jack H. and Nozaki, Hiroshi and Vermette, Jason R.},
  title   = {Maximizing the Order of a Regular Graph of Given Valency and Second Eigenvalue},
  journal = {SIAM Journal on Discrete Mathematics},
  volume  = {30},
  number  = {3},
  pages   = {1509--1525},
  year    = {2016},
  doi     = {10.1137/15M1030935}
}

@article{Jorgensen2005,
  author  = {J{\o}rgensen, Leif K.},
  title   = {Girth 5 Graphs from Relative Difference Sets},
  journal = {Discrete Mathematics},
  volume  = {293},
  number  = {1--3},
  pages   = {177--184},
  year    = {2005},
  doi     = {10.1016/j.disc.2004.08.029}
}

@article{AbreuEtAl2008,
  author  = {Abreu, Marien and Funk, Martin and Labbate, Domenico and Napolitano, Vito},
  title   = {A Family of Regular Graphs of Girth 5},
  journal = {Discrete Mathematics},
  volume  = {308},
  number  = {10},
  pages   = {1810--1815},
  year    = {2008},
  doi     = {10.1016/j.disc.2007.04.031}
}

@article{DalfoVanDamFiol2012,
  author  = {Dalf{\'o}, Cristina and van Dam, Edwin R. and Fiol, Miquel {\`A}ngel},
  title   = {On Perturbations of Almost Distance-Regular Graphs},
  journal = {Linear Algebra and its Applications},
  volume  = {435},
  number  = {10},
  pages   = {2626--2638},
  year    = {2011},
  doi     = {10.1016/j.laa.2011.05.004}
}

@misc{Biggs2010,
  author        = {Biggs, Norman},
  title         = {The Second Subconstituent of Some Strongly Regular Graphs},
  year          = {2010},
  eprint        = {1003.0175},
  archiveprefix = {arXiv},
  primaryclass  = {math.CO}
}
'''


def revise_bib(text: str) -> str:
    for key in (
        "Backelin2015",
        "Fiol2016",
        "Nozaki2015",
        "CioabaEtAl2016",
        "Jorgensen2005",
        "AbreuEtAl2008",
        "DalfoVanDamFiol2012",
        "Biggs2010",
    ):
        if re.search(r"@[A-Za-z]+\{" + re.escape(key) + r",", text):
            raise AssertionError(f"bibliography already contains {key}")
    return text.rstrip() + BIB_ENTRIES + "\n"


def citation_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        keys.update(item.strip() for item in match.group(1).split(","))
    return keys


def bibliography_keys(bib: str) -> set[str]:
    return set(re.findall(r"@[A-Za-z]+\{([^,]+),", bib))


def verify_paths(tex: str) -> None:
    for command in ("codefile", "datafile"):
        for path in re.findall(r"\\" + command + r"\{([^}]+)\}", tex):
            if not (ROOT / path).is_file():
                raise AssertionError(f"missing inline repository path: {path}")


def main() -> None:
    tex = revise_tex(TEX.read_text(encoding="utf-8"))
    bib = revise_bib(BIB.read_text(encoding="utf-8"))

    missing = citation_keys(tex) - bibliography_keys(bib)
    if missing:
        raise AssertionError(f"missing bibliography keys: {sorted(missing)}")
    verify_paths(tex)

    if any(ord(char) < 32 and char not in "\t\n" for char in tex + bib):
        raise AssertionError("control byte introduced by revision")

    TEX.write_text(tex, encoding="utf-8", newline="\n")
    BIB.write_text(bib, encoding="utf-8", newline="\n")
    print("v2.2 mathematical/prose revision: PASS")
    print(f"citations checked: {len(citation_keys(tex))}")
    print("inline repository paths: PASS")


if __name__ == "__main__":
    main()
