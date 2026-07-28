#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def revise_tex(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = [
        (
            "The Moore bound is attained, so adjacent vertices have no common neighbour and\n"
            "nonadjacent vertices have exactly one.  Therefore\n",
            "The Moore bound is attained, so adjacent vertices have no common neighbour and\n"
            "nonadjacent vertices have exactly one.  Given an edge \\(uv\\), choose\n"
            "\\(x\\in N(u)\\setminus\\{v\\}\\) and \\(y\\in N(v)\\setminus\\{u\\}\\).  The vertices\n"
            "\\(x,y\\) are nonadjacent, since an edge would create a four-cycle, and their\n"
            "unique common neighbour completes a five-cycle through \\(uv\\).  Therefore\n",
            "Moore girth witness",
        ),
        (
            "Let \\(G\\) be connected and \\(k\\)-regular, with diameter \\(d\\) and girth at\n"
            "least \\(2d-1\\).  Define\n",
            "Let \\(G\\) be connected and \\(k\\)-regular, with diameter \\(d\\) and girth at\n"
            "least \\(2d-1\\).  Let \\(A_i\\) denote the distance-\\(i\\) matrix, and define\n",
            "distance matrix notation",
        ),
        (
            "Let \\(G\\) be any connected finite simple graph, and let \\(u,v\\) be vertices at\n"
            "distance \\(d\\ge5\\).  Put \\(p=d(u)\\) and \\(q=d(v)\\).  Then\n"
            "\\[\n"
            " \\boxed{\n"
            " \\lambda_{\\min}(D(G))\n"
            " \\le p+q-2-\\sqrt{(p-q)^2+pq(d-2)^2}.\n"
            " }\n"
            "\\]\n"
            "If \\(\\delta\\) is the ordinary minimum degree, then\n"
            "\\[\n"
            " \\boxed{\n"
            " \\lambda_{\\min}(D(G))\\le-\\delta(d-4)-2.\n"
            " }\n"
            "\\]\n"
            "Consequently every strict WOW-284 counterexample satisfies\n"
            "\\[\n"
            " \\Delta>\\delta(d-4)+2.\n"
            "\\]\n",
            "Let \\(G\\) be any connected finite simple graph, and let \\(u,v\\) be vertices at\n"
            "distance \\(\\ell=d_G(u,v)\\ge5\\).  Put \\(p=d(u)\\) and \\(q=d(v)\\).  Then\n"
            "\\[\n"
            " \\boxed{\n"
            " \\lambda_{\\min}(D(G))\n"
            " \\le p+q-2-\\sqrt{(p-q)^2+pq(\\ell-2)^2}.\n"
            " }\n"
            "\\]\n"
            "If \\(\\delta\\) is the ordinary minimum degree, then\n"
            "\\[\n"
            " \\boxed{\n"
            " \\lambda_{\\min}(D(G))\\le-\\delta(\\ell-4)-2.\n"
            " }\n"
            "\\]\n"
            "Consequently every strict WOW-284 counterexample satisfies\n"
            "\\[\n"
            " \\Delta>\\delta(\\ell-4)+2,\n"
            "\\]\n"
            "where \\(\\Delta\\) is the ordinary maximum degree.\n",
            "endpoint theorem notation",
        ),
        (
            "neighbourhood distances are at most two; between the two neighbourhoods they\n"
            "are at least \\(d-2\\).  Since the cross products are negative, the Rayleigh\n",
            "neighbourhood distances are at most two; between the two neighbourhoods they\n"
            "are at least \\(\\ell-2\\).  Since the cross products are negative, the Rayleigh\n",
            "endpoint proof distance",
        ),
        (
            " 2(p-1)&-(d-2)\\sqrt{pq}\\\\\n"
            " -(d-2)\\sqrt{pq}&2(q-1)\n",
            " 2(p-1)&-(\\ell-2)\\sqrt{pq}\\\\\n"
            " -(\\ell-2)\\sqrt{pq}&2(q-1)\n",
            "endpoint matrix",
        ),
        (
            "\\(p=\\delta+\\alpha\\), \\(q=\\delta+\\beta\\), and \\(t=d-2\\).  The identity\n",
            "\\(p=\\delta+\\alpha\\), \\(q=\\delta+\\beta\\), and \\(t=\\ell-2\\).  The identity\n",
            "endpoint t",
        ),
        (
            "In a strict\n"
            "counterexample, each factor \\(2k-2-y_i^2\\) is positive.  The sum cannot vanish: otherwise every nonprincipal adjacency eigenvalue\n"
            "would equal \\(-2\\), and \\(\\tr A=0\\) would give\n",
            "In a strict\n"
            "counterexample, each factor \\(2k-2-y_i^2\\) is positive.  The sum cannot\n"
            "vanish: otherwise every nonprincipal adjacency eigenvalue would equal\n"
            "\\(-2\\), and \\(\\tr A=0\\) would give\n",
            "moment sentence flow",
        ),
        (
            "bound \\(n\\ge k+1\\) for a simple \\(k\\)-regular graph.  The identity is checked symbolically by\n",
            "bound \\(n\\ge k+1\\) for a simple \\(k\\)-regular graph.  The identity is\n"
            "checked symbolically by\n",
            "moment sentence flow 2",
        ),
        (
            "contradicting \\(\\delta^*=6\\).  Diameter two would force\n"
            "\\((x-6)(x^2+x-5)^{18}\\); its root sum is \\(-12\\), contradicting\n",
            "contradicting \\(\\delta^*=6\\).  Diameter two would force equality in the\n"
            "Moore bound, hence order \\(37\\) and adjacency characteristic polynomial\n"
            "\\((x-6)(x^2+x-5)^{18}\\); its root sum is \\(-12\\), contradicting\n",
            "degree6 diameter2",
        ),
        (
            "Let \\(B\\) be the surviving-vertex by deleted-vertex incidence matrix.  Then\n",
            "Let \\(B\\) be the surviving-vertex by deleted-vertex incidence matrix, with\n"
            "\\(B_{xz}=1\\) exactly when \\(x\\sim_M z\\).  Then\n",
            "small puncture incidence definition",
        ),
        (
            "OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof\n"
            "exploration, and Lean formalization.  No AI system is an\n",
            "OpenAI's ChatGPT assisted with adversarial proof checking, proof exploration,\n"
            "and Lean formalization.  No AI system is an\n",
            "AI disclosure",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, f"{path}: {label}")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_text(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new)
    elif new not in text:
        raise AssertionError(label)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    if "OpenAI's ChatGPT assisted" not in (ROOT / "main.tex").read_text(encoding="utf-8"):
        revise_tex(ROOT / "main.tex")
        revise_tex(ROOT / "v22" / "main.tex")
    update_text(
        ROOT / "PROVENANCE.md",
        "OpenAI ChatGPT-5.6 Sol Pro assisted",
        "OpenAI's ChatGPT assisted",
        "provenance AI disclosure",
    )
    update_text(
        ROOT / "scripts" / "sync_manuscript_artifacts.py",
        "OpenAI ChatGPT-5.6 Sol Pro assisted",
        "OpenAI's ChatGPT assisted",
        "synchronization AI marker",
    )
    update_text(
        ROOT / "scripts" / "validate_repository.py",
        "OpenAI ChatGPT-5.6 Sol Pro assisted",
        "OpenAI's ChatGPT assisted",
        "repository-validation AI marker",
    )
    print("final arXiv last line pass: PASS")


if __name__ == "__main__":
    main()
