# Independent review — CJ-0001 — manuscript revision 2 (whole document)

- **Reviewer:** an OpenAI model run by the project director through Codex.
  The director's description: "GPT Astra 6 (Extra High), through Codex". The
  report's own description: "Codex (OpenAI, agente baseado em GPT-6)". No
  exact model identifier string was supplied. **Different vendor from the
  author** (the author is Claude, Anthropic).
- **Date:** 2026-11-27 (report dated "27 de novembro de 2026").
- **Independence:** obtained by the director outside this repository. By its
  own account the reviewer received `main.tex` and followed
  `REVIEW-PROMPT.md` (after the director confirmed it). It did not receive the
  project's code, notes or earlier reviews ("Não recebi nem usei o código do
  projeto"; "Não usei os relatos das revisões anteriores como evidência de
  correção"). This session cannot verify that account beyond the hashes
  below.
- **Revision reviewed:** `manuscripts/CJ-0001-collins-shor/main.tex` at
  revision 2, commit `87c3c8c`. The report gives the SHA-256 of the bytes it
  read, `5dd8d2b397e78ddf7a41d13d3fe07f115e5405583ee379e2fc0bd184865b42a9`.
  **Provenance check (session 15, 21:03 local):** equal to the SHA-256 of
  `git show 87c3c8c:manuscripts/CJ-0001-collins-shor/main.tex`, and of the
  director's file `D:\Usuarios\GBB\Downloads\main.tex` (the path named in the
  report). The `REVIEW-PROMPT.md` in that folder has the SHA-256 of the
  repository's file (`049ee979…a351e`). So the review applies to revision 2
  exactly.
- **Material given to the reviewer:** `main.tex` (revision 2) and
  `REVIEW-PROMPT.md`; the primary sources were consulted by the reviewer on
  the web (URLs in the report).
- **The report itself:** kept verbatim, in Portuguese, in
  [`2026-11-27-codex-gpt-astra-6-manuscript-r2.original-pt.txt`](2026-11-27-codex-gpt-astra-6-manuscript-r2.original-pt.txt).
  The director supplied its text in the session; the file on the director's
  machine (`parecer-revisao.txt`) was not found on this disk, so the stored
  copy is the text as received in the session, not a byte copy of that file.
  The companion files the report names (`verify_main.py`,
  `verification-results.json`, `tie-example.json`) were not supplied and were
  not examined.

## Statement as read by the reviewer

For every tree of order `n ≥ 3`, every maximizing index `p` of the normalized
coefficients satisfies `⌊n/2⌋ ≤ p ≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉`; the
star has a unique maximum at the lower bound; the path attains the outer
upper bound for infinitely many `n`. (Report, end of section 2.)

## Findings (summary in English of the report's section 1)

| # | Class | Location | Finding |
| --- | --- | --- | --- |
| 1 | ERROR | Remark 9.6 (`rem:AMW`) | "±√μ_j (over the Laplacian eigenvalues) together with zeros" miscounts the zero eigenvalue: `S(T)` has `2n − 1` vertices; its spectrum is `{0} ∪ {±√μ_j : j = 1..n−1}` over the positive Laplacian eigenvalues only, with exactly one zero. The avm identity is unaffected. Not used by the proof of Theorem 9.5. |
| 2 | WORDING | Section 12, item 1 | The claim that the other `n` "would need" a mode–mean inequality sharper than Darroch's is too strong: the results already settle every `n` with `p(P_n) = ⌈ξ⌉`, e.g. `n = 9` (`ξ ≈ 4.975`, `K = 5`, `h_9(4) = 10 > 0`, so `p(P_9) = 5`). The question remains only where `p(P_n) < K`; a sharper inequality is one possible approach. |
| 3 | WORDING | Sections 1 and 9 | `φ` (golden ratio) is used but never defined. |
| 4 | WORDING | Abstract | The Graham–Lovász peak should be `⌊n/2⌋`, as on p. 83 of their paper (reproduced by Aalipour et al.), not `n/2`. |
| 5 | CITATION | Remark 9.6; Section 15 | The relation with Andriantiana–Misanantenaina–Wagner can be stated precisely: with the correction of finding 1 the reduction works (reconstructed in the report: incidence matrix, signature similarity, rank `n − 1`, matchings of a forest, their Lemma 5.1), so Theorem 9.5 is a consequence of their Theorem 4.4; the path-merging proof is an independent proof. This does not bear on the novelty of the Main Theorem's bounds. |
| 6 | WORDING | Section 12, item 3 | `R(K, ν)` is used without definition (only `R_w` with weight at the root is defined). |

No finding classified as GAP. Verdict: "no gap found within the scope of
this review".

Section 2 of the report records a reconstruction of Sections 2–11 statement
by statement (signs and powers of 2 in Lemma 2.1; the GL inverse re-derived;
the cone rules; the minors and the path cofactor formula; Lemma 5.1 by the
Schur complement; Propositions 6.1–6.3 including the sum of squares and the
cone levels; the non-circularity of the induction of Theorem 7.1; Lemmas 7.4,
7.5 with their boundary cases `n = 3, 4`; the interlacing directions and the
inertia in Section 8; the gluing formula, Lemma 9.3 with its convexity step,
Lemma 9.4, the leaf-count induction of Theorem 9.5; Lemma 9.7 by a second
derivation; Darroch's rule with two modes; the passage from
`p < ξ + 3/5` to `p ≤ ⌈ξ − 2/5⌉`; Lemma 11.1 and Corollary 11.2). It suggests
an exact replacement of the decimal estimate at the end of Lemma 9.3, and a
closed form `tr(I + L_{P_n})^{−1} = 2/5 + (n/√5) coth(2n log φ)`.

Section 3 of the report describes its own exact checker (not seen by this
session): 436 trees of orders 1–11 and more (rooted choices, merges, the
lemmas of Sections 9 and 11, the star's shape for `n ≤ 300`), cone
memberships certified by exact rational certificates, no failure; and a tie at
order 13 with `d_6 = d_7 = 189972`.

Sections 4–5 list the sources consulted (Aalipour et al. v3 and the journal
version; Graham–Lovász scan; Pitman pp. 281, 284; Collins's preprint, where
the path theorem is numbered Theorem 2, p. 6, so the manuscript's "Theorem 3,
p. 31" could not be confirmed against the journal; AMW arXiv v1; Hogben–
Reinhart 2021) and what was not verified (the project's files and runs, the
enumeration to order 23, Lean, provenance claims, Darroch's and Graham–
Pollak's original papers, Collins's thesis, the typesetting).

## Assessment by the principal investigator (session 15)

This assessment is the author's response to the review, not a review. Each
finding was checked against the text of revision 2 and, where it states
mathematics, re-derived or recomputed in this session.

1. **Accepted (error, outside the proof of the Main Theorem).** The count is
   right: `B` is `n × (n−1)` of rank `n − 1`, so the `2n − 1` eigenvalues of
   `S(T)` are `±√μ_j` for the `n − 1` positive `μ_j` and one `0`. Revision 3
   states this and proves the reduction in full (Remark 9.6).
2. **Accepted.** Recomputed exactly (`amw_reduction_check.py`, part D): for
   `3 ≤ n ≤ 2000`, the bound settles `p(T) ≤ p(P_n)` for 799 values with
   fractional part of `ξ` below `2/5` and for 393 further values with
   `p(P_n) = ⌈ξ⌉`; 806 values remain open (the first: 3, 5, 7, 8, 10, all
   below 24, where the exhaustive computation settles them). `n = 9`:
   `⌈ξ − 2/5⌉ = 5 = p(P_9)`, `h_9(4) = 334 − 324 = 10`, confirmed. The same
   overstatement was in `STATE.md` (Next step (e), (PX-peak)); corrected there
   too.
3. **Accepted.** `φ = (1 + √5)/2` defined at its first use and in the
   conventions.
4. **Accepted provisionally; wording settled after the literature audit of
   session 15** (see the dossier, section of session 15, for what Graham–
   Lovász p. 83 says). The manuscript's own statements already use the floor.
5. **Accepted, after an independent check.** The statements of AMW Theorem
   4.4 (`avm(T′) ≤ aN + b` for every non-path tree of order `N`,
   `a = (5−√5)/10`, `b = (7√5−17)/10`) and Lemma 4.2, eq. (8) (the path) were
   read in the arXiv HTML rendering of v1 in this session; Lemma 5.1 was not
   read verbatim, and is not needed, since its forest case is proved in
   Remark 9.6 in three lines. Strictness, which the verbatim statement of
   Theorem 4.4 does not state, follows from eq. (8): `avm(P_N) > aN + b` for
   `N ≥ 4` (proved in Remark 9.6; checked exactly for `4 ≤ N ≤ 200`). Exact
   checks of the reduction: the matching numbers of `S(T)` equal the
   coefficients of `det(I + tL_T)` and `avm(S(T)) = n − tr(I+L_T)^{−1}` on all
   94 trees of order 2–9; the path is the unique avm maximizer on all 32,507
   trees of order 2–16. **Consequence for the records:** MD-0023 (Theorem T10)
   is a consequence of a published result; its novelty becomes
   `prior-resolution-identified` (as a statement; the proof by merging
   pendant paths is independent of AMW's). The upper half of the Main Theorem
   is not affected: it uses T10 as a lemma, and now has two independent
   proofs of that lemma.
6. **Accepted.** `R(K, ν)` defined in item 3 (it matches `R(T, ν)` of
   `notes/gamma-components.md`, Proposition S14, and reduces to `R_w` for
   `ν = w e_u`).
7. **Suggestions taken:** the exact estimate `log φ = artanh(1/√5) > 1/√5`,
   `tanh(3 log φ) = 2/√5`, so `3 log φ · tanh(3 log φ) > 6/5 > 1`, replaces the
   decimal one in Lemma 9.3 (checked: `φ^6 = 8φ + 5`,
   `(4φ + 2)/(4φ + 3) = 2/√5`). The closed form with `coth` is equivalent to
   Lemma 9.7 (`coth(2n log φ) = 1 + 2r^{2n}/(1 − r^{2n})`, `r = φ^{−2}`); not
   added.
8. **Tie at order 13:** confirmed independently in this session (all 1,301
   trees of order 13; exactly one tie, indices 6 and 7, value 189972).
9. **Collins's numbering:** referred to the literature audit of session 15.

## Verdict

`no gap found within stated scope` (the reviewer's). It applies to revision 2
(`87c3c8c`) only. It is an AI review, by a model of a different vendor from
the author's; it is not human or peer review, and its favourable verdict is
not evidence of correctness or originality beyond what it checked.
