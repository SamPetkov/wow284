#!/usr/bin/env python3
"""Third fail-closed proof-completeness pass for the expanded manuscript."""
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
            "abstract-conjecture-verb",
            "WOW-284 predicts that the minimum dual degree",
            "WOW-284 asserts that the minimum dual degree",
        ),
        (
            "pdf-keywords",
            "pdfkeywords={distance spectrum, dual degree, Moore graph, spectral obstruction, deletion stability}",
            "pdfkeywords={distance spectrum, dual degree, Moore graph}",
        ),
        (
            "manuscript-keywords",
            r"\keywords{distance spectrum, dual degree, Moore graph, spectral obstruction, deletion stability}",
            r"\keywords{distance spectrum, dual degree, Moore graph}",
        ),
        (
            "abstract-formal-verification-scope",
            "All theorem-level computations use exact arithmetic; independent Python\n"
            "certificates are cited inline, and the explicit finite counterexamples have\n"
            "Lean 4.31 kernel-checked certificates.",
            "All theorem-level computations use exact arithmetic, with independent Python\n"
            "certificates cited inline.  Lean 4.31 kernel-checks the complete graph-level\n"
            "proof for the 50-vertex counterexample, finite spectral certificates for the\n"
            "constructions of orders \\(38,39,40,42\\), and, as a separate analytic theorem,\n"
            "the exact one-variable LP optimum and coefficient-level optimizer rigidity for\n"
            "every integer \\(k\\ge4\\).",
        ),
        (
            "forward-dependency",
            "\\begin{proof}\n"
            "Let the degree be \\(k\\).  Lemma~\\ref{lem:diam-rayleigh} and strictness give\n"
            "\\(\\diam(G)<k\\).",
            "\\begin{proof}\n"
            "We use the LP ceiling proved independently in\n"
            "Theorem~\\ref{thm:lp-ceiling}; that theorem does not depend on the present\n"
            "degree reduction.  Let the degree be \\(k\\).\n"
            "Lemma~\\ref{lem:diam-rayleigh} and strictness give \\(\\diam(G)<k\\).",
        ),
        (
            "second-subconstituent-diameter",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  The remaining vertices sharing\n"
            "the unique neighbour of a chosen vertex are at distance three, so\n"
            "Theorem~\\ref{thm:diameter-three-score} applies.",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  It remains to identify the\n"
            "diameter of \\(X\\).  If the unique common neighbour in \\(M\\) of two\n"
            "nonadjacent vertices \\(x,y\\in X\\) lies in \\(X\\), their distance in \\(X\\)\n"
            "is two.  Otherwise it is their common parent in \\(N(v)\\).  Choose\n"
            "\\(b\\in N_X(x)\\).  Then \\(b\\not\\sim y\\), and the unique common neighbour\n"
            "\\(c\\) of \\(b,y\\) belongs to \\(X\\): it cannot be \\(v\\), and it cannot\n"
            "lie in \\(N(v)\\), since \\(b\\) and \\(y\\) have different parents there.\n"
            "Thus \\(x-b-c-y\\) is a path in \\(X\\).  Pairs with a common parent have no\n"
            "length-two path in \\(X\\), so \\(X\\) has diameter three and\n"
            "Theorem~\\ref{thm:diameter-three-score} applies.",
        ),
        (
            "one-puncture-path-location",
            "For distinct \\(a,a'\\in A\\), choose a neighbour \\(b\\in B\\) of \\(a\\).  The\n"
            "unique common neighbour \\(c\\) of \\(b,a'\\) lies in \\(B\\), giving the\n"
            "surviving path \\(a-b-c-a'\\).",
            "For distinct \\(a,a'\\in A\\), choose a neighbour \\(b\\in B\\) of \\(a\\).  The\n"
            "vertices \\(b,a'\\) are nonadjacent, and their unique common neighbour \\(c\\)\n"
            "lies in \\(B\\): it is not \\(v\\), since \\(b\\not\\sim v\\), and it is not in\n"
            "\\(A\\), since an edge inside \\(A\\) would form a triangle through \\(v\\).\n"
            "Hence \\(a-b-c-a'\\) is a surviving path.",
        ),
        (
            "edge-puncture-path-location",
            "Only pairs inside \\(A\\) or inside \\(B\\) lose a\n"
            "length-two path; the same unique-common-neighbour construction supplies a\n"
            "surviving length-three path.",
            "Only pairs inside \\(A\\) or inside \\(B\\) lose a length-two path.  For\n"
            "distinct \\(a,a'\\in A\\), choose a residual neighbour \\(c\\) of \\(a\\).  The\n"
            "vertices \\(c,a'\\) are nonadjacent, and their unique common neighbour is also\n"
            "residual: it cannot be one of the deleted endpoints, cannot lie in \\(A\\) by\n"
            "triangle-freeness, and cannot lie in \\(B\\) because no edge joins \\(A\\) to\n"
            "\\(B\\).  This gives a surviving length-three path; the argument for \\(B\\) is\n"
            "symmetric.",
        ),
        (
            "nonadjacent-score-bound",
            "Proposition~\\ref{prop:deletion-stability} gives a positive lower bound for\n"
            "the child score for every \\(k\\ge6\\).  After the sign-preserving squarings,\n"
            "the remaining condition is \\(P(k)>0\\), where\n",
            "Since the parent Moore graph has score\n"
            "\\(k-(3+\\Delta)/2\\) and \\(a-b=2/k\\),\n"
            "Proposition~\\ref{prop:deletion-stability} gives\n"
            "\\[\n"
            " \\Phi(H)\\ge\n"
            " \\frac{3k-5-\\Delta-\\sqrt{k^2+4k-4}}2-\\frac2k.\n"
            "\\]\n"
            "For \\(k\\ge6\\), the sign-preserving squarings reduce positivity of this\n"
            "lower bound to \\(P(k)>0\\), where\n",
        ),
        (
            "small-puncture-grammar",
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x.\n"
            "\\]\n"
            "and\n"
            "\\[\n"
            " d_H^*(x)\n"
            " \\ge k-\\frac{s-t_x}{k-t_x}\n"
            " \\ge k-\\frac{s}{k}.\n"
            "\\]\n",
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x.\n"
            "\\]\n"
            "Consequently,\n"
            "\\[\n"
            " d_H^*(x)\n"
            " \\ge k-\\frac{s-t_x}{k-t_x}\n"
            " \\ge k-\\frac{s}{k},\n"
            "\\]\n"
            "where the last inequality follows from\n"
            "\\[\n"
            " \\left(k-\\frac{s-t}{k-t}\\right)-\\left(k-\\frac{s}{k}\\right)\n"
            " =\\frac{t(k-s)}{k(k-t)}\\ge0.\n"
            "\\]\n",
        ),
        (
            "nonadjacent-linebreak",
            "The direct sum,\n"
            "injectivity, orthogonality, all recomputed distances, and the polynomial sign\n",
            "The direct-sum decomposition, injectivity, orthogonality, all recomputed\n"
            "distances, and the polynomial sign\n",
        ),
        (
            "verification-table-layout",
            "\\begin{center}\n"
            "\\begin{tabular}{p{0.39\\textwidth}p{0.53\\textwidth}}\n",
            "\\begin{center}\n"
            "\\begingroup\n"
            "\\scriptsize\n"
            "\\setlength{\\tabcolsep}{4pt}\n"
            "\\renewcommand{\\arraystretch}{1.15}\n"
            "\\begin{tabular}{@{}p{0.30\\textwidth}p{0.67\\textwidth}@{}}\n",
        ),
        (
            "verification-table-end",
            "\\bottomrule\n"
            "\\end{tabular}\n"
            "\\end{center}\n"
            "\n"
            "The explicit \\(50\\)-vertex counterexample",
            "\\bottomrule\n"
            "\\end{tabular}\n"
            "\\endgroup\n"
            "\\end{center}\n"
            "\n"
            "The explicit \\(50\\)-vertex counterexample",
        ),
        (
            "ai-disclosure-scope",
            "OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, literature\n"
            "search, exact verification code, and Lean formalization.",
            "OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof\n"
            "exploration, and Lean formalization.",
        ),
        (
            "novelty-disclaimer-wording",
            "Search silence is not proof\n"
            "of novelty.  Accordingly, we use ``derive'' and ``prove'' rather than ``first''\n"
            "or ``previously unknown'', and make no minimum-order claim.",
            "Search silence is not proof of novelty.  Accordingly, we avoid unsupported\n"
            "priority language and make no minimum-order claim.",
        ),
        (
            "completed-lean-scope",
            "The explicit \\(50\\)-vertex counterexample is fully formalized in Lean 4.31 with\n"
            "Mathlib 4.31 \\cite{deMouraUllrich2021,Mathlib2020}.  The development checks the\n"
            "coordinate graph, regularity, the complete common-neighbour certificate, girth,\n"
            "the adjacency-square and distance-matrix identities, and an exact rational\n"
            "diagonalization with multiplicities.  Lean also kernel-checks finite spectral\n"
            "certificates for the orders \\(38,39,40,42\\).  For orders \\(38,39,42\\), these\n"
            "are positive-definiteness certificates for the corresponding shifted distance\n"
            "matrices; the order-\\(40\\) endpoint contains a complete exact diagonalization.\n"
            "The non-\\(50\\) formal statements are deliberately described as finite spectral\n"
            "certificates rather than as a single Mathlib theorem bundling every\n"
            "graph-theoretic phrase.  The LP ceiling, optimizer rigidity, punctured-Moore\n"
            "spectra, and deletion-robustness theorems remain conventional analytic proofs\n"
            "with exact executable audits; they are not included in the Lean claim above.",
            "The explicit \\(50\\)-vertex counterexample is fully formalized in Lean 4.31\n"
            "with Mathlib 4.31 \\cite{deMouraUllrich2021,Mathlib2020}.  The development\n"
            "checks the coordinate graph, regularity, the exhaustive common-neighbour\n"
            "certificate, girth five, the adjacency-square and distance-matrix identities,\n"
            "and an exact rational diagonalization with multiplicities.  Thus the\n"
            "\\(50\\)-vertex result is verified at graph level, including its least distance\n"
            "eigenvalue and strict WOW-284 gap.\n"
            "\n"
            "Lean also kernel-checks finite spectral certificates attached to the explicit\n"
            "constructions of orders \\(38,39,40,42\\).  For orders \\(38,39,42\\), the\n"
            "endpoints certify the stated minimum dual-degree data, positive definiteness of\n"
            "the corresponding shifted finite distance matrix, and hence the strict bound\n"
            "for every nonzero real eigenpair.  For order \\(40\\), Lean certifies a two-sided\n"
            "invertible exact diagonalization, the diagonal-entry multiplicities, the\n"
            "attained least eigenvalue \\(-5\\), dual degree six, and gap one.  These\n"
            "non-\\(50\\) endpoints are finite spectral certificates: they do not identify\n"
            "each semantic matrix with \\texttt{SimpleGraph.dist} and bundle every\n"
            "structural hypothesis into one public theorem.\n"
            "\n"
            "Separately, Lean formalizes the analytic optimization statement in\n"
            "Theorem~\\ref{thm:lp-ceiling}.  For every integer \\(k\\ge4\\) and every admissible\n"
            "finitely supported expansion\n"
            "\\[\n"
            "  f=\\sum_i c_iF_i,\n"
            "  \\qquad c_0>0,\n"
            "  \\qquad c_i\\ge0\\quad(i\\ge5),\n"
            "  \\qquad f\\vert_{I_k}\\le0,\n"
            "\\]\n"
            "it proves\n"
            "\\[\n"
            "  B_kc_0\\le f(k),\n"
            "  \\qquad B_k=\\frac{(k+2)(k^2+3)}6.\n"
            "\\]\n"
            "The formal development defines the coefficient family of the displayed\n"
            "quartic \\(f_*\\), proves that it is admissible and attains equality, and proves\n"
            "that every equality case is its unique positive scalar multiple, both as a\n"
            "polynomial and at coefficient level.  The kernel-checked dependency chain\n"
            "includes the nonbacktracking recurrence, the exact primal expansion, positivity\n"
            "and moment identities for the three-point dual certificate, strict slacks in\n"
            "degrees \\(5\\) through \\(9\\), the Chebyshev tail for every degree at least\n"
            "\\(10\\), finite-support weak duality, complementary slackness, and optimizer\n"
            "rigidity.\n"
            "\n"
            "This LP formalization is deliberately graph-independent.  It does not\n"
            "formalize the trace interpretation of the \\(F_i(A)\\), the girth-five\n"
            "vanishing and nonnegativity statements, the spectral trace decomposition, or\n"
            "the passage from the analytic LP inequality to graph-order bounds.\n"
            "Consequently the graph conclusions \\(n<B_k\\), the degree-six reductions\n"
            "\\(n\\le51\\) and \\(n\\le50\\), and the edge-local cycle argument remain\n"
            "conventional analytic proofs, with exact executable audits where cited.  The\n"
            "punctured-Moore spectra, the general deletion-stability inequality, the\n"
            "small-puncture normal form, and the Hoffman--Singleton deletion-radius theorem\n"
            "are likewise analytic results supported by exact Python audits; they are not\n"
            "part of the Lean claim.",
        ),
    ]

    for label, old, new in replacements:
        text = replace_once(text, old, new, label)

    if any(ord(char) < 32 and char not in "\t\n" for char in text):
        raise AssertionError("control byte introduced in third pass")
    TEX.write_text(text, encoding="utf-8", newline="\n")
    print("v2.2 third proof-completeness pass: PASS")


if __name__ == "__main__":
    main()
