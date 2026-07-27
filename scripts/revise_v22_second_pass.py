#!/usr/bin/env python3
"""Second fail-closed line-by-line revision of the expanded WOW-284 manuscript."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "v22" / "main.tex"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = TEX.read_text(encoding="utf-8")

    replacements: list[tuple[str, str, str]] = [
        (
            "abstract-rhythm",
            "regular strict counterexample has degree at least six and diameter at most\n"
            "four; diameter-four counterexamples are excluded through degree nine.  We determine the\n",
            "regular strict counterexample has degree at least six and diameter at most\n"
            "four, and every diameter-four counterexample has degree at least ten.  We\n"
            "determine the\n",
        ),
        (
            "edge-local-walks",
            "The spectral window gives \\(M\\succeq0\\).  On an edge,\n"
            "\\[\n"
            " (A^3)_{uv}=2k-1,\n"
            " \\qquad (A^4)_{uv}=\\sigma_{uv},\n"
            "\\]\n"
            "so the diagonal and edge entries of \\(M\\) are\n"
            "\\[\n"
            " a=\\frac{C_k}{n}-6(k+2),\n"
            " \\quad\n"
            " b=\\frac{C_k}{n}-(4k+14)-\\sigma_{uv}.\n"
            "\\]\n"
            "The \\(2\\times2\\) principal minor gives \\(-a\\le b\\le a\\), yielding the first\n"
            "two bounds with their stated directions.\n"
            "\n"
            "For the last bound, radius-two balls have size \\(k^2+1\\), and\n"
            "\\[\n"
            " |B_2(u)\\cap B_2(v)|=2k+\\sigma_{uv}.\n"
            "\\]\n"
            "The vertices at distance two from both endpoints are in bijection with the\n"
            "\\(5\\)-cycles through \\(uv\\).  Inclusion--exclusion gives the result.  The walk\n"
            "classification, sign directions, and radius-two bijection are independently\n"
            "checked by \\codefile{scripts/verify_proof_audit_01_edge_local.py}.",
            "The spectral window gives \\(M\\succeq0\\).  For an edge \\(uv\\),\n"
            "\\[\n"
            " (A^3)_{uv}=\\sum_{z\\sim v}(A^2)_{uz}=k+(k-1)=2k-1.\n"
            "\\]\n"
            "Here \\(z=u\\) contributes \\(k\\), while every other neighbour of \\(v\\) is at\n"
            "distance two from \\(u\\) and has a unique length-two path from \\(u\\).\n"
            "Moreover,\n"
            "\\[\n"
            " (A^4)_{uv}=\\sum_z(A^2)_{uz}(A^2)_{zv}=\\sigma_{uv}.\n"
            "\\]\n"
            "Indeed, the nonzero summands away from the diagonal are precisely the vertices\n"
            "at distance two from both \\(u\\) and \\(v\\).  Their two unique length-two\n"
            "paths, together with \\(uv\\), form a five-cycle, and each five-cycle through\n"
            "\\(uv\\) yields one such vertex.  Since\n"
            "\\(C_k=(k+2)^2(k^2+3)\\), the diagonal and edge entries of \\(M\\) are\n"
            "\\[\n"
            " a=\\frac{C_k}{n}-6(k+2),\n"
            " \\qquad\n"
            " b=\\frac{C_k}{n}-(4k+14)-\\sigma_{uv}.\n"
            "\\]\n"
            "The principal submatrix on \\(\\{u,v\\}\\) is\n"
            "\\(\\bigl(\\begin{smallmatrix}a&b\\\\b&a\\end{smallmatrix}\\bigr)\\), so\n"
            "\\(a\\ge0\\) and \\(-a\\le b\\le a\\).  The inequality \\(b\\le a\\) gives\n"
            "\\(\\sigma_{uv}\\ge2k-2\\), while \\(b\\ge-a\\) gives the stated upper bound.\n"
            "\n"
            "For the final bound, every radius-two ball has size \\(k^2+1\\).  The set\n"
            "\\[\n"
            " \\{u,v\\}\\cup(N(u)\\setminus\\{v\\})\\cup(N(v)\\setminus\\{u\\})\n"
            "\\]\n"
            "contains \\(2k\\) vertices and lies in \\(B_2(u)\\cap B_2(v)\\).  Every further\n"
            "intersection vertex is at distance two from both endpoints and is therefore in\n"
            "the preceding five-cycle bijection.  Hence\n"
            "\\[\n"
            " |B_2(u)\\cap B_2(v)|=2k+\\sigma_{uv}.\n"
            "\\]\n"
            "Inclusion--exclusion and \\(n=k^2+1+c\\) now give\n"
            "\\(\\sigma_{uv}\\ge(k-1)^2-c\\).  The complete walk classification, sign\n"
            "directions, and radius-two bijection are independently checked by\n"
            "\\codefile{scripts/verify_proof_audit_01_edge_local.py}.",
        ),
        (
            "low-degree-windows",
            "Apply Theorems~\\ref{thm:diameter-four} and~\\ref{thm:lp-ceiling}, then use the\n"
            "parity of \\(kn\\).  At \\(k=8,n=111\\), the edge-local bounds force every edge\n"
            "into exactly \\(14\\) five-cycles, but\n"
            "\\[\n"
            " 5N_5=14\\cdot444=6216\n"
            "\\]\n"
            "is impossible.  Exact integer arithmetic is checked by\n"
            "\\codefile{scripts/verify_low_degree_windows.py}.",
            "Theorem~\\ref{thm:diameter-four} removes diameter four for these degrees.  At\n"
            "\\(k=7\\), the diameter-two case is the order-​\\(50\\) Hoffman--Singleton graph,\n"
            "whereas Theorem~\\ref{thm:lp-ceiling} gives \\(n<78\\) in diameter three;\n"
            "the handshake lemma makes \\(n\\) even, so \\(n\\le76\\).  At \\(k=8\\) and\n"
            "\\(k=9\\), the Moore multiplicities are nonintegral, so diameter two is\n"
            "impossible.  The LP ceiling gives \\(n\\le111\\) for \\(k=8\\) and\n"
            "\\(n\\le153\\) for \\(k=9\\); parity improves the latter to \\(152\\).  Finally,\n"
            "at \\(k=8,n=111\\), the edge-local bounds force every edge into exactly\n"
            "\\(14\\) five-cycles, but\n"
            "\\[\n"
            " 5N_5=14\\cdot444=6216\n"
            "\\]\n"
            "is impossible.  Exact integer arithmetic is checked by\n"
            "\\codefile{scripts/verify_low_degree_windows.py}.",
        ),
        (
            "order50-layer-signs",
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
            "high-edge subgraph and the formula for \\(N_5\\).",
            "The diameter reduction used in Theorem~\\ref{thm:degree-six-fifty} applies\n"
            "verbatim: diameter at least four gives a Rayleigh quotient at most \\(-8\\), and\n"
            "diameter two gives the trace contradiction from\n"
            "\\((x-6)(x^2+x-5)^{18}\\).  Hence the diameter is three.  Around a fixed vertex\n"
            "the distance layers have sizes \\(1,6,30,13\\).  If \\(\\tau\\) is the number of\n"
            "five-cycles through the centre, the average row quotient is similar to the\n"
            "symmetric compression on normalized layer indicators.  Its nonprincipal factor\n"
            "\\(q_\\tau\\) satisfies\n"
            "\\[\n"
            " 195q_\\tau(-1+\\sqrt{10})\n"
            " =(-215+56\\sqrt{10})\\tau+7350-1860\\sqrt{10}.\n"
            "\\]\n"
            "The coefficient of \\(\\tau\\) is negative because\n"
            "\\(56^2\\cdot10<215^2\\), and at \\(\\tau=39\\) the right-hand side is\n"
            "\\(9(-115+36\\sqrt{10})<0\\).  Also\n"
            "\\[\n"
            " 195q_\\tau(6)=1500(75-\\tau)>0.\n"
            "\\]\n"
            "The last inequality is strict: the third layer is nonempty and connected to the\n"
            "second, while their edge count is \\(150-2\\tau\\).  Thus \\(\\tau\\ge39\\)\n"
            "would place a nonprincipal compression eigenvalue in\n"
            "\\((-1+\\sqrt{10},6)\\), contradicting interlacing and the open WOW window.\n"
            "Conversely, \\(150-2\\tau\\le13\\cdot6\\), so \\(\\tau\\ge36\\).  Hence\n"
            "\\(\\tau\\in\\{36,37,38\\}\\).  Finally,\n"
            "\\(\\sum_{e\\ni v}\\sigma_e=2\\tau(v)\\), so the high-edge degree is\n"
            "\\(2\\tau(v)-72\\); counting edge--five-cycle incidences gives\n"
            "\\(5N_5=12\\cdot150+m\\).",
        ),
        (
            "order50-kernel",
            "At equality, the Gram norm of \\(e_u-e_w\\) vanishes, so this vector lies in\n"
            "the kernel of the centered matrix.  On \\(\\one^\\perp\\), that kernel is the\n"
            "adjacency \\(-2\\)-eigenspace; however, the \\(u\\)-coordinate of\n"
            "\\(A(e_u-e_w)\\) is zero because \\(u\\not\\sim w\\), whereas the\n"
            "\\(u\\)-coordinate of \\(-2(e_u-e_w)\\) is \\(-2\\).  This excludes\n",
            "At equality, the Gram norm of \\(e_u-e_w\\) vanishes, so this vector lies in\n"
            "the kernel of the centered matrix.  On \\(\\one^\\perp\\), that matrix is\n"
            "\\(-f_6(A)\\).  The strict shifted window excludes the two endpoint zeros of\n"
            "\\(f_6\\), leaving only its double zero at \\(-2\\); hence the kernel there is\n"
            "exactly the adjacency \\(-2\\)-eigenspace.  However, the \\(u\\)-coordinate of\n"
            "\\(A(e_u-e_w)\\) is zero because \\(u\\not\\sim w\\), whereas the\n"
            "\\(u\\)-coordinate of \\(-2(e_u-e_w)\\) is \\(-2\\).  This excludes\n",
        ),
        (
            "puncture-architecture",
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
            "For one deleted vertex, put \\(A=N(v)\\), \\(B=\\Gamma_2(v)\\), let \\(C\\) be\n"
            "the \\(A\\)-by-\\(B\\) incidence matrix, and let \\(B_0\\) be the adjacency\n"
            "matrix on \\(B\\).  Only pairs inside \\(A\\) lose their unique length-two path.\n"
            "For distinct \\(a,a'\\in A\\), choose a neighbour \\(b\\in B\\) of \\(a\\).  The\n"
            "unique common neighbour \\(c\\) of \\(b,a'\\) lies in \\(B\\), giving the\n"
            "surviving path \\(a-b-c-a'\\).  Hence\n"
            "\\[\n"
            " D(H)=\\begin{pmatrix}3(J-I)&2J-C\\\\2J-C^{\\mathsf T}&2(J-I)-B_0\\end{pmatrix}.\n"
            "\\]\n"
            "The normalized constant quotient is\n"
            "\\[\n"
            " Q_1=\\begin{pmatrix}\n"
            " 3(k-1)&(2k-1)\\sqrt{k-1}\\\\\n"
            " (2k-1)\\sqrt{k-1}&2k^2-3k-1\n"
            " \\end{pmatrix},\n"
            "\\]\n"
            "whose eigenvalues are \\(\\rho_\\pm\\).  The identities\n"
            "\\(CC^{\\mathsf T}=(k-1)I\\), \\(CB_0=J-C\\), and the bottom-right block of the\n"
            "Moore relation yield\n"
            "\\[\n"
            " \\mathbb R^{V(H)}=W_{\\mathrm{const}}\\perp W_{\\mathrm{inc}}\\perp\\ker C,\n"
            " \\qquad 2+2(k-1)+k(k-2)=k^2.\n"
            "\\]\n"
            "On each zero-sum incidence module the action matrix is\n"
            "\\(\\bigl(\\begin{smallmatrix}-3&-(k-1)\\\\-1&-1\\end{smallmatrix}\\bigr)\\),\n"
            "giving \\(-2\\pm\\sqrt{k}\\).  On \\(\\ker C\\),\n"
            "\\(B_0^2+B_0-(k-1)I=0\\), \\(D=-2I-B_0\\), and the trace of \\(B_0\\) is\n"
            "zero after removing the constant and incidence images; dimension and trace give\n"
            "\\(m_\\pm\\).\n"
            "\n"
            "For an adjacent deleted pair, put\n"
            "\\(A=N(u)\\setminus\\{v\\}\\), \\(B=N(v)\\setminus\\{u\\}\\), and let \\(C\\) be\n"
            "the residual cell.  Only pairs inside \\(A\\) or inside \\(B\\) lose a\n"
            "length-two path; the same unique-common-neighbour construction supplies a\n"
            "surviving length-three path.  The antisymmetric constant line has eigenvalue\n"
            "\\(k-4\\), and the normalized symmetric quotient is\n"
            "\\[\n"
            " Q_2=\\begin{pmatrix}\n"
            " 5k-8&\\sqrt{(k-1)(2k-3)(4k-6)}\\\\\n"
            " \\sqrt{(k-1)(2k-3)(4k-6)}&2k^2-5k+2\n"
            " \\end{pmatrix},\n"
            "\\]\n"
            "with eigenvalues \\(\\sigma_\\pm\\).  Two zero-sum incidence modules and a\n"
            "residual kernel complete the decomposition, with\n"
            "\\[\n"
            " 3+2(2k-4)+(k-2)^2=k^2-1.\n"
            "\\]\n"
            "The residual adjacency trace is \\(k-2\\), giving \\(a_\\pm\\).  The residual\n"
            "negative root is greater than \\(-2-\\sqrt{k}\\), and the same is true of the\n"
            "smaller constant-quotient roots because\n"
            "\\[\n"
            " \\det(Q_1+(2+\\sqrt{k})I)\n"
            " =k(2k^2+2k^{3/2}-3k+2)>0,\n"
            "\\]\n"
            "\\[\n"
            " \\det(Q_2+(2+\\sqrt{k})I)\n"
            " =(\\sqrt{k}-1)(\\sqrt{k}+1)\n"
            " (2k^2+2k^{3/2}-3k+2\\sqrt{k}+6)>0.\n"
            "\\]\n"
            "Exact quotient normalization, trace-to-multiplicity equations, replacement\n"
            "paths, and all least-root comparisons are independently checked by\n"
            "\\codefile{scripts/verify_proof_audit_05_small_moore_punctures.py}.",
        ),
        (
            "nonadjacent-polynomial-expansion",
            "Writing \\(k=m+6\\) makes every coefficient positive.  The direct sum,\n",
            "Writing \\(k=m+6\\) gives\n"
            "\\[\n"
            "\\begin{aligned}\n"
            " P(m+6)={}&4m^8+153m^7+2489m^6+22329m^5\\\\\n"
            " &+119437m^4+382236m^3+685268m^2\\\\\n"
            " &+559616m+75952>0.\n"
            "\\end{aligned}\n"
            "\\]\n"
            "The direct sum,\n",
        ),
        (
            "small-puncture-paths",
            "If the unique common neighbour of two surviving nonadjacent vertices is\n"
            "deleted, the Moore geometry constructs \\(k-1\\) internally vertex-disjoint\n"
            "length-three replacement paths.  Since at most \\(s-1\\le k-2\\) further\n"
            "vertices are deleted, one survives.  Thus the distance increases from two to\n"
            "exactly three precisely when a deleted vertex was the unique common neighbour,\n"
            "which proves the matrix formula.\n"
            "\n"
            "For \\(x\\in V(H)\\), let \\(t_x=|N_M(x)\\cap S|\\).  Then\n"
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x\n"
            "\\]\n",
            "Let \\(x,y\\in V(H)\\) be nonadjacent in \\(M\\), and suppose their unique common\n"
            "neighbour \\(z\\) lies in \\(S\\).  For every\n"
            "\\(a\\in N_M(x)\\setminus\\{z\\}\\), the vertices \\(a,y\\) are nonadjacent and\n"
            "have a unique common neighbour \\(b_a\\).  Thus\n"
            "\\[\n"
            " x-a-b_a-y\n"
            "\\]\n"
            "is a length-three path.  These \\(k-1\\) paths are internally vertex-disjoint:\n"
            "a shared vertex \\(b_a=b_{a'}\\) would give a four-cycle, while\n"
            "\\(b_a=a'\\) would give a triangle through \\(x\\).  Besides \\(z\\), at most\n"
            "\\(s-1\\le k-2\\) vertices are deleted, so one path survives.  Hence a destroyed\n"
            "length-two path becomes distance exactly three, which proves the matrix formula.\n"
            "\n"
            "For \\(x\\in V(H)\\), let \\(t_x=|N_M(x)\\cap S|\\).  A deleted neighbour of\n"
            "\\(x\\) is adjacent to no surviving neighbour of \\(x\\), by triangle-freeness;\n"
            "each other deleted vertex has at most one common neighbour with \\(x\\).  Thus\n"
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x.\n"
            "\\]\n",
        ),
        (
            "jorgensen-typography",
            "J\\o rgensen's \\(9\\)-regular order-\\(96\\) graph of girth five is an exact equality\n",
            "J{\\o}rgensen's \\(9\\)-regular order-\\(96\\) graph of girth five is an exact equality\n",
        ),
        (
            "jorgensen-typography-2",
            "with multiplicity eight.  The construction is due to J\\o rgensen\n",
            "with multiplicity eight.  The construction is due to J{\\o}rgensen\n",
        ),
        (
            "prime-field-proof",
            "The zero Fourier block has eigenvalues \\(m+2\\), \\(2-m\\), and \\(2\\) with\n"
            "multiplicity \\(2m-2\\); the shifted WOW window leaves only\n"
            "\\(m\\in\\{4,5,6\\}\\).  Let \\(\\omega=e^{2\\pi\\mathrm i/q}\\).  On the nonzero character\n"
            "\\(t=1\\), the adjacency block has form\n"
            "\\[\n"
            " \\begin{pmatrix}aI&M\\\\M^*&bI\\end{pmatrix},\n"
            " \\qquad M_{ik}=\\omega^{ik},\n"
            "\\]\n"
            "and \\(\\|M\\|_F^2=m^2\\), so its largest singular value is at least\n"
            "\\(\\sqrt m\\).  The block therefore has a nonprincipal eigenvalue at least\n"
            "\\[\n"
            " \\sqrt m+\\cos(\\pi/7)-\\frac12,\n"
            "\\]\n"
            "which lies above \\(-1+\\sqrt{2m+2}\\) for \\(m=4,5,6\\).  The common-neighbour\n",
            "The zero Fourier block has eigenvalues \\(m+2\\), \\(2-m\\), and \\(2\\) with\n"
            "multiplicity \\(2m-2\\); the shifted WOW window leaves only\n"
            "\\(m\\in\\{4,5,6\\}\\).  Let \\(\\omega=e^{2\\pi\\mathrm i/q}\\).  On the nonzero\n"
            "character \\(t=1\\), the adjacency block has form\n"
            "\\[\n"
            " \\begin{pmatrix}aI&M\\\\M^*&bI\\end{pmatrix},\n"
            " \\qquad a=2\\cos\\frac{2\\pi}{q},\n"
            " \\quad b=2\\cos\\frac{4\\pi}{q},\n"
            " \\quad M_{ik}=\\omega^{ik}.\n"
            "\\]\n"
            "If \\(\\sigma\\) is a singular value of \\(M\\), the associated two-dimensional\n"
            "invariant subspace carries\n"
            "\\(\\bigl(\\begin{smallmatrix}a&\\sigma\\\\\\sigma&b\\end{smallmatrix}\\bigr)\\).\n"
            "Since \\(\\|M\\|_F^2=m^2\\), one singular value satisfies\n"
            "\\(\\sigma^2\\ge m\\), and the block has a nonprincipal eigenvalue at least\n"
            "\\[\n"
            " \\sqrt m+\\frac{a+b}{2}\n"
            " \\ge \\sqrt m+\\cos(\\pi/7)-\\frac12.\n"
            "\\]\n"
            "Here the last inequality uses\n"
            "\\(2\\cos(2\\pi/7)+2\\cos(4\\pi/7)=2\\cos(\\pi/7)-1\\).\n"
            "Moreover \\(\\cos(\\pi/7)>\\sqrt3/2\\), and the increasing function\n"
            "\\(h(m)=\\sqrt{2m+2}-\\sqrt m\\) satisfies\n"
            "\\[\n"
            " h(m)\\le h(6)=\\sqrt{14}-\\sqrt6\n"
            " <\\frac{27}{20}<\\frac{\\sqrt3+1}{2}.\n"
            "\\]\n"
            "Thus the displayed nonprincipal eigenvalue lies above\n"
            "\\(-1+\\sqrt{2m+2}\\) for \\(m=4,5,6\\).  The common-neighbour\n",
        ),
        (
            "matching-number-format",
            "All \\(120\\) matchings, \\(400\\) coordinate maps,\n"
            "\\(48000\\) matching images, orbit coverage, graph hypotheses, and root\n",
            "All \\(120\\) matchings, \\(400\\) coordinate maps,\n"
            "\\(48{,}000\\) matching images, orbit coverage, graph hypotheses, and root\n",
        ),
    ]

    for label, old, new in replacements:
        text = replace_once(text, old, new, label)

    if "\u200b" in text:
        text = text.replace("\u200b", "")
    if any(ord(char) < 32 and char not in "\t\n" for char in text):
        raise AssertionError("control byte introduced in second pass")

    TEX.write_text(text, encoding="utf-8", newline="\n")
    print("v2.2 second mathematical/prose pass: PASS")


if __name__ == "__main__":
    main()
