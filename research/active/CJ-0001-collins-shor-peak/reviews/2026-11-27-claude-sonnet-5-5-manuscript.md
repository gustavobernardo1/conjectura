# Independent review — CJ-0001 — whole manuscript, both halves of the Collins–Shor conjecture

- **Reviewer:** claude-sonnet-5-5 (Claude Code subagent `adversarial-reviewer`).
- **Date:** 2026-11-27.
- **Independence:** fresh context; the task message gave only the primary source
  (Conjecture 1.2 of arXiv:1507.02341), the file under review and the review
  instructions. I wrote the statement down from the primary source (read in the
  arXiv PDF, v3) before reading the proofs, and did not read `research/active/`
  notes or earlier review reports before finishing my own assessment. All
  verification code was written by me from the manuscript's definitions
  (scratchpad `lib.py`, `t1.py` to `t8.py`); I did not open the author's
  scripts. **Limits of independence:** (i) same vendor as the author, and the
  same model identifier as several earlier reviewers named in Section 16 of the
  manuscript (this is not a different-model review); (ii) the session scratchpad
  directory already contained files from other contexts (`ms_check.py`,
  `extract.py`, `edit3.py`, `dk.py`, `tex/`, `pdf/`, `wt14/` ...); I did not
  open or run any of them; (iii) I did not verify the review history that
  Section 16 reports.
- **Revision reviewed:** Git revision `8df6bea` (`8df6beac16b54e218d66ec3470a3f49a91546b17`).
  `git diff 8df6bea -- manuscripts/CJ-0001-collins-shor/main.tex` is empty, and
  the working-tree file is identical to that revision. (At the time of writing
  `HEAD` had moved to `2047ebb`; the file is unchanged.)
  File: `manuscripts/CJ-0001-collins-shor/main.tex`, 1855 lines,
  SHA-256 `0bf1928f33c215e046d49fd3e0a4b0db0cff80b3f8dd7d6819580da327e711c8`.
  It compiles with `pdflatex` (two passes, 30 pages, no undefined references
  or citations).
- **Material given to the reviewer:** the task message and the file above. The
  untracked files `manuscripts/CJ-0001-collins-shor/README.md` and
  `REVIEW-PROMPT.md` were not read.

> **Numbering.** Lemma, theorem and section numbers below are those of the compiled document (labels `lem:ident` = 2.1, `lem:R1` = 2.2, `lem:L1` = 2.3, `lem:A` = 3.2, `lem:K` = 4.2, `lem:path` = 4.3, `cor:phi1` = 4.4, `lem:star` = 5.1, `prop:rules` = 5.2, `cor:leaf` = 5.3, `prop:S33/S34/S35` = 6.1/6.2/6.3, `thm:T5` = 7.1, `thm:lower` = 7.3, `lem:starvalue` = 7.4, `lem:S40/S41/S42` = 8.1/8.2/8.3, `lem:S43/S43p/S44/S45` = 9.1/9.2/9.3/9.4, `thm:T10` = 9.5, `lem:S46` = 9.7, `thm:upper` = 10.1, `cor:sharper` = 10.2, `lem:S47` = 11.1, `cor:pathceil` = 11.2; sections 12 open problems, 13 computational evidence, 14 formal verification, 15 literature, 16 status). The local names (R1, S33, T5, ...) are the manuscript's own labels.

## Statement as read from the primary source

AAB (arXiv:1507.02341v3), Conjecture 1.2 (Collins–Shor): "The [normalized]
coefficients of the distance characteristic polynomial for any tree T with n
vertices are unimodal with peak between ⌊n/2⌋ and ⌈n − n/√5⌉." Here
d_k(T) = 2^{k−(n−2)} |δ_k(T)|, 0 ≤ k ≤ n−2, n ≥ 3 (AAB, Section 1, Fact 1.1,
Observation 3.1). AAB Theorem 2.1 gives positivity, log-concavity and
unimodality; Theorem 3.3 gives peak ≤ ⌈2n/3⌉. The unimodality is already
known, so the content is: for every tree of order n ≥ 3 the peak lies in
[⌊n/2⌋, ⌈n − n/√5⌉]. The task asks for the strong reading of ties: every
index p with d_p = max_k d_k must lie in that interval. Neither source defines
the tie reading.

What the manuscript claims (Main Theorem): for every tree with n ≥ 3 and every
maximizing index p, ⌊n/2⌋ ≤ p ≤ ⌈n − n/√5 − 2/5⌉ ≤ ⌈n − n/√5⌉, with both outer
bounds attained (star for every n ≥ 3, path for infinitely many n). This is a
statement about that exact conjecture, in the strong reading. The 2/5 is a
strengthening of the upper bound, not a change of the statement.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | Checked: n ≥ 3 throughout the Main Theorem; n ≥ 2 for Lemma 2.1 (ident), Lemma 2.3 (L1), Theorem 7.3(b); n ≥ 1 where used for rooted trees; |X| ≥ 2 where Lemmas 9.2, 9.4 need it. The hypotheses of Lemma 5.1 (any w ≥ 0, any rooted tree, a = 1 treated separately), of Lemma 4.2 (ν ≠ 0, with the leaf choice making ν' ≠ 0) and of Prop. 6.3 are satisfied at every use. The strong tie reading is covered on both sides: Lemma 2.2 (R1) plus (LC) for the lower bound, Lemma 8.2 (S41) for the upper bound. The only hypothesis I could not trace to the source is (LC) as "positive and log-concave on d_0..d_{n−2}": AAB Thm 2.1(iii) says exactly this, so it is fine. |
| Quantifiers | "Every maximizing index" is proved, not "some". Lemma 2.2: statement quantifies correctly (see defect 1 for the proof sentence). Theorem 7.3(c): "every maximizing index ≥ ⌊n/2⌋" follows from d_m > d_{m−1} plus log-concavity. Theorem 10.1: m_q is any maximizing index of q (Darroch applies to each), then the contradiction argument ("q_{K+1} < q_K") correctly handles q_K = q_{K+1} ties. "For infinitely many n" for the path rests on Kronecker density (infinitely many n, since the sequence {nξ} has no repeats): correct. |
| Mathematical definitions | Checked against my own code: ℓ_T, Φ, M(K,ν), Ψ, Ω, H, G, E, R_w, π_w, state, plant, merge, the cones K_d (including K_d = K_0 for d ≤ 0), a_v, J, W, Q^1. All agree with the text. Sign/normalization of ℓ_T: [x^k]ℓ_T = d_k for k ≤ n−2 (and −4 at x^n, 0 at x^{n−1}) confirmed on all trees n ≤ 15 against the distance matrix. |
| Boundary cases | n = 3 (P_3 = S_3, ℓ_T − ℓ_S = 0, p = 1 = ⌊3/2⌋ and ≤ ⌈1.258⌉ = 2); n = 4 (⌊4/2⌋ = 2 = ⌈4 − 1.789 − 0.4⌉, both trees peak at 2 — tested); n = 5; a = 1 (state (1,0,0,0,−(1+2x)²), E = 0, planted single vertex Ê = 0 — checked symbolically and in code); a single branch (q = 1 in Prop. 6.2(d): E = Ê_1, no X terms); empty sums (H = G = 0, Ω = 0 when a = 1; empty product Ψ = 1); d ≤ 0 in cones; d = 0 in Lemma 4.3 (path); Q = ∅ in Lemma 4.3 and Cor. 4.4 (b = 2: minor = 1, x·1 ∈ K_2); merge with a one-vertex tree (R_0 unchanged; checked). m ≤ n−2 for n ≥ 3 (n = 3: m = 1 ≤ 1). K ≥ 2 and the case K ≥ n−2 in Theorem 10.1. For the path: n = 3, 4, 5 handled directly in Lemma 11.1, and I recomputed h_3(2) = 20, h_4(2) = 6, h_5(2) = −12, h_5(3) = 64. No boundary failure found. |
| Intermediate lemmas | See the per-lemma list below. All reconstructed by hand; none failed. One proof sentence is false as written (defect 1); the lemma itself is true. |
| Logical implications | Main Theorem ⇐ Thm 7.3(c) + Thm 10.1 + Lemma 2.2 + (LC): correct. Thm 7.3(b) ⇐ Cor. 5.3(c) + Thm 7.3(a): telescoping identity re-derived. Thm 7.3(a) ⇐ Cor. 4.4 + Thm 7.1(i): correct (product expansion over non-empty subsets lands in K_{n−1}). Thm 7.1 ⇐ Prop. 6.1 (S33), 6.2 (S34), 6.3 (S35), Lemma 4.2: the induction is well founded (branches have smaller order; (i)–(iii) are used for branches only), and the cone arithmetic (K_{a_i+2}·K_{Σ a_t} etc.) was recomputed term by term. Thm 10.1 ⇐ Lemma 8.1, 8.2, 8.3, Thm 9.5, Lemma 9.4, Darroch: correct (details below). Attainment clauses: see defect 3. |
| Dependency assumptions | Cited without proof: (GL), (GP), (LC), (W), (N), (D), (M), (PS), (C), (Kr). I re-checked what can be checked: (GL)+(GP) indirectly (Cor. 5.3(a) was tested against ℓ_T computed from the actual distance matrix for every rooted tree of order ≤ 8, 0 failures); (LC) is AAB Thm 2.1 (read); (W), (N): standard, statements correct; (D): Darroch's mode rule — the manuscript's use needs only m_q < μ + 1 for every mode; I tested this exactly with Fractions on 8,000 random Poisson-binomial distributions (including near-0/near-1 probabilities and ties), 0 violations (largest |k − μ| = 0.768); (C): checked against the distance matrix for 3 ≤ n ≤ 30 (and ≤ 40 in an earlier run of my script; see Reproduction). Not read by me: Darroch 1964, Collins 1989, Graham–Lovász 1978, Graham–Pollak 1971. |
| Counterexample attempts | (1) Exhaustive: every tree of order 3..15 (13,186 trees), exact integer d_k from the characteristic polynomial of D, every maximizing index in [⌊n/2⌋, ⌈n−n/√5−0.4⌉]: 0 violations, one tie (n = 13). (2) Theorem 7.3(b): ℓ_T − ℓ_{S_n} ∈ K_{n−1} via my own exact-rational simplex for every tree of order 3..11 (434 trees in total): all pass; checker sanity-tested on known non-members (1 ∉ K_1, x ∉ K_3, 1+x+x² ∉ K_2) and members. (3) Rooted calculus: Lemma 5.1 (w = 0,1,2), Prop. 5.2(b),(c), Cor. 5.3(a), Prop. 6.1(a)–(e), 6.2(a),(b), Lemma 4.3, Cor. 4.4, Lemma 4.2 membership, T5(i)–(iii) on every rooted tree of order ≤ 8 (13,171 checks, 0 failures); merge rules 5.2(d), 6.2(c) and Prop. 6.3 (including the sum-of-squares identity and its cone membership) on all pairs of rooted trees of order ≤ 4 (196 pairs each, 0 failures). (4) Upper half: Lemma 9.1 and Lemma 9.2 on all pairs of rooted trees of order ≤ 5 (exact); Lemma 9.3 (S44) on paths N = 2..30 for every r (exact); Thm 9.5 (T10) on every tree of order ≤ 14 (exact), equality only for paths; Lemma 9.7 formula for n < 40 (1e-9); path peak criterion (Lemma 11.1) against exact d_k for n ≤ 30 and against the criterion alone for n ≤ 20,000 (p ≤ ⌈ξ − 0.4⌉ always; p = ⌈ξ⌉ for 593 values of n ≤ 20,000 in my 20,000 run: consistent with the manuscript). (5) Star: formula of Cor. 5.3(d) vs exact d_k for n ≤ 59; unique maximum at ⌊n/2⌋ for 3 ≤ n ≤ 700 (not 3000: that run was cut); the closed forms of Lemma 7.4 for n ≤ 700. No counterexample to anything. |
| Formalization scope | Manuscript Section 14 says only auxiliary statements are formalized (Lemma 2.2 general form, cones and Lemma 3.2 (A), the sequence part of Lemma 8.2). I did not re-run `scripts/verify_lean.py` (not requested; out of the manuscript-reading scope). The manuscript does not claim formal verification of the main results. Its description of the Lean scope is not overstated on its face. |
| Novelty coverage | The manuscript claims no originality and states the search coverage. My own check (two web searches plus fetches of three arXiv abstracts, standard mode only, so limited): no prior resolution found. Papers found that Section 15 does not name: Abiad, Brimkov, Hayat, Khramova, Koolen, arXiv:2206.07561 (block graphs, not trees); Jana, Mahato, Sivasubramanian, arXiv:2407.03309 (Min-4PC and 2-Steiner matrices of trees). Neither resolves the Collins–Shor conjecture for trees (from abstracts only). They may be among the "five citing papers" the manuscript says it examined; I cannot tell. AMW (arXiv:1903.09825): I only confirmed that it characterizes extremal trees for the average matching size; I did not check the claimed Lemma 5.1 / Theorem 4.4 / avm identities, and the manuscript flags this as unreviewed. The hedges ("very probably known", "not evidence of originality") are adequate. The claim "no prior statement of coefficientwise minimality of the star" is a search-coverage statement and is hedged. I make no novelty claim either. |
| Unresolved gaps | None in the proofs of the two inequalities. Open items are the defects below (attainment clauses, unread classical sources, wording). |

### Per-lemma list (each reconstructed independently)

- Lemma 2.1 (ident), Lemma 2.3 (L1): re-derived (matrix determinant lemma, adj(−M) = (−1)^{n−1} adj M, (GP)). OK. n = 2 check OK.
- Lemma 2.2 (R1): OK as a lemma; one proof sentence false (defect 1).
- (K1),(K2), Lemma 3.2 (A): OK; case analysis a ≤ 0 / a ≥ 1 and i ≥ 2a−1 ≥ a verified.
- Lemma 4.1 (blocks): OK (tree ⇒ exactly one edge from each component of K[Q] to P).
- Lemma 4.2 (K): identity (K3) re-derived; induction and the choice of a leaf with ν' ≠ 0 OK; second term is a product of Φ(K',ν|+e_a) with non-zero weights; cone count j−2 then +2. Tested.
- Lemma 4.3 (path): Schur complement argument OK (the off-diagonal entries of M[V(P),Q]M[Q]^{-1}M[Q,V(P)] vanish because each component of K[Q] has exactly one vertex adjacent to P and that vertex has exactly one neighbour on P); the lower-triangular minor and sign OK; cone claim OK. Tested for all vertex pairs of all rooted trees ≤ 8.
- Cor. 4.4 (phi1): OK, by (K3) with ν = e_c and a leaf ≠ c; tested.
- Lemma 5.1 (star): re-derived from the Schur complement; the identification of the restriction of p^{(w)} to A_i with p^{(1)} of the branch OK. Tested w = 0,1,2.
- Prop. 5.2 (a)–(d): (b) and (c) re-derived by hand including the Ψ-coefficient cancellation (coefficient of Ψ in (b) is (1+2x)^2; in (c) the cancellation to 0); (d) R_0 merge formula re-derived by the divisibility argument. Tested on all rooted trees ≤ 8 and all merges of small trees.
- Cor. 5.3 (a)–(d): re-derived. (b) uses plant rule only.
- Prop. 6.1 (S33): (a) through (e) re-derived, including Lδ = τ − 2e_u, p^{(1)} = M^1(1+δ) − δ, and the symmetrisation giving R_1 = Q^1 + x²W. Cone memberships a_v ∈ K_{a+δ_v−3} etc. recomputed. Tested.
- Prop. 6.2 (S34): (a)–(d) re-derived (the H-coefficient 3x²+2x³ recomputed). Tested.
- Prop. 6.3 (S35): the sum-of-squares identity re-derived; membership count (three terms) recomputed. Tested for all pairs of rooted trees of order ≤ 4 (exact identity and cone membership).
- Thm 7.1 (T5): induction closes; (iii) ⇐ (i),(ii). OK.
- Thm 7.3, Lemma 7.4: OK; closed forms for the star verified for 3 ≤ n ≤ 700.
- Lemma 8.1 (S40): inertia argument (rank-one update, determinant sign) OK; α = Σβ_i OK.
- Lemma 8.2 (S41): re-derived, including j = 0 and the two sub-cases; the strict decrease of ratios uses Newton with real zeros: OK.
- Lemma 8.3 (S42): OK.
- Lemma 9.1 (S43), 9.2 (S43p): re-derived (Schur complement, Sherman–Morrison); tested; the extremal-entry argument G_{wv} ≤ G_vv/2 OK.
- Lemma 9.3 (S44): hyperbolic closed form, formulas (G_rr) and (c_r) re-derived; ψ'' computation and the numerical bound z tanh z > 1.29 OK; δ_0 = δ_1 identity OK; equality case N = 2, r = 1 only. Tested exactly for N ≤ 30.
- Lemma 9.4 (S45): the algebra for 𝒩 re-derived; the chain 1−κ ≥ −(a−1)/2, c' ≥ c, c > 3/5 gives 𝒩 > 0. OK.
- Thm 9.5 (T10): induction on the number of leaves OK (choice of v at maximum distance from a leaf ρ; the two branches are pendant paths; |X| ≥ 2).
- Lemma 9.7 (S46): Poisson kernel evaluation OK; formula verified numerically.
- Thm 10.1, Cor. 10.2: OK (integer m_q < ξ + 3/5 with ξ irrational gives m_q ≤ ⌈ξ − 2/5⌉; the contradiction argument for q_{K+1} < q_K).
- Lemma 11.1 (S47), Cor. 11.2: ratio formula and h_n re-derived; k_0 ≤ n−1; location for n ≥ 6 and n = 3,4,5; corollary (a),(b),(c) re-derived. Exact check against the distance matrix for n ≤ 30 and the criterion for n ≤ 20,000.

## Defects

1. **error (minor; lemma remains true).** Lemma 2.2 (R1), proof, second sentence: "the sequence is non-increasing from j−1 on and j−1 is a maximizing index" is false as written. Example: a = (4, 2, 1), j = 2: a_1 = 2 ≥ a_2 = 1 but index 1 is not maximizing (the maximum is at index 0). What is true and what the lemma needs: if a maximizing index p ≥ j existed, then a_{j−1} ≥ a_p, so j−1 is also maximizing, hence "every maximizing index ≥ j" fails. The (⇒) direction of the lemma is not used in the Main Theorem (only "a_{j−1} < a_j ⇒ every maximizing index ≥ j"), so no consequence for the proof.
2. **wording / numerical statement (evidence section, not part of a proof).** Section 13 (computational evidence), item 2: "star minimality ... for all 1,346,023 trees of order 3 to 20". The number of trees of order 3..20 is 1,346,022 (tree counts A000055 typed from memory, cross-checked: they reproduce my own enumeration through order 15 and the manuscript's total 23,942,357 for orders 3..23); 1,346,023 is the count for orders 2..20, and Theorem 7.3(b) is stated for n ≥ 2. Either "order 2 to 20" or the count should be corrected. The count 23,942,357 for orders 3..23 is correct (I recomputed it); I did not re-run the exhaustive search above order 15.
3. **gap (confined to the attainment clauses of the Main Theorem, not to the conjecture).** "The lower one [is attained] by the star S_n for every n ≥ 3" is justified by citing [Col89, Thm 1] and by "an elementary computation ... not reproduced here" plus an exact check for 3 ≤ n < 400. The manuscript itself says (Remarks 7.5 and 7.6) that the proof for all n is not written out. I reproduced the unique peak at ⌊n/2⌋ for n ≤ 700 only. The same holds for "the upper bound is attained by the path for infinitely many n": it needs (C) for all n, which is a citation of [Col89, Thm 3] (checked here for n ≤ 30). The attainment clauses are therefore as strong as the citation to Collins, and the Main Theorem's "attained" sentence should be marked as resting on [Col89] plus finite checks. The proof that every tree's peak lies in the interval does not depend on this.
4. **citation (acknowledged by the manuscript).** Darroch's paper, Collins's paper, Graham–Lovász and Graham–Pollak were not read by the author; I did not read them either. The manuscript quotes Collins's Conjecture 9 verbatim ("CPD(T)", "n(1−1/√5)") — I could not verify the quotation, only AAB's description of it ("stated without the floor or ceiling"). For (D) I rederived from memory the consequence needed (every mode within distance < 1 of the mean) and tested it exactly; this is a test, not a proof of the cited statement.
5. **wording.** Main Theorem: "Both outer bounds are attained ... the upper one by the path for infinitely many n". The displayed upper bound is ⌈n − n/√5 − 2/5⌉; what Cor. 11.2(c) proves is p(P_n) = ⌈n − n/√5⌉ for infinitely many n. These coincide at such n because {ξ} > 4/5 forces ⌈ξ − 2/5⌉ = ⌈ξ⌉ (this is said later, in the "Consistency with Theorem 10.1" paragraph, but not in the proof of the Main Theorem).
6. **wording.** Section 12 ("Further remarks and open problems"), item 2: "The analogous comparison with the star at k = ⌊n/2⌋−1 is false (the double star S(9,9), order 20)" does not say which direction of the inequality is meant. I checked: for S(9,9), d_{10}/d_9 = 10791/10255 ≈ 1.05227 < 99/94 ≈ 1.05319 for the star, so the comparison "≥ star's ratio" fails and "≤ star's ratio" holds there; the sentence is correct only for the former. The claim d_1 = 2n² − 6 − Σk_v² is correct (checked n ≤ 11); the ratio comparison with the path holds on all trees of order 4..12 in my run (the manuscript claims 4..20).
7. **citation / literature.** Section 15 does not mention arXiv:2206.07561 and arXiv:2407.03309 (related distance-matrix peak questions for block graphs and for other matrices of trees; neither resolves the conjecture on the evidence of their abstracts). If the "five citing papers" include them, no change is needed; otherwise they should be listed. The manuscript's search coverage statement is otherwise honest.
8. **wording.** Section 16 (status) states that earlier AI reviewers "reported no gap". This review does not check or endorse that history. The present review is by the same model identifier as three of those earlier reviewers; independence is limited as stated above.

I found no gap, error or counterexample in Sections 4–7 (lower bound) or in Sections 8–12 (upper bound and path).

## Reproduction

All commands run from `d:\conjectura` with `uv run python <script>`; scripts are in the session scratchpad (`.../scratchpad/lib.py`, `t1.py` ... `t8.py`, `refs.py`; not committed). Library: `python-flint` (exact integer polynomials and matrices), `networkx` 3.7 (tree enumeration), `fractions.Fraction`.

- `git rev-parse HEAD`, `git diff 8df6bea -- manuscripts/CJ-0001-collins-shor/main.tex` (empty), `sha256sum` of the file: values above.
- `t1.py 8`: 13,171 single-rooted-tree checks (orders 1..8, every root) + 196 merges + 196 planted pairs, 0 failures (identities of Lemma 5.1, Prop. 5.2, Cor. 5.3(a), Prop. 6.1, 6.2, 6.3, Lemma 4.3, cone memberships of Lemma 4.2, Cor. 4.4, Thm 7.1(i)–(iii) via an exact Bland-rule simplex written for this review). Cone checker sanity-tested in `t8.py`.
- `t7.py 11`: ℓ_T − ℓ_{S_n} ∈ K_{n−1} for all trees of order 3..11 (434 trees in total), 0 failures.
- `t2.py 15`: exhaustive strong-tie check of the Main Theorem, orders 3..15, integers from the characteristic polynomial; 13,186 trees, 0 violations of [⌊n/2⌋, ⌈n−n/√5−0.4⌉], one tie (n = 13).
- `t3.py`: Lemma 9.1 (S43) and 9.2 (S43p) on all pairs of rooted trees of order ≤ 5 (exact, Fractions via fmpq); Lemma 9.3 on paths N ≤ 30; Thm 9.5 on all trees ≤ 14; Lemma 9.7 formula n < 40 (floating, 1e-9; exploratory for that last item).
- `t4b.py` (a shortened copy of `t4.py`; ranges: star n ≤ 700, path criterion n ≤ 3000, Collins formula n ≤ 30, 8,000 Darroch trials), `t6.py` (path criterion with 60-digit decimals, n ≤ 20,000: p ≤ ⌈ξ−0.4⌉ always), `t5.py` (tree counts, S(9,9), d_1 formula, path ratio comparison n ≤ 12). The longer `t4.py` run (star to 3000, Darroch 30,000) was started in the background and not awaited; none of its results are used here.
- Primary source: arXiv:1507.02341v3 PDF read (statement of Conj. 1.2, Fact 1.1, Thm 2.1, Obs. 3.1, Thm 3.3).
- Compilation: `pdflatex main.tex` twice in a scratch copy: 30 pages, no undefined reference or citation (labels and bibliography are consistent).
- Not run: `scripts/verify_lean.py`, `uv run pytest`; the exhaustive computation to order 23 and the stored results the manuscript cites.

## Verdict

`no gap found within stated scope`

Scope: this verdict applies only to `manuscripts/CJ-0001-collins-shor/main.tex`
at revision `8df6bea` (SHA-256 above). I found no gap in the two proofs (lower
bound d_m(T) − d_{m−1}(T) > 0 hence every maximizing index ≥ ⌊n/2⌋, via the
cone argument; upper bound every maximizing index ≤ ⌈n − n/√5 − 2/5⌉ via the
spectral route) under the strong tie reading, conditional on the cited classical
results ((GL), (GP), (LC), Weyl, Newton, Darroch's rule, the Laplacian spectrum
of the path, Kronecker), which I did not re-prove, and on the checks listed.
It does not cover: the attainment clauses beyond the cited Collins results
(defect 3); the correctness of the cited statements at their original sources;
the unreviewed Remark about AMW; novelty (unknown; my coverage was two web
searches and three arXiv abstracts); formal verification; or any revision other
than the one named. It is an AI review by the same model identifier as earlier
reviewers of parts of this text; it is not peer review and not human review.

Classification of defects: gap 1 (3, attainment only), error 1 (1, minor),
wording 4 (2, 5, 6, 8), citation 2 (4, 7).
