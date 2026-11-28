# CJ-0001 — manuscript of the candidate proof of the Collins–Shor conjecture

`main.tex` is a self-contained candidate proof, for every tree `T` with
`n ≥ 3` vertices, that every index `p` at which the normalized coefficients
`d_0, …, d_{n−2}` of the distance characteristic polynomial are maximal
satisfies `⌊n/2⌋ ≤ p ≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉` (Conjecture 1.2 of
arXiv:1507.02341; Conjecture 9 of Collins, Discrete Appl. Math. 25 (1989)).

**Status.** Draft written with AI assistance (Claude, model
`claude-opus-5-5`, sessions 14 and 15, 2026-11-27) from the project's notes.
It has been reviewed only by AI models (table below). No mathematician has
read it. It is a **candidate proof**, not an established result. Not for
distribution: any outside use is decided by the project director.

## Versions

A review applies to one revision. Every revision is retrievable with
`git show <commit>:manuscripts/CJ-0001-collins-shor/main.tex`; revision 2,
the one reviewed as a whole by a model of another vendor, is also kept
byte-identical in [`versions/r2/main.tex`](versions/r2/main.tex), so that it
survives any later rewriting of `main.tex`. Reviews are in
`research/active/CJ-0001-collins-shor-peak/reviews/`.

| Revision | Commit | SHA-256 of `main.tex` | Reviews of this revision | Checks |
| --- | --- | --- | --- | --- |
| 1 | `8df6bea` | `8feaaa4b…a1a5f0` | whole document: `claude-opus-5-5`, `claude-sonnet-5-5` (fresh contexts, Anthropic); no gap found within stated scope | `manuscript_check.py` (lower half), 11,379 checks, 0 failures |
| 2 | `87c3c8c` | `5dd8d2b3…5b42a9` | changes only: `claude-sonnet-5-5` recheck, no gap; whole document: an OpenAI model through Codex ("GPT Astra 6 (Extra High)", director's description), no gap found within the scope of its review, six findings (one error in a remark not used by the Main Theorem, five of wording or citation) | as revision 1; Lemma 7.5 for `n < 800` |
| 3 | `f695cbd` | `3477baa0…37d917b` | changes only: `claude-opus-5-5` recheck (fresh context, the author's model), no gap found within stated scope, eight defects of wording, status or provenance | `amw_reduction_check.py` (Remark 9.6 and Section 12, item 1), 0 failures |
| 4 | session 15 | see `git log` | the added Lemma 11.3 as a note: `claude-sonnet-5-5` (`notes/path-formula.md` at `e15ae8f`), no gap; the recheck of revision 4 itself: journal of session 15 | `path_formula_check.py` (Lemma 11.3, paths of order 2 to 60), 0 failures |

Revision 3 corrects the six findings of the review of revision 2 (and
replaces one decimal estimate in the proof of Lemma 9.3 by an exact one).
Revision 4 corrects the eight defects of the recheck of revision 3 and adds
Lemma 11.3, a proof of Collins's formula, so that Section 11 no longer needs
it as a citation. Revisions 2 and 3 are kept byte-identical in
[`versions/`](versions/).

## Compiling

Plain LaTeX with standard packages (`amsart`, `amsmath`, `amssymb`, `amsthm`,
`hyperref`). Run `pdflatex main.tex` twice (three times for the table of
contents). Checked with MiKTeX pdfLaTeX on 2026-11-27: 30 pages (first
version), 32 pages (revision 2), no undefined reference. The PDF is not committed.

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
