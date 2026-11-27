# Independent review — CJ-0001 — Lemma S37, Proposition S38, Theorem T7, Lemma S39, Theorem T8 and the section on the location of the peak (`notes/path-maximality.md`)

- **Reviewer:** Claude, model `claude-opus-5-5` (adversarial-reviewer subagent).
- **Date:** 2026-11-27 (work done 14:27 to about 14:45 local time, by the clock).
- **Independence:** a fresh context, launched by the main session. It got the
  task (claim, file, hash, dependencies, checks to make) but none of the
  author's reasoning beyond what is written in the repository. **Limit:**
  the reviewer is the same model as the author of the note
  (`claude-opus-5-5`), so this is not a review by a different model. The
  reviewer read the note and its dependencies. It reconstructed the proofs
  by hand and wrote its own code before it consulted the journal. It then
  read some journal passages: session 11, the lines around the ratio
  observation and the stored symbolic snippet, and the grep matches for
  session 12. They were read only to check where the computations claimed
  in the note came from. The reviewer did not import any project
  experiment module.
- **Revision reviewed:** commit `8b03309499bf14baa1316cb84419ad56d92046b9`
  (HEAD at the start of the review). Uncommitted files in the working tree
  (`experiments/.../tree_shift.py`, `results/tree-shift.json`,
  `tests/test_cj0001_tree_shift.py`, the README change) belong to another
  agent and were not read or used. The SHA-256 of each file, taken from
  `git show 8b03309:<path>`:
  - `research/active/CJ-0001-collins-shor-peak/notes/path-maximality.md`: `b2c0f38ad7050455aa19ac369994bc94ff07ce799bfab93145da91625698ccf5` (git blob `2fa9ded9287d0ac1e391492524f13eeb80deb37f`). This is the file under review.
  - `notes/lower-bound.md`: `d149fd5b6d3ac510f07f4aacca7f419dfbdc9d4dfb5d4bdf38719ac2b07c614d`
  - `notes/rooted-calculus.md`: `5080ea4888af2498dd8c2db4e8cfa79741cd3768b5752949b774ce830140bc92`
  - `notes/wiener-form.md`: `f8d0d773da704d1d09b89fbb0ba1914224eba699a6f11cd1a0c01309d5bc707c`
  - `notes/leaf-telescoping.md`: `66c64a0f250f2dd0420cce99cdfff3d81de3d1fd8fe0f0446ebd96f8df88d06e`
  - `notes/lemmas.md`: `a225898814df1ae584d9c58cb2c983d89bcbbd83121458c8058e9bfc4ca03c6e`
  - `STATE.md`: `2534366f785ec4d0213655d1b252cbbd35855458810fc987a8bff4cc808a58f3`
  - `experiments/CJ-0001-collins-shor-peak/tree_shift_symbolic.py`: `d6198737ba2b9cda366fc5995b4c440b7c710b6950093dd4512c8326a787a5e0`
- **Material given to the reviewer:** the task message. It named the claim,
  the revision and the hash, listed the dependencies and their review
  status, and gave the checks to carry out with a budget of about 30 minutes
  and about 60 tool calls. The statement and definitions were taken from
  `STATE.md` ("Exact statement", "Definitions and conventions").

## Statement as read from the primary source

This was written down before the proofs were read.

- **Conjecture (Collins–Shor), Conjecture 1.2 of arXiv:1507.02341, as quoted
  in `STATE.md`.** For every tree `T` of order `n ≥ 3`, every index at which
  `d_0(T), …, d_{n−2}(T)` is maximal lies in `[⌊n/2⌋, ⌈n − n/√5⌉]`. Here
  `d_k = 2^{k−(n−2)}|δ_k|` and `δ_k = [x^k] det(D − xI)`. This uses the
  project's strong reading of ties.
- **`ℓ_T(x) = −2^{−(n−2)} det(2xI − D)`** (`wiener-form.md`). For
  `0 ≤ k ≤ n−2` its coefficient of `x^k` is `d_k`. The coefficient of
  `x^{n−1}` is `0` and that of `x^n` is `−4`.
- **Cones.** `K_d` is the set of non-negative combinations of `x^e(1+x)^i`
  with `2e + i ≥ d`. `C_d` is the set of those with
  `e + i ≤ d ≤ 2e + i`.
- **Claims under review.**
  - (S37) For all rooted trees `(A,u)`, `(B,v)` with zero weights and every
    `k ≥ 1`, there is an explicit bilinear formula for `ℓ_{T_k} − ℓ_{T′_k}`.
  - (S38) Each of its terms is in `K_{n−1}` when `a, b ≥ 2`.
  - (T7) `ℓ_{T_k} − ℓ_{T′_k} ∈ C_{n−1}`, with the consequences for the
    coefficients and for the increments `μ ≤ ⌊n/2⌋`.
  - (S39) Every non-path tree is `T′_k(A,B)` with `a, b ≥ 2`, `k ≥ 1`, and
    `T_k(A,B)` has one leaf fewer.
  - (T8) For every tree `T` of order `n ≥ 2`, `ℓ_{P_n} − ℓ_T ∈ C_{n−1}`.
  - The equality remark.
  - The statements of the section on the location of the peak.
- **Csikvári's generalized tree shift (GTS).** The reviewer knew it from
  memory, and it was confirmed in the restatement in arXiv:1711.09787,
  Definition 3 (a secondary source; Csikvári's papers were not read). Take
  a path from `x` to `y` whose inner vertices have degree 2, and let `z` be
  the neighbour of `y` on it. Move every neighbour of `y` other than `z` to
  `x`. If `x` or `y` is a leaf, the result is isomorphic to the original
  tree; otherwise it has one more leaf.
  - **Comparison with the note.** In the note `x = u` and `y = v`. `T_k(A,B)`
    is the general tree in which the inner vertices of the path have
    degree 2, so `T_k → T′_k` is exactly the GTS.
  - **Non-trivial case.** "Neither end is a leaf" is the same condition as
    `a, b ≥ 2`.
  - **Conclusion.** The note's `T_k` and `T′_k` agree with Csikvári's
    definition.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | The note's hypotheses are correct, with no hidden assumptions. All weights are zero. `T7`, `S38` and `S39` need `a, b ≥ 2` and `k ≥ 1`. `S37` holds for all `a, b ≥ 1`. Every dependency is used inside its own hypotheses: S33 and T5 need `a ≥ 1` and weight zero, with the state of `(A, 0, u)` at the root `u` of `A` (and `v` of `B`). S34(b), (c) need root weight zero, and after a plant the new root has weight zero, so `J` can be applied again. Lemma K needs an integer weight `ν ≥ 0`, `ν ≠ 0`: here it is `e_1 + e_j`, and `2e_1` when `j = 1`. Lemma A(a) needs `2e + i ≥ 2μ − 1`. (K4) needs degree `≤ d`. |
| Quantifiers | Correct. S37: for all rooted trees and all `k ≥ 1`. T8: for every tree of order `n ≥ 2`, with the increments for `n ≥ 3` and `1 ≤ μ ≤ ⌊n/2⌋`. The induction in T8 runs over the number of leaves. Every non-path tree is covered by S39. |
| Mathematical definitions | Checked against the dependencies. **`J`:** each of its five rows is S34(b), using `Ω^ = R(A,e_u) = E + (1+x)(Ω + xH)` from S34(a). **Merge:** it is S34(c). **`χ`:** the reviewer re-derived it from S23(a) (`xℓ = R + (1+4x)Φ`), `R = E + Ω − (1+2x)²Ψ + 2xG` and `Φ = Ψ + xH`, and also re-proved S23(a) from L1 (`adj(M)1 = Φ1`, `1ᵀτ = 2`). S23(a) was reviewed in the T5–T6 review. **`a_j`:** `a_j = Φ(P_j, e_1 + e_j)`; the diagonal is `1 + 2x` everywhere (for `j = 1` the weight is 2) and the entries beside it are `−x`. **Shifts:** `T_k = merge(plant^k(A,u),(B,v))` and `T′_k = merge(merge(A,B), plant^k(•))` both have order `a + b + k − 1` and are the trees described. **`e`:** the state of `•`, `(1,0,0,0,0)`, has `E = −(1+2x)² + (1+2x)² = 0`. |
| Boundary cases | **`k = 0`:** `Δ_0 = 0`, because merging with `•` leaves the state unchanged (checked symbolically). **`k = 1`:** S37 reduces to S36, because `2xγ_1ĜĜ = 2GG/x` and `2(1+x) + 3x = 2 + 5x`. **`a = b = 2`, `k = 1`:** `P_4 → S_4`. By hand, the state of an edge rooted at an end is `(1+x, 1, 0, 0, 0)`, so the difference is `2x + 5x² = 2x(1+x) + 3x² ∈ C_3`. By L2, `d_1` is 16 for `P_4` and 14 for `S_4`. `d_2` is 20 for `P_4` (Collins's path formula) and 15 for `S_4`. **`a = 1` or `b = 1`:** the right side is 0. This was checked on actual trees: 3,080 cases include all of them, and the difference is 0. **`n = 4, 5`:** covered by the shift checks. **`n = 2, 3`:** T8 is trivial (every tree is a path). **`μ ≤ n − 2`:** this holds when `n ≥ 3`. |
| Lemma S37 | **Verified.** The reviewer reconstructed the proof. **Generating function:** `Σ_k J^k t^k = adj(I − tJ)/det(I − tJ)`, and `χ` and `m` are linear in the argument that carries `J^k`, so `F = L/det(I − tJ)` with `deg_t L ≤ 4`. The computed degree is 4. **Determinant:** with the order `(Ψ,H \| G \| Ω,E)` the matrix is block lower triangular. The blocks are `[[1+x,x],[1,x]]`, `(x)` and `[[1+x,1],[x,x]]`, and both 2×2 blocks have trace `1+2x` and determinant `x²`. So `det(I − tJ) = (1 − xt)Q²` (confirmed symbolically). **The four series:** the reviewer re-derived the generating functions of `a_{k−1}`, `γ_k`, `γ_{k−1}` and `ρ_k`. For `ρ_k`, put `j = k−2−i`; this gives `x t² (1−xt)^{−2} (t/Q)′`. **Degree bound:** `Q − tQ′ = 1 − x²t²`, so the four contributions to `DC` have degrees 5, 4, 5 and 4, and `D(F − C) = N` has degree at most 5. Since `D(0) = 1`, agreement of `Δ_k` with `c_k` for `k ≤ 5` forces `N ≡ 0 mod t⁶`, hence `N = 0`. **Computations:** the reviewer's own code checked the closed form for `k = 1..8` in free variables and `F = C` as rational functions. It also checked the formula on actual trees, with `ℓ` taken from the distance matrix and the states from their definitions; see Reproduction. |
| Proposition S38 | **Verified, level by level.** `a_j ∈ K_j` by Lemma K, and `a_0 = 1 ∈ K_0`. `x^i a_{k−1−i} ∈ K_{k−1+i} ⊆ K_{k−1}`, so `γ_k ∈ K_{k−1}` and `γ_{k−1} ∈ K_{k−2}` (`k ≥ 2`). `x·x^{i+1}a_{k−2−i} ∈ K_{k+2+i}`, so `xρ_k ∈ K_{k+2}`; its coefficients `(i+1)(k−1−i)` are non-negative. With `H ∈ K_{a−2}`, `Ĝ ∈ K_{a−1}` and `E ∈ K_{a+1}` (S33(b), (c), T5(ii)), the six products land in `K_{n−1}`, `K_n`, `K_n`, `K_{n−1}`, `K_n` and `K_{n−1}`; the reviewer recomputed each exponent sum. All the scalar coefficients (2, 2, 2, 3) are positive. |
| Theorem T7 | **Verified.** The difference is in `K_{n−1}` and has degree `≤ n−2`, because both trees have order `n`, so the coefficients of `x^n` and `x^{n−1}` agree. (K4) then gives `C_{n−1}`. The coefficient inequalities follow from non-negativity. The increments follow from `K_{n−1} ⊆ K_{2μ−1}` for `μ ≤ ⌊n/2⌋` and Lemma A(a). By computation, `ℓ_{T_k} − ℓ_{T′_k} ∈ C_{n−1}` holds for all 95,248 ordered GTS on trees of order 4 to 14, in which isomorphic duplicates are included. |
| Lemma S39 | **Verified.** The walk from a leaf through vertices of degree 2 stops at a vertex `z` with `deg z ≥ 3` unless the tree is a path. `z` has at least two neighbours off the path. Each component of `T′ − z` other than the path piece contains exactly one of them, so a split into non-empty `N_1`, `N_2` gives `A` and `B` with `a, b ≥ 2` and `T′ = T′_k(A,B)`. **Leaf count:** the vertices of `A ∖ z` keep their degree. `z` is not a leaf of `T′`. In `T_k` the two ends have degree `deg_A(u) + 1 ≥ 2` and `deg_B(v) + 1 ≥ 2`. So the count drops by exactly one (the leaf `w`). **Attack:** every leaf and every split of every non-path tree of order 3 to 11 gave 34,928 constructions. In all of them, `T′_k ≅ T′` (networkx isomorphism), `a, b ≥ 2`, `T_k` is a tree of order `n`, and `T_k` has one leaf fewer. There was no failure. |
| Theorem T8 | **Verified.** The induction on the number of leaves is sound. The base case is the path, the only tree with two leaves. The step uses S39 and T7 with their exact hypotheses, and `C_{n−1}` is closed under addition. The combined statement with T6(b) and the inequalities follow as in T7, with (K1) `C ⊆ K`. |
| Remark (equality) | **Verified.** `Σ deg² = Σ(deg−2)² + 4n − 8`. `Σ(deg−2)² ≥ #leaves`, which is at least 3 for a non-path and exactly 2 for the path. So `d_1(T) < d_1(P_n)` for every non-path tree; this was checked on all trees of order ≤ 18. The parenthetical sentence about the star has a wording defect (D3). |
| Section "location of the peak" | **The implications are correct, and no peak claim is proved that is not.** **Item 1** follows from T6(b) and T8. **Item 2:** the range is exact. `2μ − 1 ≤ n − 1` if and only if `μ ≤ ⌊n/2⌋`, and the generator `(1+x)^{n−1} ∈ K_{n−1}` has `λ_μ < 0` for `μ > n/2`. **Item 3, lower side:** it rests on T6(c), as stated. The star's peak is unique at `⌊n/2⌋`; the reviewer proved this by hand from `d_k(S_n) = (n−k−1)(C(n−1,k) + 4C(n−1,k−1))` (`d_{m+1}/d_m = (5m²−7m−6)/(5m²−5)` for `n = 2m` and `(5m²−m−4)/(5m²+m)` for `n = 2m+1`, both `< 1`) and checked it for `n = 3..160`. **Counterexample sequences:** `(1,2,3) ≤ (1,10,9)`; both are log-concave, and their maxima are at indices 2 and 1. The example is correct. **(PX-peak)** is stated as open, which is correct. It holds for every tree of order ≤ 18 (reviewer, all 205,003 trees). **(PM) ⇒ (PX-peak):** correct, by S39 and transitivity, with the same induction as T8. **(PX-peak) plus "`p_max(P_n) ≤ ⌈n − n/√5⌉` for all n" ⇒ every maximizing index is `≤ M`:** correct as an implication. Its premise is a reading of Collins's informal last step, not his stated theorem (D6); the reviewer checked it for `n = 3..160`. **(PM)** never failed on the 95,248 shifts. The remarks on ratio dominance and on "cannot be obtained through the cone" are overstated (D5). |
| Logical implications | S37 needs S34(b), (c), S23(a) and the finite identity, which is replaced by the `F = C` check. S38 needs Lemma K, (K2), S33 and T5. T7 needs S37, S38, (K4) and Lemma A(a). T8 needs T7, S39 and induction. The combined statement needs T6(b). Every arrow was checked. No arrow uses an open statement ((PX-peak), (PM), or Collins Theorem 3). |
| Dependency assumptions | **Relied on, with their earlier review status:** S33, S34(a)–(c), T5(ii), T6(b), (K4), Lemma K, Lemma A(a) and L2. **Re-derived here:** S23(a) from L1, the plant matrix and the `χ` formula. **Checked on actual trees from their definitions** (`R(T,ν) = (N+j−1)(1+x)Φ − pᵀadj(M)p`, `Ω = Σ_i R(T_i, e_{u_i})P_i`, `G = (1+2x)Ψ − π_u`): the plant rule `J` (29 rooted trees of order ≤ 5, one plant each), `xℓ = χ(s)`, and S37 itself. The merge rule was checked only through S37 on actual trees. Lemma K and T5 were not re-proved. **External:** Fact 1.1 and Theorem 2.1 of arXiv:1507.02341 (sign and log-concavity), as used in T6, were not re-checked. |
| Counterexample attempts | **None found.** **(a)** The symbolic identity held. **(b)** S37 on actual trees: 3,080 cases (rooted trees of order 1–5, `a + b ≤ 9`, `k = 1..5`, trees up to order 13), 0 failures. **(c)** T8 (membership in `C_{n−1}`, every coefficient, every increment `μ ≤ ⌊n/2⌋`) on all 205,003 trees of order 2–18 (counts agree with OEIS A000055), on 104 extreme trees of order 60, 61, 64 and 75 (stars, brooms, spiders, double stars, random caterpillars, random Prüfer trees), and on 18 trees of order 100 and 121: 0 failures. **(d)** S39: 34,928 constructions, 0 failures. **Also:** T7 and the leaf count on 95,248 ordered GTS of orders 4–14, 0 failures. **Membership test:** a polynomial is placed in `C_d` when its (unique) half-gamma expansion has non-negative coefficients. That is a direct witness of membership, so the test does not depend on Lemma C. |
| Formalization scope | Not in scope. No Lean statement corresponds to S37–T8. `verify_lean.py` was not run. |
| Novelty coverage | **Not assessed.** The note claims no novelty. The reviewer ran two web searches (standard mode): "coefficients distance characteristic polynomial trees path maximal star minimal each coefficient" and "generalized tree shift Csikvári distance matrix characteristic polynomial coefficients trees". Neither turned up a statement of coefficientwise extremality of the path for the distance polynomial, or of GTS monotonicity for it. **Not read and possibly relevant:** arXiv:1711.09787 (q-Laplacians along the GTS poset, linked to the exponential distance matrix) beyond its definition; Nagar–Sivasubramanian (SLC); arXiv:2405.09027 (Ding, the Tutte polynomial along Csikvári's poset); Csikvári's two papers; Graham–Lovász (1978). This is not a literature search, and originality is not established. |
| Unresolved gaps | **None found.** No step was left that the reviewer could not reconstruct. |

### Defects (not gaps)

- **D1. Where the "k = 1..12" check came from.** The proof says the finite
  identity `Δ_k = c_k` "was checked by exact symbolic computation for
  `k = 1, …, 12`" and points to the journal of session 11. The code recorded
  there only prints `factor(Δ_k)`. It does not compare `Δ_k` with `c_k`. The
  lemma does not depend on this, because the stored script checks `F = C`
  directly; the reviewer reran it and also checked independently. But the
  sentence claims a comparison that the recorded code does not make.
- **D2. Notation clashes.**
  - `a_j` (the path determinant) is used next to `a = |A|`, and next to
    `a_v = x^{δ_v−1}Π_{uv}` from `lower-bound.md`, which the note imports.
  - `ρ_k` clashes with `ρ_k(T) = d_{k+1}/d_k` (`STATE.md`) and with `ρ` (the
    `R` of `B`) in the proof of S36.
  - `C(t)` clashes with the cones `C_d`, and `Q(t)` with `Q¹`.
  - In T8, `T_0 := T_k(A,B)` reads as the case `k = 0` of `T_k`, which is a
    different tree (`merge(A,B)`, of order `a + b − 1`).
- **D3. Equality remark, last sentence.** It says "the same computation
  gives `d_1(T) > d_1(S_n)` when `T` is not the star", and then "not proved
  here". These contradict each other. The statement is true, because the
  star uniquely maximizes `Σ deg²` among trees, but it does not follow from
  "the same computation".
- **D4. Star peak, citation.** "single maximizing index `⌊n/2⌋` (Collins
  1989, Theorem 1; S23(d))": S23(d) gives only `d_{m−1} < d_m`. The other
  side rests on Collins's Theorem 1 alone. The reviewer proved it from the
  closed form (see the table).
- **D5. Two negative claims are stronger than their support.**
  - "(PM) cannot be obtained from Lemma S37 through the cone". What is shown
    is only that `C_{n−1}` does not control `λ_μ` for `μ > ⌊n/2⌋`. This is a
    claim about methods, not a proof.
  - "the ratio `d_{j+1}/d_j` is not monotone for `j ≥ ⌊n/2⌋` … So a proof of
    (PM) cannot go through ratio dominance". Failure at *some*
    `j ≥ ⌊n/2⌋` does not by itself rule out dominance at the single index
    `j = p_max(T_k)`, which is all such a proof would need.
  - The reviewer's computation shows that dominance fails at that index too:
    2,292 of 95,248 ordered shifts, orders 4–14. The smallest is
    `S(2,2) → S_6`, with `ρ_3 = 65/148` against `45/100`, where `p_max = 3`
    for both. So the conclusion about pointwise ratio dominance is true, but
    the note's cited evidence (unstored scratch) does not support it as
    written.
- **D6. Premise attributed to Collins.** The inequality
  `p_max(P_n) ≤ ⌈n − n/√5⌉` for every `n` is written after "Collins's
  theorem on the path". Per the dossier, Theorem 3 as stated says only "peak
  at `n(1 − 1/√5)`", and the bound comes from its informal last step. The
  note does flag this informality. The reviewer checked the inequality only
  for `n = 3..160`.
- **D7. Header dependency list.** It says that everything rests on
  `lower-bound.md` and S19. It omits S23(a) (`leaf-telescoping.md`), Lemma K
  and Lemma A(a) (`wiener-form.md`), and L2 (`lemmas.md`), which the body
  uses.
- **D8. Unstored scratch runs.** The "Exact checks" of session 11 are not
  stored, and the note acknowledges this ("Owed"). The figure 81,134 for
  orders 4–17 agrees with OEIS A000055.

## Reproduction

All commands were run from `d:\conjectura` at `8b03309`. The scripts are in
the reviewer's scratch directory
(`C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\a6e6cca6-e58c-444f-9aab-25f87b31d224\scratchpad\`).
They are not in the repository.

1. **Stored script of the note, extracted with `git show`.**
   `uv run --with sympy==1.14.0 python -I <scratch>/stored/tree_shift_symbolic.py`
   printed `F - closed form = 0` and "generating functions of a_j and rho_k
   agree with their definitions up to t^8", sympy 1.14.0 (about 11 s).
2. **`rev_a_symbolic.py`** (reviewer's code, sympy 1.14.0). Results:
   - The closed form of S37 equals `χ(m(J^k s_A, s_B)) − χ(m(m(s_A,s_B), J^k e))`
     for `k = 1..8` in ten free state variables.
   - `det(I − tJ) = (1 − xt)Q²`.
   - The `k = 0` case gives 0.
   - The numerator `L` has `t`-degree 4.
   - `F − C = 0` as rational functions.
   - `Q − tQ′ = 1 − x²t²`.
3. **`rev_b_trees.py`** (sympy, networkx 3.7, python-flint 0.9.0).
   - **Method:** `ℓ` is taken from `fmpz_mat(D).charpoly()` and normalized.
     The states come from their definitions (Laplacian determinants,
     adjugate, `R(T,ν)`, `Ω`), with no use of the plant or merge rules.
   - **Plant rule `J`:** 0 failures on 29 rooted trees.
   - **`xℓ = χ(s)`:** 0 failures.
   - **S37 on actual trees:** 3,080 checks, 0 failures (113 s).
4. **`rev_c_T8.py 18 14`.**
   - **Tree counts:** orders 2–18 match A000055 (123,867 at order 18).
   - **T8:** 0 failures in `C_{n−1}`, in the coefficients and in the
     increments.
   - **(PX-peak):** 0 failures.
   - **`d_1(T) < d_1(P_n)`:** 0 failures.
   - **Families:** 104 trees at n ∈ {60, 61, 64, 75}, 0 failures.
   - **GTS, orders 4–14:** 95,248 shifts. T7: 0 failures. Leaf count: 0
     failures. (PM): 0 failures.
   - **Ratio dominance:** violated at some `j ≥ ⌊n/2⌋` in 89,068 shifts, and
     at `j = p_max(T_k)` in 2,292 shifts.
   - **Time:** 100 s in total.
5. **`rev_d_S39_peaks.py`.**
   - **S39:** 34,928 constructions, 0 failures.
   - **Star:** a unique maximizing index `⌊n/2⌋` for `n = 3..160`, 0
     failures.
   - **Path:** `p_max(P_n) ≤ n − isqrt(n²//5)` for `n = 3..160`, 0 failures.
   - **Counterexample sequences:** the note's example was confirmed.
   - **T8 at n = 100, 121:** 18 trees, 0 failures.
6. **`rev_e_ratio.py`.** It prints `S(2,2)`: `d = [5,44,126,148,65]` and
   `S_6`: `d = [5,36,90,100,45]`. Both have `p_max = 3`, and
   `45/100 > 65/148`.

The project's test suite was not run (instruction of the caller).
`verify_lean.py` was not run (Lean is not in scope).

## Verdict

`no gap found within stated scope`

**What the verdict covers.**
- The mathematical content of `notes/path-maximality.md` at `8b03309`:
  Lemma S37, Proposition S38, Theorem T7, Lemma S39, Theorem T8, the
  equality remark, and the logical status of the implications in the section
  on the location of the peak.
- Every step was reconstructed by the reviewer.
- The finite identity was re-verified by independent code.
- The statements were tested on actual trees, as listed above.
- (PM) ⇒ (PX-peak) is a correct implication.
- (PX-peak) together with "`p_max(P_n) ≤ ⌈n − n/√5⌉` for all `n`" ⇒ the
  upper half is a correct implication.
- The section proves nothing about the peak index beyond T6(c) (the lower
  half), and it labels (PX-peak), (PM) and the path bound as unproved or
  informal.

**What the verdict does not cover.**
- The correctness of the dependencies: S33, S34, T5, T6, Lemma K, Lemma A,
  (K4), L1 and L2 were relied on with their earlier review status. They were
  checked here only through their consequences on small trees, except where
  re-derived as stated above.
- Fact 1.1 and Theorem 2.1 of the source.
- Collins's Theorem 3.
- Any Lean formalization.
- Novelty, which was not assessed.
- The defects D1–D8, which are not gaps but should be corrected.

**Independence.** It was limited: the reviewer and the author are the same
model (`claude-opus-5-5`). This is an AI review, not a human review. It
applies only to revision `8b03309` and to the file hashes listed above.
