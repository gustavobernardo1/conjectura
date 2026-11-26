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
