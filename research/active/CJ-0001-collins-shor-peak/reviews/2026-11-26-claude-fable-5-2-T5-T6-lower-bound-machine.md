# Independent review — CJ-0001 — Lemma S32, Propositions S33 to S36, Theorems T5 and T6 (`notes/lower-bound.md`): machine re-derivation

- **Reviewer:** AI model `claude-fable-5-2` (Claude Code subagent in the role
  "adversarial reviewer"). No human took part.
- **Date:** 2026-11-26.
- **Independence:** a fresh context that received the task statement, the
  primary source and the file under review, and not the author's reasoning
  trail (the journal was not read; of `STATE.md` only the sections "Exact
  statement" and "Definitions and conventions" were read). **Limited:** the
  reviewer is the same model as the author of the note (`claude-fable-5-2`
  according to the note's header), so this is independence of context, not of
  model. No report named `*T5-T6-lower-bound*` by another reviewer was read.
  All decisive computations were made with code written for this review from
  the definitions in the notes; nothing was imported from `experiments/`. Two
  contacts with the author's computational material, both without effect on
  the checks: the first 40 lines (docstring) of the then-untracked
  `experiments/CJ-0001-collins-shor-peak/lower_bound.py` were displayed, and
  the then-untracked `results/lower-bound.json` was searched for its counts
  (used only for defect D2/D3 below).
- **Revision reviewed:** Git commit `74d65b0`. File
  `research/active/CJ-0001-collins-shor-peak/notes/lower-bound.md`, SHA-256
  `d149fd5b6d3ac510f07f4aacca7f419dfbdc9d4dfb5d4bdf38719ac2b07c614d`
  (checked at the start, in the middle and at the end of the review).
  Dependencies as committed at `74d65b0` (SHA-256, first 16 hex digits;
  working-tree copies identical): `wiener-form.md` `f8d0d773da704d1d`,
  `rooted-calculus.md` `5080ea4888af2498`, `gamma-components.md`
  `f2057b1fb60f65be`, `leaf-telescoping.md` `66c64a0f250f2dd0`, `lemmas.md`
  `a225898814df1ae5`, `gamma-reduction.md` `49f33f738105a773`.
  During the review the branch advanced to `f2a46c8` (two commits by another
  process: dossier, `STATE.md`, journal, `lower_bound.py`, its test and README
  entry). The file under review is byte-identical at `f2a46c8`; nothing else
  of `f2a46c8` was reviewed. The reviewer modified nothing in the repository
  except this report.
- **Material given to the reviewer:** the task (claim, dependencies, emphasis:
  an independent machine re-derivation and a hunt for a counterexample);
  `AGENTS.md`; `research/templates/review.md`; the notes listed above.
  The primary source arXiv:1507.02341v3 was fetched and pages 1 to 9 were
  read as a PDF by the reviewer.

## Statement as read from the primary source

Written before reading the proofs. Source: Aalipour, Abiad, Berikkyzy,
Hogben, Kenter, Lin, Tait, arXiv:1507.02341v3 (20 Apr 2017), pages 2 to 5.

- `D(G)` is the distance matrix of a connected graph `G` of order `n`;
  `δ_k(G)` is the coefficient of `x^k` in `det(D(G) − xI)`. The order is
  assumed to be at least three. For `0 ≤ k ≤ n − 2`,
  `d_k(G) = 2^k |δ_k(G)| / 2^{n−2}` (the normalized coefficients).
- Fact 1.1 (Graham–Lovász): for a tree, `(−1)^{n−1} δ_k(T) > 0` for
  `0 ≤ k ≤ n − 2`. Theorem 2.1(iii): `d_0(T), …, d_{n−2}(T)` is log-concave
  and unimodal. Observation 3.1: `ℓ_T(x) = −2^{−(n−2)} det(2xI − D(T))` is
  real-rooted with coefficients `−4` at `x^n`, `0` at `x^{n−1}`, `d_k(T) > 0`
  at `x^k`, `0 ≤ k ≤ n − 2`.
- Conjecture 1.2 (Collins–Shor): for every tree `T` with `n` vertices the
  normalized coefficients are unimodal with peak between `⌊n/2⌋` and
  `⌈n − n/√5⌉`. The source does not say how a tie at the maximum is read.
- What the source itself proves about the peak: at most `⌈2n/3⌉`
  (Theorem 3.3) and at least `⌊(n−2)/(1+d)⌋`, `d` the diameter (Theorem 3.6);
  it reports a computer confirmation of the conjecture for order at most 20.

The claim under review (Theorem T6(c)): for **every** tree `T` of order
`n ≥ 3`, with `m = ⌊n/2⌋`, `d_m(T) − d_{m−1}(T) ≥ d_m(S_n) − d_{m−1}(S_n) > 0`,
hence every maximizing index of `d_0, …, d_{n−2}` is at least `⌊n/2⌋`. This
is the lower half of Conjecture 1.2 in the strong reading of ties, for the
same objects (`δ_k`, `d_k`, `n ≥ 3`) and the same quantifier (every tree).
It is not the conjecture: the upper bound `⌈n − n/√5⌉` is not addressed, and
the note does not claim it.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | No hypothesis is added or dropped. T6(c) is for every tree of order `n ≥ 3`, as in the source. T5 is for every rooted tree of order `a ≥ 1`, weight zero; T6(a) for `n ≥ 1`; T6(b) for `n ≥ 2`; S36 for a non-pendant edge (`a, b ≥ 2`). Lemma K and Lemma S32 need integer weights `ν ≥ 0` (Lemma K: `ν ≠ 0`); every use supplies a non-zero weight (the unit added at the vertex next to the removed path). |
| Quantifiers | "For every tree" and "for every vertex `u`" are kept throughout. The induction of T5 is on the order `a`, for all rooted trees of that order simultaneously; (i) and (ii) at order `a` use (i), (ii), (iii) only at orders `a_i ≤ a − 1`, and (iii) at an order follows from (i), (ii) at the same order. Well-founded. The strict inequality in T6(c) comes only from the star (S23(d)); for a general tree the proof gives `≥` against the star, which is what is stated. |
| Mathematical definitions | `ℓ_T`, `d_k` agree with the source (Observation 3.1). `K_d`: non-negative combinations of `x^e(1+x)^i`, `2e + i ≥ d`, any integer `d` (for `d ≤ 0` it is the set of polynomials with non-negative coefficients; the rules (K2) hold for negative indices too, which is needed for `H ∈ K_{a−2}` at `a = 1`). `C_d` as in `gamma-reduction.md`. The state `(Ψ, H, G, Ω, R)`, `E`, `a_v`, `Q¹` were implemented from their definitions and every identity that relates them was tested (see Reproduction). The definition of `r_u(T)` in `lower-bound.md` agrees with `leaf-telescoping.md`. |
| Boundary cases | `a = 1`: `Ψ = 1`, `H = G = Ω = 0`, `R = −(1+2x)²`, `E = 0`, `R(A, e_u) = 0`: checked by hand and by machine. `a = 2`: `E = 0`, `R(A, e_u) = x(1+x) ∈ K_3`: by hand. Child subtrees that are single vertices (`a_i = 1`): the planted tree is one edge, with `Ψ^_i = 1 + x`, `H^_i = 1`, `G^_i = 0`, `Ω^_i = 0`, `E^_i = 0`; the proof of S35 covers it (empty sums) and the machine check includes all 7,813 pairs with a single-vertex tree. `q = 1`: S34(d) is `E = E^_1`, empty products equal to 1. `n = 2` in T6(b): the difference is `0`. `n = 3, 4` in T6(c): `m = 1`, `1 ≤ m ≤ n − 2` holds; checked from the distance matrix. S36 with `a = 1` (outside its hypothesis): both sides vanish. Nothing found. |
| Lemma S32 | The proof is by reference to the proof of Lemma S24. Reconstructed: that proof uses positive definiteness for `x > 0`, the block structure of `M[Q]` over the components of `K − V(P)`, the fact that each component touches the path at one vertex with one neighbour on the path, and the tridiagonal Schur complement; none of these uses the diagonal entries, so the argument holds with weights. The cone statement follows from Lemma K because each block has the extra unit weight at `a_{K′}`. Machine: all ordered pairs `(v, v′)` of 1,458 weighted rooted trees of order 1 to 9 — no failure. **No gap.** (Defect D5.) |
| (K2), (K4) | Verified by hand from the definition. (K4) is correct: generators have non-negative coefficients, so no generator of a positive combination exceeds the degree of the sum. |
| Lemma K and (K3) (dependency) | Proof read and reconstructed by hand, including the choice of the leaf (`ν′ ≠ 0`) and `j = 2`. Machine: (K3) at every leaf (6,270 instances), `Φ(K, ν) ∈ K_j` (965 weighted trees) — no failure. |
| Proposition S33 | (a) level count `(a − δ_v − 1) + 2(δ_v − 1) = a + δ_v − 3`: correct. (b), (c), (e): re-derived by hand line by line (`Lδ = τ − 2e_u`; `p = M¹(1+δ) − δ`; `(1+δ)ᵀM¹(1+δ) = Σ(1+δ_v)² + xa`; the symmetrization giving `Q¹`); (d) is S32 with `d = 0`. Level of `Q¹`: `x^d K_{a−d−1} ⊆ K_{a+d−1} ⊆ K_a` for `d ≥ 1`: correct. Machine: identities and all memberships on 7,813 rooted trees of order 1 to 12 (80,851 pairs `(u, v)`), 400 random rooted trees of order 13 to 40 and 46 rooted trees of order 40 to 51 — no failure. **No gap.** |
| Proposition S34 | (a), (b), (c) re-derived by hand (the coefficient `x(1+2x)² − x(1+x) − 2x³ = 3x² + 2x³` is right); the induction of (d) checked by hand. Machine: (a), (b) with the planted tree's state computed from its definition on the same rooted trees; (c) on 18,048 pairs; (d) on 310 tuples with `q = 3, 4, 5` — no failure. **No gap.** |
| Proposition S35 | Identity re-derived by hand (`G^_i = x²J_i`, `R¹_i = Q¹_i + x²W_i`, `H_1W_2 + H_2W_1 − 2J_1J_2 = Σ a_v a_{v′}(δ_v − δ_{v′})²`). Levels: `2 + (a_1 − 1) + (a_2 + 1)`, `4 + (a_1 − 2) + a_2`, `8 + (a_1 − 2) + (a_2 − 2)`: the first two are exactly `a_1 + a_2 + 2`, the third is larger. Machine: identity, membership of the left side and of each of the three groups in `K_{a_1+a_2+2}`, on 18,048 pairs (`a_1 + a_2 ≤ 13`) and 200 random pairs of orders 13 to 40 — no failure. **No gap.** |
| Theorem T5 | Level counting checked term by term: `Ω`: `(a_i + 1) + Σ_{l≠i} a_l = a`; `E^_i ∈ K_{a_i+2}` (tight terms `xΩ_i` and `3x²H_i`); `E^_iP_i`: `a_i + 2 + (a − 1 − a_i) = a + 1`; `X_{il}P_{il}`: `a + 1`; (iii): `x(1+x)H ∈ K_{(a−2)+3}`. `Σ a_i = a − 1` is right. The degree bound `a + 1` for `R(A, e_u)` and (K4) give `C_{a+1}`. Machine: (i), (ii), (iii), the `C` statement, `E^ ∈ K_{a+2}`, and the decomposition `E = Σ E^_iP_i + Σ X_{il}P_{il}` with every term in `K_{a+1}` (485 rooted trees of order 2 to 9) — no failure. **No gap.** |
| Theorem T6 | (a) the claim `Φ(B, e_c) − (1+x)^j ∈ K_j` and the product expansion: correct; `(1+4x) = (1+x) + 3x`. (b) telescoping minus the star: correct; degree at most `n − 2`. (c) `2m − 1 ≤ n − 1`, Lemma A(a), `1 ≤ m ≤ n − 2`: correct; R1 applies with `j = m`, `r = n − 2`. Machine, from the distance matrix only: (b) and (c) for every tree of order 2 to 18 (205,003 trees) and 129 trees of order up to 260 — no failure; equality in (c) for exactly one tree of each order 3 to 18. **No gap.** |
| Proposition S23(a), (b), (c) (dependency, not reviewed before) | (a) and (b) re-derived by hand from L1, S15 and the leaf expansion of `Φ`; (c) is the iteration of (b) from `ℓ = −4x`; the case `n = 1` is consistent. Machine, with `ℓ_T` from the distance matrix and not from L1: (a) and (b) on 7,813 + 400 rooted trees, (c) on 120 random trees of order 2 to 14 with a random build order — no failure. (d): the algebra of both parities re-derived; positivity checked for `3 ≤ n ≤ 1200`, the closed form for even `n` (Remark 3) also; `ℓ_{S_n}` against the distance matrix for `n ≤ 60`. **No gap found in (a) to (d).** |
| Proposition S19(b), (c), (d), S15, S16 (dependencies) | Proofs read; not re-derived line by line in this review. Machine, from the definitions, with random integer weights and roots: raise, plant and merge (including the terms with the root weights) on 2,729 instances each — no failure. S15 and S16 enter only through S19(b), (c) and S23(b), which were tested directly. |
| Proposition S36 | The cone part checked by hand (`(a−2) + (b+1)`, `3 + (a−2) + (b−2)`, `2 + (a−1) + (b−1)`). The polynomial identity was **not** expanded by hand; it was verified by machine with `ℓ_T`, `ℓ_{T′}` from the distance matrices on 10,235 pairs with `a, b ≥ 2`, `a + b ≤ 13` (and 7,813 degenerate pairs with a single vertex, `0 = 0`), and on 200 random pairs with `n` between 26 and 80. Each term in `K_{n−1}`, the difference in `C_{n−1}`, Remark 1 (`[x] = 2k_A(u)k_B(v)`, `x² | E`) — no failure. No error found; the algebraic derivation in the text is confirmed only by these instances. |
| Logical implications | S32 ⇒ S33(a), (d), (e); S33 + S19 ⇒ S34, S35; S33, S34, S35, Lemma K ⇒ T5 (induction); T5(i), Lemma S32, (K3) ⇒ T6(a); T6(a), S23(c), (d) ⇒ T6(b); T6(b), Lemma A(a), S23(d), R1 ⇒ T6(c). Each arrow was followed; the lemmas cover all trees (every rooted tree of order `a ≥ 2` is the merge of `q ≥ 1` planted trees; every tree is built by adding pendant vertices). No missing case found. |
| Dependency assumptions | External, not re-proved here: Graham–Pollak (`det D`), used in L1; Theorem 2.1 of the source (log-concavity), used in R1 for the last sentence of T6(c); Fact 1.1 (sign). The Graham–Lovász formula for `D^{−1}` was reconstructed from `LD = τ1ᵀ − 2I` and `τᵀD = (n−1)1ᵀ`. Fact 1.1 held on every tree computed (0 failures) and L1 is confirmed on the computed range through S23(a). Lemma A(a) and R1 are said to be formalized in Lean; that was not re-run here. Remark 2 and the last clause of Remark 3 after T6 use Proposition S30 of `even-order.md`, which the note itself marks as not reviewed: **not assessed**. |
| Counterexample attempts | Directed at T6(b), (c) and at every intermediate membership. All trees of order 2 to 18; paths (to order 260), brooms, double stars (including `S(1, 198)`, `S(100, 100)`), spiders with 50 to 120 legs of length 2 (orders 101 to 241) and variants, spiders with legs of length 3 and 25, balanced caterpillars with spine 2 to 15 at orders 100 to 240, 40 random trees of order 60 to 140; T5 and S33 on rooted versions of these families at order 40 to 51 and on 400 random rooted trees of order 13 to 40. The final statement read directly (every maximizing index `≥ ⌊n/2⌋`) for all 32,506 trees of order 3 to 16 and 12 large trees. **No counterexample found.** This is finite evidence within that coverage only. |
| Formalization scope | No Lean formalization of S32 to S36, T5 or T6 is claimed in the reviewed revision; formal status of these statements: not started. `scripts/verify_lean.py` was not run (it writes a receipt, and the reviewer may write only this report). |
| Novelty coverage | **Not assessed.** One web search (query: distance characteristic polynomial, tree, normalized coefficients, peak, `n/2`, Collins, Shor, proof, lower bound) returned no source that proves the bound `⌊n/2⌋`; the source itself (read) proves `⌊(n−2)/(1+d)⌋`. arXiv:2206.07561, arXiv:2407.03309, the journal version and Collins's papers were not read. This establishes nothing about originality. |
| Unresolved gaps | None found in the mathematics within the scope below. Defects (not gaps) are listed next. |

### Defects (do not affect the validity of the argument)

- **D1 (reproducibility at the reviewed revision).** The section "Exact
  checks" refers to `experiments/CJ-0001-collins-shor-peak/lower_bound.py`,
  to "its entry in the experiments README" and to a result file. None of the
  three exists in the tree of `74d65b0` (`git ls-tree -r 74d65b0` lists only
  the note; the README of that revision has no such entry). The documented
  computation therefore could not be re-run from the reviewed revision. (The
  script and README entry appear in the later commit `f2a46c8`, which was not
  reviewed and whose script was not run; the result file was still untracked.)
- **D2 (a count that does not match its description).** "Every pair of rooted
  trees whose merge has order at most 9 (778 pairs)": by the reviewer's own
  enumeration that set has 1,021 unordered pairs (1,064 if pairs of equal
  order are counted as ordered). 778 is the number obtained when only rooted
  trees of order at most 8 are used (the 286 pairs "single vertex with a tree
  of order 9" are missing). Either the description or the count is wrong.
- **D3 (degenerate cases counted).** "S36: the formula on 1,064 pairs":
  486 of these have a single-vertex tree, for which the edge is pendant
  (outside the hypothesis of S36) and the identity is `0 = 0`; 578 pairs are
  within the hypothesis.
- **D4 (notation).** `a_v` (a polynomial), `a_i`, `a_1`, `a_2` (orders),
  `a_{K′}` (a vertex) and `a` (an order) coexist, in S35 within one
  statement; `X` is both the placeholder for `H, G, Ω` and the polynomial
  `X_{il}`; `Q` is a vertex set in S32 and `Q¹` a polynomial; `M` is the
  matrix here and the upper bound `⌈n − n/√5⌉` in `STATE.md`.
- **D5 (proof by reference).** The proof of Lemma S32 says that "the proof of
  Lemma S24 uses of the matrix only that …" instead of giving the argument.
  The reviewer could reconstruct it, so it is not a gap, but a result package
  should carry the weighted argument in full. The same holds for the reliance
  of the headline on S23(a) to (c), which had no review before this one.

## Reproduction

Environment: `uv run python` at the repository root (Python 3.12.4,
python-flint 0.9.0, networkx 3.7; sympy not installed). Exact integer
arithmetic only (`fmpz`, `fmpz_poly`, `fmpz_mat`); no floating point.
Scratch code, outside the repository:
`rev.py` (SHA-256 `982cd3e5…7b31a`) and `rev2.py` (SHA-256 `678ae985…70286`)
in the session scratch directory; they are not stored in the repository, so
the runs below are reported, not reproducible from the repository.

How things were computed (all from the definitions in the notes):

- `Φ(T, ν) = det(I + x(L + diag ν))` and `adj(M)` by Faddeev–LeVerrier with
  the final check `M · adj(M) = Φ · I`; `Φ` compared with the characteristic
  polynomial computed by FLINT; `adj(M)` compared with the cofactor matrix at
  `a + 1` integer points for order at most 6 (111 weighted trees). Minors
  `det M[Q]` independently, from the characteristic polynomial of the
  principal submatrix.
- `p`, `R(T, ν)`, and the state `(Ψ, H, G, Ω, R)` literally from the
  definitions of `gamma-components.md` and `rooted-calculus.md` (`Ω` from the
  components of `T − u` with the raised weights; `Ψ = adj(M)_{uu}` also
  compared with the product over the components). Planted and merged trees
  were built as graphs and their states computed from the definition.
- `ℓ_T = Σ_{k ≤ n−2} d_k x^k − 4x^n` with `d_k = 2^{k−(n−2)}|δ_k|` from the
  characteristic polynomial of the distance matrix (never from L1).
- **Membership in `K_d`.** Since
  `x^e(1+x)^i = x^e(1+x)^{i−1} + x^{e+1}(1+x)^{i−1}` and both pieces remain
  generators when `2e + i > d` and `i ≥ 1`, the cone `K_d` (`d ≥ 1`) is
  generated by `x^e(1+x)^{d−2e}` (`2e < d`) and the monomials `x^e`
  (`2e ≥ d`). These are linearly independent (triangular in the lowest
  term), so membership is the non-negativity of unique coordinates, for a
  polynomial of **any** degree; for `d ≤ 0` it is the non-negativity of the
  coefficients. For degree at most `d` this is the half-gamma test of `C_d`.
  Membership in `C_d` was decided as "degree at most `d` and in `K_d`". The
  test was sanity-checked on 2,000 random combinations of generators and on
  three known non-members.

Commands (from the repository root) and results; every line below ended with
"ANY FAILURE: False":

| Command | Coverage | Result |
| --- | --- | --- |
| `uv run python rev.py core 12 13` | all 7,813 rooted trees of order 1 to 12 (counts per order 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842, 4766): S24, S33(a)–(e) with all memberships (including `adj(M¹)_{vv′} ∈ K_{a+d−1}` for all pairs), S34(a), (b), S19(b), (c), T5(i)–(iii) and `C_{a+1}`, `E^ ∈ K_{a+2}`, T6(a) and its claim, S23(a), (b); 18,048 unordered pairs with `a_1 + a_2 ≤ 13` (10,235 with both orders ≥ 2): S19(d), S34(c), S35 identity and cone, S36 formula, terms and cone; S34(d) on 310 tuples; the decomposition of the proof of T5(ii) on 485 rooted trees | no failure |
| `uv run python rev.py weights 9` | 1,458 weighted rooted trees of order 1 to 9: Lemma S32 for all pairs, Lemma K (965), (K3) (6,270), S19(b), (c), (d) with weights (2,729 each) | no failure |
| `uv run python rev.py random 400 13 40` | 400 random rooted trees of order 13 to 40 (random recursive, preferential, paths, caterpillars, spiders, brooms, binary): the per-tree checks above (the membership of every `adj(M¹)_{vv′}` only for order at most 24); 200 pairs: S35, S36 | no failure |
| `uv run python rev.py t6 18` | every tree of order 2 to 18 (205,003; networkx enumeration): T6(b) in `K_{n−1}` and `C_{n−1}`, `d_k(T) ≥ d_k(S_n)`, T6(c) | no failure; equality in (c) for one tree per order |
| `uv run python rev.py fam` | 129 trees of order up to 260 (families listed above): T6(b), (c); S23(d); T5/S33 on 46 rooted trees of order 40 to 51; S23(c) on 120 trees; Lemma A(a) on 8,960 generators | no failure |
| `uv run python rev2.py 16` | every tree of order 3 to 16 (32,506): positivity, log-concavity, every maximizing index `≥ ⌊n/2⌋`; pair counts for D2, D3 | no violation; one tree has a tie at the maximum (its indices are `≥ ⌊n/2⌋`) |

Fact 1.1 (sign of `δ_k`) held on every tree for which `ℓ_T` was computed.

Not run: `experiments/CJ-0001-collins-shor-peak/lower_bound.py` (absent from
the reviewed revision, see D1); `scripts/verify_lean.py`; `uv run pytest`.

## Verdict

`no gap found within stated scope`

Scope. Revision `74d65b0` of `notes/lower-bound.md` (SHA-256 above): Lemma
S32, Propositions S33, S34, S35, Theorem T5, Theorem T6(a), (b), (c), and
Proposition S23(a) to (d) of `leaf-telescoping.md` as used there. For these
the reviewer reconstructed every step of the written proofs by hand (with the
exception stated next) and found no failure in the exact computations listed.
Proposition S36: the cone argument was reconstructed; its polynomial identity
was verified by machine on the stated instances and not expanded by hand.
Propositions S19(b), (c), (d), S15, S16 were read and machine-checked from the
definitions (with weights), not re-derived line by line. The verdict assumes
the cited external theorems (Graham–Pollak; Fact 1.1 and Theorem 2.1 of
arXiv:1507.02341).

Not covered: novelty (unassessed); any Lean formalization (none claimed);
the upper bound of the conjecture; Remark 2 and the reference to S30(d) in
Remark 3 after T6; the stored experiment script and its result file; human
review. The review is by an AI model of the same family as the author, in a
fresh context; it is not human peer review. It applies only to the revision
named above.
