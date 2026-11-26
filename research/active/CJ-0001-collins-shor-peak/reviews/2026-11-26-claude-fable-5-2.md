# Independent review — CJ-0001 — lemmas R1, L1, L2, L3 and the evidence claims of `STATE.md`

- **Reviewer:** Claude, model `claude-fable-5-2` (same model family as the
  author; fresh context without the author's reasoning).
- **Date:** 2026-11-26.
- **Independence:** a fresh subagent context that received the file paths, the
  primary-source reference and a checklist, and not the author's reasoning
  trail. **This is an AI review, not human review and not peer review.** The
  independence is limited: the reviewer is the same model as the author, so
  shared blind spots are possible. A different model or a mathematician has not
  looked at this material.
- **Revision reviewed:** Git commit `e34acfc0bf363fc5c340a7f1611ad0b67c53788d`,
  branch `research`, working tree clean at the start of the review.

  | File | SHA-256 (working tree) | Git blob |
  | --- | --- | --- |
  | `research/active/CJ-0001-collins-shor-peak/notes/lemmas.md` | `228d011d121eede7e6045a4552eb0c173142d5701da0dd78c546762603c62672` | `0d27f32ed5ae4d65bb8de3968f0b8ad9da60b8ab` |
  | `research/active/CJ-0001-collins-shor-peak/STATE.md` | `191b01fe0d680aee9b4ba754f9fb6e394a4071d445517c90ea690ad6928dec9e` | `8649df6ae376550af97f80c6a7e17b5f7a17bbf3` |

- **Material given to the reviewer:** the repository at that revision; the
  reference arXiv:1507.02341. The TeX source of arXiv:1507.02341
  (`DistanceCharPolyLogConcaveS.tex`, last version dated 2017-04-20) was
  downloaded by the reviewer and read directly.

## Statement as read from the primary source

Written before reading the proofs, from the TeX source of arXiv:1507.02341.

- Objects: a tree `T` of order `n` ("the order of a graph is assumed to be at
  least three"); `δ_k(T)` is the coefficient of `x^k` in `det(D(T) − xI)`;
  `d_k(G) = 2^k |δ_k(G)| / 2^{n−2}` for `0 ≤ k ≤ n−2` (normalized coefficients).
- Fact 1.1 (cited there to Graham–Lovász, Eq. (44)): `(−1)^{n−1} δ_k(T) > 0`
  for `0 ≤ k ≤ n−2`.
- Conjecture 1.2 (Collins–Shor), verbatim: "The [normalized] coefficients of
  the distance characteristic polynomial for any tree `T` with `n` vertices are
  unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`." Quantifier: every tree,
  every `n` (with `n ≥ 3` by the standing assumption).
- The source defines *unimodal* with weak inequalities and never defines "peak"
  when the maximum is attained twice. The tie convention is therefore a choice
  of the project, as `STATE.md` says.
- Theorem 2.1(iii): `d_0, …, d_{n−2}` is log-concave and unimodal.
  Observation 3.1: `ℓ_T(x) = −2^{−(n−2)} det(2xI − D)` is real-rooted with
  coefficients `−4` (`x^n`), `0` (`x^{n−1}`), `d_k > 0` (`x^k`, `k ≤ n−2`).
  Theorem 3.3 (peak at most `⌈(2−ρ)n/(3−ρ)⌉`) uses
  `d_1(T) = 2n(n−1) − 2 N_{P_3}(T) − 4`, cited to Edelberg–Garey–Graham.
- The source says Collins's Conjecture 9 is stated without floor and ceiling,
  that Collins's Theorem 1 gives `⌊n/2⌋` for stars, and that the path may attain
  the floor or the ceiling of `n − n/√5`. "Computations on Sage confirm this
  conjecture for all trees of order at most 20."

The quotation, the definitions, the theorem numbers (Fact 1.1, Conjecture 1.2,
Theorem 2.1, Observation 3.1, Theorem 3.3) and `M = ⌈n − n/√5⌉ = n − ⌊n/√5⌋ =
n − isqrt(n² // 5)` in `STATE.md` agree with the source and with my own
derivation (`n/√5` is irrational; `⌊√y⌋ = isqrt(⌊y⌋)`).

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | R1 needs positivity and log-concavity of `d_0..d_{n−2}`; both are taken from the source (Fact 1.1, Theorem 2.1(iii)), whose proofs I did not check. L1 needs Graham–Pollak and the Graham–Lovász inverse formula. L3 assumes every `c_i ≥ 1`; this is sufficient, and my tests show it is not necessary when `n ≥ 2s` (the identity also held for `c = (2,0,3)` and `(0,3)`), so the hypothesis is conservative, not wrong. |
| Quantifiers | R1 is stated only for the two indices `m` and `M` but its proof of the second bullet applies "the first claim" to the reversed sequence at the different index `n−2−M`. The proof given is in fact valid for any index `1 ≤ j ≤ n−2`, so this is a presentation gap, not a mathematical one: the first claim should be stated for a general index. **Hypothesis A(ii) in `STATE.md` is ill-defined at `n = 4`** (and `n = 3`): it quantifies over `0 ≤ k ≤ p_n`, but `ρ_k = d_{k+1}/d_k` requires `k ≤ n−3` and `p_4 = 2 = n−2` (my computation and `results/ratio-extremality-04-17.json`, order 4, `path_peak` 2, `range_ii` [0, 1]). The code tests `k ≤ min(p_n, n−3)` (`ratio_extremality.py` lines 65 and 118), which is not the statement written in `STATE.md`. The "Consequence" paragraph (`ρ_{p_n}(P_n) < 1`) has no meaning at `n = 4`. For `n ≥ 5` the recorded `p_n ≤ n−3` in all orders computed. |
| Mathematical definitions | `d_k`, `δ_k`, `ℓ_T`, `m`, `M` agree with the source. I confirmed by direct computation that the coefficient of `x^k` in `ℓ_T` equals `d_k` (and `0`, `−4` at the top) on every tree tested. |
| Boundary cases | `n = 3`: `m = 1 = n−2`, `M = 2 ≥ n−2`, star = path, both equalities of L2 hold at once, consistent with the wording. `M ≥ n−2` exactly for `n ≤ 6`; this case is not treated in the proof of R1 but is trivial. Ties: R1 tested on abstract log-concave sequences with plateaus at every position; no tie occurred among my trees (the repository records a single tie, order 13, which I did not recompute). L3: `s = 1` (stars, including `c = (2)`), `c_i = 1`, `n = 2s` (for example `P_4 = (1,1)` and `(1,1,1,1,1)`) all pass. |
| R1 | **No gap found within stated scope.** Reconstructed: ratios of a positive log-concave sequence are non-increasing; `d_{j−1} < d_j` forces strict increase up to `j`; `d_{j−1} ≥ d_j` forces non-increase from `j−1` on, so a maximizer `≤ j−1` exists. Reversal gives the upper criterion. The equivalences are for the strong tie reading; under the weak reading the lower criterion would be `d_{m−1} ≤ d_m`. Tested: 20,000 random positive log-concave rational sequences (all indices, ties included); all 18,247 labelled trees of order 3–7; 88 named/random trees of order 3–14; 1,350 random trees of order 8–16. 0 failures. |
| L1 | **No gap found within stated scope.** Each algebraic step reconstructed (factorisation through `D^{-1}`, matrix determinant lemma, signs of `det(−B)` and `adj(−B)`, final scaling). The inverse formula, which the file says is "quoted from memory", I re-derived: `LD = τ𝟙ᵀ − 2I` (entrywise, using that exactly one neighbour of `i` is closer to `j`) and `Dτ = (n−1)𝟙` (sum over edges), hence `(−L/2 + ττᵀ/(2(n−1))) D = I`. Graham–Pollak I did not re-derive. Tested exactly: `det D`, the inverse formula and L1 as a polynomial identity (at `n+1` points, degree `≤ n`, both sides by Gaussian elimination over `Fraction`) on all 1,440 labelled trees of order 3–6, 88 trees of order 3–14, and the two order-20 trees. 0 failures. The "Checks" paragraph (`adj(L) = J`, coefficient `−4`) is correct. |
| L2 | **No gap found within stated scope.** Coefficient extraction and the `e_v` argument reconstructed, including both equality cases. Tested on all 18,247 labelled trees of order 3–7 plus the trees above: formula, both bounds, equality iff star / iff path. 0 failures. The formula is algebraically the same as `d_1 = 2n(n−1) − 2N_{P_3} − 4` in the proof of Theorem 3.3 of the source; see "Novelty coverage". |
| L3 | **No gap found within stated scope.** Equitable partition, the action on class-constant vectors (matrix `Q` in the basis of indicator vectors), the `−2` eigenspace of dimension `Σ(c_i − 1) = n − 2s`, and the rescaling to `ℓ_T` reconstructed. Tested: the full identity `det(xI − D) = (x+2)^{n−2s} det(xI − Q)` coefficient by coefficient, and the binomial form for every `d_k`, on 29 caterpillars (17 chosen, 12 random; `s` from 1 to 7). 0 failures. |
| Logical implications | `STATE.md` uses R1 at the index `p_n` (consequence of A(ii)); this needs the general-index form noted above. The dependency map is otherwise consistent with the lemmas. O1's reduction (`s = 2`, `d_k ∝ Σ_{j=0}^{4} g_j C(n−4, k−j)`) follows from L3 and matched my computation for double stars. |
| Dependency assumptions | Cited and not verified by the project or by me: Collins (1989), Theorems 1 and 3 (via the source); Graham–Lovász (1978), sign pattern; Graham–Pollak; Edelberg–Garey–Graham. Theorem 2.1 of the source was read but its proof not checked. The upper-half plan in `STATE.md` rests on Collins's path theorem, which nobody in the project has read; `STATE.md` says so. |
| Counterexample attempts | Against the lemmas: the test sets above, plus a negative control for L3 with `c_i = 0`. None found. Against the refutation of A(i): recomputed, see Reproduction; it stands. |
| Formalization scope | None exists for CJ-0001 and none is claimed. Not assessed. Lean was not run. |
| Novelty coverage | I performed no literature search. `STATE.md` (obligation 1) says it is unknown whether L1–L3 are in the literature; for L2 this is inaccurate as worded, since the `d_1` formula is in the source that the project read (proof of Theorem 3.3), and `notes/lemmas.md` itself notes the relation. The `STATE.md` table entry "Proved here" for L2 should say that the formula is a restatement of a cited one. No file claims novelty; `notes/lemmas.md` and `STATE.md` both say novelty is unknown. |
| Unresolved gaps | See the discrepancy list below. None of them invalidates R1, L1, L2, L3, the counts in E1–E4 or the counterexample to A(i). |

## Claims versus evidence (`STATE.md` against `experiments/…/results/*.json`)

Confirmed against the JSON files: E1 (1,346,022 trees, orders 3–20, 0
violations, 0 guard failures, counts equal to the reference list); E2
(22,596,335 = 2,144,505 + 5,623,756 + 14,828,074, 0 violations); E3 (one tie,
order 13, indices 6 and 7, interval [6, 8]; guards cover `d_0 = n−1` and
unimodality); E4 (peak in `{⌊n/2⌋, ⌊n/2⌋+1}` for every order 3–23; star peak =
minimum, path peak = maximum); A(ii) counts (1,346,021 trees, orders 4–20;
10,000 = 400 × 5 models × 5 orders, seed 20261126, 0 violations); A(i) (522,956
trees of order 4–19 with 0 violations; 10 violating trees at order 20, which I
identified from the layouts as `S(a,18−a)`, `1 ≤ a ≤ 9`, and the spider; the
star-minimising index set at order 20 is `{0..8}`, so all violations are at
`k = 9`); the index sets for `10 ≤ n ≤ 19`; the Q1 and Q2 numbers; the timings
(2,014 s, about 41 minutes in total); 87 tests in `tests/test_cj0001_distpoly.py`.

Discrepancies, most serious first:

1. **The repository's check of L3 is weaker than described.**
   `notes/lemmas.md`, L3: "*Check.* Exact agreement with the direct `n × n`
   computation on six caterpillars"; `STATE.md`, row L3: "checked exactly on six
   caterpillars". The validation step (`near_star_families.py`, lines 107–110)
   asserts only that the single ratio `q = d_{m−1}/d_m` agrees. It does not
   compare the determinant identity or the other coefficients. (My own test of
   the full identity passed, so the lemma is not in doubt; the description of
   the repository's evidence is.)
2. **"once `n ≥ 20`" overstates the evidence.** `STATE.md`: "the star is not
   the extremal tree for the lower bound once `n ≥ 20`";
   `learning/CJ-0001-collins-shor-peak.md`, section 8: "from there on, the
   balanced double star is closer to violating the lower bound than the star
   is". The evidence is: order 20 (exhaustive), even orders 22–40 (double
   stars), and sampled trees of the even orders 24, 30, 40, 60, 90. There is no
   evidence at odd orders. My computation: at `n = 21, 23, 25` **no** double
   star has a larger `q` than the star (best double star `S(1, n−3)`, e.g.
   `0.86127 < 0.86275` at `n = 21`); a double star exceeds the star at
   `n = 31` and `n = 41`. Whether some other tree exceeds the star at odd
   orders 21–29 is not known from anything in the repository.
3. **Result files do not carry what the rules require.** `AGENTS.md` §5: "Say
   'verified' only with the command that was run, its result, and the revision
   it ran on." `docs/verification-policy.md`: "The result file states the exact
   range covered, the counts, the versions and the command." None of the six
   JSON files records a command or a Git revision; the two
   `ratio-extremality-*` files, the sampled file and `near-star-families.json`
   record no versions either. The runs predate the first commit (journal:
   "Repository revision at start: none"), so E1–E4 are labelled "Verified
   computationally" without a revision. Commands exist only in the experiments
   `README.md`. File modification times are consistent with each result having
   been produced after the last edit of its script, but that is not a recorded
   provenance.
4. **Hypothesis A(ii) is mis-stated at `n = 4`** and its evidence line
   ("order 4 to 20") covers a different index range from the statement; see
   "Quantifiers" above.
5. **Assertions not backed by a result file.** `STATE.md`: "(the star is, at
   some orders)" — no file records where the star maximises `ρ_k` (I confirmed
   one instance myself: `n = 7`, `k = 4`). "The margin is `O(1/n)` for every
   fixed near-star shape" (Remaining obstacles) is stated as fact; the evidence
   is numerical, for balanced caterpillars with spine at most 16 at four
   orders, and Q1 itself says "no proof attempted". "for even `n` it tends to
   0" is likewise an extrapolation.
6. **Budget rule.** `autoresearch.md` and `docs/research-policy.md` cap
   computation at 30 minutes unless the director approved a larger campaign in
   `STATE.md`. About 41 minutes were used; the order 21–23 run alone took
   2,014 s, so the written stopping condition ("stop at order 23") and the
   written budget were incompatible from the start. No approval is recorded.
   The overrun is disclosed in `STATE.md` and the journal.
7. **Provenance of the reference tree counts.** `distpoly.py` line 26 says the
   A000055 values are "quoted from the OEIS entry"; the journal records no
   access to OEIS (one TeX download and one web search), and the dossier lists
   tree counts as "quoted from memory". The values for orders 3–23 agree with
   the values I know; I did not fetch OEIS either.
8. **Completeness of the enumeration** for orders 11–23 rests on the count
   matching A000055 and on networkx private generators; pairwise
   non-isomorphism is tested only to order 10. The experiments `README.md` says
   this; the E1–E3 rows of `STATE.md` do not.
9. **Journal version stated as fact.** `STATE.md` ("Electron. J. Linear
   Algebra, 2018") and `research/catalogue.json` give the journal reference
   without qualification, while the dossier lists it under "Unverified items"
   (search snippet only). The catalogue's `open_status.evidence` calls the
   preprint "arXiv:1507.02341 (2018)"; the arXiv versions are dated 2015 and
   2017.
10. **Dossier `research/candidates/CJ-0001-collins-shor-peak.md` is internally
    inconsistent.** Line 11 says the statement was compared with the TeX
    source; "Unverified items" still says the statement is "the fetch tool's
    rendering … not a character-exact quotation; tie-breaking convention …
    not checked". "Open-status evidence" attributes "No more results are known
    about that conjecture" to arXiv:1507.02341, which is quoting the 2014
    survey of Aouchiche and Hansen (the project notes at the end get this
    right). "(zeros are involved)" for the Heawood example is not what the
    passage of the source I read says (it speaks of coefficients of different
    signs).
11. **Paths named in `AGENTS.md` that do not exist at this revision:**
    `research/archive/` (also in `docs/methodology.md`) and
    `research/active/CJ-0001-collins-shor-peak/reviews/` (created by this
    report).
12. Journal timing "(109 s)" for the sampled run: the per-order `seconds` in
    `ratio-extremality-sampled.json` sum to 99.5 s; `near-star-families.json`
    has no timing field for the quoted 111 s.

No use of "new" or "novel" as a claim was found in any Markdown file (search
for `novel`, `new result/theorem/lemma/proof`, `first proof`, `we prove`,
`breakthrough`). No finite verification is presented as a proof in the
"Established results" table. Relative Markdown links: 51 tracked `.md` files,
no broken link (one false positive inside a formula). `README.md`,
`research/INDEX.md` and the catalogue agree on 15 problems, the scores
80.2 / 79.2 / 78.1 and the four status fields of CJ-0001.

## Reproduction

All of the following is my own code, written from the definitions, importing
nothing from the repository (plain Python, `int` and `fractions.Fraction`;
characteristic polynomials by integer Faddeev–LeVerrier with a Cayley–Hamilton
check, determinants cross-checked by Gaussian elimination). Scripts were kept
outside the repository in the session scratch directory
(`math_check.py`, `extremal_small.py`) and are not preserved.

- `uv run python <scratch>/math_check.py` — exit status 0, "TOTAL FAILURES: 0",
  150 s. Contents: the tests listed in the Findings table, and:
  - `q(S_20) = 94/99` and `q(S(9,9)) = 10255/10791`, with `m = 10`,
    `q = d_9/d_10`, by direct `20 × 20` computation and again through my own
    implementation of L3. `10255/10791 > 94/99`. **The counterexample claim is
    confirmed.**
  - For each of the ten listed order-20 trees, `ρ_k(T) < ρ_k(S_20)` holds at
    `k = 9` and at no `k ≤ 8`; all ten have `q < 1`. Four other near-star
    trees of order 20 that I tried do not violate A(i).
  - Even orders 6–40: star `q`, best double star and its `q` agree exactly
    with every entry of `double_star_vs_star` in `near-star-families.json`;
    the first even order where a double star exceeds the star is 20; from 20
    to 40 the balanced double star is the best one and exceeds the star; all
    double stars of every order 4–40 have `q < 1`.
  - `q(S_17) ≈ 0.8341`.
  - Balanced caterpillars: `n(1−q)` for spine 1–4 at `n = 10³, 10⁴, 10⁵`
    agrees with the JSON to the printed digits; best spine 3 at `n = 100`
    (spines 1–30 scanned), 7 at `n = 1000` (1–20), 15 at `n = 10⁴` (1–22),
    and spine 33 beats 32 and 34 at `n = 10⁵`; margins `8.4496e−3`,
    `5.0968e−4`, `2.6454e−5`, `1.2905e−6`.
- `uv run python <scratch>/extremal_small.py` — my own enumeration of all
  labelled trees of order 4–7 reproduces the tree counts (2, 3, 6, 11), the
  peaks, `p_n`, and the star-minimising and path-maximising index sets of
  `ratio-extremality-04-17.json` for those orders.
- A one-off comparison of double stars with the star at
  `n = 19, 21, 23, 25, 31, 41, 42, 50, 60` (discrepancy 2).
- `uv run pytest -m "not lean" -q` — 110 passed, 11 deselected.
- `uv run python scripts/catalogue.py validate` — "15 problem(s), 0 error(s)";
  `render --check` — "research/INDEX.md is up to date".
- arXiv abstract pages 1507.02341, 2206.07561, 2103.00647, 2104.14516 fetched:
  titles, authors and dates agree with the dossier. No journal reference was
  visible in what I extracted.

**Not checked.** Lean, `lake`, `scripts/verify_lean.py` and the tests marked
`lean` (not run, by instruction). The exhaustive runs were not repeated: E1–E4,
"exactly 10" violators at order 20, the order-13 tie and the A(ii) counts were
compared with the JSON files only, apart from my enumeration of orders 4–7.
The sampled run was not repeated. Values at `n = 10⁶` and the best spine
outside the ranges stated above were not recomputed. Collins (1989),
Graham–Lovász (1978), Graham–Pollak and Edelberg–Garey–Graham were not read.
No novelty search was made. Of the documents in Part C, `AGENTS.md`,
`README.md`, `autoresearch.md`, `docs/verification-policy.md`,
`research/scouting-log.md`, `research/INDEX.md`, the CJ-0001 dossier and the
journal were read in full; `docs/methodology.md`, `docs/research-policy.md`,
the learning guide and the dossiers CJ-0002, CJ-0004, CJ-0007 only in part;
`docs/publication-policy.md`, `docs/attribution-policy.md` and
`docs/learning-guide.md` not at all. The literature claims of the scouting log
and of the other dossiers were not verified.

## Verdict

| Item | Verdict |
| --- | --- |
| R1 | `no gap found within stated scope` (state the first claim for a general index) |
| L1 | `no gap found within stated scope` |
| L2 | `no gap found within stated scope` (formula already in the source) |
| L3 | `no gap found within stated scope` |
| Counterexample to Hypothesis A(i) at order 20 | confirmed by independent exact computation |
| Claims versus evidence in `STATE.md` (Part B) | `gap found` — discrepancies 1, 2, 4, 5 |
| Repository consistency (Part C) | `gap found` — discrepancies 3, 6–12 |
| **Overall** | `gap found`, in the description of evidence and in one hypothesis statement; not in the proofs of R1, L1, L2, L3 |

Scope: the proofs as written in `notes/lemmas.md`, tested on the finite sets of
trees listed above, and the numerical claims of three sections of `STATE.md`
compared with the result files. The verdict does not cover the correctness of
the cited theorems, the completeness of the exhaustive enumerations, novelty,
or any formalization. This review applies only to revision
`e34acfc0bf363fc5c340a7f1611ad0b67c53788d`.
