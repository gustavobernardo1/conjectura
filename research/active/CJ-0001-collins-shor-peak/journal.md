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
  started at 20:36 UTC, each in its own context: `literature-auditor`
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

