# CJ-0001 — manuscript of the candidate proof of the Collins–Shor conjecture

`main.tex` is a self-contained candidate proof, for every tree `T` with
`n ≥ 3` vertices, that every index `p` at which the normalized coefficients
`d_0, …, d_{n−2}` of the distance characteristic polynomial are maximal
satisfies `⌊n/2⌋ ≤ p ≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉` (Conjecture 1.2 of
arXiv:1507.02341; Conjecture 9 of Collins, Discrete Appl. Math. 25 (1989)).

**Status.** Draft written with AI assistance (Claude, model
`claude-opus-5-5`, session 14, 2026-11-27) from the project's notes. Its
parts were reviewed earlier by AI models of one vendor (Anthropic); the
document as a whole is under review (see `STATE.md` of the investigation,
obligation 14). No mathematician has read it. It is a **candidate proof**,
not an established result. Not for distribution: any outside use is decided
by the project director.

## Compiling

Plain LaTeX with standard packages (`amsart`, `amsmath`, `amssymb`, `amsthm`,
`hyperref`). Run `pdflatex main.tex` twice (three times for the table of
contents). Checked with MiKTeX pdfLaTeX on 2026-11-27: 30 pages, no undefined
reference. The PDF is not committed.

## Structure

| Sections | Content | Depends on |
| --- | --- | --- |
| 1–2 | Statement, main theorem, classical results used, two elementary lemmas | — |
| 3–7 | Lower bound `p ≥ ⌊n/2⌋`: cones `K_d`, minors, rooted trees, distances, the induction (Theorem 7.1), star minimality (Theorem 7.3) | 2 |
| 8–10 | Upper bound `p < n − n/√5 + 3/5`: spectral form, Darroch's rule, interlacing, the trace of `(I+L)^{-1}` and its minimization by the path | 2 |
| 11 | The exact peak of the path; sharpness of the upper bound | 2, Collins's formula |
| 12–16, App. A | Open problems, computations, Lean, literature, status, provenance | — |

The two halves are independent of each other.

## For reviewers (in particular of other vendors)

The prompt in [`REVIEW-PROMPT.md`](REVIEW-PROMPT.md) is the one to give an
independent reviewer together with `main.tex` (or its PDF) and the primary
source. Give nothing else: not the project's notes, not earlier reviews, not
this README beyond the prompt. A review applies to one revision of
`main.tex`; record its Git commit and SHA-256.

Reports go to
`research/active/CJ-0001-collins-shor-peak/reviews/<date>-<model>-manuscript.md`
in the format of `research/templates/review.md`.

## Computations

`experiments/CJ-0001-collins-shor-peak/manuscript_check.py` checks the lower
half as written here, from its own definitions (exact arithmetic; result
`results/manuscript-check.json`). The other computations cited in Section 13
are described in `experiments/CJ-0001-collins-shor-peak/README.md`.
