# CJ-0001 — journal

Append-only. One entry per session. Current truth is in `STATE.md`.

## Session 1 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`, in Claude Code. No human
  mathematical input during the session; the session was started by the project
  director's initialization request.
- **Role(s):** Research Director, Literature Auditor (statement only),
  Computational Experimenter, Mathematical Researcher.
- **Repository revision at start:** none (the session created the repository).
- **Objective (exact):** (1) fix the exact statement of the Collins–Shor
  conjecture from a primary source; (2) reproduce the published exhaustive
  verification for trees of order at most 20 with exact arithmetic and an
  independent check; (3) extend it beyond order 20; (4) look for structure that
  suggests a provable intermediate statement, and try to break whatever is found.
- **Approach:** exact integer characteristic polynomials of distance matrices
  over all trees of each order; comparison of every tree with the star and the
  path; exact formulas for structured families at large orders.
- **Falsification test:** any tree with a maximizing index outside
  `[⌊n/2⌋, ⌈n − n/√5⌉]`; and, for each sharper hypothesis, sampled and structured
  trees beyond the exhaustive range.
- **Stopping conditions:** stop the exhaustive search at order 23; stop the
  session once the state is recorded with a concrete next objective.
- **Budget:** 30 minutes of computation; one session.

### What was done

All computations use exact integer or rational arithmetic. Commands are run from
the repository root with `uv run python`.

1. Statement: downloaded the TeX source of arXiv:1507.02341 and read
   Conjecture 1.2 and its context. One web search for later work.
2. `tests/test_cj0001_distpoly.py`: 87 tests pass — tree counts against OEIS
   A000055 (orders 1–12), pairwise non-isomorphism by an independent canonical
   form (orders 2–10), agreement of the main computation with an independent
   Laplacian-based method on every tree of order 3–9, Graham–Pollak and the
   formula for `d_{n−2}` on every tree of order 3–11, the star's peak for orders
   3–40, the `d_1` formula, and the order-20 refutation by both methods.
3. `exhaustive.py --min-order 3 --max-order 20 --workers 7`: 1,346,022 trees,
   0 violations, 0 guard failures, counts match (90 s).
4. `exhaustive.py --min-order 21 --max-order 23 --workers 7`: 22,596,335 trees,
   0 violations, 0 guard failures, counts match (2,014 s).
5. `ratio_extremality.py exhaustive` for orders 4–17 and 18–20: Hypothesis A(ii)
   holds on all 1,346,021 trees; Hypothesis A(i) holds through order 19 and
   fails for 10 trees of order 20 (109 s in total).
6. `ratio_extremality.py sampled --orders 24 30 40 60 90 --samples 400 --seed
   20261126`: 10,000 trees; 0 violations of A(ii) and of the conjecture; 108
   violations of A(i), all in the caterpillar and preferential-attachment
   models (109 s).
7. `near_star_families.py`: double stars against the star for even orders
   6–40; balanced caterpillars at orders 10³ to 10⁶ through the quotient-matrix
   formula (111 s).

### Findings

See `STATE.md` for the precise statements and evidence levels: E1–E4 (exhaustive
verification through order 23), R1 and L1–L3 (short proofs, unreviewed),
Hypothesis A(ii) (open, supported), Hypothesis A(i) (refuted at order 20 by the
double star `S(9,9)`), Questions Q1 and Q2.

### What failed

- Hypothesis A(i): refuted (recorded in `STATE.md`).
- A first version of `near_star_families.py` used full binomial coefficients and
  did not finish at order 10⁶ within ten minutes; it was stopped and rewritten
  with exact binomial ratios. No result of the first version was used.
- The 30-minute computation budget was exceeded: about 41 minutes of recorded
  computation, because the order-23 run (23 minutes) was allowed to finish.
- Not done: reading Collins (1989) and Graham–Lovász (1978); any independent
  review; any formalization.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` |
| Computation wall-clock | about 2,430 s recorded by the scripts (7 worker processes for the exhaustive runs; Intel Core i7-7700, 16 GB RAM, Windows 10) |
| Token usage | unavailable (not reported to the agent for the main session) |
| Research iterations | 1 session |
| Proof attempts | 4 short lemmas written (R1, L1, L2, L3); none reviewed |
| Counterexamples found | 0 to the conjecture; 1 family refuting Hypothesis A(i) |
| Formalization attempts | 0 |
| Successful verifications | 87 tests; 2 exhaustive runs; cross-check by an independent method |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable contributions: reproducible exhaustive verification through order 23;
a refuted natural hypothesis with an explicit counterexample; an open sharper
hypothesis for the upper bound; a concrete provable-looking objective (O1 in
`STATE.md`: the lower bound for double stars), to be preceded by a literature
audit of Collins (1989) and arXiv:2206.07561.

## Session 1, addendum — 2026-11-26 — independent review and corrections

- **Agent / model:** reviewer: Claude, model `claude-fable-5-2`, launched as a
  fresh context that received the file paths and a checklist but not the
  reasoning of the author; corrections: the author agent (same model).
- **Objective:** obtain an adversarial review of `notes/lemmas.md` and of the
  claims in `STATE.md` at revision `e34acfc`, and correct what it finds.

### What was done

1. Review report: `reviews/2026-11-26-claude-fable-5-2.md`. Verdict for R1, L1,
   L2, L3: no gap found within stated scope. The reviewer re-derived the
   Graham–Lovász inverse formula, recomputed the order-20 counterexample with
   its own code, and matched every number in `STATE.md` against the result
   files. It did not rerun the exhaustive experiments, did not check Collins
   (1989) or Graham–Lovász (1978), and did not assess novelty.
2. Discrepancies reported and the response to each:
   - L3 was validated on one ratio only → now validated on every coefficient,
     ten caterpillars, with a test.
   - "The star is not extremal once n ≥ 20" overstated the evidence → double
     stars now compared with the star at every order 6–41; wording corrected
     (even orders 20–40 and odd orders 29–41).
   - Result files lacked command, revision and versions → a `run` block is now
     written by every script; five files regenerated at `ed232ec` with
     identical numbers. `exhaustive-21-23.json` was not regenerated (34
     minutes) and is flagged as an open obligation.
   - Hypothesis A(ii) had an undefined index at n = 4 → range stated as
     `0 ≤ k ≤ min(p_n, n−3)`.
   - Two statements had no result file behind them → reworded to what the
     files show.
   - The budget overrun had no recorded approval → stated as the decision of
     the agent, for review by the director.
   - The OEIS reference values had not been checked against OEIS → compared
     with the OEIS b-file of A000055 on 2026-11-26 (identical for n = 0..25).
   - The journal reference of the source was unverified → marked as such in
     the catalogue, the dossier and `STATE.md`.
   - The dossier contradicted itself about the statement check and
     misattributed a quotation → corrections added to the dossier.
   - `AGENTS.md` named directories that did not exist → wording corrected.
   - The formula of L2 is already in the source → L2 marked as known.
   - R1 was restated in a general form, as the reviewer suggested. The restated
     version has not been re-reviewed.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author and reviewer) |
| Reviewer usage reported by the environment | 208,254 subagent tokens, 30 tool calls, about 13 minutes |
| Computation wall-clock for the regenerated files | about 6 minutes |
| Token usage of the main session | unavailable |

### Outcome

No mathematical error was found. Several statements were more confident than
their evidence and have been corrected. The catalogue status remains
`not-reviewed`: one same-model AI review of an earlier revision does not meet
the bar for `ai-reviewed` on a revision that was edited afterwards.

## Session 2 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`, in Claude Code. The
  session followed a request of the project director to extend the repository
  (registry of contributions, exploration mode, project summary) and then to
  return to research. No human mathematical input.
- **Mode:** focused work.
- **Role(s):** Research Director, Mathematical Researcher, Computational
  Experimenter; Literature Auditor as a separate subagent (same model).
- **Repository revision at start:** `c31fdb2` (branch `research`).
- **Objective (exact):** O1 of `STATE.md`. For all integers `a, b ≥ 1`, with
  `n = a + b + 2` and `m = ⌊n/2⌋`: `d_{m−1}(S(a,b)) < d_m(S(a,b))`, where
  `S(a,b)` is the double star. By R1 this is the lower bound of the
  Collins–Shor conjecture for double stars.
- **Approach:** L3 with spine length 2 gives `d_k = Σ_j g_j(a,b) C(n−4, k−j)`
  with `g_j` read from a `4 × 4` determinant. The determinant is affine in each
  of `a` and `b`, so for fixed `n` the difference `d_m − d_{m−1}` is affine in
  `t = ab`; positivity then has to be checked only at the two ends of the range
  of `t`, where it is a statement about one-variable polynomials.
- **Falsification test:** the closed formula must reproduce the exact
  coefficients of the direct `n × n` computation before any proof is attempted;
  a single double star with `d_{m−1} ≥ d_m` refutes the objective (none exists
  for `n ≤ 23` by E1 and E2).
- **Stopping conditions:** done when a written proof exists, the formula is
  cross-checked exactly for all `a + b ≤ 200`, and an independent review has
  been requested. Stop if the formula disagrees with the direct computation or
  positivity fails on an infinite range.
- **Budget:** 60 minutes of agent work; at most 10 minutes of computation; the
  literature audit at most 25 minutes.
- **Deferred obligation:** the rerun of orders 21 to 23 (obligation 3, about 34
  minutes) exceeds the default computation budget and waits for the director's
  approval. MD-0001 stays `partial-result` until then.

### What was done

Before the research, in the same working session and at the director's
request: the registry of contributions, the exploration mode and the generated
summary were added (commits `1a11982`, `48b94fe`, merged in `6e2583a`), and
five findings of session 1 were registered as MD-0001 to MD-0005 (`c31fdb2`).
The local identifiers were not changed.

All computations are exact. Commands are run from the repository root with
`uv run python`.

1. **Literature audit** (separate agent context, `literature-auditor`). Read in
   full: arXiv:1507.02341v3, arXiv:2206.07561v1, arXiv:2407.03309v1. Read in
   part: arXiv:2103.00647 (pp. 5–12), Graham–Lovász 1978 (pp. 60–67, 80–86, a
   scan). Not accessible: Collins (1989) and her thesis. Nine web queries, two
   citation lists. The record is in the dossier.
2. **Symbolic determinant.** The `4 × 4` quotient determinant of the double
   star, with python-flint multivariate polynomials, gives
   `g_0 = s+1`, `g_1 = 2t+6s+2`, `g_2 = 5t+9s−3`, `g_3 = 4s−8`, `g_4 = −4`
   (`s = a+b`, `t = ab`).
3. **Proof.** Written by hand in `notes/double-stars.md`: Lemma D1, two closed
   forms for `d_m − d_{m−1}`, a sign argument for `d_{m+1} − d_m`, conclusion by
   log-concavity.
4. **Falsification test and cross-check.**
   `double_stars.py --out results/double-stars.json`, at revision `241dc03` on a
   clean tree: the symbolic determinant agrees with the stated polynomials; for
   all 10,000 double stars with `a + b ≤ 200` the closed forms, both
   inequalities and the uniqueness of the peak hold; the whole sequence agrees
   with the direct `n × n` determinant on 404 double stars; the star formulas
   hold for orders 3 to 202. 0 failures. 55.5 s.
5. `uv run pytest tests/test_cj0001_distpoly.py`: 96 passed (one new test).
6. **Independent review** of revision `5e5ef14` by a fresh context
   (`adversarial-reviewer`, same model): report
   `reviews/2026-11-26-claude-fable-5-2-T1.md`.

### Findings

- **T1 (candidate proof; registered as MD-0006).** For every double star
  `S(a,b)`, `a, b ≥ 1`: `d_{m−1} < d_m`, and `d_{m+1} < d_m` when the index
  exists, with `m = ⌊n/2⌋`. So the peak is exactly `⌊n/2⌋` and the Collins–Shor
  conjecture holds for trees of diameter 3. The objective O1 asked only for
  the first inequality. Review: no gap found within stated scope; the reviewer
  recomputed the coefficients from the definition on 129 double stars with its
  own code and found no counterexample among 562,500 double stars with
  `a + b ≤ 1500`. This is an AI review by the same model family, not a human
  review. Novelty: no earlier statement found within a bounded search; Collins
  (1989) is unread.
- **L1 is known** (registry record MD-0002 set to `previously-resolved`): it is
  a rewriting of Graham–Lovász 1978, eqs. (10)–(12). The inverse formula quoted
  from memory in session 1 is their Lemma 1, p. 66.
- **L3 is known** (MD-0003 set to `previously-resolved`): a direct special case
  of Theorem 3.3 of Hogben–Reinhart, arXiv:2103.00647.
- A subforest formula for every `δ_k` exists (Graham–Lovász, Theorem at
  eq. (42)); the "formula for `d_2`" that session 1 planned to derive does not
  need deriving.
- In the sources read, the peak is located only for stars and paths, and the
  only published exhaustive verification is for order at most 20.

### What failed

- Nothing mathematical failed in this session, which is itself a reason for
  caution: T1 came out in one pass, and its only review shares the author's
  model.
- The review found eight minor defects in the notes (incomplete dependency
  list; two unproved asides; notation used with two meanings; one check
  described as "agreement" that is only proportionality). They are listed in
  `STATE.md`, obligation 2. The notes were left unchanged so that the review
  still applies to the text as it stands.
- Collins (1989) could not be obtained. The claim about trees of diameter at
  most 3 therefore still rests on a second-hand report for stars.
- Not done: the rerun of orders 21 to 23; any formalization; a comparison with
  Table II of Graham–Lovász.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author, auditor and reviewer; three separate contexts) |
| Computation wall-clock | about 2 minutes for the research (two runs of `double_stars.py`, 60 s and 55.5 s); the Lean verification for the infrastructure change took 5 minutes; the full test suite 254 s |
| Literature audit, as reported by the environment | 165,602 subagent tokens, 48 tool calls, about 6 minutes |
| Review, as reported by the environment | 101,892 subagent tokens, 21 tool calls, about 9 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective, 1 approach |
| Proof attempts | 1 (T1), reviewed once |
| Counterexamples found | 0 |
| Formalization attempts | 0 |
| Successful verifications | 96 tests; 10,000 double stars and 200 stars checked exactly; independent recomputation by the reviewer |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable: a candidate proof of the Collins–Shor conjecture for double stars
with an independent AI review and an exact cross-check; a literature audit that
reclassified two tools as known. The catalogue status of CJ-0001 is unchanged
(`active-investigation`): promotion is not decided in the session that
produced the claim. Next: objective O2 in `STATE.md` (caterpillars with spine
length 3), after or together with the open obligations listed there.

## Session 3 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`. Director's instruction
  for the session: after the profile-integration task (commit `98ab52d`),
  "return to mathematical research".
- **Mode:** focused work.
- **Role(s):** research director, mathematical researcher, computational
  experimenter. Review, if a claim results, by a fresh context.
- **Repository revision at start:** `98ab52d` (branch `research`, clean tree).
- **Objective (exact):** O2 of `STATE.md`. For all integers
  `c_1, c_2, c_3 ≥ 1`, let `T` be the caterpillar whose spine is a path on
  three vertices carrying `c_1, c_2, c_3` pendant leaves, `n = 3 + c_1 + c_2 + c_3`,
  `m = ⌊n/2⌋`. Decide whether `d_{m−1}(T) < d_m(T)`, and whether
  `d_{m+1}(T) < d_m(T)`; in every case locate all maximizing indices and
  compare them with `[⌊n/2⌋, ⌈n − n/√5⌉]`.
- **Approach:** as for T1. L3 with `s = 3` gives
  `d_k = Σ_{j=0}^{6} g_j C(n−6, k−j)` with `g_j` polynomial in the `c_i`
  (affine in each). Compute the `g_j` symbolically; reduce `d_m − d_{m−1}` for
  each parity to a positive binomial times a polynomial in `m` and the `c_i`;
  prove positivity on `c_i ≥ 1`. Then the same for `d_{m+1} − d_m`.
- **Falsification test (run first):** exact evaluation of the whole sequence
  for every `(c_1, c_2, c_3)` with sum at most 300; a non-positive
  `d_m − d_{m−1}` would refute the conjecture, and a peak other than `m`
  changes the statement to be proved.
- **Stopping conditions:** done when both differences are reduced to explicit
  polynomials whose signs are settled by a written argument and cross-checked
  exactly, or when the peak is shown to depend on the `c_i` in a way that is
  then described exactly. Stop without a claim if positivity does not follow
  from a short argument within the budget; record the polynomial.
- **Budget:** about 60 minutes of agent work; computation at most 15 minutes
  of wall-clock time, largest instance `c_1 + c_2 + c_3 = 300` (closed form)
  and order 63 (direct determinant); one review subagent if a candidate proof
  results.
- **Deferred obligations:** the open obligations 1 to 7 of `STATE.md` are not
  addressed. Obligations 1, 2 and 4 need a human reader, an inaccessible paper
  or the director's approval of a budget; O2 does not depend on any of them
  except through L3 (known, Hogben–Reinhart) and Theorem 2.1 of the source.

### What was done

All computations are exact (integers, rationals, integer polynomials).

1. Exploratory scripts (scratch directory, not kept): symbolic expansion of
   the `6 × 6` quotient determinant with python-flint; the four differences
   as polynomials in `m, a, c`; rewriting in `u = a + c`, `v = ac`; factoring.
2. Falsification test, run before any proof: every `K(a,b,c)` with
   `a + b + c ≤ 300` (`a ≤ c`), 2,238,725 trees, coefficients from the closed
   form at the indices `m−1, …, m+2`. Result: `d_{m−1} < d_m > d_{m+1}` in every
   case, no tie. 209.4 s.
3. Proof written: `notes/spine3.md` (Theorem T2). Committed with
   `experiments/CJ-0001-collins-shor-peak/spine3.py` and
   `test_spine3_closed_forms_and_peak` as `74cb5bb`.
4. `uv run python experiments/CJ-0001-collins-shor-peak/spine3.py --out …/results/spine3.json`
   on the clean tree at `74cb5bb`: symbolic derivation agrees with the stated
   forms; sign conditions for `3 ≤ m ≤ 2000`; 2,238,725 trees, 0 failures;
   17,545 whole sequences; 621 direct determinants. 356.7 s.
5. Independent review of `74cb5bb` by the `adversarial-reviewer` subagent run
   on `claude-opus-5-5` (fresh context; it was given the paths, the revision,
   the source reference and the checklist, and not the reasoning):
   `reviews/2026-11-26-claude-opus-5-5-T2.md`.
6. One-off exploratory check of `b = 0` (direct determinant, 169 trees with
   `a + c ≤ 26`), to choose the next step. Script not kept.
7. `uv run pytest`, `scripts/catalogue.py validate` and `render`: results in
   the commit that contains this entry.

### Findings

- **T2 (candidate proof, AI-reviewed, registered as MD-0007).** For
  `a, b, c ≥ 1`, the only maximizing index of `K(a,b,c)` is `⌊n/2⌋`; the
  conjecture holds for these trees. Written proof with two computer-assisted
  polynomial identities; exact finite checks; review verdict "no gap found
  within stated scope", the reviewer having recomputed both identities with
  its own code from distance matrices. Not read by a mathematician. Novelty:
  nothing found in a small bounded search; no dedicated literature audit.
- Structure: each difference is a positive factor times `vK + R` with `K > 0`,
  so for fixed `m, u` the minimum is at `v = u − 1`; `(u−1)K + R` is concave
  in `u`, so the minimum over the family is at `K(1, n−5, 1)` or `K(1, 1, n−5)`.
- Observation (exact, exploratory, script not kept): for `K(a,0,c)` with
  `a + c ≤ 26` the only maximizing index is `⌊n/2⌋`.
- Observation (exact, from `results/spine3.json`): the smallest relative margin
  among even orders with `a + b + c ≤ 300` is `≈ 0.002386` at `K(59,180,60)`.

### What failed

- Nothing mathematical failed. As in session 2 the proof came out in one pass,
  which is a reason for caution, not for confidence; this time the review was
  done by a different model, of the same vendor.
- The review found eight defects of record and presentation (D1 to D8),
  listed in `STATE.md`, obligation 8. Two were the author's wording errors in
  the notes (D5, D6), one an undeclared limitation of the finite checks (D3),
  one a title broader than the theorem (D4). The brief given to the reviewer
  misquoted the title of arXiv:1507.02341 (D8); the commit subject of
  `74cb5bb` overstates the scope. The notes were left unchanged so that the
  review applies to them as they stand.
- Not done: any literature audit for this statement; the open obligations 1
  to 7; the extension to `b = 0`; anything uniform in the spine length.
- Budget: the session exceeded the planned 60 minutes of agent work, mostly
  because the review ran for about 15 minutes; the exact duration was not
  measured. Computation stayed within the 15 minutes planned.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author); `claude-opus-5-5` (reviewer, separate context) |
| Computation wall-clock | about 10 minutes for the research (209.4 s falsification scan, 356.7 s full run, short trial runs); the full test suite about 4 minutes per run |
| Review, as reported by the environment | 164,439 subagent tokens, 47 tool calls, about 15 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective, 1 approach |
| Proof attempts | 1 (T2), reviewed once |
| Counterexamples found | 0 |
| Formalization attempts | 0 |
| Successful verifications | 97 tests in `tests/test_cj0001_distpoly.py`; 2,238,725 caterpillars checked exactly; independent recomputation by the reviewer |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable: a candidate proof of the Collins–Shor conjecture for the caterpillars
`K(a,b,c)` with `a, b, c ≥ 1`, with an exact cross-check and an independent AI
review by a different model; registry record MD-0007. The catalogue status of
CJ-0001 is unchanged (`active-investigation`). Next: objective O3 in
`STATE.md` (the case `b = 0`, which would complete the caterpillars of
diameter 4), together with the corrections of obligation 8.

## Session 4 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`. Director's instructions
  of 2026-11-26 for this session: keep MD-0006 and MD-0007 as candidate
  theorems; correct the presentation defects and publish (done before this
  entry: commits `1c38662`, `30fc1e1`, promotion `dc84a3a` on `main`, merge
  `cda133c`, both branches pushed); continue with O3; explore whether the
  identities and positivity arguments for short spines suggest a framework for
  arbitrary spine length; formalize progressively; respect budgets.
- **Mode:** focused work on O3, then exploration (general spine length). The
  two parts are recorded separately below.
- **Role(s):** research director, mathematical researcher, computational
  experimenter. Review of the O3 claim by a fresh context; one formalization
  subagent.
- **Repository revision at start:** `cda133c` (branch `research`, clean tree).
- **Objective (exact), focused part:** O3 of `STATE.md`. For all integers
  `a, c ≥ 1` with `a + c ≥ 3`, let `K(a,0,c)` be the caterpillar with spine
  `v_1 v_2 v_3` in which `v_1`, `v_3` carry `a`, `c` pendant leaves and `v_2`
  none, `n = a + c + 3`, `m = ⌊n/2⌋`. Decide whether `d_{m−1} < d_m` and
  `d_{m+1} < d_m`.
- **Approach:** as planned in `STATE.md`: show that the formula of Lemma C1 of
  `notes/spine3.md` stays valid at `b = 0` for `n ≥ 6`; the identities of
  Lemma C2 then hold with `u = n − 3`; check `K > 0` and `H > 0` there.
- **Falsification test (run first):** closed form at `b = 0` against the direct
  determinant for `a + c ≤ 40`, with the location of every maximizing index.
- **Stopping conditions:** done when the four values `H(m, n−3)` are explicit
  polynomials with a written sign argument, cross-checked exactly; stop without
  a claim if the formula at `b = 0` disagrees with the direct determinant.
- **What is explored, exploration part:** for a caterpillar with `s` spine
  vertices and a fixed order, `d_m − d_{m−1}` is multi-affine in the leaf
  numbers; is there a sign pattern in its mixed second partials that explains
  the reductions used for `s = 2` and `s = 3` and survives for larger `s`?
- **Budget:** about 60 minutes of agent work for the two parts together;
  computation at most 15 minutes of wall-clock time (largest instances:
  `a + c = 600` by closed form, order 43 by direct determinant, spines of at
  most 8 vertices and orders at most 200 for the exploration); one review
  subagent for the O3 claim; one formalization subagent limited to one lemma
  (the general form of R1), about 25 minutes and 8 builds.
- **Order of work, as it happened:** the exploratory computations for both
  parts were made in a scratch directory while an independent recheck of the
  revised notes was running and the working tree had to stay unchanged; this
  header was written into the journal after those computations and before the
  files of the session were added. The plan for O3 is the one recorded in
  `STATE.md` at the end of session 3.
- **Deferred obligations:** obligations 1, 3, 4, 5 and 7 of `STATE.md` are not
  addressed (obligation 7, formalization, only by the one lemma above).

### What was done

All computations are exact (integers and integer polynomials).

Before the research (same day, recorded here because it changed files of the
investigation): the presentation defects found by the reviews of T1 and T2 were
corrected (`1c38662`); an independent recheck of that revision by
`claude-opus-5-5` found no change to the mathematics, both earlier verdicts
still applicable, and several wrong or loose new sentences, which were
corrected (`30fc1e1`); the infrastructure was promoted to `main` (`dc84a3a`,
receipt `f7cca69`), `main` was merged back (`cda133c`), and both branches were
pushed with the director's authorization.

Focused part (O3):

1. Falsification test: the formula of Lemma C1 at `b = 0` against the direct
   determinant, with the location of the maximum, for all 399 trees with
   `3 ≤ a + c ≤ 40`: equal, maximum at `⌊n/2⌋` only. `H(m, n−3)` computed
   symbolically in the four cases: positive coefficients in `t = m − 3`.
2. Proof written: `notes/diameter4-caterpillars.md` (Theorem T3, Lemma C1′,
   corollary). Script `diameter4.py`, test
   `test_diameter4_caterpillars_without_central_leaf`. Committed as `d2eb9ac`.
3. `diameter4.py` on the clean tree at `d1d6d7c`: 89,999 trees with
   `a + c ≤ 600`, 0 failures; 402 direct determinants; 31.0 s.
4. Independent review of `d2eb9ac` by the `adversarial-reviewer` subagent on
   `claude-opus-5-5`: `reviews/2026-11-26-claude-opus-5-5-T3.md`.

Exploration part (general spine length):

5. `mixed_partials.py`: the `g_j` for `2 ≤ s ≤ 8` by interpolation, validated
   against the direct determinant (9, 35, 139, 555, 258, 753 and 2,208 small
   caterpillars for `s = 2, …, 8`, empty inner classes included); the
   certificate for the mixed second partials of `d_m − d_{m−1}` for every
   order from `2s` to 200, on both domains; the values at the vertices of each
   slice; the same for `d_m − d_{m+1}`. Clean tree at `d1d6d7c`, 45.7 s.
6. `mixed_partials_s3.py`: for three spine vertices, the mixed partials and the
   vertex values as polynomials in `m`.
7. One inline computation, then added to `mixed_partials.py` and to the tests:
   in which `g_j` the product of all leaf numbers occurs.
8. Notes: `notes/vertex-principle.md`.

Formalization:

9. `formalization-agent` subagent (model `claude-fable-5-2`): the general form
   of R1 in Lean, `Conjectura/Research/CollinsShorPeak/LogConcavePeak.lean`,
   four theorems registered. Its report: about 14 minutes, 2 pipeline runs and
   the Lean test suite; all proofs compiled on the first attempt.
10. `uv run python scripts/verify_lean.py` on the clean tree at `abe4a38`:
    all six checks passed, the new module replayed by the kernel; receipt
    `verification/receipts/20261126T103507Z-abe4a38f30-passed.json`.
11. `uv run pytest`, `scripts/catalogue.py validate` and `render`: results in
    the commit that contains this entry.

### Findings

- **T3 (candidate proof, AI-reviewed, MD-0008).** For `a, c ≥ 1`, `a + c ≥ 3`,
  the only maximizing index of `K(a,0,c)` is `⌊n/2⌋`. Review verdict "no gap
  found within stated scope"; the reviewer rebuilt Lemma C1′ by hand and
  recomputed the identities at `b = 0` with its own code. With T2 and `P_5`:
  every caterpillar of diameter 4, conditional on T2. Not read by a
  mathematician; no literature audit.
- **L4 (proved here, unreviewed).** The vertex principle for multi-affine
  functions with non-negative mixed second partials.
- **Hypothesis V (conjecture, MD-0009).** Non-negativity of the mixed second
  partials of `D_n`. Exact evidence: certificate with 0 failures for
  `2 ≤ s ≤ 8`, orders up to 200. For `s = 3` and every order it is an explicit
  computer-assisted identity (unreviewed), which with L4 reproduces the lower
  inequalities of T2 and T3.
- **Observation, uniform in `s`.** For `2 ≤ s ≤ 8` the product `c_1 ⋯ c_s`
  occurs only in `g_{s−1}` and `g_s`, with coefficients `s` and `s + 3`; its
  coefficient in `D_n` is then `3·C(2k,k)/(k+1)` (even order) or
  `(2s+6)·C(2k+1,k+1)/(k+2)` (odd order), `k = m − s`.
- **The upper difference does not follow the pattern**: certificate failures
  from `s = 4`, and vertex trees with `d_{m+1} ≥ d_m` from `s = 6`.
- **Lean.** The general form of R1 is formally proved (axioms: `propext`,
  `Classical.choice`, `Quot.sound`). It is a lemma about sequences.

### What failed

- The first revision of the notes of T1 and T2 introduced new errors (a false
  statement about where a phrase is used, a wrong count, an inaccurate
  description of a check), found by the recheck. A revision made to correct
  presentation needs the same care as the proof.
- `results/diameter4.json` and `results/mixed-partials.json` were first
  produced on an unclean tree (another agent's uncommitted files, and one of
  the two result files itself); they were discarded and produced again at
  `d1d6d7c`. The reviewer of T3 saw the discarded copy and recorded it (E2).
- The first version of `mixed_partials.py` validated the closed form for
  `s = 8` on a single tree; widened to 2,208 before the result file was made.
- The review of T3 found six defects of record and presentation (E1 to E6),
  listed in `STATE.md`, obligation 9. The notes are left as reviewed.
- Push events do not start the CI workflow on this repository; the runs
  inspected after the publication were started by hand (`workflow_dispatch`).
- `STATE.md` is now about 480 lines, above the 400 it aims for. It needs
  compacting (the long obligations could move to a note).
- Not done: the hand derivation or review of the `s = 3` identities; `s = 4`;
  any proof of the top-coefficient pattern; a literature audit; obligations 1,
  3, 4 and 5.
- Budget: the work of this entry, with the publication tasks before it,
  exceeded 60 minutes of agent time by a wide margin (three review or recheck
  subagents of about 15 minutes each, one formalization subagent of 14
  minutes, two full Lean verifications and three full test runs); the
  duration was not measured. Research computation stayed under 5 minutes.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author, formalization subagent); `claude-opus-5-5` (recheck and review, separate contexts) |
| Computation wall-clock | research: about 3 minutes (45.7 s and 31.0 s for the result files, repeated once; short trial runs); Lean verification about 5 minutes per run (two runs); full test suite 6 to 7 minutes per run |
| Recheck of T1 and T2, as reported by the environment | 199,837 subagent tokens, 48 tool calls, about 17 minutes |
| Review of T3, as reported by the environment | 181,173 subagent tokens, 41 tool calls, about 14 minutes |
| Formalization, as reported by the environment | 73,115 subagent tokens, 27 tool calls, about 15 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective (O3), 1 approach; 1 exploration |
| Proof attempts | 1 (T3), reviewed once; L4 (unreviewed) |
| Counterexamples found | 0 |
| Formalization attempts | 1 (general form of R1), successful |
| Successful verifications | 100 tests in `tests/test_cj0001_distpoly.py`; 89,999 trees `K(a,0,c)` checked exactly; the certificate for 7 spine lengths and orders up to 200; independent recomputation by the reviewer; Lean pipeline passed with receipt |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable: a candidate proof for the caterpillars `K(a,0,c)` with an independent
AI review (MD-0008), which with T2 covers every caterpillar of diameter 4; a
mechanism that explains the three proofs obtained so far and is supported by
exact computation for up to eight spine vertices (Lemma L4 and Hypothesis V,
MD-0009); one statement of the same form for every spine length (the top
coefficient, an observation); and the first Lean lemma of the investigation.
The mathematical status of CJ-0001 is unchanged (`active-investigation`); its
formal status is `partial`, with the scope stated in `STATE.md`. Next:
objective O4 in `STATE.md` (four spine vertices), after or together with the
obligations 8 to 10.

## Session 5 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2`. Director's instructions
  for the session: prioritize Hypothesis V (MD-0009) and what it could give for
  every spine length — validity of the extremal reduction under the fixed-order
  constraint, a general positivity argument for the mixed second partials, the
  coefficient of the product of all leaf counts, the standalone value of the
  reduction, a mechanism for the upper bound; use O4 as a tool, not as a goal;
  formalize the reduction when it stabilizes; check the literature for T1 to T3
  and for the framework; keep MD-0006 to MD-0008 as candidates; compact
  `STATE.md`; the CI question only if the budget permits. Publication of
  `research` (not `main`) authorized for the commits up to `ef98710` and for
  the verified commits of this session.
- **Mode:** exploration aimed at a general mechanism, with focused work on any
  statement that becomes exact during the session.
- **Role(s):** research director, mathematical researcher, computational
  experimenter; one literature-auditor subagent and one formalization
  subagent. No adversarial review is planned inside this budget: what the
  session proves is recorded as unreviewed.
- **Repository revision at start:** `ef98710` (branch `research`, clean tree,
  pushed at the start of the session).
- **What is explored:** the structure of the polynomials `g_j` for a tree made
  of a skeleton with pendant leaves — why the product of all leaf counts has
  the coefficients `s` and `s + 3`, and whether the same computation describes
  the other coefficients and applies to skeletons that are not paths.
- **Falsification tests:** every identity derived by hand is compared with
  exact computation on all skeleton trees with few vertices before it is
  written down; Hypothesis V is tested on skeletons that are not paths.
- **Stopping conditions:** stop the mathematics at 11:42 UTC whatever its
  state, to leave time for records, verification and the compaction of
  `STATE.md`.
- **Budget (binding, set by the director):** 60 minutes of wall-clock time
  from 11:04 UTC to the last commit, subagents, verification and records
  included; the subagents are limited to 12 and 14 minutes and run
  concurrently. Computation at most 5 minutes.
- **Deferred obligations:** obligations 8 to 10 of `STATE.md` (revision and
  recheck of the notes, review of L4 and of the `s = 3` identities) are not
  addressed, except that the literature audit bears on obligations 1, 8 and 9
  and the formalization on obligation 10.

### What was done

All computations are exact (integers, rationals, integer polynomials).

1. `research` pushed at the start (`ef98710`), with the director's
   authorization; CI dispatched by hand on that head.
2. `skeleton_structure.py`, written in this session: for a skeleton tree `S`
   and leaf numbers `c`, the polynomials `g_j` by interpolation; Lemma S1
   against direct determinants; Proposition S2 at more rational points than
   the degree; Proposition S3; the certificate of `mixed_partials.py` on
   `c ≥ 0`; Property Γ; the one-vertex formula; locality. Runs: every tree
   with at most 5, 6 and 7 vertices while the statements were being found
   (2 s, 4 s, 28 s and 18 s); every tree with at most 8 vertices and orders up
   to 100 (186 s, on an unclean tree, kept only as a trial); and the run of
   the result file, on the clean tree at `7c1a9dd`, with orders up to 40.
3. Notes: `notes/skeleton-identity.md` (Lemma S1, Propositions S2 to S4,
   Property Γ, Corollary S5, two observations, remarks).
4. `literature-auditor` subagent (model `claude-fable-5-2`, separate context):
   6 searches, 6 fetches, 2 failed; section "Literature audit 2026-11-26
   (session 5)" of the dossier.
5. `formalization-agent` subagent (model `claude-fable-5-2`):
   `Conjectura/Research/CollinsShorPeak/ExtremalReduction.lean`, two theorems
   registered.
6. `uv run python scripts/verify_lean.py` on the clean tree at `7c1a9dd`;
   `uv run pytest`; `scripts/catalogue.py validate` and `render`: results in
   the commit that contains this entry.
7. `STATE.md` compacted; the obligations as they stood are in
   `notes/obligations.md`.

### Findings

Answers to the director's five questions, each with its level of evidence.

- **Is the extremal reduction valid under the fixed-order constraint?** Yes,
  as stated in Lemma L4: the moves `c → c ± (e_i − e_k)` keep the sum, hence
  the order, and the hypothesis on the mixed partials is needed only at
  integer points of the slice. Proved by hand (session 4), unreviewed; its
  discrete core — concavity on an integer interval and the exchange step for
  two coordinates — is now proved in Lean. The induction over `s` coordinates
  is not formalized. The closed form it is applied to needed empty leaf
  classes: Lemma S1 proves that for every skeleton (unreviewed).
- **A general positivity argument for the mixed second partials?** Partly. The
  expansion over subsets (S2) writes the coefficient of each product of leaf
  numbers as `x^{a−1}(1+x)^{s−a} r_A(x)`, and Proposition S4 shows that a
  non-negative expansion of `r_A` in the basis `x^e(1+x)^{d−2e}`, `x^e`
  (Property Γ) makes that coefficient non-negative in `d_m − d_{m−1}` for
  every order at once. Property Γ holds, by exact computation, for all 47
  trees with at most 8 vertices as skeleton (7,448 subsets, 0 failures). So
  Hypothesis V is established, computer-assisted and unreviewed, for those
  skeletons and every order — for path skeletons with `s ≤ 8` in particular —
  and it is a conjecture in general (Conjecture Γ, MD-0010). No induction or
  recurrence was found.
- **The coefficient of the product of all leaf counts.** Proved for every
  tree: `r_V = (s+3)x + s` (Proposition S3; Graham–Pollak and the
  Graham–Lovász inverse). The pattern observed in session 4 for paths is a
  theorem for every skeleton, pending review. Beyond it, as exact
  observations: for a subset missing one vertex of degree `g`,
  `r_A = (s−1)(1+x)² + [(g−1)s + 2g + 1]x + [(g−1)(s+6−g) + 3]x²`; and `r_A`
  depends only on `s` and on the Laplacian of the skeleton restricted to the
  missing vertices.
- **Is the extremal reduction a useful standalone result?** L4 alone is
  elementary. The combination L4 + S1 + S4 + Γ is a statement about all trees
  with at least as many leaves as non-leaf vertices: for the 47 skeletons, the
  lower inequality of every such tree is at least that of a tree "skeleton
  plus one star". It is not yet a result about the conjecture, because those
  trees are not treated; in the orders computed (up to 100) all are positive.
- **The upper bound.** No mechanism. The analogue of the certificate fails for
  `d_m − d_{m+1}`, Proposition S4 is specific to the index `⌊n/2⌋`, and the
  upper bound involves the coefficients with `|A| ≤ 1`, which Γ does not
  control.
- **Literature.** The closed formula of T1 (Lemma D1) is in print:
  Xue–Liu–Jia, Filomat 30:6 (2016), Lemma 2.3, and do Nascimento's thesis
  (2018), Prop. 3.2.1; the project's polynomial coincides with theirs. The
  formula behind T3 is Prop. 3.2.6 of the thesis; the balanced case of T2 is
  Prop. 3.2.9. No statement on the location of the peak for these families was
  found, and nothing on the multi-affine structure or the expansion, within a
  small search. Collins (1993), which treats double stars, was not accessed.

### What failed

- No proof of Conjecture Γ, and no review of anything written in this
  session. The proofs of S1 to S4 came out in one pass; they are checked
  against exact computation, which is not a review.
- The reformulation through forest polynomials is a remark without a careful
  derivation.
- The 186-second run on all trees with at most 8 vertices was made before its
  script was committed; the result file was produced again on a clean tree
  with a shorter range of orders (the range check is superseded by Γ, which
  does not depend on the order).
- The clock: the subagents were told to stop at 12 and 14 minutes and reported
  that they could not measure time; the environment reports 4.1 and 9.7
  minutes for them.
- The missing push-triggered CI was looked at, read-only, while the Lean
  verification was running, and not resolved. Facts: the workflow is `active`
  and lists `push` for both branches; all five runs of the repository are
  `workflow_dispatch`; the repository's event feed (`/repos/…/events`) contains
  a single event, the creation of `main` at 07:18 UTC, and no `PushEvent` for
  any of the day's pushes, although `pushed_at` is current; the repository was
  created the same day. So GitHub is not emitting push events for this
  repository, to the feed or to Actions. Whether that is a restriction on the
  account or the repository, or a delay, cannot be determined from here; it is
  for the director to check in the account's settings or with GitHub Support.
  Manual dispatch works and is recorded in the agent's memory notes.
- Not done: the revision of the notes of T1 to T3 with the citations found;
  O4 as such.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author and both subagents, separate contexts) |
| Session wall-clock | from 11:04 UTC to the last commit; the commit times are in the Git history |
| Computation wall-clock | about 5.8 minutes for the research (trial runs of 2, 4, 28, 186 and 18 seconds and the result run of 110 seconds), against 5 planned; one Lean verification of about 3 minutes and one full test run in addition |
| Literature audit, as reported by the environment | 101,841 subagent tokens, 28 tool calls, 4.1 minutes |
| Formalization, as reported by the environment | 59,294 subagent tokens, 19 tool calls, 9.7 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 exploration; 4 statements proved by hand (S1 to S4), 1 conjecture, 2 observations |
| Proof attempts | S1, S2, S3, S4: written, unreviewed. Γ: none |
| Counterexamples found | 0 (none to Γ among 7,448 subsets) |
| Formalization attempts | 1 module, 2 theorems, successful |
| Successful verifications | 101 tests in `tests/test_cj0001_distpoly.py`; 7,820 identities and 7,448 expansions; Lean pipeline with receipt |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable: a structural description of the coefficient polynomials of any tree
with pendant leaves (S1, S2), a theorem-level explanation of the top
coefficient (S3), an order-independent property (Γ) that turns Hypothesis V
into a finite statement per skeleton and is verified for every skeleton with
at most 8 vertices, the discrete core of the extremal reduction in Lean, and a
literature audit that places the formulas of T1 to T3 in print. Nothing was
promoted; MD-0006 to MD-0008 remain candidate theorems. Next: objective O5 in
`STATE.md` (Property Γ for subsets missing one vertex, by hand), after or with
obligations 1 to 3.

## Session 6 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2` (research director; the
  same model wrote session 5, in another context). Director's instructions for
  the session, in order: (1) independent adversarial review of Lemma S1 and
  Propositions S2, S3, S4 of `notes/skeleton-identity.md` at revision
  `1bb2bbe`, a gap taking precedence over everything else; (2) literature:
  Collins 1993 from a local PDF supplied by the director (not to be copied
  into the repository), then the Discrete Appl. Math. 2019 paper of do
  Nascimento, Del-Vecchio and de Freitas and pages 16 to 37 of the 2018
  thesis; (3) objective O5 only if time remains. MD-0006 to MD-0008 stay
  candidates; nothing is promoted. Push of this session's verified commits to
  `research` only is authorized; CI is dispatched by hand.
- **Mode:** focused work (review and literature audit first; O5 is the one
  exact mathematical objective, conditional on time).
- **Role(s):** research director; literature auditor for Collins 1993;
  mathematical researcher for O5 if reached. Subagents: one
  `adversarial-reviewer` (fresh context, model `claude-opus-5-5`, given the
  primary source reference, the file paths, the revision and the review
  template only); one `literature-auditor` for the 2019 paper and the thesis.
- **Repository revision at start:** `2c1cff1` (branch `research`, clean tree).
  `git diff 1bb2bbe 2c1cff1` is empty: the files reviewed are those of
  `1bb2bbe`.
- **Objective (exact), O5:** for every tree `S` on `s >= 3` vertices and every
  vertex `w` of degree `g`, with `A = V \ {w}`:
  `r_A(x) = (s-1)(1+x)^2 + [(g-1)s + 2g + 1] x + [(g-1)(s+6-g) + 3] x^2`,
  proved by hand from `P^{-1} = -L/2 + tau tau^T/(2(s-1))`, in a form that
  extends to more missing vertices.
- **Approach:** as in Proposition S3: `N_A` is `2x I_Abar` minus a
  perturbation of `P` of rank at most 2; reduce `det N_A` to `det P`,
  `P^{-1}1` and entries of `P^{-1}` on `Abar`.
- **Falsification test:** the closed form against the stored exact expansions
  for the 47 trees with 2 to 8 vertices, and against a fresh direct
  computation of `det N_A` before any proof is written.
- **Stopping conditions:** a gap reported by the reviewer stops O5 and the
  repair takes over. The mathematics stops at 16:08 UTC whatever its state.
  Subagents are told to return by 15:55 UTC; a report that has not arrived by
  16:10 UTC is recorded as not obtained.
- **Budget (binding, set by the director):** 60 minutes of agent work from
  15:26 UTC to 16:26 UTC, review, verification, records, push and CI dispatch
  included. Computation at most 5 minutes of wall-clock time.
- **Deferred obligations:** 2 (revision of the notes of T1 to T3) unless time
  remains; 4 to 8 untouched.

### What was done

All computations are exact (integers and rationals). Times are UTC, from
`date -u` in the session's shell.

1. 15:26 start; `STATE.md` read; the header of this entry written before any
   other work.
2. **Review of S1 to S4** (priority 1). `adversarial-reviewer` subagent, model
   `claude-opus-5-5`, fresh context, given the file path, the revision
   `1bb2bbe`, the primary-source references, a list of boundary cases to
   test and the template — no reasoning of the author. Report:
   [`reviews/2026-11-26-claude-opus-5-5-S1-S4.md`](reviews/2026-11-26-claude-opus-5-5-S1-S4.md).
3. **Collins 1993** (priority 2) read by the main context: the PDF supplied by
   the director, 9 pages, all read as page images. It is the author's
   manuscript, not the journal's pages. Not copied into the repository.
4. `literature-auditor` subagent (model `claude-fable-5-2`, separate context)
   for the Discrete Appl. Math. 2019 paper and thesis pages 16 to 37: 2 web
   queries, the thesis PDF fetched by the route of session 5 and pages 14 to
   38 read as images; the 2019 paper could not be opened (HTTP 403 from the
   publisher and from CORE, HTTP 429 from one index, bot protection on a
   catalogue). The auditor reports one mistake of its own: a first DOI was
   guessed and belonged to another paper; nothing from it was used. Section
   "Literature audit 2026-11-26 (session 6)" of the dossier.
5. **Objective O5** (priority 3), while the subagents were running: the
   identity `N_A = −P + WKWᵀ` and the reduction to a determinant of size
   `t + 1` were derived by hand, then the Laplacian form, the one-vertex and
   two-vertex formulas and the decomposition for independent complements.
   Before anything was written down, `locality_check.py` (new, sharing no
   code with `skeleton_structure.py`) compared each formula with the
   definition of `r_A` on the 47 trees with 2 to 8 vertices: runs of 38 s,
   35 s and 35 s (the script grew between runs; the first attempt stopped on
   a singular matrix because negative evaluation points were used, which was
   a defect of the script, not of a formula). Both this script and
   `skeleton_structure.py` take their trees from the enumeration of networkx
   (47 trees, the known count); they share no other code. Notes:
   [`notes/skeleton-locality.md`](notes/skeleton-locality.md). Committed as
   `1805bca` together with the first review report.
6. **Review of S6 to S10 and Lemma C**: a second `adversarial-reviewer`
   subagent (`claude-opus-5-5`, fresh context) on `1805bca`. Report:
   [`reviews/2026-11-26-claude-opus-5-5-S6-S10.md`](reviews/2026-11-26-claude-opus-5-5-S6-S10.md).
7. While it ran, an exploration of the remaining case (scratch script, then
   `gamma_pieces.py`, 11 s): which pieces of the Laplacian form have the
   required weight. It suggested Lemma F and the reduction S11, written in
   [`notes/gamma-reduction.md`](notes/gamma-reduction.md); committed as
   `5622d19` with the second review report, two regression tests and the
   dossier section.
8. **Review of Lemma F, Corollary F′ and S11**: a third `adversarial-reviewer`
   subagent (`claude-opus-5-5`, fresh context) on `5622d19`. Report:
   [`reviews/2026-11-26-claude-opus-5-5-F-S11.md`](reviews/2026-11-26-claude-opus-5-5-F-S11.md)
   — a gap in one paragraph. The note was revised for every defect of the
   report and committed as `7acd425` with it; a fourth fresh context
   (`claude-opus-5-5`) rechecked the revision:
   [`reviews/2026-11-26-claude-opus-5-5-recheck-F-S11.md`](reviews/2026-11-26-claude-opus-5-5-recheck-F-S11.md).
   Both result files were regenerated at `5622d19`, a revision that contains
   their scripts (the first runs were made before the scripts were
   committed); the totals are identical. The working tree then held
   uncommitted record files (`STATE.md`, the registry), not code or data.
9. Registry: MD-0010 updated (evidence, limitations, novelty coverage; its
   statement and fingerprint unchanged); MD-0011 and MD-0012 registered.
   `STATE.md` updated. `uv run pytest`, `scripts/catalogue.py validate` and
   `render`: results under Outcome.

### Findings

- **Review of session 5 (S1 to S4): no gap found within stated scope**, for
  each statement and overall (AI review; same vendor and family as the
  author). The reviewer reconstructed the four proofs and ran its own exact
  checks (S1 on 293 trees with zeros among the leaf numbers; S2 for 198 leaf
  vectors and every subset on skeletons with at most 4 vertices; S3 on 5
  trees; the binomial lemma of S4 on 3,360 pairs and its use on 15,075
  tuples). Defects, none mathematical: the bound `deg r_A ≤ s − a + 1` is
  asserted with a reason that covers only the `1/x` part (a one-line cofactor
  argument closes it; `skeleton-locality.md` now contains that argument);
  `γ_A` is defined in the statement of S2 only for `x ≠ 0`; `M_A` names two
  different matrices; `p_∅` is a Laurent expression. Not covered: Corollary
  S5, Lemma L4, the Γ computation; the two classical formulas were checked by
  computation, not against the printed papers.
- **Literature.** Collins's manuscript contains the divisor principle for an
  invariant subspace and for vertex orbits (Theorems 1 and 2), the lower bound
  `p − q` for the multiplicity of `−2` (Corollary 7), the polynomial of the
  star (Corollary 5) and of the balanced double star only (Corollary 6), and
  the full `k`-ary trees. **It contains no statement on the coefficients or
  their maximum, no general double star, no caterpillar, no expansion in the
  leaf numbers.** Corollary 6 as printed in the manuscript fails against
  direct computation for `n = 1, …, 6` (its roots sum to `−2`); the factors
  `(λ² + (n+3)λ + 2)(λ² − (5n−1)λ − 4n − 2)` hold in those six cases. Thesis
  pages 14 to 38: multiplicity of `−2` and number of distinct eigenvalues for
  double brooms and caterpillars; nothing on coefficients, no expansion over
  subsets, no `det(P + αJ)`. The 2019 paper: not read. So, within the pages
  read in sessions 2, 5 and 6: no prior statement of the peak results
  (MD-0006 to MD-0008), of S2 or of `r_V = (s+3)x + s` was found; this does
  not establish novelty, and the 2019 paper, Collins 1989 and the published
  version of Collins 1993 remain unread.
- **O5 and beyond (MD-0011; proved by hand, AI-reviewed, exact check on the
  47 trees).** For every tree and every `A`, with `B = V ∖ A`:
  `r_A = Φ_B [a(1+x) + (3 + 3H − 2e_B)x] − x² zᵀ adj(I + xL_B) z` (S6, S7): the
  dependence on the skeleton is only through `s` and the Laplacian block
  `L_B`, which proves the observation "Locality" of session 5 in general. The
  formula for one missing vertex follows in three lines (S8); two missing
  vertices are done by explicit inequalities (S9); and **when `B` is
  independent, `r_A` has an explicit decomposition into terms of weight at
  least `t + 1`, hence Property Γ's requirement holds, for every tree** (S10).
  The mechanism asked for: Lemma C turns Γ into membership in a cone closed
  under products, and the negative term `−4h_w² x² Φ_w` is absorbed by
  `a(1+x)Φ_B` at the price of the coefficient `a − H`, which is positive
  because the edges leaving an independent set form a forest. Review of
  `1805bca`: no gap found within stated scope for each of S6 to S10, Lemma C
  and the degree claim; the reviewer recomputed everything on 152 labelled
  trees (4,988 subsets). Defects: the count "1,011 cases" for S9 includes one
  case with `s = 2`, outside the statement (1,010 within it); three of
  wording.
- **Reduction (MD-0012; proved by hand; exact check on the 47 trees).**
  Lemma F: `det(I + x(L_T + diag ν))` has weight at least the number of
  vertices, by removing a leaf. Hence the positive term of the Laplacian form
  always has the required weight (F′), and contracting the components of
  `S[A]` changes `r_A` by `(a − a′)(1+x)Φ_B` (S11): Γ extended to `|A| = 1`
  follows for all trees from its case `A` independent. Review of
  `5622d19`: no gap in the cones, Lemma F, F′ and S11 (Lemma F recomputed by
  the reviewer on 41,276 weighted trees; integrality of the weights is
  needed, with a counterexample for `ν = (1/2, 0)`); **gap found** in the
  paragraph "What this gives": the case `A = V` of Γ⁺ is covered neither by
  S11 nor by "`A` independent" and needs Proposition S3. Repaired in one
  revision. Recheck of `7acd425`: the gap is closed, no statement or proof
  step of the three results was changed, no new error; two trivial defects
  of wording remain.
- **Observations (exact, 47 trees, not proved).** Γ holds also for the 325
  subsets with one element; `zᵀ adj(I + xL_B) z` has non-negative
  coefficients in all 7,726 cases.

### What failed

- The Discrete Appl. Math. 2019 paper could not be accessed; even its
  abstract is known only by paraphrase.
- No induction on `|V ∖ A|` was found. When `V ∖ A` contains an edge the
  termwise weight count of S10 fails; S9 with adjacent vertices was proved by
  inequalities on coefficients, which do not generalize as written.
- The notes of T1 to T3 were not revised with the citations found
  (obligation 2 stands), and the defects listed by the three reviews of this
  session were not corrected, by decision: the reviewed files are unchanged.
- `locality_check.py` counts one case of S9 outside its statement (`s = 2`);
  the result file is evidence and is left as produced.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (main context and literature auditor); `claude-opus-5-5` (three reviews, separate fresh contexts) |
| Session wall-clock | from 15:26 UTC; this entry was completed at about 15:58 UTC, before the final test run, the last commits, the push and the CI run, whose times are in the Git history and in the commit messages |
| Computation wall-clock | about 3.4 minutes for the research (38 s, 35 s, 35 s, 3 s, 11 s, 11 s, the two regenerations of 33 s and 12 s, and short trials), against 5 planned; the full test suite takes 6 to 7 minutes per run and is not counted here |
| Review of S1 to S4, as reported by the environment | 72,420 subagent tokens, 16 tool calls, 6.9 minutes |
| Literature audit, as reported by the environment | 83,526 subagent tokens, 21 tool calls, 3.2 minutes |
| Review of S6 to S10, as reported by the environment | 75,727 subagent tokens, 11 tool calls, 5.5 minutes |
| Review of Lemma F and S11, as reported by the environment | 75,963 subagent tokens, 17 tool calls, 6.3 minutes; its recheck: 60,165 subagent tokens, 13 tool calls, 3.1 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective (O5), reached and extended; 1 exploration |
| Proof attempts | S6, S7, S8, S9, Lemma C, S10: written and reviewed once; Lemma F, F′, S11: written, reviewed once, one paragraph of the note repaired, rechecked |
| Counterexamples found | 0 to the project's statements; Corollary 6 of Collins's manuscript fails as printed for `n = 1, …, 6` |
| Formalization attempts | 0 |
| Successful verifications | 3 exact result runs with 0 failures (7,820 subsets; 7,726 subsets); `uv run pytest`: run after this entry was written; its result is in the message of the commit that contains this entry |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress. Priority 1: the review owed for session 5 was obtained and
found no gap in S1 to S4. Priority 2: Collins 1993 was read (in the author's
manuscript) and thesis pages 14 to 38; neither contains a statement of the
peak results, the subset expansion or the identity for `r_V`; the 2019 paper
was not accessible. Priority 3: O5 was proved, together with the mechanism
behind it (the Laplacian form of `r_A`), Property Γ for independent
complements, and a reduction of the conjecture to independent `A`; all of it
has a written proof, an exact check on the 47 small trees and one AI review
(the reduction: one review, one repair, one recheck). Nothing was promoted:
MD-0006 to MD-0008 are unchanged; MD-0011 and MD-0012 are new records at
`candidate-proof` with external review `ai-reviewed`; MD-0010 is still a
conjecture. The session stopped the mathematics at about 15:45 UTC, well
before the limit of 16:08, because the remaining case (an edge inside
`V ∖ A`) needs a new idea and the time left was better spent on the third
review and its repair.

Not done: the revision of the notes of T1 to T3 (obligation 2); the
corrections of wording asked by the reviews of `skeleton-identity.md` and
`skeleton-locality.md` (obligation 3a); any literature search for MD-0011
and MD-0012.

The results of `uv run pytest`, `scripts/catalogue.py validate` and
`render --check`, of the push to `research` and of the CI run dispatched by
hand are produced after this entry is written; they are in the message of
the commit that contains this entry (tests, validation) and in the report
to the director (push, CI).

Next step: objective O6 in `STATE.md` — Property Γ⁺ for `A` independent and
`S[B]` a single edge plus isolated vertices, by an explicit grouping in the
cones `C_d`.

## Session 7 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2` (main context, Claude
  Code). Human: G. B. Brito, director, by written instructions at the start
  (priorities; a mathematical observation, quoted under Findings; approval of
  the classifications of MD-0011 and MD-0012; authorization to push verified
  commits to `research` only; the automatic CI trigger works).
- **Mode:** focused work (reviews owed; objective O6), with an exploration of
  the director's observation inside it.
- **Role(s):** research director; mathematical researcher and computational
  experimenter for O6. Subagents: three `adversarial-reviewer` contexts
  (`claude-opus-5-5`, fresh, given the catalogue id, the primary source
  reference, file paths, revision and template only) and one
  `literature-auditor` (`claude-fable-5-2`, separate context).
- **Repository revision at start:** `9499572` (branch `research`, clean tree).
- **Deviation from the protocol, recorded:** this header was written at about
  17:16 UTC, after the mathematics, not before it (steps 5 to 8 ask for it
  first). The objective, falsification test and budget below are those the
  session actually worked under: O6 and its test are in `STATE.md` as left by
  session 6, and the budget is the director's standing decision.
- **Objective (exact), O6 as left by session 6, widened by the director's
  instructions:** show that
  `Φ_B [a(1+x) + (3 + 3H − 2e_B)x] − x² zᵀ adj(I + xL_B) z ∈ C_{t+1}` for `A`
  independent, by a structural argument valid for arbitrary forest components
  of `S[B]`; find a companion recurrence for the adjugate quadratic form
  alongside Lemma F; examine what the spectral identity for
  `zᵀ adj(I + xL_B) z` gives beyond non-negative coefficients.
- **Approach:** (1) the spectral identity as a partial-fraction expansion of
  `r_A/Φ_B`; (2) split `r_A` over the components of `S[B]`; (3) Schur
  complements at a leaf for the adjugate, as in Lemma F for the determinant.
- **Falsification test:** every identity and every cone membership against
  exact computation on the 47 small skeletons and on all small weighted trees
  before it is written (`component_form.py`).
- **Stopping conditions:** mathematics stops at 17:36 UTC; a gap reported by a
  reviewer takes precedence over new mathematics.
- **Budget (binding, director's standing decision):** 60 minutes of agent
  work, 16:51 to 17:51 UTC, reviews, verification, records and push included.
  Computation: at most 30 minutes of wall-clock time (default of
  `autoresearch.md`).
- **Deferred obligations:** 2 (revision of the notes of T1 to T3), 3a (the
  revisions owed after the reviews of session 6), 4 to 8.

### What was done

All computations are exact (Python integers and rationals). Times are UTC,
from `date -u` in the session's shell.

1. 16:51 start; `AGENTS.md`, `autoresearch.md`, `STATE.md`, the notes of
   session 6 and the last journal entry read.
2. Three subagents started at once on `9499572`: review of Lemma L4 and
   Corollary S5; review of the computation of Property Γ
   (`skeleton_structure.py` and its result file); literature audit for
   MD-0011 and MD-0012. Reports:
   [`reviews/2026-11-26-claude-opus-5-5-L4-S5.md`](reviews/2026-11-26-claude-opus-5-5-L4-S5.md),
   [`reviews/2026-11-26-claude-opus-5-5-gamma-computation.md`](reviews/2026-11-26-claude-opus-5-5-gamma-computation.md),
   and the section "Literature audit 2026-11-26 (session 7)" of the dossier.
3. O6, by hand, while they ran: the partial-fraction form of `r_A/Φ_B`, the
   real roots, the bound on the leading coefficient, the third form of `r_A`,
   the component polynomial `R(T, ν)`, the recurrences at a leaf. Two
   attempts abandoned on paper (roots, Darroch; under What failed).
4. `component_form.py` written; trial runs on small sizes (3 s, 14 s, 20 s);
   three full runs of 170 s each: one before Part 3 existed, one with the
   final script on a dirty tree at `9499572`, and — after the commit
   `b0a4dbe` — one on a clean tree at `b0a4dbe`, identical to the second
   apart from the provenance and timing fields. After the review a fourth run
   (180.9 s) was made with one more check in Part 3 (statement (E″), under
   Findings); **the stored result file is that fourth run**. It records
   revision `b0a4dbe` and a dirty tree: the script it ran is the version
   committed together with it (it differs from `b0a4dbe` by the added check
   only), and the record files were being edited. Every count it shares with
   the third run is identical. A trial with weights up to 4 and `j ≤ 5` (10,772 weighted trees,
   31,460 leaves; zero failures of Γ_c, of the identities and of `E`) was not
   stored.
5. Note [`notes/gamma-components.md`](notes/gamma-components.md) written and
   committed (`b0a4dbe`) with the script, the result file, the two review
   reports and the dossier section.
6. Review of the new note: a fourth `adversarial-reviewer` context
   (`claude-opus-5-5`, fresh) on `b0a4dbe`. Outcome: under Findings.
7. Registry: MD-0009, MD-0010 (evidence), MD-0011, MD-0012 (novelty search
   recorded), MD-0013 and MD-0014 registered. `STATE.md` updated.

### Findings

- **Review of L4 and S5 (AI, `claude-opus-5-5`, revision `9499572`): no gap
  found within stated scope**, for each. L4: every step reconstructed, the
  boundary cases checked, a second proof found (the hypothesis is equivalent
  to non-negative coefficients of degree ≥ 2 in the shifted variables; the
  lemma then holds at real points of the slice); 8,000 random functions, 0
  violations. S5: tested against the distance matrix on 21,929 trees over the
  13 skeletons with 2 to 6 vertices, 0 below the vertex minimum. The reviewer
  states what S5 proves: an inequality `≥`, no positivity, orders `n ≥ 2s`.
  Defects: two stale statements in `vertex-principle.md`; the remark under
  Conjecture Γ should say "at least two non-leaf vertices". L4 itself is not
  formalized (the Lean files hold one exchange step), as the files say.
- **Review of the Γ computation (AI, `claude-opus-5-5`, revision `9499572`):
  no gap found within stated scope.** Independent recomputation from the
  definition of `r_A`, with the reviewer's own tree enumeration (two
  methods): 7,448 pairs, 0 failures, agreement with the repository
  coefficient by coefficient; rerun of the script identical apart from timing
  (129 s). Seven defects of wording and provenance, none changing the claim:
  S1 was checked with zero leaf numbers only for `s ≤ 5`; "orders up to 100"
  has no committed evidence; the result file records `7c1a9dd` and a
  temporary output path; stale review status in the note; "every order"
  without `n ≥ 2s`; the test covers `s ≤ 5`; the README's timing.
- **Literature audit for MD-0011 and MD-0012 (first search; novelty not
  established).** No identical statement found. To be cited:
  Bapat–Kirkland–Neumann 2005, Theorem 2.1 and Theorem 2.4 — **the
  determinant behind Proposition S3 is in print** (`det(D + xJ)` for weighted
  trees), which corrects the "not found" of session 6 for that determinant
  (the statement `r_V = (s+3)x + s` itself was not found);
  Richman–Shokrieh–Wu, arXiv:2411.11488, Theorems A and 4.4 (principal minors
  of `D` through a Laplacian minor on the complement; same shape as S7, a
  different determinant). The literature most likely to contain Lemma F
  (matching polynomials of forests, Laplacian coefficients of trees) was
  identified and not read. Not searched: MathSciNet, zbMATH, Google Scholar.
  Novelty of both records: `preliminary-search-completed`.
- **The director's observation** (human mathematics): since `L_B` is
  symmetric positive semidefinite, `zᵀ adj(I + xL_B) z = Σ_i y_i² Π_{l≠i}(1 + xλ_l)`
  with `y = Uᵀz`, `λ_l ≥ 0`, which gives coefficientwise non-negativity.
  Checked and written as Proposition S13(b); it proves the observation that
  session 6 had left as a computation on the 47 trees.
- **What it yields (MD-0013; proved by hand, exact check on the 47 trees):**
  `r_A/Φ_B = a + C + κx − Σ_l (c_l/μ_l²)/(1 + μ_l x)` is increasing between
  its poles, so **all `t + 1` roots of `r_A` are real and negative** for
  every tree and every `A` with `1 ≤ a ≤ s − 1`; the leading coefficient is
  `κ det L_B` with `κ = s + 3 − τ_BᵀL_B^{−1}τ_B ≥ 4` (equality iff `a = 1`;
  `κ = 4 + 2/(1ᵀP_A^{−1}1)`). Hence positive, log-concave coefficients. It
  does **not** yield Γ: real negative roots do not imply the half-gamma
  expansion.
- **Component form and recurrences (MD-0014; proved by hand, exact checks):**
  `r_A = r_V Φ_B − pᵀ adj(I + xL_B) p` (S12);
  `r_A = [(1+4x) + e_A(1+x)]Φ_B + Σ_i R(T_i, ν) Π_{l≠i}Φ(T_l, ν)` (S14), so Γ⁺
  follows from Γ_c, a statement about one weighted tree; Lemma G gives the
  adjugate after removing a leaf and after raising a weight; for a leaf of
  weight 0, `R(T, ν) = (1+x)R(T−w, ν) + x[ν_u(1+x)Ψ + Σ R_i P_i]` — every term
  in the cone under the induction hypothesis (S15, S18); for a leaf of weight
  `n`, `R(T, ν) = R(T, ν⁰) + nE + n(n−1)xΦ(T−w, ν+e_u)` (S17). **Γ_c, hence
  Γ⁺ and Conjecture Γ, is reduced to statement (E): `E ∈ C_{j+1}`.**
- **Exact computation (`results/component-form.json`; the counts below are
  the same in the run on a clean tree at `b0a4dbe` and in the stored fourth
  run):** 47 trees, 7,726 subsets: 0 polynomials with a
  non-real or non-negative root, 0 failures of the degree, of the
  leading-coefficient identity, of `κ ≥ 4` and its equality case, of the
  identity with `P_A` (7,401 subsets); 2,263 independent `A`, 4,344
  components, 0 failures of S14. Weighted trees with `j ≤ 7`, weights 0 to 2:
  29,336; `R ∉ C_{j+1}`: 0; 111,768 leaves: Lemma G failures 0,
  `R(T, ν) − mR(T−w, ν) ∉ C_{j+1}`: 0. Part 3 (`j ≤ 6`): 17,856 leaves; S17
  failures 0; `R(T, ν⁰) ∉ C_{j+1}`: 0; `E ∉ C_{j+1}`: 0; `E* ∉ C_{j+1}`: 972.
- **Review of S12 to S18 and Lemma G (AI, `claude-opus-5-5`, revision
  `b0a4dbe`): no gap found within stated scope**, for each statement (the
  cone inclusions, S12, S13(a) to (e), S14, G1, G2, S15, S16, S17, S18, the
  reduction of Γ_c to (E), the example for `E*`). The reviewer checked that
  S18 never uses Γ_c at the same size, that every use of Lemma F has a
  non-zero integer weight, the degenerate cases, strictness in S13(c) and the
  completeness of the root count in S13(d); and recomputed with its own code,
  `r_A` from the determinant `N_A`: S12, S13(b) to (e), S14 on 1,884 subsets
  of the 24 trees with `s ≤ 7`; on weighted trees with `j ≤ 4`, weights 0 to
  3: Γ_c (591), G2 (11,328 entries), S16 (2,276), S15 (360), S17 (1,440), (E)
  with all leaf weights `≥ 1` (702): no failure. Three defects of wording:
  "two elementary facts" lists three; (E) does not state its quantifiers (the
  reduction is valid for "some leaf"); the opening paragraph calls a
  sufficient condition a "reduction" and a family "one explicit polynomial".
  Not checked by the reviewer: the counts of the note's section on
  computation; the attribution sentence against the director's instructions;
  novelty. S13(e) rests on the Graham–Lovász inverse, checked in the project
  by computation only. The note is left byte-identical to `b0a4dbe`; the
  defects are owed one revision.
- **After the review, an observation (exact computation, not in the note,
  not reviewed): (E″)** — `E − xR(T′, ν + e_u) = (1+5x+3x²)Φ′ + (x+4x²)Ψ + 2x²π′`
  is in `C_{j+1}` in all 17,856 cases of Part 3 and in the trial with weights
  up to 4 (31,460 cases). It implies (E) and involves no `R`. The script
  gained one field for it and the result file was regenerated (a fourth full
  run; its revision and tree state are in the file).
- **Scratch computation at the end of the session (not stored, not
  reviewed):** with `F(T, ν, u) = (1+5x+3x²)Φ + (x+4x²)Ψ_u + 2x²π_u`, two leaf
  recursions for `F` derived from Lemma G2, and the slope of `F` in a leaf
  weight, hold in all 10,089 cases with at most 5 vertices and weights 0 to 2;
  `F ∈ C_{j+2}` in all 4,395 rooted weighted trees, zero weight included; the
  slope is in `C_{j+2}` in every case. The formulas and the resulting target
  (S) are in the section *Next step* of `STATE.md`.

### What failed

- **Γ is not proved.** Statement (E) is open; `E*` alone leaves the cone
  (star with three leaves of weights 2, 2, 3, centre of weight 0), so the
  absorption must use `xR(T′, ν+e_u)` or `(1+x)Φ(T, ν⁰)`. Two hypotheses on
  the linear form `π_u` were tried on paper and dropped because they do not
  reproduce under the expansion at a vertex (negative terms `−2qx²Ψ` remain).
- **Roots.** Real-rootedness does not give the cone; pairing roots cannot
  work for long paths.
- **Darroch's theorem** on the mode of a real-rooted polynomial, as a
  substitute for Γ in Proposition S4: the index needed is the upper central
  one, where a mean bound decides nothing; and real roots with mean equal to
  half the degree are not sufficient (`(1+0.6x)²(1+3x)(1+x)²`: coefficients
  `13.36` and `13.2` at indices 2 and 3; hand computation, not rerun).
- The header of this entry was written after the work (above).
- No regression test was added for `component_form.py`.
- `STATE.md` is above its target of 400 lines.
- Not done: the revisions of notes owed after the reviews of sessions 6 and
  7; obligation 2; any literature search for MD-0013 and MD-0014.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (main context, literature auditor); `claude-opus-5-5` (reviews, separate fresh contexts) |
| Session wall-clock | from 16:51 UTC; this entry was written at about 17:16 to 17:20 UTC; later times are in the Git history |
| Computation wall-clock | about 13 minutes for the research (four full runs of about 170 s; trials of 3 s, 14 s, 20 s, 20 s); the reviewers' own computations (about 40 s, 222 s) and the test suite are not counted |
| Review of L4 and S5, as reported by the environment | 112,403 subagent tokens, 25 tool calls, 9.5 minutes |
| Review of the Γ computation, as reported by the environment | 116,036 subagent tokens, 34 tool calls, 10.4 minutes |
| Literature audit, as reported by the environment | 155,420 subagent tokens, 42 tool calls, 5.5 minutes |
| Review of S12 to S18, as reported by the environment | 103,146 subagent tokens, 16 tool calls, 8.4 minutes |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective (O6): not reached as stated; reduced to (E) |
| Proof attempts | S12, S13, S14, Lemma G, S15, S16, S17, S18: written once; Γ_c: not proved |
| Counterexamples found | 0 to the project's statements; `E*` alone outside the cone (972 cases) |
| Formalization attempts | 0 |
| Successful verifications | 1 exact result run on a clean tree with 0 failures; tests and validation: in the message of the commit that contains this entry |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress, and the main objective not reached. The three reviews owed
were obtained (no gap found in L4, S5 and the Γ computation; lists of defects
recorded). The originality of MD-0011 and MD-0012 had a first audit: nothing
identical found, three sources to cite, the most relevant literature for
Lemma F still unread. The director's spectral identity gives a new structural
fact — `r_A` has only real negative roots — and O6 was turned into an
induction on a leaf that closes for leaves of weight 0 and leaves one
explicit statement, (E), for leaves of positive weight. Nothing was promoted:
MD-0013 and MD-0014 are candidates.

Next step: objective O7 in `STATE.md` — prove (E) through (E″).

## Session 8 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2` (main context, Claude
  Code). Human: G. B. Brito, director, by written instructions at the start
  (approval of the classifications of MD-0011 to MD-0014 as they stand;
  priorities, quoted under Objective; authorization to push verified commits
  to `research` only).
- **Mode:** focused work on O7 and statement (S), with an exploration inside
  it (is there an induction that closes, or a structural argument that avoids
  the hierarchy of auxiliary inequalities).
- **Role(s):** research director; mathematical researcher for O7. Subagents
  started at about 20:30 UTC, each in its own context: `literature-auditor`
  (first originality search for MD-0013 and MD-0014), `formalization-agent`
  (L4 in `s` variables; foundations of the cone `C_d`),
  `computational-experimenter` (the scratch computations of session 7 as a
  stored script; regression test for `component_form.py`).
- **Repository revision at start:** `9069d88` (branch `research`, clean tree).
- **Objective (exact), O7 as left by session 7 and the director's
  instructions:** decide whether statement (S) of `STATE.md` — for every tree
  `T` on `j ≥ 1` vertices, all vertices `u, v` and every integer weight
  `ν ≥ 0`, `x[F(T, ν + e_v, u) − 2x³ adj(M(T, ν))_{uv}] ∈ C_{j+3}` — can be
  proved by an induction over a family indexed by a multiset of vertices, or
  whether another structural argument avoids the growing family of auxiliary
  inequalities; write down the exact chain from (S) to Conjecture Γ and look
  for a weaker sufficient condition.
- **Approach:** (1) instead of removing a leaf anywhere in the tree (which
  forces several marked vertices), generate rooted weighted trees by three
  operations at the root — raise the root weight, put a new root above, merge
  two trees at the root — and look for a finite list of polynomials attached
  to a rooted tree whose cone memberships are preserved by the three
  operations; (2) the forest expansion of `Φ` and of the adjugate.
- **Falsification test:** every identity and every cone membership against
  exact computation on all small rooted weighted trees before it is written.
- **Stopping conditions:** mathematics stops at 21:05 UTC; a failure of (S)
  or of (E″) reported by the stored computation takes precedence.
- **Budget (binding, director's standing decision):** 60 minutes of agent
  work, 20:28 to 21:28 UTC, verification, records and push included.
  Computation: at most 30 minutes of wall-clock time in total, of which 15
  are given to the experimenter.
- **Deferred obligations:** 1 (except MD-0013 and MD-0014), 2, 3 (the
  revisions of notes owed after the reviews), 4 to 6, 8.


### What was done

All computations are exact (Python integers and rationals). Times are UTC,
from `date -u` in the session's shell.

1. 20:28 start; `AGENTS.md`, `autoresearch.md`, `STATE.md`,
   `notes/gamma-components.md`, the last journal entry and
   `component_form.py` read. Three subagents started at about 20:30 on
   `9069d88` (roles above).
2. O7 by hand: the rooted state `(Ψ, H, G, Ω, R)`, its rules, and from them
   the leading coefficient of `F` on a star, which is negative for many heavy
   leaves. Scratch computations (not stored; 29 s, 4 s, 38 s, 2 s, 100 s,
   35 s, about 20 s): the leading-coefficient formula on stars; (E″), (E) and
   Γ_c on 11,658 stars; Γ_c and (E) on 2,945 random weighted trees; the rooted
   identities; (Λ) and monotonicity on 29,295 rooted stars (up to 7 leaves,
   weights up to 8) and 8,198 rooted random trees; Lemma (★) and S20(d) on 750
   rooted trees; the bracket `Λ⁰` (under Findings).
3. `rooted_state.py` written (importable); trial run 40.7 s; stored run
   146.4 s on a dirty tree at `9069d88` (`results/rooted-state.json`).
4. The experimenter's report (separate context, 15 minutes, 50 tool calls):
   `slope_family.py` (stored run 330 s), `slope_family_extension.py`,
   `slope_family_verify.py`, their result files, the README section and
   `tests/test_cj0001_component_form.py`.
5. Note [`notes/rooted-calculus.md`](notes/rooted-calculus.md) written;
   `tests/test_cj0001_rooted_state.py` added; both test files run (17
   passed); commit `59c47f7` (note, scripts, results, tests, the dossier
   section written by the literature auditor, this entry's header).
6. Review of the new note: an `adversarial-reviewer` context (fresh, model
   `claude-opus-5-5` requested) on `59c47f7`, given the catalogue id, the
   primary source reference, the file paths, the revision and the template.
   Outcome: under Findings.
7. Registry: MD-0013 and MD-0014 (novelty search recorded), MD-0015
   registered. `STATE.md` compacted (467 → 369 lines before the last edits);
   the text removed from it was moved verbatim to
   [`notes/dead-ends.md`](notes/dead-ends.md) (new) and
   [`notes/obligations.md`](notes/obligations.md).
8. Lean: under Findings.

### Findings

- **(E″) and (S) are false (Proposition S21; MD-0015).** For the star with
  centre `u` of weight `n_0` and leaves of weights `n_i`, the coefficient of
  `x^{q+3}` in `F(T, ν, u)` is `Π(1+n_i) · (4 + n_0 − Σ n_i/(1+n_i))` (proved
  from the rooted rules; 0 mismatches on 2,769 stars). Six leaves of weight 3:
  `−2048`. The smallest failure found is at 6 vertices (five leaves of weight
  4: `F` has degree 7, its expansion of degree 8 ends in `−1`); it is the
  only failure of (E″) among the 614,805 rooted cases with `j ≤ 6`, weights 0
  to 4 (`slope-family.json`). (S) fails in 7,225 of 3,630,605 cases there,
  first at 5 vertices (star, leaf weights 2, 3, 4, 4, `u = v` the centre:
  leading coefficient `−5`); four leaves of weight 4: `−125`. Confirmed by a
  checker that shares no code with the search (5 + 6 failures). The three
  leaf identities for `F` that session 7 had found in a scratch run are
  correct (0 failures in 1,403,375, 359,675 and 1,410,440 cases); the count
  10,089 of session 7 is reproduced. **Answer to the director's question:**
  the family indexed by multisets of vertices does not give a closed
  induction, because its first two members are false; no family built on
  (E″) can.
- **(E), Γ_c and Conjecture Γ are not affected.** In every counterexample
  `E`, `R` and `Λ` are in their cones; `E = xR(T′, ν+e_u) + F`, and on stars
  the leading coefficient of `E` is `Π(4 + 8σ) > 0` (hand computation for
  `n_0 = 0`, equal leaf weights; `112500` for five leaves of weight 4,
  computed). (E) holds in the experimenter's 1,000 extension cases (leaf
  weights up to 200).
- **A structural description without marked multisets (S19, S20; MD-0015).**
  `ΨR = Φ[ν_u(1+x)Ψ + Ω] − π_u²` (★); `G = (1+2x)Ψ − π_u` has non-negative
  coefficients; rules for raising the root weight, a new root, and merging
  two rooted trees. In the merge rule every term is a product of quantities
  that are in cones under an induction hypothesis, except `−2G_1G_2`. The
  increment of `R` at any vertex is
  `Δ_u = [(1+2x)² + 2xν_u]Ψ + Σ_c Λ(T_c, ν, c)P_c`, and at a new leaf
  `E = (1+2x)²Φ(T, ν+e_u) + Λ(T, ν, u)`, with one negative term `−4x²G`.
  Identities: 0 failures on 4,395 rooted trees and 10,404 merges.
- **Statement (Λ) (new; conjecture inside MD-0015).** `Λ(T, ν, u) ∈ C_{j+2}`
  for every rooted weighted tree, zero weight included. It implies that `R`
  is non-decreasing in every weight at every vertex, hence (E) at every
  leaf, Γ_c, Γ⁺ and Γ (S22). No failure: 4,395 + 11,085 + 3,269 rooted trees
  stored; 29,295 + 8,198 in scratch runs. It is not proved.
- **The bracket `Λ⁰` alone fails** (scratch): `xΛ⁰ ∈ C_{j+2}` fails in 8 of
  4,395 and 7 of 18,009 cases (smallest: two vertices, zero weights). So the
  branch terms of the recursion for `Λ` are needed at least for small
  weights. Not classified.
- **Dependency chain and weaker conditions** (`rooted-calculus.md`, last
  section): `Γ ⇐ Γ⁺ ⇐ Γ⁺ for A independent ⇐ Γ_c ⇐ (E) ⇐ (Λ)`; only S11 is an
  equivalence. The requirement of S4 (Γ_w) is strictly weaker than Γ
  (`1 + x + x² ∉ C_2` satisfies it; checked for `1 ≤ L < 60` and by the
  argument on palindromic unimodal polynomials), but the larger cone is not
  known to be closed under products. No weaker condition that is easier to
  establish was found.
- **Literature audit for MD-0013 and MD-0014 (first search; novelty not
  established).** MD-0013: item (iv) and the bound `κ ≥ 4` with its equality
  case are **implied by Richman–Shokrieh–Wu, arXiv:2411.11488v2** (Theorems
  A, 2.4, 4.4, 4.6(b)) through a bridging step that is the auditor's own and
  unreviewed; that paper gives sharper bounds on `κ − 4`. The auditor also
  remarks that the real roots follow from S12 by a definite pencil
  (`r_A = det(A_0 + xA_1)`, both positive definite; unreviewed), and that
  the director's identity is the spectral decomposition of the adjugate
  (Castillo–Zaballa, arXiv:2103.13739, Thm 2.1). Nothing found on `r_A`, S12,
  its degree or its roots. MD-0014: nothing identical or implying found;
  Lemma G1 is classical; `Φ(T, ν)` is the principal Laplacian matching
  polynomial of arXiv:2410.14112. Not searched: MathSciNet, zbMATH, Google
  Scholar, books. Both records: `preliminary-search-completed`.
- **After the note was committed (scratch, not in the note, not reviewed):**
  in every case where `xΛ⁰ ∈ C_{j+2}` fails, `ν = 0`. So on the range tested
  (Λ) splits into (Λ⁰) for `ν ≠ 0` — a statement with no `Λ` and no `Ω` — and
  (Λ) for trees with zero weights. Hand computation, not checked by machine:
  `ΨΛ⁰ = Φ[(1 − x + ν_u(1+x))Ψ + Ω] + 2(1+x)ΨG + 2x(1+ν_u)Ψ² − G²`.
- **Review of `notes/rooted-calculus.md` (AI, `claude-opus-5-5`, revision
  `59c47f7`): no gap found within stated scope**, for Lemma (★), S19 (a) to
  (e), S20 (a) to (d), S21 (a) to (c), S22 and the paragraph on Γ_w. Every
  step rebuilt by hand; the counterexamples checked against (E″) and (S) as
  they read in `STATE.md` at `59c47f7`, with the reviewer's own exact code
  (six leaves of weight 3: `−2048`; five leaves of weight 4: `F` as quoted,
  expansion ending in `−1`, and `E`, `Λ`, `R` in their cones; four leaves of
  weight 4: `−125`); identities recomputed on the 102 rooted weighted trees
  with at most 3 vertices and on 3,843 merges; the counts of the note match
  the result files. The reviewer's search for a counterexample to (Λ) and
  to monotonicity covered **only stars with equal leaf weights** (at most 6
  leaves, weights up to about 30; 2,462 rooted cases; no failure); its other
  planned families were not reached, and one of its runs timed out (it
  reports about 6.5 minutes of computation against the 4 allowed). Seven
  defects of wording, none affecting a result: the degrees of `H` and `G` in
  the proof of S21 when all weights are 0; "strictly larger" for Γ_w argued
  only for `d ≥ 2` (true for `d = 1` by another example); Remark 2 after S19
  ignores parts of zero weight; "in every counterexample `E`, `R`, `Λ` are
  in their cones" is shown example by example for two stars only, and the
  sentence on the leading coefficient does not fit the five-leaf example;
  "(S) fails first at `j = 5`" refers to `j` only; the result files record a
  dirty tree at `9069d88`; (★) and S20(d) were checked by an unstored
  script. Not checked by the reviewer: a rerun of the repository scripts,
  the earlier results the note depends on, novelty. The note is left
  byte-identical to `59c47f7`; the defects are owed one revision.
- **Lean (formalization agent, separate context; 37 minutes, 41 tool
  calls).** Two new modules, eight theorems registered (14 for CJ-0001 in
  all). `VertexPrinciple.lean`: `vertex_principle_discrete` and
  `vertex_principle_discrete_min` — for any finite index type, a function on
  integer points that satisfies the exchange inequality
  `f(c+e_i−e_k) + f(c+e_k−e_i) ≤ 2f(c)` at the slice points with both
  coordinates above their bounds is, at every point of the slice, at least
  its value at some vertex `λ + (S−Σλ)e_p`; with a non-vacuity witness in
  three variables. **This is the discrete core of L4 in `s` variables, not
  L4 as written**: the step from a multi-affine polynomial with non-negative
  mixed partials to the exchange inequality is not formalized.
  `HalfGammaCone.lean` (real polynomials): the cone `C_d` as an inductive
  predicate; `C_d·C_e ⊆ C_{d+e}`; `x·C_d ⊆ C_{d+1}`, `x·C_d ⊆ C_{d+2}`,
  `(1+x)·C_d ⊆ C_{d+1}`, `x(1+x)·C_d ⊆ C_{d+3}`; **Lemma C** (every element
  of `C_d` has a non-negative half-gamma expansion of degree `d`); some
  memberships (`1+4x ∈ C_1`, `x(1+5x+3x²) ∈ C_4`). Not formalized: that the
  inductive predicate equals the explicit non-negative sums; a
  non-membership example; uniqueness of the expansion. Verification as
  reported by the agent: `uv run python scripts/verify_lean.py`, verdict
  passed (six checks, six modules replayed), receipt
  `20261126T210612Z-59c47f7bc2-dirty-passed.json` — on a dirty tree, so not
  evidence for a commit; an earlier run of the same script while the
  registry held placeholder fingerprints wrote
  `20261126T205121Z-59c47f7bc2-dirty-failed.json` (registry check only).
  The run on a clean tree after the commit, and its receipt, are in the Git
  history after this entry. The main context read the registered statements
  (`vertex_principle_discrete`, `HalfGammaCone`, `HasNonnegHalfGamma`,
  Lemma C) against the notes and found the differences to be those the
  docstrings state; that is not an independent comparison. MD-0011 (whose
  item (ii) is Lemma C) gets the formal status `partial`.

### What failed

- **Γ is not proved, and neither is (E).** The plan of session 7 for (E) is
  closed by counterexamples; its replacement (Λ) is a conjecture.
- No induction for (Λ) was found: the branch recursion leaves `−x²Φ` and
  `−2x²G`, and the merge rule leaves `−2G_1G_2`.
- No weaker sufficient condition that is easier to prove was found; Γ_w is
  weaker but lacks the product structure.
- The session-7 computations had been run on too small a range of weights
  (0 to 2) to see the failure of (E″); the same caution applies to (Λ),
  tested here with weights up to 20 on random trees and up to 8 on stars.
- `results/rooted-state.json` was produced on a dirty tree at `9069d88`, by
  the script as committed in `59c47f7`; it was not rerun on a clean tree.
- Not done: the revisions of notes owed after earlier reviews (obligation 3);
  obligation 2; a literature search for MD-0015.
- **Lean:** L4 as written is not formalized (the bridge from multi-affine
  polynomials was not attempted); the formalization agent used 37 minutes
  against the 35 allowed, two verification runs taking about 20 of them.
- **Budget.** The reviewer exceeded its computation allowance (about 6.5
  minutes against 4) and reached only one of its planned families of trees.
  Whether the session as a whole stayed within 60 minutes is recorded under
  Telemetry and in the Git history.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (main context, literature auditor, computational experimenter, formalization agent, as far as the environment states); reviewer: see its report |
| Session wall-clock | from 20:28 UTC; this entry was completed at about 21:10 UTC; later steps (verification of the Lean library on a clean tree, the full test suite, push) are in the Git history |
| Computation wall-clock | main context: about 7.5 minutes (scratch runs listed above, trial 41 s, stored run 146 s, later scratch runs about 1 minute); experimenter: about 6.2 minutes as reported by it; tests not counted |
| Literature audit, as reported by the environment | 127,336 subagent tokens, 38 tool calls, 8.6 minutes |
| Computational experimenter, as reported by the environment | 173,199 subagent tokens, 50 tool calls, 15.0 minutes |
| Review of S19 to S22, as reported by the environment | 136,952 subagent tokens, 28 tool calls, 14.8 minutes |
| Formalization agent, as reported by the environment | 129,731 subagent tokens, 41 tool calls, 37.0 minutes |
| Formalization attempts | 2 modules, 8 theorems registered; 1 verification run passed on a dirty tree, 1 failed (placeholder fingerprints); the clean run is after this entry |
| Successful verifications | tests and validation: in the message of the commit that contains this entry and of those after it |
| Token usage of the main session | unavailable |
| Research iterations | 1 objective (O7): the plan through (E″) and (S) refuted; replaced by (Λ) |
| Proof attempts | (★), S19, S20, S21, S22: written once; (Λ): not proved |
| Counterexamples found | to (E″) and (S), statements of this investigation (smallest at 6 and 5 vertices); 0 to the published conjecture, to Γ, Γ_c, (E) or (Λ) |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress, of a mostly negative kind on the main objective. The route
that session 7 proposed for (E) is closed: (E″) and (S) are false, with
explicit counterexamples confirmed by an independent checker and by the
reviewer. What replaces it is a description of `R(T, ν)` by a rooted state
with three rules, in which the obstruction is one explicit negative term, and
a new sufficient condition, (Λ), that survives every test made — on ranges
that are still modest, and with the lesson of this session that such ranges
can mislead. Nothing was promoted: MD-0015 is a candidate with one AI review;
the novelty of MD-0013 and MD-0014 is `preliminary-search-completed`, with
part of MD-0013 identified as implied by a published paper. Lean now has the
discrete vertex principle in any number of variables and the cone `C_d` with
Lemma C.

Next step: objective O8 in `STATE.md` — test statement (Λ⁰) and (Λ) on wider
families, then prove (Λ) or refute it.

## Session 9 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2` (main context, Claude
  Code). Human: G. B. Brito, director, by written instructions at the start:
  maximize valid, original and meaningful discoveries; allocate effort by
  independent judgment; earlier directions and suggestions are revisable;
  do not optimize the number of registered contributions; MD-0013 keeps its
  identifier and review provenance, with known consequences of prior
  literature distinguished from potentially original statements; the current
  classifications are approved; verified commits may be pushed to `research`
  only.
- **Mode:** exploration (21:31 to about 21:45 UTC), then focused work on the
  statement found (Theorem T4). The switch is recorded here.
- **Role(s):** research director; mathematical researcher. Subagents, each in
  its own context: `literature-auditor` (first prior-art search for the leaf
  recursion and star minimality), `adversarial-reviewer` (model
  `claude-opus-5-5` requested; review of `notes/wiener-form.md` at `b5d9294`).
- **Repository revision at start:** `61085bc` (branch `research`, clean tree).
- **What was explored (written before starting):** whether the distance
  polynomial `ℓ_T` of the whole tree — not the coefficient polynomials `r_A`
  of a skeleton — already has a non-negative lower-half gamma expansion, so
  that the chain Γ, L4, "skeleton plus one star" could be bypassed.
- **Objective (exact, from 21:45):** for every tree of order `n ≥ 3`,
  `d_{μ−1} < d_μ` with `μ = ⌊(n−1)/2⌋` (Theorem T4 of `notes/wiener-form.md`).
- **Approach:** an exact identity for `n²ℓ_T` with a single negative term (the
  Wiener form), and the linear functional `λ_μ = [x^μ] − [x^{μ−1}]` on the
  cones `K_d` of non-negative combinations of `x^e(1+x)^i`, `2e + i ≥ d`.
- **Falsification test:** every identity and every sign in the proof against
  exact computation on all small trees before it is written
  (`wiener_form.py`), with `ℓ_T` taken from the distance matrix.
- **Stopping conditions:** mathematics stops at about 22:00 UTC; a failure
  reported by the computation or a gap reported by the reviewer takes
  precedence over everything else.
- **Budget (binding, director's standing decision):** 60 minutes of agent
  work, 21:31 to 22:31 UTC, review, records and push included. Computation:
  at most 30 minutes of wall-clock time in total.
- **Deferred obligations:** 1 to 8 of `STATE.md`, and objective O8 (statement
  (Λ)), deferred for a more promising idea as `AGENTS.md` section 3 allows.
  No claim that depends on them is promoted.

### What was done

All computations are exact (Python integers; python-flint for characteristic
polynomials). Times are UTC, from `date -u` in the session's shell.

1. 21:31 start; `AGENTS.md`, `autoresearch.md`, `STATE.md`,
   `notes/rooted-calculus.md`, `notes/gamma-components.md` and the journal
   entry of session 8 read.
2. Scratch (not stored, each under 30 s): the lower-half gamma vector of
   `ℓ_T` with centre `n − 2`, `n − 1`, `n`, `n + 1` for all trees of order 3 to
   15; the leaf recursion and the one-element polynomials on all rooted trees
   of order at most 9; `ℓ_T + 4x(1+x)^{n−1} ∈ C_{n−1}` for orders 3 to 15;
   `ℓ_T − ℓ_star ∈ C_{n−1}` for orders 3 to 18; `R(B, e_c)/x` for small rooted
   paths and stars.
3. `leaf_telescoping.py` written and committed alone (`6c23eea`) so that its
   stored run starts on a clean tree; stored run 365.5 s
   (`results/leaf-telescoping.json`).
4. `literature-auditor` started at about 21:39 (9-minute budget): section
   "Audit for session 9" of the dossier.
5. The Wiener form and Theorem T4 found by hand (about 21:42 to 21:45);
   `wiener_form.py` written; trial run to order 10 (0 failures); notes
   `wiener-form.md` and `leaf-telescoping.md` written; commit `f414cd8`;
   stored run of `wiener_form.py` on the clean tree at `f414cd8`, 119.7 s
   (`results/wiener-form.json`), committed as `b5d9294`.
6. `adversarial-reviewer` started at about 21:51 on `b5d9294` (fresh context;
   given the catalogue id, the source reference, the path and hash of the
   note, the statement to be registered and the template; not given the
   author's reasoning). Outcome: under Findings.
7. `tests/test_cj0001_wiener_form.py` added (6 tests). Registry: MD-0016 and
   MD-0017 registered; MD-0013 classified item by item in its `limitations`
   (statement, fingerprint and review evidence unchanged; the schema does not
   allow a new key under `novelty_search`, so no key was added). `STATE.md`
   updated; the text of objective O8 and the list of sources read were moved
   to `notes/obligations.md` (verbatim except for the target of one link).

### Findings

- **The Wiener form (Proposition S25; MD-0016, item (i)).** For every tree of
  order `n ≥ 2`: `n²ℓ_T = 4(W − nx)Φ + Σ_{u<v} (t_u − t_v)² x^{dist(u,v)−1} Π_{uv}`,
  with `t = D1`, `W` the Wiener index, `Φ = det(I + xL)` and
  `Π_{uv} = det (I + xL)[V ∖ path(u, v)]`. Written proof (from `Lt = nτ − 2·1`
  and L1). Exact check: 987 trees of order 2 to 12, 56,764 pairs, `ℓ_T` from
  the distance matrix; 0 failures.
- **Theorem T4 (candidate; MD-0016, item (ii)).** For every tree of order
  `n ≥ 3`, `d_{μ−1} < d_μ` with `μ = ⌊(n−1)/2⌋`; so every maximizing index is
  at least `⌊(n−1)/2⌋`. **For odd `n` this is the lower bound of the
  Collins–Shor conjecture; for even `n` it is one less, and the conjectured
  bound is not proved.** Written proof; every sign in it checked on the 987
  trees; the inequality alone on the 499,372 trees of order 13 to 19;
  0 failures. Finite checks are not the proof.
- **Leaf recursion (Proposition S23).** `ℓ_{T+leaf at u} = (1+x)ℓ_T + r_u(T)`,
  `R(T, 0) = xℓ_T − (1+4x)Φ_T`, and the telescoped formula
  `ℓ_T = −4x(1+x)^{n−1} + Σ_k (1+x)^{n−1−k} r_{u_k}(T_k)`. Written proof;
  0 failures on the 4,394 rooted trees of order at most 11.
- **Statement (SM) (new conjecture; MD-0017).** `ℓ_T − ℓ_{S_n} ∈ C_{n−1}` for
  every tree: 0 failures on the 1,346,023 trees of order 3 to 20, equality
  only for the star. It implies the lower bound for every tree, and follows
  from (Γ_c¹), the case of Γ_c with one unit of weight (Proposition S27,
  written proof, unreviewed). (Γ_c¹): 0 failures on the 4,394 rooted trees.
- **Scratch observations, not stored:** the lower-half gamma vector of `ℓ_T`
  with centre `n − 1` and `n − 2` is non-negative for all trees of order 3 to
  15, and fails with centre `n` (already at order 4);
  `ℓ_T + 4x(1+x)^{n−1} ∈ C_{n−1}` for orders 3 to 15; for the star rooted at
  its centre `R(B, e_c) = (j−1) x (1+x)^{j−1}` (orders 2 to 6).
- **Hand computations, not checked by machine and not reviewed:** the rooted
  form `ℓ_T = (1/x) Σ_{u<v} (δ_u − δ_v)² adj_{uv} + 4 Σ_v δ_v adj_{cv} − 4x adj_{cc}`
  (`δ` the distances from any vertex `c`); the formula for `R(B, e_c)` at the
  end of `leaf-telescoping.md`; the edge decomposition in step 2 of the new
  "Next step".
- **Literature audit of session 9 (first search; novelty not established).**
  Nothing found on the leaf recursion, on a coefficientwise or cone-order
  extremality of the star for the distance polynomial, on gamma-type
  expansions for it, or on progress on the lower bound of the peak (arXiv
  listing: 5 entries, the latest of June 2022; 5 citing papers). One unread
  lead: `core.ac.uk/download/10129286.pdf` (HTTP 403), which a search snippet
  describes as building the polynomial leaf by leaf. **No search was made
  for the Wiener form.** Not searched: MathSciNet, zbMATH, Google Scholar,
  MathOverflow, books.
- **MD-0013.** Known consequences of prior literature: `κ ≥ 4` with its
  equality case and item (iv) (Richman–Shokrieh–Wu, through an unreviewed
  bridging step), positive definiteness of `L_B`, and the spectral identity
  used in the proof. Potentially original (no source found within the
  session-8 coverage): the third form, the degree and leading coefficient,
  the real roots.
- **Review of `notes/wiener-form.md` (AI, `claude-opus-5-5`, revision
  `b5d9294`, fresh context):** no gap found within stated scope for Lemma
  S24, Propositions S25, S26, Lemma A, Theorem T4 and its corollary, each
  reconstructed by hand; the registered wording of MD-0016 matches what is
  proved; the note is plain about the even case. Reviewer's own exact code:
  5,450 trees of orders 2 to 14 and special trees up to order 40, 50,262
  adjugate entries, 10,882 cases of Lemma A; no counterexample. Three
  defects of wording, none mathematical (owed: one revision, then a
  recheck). Of `leaf-telescoping.md` it checked S23(d), S27(a), (b) and the
  algebra of S27(c); **S23(a) to (c) are unreviewed**. Not covered: the
  literature, the external facts, the dependencies L1, Lemma F, Lemma C.
  This is one AI review by a model of the same vendor; it is not human
  review, and T4 stays a candidate theorem.
- **Scratch runs made while the review was running (exact, not stored):**
  the two hand formulas (the rooted form of `ℓ_T`; the pair formula for
  `R(B, e_c)`) hold on the 326 rooted trees of order at most 8; the right
  side of inequality (3) of `wiener-form.md` is positive for every tree of
  even order 4 to 14 and is at least 72% of `n²(d_m − d_{m−1})`.
- **A family of identities (hand computation at the end of the session, not
  checked by machine except in the two cases named, not reviewed).** For
  every real vector `π` on the vertices with `1ᵀπ = 1` and `f = Dπ`:
  `ℓ_T = −2(πᵀDπ)Φ + (1/x) Σ_{u<v} (f_u − f_v)² adj_{uv} + 4 πᵀ adj f − 4x πᵀ adj π`
  (from `Lf = τ − 2π`). The uniform `π` gives the Wiener form (S25, checked);
  `π = e_c` gives the rooted form (checked in scratch). Other choices of `π`
  have not been examined; they are a possible tool for the even orders.

### What failed

- A lower-half gamma expansion of `ℓ_T` with centre `n` (what the even case
  would need) fails already at order 4.
- A proof of (Γ_c¹), hence of (SM), was not found: removing a leaf that is
  not adjacent to the root leaves the family of unit weights.
- The even case of the lower half is not reached by the Wiener form as it
  stands (the edge polynomials are in `K_{n−2}` only).
- `STATE.md` has 418 lines, above the aim of 400.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author); `claude-fable-5-2` (literature auditor); reviewer: see its report |
| Computation wall-clock | stored runs 365.5 s + 119.7 s; scratch and trial runs about 90 s; test suite: see "Outcome" |
| Token usage | main context unavailable; subagents as reported by the environment: literature auditor 50,431 tokens, 23 tool uses, 146 s; reviewer 83,268 tokens, 21 tool uses, 360 s |
| Research iterations | 1 exploration, 1 focused objective |
| Proof attempts | 2 (T4: complete written proof; (Γ_c¹): not found) |
| Counterexamples found | 0 |
| Formalization attempts | 0 |
| Successful verifications | stored runs of `leaf_telescoping.py` and `wiener_form.py` (0 failures); `catalogue.py validate`; the test suite (under Outcome); one independent AI review of T4 (no gap found) |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress. **Theorem T4 (candidate, one AI review, no gap found):
for every tree of order `n ≥ 3` the peak of the normalized coefficients is at
least `⌊(n−1)/2⌋` — the lower bound of the Collins–Shor conjecture for trees
of odd order.** It rests on the Wiener form of `ℓ_T` (Proposition S25). It is
not an established result of the project: no human reader, originality
unknown, and for even order the conjectured bound is not proved. New
conjecture (SM) (MD-0017), exact to order 20, which would give the lower
bound for every tree. Records: `notes/wiener-form.md`,
`notes/leaf-telescoping.md`, MD-0016, MD-0017, the classification of MD-0013.

Verification commands (revision of the commit that contains this entry,
except where a revision is named): `wiener_form.py` at `f414cd8` and
`leaf_telescoping.py` at `6c23eea`, clean tree at start, 0 failures;
`uv run python scripts/catalogue.py validate`: 15 problems, 17 contributions,
0 errors; `render --check`: up to date. Test suite: a first full run,
started before the session's records were complete, gave 2 failed, 176 passed in 425 s.
`test_committed_registry_is_valid_and_summary_is_current` failed because it
read the registry while this session was still writing it, before the views
were regenerated. The link
check `test_relative_markdown_links_resolve` failed for two reasons — a link
moved with the text of O8 into `notes/obligations.md` (target corrected), and
the formula `[x^μ](xg)` inside inline code in `wiener-form.md`, which the
check read as a link (the check now ignores inline code, as Markdown does;
the reviewed note was not touched). Second full run on the final tree:
178 passed in 388 s. `verify_lean.py` was not run: no Lean source changed.

A tooling change of this session, with its reason: `tests/test_repository.py`
(the link check, above). Budget: 21:31 to about 22:12 UTC of the 60 minutes;
computation about 10 minutes of wall-clock time in stored and scratch runs,
plus the test suite.

Next step: objective O9 in `STATE.md` (the even orders, from inequality (3)
of `wiener-form.md`), after obligation 9 (the revision of `wiener-form.md`
for the three defects of wording and its recheck; a review of
`leaf-telescoping.md`; a literature search for the Wiener form). Decisions
left to the director: whether CJ-0001 moves to `partial-result` once T4 has
had a human reader; whether T4 should be shown to a specialist.

## Session 10 — 2026-11-26

- **Agent / model:** Claude, model `claude-fable-5-2` (main context, Claude
  Code). Human: G. B. Brito, director, by written instructions at the start:
  continue under the existing harness; MD-0016 is a significant candidate
  result and is to receive independent validation and an originality
  assessment before promotion (a preliminary reading by GPT-6.2 found no
  apparent gap in the principal steps, and is not a complete proof audit);
  CJ-0001 keeps its status until the validation requirements are met; the
  AI investigator chooses the next direction by its own judgment; verified
  commits may be pushed to `research` only.
- **Mode:** focused work on two objectives (below), with a short exploration
  inside the second, recorded as such.
- **Role(s):** research director; mathematical researcher. Subagents, each in
  its own context: `literature-auditor` (model `claude-fable-5-2`;
  originality of MD-0016), `formalization-agent` (model `claude-fable-5-2`;
  Lemma A and the cones `K_d` in Lean), `adversarial-reviewer` (model
  `claude-opus-5-5`; complete proof audit of Theorem T4 at `a3e5179`).
- **Repository revision at start:** `b217dcc` (branch `research`, clean tree).
- **Objective 1 (obligation 9, owed first):** validation of MD-0016 — the one
  revision of `notes/wiener-form.md` for the three defects of the review of
  `b5d9294`, a recheck by a fresh context in the form of a complete proof
  audit, a literature audit for the Wiener form and the bound on the peak,
  and Lean for Lemma A and the cones.
- **Objective 2 (O9, exact):** for every tree of even order `n = 2m`,
  `d_{m−1} < d_m`; or find the obstruction. Start from inequality (3) of
  `wiener-form.md`.
- **Approach (objective 2):** split `Φ = (1+x)^{n−1} + xΘ` (the first part is
  invisible to `λ_m`) and compare `Θ` with the edge polynomials in the cone
  `K_{n−2}`; if that fails, find where the Wiener form loses the even case.
- **Falsification test:** the cone inequality on all small trees and then on
  large members of the worst family, before any attempt at a proof.
- **Stopping conditions:** mathematics stops at about 23:10 UTC; a gap
  reported by the audit takes precedence over everything else.
- **Budget (binding, director's standing decision):** 60 minutes of agent
  work, 22:39 to 23:39 UTC, reviews, records and push included.
  Computation: at most 30 minutes of wall-clock time in total. Subagents:
  12 minutes (literature), 22 minutes (Lean), 14 minutes (audit).
- **Deferred obligations:** 1 to 8 of `STATE.md`; the review of
  `leaf-telescoping.md`. No claim that depends on them is promoted.

### What was done

All computations are exact (Python integers; python-flint for characteristic
polynomials). Times are UTC, from `date -u` in the session's shell.

1. 22:39 start; `AGENTS.md`, `autoresearch.md`, `STATE.md`,
   `notes/wiener-form.md`, `notes/leaf-telescoping.md`, the journal entry of
   session 9 and the findings of the review of `b5d9294` read.
2. 22:41, in parallel: `literature-auditor` (originality of MD-0016; it wrote
   the dossier section "Audit for session 10") and `formalization-agent`
   (`WienerCone.lean`).
3. Scratch (not stored, each under 1 minute): the cone inequality
   `Θ_T − w Σ_e Π_e ∈ C_{n−2}` (largest `w` per tree; it decreases from `1/2`
   at order 4 to `49/192` at order 15, on spiders with legs of length 2);
   the refined statement `4(W − 3n)Θ_T − 16n(1+x)^{n−2} − Σ_e (n − 2n_e)² Π_e ∈ C_{n−2}`,
   which would imply that the right side of inequality (3) is positive: no
   failure on the trees of order 7 to 15, **failure** on spiders with legs of
   length 2 at `n = 30, 40, 60, 80`; then inequality (3) itself on large
   paths, stars, brooms and spiders: **negative at `n = 100`** for the spider
   with 49 legs of length 2 and one pendant vertex.
4. `notes/wiener-form.md` revised once (the three defects; Lemma K; a section
   on prior literature; no statement changed) and committed with the dossier
   section as `a3e5179`. `adversarial-reviewer` started on `a3e5179` (fresh
   context; given the source reference, the two note paths with their
   hashes, the registered statement and the template; told not to read the
   journal, `STATE.md` or the earlier review; not given the author's
   reasoning).
5. The rooted form, the explicit leaf polynomial and the remainder `Ω_T`
   derived by hand; `even_order.py` written with a second determinant routine
   that uses no characteristic polynomial; trial run; `notes/even-order.md`
   written; `tests/test_cj0001_even_order.py` (6 tests).
6. The seven Lean statements compared with the note by the author of the
   session and registered; commit `5db7165`; stored run of `even_order.py` on
   the clean tree at `5db7165`, 39.6 s (`results/even-order.json`, commit
   `f1e3364`); `scripts/verify_lean.py` on the clean tree (under Outcome).
7. Scratch (not stored): the "vertical groups" of the leaf polynomial (for a
   vertex `b` at depth at least 2, the terms of `Ω_c` indexed by `b` and its
   ancestors) are **not** all in the cone `C_k`: no failure up to order 7,
   5 failures of 966 at order 8, 56 of 7,632 at order 10.
8. Registry: MD-0016 updated (evidence, formal `partial`, novelty
   `preliminary-search-completed` with its search record), MD-0017 ((SM⁺)
   recorded), MD-0018 registered. `STATE.md` updated.

### Findings

- **Complete audit of Theorem T4 (AI, `claude-opus-5-5`, revision `a3e5179`,
  fresh context, independent of the first review): no gap found within
  stated scope.** Re-proved by hand: Lemma K, (K1), (K2), Lemma S24,
  Propositions S25 and S26, Lemma A, Theorem T4, the corollary, and the
  dependencies L1 (from the Graham–Pollak determinant and the Graham–Lovász
  inverse, the inverse itself re-proved), L2 and R1. The registered statement
  of MD-0016 is what is proved; the note is plain about even order.
  Reviewer's own exact code: 533 trees of orders 2 to 11 (20,398 pairs) for
  every identity; 285 weighted trees for Lemma K; 237,471 grid points for
  Lemma A; 32,413 trees of orders 10 to 16 for T4; families to order 40; no
  counterexample. Not re-proved: the Graham–Pollak determinant; Theorem 2.1
  of the source (log-concavity). **Five defects of citation and wording,
  none mathematical** (D1: S26 and the tools list still cite Lemma F; D2: the
  edge formula for `W` is uncited; D3: L1 is stated for `n ≥ 3` and used at
  `n = 2`; D4: the `C`-clause of S24 rests on Lemma F, disclosed; D5: Lemma K
  is a strong induction). Owed: one revision, then a recheck. This is a
  second AI review by a model of the author's vendor. It is not human
  review; T4 stays a candidate theorem and CJ-0001 keeps its status.
- **Originality of MD-0016 (first search; not established).** Known, through
  bridging steps written by the auditor and not reviewed: the first equality
  of Lemma S24 (path expansion of a cofactor, Maybee–Olesky–van den
  Driessche–Wiener 1989, read only as quoted in Chebotarev–Shamis) and
  `Lt = nτ − 2·1` (from the Graham–Lovász inverse). **No source found, within
  a thin coverage, for the Wiener form (S25) or for the bound of T4.** The
  2014 survey of Aouchiche and Hansen (read directly, p. 307) says of the
  conjecture: "No more results are known about that conjecture"; the two
  follow-up papers (machine summaries only) prove nothing on the peak for
  trees. Unread: Collins 1989, Collins's thesis (HTTP 403 and 429), Merris
  1990, Graham–Lovász pp. 72–88, Bapat's book. Not searched: MathSciNet,
  zbMATH, Google Scholar. The Wiener form is a few lines from known
  ingredients, so a prior statement in an unread source is plausible.
- **Lean (`WienerCone.lean`, no `sorry`):** the cones `K_d` as an inductive
  predicate with (K1) and (K2); Lemma A(a) and A(b) on the cone, with the
  strict form of A(b) under `f(0) > 0`, which is the form the proof of T4
  uses. Nothing about trees or determinants. Seven theorems registered.
- **Inequality (3) of `wiener-form.md` is false in general (Finding S31).**
  For the spiders with `(n−2)/2` legs of length 2 and one pendant vertex its
  right side is positive for even `n` from 80 to 98 and negative from 100 to
  110 (two implementations agree at every order); `d_{m−1} < d_m` holds on
  all of them. Step 1 of the "Next step" of session 9 is refuted as a route.
- **Rooted form (Proposition S28), leaf polynomial (S29), remainder (S30);
  MD-0018, candidate, unreviewed.** `ℓ_T = (1+4x)Θ_T − 4x(1+x)^{n−1} + Ω_T`
  with `xΘ_T = Φ − (1+x)^{n−1}` and `Ω_T` a polynomial with non-negative
  coefficients, equal to `Σ_k (1+x)^{n−1−k} Ω_{u_k}(T_k)` for every
  construction of the tree leaf by leaf, each `Ω_c` given by an explicit
  formula. **For even `n = 2m ≥ 4`:
  `d_m − d_{m−1} ≥ (n−1)(3m−5)/(m+1)·Cat_{m−1} + λ_m(Ω_T)`**, with equality
  for the star. So the lower bound for even order follows from
  `λ_m(Ω_T) ≥ 0`, and only the "deep edge" terms of `Ω_T` can be negative
  under `λ_m`. Exact checks: S28 and S29 on 748 rooted trees (orders 2 to
  9); `Ω_T ≥ 0` on the 13,186 trees of order 3 to 15; 0 failures. This
  proves the non-negativity of `Ω` in the unweighted case, which `STATE.md`
  listed as observed and unproved.
- **Statement (SM⁺):** `Ω_T ∈ C_{n−1}` for every tree: 0 failures on the
  13,186 trees of order 3 to 15, `Ω_T = 0` only for the star.
  `(Γ_c¹) ⇒ (SM⁺) ⇒ (SM)`. Recorded under MD-0017.
- **The leaf remainder as a quadratic form (hand computation; exact scratch
  check, not stored, not reviewed).** For a rooted tree `(B, c)` with
  `M¹ = I + xL¹`, `L¹ = L_B + e_c e_cᵀ`, `Φ¹ = det M¹` and `δ` the distances
  from `c`: `R(B, e_c) = δᵀ(Φ¹·I − adj M¹)δ = x δᵀ L¹ adj(M¹) δ`, that is
  `R(B, e_c) = Σ_i (δ·w_i)² xθ_i Π_{l≠i}(1 + θ_l x)` over an orthonormal
  eigenbasis `(θ_i, w_i)` of `L¹`. Checked on the 326 rooted trees of order
  at most 8, with `R(B, e_c)` taken as `Ω_u` of the tree `B` plus a pendant
  vertex `u` at `c`, computed from distance matrices. So (Γ_c¹) is a
  statement about the spectral measure of `δ` for the grounded Laplacian.
- **Scratch, not stored:** (SM⁺) also holds for paths, brooms, double
  brooms and four kinds of spiders at `n = 30, 60, 100, 150`, and there
  `λ_m(Ω_T)` is between 0.59 and 10¹⁸ times the star's margin
  `(n−1)(3m−5)/(m+1)·Cat_{m−1}`: far from the star the remainder is
  enormous, and the tight cases are the trees close to the star (for the
  star with one subdivided edge, `Ω_T = (n−3)x(1+x)^{n−3}` and
  `λ_m(Ω_T) = 0`, by hand).
- **Hand computation, not checked by machine:** the identity
  `xΩ_T = R(T, 0) + (1+2x)²(1+x)^{n−1}`.

### What failed

- A proof of the lower bound for even order: not found.
- The route through inequality (3) (S31), and the cone statement that would
  have implied it (item 3).
- The vertical groups of the leaf polynomial are not in the cone (item 7).
- A term by term comparison of one deep-edge term with the terms of `Ω_c`
  at higher level fails when the vertices near the edge have large degree
  (hand estimate, not written out).
- The audit found five defects in the revision of `wiener-form.md`, so the
  note needs a second revision (the session's rule allows one per review).
- Collins's thesis could not be read (HTTP 403, HTTP 429).

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author, literature auditor, formalization agent); `claude-opus-5-5` (reviewer, as reported by it) |
| Computation wall-clock | stored run 39.6 s; scratch and trial runs about 80 s; `verify_lean.py` twice and the test suite: see "Outcome" |
| Token usage | main context unavailable; subagents as reported by the environment: literature auditor 120,001 tokens, 34 tool uses, 359 s; formalization agent 98,005 tokens, 24 tool uses, 748 s; reviewer 79,578 tokens, 21 tool uses, 451 s |
| Research iterations | 2 focused objectives, 1 exploration inside the second |
| Proof attempts | 2 (S28 to S30: complete written proofs; the even case: not found) |
| Counterexamples found | 1 (to the positivity of the right side of inequality (3), order 100; not to the conjecture) |
| Formalization attempts | 1 (complete for its scope) |
| Successful verifications | one independent AI audit of T4 (no gap found); stored run of `even_order.py` (0 failures); `lake build` and `verify_lean.py`; `catalogue.py validate`; the test suite (under Outcome) |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress on validation, and a reduction — not a proof — for the even
orders.

**MD-0016 (Theorem T4) stays a candidate and CJ-0001 keeps its status.** It
now has two independent AI reviews with no gap found (the second a complete
proof audit of the revised, self-contained note), a first literature audit
that found no prior statement of the Wiener form or of the bound within a
thin coverage (novelty `preliminary-search-completed`), and Lean for Lemma A
and the cones (formal `partial`). What promotion still needs is in
obligation 9 of `STATE.md`: one more revision of the note for the five
defects of wording and its recheck; a reader outside the author's vendor or
a human reader; the unread sources (Collins 1989 and thesis first); a result
package. None of this session's reviews is human review.

**Even orders.** Not proved. New: the decomposition
`ℓ_T = (1+4x)Θ_T − 4x(1+x)^{n−1} + Ω_T` with `Ω_T ≥ 0` coefficientwise and the
bound `d_m − d_{m−1} ≥ (n−1)(3m−5)/(m+1)·Cat_{m−1} + λ_m(Ω_T)` (MD-0018,
candidate, unreviewed); the conjecture (SM⁺); and the negative result that
inequality (3) of `wiener-form.md` fails at order 100.

Verification commands: `uv run python even_order.py --max-a 9 --max-b 15 --max-c 14 --family 80 110 --out results/even-order.json`
at `5db7165`, clean tree at start, 0 failures, 39.6 s.
`lake build` (formalization agent, tree `a3e5179` plus the new file):
"Build completed successfully (2738 jobs)". `uv run python scripts/verify_lean.py`
at `f1e3364`, clean tree: VERDICT passed, receipt
`verification/receipts/20261126T230958Z-f1e33649ee-passed.json` (an earlier
run with `--show-fingerprints --no-receipt`, made to obtain the fingerprints
of the seven new entries, reported "failed" as it must while they were
unset). `uv run python scripts/catalogue.py validate`: 15 problems,
18 contributions, 0 errors; `render --check`: up to date at the commit that
contains this entry. Test suite (`uv run pytest`): 184 passed in 642.76 s, on the
tree of the commit that contains this entry except for this sentence and the
end time below, which were filled in after the run.

Budget: 22:39 to about 23:26 UTC of the 60 minutes. Computation: about
2 minutes of stored, trial and scratch runs; `verify_lean.py` twice (about
5 minutes each) and the test suite are in addition. `STATE.md` has 434 lines,
above the aim of 400, after moving the chain of sufficient conditions for
Conjecture Γ to `notes/gamma-chain.md` (verbatim).

Next step: objective O10 in `STATE.md` (a lower bound for `λ_m(Ω_T)`, or
(SM⁺)), after obligation 9. Decisions left to the director: who reads T4
outside the author's vendor, and whether Collins's thesis can be obtained
(the copies reachable from this environment refused automated access).

## Session 11 — 2026-11-26

- **Entry status:** completed (closed at the end of the session; it was
  marked "in progress" until then).
- **Agent / model:** Claude, model `claude-fable-5-2` (Research Director,
  main session), until the session was interrupted during its closing
  steps; the closing steps after the interruption by Claude, model
  `claude-opus-5-5` (see "Interruption and resumption" at the end of this
  entry). Human participant: the director, who supplied the two
  Collins sources as local files and the instructions recorded below.
- **Mode:** focused work for the literature objective; exploration for the
  even orders, which became focused work when an induction closed (the
  switch is recorded in the first checkpoint).
- **Role(s):** Research Director; literature reading (both sources read by
  the main session); mathematical research; computation.
- **Repository revision at start:** `759d93f` (`research`), the harness
  commit of this session (session budget of 120 minutes, checkpoints),
  promoted to `main` as `2b687db` by cherry-pick before the research began.
- **Director's instructions for this session:** read Collins (1986) and
  Collins (1989), now available locally, and reassess the originality and
  the implications of the project's results (leaf recursion, Wiener form,
  T4); rely on independent AI review, adversarial verification, exact
  computation and Lean for the current phase, human specialist consultation
  being deferred until there is a mature manuscript; allocate effort by
  independent mathematical judgment; do not optimize the number of
  registered contributions; verified commits may be pushed to `research`
  for research contributions. The PDFs are not to be committed.
- **Objective (exact):** (1) Record, for each of S23 (leaf recursion), S25
  (Wiener form), T4, S23(d) (the star) and the statement of the conjecture,
  whether Collins's thesis or her 1989 paper contains it, an equivalent, or a
  precursor, with page and statement numbers. (2) Explore the even orders
  from a new side: the behaviour of `ℓ_T` when a non-pendant edge is
  contracted and a pendant vertex is added.
- **Approach:** (1) read both sources in full. (2) the rooted calculus of
  `notes/rooted-calculus.md` (plant, merge) applied to the two trees.
- **Falsification test:** for (2), the exact test of
  `ℓ_T − ℓ_{T'} ∈ C_{n−1}` on every tree and every non-pendant edge of small
  order, run first.
- **Stopping conditions:** (1) both sources read and compared. (2) stop if
  the contraction statement fails on small trees, or if no proof structure
  appears within about 40 minutes.
- **Budget:** time: at most 120 minutes, the last 20 or so reserved for
  verification, documentation and persistence; the research began at 22:22
  local time (UTC−3; 01:22 UTC on 2026-11-27), while the test suite of the
  harness commit was running, so the ceiling is 00:22 local and the working
  part ends at about 00:02. Computation: 30 minutes of wall-clock time,
  largest instance: all trees of order 16. Tokens: not limited by the
  director; not reported by the environment for the main context.

### Checkpoints

- **+17 min (22:39 local, clock reading):** *Established.* Both Collins
  sources read (the 1989 paper from its nine page images; the thesis from
  page images for pp. 30–47 and 55–61 and from its OCR text layer for the
  rest); the comparison is not yet written in the dossier. Exact, scratch
  only: `ℓ_T − ℓ_{T'} ∈ C_{n−1}` for every tree of order 4 to 16 and every
  non-pendant edge (216,000 pairs, no failure). Derived by hand and checked
  exactly on every rooted tree of order ≤ 9 (486 rooted trees, 778 pairs):
  the formula `ℓ_T − ℓ_{T'} = H_A E_B + H_B E_A + x(2+5x)H_A H_B + 2G_A G_B/x`
  with `E = R − Ω + (1+2x)²Ψ − 2xG`; `H = Σ_v x^{δ_v−1}Π_{uv}`,
  `G = Σ_v (δ_v−1)x^{δ_v}Π_{uv}`; the plant rule
  `E^ = x[E + Ω + 2G + x(3+2x)H]` and the merge rule
  `E = E_1Ψ_2 + E_2Ψ_1 + x(H_1Ω_2 + H_2Ω_1) − 2G_1G_2`; and an identity that
  turns the negative term of the merge of two planted trees into a sum of
  squares. With these an induction on rooted trees appears to close for the
  system `Ψ ∈ C_{a−1}`, `H ∈ C_{a−2}`, `G/x ∈ C_{a−1}`, `Ω ∈ C_a`,
  `E ∈ C_{a+1}`; it would give (Γ_c¹), hence (SM) and the lower bound
  `⌊n/2⌋` for every tree. **Not written, not reviewed: a candidate
  argument in the author's head and in scratch files only.** The mode
  switches to focused work: write the proof, store the computation, obtain
  an independent review. *Unfinished, and where:* scratch scripts
  `contract_test.py`, `cm_formula.py`, `system_check.py` in the session's
  scratch directory (outside the repository). *Next action:* write
  `notes/contraction.md`.
- **+40 min (23:02 local, clock reading):** *Established since the last
  checkpoint.* `notes/lower-bound.md` written and committed at `74d65b0`
  (S32 to S36, Theorems T5 and T6; a candidate proof, **unreviewed**). The
  identities it uses were checked exactly in scratch on every rooted tree of
  order ≤ 9 before it was written (486 rooted trees, 778 pairs, no failure;
  the count of contraction pairs of the first checkpoint is 220,181, not
  "216,000"). The dossier has the reading of Collins (1986) and Collins
  (1989), with exact checks of the formulas read (scratch `collins_check.py`:
  star and path formulas for orders 3 to 30, Table 1 row 9, Theorem 4 of the
  thesis on 142 pairs). `STATE.md` partly updated (results table, dependency
  map, decisions, obstacles); its obligations and next step are **not yet
  rewritten**. *Unfinished, and where.* Four delegated tasks are running in
  fresh contexts: two adversarial reviews of `lower-bound.md` at `74d65b0`
  (one by `claude-opus-5-5` if the environment grants it, one emphasising an
  independent machine re-derivation), the stored computation
  `experiments/CJ-0001-collins-shor-peak/lower_bound.py` with its test, and
  a Lean file `LowerBoundCone.lean` for the cone arithmetic of T5 and S35.
  None has reported. A scratch exploration for the upper half is running
  (orders 13 to 15): along generalized tree shifts the peak never moved up
  for orders 5 to 12 (exact, scratch, 6,809 shifts); the ratio
  `d_{k+1}/d_k` is *not* monotone along them for `k` above about `n/2`.
  *Next action:* read the reports as they arrive; then registry, obligations,
  next step, verification.
- **+58 min (23:20 local, clock reading; correction: the previous checkpoint
  was written at 22:57, +35 min, not at 23:02):** *Established since the
  last checkpoint.* Both reviews returned "no gap found within stated scope"
  (reports committed at `77a8bc8`). The stored computation exists and was
  rerun on a clean tree at `b1359cc` (1,040,693 checks, 0 failures; result
  committed at `6e6432c`). The literature audit is in the dossier.
  `LowerBoundCone.lean` is committed (`b1359cc`); `verify_lean.py
  --no-receipt` passed on the working tree, as reported by the formalizing
  agent. `STATE.md` is rewritten (commits `8b4139e`, `b1359cc`). New
  observations, scratch only: (GS), (PX), and the bilinear form of the tree
  shift for path lengths up to 9. *Unfinished, and where.* `verify_lean.py`
  is running on the clean tree `6e6432c` for the receipt; the registry
  (MD-0019, MD-0017), the catalogue fields about Collins, the generated
  views, the full test suite and the rest of this entry are not done. The
  configuration for the registry update is in the scratch directory
  (`registry_s11.py`, `reviews.json`). *Next action:* apply the registry
  update when the receipt is written, validate, run the test suite, close
  this entry. No new mathematics in what remains of the session.

### What was done

Harness first (not research): the session budget of 120 minutes and the
checkpoints, commit `759d93f` on `research`, cherry-picked to `main` as
`2b687db`; `uv run pytest` on `research` 185 passed (680 s); on `main` the
tests that do not need Lean, 42 passed, and the catalogue checks; CI passed
on both branches, Lean job included.

Reading. Collins (1989) in full from its page images; Collins (1986):
pp. 30–47 and 55–61 from page images, the rest from the OCR text layer
(formulas of pp. 13–29 and 48–54 not reliably legible). The comparison is in
the dossier, section "Primary sources read in session 11". Exact scratch
checks of what was read (`collins_check.py`, run with
`uv run --with sympy`, not stored): the star and path formulas of the 1989
paper for orders 3 to 30, Table 1 row `n = 9`, Theorem 4 of the thesis with
leaf weight 1 and its dictionary with `r_u` on 142 (tree, vertex) pairs.

Mathematics. Falsification test first: `ℓ_T − ℓ_{T′} ∈ C_{n−1}` for the
contraction of a non-pendant edge, all trees of order 4 to 12 (no failure),
then 13 to 16. Then, by hand: the formula of S36 from the plant and merge
rules; the formulas `H = Σ a_v`, `G = xΣ(δ_v − 1)a_v` from `Lδ = τ − 2e_u`;
the quadratic form of `R(A, e_u)`; the polynomial `E` and its rules; the
identity for two planted trees. Each was checked exactly in scratch before
it was relied on (`cm_formula.py`, `system_check.py`). A first attempt to
prove `E ∈ C_{a+1}` term by term from its explicit positive formula failed
(see "What failed"); the induction that works keeps `Ω` and `R(A_l, e_{c_l})`
whole. Written as `notes/lower-bound.md`, committed at `74d65b0`.

Delegated, each in a fresh context:

- adversarial review, `claude-opus-5-5`:
  `reviews/2026-11-26-claude-opus-5-5-T5-T6-lower-bound.md`;
- adversarial review with a machine re-derivation, `claude-fable-5-2`:
  `reviews/2026-11-26-claude-fable-5-2-T5-T6-lower-bound-machine.md`;
- stored computation and test (computational-experimenter,
  `claude-fable-5-2`): `experiments/CJ-0001-collins-shor-peak/lower_bound.py`,
  `tests/test_cj0001_lower_bound.py`;
- Lean (formalization-agent, `claude-fable-5-2`): see "Findings";
- literature audit (literature-auditor, `claude-fable-5-2`): the dossier,
  section "Audit for session 11".

Exploration for the upper half (scratch, not stored): `ratio_test.py`
(exact) and `upper_cone.py` (floating-point LP, exploratory).

### Findings

Each with its level of evidence. Nothing is promoted in this session.

1. **Theorem T5 (statement (Γ_c¹)) and Theorem T6: for every tree of order
   `n ≥ 3`, `d_{m−1} < d_m`, `m = ⌊n/2⌋`** — the lower half of the
   Collins–Shor conjecture for every tree — with star minimality (SM) on the
   way. Level: **candidate proof**, written (`notes/lower-bound.md`); two
   independent AI reviews of revision `74d65b0`, both "no gap found within
   stated scope" (one by a different model of the same vendor, with every
   step and the unreviewed S23(a) to (c) reconstructed by hand; one by the
   author's model in a fresh context, with a machine re-derivation from the
   definitions); exact checks by three independent codes (the stored
   script; each reviewer's own): T6(b), (c) on all trees of order ≤ 18.
   Not a human review; S19 was not re-derived by either reviewer; novelty
   not established. Registered as MD-0019; MD-0017 (the conjecture (SM)) now
   has a candidate proof.
2. **Proposition S36**: the explicit formula for `ℓ_T − ℓ_{T′}` under the
   contraction of a non-pendant edge, and its membership in `C_{n−1}`. Level:
   candidate proof, same reviews (the identity was expanded by hand by one
   reviewer and machine-checked by both); exact on 220,181 pairs for the
   membership.
3. **Literature.** S23(d) is Collins 1989, Theorem 1 (known). The leaf
   recursion has a precursor in Theorem 4 of Collins's thesis, and the merge
   rule in its Theorem 7; neither source contains the Wiener form, T4, or
   anything like T5, T6, S36. Conjecture 9 has no floor or ceiling; the
   floor is the only reading consistent with Theorem 1 of the same paper.
   Level: first-hand reading, with the stated limit on the OCR pages.
4. **Upper half, observations only.** (PM): along generalized tree shifts
   the peak never moved up, orders 5 to 15, 127,192 shifts (exact, scratch).
   The ratio `d_{k+1}/d_k` is not monotone along shifts for `k ≥ ⌊n/2⌋`.
   Floating-point LP (exploratory): the truncated `ℓ_T` is in the cone of the
   `x^e(1+x)^i` with `2e + i ≤ 2M + 1` for all trees of order 5 to 14, with no
   margin at order 14 for two trees close to the star.
5. **Generalized tree shift and path maximality, observations.** (GS):
   `ℓ_T − ℓ_{T′} ∈ C_{n−1}` along the shift of Csikvári for a path of any
   length — exact, scratch, every tree of order 5 to 13 and every shift, no
   failure. (PX): `ℓ_{P_n} − ℓ_T ∈ C_{n−1}` for the 81,134 trees of order 4 to
   17 (exact, scratch). The bilinear form of the shift along a path of
   length `k`, computed symbolically in free state variables for `k = 1` to
   `12` (sympy, scratch), is
   `x(ℓ_T − ℓ_{T′}) = x a_{k−1}(H_AE_B + E_AH_B) + 2γ_k G_AG_B + 2x²γ_{k−1}(H_AG_B + G_AH_B) + x²[2(1+x)γ_k + 3x a_{k−1} + xΣ_{i=0}^{k−2}(i+1)(k−1−i)x^i a_{k−2−i}] H_AH_B`,
   with `a_j` the determinant of the `j × j` tridiagonal matrix with `1 + 2x`
   on the diagonal and `−x` beside it (`a_0 = 1`) and
   `γ_k = Σ_{i<k} x^i a_{k−1−i}`. Every coefficient is non-negative, and with
   `a_j ∈ K_j` (Lemma K), T5 and S33 every term is in `K_{n−1}`. So (GS) for
   path lengths at most 12 would follow from T5 and a computer-algebra
   identity, and the general case from a proof of this closed form by
   induction on `k` — **none of this is written as a proof, the level count
   was done by hand once, and nothing here is reviewed**. Not
   registered; `STATE.md`, objective O12.
   The whole of the symbolic computation, so that it can be repeated
   without the scratch directory (run with `uv run --with sympy python`):

   ```python
   import sympy as sp
   x = sp.symbols("x")
   def plant(s):            # state (Psi, H, G, Omega, E); Proposition S34(b)
       P, H, G, O, E = s
       return ((1+x)*P + x*H, P + x*H, x*(x*H + G), E + (1+x)*(O + x*H),
               x*(E + O + 2*G + x*(3+2*x)*H))
   def merge(s, t):         # Proposition S34(c)
       P1, H1, G1, O1, E1 = s; P2, H2, G2, O2, E2 = t
       return (P1*P2, H1*P2 + H2*P1, G1*P2 + G2*P1, O1*P2 + O2*P1,
               E1*P2 + E2*P1 + x*(H1*O2 + H2*O1) - 2*G1*G2)
   def xl(s):               # x * l_T, from S23(a) and the definition of E
       P, H, G, O, E = s
       return E + O + 2*x*G + x*(1+4*x)*H - 4*x**2*P
   A = sp.symbols("PA HA GA OA EA"); B = sp.symbols("PB HB GB OB EB")
   sA, path = A, (sp.Integer(1), 0, 0, 0, 0)
   for k in range(1, 13):   # shift along a path of length k
       sA, path = plant(sA), plant(path)
       print(k, sp.factor(sp.expand(xl(merge(sA, B)) - xl(merge(merge(A, B), path)))))
   ```
6. **Lean** (formalization-agent, fresh context): `formalization/Conjectura/Research/CollinsShorPeak/LowerBoundCone.lean`,
   six registered theorems (`plant_E_mem`, `raised_R_mem`, `sum_sq_identity`,
   `two_planted_identity`, `two_planted_mem`, `two_planted_lhs_mem`): the
   cone arithmetic of the plant step and of the step "(iii) from (i) and
   (ii)" in the proof of T5, and the identity and the membership of S35,
   for arbitrary real polynomials with the memberships as hypotheses and
   orders at least 2. **Nothing about trees, the rooted state, S19, Lemma
   K, S32, the induction of T5 or T6 is formalized.** The first build
   failed on three proof steps, which were repaired without changing a
   statement. The Lean statements were compared with the note by the
   formalizing agent and by the author (the main session read the six
   statements against S34(b), S35 and the proof of T5): no independent
   comparison. Formal status of MD-0019: `partial`, with this scope.

### What failed

- Proving `E ∈ C_{a+1}` directly from the positive formula
  `E = 2(1+x)G + Σ_{(ii)} + Σ_{(iii)}` (sum over pairs of vertices): the
  terms `x²Π_{e∪{u,y}}` (an edge `e` away from the root, `y` a neighbour of
  the root) are one level short, and only those with `e` at depth 2 have an
  obvious partner. This is the deep-edge obstruction of session 10 again.
  It is not needed: the induction of T5 never isolates these terms.
- Ratio dominance along tree shifts, as a route to the upper half: false
  from order 6 at indices `k ≥ ⌊n/2⌋`.
- Recording error: the second checkpoint says "23:02 local, clock reading";
  the clock, read in the same command that appended it, said 22:57. The
  count "216,000" of the first checkpoint is 220,181.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-fable-5-2` (author; experimenter; second reviewer; literature auditor; formalization agent); `claude-opus-5-5` (first reviewer, as reported by it; and the main session after the interruption, closing steps only) |
| Computation wall-clock | stored run of `lower_bound.py`: 53.8 s; scratch runs in total about 5 minutes (the largest: contraction test to order 16, about 105 s; tree shifts to order 15, about 65 s; path maximality to order 17, about 37 s; floating-point LP to order 14, a few minutes in the background); test suites and `verify_lean.py`: see "Outcome" |
| Token usage | main context unavailable; subagents as reported by the environment: experimenter 144,586 tokens, 28 tool uses, 678 s; first reviewer 187,787 tokens, 40 tool uses, 813 s; second reviewer 188,406 tokens, 30 tool uses, 933 s; literature auditor 135,748 tokens, 41 tool uses, 369 s; formalization agent 116,506 tokens, 37 tool uses, 1,424 s |
| Research iterations | 1 focused objective (the two sources), 1 exploration that became a focused objective (the lower half), 2 explorations (upper half; tree shift) |
| Proof attempts | 2 (`E ∈ C_{a+1}` term by term: failed; the induction of T5: complete written proof) |
| Counterexamples found | 0 to the conjecture or to any statement of the note; ratio dominance along shifts refuted (order 6) |
| Formalization attempts | 1 (complete for its scope; one failed build on the way) |
| Successful verifications | two independent AI reviews (no gap found); stored run of `lower_bound.py` (0 failures); the exact checks of Collins's formulas; the commands under "Outcome" |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress, of the first order for this investigation, and all of it
at the level of a **candidate**.

**The lower half of the Collins–Shor conjecture has a candidate proof for
every tree** (Theorem T6(c): `d_{m−1} < d_m`, `m = ⌊n/2⌋`; MD-0019), by a
proof of statement (Γ_c¹) that sessions 9 and 10 had left open. It has two
independent AI reviews of one revision with no gap found, three independent
exact codes agreeing on all trees of order at most 18, and a first literature
search that found no prior statement within a shallow coverage. It has no
human review, its reviewers are models of the author's vendor, the rule S19
it rests on was not re-derived this session, and its originality is not
established. **CJ-0001 keeps the status `active-investigation`**: the upper
half is open and has no mechanism, and nothing is promoted in the session
that produced a claim. By the director's instruction human consultation waits
for a mature manuscript; the next steps of validation are in obligation 11 of
`STATE.md`.

**Reading of Collins.** Done, with its limits recorded. It changes the
description of S23 (the star is Collins 1989, Theorem 1; a leaf formula is
Theorem 4 of the thesis) and of S19(d) (Theorem 7 of the thesis), and it
finds nothing equivalent to the Wiener form, T4, T5, T6 or S36. The operation
of S36 is itself known (Csikvári, Guo, Mohar), as the audit of this session
found.

**An error of handling, corrected.** While `verify_lean.py` was running on
the clean tree `6e6432c`, a dry run of the registry update that was meant
for a scratch worktree wrote `research/discoveries.json` and
`research/catalogue.json` in the repository (a path substitution did not
apply). The two files were restored from Git about a minute later, before
the verifier finished; it reads them only for the list of identifiers,
which the write did not change, and it builds nothing from them. The
receipt records a clean tree, which was true when it was written; this
paragraph is the record that the tree was not clean throughout the run.
The same update was then validated in the scratch worktree and applied.

Verification commands. `uv run python experiments/CJ-0001-collins-shor-peak/lower_bound.py --max-rooted 9 --max-merge 9 --max-pairs 10 --max-contract 16 --out experiments/CJ-0001-collins-shor-peak/results/lower-bound.json`
at `b1359cc`, clean tree: 1,040,693 checks, 0 failures, 53.8 s.
`uv run python scripts/verify_lean.py` at `6e6432c`: VERDICT passed, receipt
`verification/receipts/20261127T022617Z-6e6432c223-passed.json` (see the paragraph above).
`uv run python scripts/catalogue.py validate`: 15 problems, 19 contributions,
0 errors; `render --check`: up to date at the commit that contains this
entry. Test suite (`uv run pytest`): 195 passed in 547.93 s, run by the resuming
model on the tree of the commit that contains this entry plus the edit of
`.claude/skills/research-session/SKILL.md` described below (which
`tests/test_repository.py` reads), and before these two sentences were
filled in.

Budget: the session started at 22:22 local time; `claude-fable-5-2` worked until
about 23:27 (about 65 minutes); after a pause of about 12 minutes
`claude-opus-5-5` did the closing from 23:39 to about 23:52 (clock
readings) — within the ceiling of 120 minutes, reserve included.
Computation: the stored run (53.8 s) and the experimenter's two trial runs
(75.8 s and 60.8 s, as it reported); scratch runs about 5 minutes; in
addition `verify_lean.py` once on the clean tree (about 6 minutes; the
formalizing agent ran it twice more without a receipt, about 8 minutes
each, as it reported) and the full test suite twice (680 s for the harness
commit at the start, 548 s at the end). `STATE.md` has 471 lines, above the aim of
400, after moving the text on Conjecture Γ, the route of sessions 4 to 8,
obligations 1 to 8 and the decisions of sessions 1 to 8 to the notes
(verbatim).

**Interruption and resumption.** At about 23:27 local time the session,
then run by `claude-fable-5-2`, was stopped while it was writing the
closing part of this entry. At that point the registry (MD-0019 added,
MD-0017 and the literature notes of MD-0015, MD-0016, MD-0018 updated), the
catalogue fields on Collins, `STATE.md`, the generated views and the Lean
receipt of `6e6432c` were written but not committed, and two sentences of
this entry (the test suite, the budget) were placeholders. The director
switched the model to `claude-opus-5-5` and asked for the session to be
resumed without restarting it. The resuming model checked the working tree
against the last checkpoint and the closing text (`git status`: exactly
those files; `catalogue.py validate`: 0 errors), filled the two sentences,
recorded this paragraph, ran the verifications below and committed. It did
no mathematics and changed no statement, proof, status or classification
written by the session. In the same pause the director also had a change
made to the skill `research-session` (a model and effort line and a cap on
subagents, for cost); that change is not part of this session's commits.

Next step: `STATE.md`, section "Next step" — obligation 11 (one revision of
`lower-bound.md` and a self-contained manuscript of the lower half), then
objective O12 (the generalized tree shift for every path length, hence path
maximality), then O11 (the upper half).


## Session 12 — 2026-11-26 to 2026-11-27

- **Entry status:** completed; stopped early, with the objective reached
  (it had been stopped at the director's request at about 00:05 on
  2026-11-27 and was resumed at 14:23 the same day).
- **Agent / model:** Claude, model `claude-opus-5-5` (Research Director,
  main session). Principal investigator: `claude-opus-5-5`, by the
  director's decision, while `claude-fable-5-2` is unavailable. Human
  participant: the director (instructions below).
- **Mode:** focused work.
- **Repository revision at start:** `4ca441e` (`research`), the harness
  commit "Cost-efficient model assignment for the research harness"
  (promoted to `main` as `ddc2edf`).
- **Director's instructions:** continue research under the existing harness
  with Opus 5.5 as principal investigator; maximize valid mathematical
  discoveries per available usage budget without sacrificing correctness,
  originality or integrity; MD-0019 keeps its candidate status pending
  further validation and originality assessment; verified research
  contributions may be pushed to `research` only.
- **Objective (exact), O12 of `STATE.md`:** for rooted trees `(A, u)`,
  `(B, v)` with `a, b ≥ 2` and every `k ≥ 1`, prove
  `ℓ_{T_k} − ℓ_{T′_k} ∈ C_{n−1}` for the generalized tree shift (`T_k`: `A`
  and `B` joined by a path of length `k`; `T′_k`: `A` and `B` glued, with a
  pendant path of length `k`), and deduce `ℓ_{P_n} − ℓ_T ∈ C_{n−1}` for every
  tree of order `n`.
- **Approach:** plant is linear and merge bilinear in the state
  `(Ψ, H, G, Ω, E)`, so the difference along a shift has a rational
  generating function in the path length; prove the closed form found in
  session 11 for all `k` by bounding the degree of the numerator, then count
  cone levels with T5 and Lemma K.
- **Falsification test:** the closed form against the generating function
  as rational functions; (GS) and (PX) had already been checked exactly on
  all trees of order up to 13 and 17 (session 11, scratch).
- **Stopping conditions:** done when the note is written, stored with its
  computation, and reviewed; stop if the generating-function identity fails.
- **Budget:** at most 120 minutes; started at 23:57 local on 2026-11-26
  (clock reading). Computation: 30 minutes. Deferred by this choice:
  obligation 11(a) (the revision of `lower-bound.md` for defects of wording)
  — O12 was judged the better use of the budget because session 11 had
  already found its closed form for `k ≤ 12`.

### Checkpoints

- **+8 min (00:05 local, 2026-11-27, clock reading; stopped here at the
  director's request):** *Established, at the level stated.* The closed form
  of Lemma S37 holds as an identity of rational generating functions in the
  path length (exact symbolic computation, sympy 1.14.0, saved as
  `experiments/CJ-0001-collins-shor-peak/tree_shift_symbolic.py`). A written
  proof of Lemma S37 (generating functions; `det(I − tP) = (1 − xt)Q(t)²`;
  numerator of degree at most 5, so `k ≤ 5` suffices), Proposition S38 (cone
  levels), Theorem T7 (every generalized shift lowers `ℓ` in the cone order),
  Lemma S39 (every tree but the path is the result of a shift that removes
  one leaf) and Theorem T8 (path maximality:
  `ℓ_{S_n} ≤ ℓ_T ≤ ℓ_{P_n}` in the cone order, so `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)`)
  is saved as `notes/path-maximality.md` — **a draft, not reread, not
  reviewed, not registered**; it depends on the candidate results of
  `lower-bound.md` (MD-0019) and on S19 (MD-0015). *Unfinished.* (1) Reread
  the draft against `lower-bound.md` (levels, the degree bound in the proof
  of S37, Lemma S39). (2) The stored experiment `tree_shift.py` with a test
  and a README entry (delegate to `computational-experimenter`): the
  factorization of `det(I − tP)`, the closed form for `k ≤ 12`, the lemma on
  actual trees from the distance matrix, (GS) on all shifts and (PX) on all
  trees in ranges that fit the budget; the scratch scripts of sessions 11
  and 12 are in a scratch directory that may not survive, and the code of
  the session-11 symbolic check is in the journal of session 11. (3) One
  independent review (`adversarial-reviewer`, Opus; the author is also
  Opus, so independence is by context only — record it). (4) Register the
  result (one record, type theorem, candidate) after the review; update
  `STATE.md`. *Next action on resuming:* item (1).
- **Resumed at 14:23 local on 2026-11-27 (clock reading), same model
  (`claude-opus-5-5`), on the director's instruction "resume session 12 from
  the existing checkpoint under the current harness; distinguish
  coefficientwise extremality from peak-location extremality".** The tree was
  clean at `00f30ef`, as the checkpoint describes. Remaining budget: 112
  minutes (ceiling about 16:15). Item (1), reread of the draft: two defects
  found by its author. Remark 1 claimed an exact computation (no tree other
  than `P_n` with `ℓ_T = ℓ_{P_n}` for `n ≤ 17`) that had **not** been made —
  the scratch scripts tested membership in the cone only; it is replaced by a
  proof from L2. Notation: the plant matrix was called `P` (as the paths
  `P_n`) and the linear functional `λ` (as `λ_μ`). Item (2) delegated to
  `computational-experimenter` (Sonnet), with a falsification attempt of
  statement (PM) added: (PM) and Lemma S39 would give peak-location
  maximality of the path, hence, with Collins's theorem on the path, the
  upper half.
- **+27 min of work (14:50 local, clock reading):** the review returned no
  gap (report committed at `3c96980`); `tree_shift.py` stored and rerun on a
  clean tree (`3f620e1`); MD-0020 and MD-0021 registered; `STATE.md`
  rewritten. Decision: stop early, see "Outcome".

### What was done

- Reread of the draft by its author (two defects, corrected in the one
  revision before review, `8b03309`: a claimed computation that had not been
  made, now a proof from L2; notation), and a new section separating three
  kinds of extremality, at the director's request.
- `computational-experimenter` (model `claude-sonnet-5-5`, as recorded in its
  transcript) wrote `tree_shift.py`, its test and README entry; the stored
  run was repeated by the main session on a clean tree:
  `uv run --with sympy==1.14.0 python experiments/CJ-0001-collins-shor-peak/tree_shift.py --out experiments/CJ-0001-collins-shor-peak/results/tree-shift.json`
  at `3c96980`, clean tree, 282 s: parts A to F, 0 failures, 0 violations of
  (PM) (counts identical to the agent's own run on a dirty tree).
- `adversarial-reviewer` (model `claude-opus-5-5`, fresh context; the same
  model as the author) reviewed `path-maximality.md` at `8b03309`:
  `reviews/2026-11-27-claude-opus-5-5-T7-T8-path-maximality.md`, no gap found
  within stated scope, defects D1 to D8.
- Scratch, exact, not stored (`pm_brooms.py`, `pm_thin.py`): (PM) on the shift
  from a double broom (stars of `s_1` and `s_2` leaves joined by a path of
  length `L`) to a broom, 458 cases of orders 30 to 120 and a thin-margin scan
  of orders 120 to 300 — no violation; the smallest relative margin at the
  peak of `T` (a ratio of exact integers printed in floating point) was about
  0.0011 to 0.0057, shrinking roughly like `c/n` with `c` between 0.3 and 0.7.
- Registry: MD-0020 (theorem, candidate-proof, ai-reviewed through the review
  of `8b03309`, novelty preliminary-search-completed by the audit of session
  11); MD-0021 (conjecture (PM) with (PX-peak), candidate, not reviewed,
  novelty unknown).

### Findings

1. **Theorem T7 (generalized tree shift) and Theorem T8 (path
   maximality): `ℓ_{S_n} ≤ ℓ_T ≤ ℓ_{P_n}` in the cone order, so
   `d_k(S_n) ≤ d_k(T) ≤ d_k(P_n)` for every `k`, with equality with the path
   only for the path.** Level: candidate proof; one AI review, no gap, by the
   author's model in a fresh context; exact checks by two codes (stored
   experiment; the reviewer's own) on all trees of order ≤ 17 or 18. Depends
   on the candidate results MD-0019 and MD-0015. Originality not
   established; the operation and the Laplacian/adjacency analogues are
   Csikvári's, Mohar's, Zhou–Gutman's.
2. **Coefficientwise versus peak-location extremality.** The star is
   extremal in both senses at the bottom (T6(b), T6(c)); the path is the
   coefficientwise maximum (T8), but whether it is the peak-location maximum
   is open, and coefficientwise domination does not imply it. Recorded as
   (PX-peak), with the route (PM) ⇒ (PX-peak) ⇒ (with the bound on the path's
   peak) the upper half; MD-0021.
3. **The path's peak, exactly, for `n ≤ 2000`:** unique, equal to
   `⌈n − n/√5⌉` for 393 values and `⌊n − n/√5⌋` for 1,605 (part F; the
   informal last step of Collins's Theorem 3 holds in that range).
4. **Negative result, sharpened by the reviewer:** ratio dominance along a
   shift fails even at `j = p_max(T_k)` (2,292 of 95,248 shifts of orders 4 to
   14; smallest `S(2,2) → S_6`). A proof of (PM) cannot be a ratio comparison
   with `T_k`.

### What failed

- The first version of the note asserted a computation (equality only for
  the path, up to order 17) that had not been made. Found by the author's
  reread before review, replaced by a proof; recorded here and in the note.
- No idea for a proof of (PM) was found; none was attempted beyond the
  negative result above.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-opus-5-5` (principal investigator, main session; reviewer); `claude-sonnet-5-5` (computational experimenter) |
| Computation wall-clock | stored run 282 s (clean tree) and 299 s (the agent's run, dirty tree); scratch about 2 minutes; quick tests 74 s; full test suite: see "Outcome" |
| Token usage | main context unavailable; subagents as reported by the environment: experimenter 122,374 tokens, 27 tool uses, 874 s; reviewer 160,340 tokens, 36 tool uses, 969 s |
| Research iterations | 1 focused objective (O12) |
| Proof attempts | 1 (complete written proof of T7, T8; reviewed) |
| Counterexamples found | 0 (to the conjecture, to T7/T8, or to (PM)); ratio dominance at `p_max` refuted (reviewer) |
| Formalization attempts | 0 |
| Successful verifications | one independent AI review (no gap); stored run (0 failures); `catalogue.py validate`; the commands under "Outcome" |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress: a second extremal theorem (candidate, reviewed once), and a
precise, registered reduction of the upper half of the conjecture to a
monotonicity statement (PM) that holds in every case tested, with no proof
mechanism yet. MD-0019 keeps its status, as the director instructed.
CJ-0001 keeps the status `active-investigation`.

The session stopped early with the objective reached: about 35 minutes of
the 120-minute budget used (23:57–00:05 on 2026-11-26/27, then 14:23–about
15:00 on 2026-11-27), two subagents. The rest of the budget was not spent
because no concrete idea for (PM) was available to justify it.

Verification commands, run by the main session on the tree of the commit
that contains this entry (before this sentence was filled in):
`uv run python scripts/catalogue.py validate` (15 problems, 21 contributions,
0 errors); `render --check` (up to date); `uv run pytest` (207 passed in
966.65 s). While it ran, the main session misread its own clock reading as
the end of the run and briefly took the run for interrupted; it was not.

Next step: `STATE.md`, section "Next step" — obligations 11 and 12 (one
revision each of `lower-bound.md` and `path-maximality.md`, with rechecks;
the manuscript of the lower half), then objective O11 through (PM).

## Session 13 — 2026-11-27

- **Entry status:** completed; the objective was reached (15:28 to about 17:00 by the clock, about 92 of the 120 minutes; after the objective the time went to validation: rechecks, revision of the lower half, a manuscript draft, compaction of STATE.md).
- **Agent / model:** Claude, model `claude-opus-5-5` (Research Director and
  principal investigator, main session). Human participant: the director
  (instructions below).
- **Mode:** exploration, switching to focused work if a route appears.
- **Repository revision at start:** `33e277c` (`research`).
- **Director's instructions:** resolve the upper bound of the Collins-Shor
  conjecture, ideally the whole conjecture; full discretion over strategy;
  use the full 120-minute budget productively; verified commits and pushes to
  `research` only.
- **Budget:** at most 120 minutes of agent work, started 15:28 local
  (clock reading); the last 20 minutes for verification and persistence;
  computation 30 minutes of wall-clock in total.
- **What is explored:** a spectral route to the upper half, not tried in
  sessions 1 to 12: write `ℓ_T = 4(α − x)q(x)` with `q` real-rooted
  (the distance eigenvalues of a tree), compare the peak of `d` with the
  mode of `q`, the mode of `q` with its mean (Darroch), and the mean with the
  Laplacian spectrum by interlacing (Graham-Lovász inverse).
- **Deferred:** obligations 11 and 12 (revisions of `lower-bound.md` and
  `path-maximality.md`), because the director set the upper half as the
  objective and they are revisions of wording.

### Checkpoints

- **Checkpoint 1 (15:52 by the clock, 24 minutes).** Found, in exploration, a
  complete candidate argument for the **upper half** for every tree: (1)
  `ℓ_T = 4(α − x)q(x)`, `q = Π(x + β_i)` from the distance spectrum; (2) if
  `q_{k+1} < q_k` then `d` is strictly decreasing from `k` on; (3) Darroch:
  every mode of `q` is within 1 of `μ_q = Σ 1/(1+β_i)`; (4) interlacing
  (Graham-Lovász inverse; Merris 1990): `μ_q ≤ n − tr(I+L)^{-1}`; (5) the
  path minimizes `tr(I+L)^{-1}` (own proof by merging two pendant paths, the
  key step being convexity of `x/(φ^{2x}+1)` on `[3, ∞)`; the literature
  auditor found that it also follows from Andriantiana-Misanantenaina-Wagner,
  Graphs Combin. 36 (2020), Theorem 4.4, via the subdivision); (6)
  `tr(I+L_{P_n})^{-1} = n/√5 + 2/5 + (2n/√5) r^{2n}/(1 − r^{2n})`,
  `r = φ^{−2}`. Level: written in scratch only, checked in floating point on
  all trees of order ≤ 17 (exploratory). Switching to focused work: write
  the note, a stored exact check, two independent reviews. Subagents so
  far: one literature auditor.
- **Checkpoint 2 (16:00 by the clock, 32 minutes).** `notes/upper-bound.md`
  committed at `53421a6`. Registered MD-0022 (T9, the upper half) and
  MD-0023 (T10, the path minimizes the trace), both `candidate-proof`,
  `not-reviewed`; STATE.md and the dossier updated; catalogue valid, views
  rendered. Running in the background: two independent reviews of
  `53421a6` (`claude-opus-5-5` fresh context; `claude-sonnet-5-5`, a model
  other than the author's, after `claude-fable-5-2` was refused by a spend
  limit before doing any work), the stored computation `upper_bound.py`
  (computational experimenter), and a Lean formalization of Lemma S41
  (formalization agent). Subagent count: six launched (one failed at once);
  justified by the significance of the claim (two reviews are required for
  a result that settles half of a catalogued problem).
- **Objective (exact), switched to focused work at 15:52:** prove that for
  every tree `T` of order `n ≥ 3` every maximizing index of
  `d_0, …, d_{n−2}` is at most `⌈n − n/√5⌉` (the upper half of
  Conjecture 1.2 of arXiv:1507.02341, strong reading of ties).
- **Approach:** the spectral route described above; it was not among the
  approaches of sessions 1 to 12 (the dead end "Darroch's theorem" of
  session 7 concerned `r_A` at the lower central index, a different
  polynomial and index).
- **Falsification test:** each lemma and the theorem exactly on all trees of
  small order and on paths to large order (stored experiment), and by two
  reviewers' own code.
- **Stopping condition:** the note written, reviewed twice, stored with its
  computation; or a step found false.

### What was run

- Exploratory floating-point scratch (scratchpad, not stored): the chain
  peak(`d`) ≤ mode(`q`), `μ_q ≤ n − tr(I+L)^{−1}`, `tr(T) ≥ tr(P_n)` on all
  trees of order 4 to 16; the rooted recursion for the trace; the envelope of
  rooted invariants (abandoned: irregular); the merging inequality on all
  rooted trees of order 2 to 11 with `p, q ≤ 8` and on synthetic states
  (it fails for `κ` up to `1 + ε`, holds for `κ ≤ 1 + ε/2`, which is the
  true bound, S43′); the closed forms of S44 against matrix inverses.
- Literature audit (`literature-auditor`, `claude-opus-5-5`, about 6.5
  minutes, 108,814 tokens, 39 tool uses). Queries: (1) trees minimal
  Kirchhoff index fan graph join K_1 tree extremal; (2) Kirchhoff index join
  K_1 tree cone fan minimal among trees Laplacian eigenvalues 1/(1+mu)
  (extended); (3) trace of (I+L)^{-1} trees path minimizes spanning rooted
  forests expected number of roots tree extremal (extended); (4) Laplacian
  resolvent energy trees path star extremal; (5) resistance distance or
  Kirchhoff index fan graph join of a vertex and a tree extremal trees
  minimum; (6) average size of matchings trees path extremal Andriantiana
  Wagner; (7) random rooted spanning forest number of roots expectation sum
  q/(q+lambda) trees extremal path star; (8) subdivision average size of
  matchings Laplacian eigenvalues tree rooted spanning forests; (9) Collins
  Shor conjecture peak normalized coefficients distance characteristic
  polynomial tree sqrt 5 proof (extended); (10) distance characteristic
  polynomial tree coefficients peak location 2025 or 2026 arXiv (extended);
  (11) Darroch theorem mode real-rooted polynomial distance matrix tree
  coefficients peak eigenvalues; (12) Darroch 1964 "On the distribution of
  the number of successes in independent trials" mode mean; (13) Pitman
  "Probabilistic bounds on the coefficients of polynomials with only real
  zeros" Darroch mode; (14) tree Laplacian eigenvalues 1/(1+μ_i) path
  minimum; (15) Kirchhoff index of graphs with a dominating vertex trees
  K_1 ∨ T minimum fan. Findings: dossier, section "Audit for session 13".
- Reviews of `notes/upper-bound.md` at `53421a6`: `claude-opus-5-5`
  (fresh context; 107,954 tokens, 34 tool uses, 742 s) and
  `claude-sonnet-5-5` (114,491 tokens, 28 tool uses, 530 s), both "no gap
  found within stated scope", with 4 and 6 defects of provenance, wording,
  notation and citation. A third reviewer on `claude-fable-5-2` was refused
  at once by a spend limit and did no work. The Sonnet report gives
  `tanh(3 log φ) ≈ 0.9128`; the value is `0.8944` (the note's bound
  `> 0.894` is right; the slip does not affect its verdict).
- Stored computation `upper_bound.py` (computational experimenter,
  `claude-sonnet-5-5`; 110,369 tokens, 25 tool uses, 634 s): parts V, A to F,
  M; stored run at `917d657` in a clean temporary worktree (the main tree
  held another agent's uncommitted Lean files), 298.7 s, 0 failures in every
  part (A: all 1,346,023 trees of order 2 to 20).
- Revision 1 of the note (`2037b18`) for the reviewers' defects; new note
  `path-peak.md` (S47, S48), its criterion checked exactly against the peak
  of the path for `n ≤ 2000` (scratch `pp2.py`, 193 s; a first, slower
  scratch run to `n = 3000` was stopped unfinished and is not counted).
- Exploratory dead end (floating point): the polynomial `Σ_{k≤n−2} d_k x^k`
  is **not** real-rooted in general (5,416 of 5,444 trees of order 4 to 14
  fail, the first at order 5), so Darroch's rule cannot be applied to `d`
  itself to sharpen T9 towards (PX-peak).
- Exploratory (floating point): for the path the interlacing step loses
  little (`n − tr − μ_q ≈ 0.9/n`), so the gap between T9's bound
  `⌈x − 2/5⌉` and the path's peak comes from the step from `q` to `d`
  (S41) and from Darroch's rule, not from S42.
- **Checkpoint 3 (16:16 by the clock, 48 minutes).** Established at the
  level of candidate proofs with two independent AI reviews (no gap): T9 (the
  upper half) and T10. Not yet reviewed: revision 1 (recheck running) and
  `path-peak.md` (review running, same reviewer). Lean formalization of S41
  running. Next: collect those results, run the test suite, finish the
  entry, commit and push.
- Lean (formalization agent, `claude-opus-5-5`; 69,970 tokens, 25 tool
  uses, 1,111 s): `UpperBoundPeak.lean`, Lemma S41 as a statement about real
  sequences (`upperD_succ_lt`, `upperD_maxIndex_le`), registered for CJ-0001;
  `verify_lean.py` passed on a dirty tree at `45fc871` (receipt
  `20261127T191722Z-45fc87136c-dirty-passed.json`). A first receipt
  (`20261127T190943Z-917d657c9f-dirty-passed.json`), written by mistake before
  the theorems were registered, was untracked and was deleted. The principal
  investigator compared the Lean statement with S41 (hypotheses and
  conclusion match; the factor 4 and `N = n − 1` are encodings); not an
  independent comparison.
- Revision 1 of `notes/lower-bound.md` (obligation 11(a)) for the defects of
  the two reviews of `74d65b0`: Lemma S32 written out, L1 at `n = 2`
  justified, Remark 1 after S36 marked as checked but unproved, the exact
  checks cited at the stored run with its counts (1,064 pairs, of which 486
  degenerate for S36), the notational clashes listed. No statement or step
  changed.
- Exploratory (floating point): combining T9's proof with T6(c), every tree
  with `tr(I + L)^{−1} ≥ ⌈n/2⌉` has its peak exactly at `⌊n/2⌋` (if
  `⌊n/2⌋ ≤ n − 3`: every mode of `q` is `< n + 1 − tr ≤ ⌊n/2⌋ + 1`). For odd
  `n ≤ 15` no tree satisfies the hypothesis; for even `n` from 6 to 16 the
  trees that do are 6, 21, 39, 42, 45, 43 in number, of diameter at most 6,
  including the balanced double stars `S(a, a)` checked (`a = 5, 10, 20,
  50`; `S(30, 3)` fails the hypothesis). Not
  registered; an observation.
- Exploratory (floating point, paths of order 19 to 79): the peak of `d`
  equals the mode of `q` in every case, and the mode of `q` is `⌈μ_q⌉`
  only when the fractional part of `μ_q` is at least about `0.41`. So for
  the path the slack of T9 is in Darroch's step (`m_q < μ_q + 1` is loose by
  about `0.4`), not in S41 or S42. A sharper mode-mean inequality for these
  `q` (uniform over trees) is what a proof of (PX-peak) along this route
  would need.
- Scratch (exact rationals; `avm.py` in the session scratchpad, not
  stored): `avm(S(T)) = n − tr(I + L_T)^{−1}` for all 986 trees of order 2
  to 12 — the identity on which the literature route to T10
  (Andriantiana–Misanantenaina–Wagner) rests. A finite check, not a proof.

### Findings

1. **Theorem T9 (MD-0022): the upper half of the Collins–Shor conjecture
   for every tree** — every maximizing index `p` of `d_0, …, d_{n−2}`
   satisfies `p < n − n/√5 + 3/5`, so `p ≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉`.
   Level: candidate proof (`notes/upper-bound.md`); two independent AI
   reviews of `53421a6`, no gap (`claude-opus-5-5` by context;
   `claude-sonnet-5-5`, a different model of the same vendor); revision 1 at
   `2037b18`, rechecked by `claude-sonnet-5-5`, no gap; exact checks by three
   codes (stored experiment; two reviewers). Lean: Lemma S41 only. The proof
   uses only classical results (Graham–Lovász, Weyl, Newton, Darroch, the
   path spectrum) and none of the candidate results MD-0015 to MD-0021.
2. **Theorem T10 (MD-0023): the path minimizes `tr(I + L)^{−1}` among
   trees**, with a self-contained proof by merging pendant paths. Very
   probably a known consequence of Andriantiana–Misanantenaina–Wagner (2020),
   Theorem 4.4 (the auditor's derivation, unreviewed).
3. **Lemma S47, Corollary S48 (MD-0024): the exact peak of the path**, and the
   upper bound `⌈n − n/√5⌉` of the conjecture is attained for infinitely many
   `n` (when the fractional part of `n/√5` is below `1/10`, `n ≥ 30`). One AI
   review (`claude-sonnet-5-5`), no gap.
4. With T6(c) of session 11 (the lower half, candidate proof, MD-0019),
   **both halves of the conjecture now have candidate proofs**; none is
   established. With S48: for every `n`, `max_T p_max(T)` is `⌊n − n/√5⌋` or
   `⌈n − n/√5⌉`, and the conjectured upper bound is best possible for
   infinitely many `n`.
5. Validation of the lower half advanced: revision 1 of `lower-bound.md`
   (obligation 11(a)).

### What failed

- A rooted invariant `t − n/√5 ≥ Γ(ε, κ)` for an induction over plant and
  merge was explored and abandoned: the lower envelope found in the data is
  irregular. The pendant-path merging (S45) replaced it.
- A synthetic test of the merging inequality with the crude bound
  `κ ≤ 1 + ε` failed (at `ε = 1.8`); the true bound `κ ≤ 1 + ε/2` (S43′)
  is what makes it hold.
- `Σ_{k≤n−2} d_k x^k` is not real-rooted, so Darroch's rule cannot be applied
  to `d` directly; the gap between T9's bound and the path's peak, which is
  what (PX-peak) needs, remains for the `n` with fractional part of
  `n − n/√5` above `2/5`.
- The reviewer on `claude-fable-5-2` was refused by a spend limit.
- A slow scratch run (Fractions, `n ≤ 3000`) was stopped unfinished and is
  not counted; a fast exact version covered `n ≤ 2000`.
- Rechecks (`claude-sonnet-5-5`, one context for three tasks; 132,518
  tokens, 33 tool uses, 756 s in all): revision 1 of `upper-bound.md` at
  `2037b18`, no gap (four defects of bookkeeping); first review of
  `path-peak.md` at `2037b18`, no gap (four defects of wording); revision 1
  of `lower-bound.md` at `e16cb62`, no gap (five defects of bookkeeping).
  The stale README passages on the provenance of `upper_bound.py` and
  `lower_bound.py` that two of them found were corrected in this session.

### Telemetry

| Item | Value |
| --- | --- |
| Model | `claude-opus-5-5` (principal investigator, main session; literature auditor; reviewer by context; formalization agent); `claude-sonnet-5-5` (computational experimenter; reviewer of another model; rechecks); `claude-fable-5-2` requested once, refused by a spend limit before any work |
| Subagents | 7 launched (literature auditor; experimenter; two reviewers, plus one refused at once; formalization agent; one reviewer for the three rechecks). More than the default three, because the claim settles one half of a catalogued problem: `AGENTS.md` and the session skill require two independent reviews for it |
| Computation wall-clock (main session) | stored run 298.7 s (clean worktree); scratch: about 6 minutes of a slow run stopped unfinished, 196 s for the path criterion, about 3 minutes of floating-point exploration; verification: `verify_lean.py` about 7 minutes, `pytest` 552 s |
| Token usage | main context unavailable; subagents as reported by the environment: auditor 108,814; experimenter 110,369; reviewer (Opus) 107,954; reviewer (Sonnet) 114,491; formalization 69,970; rechecks 132,518 |
| Research iterations | 1 objective (the upper half), reached; 2 side results (S47, S48; revision of the lower half) |
| Proof attempts | 1 complete (T9 with T10), reviewed twice; 1 abandoned (rooted invariant) |
| Counterexamples found | 0 (to the conjecture, to any lemma); one refuted idea (real-rootedness of `Σ d_k x^k`) |
| Formalization attempts | 1, complete: Lemma S41 (two registered theorems) |
| Successful verifications | two reviews and three rechecks, no gap; stored run, 0 failures; `verify_lean.py` passed; `pytest` 217 passed; `catalogue.py validate` 0 errors; `render --check` |
| Cost estimate and assumptions | unavailable |

### Outcome and next step

Durable progress: **a candidate proof of the upper half of the Collins–Shor
conjecture for every tree** (T9, MD-0022), short and independent of the
machinery of sessions 4 to 12, reviewed twice with no gap; with the lower
half of session 11, both halves of the conjecture have candidate proofs. The
extremal step (T10, MD-0023) is very probably a known consequence of a
published theorem; the peak of the path is now located exactly (MD-0024).
Nothing is promoted: `proved` needs a result package, a documented novelty
search of the final statement and, by the decisions of sessions 10 and 11, a
consolidated manuscript and its audit. CJ-0001 keeps the status
`active-investigation` (director's decision of session 10); the principal
investigator recommends `candidate-proof`.

Verification commands run by the main session: `uv run python
scripts/verify_lean.py` (passed at `e16cb62` on a tree whose only changes
were a README edit and untracked review reports; receipt
`20261127T192616Z-e16cb626ca-dirty-passed.json`; a clean rerun after the
closing commit is recorded below if it was made); `uv run pytest` (217 passed
in 552.35 s, same tree); `uv run python scripts/catalogue.py validate` (15
problems, 24 contributions, 0 errors) and `render`, after the last registry
change.

Next step: `STATE.md`, section "Next step" — the consolidated manuscript of
the whole conjecture and its audit; `STATE.md` is 551 lines and should be
compacted (aim under 400) at the start of the next session.

Addendum (16:40 to 17:00 by the clock). `STATE.md` compacted from 551 to
about 460 lines (moved text verbatim in `notes/obligations.md`, section
"Text moved from `STATE.md` in session 13"). A publication-agent subagent
(`claude-opus-5-5`) wrote an unreviewed draft manuscript of the upper half,
`manuscripts/CJ-0001-upper-bound/main.tex` (pdfLaTeX, MiKTeX 25.12, two
runs, exit 0, 18 pages; the PDF only in the session scratchpad). It found
three small steps missing from `upper-bound.md` (a proof of Corollary 3;
`K ≥ 2` in T9; the case `Y = {v}` of S43; all immediate, supplied in the
draft) and supplied some citation details from memory, to be checked
(`STATE.md`, obligation 13). Subagents in all: 8 launched (one refused at
once). The final clean `verify_lean.py` run and the push are recorded in the
commit that follows this entry.

Final verification (16:57 by the clock): `uv run python scripts/verify_lean.py`
on a clean tree at `319c099` — toolchain, build, sources, axioms, registry,
replay passed; receipt `verification/receipts/20261127T195730Z-319c099c1c-passed.json`.
CI of the push at `b088f0a` failed in `tests/test_repository.py::test_relative_markdown_links_resolve`:
the text moved from `STATE.md` into `notes/obligations.md` kept one link
target relative to the investigation directory (`notes/obligations.md`). The
local full test run (217 passed) had been made before the compaction, so it
did not cover that change. Fixed (the target is now `obligations.md`, and the
heading says "verbatim except for the targets of relative links", as in
session 11); `uv run pytest -m "not lean"` passed locally (206 passed, 11
deselected), then pushed again.

## Session 14 — 2026-11-27

- **Entry status:** in progress.
- **Agent / model:** Claude, model `claude-opus-5-5` (Research Director and
  principal investigator, main session). Human participant: the director
  (instructions below).
- **Mode:** focused work (consolidation and validation).
- **Role(s):** research director, mathematical author of the manuscript.
- **Repository revision at start:** `1de859c` (`research`, clean tree).
- **Director's instructions (2026-11-27):** CJ-0001 may be moved from
  `active-investigation` to `candidate-proof` (this does not authorize
  `proved` or any resolved status); the primary objective is one rigorous,
  self-contained manuscript of the complete candidate proof of the
  Collins-Shor conjecture, readable without the repository's history;
  audit dependencies, hypotheses, boundary cases, citations, novelty claims
  and open obligations; distinguish original contributions, known results,
  rediscoveries and open auxiliary conjectures; prepare it for review by
  models of other vendors; human consultation deferred; no promotion on the
  strength of AI reviews; verified commits and pushes to `research` only.
- **Objective (exact):** a manuscript `manuscripts/CJ-0001-collins-shor/`
  containing complete proofs that for every tree `T` of order `n ≥ 3`,
  every maximizing index of `d_0, …, d_{n−2}` lies in
  `[⌊n/2⌋, ⌈n − n/√5⌉]` (Conjecture 1.2 of arXiv:1507.02341, strong
  reading of ties), using only cited classical results; plus an audit of
  every dependency it uses.
- **Approach:** lower half from the Graham-Lovász formula through the Wiener
  identity S24 and the rooted induction T5, T6 (`notes/lower-bound.md`,
  revision 1); upper half from the spectral route T9, T10
  (`notes/upper-bound.md`, revision 1, and the unreviewed draft
  `manuscripts/CJ-0001-upper-bound/main.tex`); simplify where possible.
- **Falsification test:** every identity and inequality in the manuscript
  re-checked exactly on small trees by a script independent of the notes'
  code before the manuscript is called complete.
- **Stopping conditions:** the manuscript written, compiled and checked; or a
  gap found that the session cannot close (then recorded as such).
- **Budget:** at most 120 minutes of agent work, started 17:13 local (clock
  reading); the last 20 minutes for verification and persistence;
  computation 30 minutes of wall-clock in total.

### Checkpoints

- **Checkpoint 1 (17:33 by the clock, 20 minutes).** CJ-0001 set to
  `candidate-proof` in `research/catalogue.json` (director's approval of
  2026-11-27; validate: 0 errors). Manuscript
  `manuscripts/CJ-0001-collins-shor/main.tex` written (30 pages, pdfLaTeX,
  no undefined reference): both halves with complete proofs. The lower half
  is restated in a shorter form: only root weights, the rules for raising
  the root weight and planting derived from the identity (★) instead of the
  recurrences S15, S16 for weighted trees; the leaf recursion S23(b) derived
  from the plant rule; the cones `C_d` dropped (only `K_d` is needed). Level:
  written; the new derivations checked by the author and by a new
  independent exact script `manuscript_check.py` (rooted trees of order ≤ 8,
  merges of order ≤ 8, trees of order ≤ 12; 11,379 checks, 0 failures, scratch
  run before storing). Unfinished: the stored run on a clean tree; an
  independent review of the whole document; STATE.md. Next: commit, stored
  run, reviews.

- **Checkpoint 2 (17:54 by the clock, 41 minutes; checkpoint 1 was at 17:32,
  not 17:33 as written).** Stored run of `manuscript_check.py` in a clean
  worktree at `8df6bea`: 11,379 exact checks, 0 failures, 258.5 s (committed
  `2047ebb`, pushed; CI started by the push). Two independent AI reviews of
  the whole manuscript at `8df6bea`: `claude-opus-5-5` (fresh context) and
  `claude-sonnet-5-5` (a model other than the author's, after
  `claude-fable-5-2` was refused at once by its monthly spend limit); both
  **no gap found within stated scope** (committed `31f6386`). Defects
  reported: the reversed last inequality of the Merris chain in a remark;
  the wording of the "only if" direction of Lemma R1 (both reviewers); the
  attainment of the lower bound resting on Collins's Theorem 1 (both); the
  count 1,346,023 for orders 3 to 20 (should be 1,346,022; the slip is in
  `leaf-telescoping.md` too); the domain `n ≥ 3`; the description of the
  Graham-Lovász conjecture; the direction of the S(9,9) ratio statement; the
  unnamed citing papers. Revision 2 of the manuscript made: all of these
  corrected; new Lemma 7.5 (the star's sequence increases strictly up to
  `⌊n/2⌋` and decreases strictly after it, by a binomial estimate), which
  makes the bounds independent of the log-concavity theorem of
  arXiv:1507.02341 and of Collins's Theorem 1; Lemma R1 removed (no longer
  used). Lemma 7.5 checked exactly for `3 ≤ n < 800` (scratch). Next: commit,
  recheck of revision 2 by a fresh context.
