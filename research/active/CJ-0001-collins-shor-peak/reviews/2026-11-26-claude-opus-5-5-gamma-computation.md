# Independent review — CJ-0001 — Property Γ for the 47 trees with 2 to 8 vertices (computation)

- **Reviewer:** AI model `claude-opus-5-5` (Claude Code subagent, role `adversarial-reviewer`).
- **Date:** 2026-11-26 (local 13:51 to about 14:05).
- **Independence:** fresh subagent context. It did not have the author's
  reasoning trail or the session's conversation. It had the task message from
  the Research Director (which names the claim, the files and the questions,
  and gives no reasoning or conclusion), the note that defines the objects, and
  the repository. The author of the claim is a different model
  (`claude-fable-5-2`). The reviewer is the same model as the other session-6
  reviewers, so the reviews are not independent of each other with respect to
  the model. The reviewer wrote down the definitions and wrote its own
  recomputation script (Appendix A) **before** reading `skeleton_structure.py`.
  It had read `notes/skeleton-identity.md` first, because the definitions are
  there.
- **Revision reviewed:** `9499572b80873e11ebf8b34afd583edfe1275aa0` (checked with
  `git rev-parse HEAD` at the start and at the end). Files and SHA-256 (the same
  at the start and at the end of the review):

  | File | SHA-256 |
  | --- | --- |
  | `experiments/CJ-0001-collins-shor-peak/skeleton_structure.py` | `a9df35c3a8150593ae0ec48cc8ffed1c0b0e2b3d2b7dad7eb52f20662d0648ec` |
  | `experiments/CJ-0001-collins-shor-peak/results/skeleton-structure.json` | `b54aed716eb41571772d68ffe5052b607a528186b15a9e9151e5278a5c1537b1` |
  | `experiments/CJ-0001-collins-shor-peak/README.md` | `a96540473584f7ee1737defef5346d9d7043e7cd547951476e2ea35f2a9b6340` |
  | `research/active/CJ-0001-collins-shor-peak/notes/skeleton-identity.md` | `747ea150c5347f33848a6ea55035746ab9ef154bf4a625fc905d08d327352ab7` |
  | `experiments/CJ-0001-collins-shor-peak/distpoly.py` (enumeration, distances, provenance) | `43a481a07fd38a320b592ff31334f0a3b102e99a82fa1c4383e0a158574d13d0` |
  | `experiments/CJ-0001-collins-shor-peak/mixed_partials.py` (imported; not used by the Γ test) | `be74832dd1273dfc1fa875e4135c69ab927defaf008e2f9d9769eb89c7a8f5d2` |
  | `tests/test_cj0001_distpoly.py` | `0a44b4344f030519a50249378abc679488fa88e8d91f6255c741470060e0872c` |
  | `research/active/CJ-0001-collins-shor-peak/STATE.md` (wording only) | `24a8eaedaf3de9281676895bc2c1810745df3e604f81c9d8974b3fbb6b75d5e2` |

  The working tree was clean at the start (my rerun recorded `tree_clean: true`).
  During the review, by another process and not by this reviewer,
  `research/candidates/CJ-0001-collins-shor-peak.md` became modified and the
  untracked file `experiments/CJ-0001-collins-shor-peak/component_form.py`
  appeared. Neither is among the reviewed files, whose hashes did not change.
- **Material given to the reviewer:** the task message (claim, file list,
  questions 1 to 5); the repository at the revision above.

## Statement as read from the primary source

**Primary source of the conjecture.** Conjecture 1.2 of Aalipour et al.,
arXiv:1507.02341 (Collins–Shor): for a tree of order `n` the normalized
coefficients `d_0, …, d_{n−2}` of the distance characteristic polynomial peak
between `⌊n/2⌋` and `⌈n − n/√5⌉`. I took this wording from `distpoly.py` and the
README and saw it confirmed in a web search summary; I did **not** reopen the
arXiv PDF. The claim under review is not the conjecture but a finite property
of objects that the project defines, so the operative definitions are those of
the note.

**Definitions (from `notes/skeleton-identity.md`, written down before reading
the script).**

- `S` a tree on `s ≥ 2` vertices, vertex set `V`, distance matrix `P`; `J` the
  all-ones `s × s` matrix, `1` the all-ones vector.
- For `A ⊆ V`: `a = |A|`, `1_A` its indicator, `I_Ā` the diagonal matrix with
  diagonal `1_{V∖A}`.
- `N_A(x) = 2x I_Ā − P − 1_A 1ᵀ − 1 1_Aᵀ − (a/2x) J` for `x ≠ 0`.
- `r_A(x) = −2^{2−s} · x · det N_A(x)`, asserted to be a polynomial of degree at
  most `d = s − a + 1`. (Check: `J` has rank one, so `det N_A` is affine in
  `1/x`; the `x`-degree is at most `s − a`; hence `x det N_A` is a polynomial of
  degree at most `s − a + 1`.)
- Non-negative half-gamma expansion of degree `d`:
  `r = Σ_{e ≥ 0, 2e < d} ρ_e x^e (1+x)^{d−2e} + Σ_{d ≤ 2e ≤ 2d} σ_e x^e`, all
  `ρ_e, σ_e ≥ 0`. The `d + 1` basis elements have lowest-degree terms
  `x^0, …, x^d`, so the expansion is unique and triangular.
- `S` has Property Γ if for **every** `A ⊆ V` with `|A| ≥ 2` the polynomial
  `r_A` has a non-negative half-gamma expansion of degree `d = s − |A| + 1`.

**Claim under review.** Property Γ holds for each of the 47 trees with 2 to 8
vertices (one per isomorphism class; 1 + 1 + 2 + 3 + 6 + 11 + 23). The number of
(tree, subset) pairs it covers is `Σ_trees (2^s − s − 1)` =
1 + 4 + 22 + 78 + 342 + 1320 + 5681 = **7,448**. Property Γ is invariant under
relabelling (simultaneous permutation of `P` and `A`), so checking every subset
of one labelled representative per class covers the claim.

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | The claim has none beyond `2 ≤ s ≤ 8` and `|A| ≥ 2`. The script loops over `size in range(2, s + 1)` and all `combinations(range(s), size)`: exactly the subsets with `|A| ≥ 2`, including `A = V`. Nothing is filtered. |
| Quantifiers | "Every tree with `2 ≤ s ≤ 8`" — covered by the 47 skeletons, verified complete and pairwise non-isomorphic (below). "Every `A` with `|A| ≥ 2`" — covered, 7,448 pairs, confirmed by my own count and by the result file (`gamma_subsets: 7448`). |
| Mathematical definitions | **Matrix and sign.** The script does *not* compute `r_A` from `N_A`. It computes `g_j` from `charpoly(Q(c))` at the `2^s` points `c ∈ {0,1}^s` and Möbius inversion (exact, because `G` is affine in each `c_v`: `c_v` occurs only in column `s+v`), takes the coefficient `p_A` of `c^A` in `Σ g_j x^j`, checks divisibility by `x^{a−1}` and (by synthetic division, `s − a` times) by `(1+x)^{s−a}`, checks `deg ≤ d`, and expands the quotient. That quotient equals the defined `r_A` only through Proposition S2. The script checks S2 for every subset of every skeleton (item 2, an `assert` executed before item 5 in the same run) at `2s + 2` points, and both sides are polynomials of degree `≤ 2s` (the formula side because `a ≥ 1` makes `(2x)^a det N_A` polynomial; `a = 0` has no `1/x` term), so the check is a complete proof of the identity on each subset. Hence the expanded polynomial is the defined `r_A`. Sign: `−det(2xI − Q)/4^{s−1}` with `det(2xI − Q) = Σ charpoly_j 2^j x^j` (FLINT returns `det(yI − Q)`; the dimension `2s` is even, so the convention does not matter for the sign). **Basis.** `rho` for `e in range((d+1)//2)`, i.e. exactly `2e < d`; `sigma = r[(d+1)//2 : d+1]`, i.e. exactly `d ≤ 2e ≤ 2d`. The subtraction uses `comb(d − 2e, step)` from the lowest degree upwards, followed by an assertion that the low part vanishes. Correct. **Degree.** `d = s − a + 1`, as in the note. |
| Exactness | Integers (`fmpz_mat.charpoly`), `Fraction` and `fmpq_mat.det` only. No floats, no modular arithmetic. "Interpolation" of the `g_j` is the exact Möbius inversion on `{0,1}^s` for a multi-affine function (`2^s` values for `2^s` unknowns). S2 is checked at `2s + 2 > 2s + 1` points. No truncation: `p` has all `2s + 1` coefficients; the degree test `any(r[d+1:])` looks at every coefficient above `d`. |
| Non-negativity test | `if expansion is None or min(expansion[0] + expansion[1]) < 0` — applied to every `ρ_e` and `σ_e` of every subset. A failure of divisibility or of the degree bound returns `None` and is counted as a Γ failure, not skipped. There is no `try/except` anywhere in the script, so no case is lost to an exception. |
| Tree enumeration | `distpoly.layouts` (Wright–Richmond–Odlyzko–McKay successor functions, private functions of networkx 3.7; the start layout is the one networkx uses). I checked the 47 parent arrays stored in the result file with my own AHU canonical form (minimum over the centres): all are trees, pairwise non-isomorphic, and they are exactly my 47 classes, obtained twice independently — by growing trees one leaf at a time and by decoding all `s^{s−2}` Prüfer sequences (262,144 for `s = 8`) — with counts 1, 1, 2, 3, 6, 11, 23. The `degrees` field of every entry matches. |
| Boundary cases | `s = 2`: one subset, `A = V`, `r_V = 2 + 5x = 2(1+x) + 3x`, `d = 1`. `A = V` for every tree: `r_V = s + (s+3)x` (47 of 47, my check; `top_expansion = [[s],[3]]` in the result file). `|A| = 2` gives the largest `d = s − 1`. No case has `d = 0`. In my recomputation no expansion coefficient is zero; the minimum is 2. |
| Intermediate lemmas | S1 to S4 were reviewed separately and not re-reviewed here. For the Γ claim itself only S2 matters (to identify the script's quotient with `r_A`), and the script checks S2 by exact computation on each subset concerned, so the Γ claim does not depend on the written proof of S2. My recomputation uses the definition of `r_A` directly and does not depend on S2. |
| Logical implications | (i) Γ for the 47 skeletons: supported by the computation alone (the script's run and my independent recomputation). (ii) "Hence Hypothesis V for those skeletons and every order": this is **not** a computational result. It rests on Γ (computation) **plus** Proposition S4 (`β_A(n) ≥ 0` for every `n ≥ 2s`), the identification of `β_A(n)` with the coefficient of `c^A` in `D_n` (S2, Lemma S1), and the multi-affine identity `∂²D_n/∂c_u∂c_v = Σ_{A ∋ u,v} β_A c^{A∖{u,v}}`, which gives `≥ 0` on real `c ≥ 0`. "Every order" means every `n ≥ 2s`, which is the range in the definition of Hypothesis V(s) in `vertex-principle.md`. The step from the path skeleton to Hypothesis V(s) of `vertex-principle.md` also needs the `D_n` there to be the `D_n` of the note for `S = P_s` ("For a path this is the matrix of Lemma L3"); I did not check that identification. The last part of Corollary S5 (the minimum over the stars, through Lemma L4) is not part of this claim and was not assessed. |
| Dependency assumptions | python-flint 0.9.0 (`charpoly`, `fmpq_mat.det`), networkx 3.7 private enumeration functions. Both are cross-checked: the enumeration by my own enumeration, and the coefficient route by my pure-Python Bareiss determinants and exact interpolation from the definition of `r_A` (coefficient-by-coefficient agreement on all 7,448 pairs, below). |
| Counterexample attempts | (a) The full recomputation (7,448 pairs): 0 failures, minimum coefficient 2. (b) Outside the claimed scope: for `s = 9`, the path, the star and three seeded random trees (Prüfer, seed 20261126), all 502 subsets each; for `s = 10`, the same five shapes, 60 random subsets each. 0 failures; minimum coefficient 2 in every case. This is not evidence for Conjecture Γ beyond these exact cases. (c) Looked for skipped or filtered cases, caught exceptions, truncated degree ranges, an off-by-one in the basis split, and a wrong sign convention for the characteristic polynomial: none found. |
| Formalization scope | Not applicable: nothing about Γ is formalized. |
| Novelty coverage | One web search (standard mode) on the Collins–Shor peak, distance characteristic polynomial coefficients, pendant leaves and gamma expansions. It returned arXiv:1507.02341, its ELA version, a 2021 survey of distance spectra (arXiv:2103.00647) and unrelated pages; nothing on the half-gamma expansion or on `r_A`. Property Γ is defined by the project, so a prior statement of it in this form is unlikely, but this single search establishes nothing about novelty. Novelty stays `unknown` as far as this review is concerned. |
| Unresolved gaps | No gap in the computation. Defects in wording and provenance are listed below; none affects the truth of the reviewed claim. |

### Defects (wording and provenance; none invalidates the Γ claim)

1. **Overstatement about the Lemma S1 check.** In "What is verified, and what is
   conjectured", the note says that for every skeleton with `2 ≤ s ≤ 8` Lemma S1
   was checked against the direct determinant "on small leaf numbers, zeros
   included". The script uses `box = 1` for `s ≥ 6` and requires `Σ c_v ≥ s`, so
   for `s = 6, 7, 8` the only vector checked is `c = (1, …, 1)`. The result
   file confirms it: "1 trees, leaf numbers in 0..1" for each of the 40
   skeletons with `s ≥ 6`. Leaf vectors with zero entries occur only among
   the 564 checks for `s ≤ 5`. Lemma S1 has a reviewed proof, so this
   affects only the description of the evidence.
2. **"Orders up to 100" without committed evidence.** The paragraph after
   Conjecture Γ says that in the range computed (orders up to 100) all the
   trees "skeleton plus one star" satisfy the inequality. The committed result
   file was produced with `--max-order 40` (orders `2s` to 40). According to
   `journal.md` (session 5), the run up to order 100 was a trial on an unclean
   tree and was not kept. So this sentence has no committed evidence. It is not
   part of the Γ claim.
3. **Provenance of the result file.** The `run` block records revision
   `7c1a9dd`, not the reviewed revision. I checked with
   `git diff 7c1a9dd 9499572 -- experiments/CJ-0001-collins-shor-peak/` that
   `skeleton_structure.py`, `distpoly.py` and `mixed_partials.py` are unchanged
   since then. `--out` points to a temporary scratch path: the stored file was
   copied in afterwards, and the copy is not recorded (the hash in
   `research/discoveries.json` does match the stored file). The per-skeleton
   field `subsets_checked` is the expression `2**s − s − 1` written by the
   script, not a count of iterations. The loop does run over exactly that many
   subsets, but the field is not independent evidence. The file stores no
   per-subset expansions or minimum coefficient, so on its own it cannot be
   checked at the coefficient level; the claim rests on the script's logic and
   on reruns.
4. **Stale reviewed-status wording.** The note's header says "none has been
   reviewed" of S1 to S4, and the "What is verified" paragraph ends with "has not
   been reviewed". `STATE.md` records AI reviews of S1 to S4. This understates
   rather than overstates.
5. **"Every order" without "n ≥ 2s".** The `STATE.md` row "Γ, finite" and the
   note's "for all orders" leave out the bound `n ≥ 2s`. That bound is part of
   the definition of Hypothesis V(s), so the wording is not an overstatement,
   but the row does not say it. The row does name S4 as the basis.
6. **Test coverage.** `test_skeleton_expansion_and_property_gamma` covers
   `s ≤ 5` only (105 of the 7,448 pairs). The cases `s = 6, 7, 8` rest on the
   script run (and now on this recomputation).
7. **Timing.** The README says "about 1 min"; the run took 109.9 s according to
   the stored file, and 129 s of wall time on my rerun. This is trivial.

## Reproduction

All runs on the reviewed revision, Windows 10, Python 3.12.4, python-flint 0.9.0, networkx 3.7.

1. **Rerun of the repository script** (from `d:\conjectura`):
   `uv run python experiments/CJ-0001-collins-shor-peak/skeleton_structure.py --max-skeleton 8 --max-order 40 --out <scratch>/skeleton-structure-rerun.json`
   — exit code 0, wall time 129 s (`seconds: 127.6` in the file), `run` block:
   revision `9499572…`, `tree_clean: true`. Totals:
   `skeletons 47, closed_form_trees 604, subset_identities 7820, gamma_failures 0, gamma_subsets 7448, one_vertex_formula_checked 323, locality_classes 505, locality_classes_with_more_than_one_expansion 0, certificate_failures 0, nonpositive_vertices 0`.
   Compared as parsed JSON with the stored result file, after removing the
   fields `run` and `seconds`: **identical**.
2. **Independent recomputation** (`gamma_check.py`, Appendix A; pure Python,
   no repository code, no third-party libraries): `python -I gamma_check.py`, 34.6 s.
   - Enumeration: the leaf-growth and Prüfer enumerations give the same
     canonical-form sets, with counts 1, 1, 2, 3, 6, 11, 23 (47 in total).
   - `r_A` from its definition: `H_A(x) = det(2x N_A(x)) = det(4x² I_Ā − 2x(P + 1_A1ᵀ + 11_Aᵀ) − aJ)`
     is computed by integer Bareiss determinants at the `2s + 1` nodes
     `x = 0, …, 2s` (a polynomial of degree `≤ 2s`, since its entries have
     degree `≤ 2`) and exact Vandermonde inversion. It is then checked at 3
     further nodes (`2s+1`, `2s+2`, `−3`), its coefficients of `x^0, …, x^{s−2}`
     are checked to be zero, and `r_A = −2^{2−2s} H_A / x^{s−1}`. In addition,
     for 1,064 pairs (every seventh), `r_A(x_0) = −2^{2−s} x_0 det N_A(x_0)` was
     checked with Fraction Gaussian elimination at `x_0 = 1/3` and `−5/2`,
     directly on `N_A` with its `1/x` term.
   - Results: **7,448 (tree, subset) pairs; 0 degree violations; 0 failures;
     minimum expansion coefficient 2** (at `s = 2`, `ρ_0` of `r_V`); 0 zero
     coefficients; all coefficients are integers; `r_V = s + (s+3)x` for 47 of 47.
3. **Tie to the stored file** (`compare_trees.py`, 19.5 s): the 47 parent arrays
   of the result file are pairwise non-isomorphic and equal to my 47 classes.
   On those exact labellings my code gives 7,448 pairs, minimum coefficient 2.
4. **Coefficient-level comparison** (`coef_compare.py`, `uv run python -B`, 28.3 s;
   it imports the repository's `half_gamma_expansion` only as the object being
   compared): repository `(ρ, σ)` and my expansion agree on **7,448 of 7,448**
   pairs, with 0 mismatches.
5. **Probe outside scope** (`beyond_scope.py`, 10.9 s): see "Counterexample
   attempts".

Total computation time: about 222 s.

## Verdict

**`no gap found within stated scope`.**

Scope: the claim "Property Γ (as defined in `notes/skeleton-identity.md` at the
revision above: non-negative half-gamma expansion of degree `d = s − |A| + 1` of
`r_A = −2^{2−s} x det N_A`, for every `A` with `|A| ≥ 2`) holds for each of the
47 trees with 2 to 8 vertices". The repository's computation computes exactly
this object, exactly, on every subset the claim covers, with nothing skipped.
The stored result file is reproduced identically. An independent
implementation from the definition confirms it: 7,448 pairs, 0 failures,
minimum coefficient 2, and agreement with the repository coefficient by
coefficient.

The review does **not** cover:

- the consequence "Hypothesis V for these skeletons and every order
  `n ≥ 2s`", which rests in addition on the written Proposition S4, on S1 and
  S2 (reviewed elsewhere), and, for the caterpillar version, on the
  identification of the `D_n` of `vertex-principle.md` with that of the note
  (not checked here);
- Corollary S5's use of Lemma L4;
- item 4 of the script (orders `2s` to 40);
- the two observations (one missing vertex, locality);
- Conjecture Γ in general;
- novelty.

The defects listed above are matters of wording and provenance and should be
corrected; none of them changes the reviewed claim. This review applies only to
revision `9499572b80873e11ebf8b34afd583edfe1275aa0` and the file hashes listed.

## Appendix A — the reviewer's recomputation script

Location (scratch, not in the repository):
`C:\Users\bezze\AppData\Local\Temp\claude\150e3719c412ed18\2231ec3e-df62-46cf-9432-4eead8ab7234\scratchpad\gamma_check.py`,
11,252 bytes, SHA-256 `183ad10c1af358aaa833912cd2a11a4ef633482a9853d78580054abea4317426`.
Auxiliary scripts in the same directory: `compare_trees.py` (2,747 bytes,
`5f94979216edcf455e1cfb5b0fe779c97afc6c6063b7931d6a422e02e357a014`),
`coef_compare.py` (1,685 bytes,
`1dc985a16450b46f33b6e1d9480c9a2e74a567c394a285e5c164857e2fd69eee`),
`beyond_scope.py` (1,495 bytes,
`95382e95dbeec2b0b2c8d42fa9a0e6b747ff6790be28a6164b50b7242faf0e83`).
The scratch directory may be cleared, so the main script is quoted in full.

```python
"""Independent recomputation of Property Gamma (CJ-0001), reviewer scratch script.

Shares no code with the repository. Exact integer / Fraction arithmetic only.

Definitions (from notes/skeleton-identity.md, read before the repository script):
  S tree on s vertices, P its distance matrix, A subset of V, a = |A|.
  N_A(x) = 2x I_Abar - P - 1_A 1^T - 1 1_A^T - (a/(2x)) J
  r_A(x) = -2^(2-s) * x * det N_A(x)
  Property Gamma: for every A with |A| >= 2, r_A = sum_{2e<d} rho_e x^e (1+x)^(d-2e)
                  + sum_{d<=2e<=2d} sigma_e x^e with all rho, sigma >= 0, d = s - a + 1.

Computation: H_A(x) := det(2x N_A(x)) has polynomial entries of degree <= 2, so it
is a polynomial of degree <= 2s; it is recovered exactly from 2s+1 integer nodes
(plus 3 extra check nodes). Then r_A = -2^(2-2s) H_A(x) / x^(s-1), checked to be
a polynomial (low coefficients of H_A vanish) of degree <= d.
"""
import itertools
import sys
import time
from fractions import Fraction


# ---------------- tree enumeration ----------------

def canon(adj):
    n = len(adj)
    if n == 1:
        return "()"
    # centers by repeated leaf stripping
    deg = [len(adj[v]) for v in range(n)]
    layer = [v for v in range(n) if deg[v] <= 1]
    removed = len(layer)
    alive = set(range(n))
    while removed < n:
        new = []
        for v in layer:
            alive.discard(v)
            for w in adj[v]:
                if w in alive:
                    deg[w] -= 1
                    if deg[w] == 1:
                        new.append(w)
        removed += len(new)
        layer = new
    centers = [v for v in layer]
    # if all remaining after loop: layer holds last layer (1 or 2 vertices)
    def enc(v, parent):
        return "(" + "".join(sorted(enc(w, v) for w in adj[v] if w != parent)) + ")"
    return min(enc(c, -1) for c in centers)


def prufer_decode(seq, n):
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    import heapq
    leaves = [i for i in range(n) if degree[i] == 1]
    heapq.heapify(leaves)
    for x in seq:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, x))
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    u = heapq.heappop(leaves)
    v = heapq.heappop(leaves)
    edges.append((u, v))
    return edges


def adj_from_edges(edges, n):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def trees_by_prufer(n):
    reps = {}
    if n == 2:
        e = [(0, 1)]
        reps[canon(adj_from_edges(e, 2))] = e
        return reps
    for seq in itertools.product(range(n), repeat=n - 2):
        e = prufer_decode(seq, n)
        k = canon(adj_from_edges(e, n))
        if k not in reps:
            reps[k] = e
    return reps


def trees_by_growth(nmax):
    out = {2: {canon(adj_from_edges([(0, 1)], 2)): [(0, 1)]}}
    for n in range(3, nmax + 1):
        reps = {}
        for e in out[n - 1].values():
            for v in range(n - 1):
                e2 = e + [(v, n - 1)]
                k = canon(adj_from_edges(e2, n))
                if k not in reps:
                    reps[k] = e2
        out[n] = reps
    return out


def dist_matrix(adj):
    n = len(adj)
    D = []
    for s0 in range(n):
        d = [-1] * n
        d[s0] = 0
        q = [s0]
        for v in q:
            for w in adj[v]:
                if d[w] < 0:
                    d[w] = d[v] + 1
                    q.append(w)
        D.append(d)
    return D


# ---------------- exact linear algebra ----------------

def det_int(M):
    """Bareiss fraction-free determinant of an integer matrix."""
    M = [row[:] for row in M]
    n = len(M)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            piv = None
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    piv = i
                    break
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = M[i][j] * M[k][k] - M[i][k] * M[k][j]
                q, r = divmod(num, prev)
                assert r == 0
                M[i][j] = q
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


def det_frac(M):
    """Gaussian elimination over Fractions."""
    M = [[Fraction(v) for v in row] for row in M]
    n = len(M)
    det = Fraction(1)
    for k in range(n):
        piv = None
        for i in range(k, n):
            if M[i][k] != 0:
                piv = i
                break
        if piv is None:
            return Fraction(0)
        if piv != k:
            M[k], M[piv] = M[piv], M[k]
            det = -det
        det *= M[k][k]
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            if f:
                for j in range(k, n):
                    M[i][j] -= f * M[k][j]
    return det


def vandermonde_inverse(nodes):
    """Exact inverse of the Vandermonde matrix V[i][j] = nodes[i]^j, as Fractions."""
    m = len(nodes)
    V = [[Fraction(x) ** j for j in range(m)] + [Fraction(int(i == r)) for r in range(m)]
         for i, x in enumerate(nodes)]
    # Gauss-Jordan
    for k in range(m):
        piv = next(i for i in range(k, m) if V[i][k] != 0)
        V[k], V[piv] = V[piv], V[k]
        p = V[k][k]
        V[k] = [v / p for v in V[k]]
        for i in range(m):
            if i != k and V[i][k] != 0:
                f = V[i][k]
                V[i] = [a - f * b for a, b in zip(V[i], V[k])]
    return [row[m:] for row in V]  # rows: coefficient index j; cols: node i


def poly_eval(c, x):
    v = Fraction(0)
    for coef in reversed(c):
        v = v * x + coef
    return v


# ---------------- r_A and the half-gamma expansion ----------------

def H_matrix(P, A, x):
    """2x * N_A(x), integer entries for integer x:
    4x^2 I_Abar - 2x (P + 1_A 1^T + 1 1_A^T) - a J."""
    s = len(P)
    a = len(A)
    inA = [v in A for v in range(s)]
    M = []
    for u in range(s):
        row = []
        for v in range(s):
            val = -2 * x * (P[u][v] + (1 if inA[u] else 0) + (1 if inA[v] else 0)) - a
            if u == v and not inA[u]:
                val += 4 * x * x
            row.append(val)
        M.append(row)
    return M


def N_matrix(P, A, x):
    """N_A(x) itself for a rational x != 0."""
    s = len(P)
    a = len(A)
    x = Fraction(x)
    M = []
    for u in range(s):
        row = []
        for v in range(s):
            val = -Fraction(P[u][v]) - (1 if u in A else 0) - (1 if v in A else 0) - Fraction(a) / (2 * x)
            if u == v and u not in A:
                val += 2 * x
            row.append(val)
        M.append(row)
    return M


def r_poly(P, A, Vinv, nodes):
    s = len(P)
    vals = [det_int(H_matrix(P, A, x)) for x in nodes]
    m = 2 * s + 1
    H = [sum(Vinv[j][i] * vals[i] for i in range(m)) for j in range(m)]
    for c in H:
        assert c.denominator == 1
    H = [int(c) for c in H]
    return H, vals


def half_gamma(r, d):
    """Unique expansion in the basis b_e = x^e (1+x)^(d-2e) (2e<d), x^e (d<=2e<=2d)."""
    rem = [Fraction(c) for c in r] + [Fraction(0)] * (d + 1 - len(r)) if len(r) <= d + 1 else None
    assert rem is not None
    coeffs = []
    for e in range(d + 1):
        c = rem[e]
        coeffs.append(("rho" if 2 * e < d else "sigma", e, c))
        if 2 * e < d:
            k = d - 2 * e
            # subtract c * x^e (1+x)^k
            binom = 1
            for i in range(k + 1):
                rem[e + i] -= c * binom
                binom = binom * (k - i) // (i + 1)
        else:
            rem[e] -= c
    assert all(v == 0 for v in rem), rem
    return coeffs


def main():
    t0 = time.time()
    smax = 8
    grown = trees_by_growth(smax)
    counts_growth = {n: len(grown[n]) for n in grown}
    counts_prufer = {}
    for n in range(2, smax + 1):
        pr = trees_by_prufer(n)
        counts_prufer[n] = len(pr)
        assert set(pr.keys()) == set(grown[n].keys()), n
    print("tree counts (growth):", counts_growth, "total", sum(counts_growth.values()))
    print("tree counts (prufer):", counts_prufer)
    print("enumeration time %.1fs" % (time.time() - t0))

    pairs = 0
    failures = []
    min_coef = None
    min_where = None
    zero_coefs = 0
    deg_viol = 0
    pointcheck = 0
    topcheck = 0
    by_s = {}
    for s in range(2, smax + 1):
        nodes = list(range(0, 2 * s + 1))
        extra = [2 * s + 1, 2 * s + 2, -3]
        Vinv = vandermonde_inverse(nodes)
        for key, edges in sorted(grown[s].items()):
            adj = adj_from_edges(edges, s)
            P = dist_matrix(adj)
            for a in range(2, s + 1):
                for A in itertools.combinations(range(s), a):
                    A = set(A)
                    H, _ = r_poly(P, A, Vinv, nodes)
                    # check interpolation at extra nodes
                    for x in extra:
                        assert poly_eval(H, x) == det_int(H_matrix(P, A, x))
                    # divisibility by x^(s-1)
                    assert all(H[j] == 0 for j in range(s - 1)), (s, A, H)
                    r = [Fraction(-H[j], 4 ** (s - 1)) for j in range(s - 1, 2 * s + 1)]
                    while r and r[-1] == 0:
                        r.pop()
                    d = s - a + 1
                    if len(r) - 1 > d:
                        deg_viol += 1
                        failures.append((s, key, sorted(A), "degree", r))
                        continue
                    # direct check against the definition at rational points with 1/x term
                    if pairs % 7 == 0:
                        for x0 in (Fraction(1, 3), Fraction(-5, 2)):
                            lhs = poly_eval(r, x0)
                            rhs = -Fraction(2) ** (2 - s) * x0 * det_frac(N_matrix(P, A, x0))
                            assert lhs == rhs, (s, A, lhs, rhs)
                        pointcheck += 1
                    if a == s:
                        assert r == [Fraction(s), Fraction(s + 3)], r
                        topcheck += 1
                    coeffs = half_gamma(r, d)
                    pairs += 1
                    by_s[s] = by_s.get(s, 0) + 1
                    for kind, e, c in coeffs:
                        if c == 0:
                            zero_coefs += 1
                        if min_coef is None or c < min_coef:
                            min_coef = c
                            min_where = (s, key, sorted(A), kind, e)
                        if c < 0:
                            failures.append((s, key, sorted(A), kind, e, c))
    print("pairs (tree, A with |A|>=2):", pairs, by_s)
    print("degree violations:", deg_viol)
    print("failures:", len(failures))
    for f in failures[:20]:
        print("  ", f)
    print("min expansion coefficient:", min_coef, "at", min_where)
    print("zero expansion coefficients:", zero_coefs)
    print("rational point checks against N_A definition:", pointcheck)
    print("A = V checks r_V = s + (s+3)x:", topcheck)
    print("total time %.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
```

Output of `python -I gamma_check.py`:

```
tree counts (growth): {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23} total 47
tree counts (prufer): {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23}
enumeration time 8.5s
pairs (tree, A with |A|>=2): 7448 {2: 1, 3: 4, 4: 22, 5: 78, 6: 342, 7: 1320, 8: 5681}
degree violations: 0
failures: 0
min expansion coefficient: 2 at (2, '(())', [0, 1], 'rho', 0)
zero expansion coefficients: 0
rational point checks against N_A definition: 1064
A = V checks r_V = s + (s+3)x: 47
total time 34.6s
```
