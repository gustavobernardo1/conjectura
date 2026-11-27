# Independent review (recheck) — CJ-0001 — `notes/upper-bound.md`, revision 1 (Theorem T9, S40 to S46, T10)

- **Reviewer:** Claude, model `claude-sonnet-5-5`, run as the `adversarial-reviewer` subagent.
- **Date:** 2026-11-27
- **Independence:** fresh subagent context. I received the task (catalogue id,
  paths, revisions, the two earlier reports) and no reasoning trail of the
  author. I am the same model that wrote one of the two reports being
  rechecked (`2026-11-27-claude-sonnet-5-5-upper-bound.md`), so independence
  from that report is limited to context; the author of the note is
  `claude-opus-5-5`. This is a recheck of a diff, not a fresh review of the
  whole proof: the unchanged steps are covered by the two earlier reports and
  were re-read only where the diff touches them.
- **Revision reviewed:** commit `2037b18c2823900d159efdacf1a68d4619bec0e3` (`2037b18`), compared with `53421a6`.
  Working copy status at review time: the files below are unmodified relative to `2037b18`
  (other files in the tree, `STATE.md` among them, are modified and were not read).
  - `research/active/CJ-0001-collins-shor-peak/notes/upper-bound.md` SHA-256 `ad21eeb615ab3a500dd0ad8575ae15ce323a09233dde6537fee7b0f6a449e0ed`
  - `experiments/CJ-0001-collins-shor-peak/upper_bound.py` SHA-256 `2de1d3efbf2d1b362e251a318178cc77b827288a0e9e82ecd58e91bcdc442b4e` (git blob `b62ebcd…`, equal to the blob at `917d657`)
  - `experiments/CJ-0001-collins-shor-peak/results/upper-bound.json` SHA-256 `989be91d97186704dca7668793ec9e7c7b0d9c2b4376fece7c048100b72f85de`
- **Material given to the reviewer:** the diff `git diff 53421a6 2037b18 -- notes/upper-bound.md`, the note, the two earlier reports, the script and the result file.

## Statement as read from the primary source

Conjecture 1.2 of arXiv:1507.02341 (read via `STATE.md`): the normalized
coefficients `d_k`, `0 ≤ k ≤ n−2`, of the distance characteristic polynomial of any tree of
order `n` are unimodal with peak between `⌊n/2⌋` and `⌈n − n/√5⌉`. The note
claims the upper half: Theorem T9, every maximizing index `p` satisfies
`p < n − n/√5 + 3/5`, hence `p ≤ ⌈n − n/√5⌉`, for every tree of order `n ≥ 3`.
The recheck concerns only the changes of revision 1; T9, S40 to S46 and T10 have the same statements and
proof steps as at `53421a6` (verified from the diff, below).

## Findings

| Item | Finding |
| --- | --- |
| Hypotheses | Unchanged. S45 and T10 only rename `p, q → j_1, j_2`; the hypotheses `|X| ≥ 2`, `j_1, j_2 ≥ 1` and the added `1 ≤ j_1 ≤ N − 1` (follows from `j_2 ≥ 1`) are consistent. |
| Quantifiers | Unchanged. In T9 the mode of `q` is now `m_q` (was `m`), the maximizing index of `d` stays `p`; no clash remains. |
| Mathematical definitions | `γ = 2 log φ` replaces `c` in S44(iii); the remaining `c_r` is the only `c` in S44. `grep` shows no stale `p, q` pendant-path names in S45 or T10 (the only `p, q` left are in the revision paragraph itself). |
| Boundary cases | `n = 1` in S46: I checked it. For `n = 1` the sum has one term `θ_0 = 0` and `Σ cos(mθ_0) = 1` for all `m`; the note's case split gives `n = 1` for even `m` (since `2n \| m` iff `m` even) and `1` for odd `m` — consistent. The formula of S46 at `n = 1` gives `1/√5 + 2/5 + (2/√5) r²/(1−r²) = 1.0000`, the trace of `(I+L_{P_1})^{-1} = [1]`. `m = 1` in the new closed form of S44: `2 sinh u sinh 2u / cosh u = 4 sinh² u = t`, the determinant of the `1×1` matrix `[t]` (`L_{P_1} = 0`); correct. |
| New sentence: closed form of `det(tI + L_{P_m})` (S44) | Correct, `m ≥ 2`. Re-derived: `t = 4 sinh² u`, `e_j = cosh((2j+1)u)/cosh u` (`e_0 = 1`, `e_1 = t+1`, recursion by `2cosh 2u·cosh((2j−1)u) = cosh((2j+1)u) + cosh((2j−3)u)`); expanding at an end, the minor of the other `m−1` vertices is `e_{m−1}` (one end has diagonal `t+1`, the vertex next to the removed end has `t+2`) and the second term is `e_{m−2}`; then `(t+1)e_{m−1} − e_{m−2} = [cosh((2m+1)u) − cosh((2m−1)u)]/cosh u = 2 sinh u sinh(2mu)/cosh u`. The `m = 2` case: `(t+1)² − 1 = t² + 2t` agrees with `e_1 = t+1, e_0 = 1`. |
| New sentence: `n = 1` / `e^{iπm/n} ≠ 1` in S46 | Correct and complete: for odd `m`, `m/n` an even integer `2l` would give `m = 2nl` even. `Re[2/(1 − e^{iψ})] = 1` is the standard `Re 1/(1 − e^{iψ}) = 1/2`. Closed form of S46 confirmed independently: `2r/(1 − r²) = 2/√5`, `Σ_{m odd} r^m = r/(1−r²) = 1/√5`, giving the `2/5` term. |
| New sentence: reworded last remark (Remarks, third bullet) | Correct. With `tr > n/√5`: `μ_q ≤ n − tr < x`, so `m_q < μ_q + 1 < x + 1`, hence `m_q ≤ ⌈x⌉` (`x` irrational); S41 then gives `p ≤ ⌈x⌉` by the argument of T9 with `K` replaced by `⌈x⌉`. The extra `2/5` is used only for `K`. The remark now says what both earlier reports said it should. |
| New sentences: header and Corollary 2 | The header now restricts "uses none of the cone machinery" to the proof of T9 and names Corollary 1 (uses T6(c), MD-0019): accurate. The Corollary 2 addition (peak of the path is `⌈x⌉` only if the fractional part of `x` exceeds `4/5`) agrees with Corollary S48(a) of `path-peak.md` and with the stored experiment (smallest fractional part among ceiling cases `0.80128`). One residual imprecision of the header, see D3 below. |
| Description of the stored computation ("Exact checks") compared with the result file | Matches `results/upper-bound.json` part by part: A (T10, trees of order 2 to 20: parameter `n_a = 20`, 2,692,065 cases); B1 (`n ≤ 200`, exact) and B2 (50 digits, `n ≤ 60`); C all trees `n_c = 18`, path `n_path = 2000` (2,026 + 205,003 cases); D (S45: `|X| = 2..8`, `j_1 + j_2 ≤ 8`, 16 pairs, 3,184 cases); E (S44(iii), `N = 2..60`); M (S43 trace identity, rooted trees of order ≤ 6, 1,369 pairs); F (S42 exploratory floating point, trees of order 3 to 14). The `run` block records the command, `git_revision` `917d657c9f…`, `tree_clean: true`, `dirty_files: []`, versions, `sources` with the SHA-256 of `upper_bound.py` (`2de1d3ef…`, equal to my hash) and `identical_to_git_revision: true`; `seconds` = 298.7 (the note says 299 s), `summary.failures` are 0 in every part. The note calls it a "provenance block"; the key in the file is `run` (plus `sources`): wording only. `upper_bound.py` is identical at `917d657` and `2037b18` (same blob). The note's commit statement is accurate (script committed at `3b95386`). I did not re-run the whole script (about 5 minutes); I re-ran my own checks only (below). |
| No-change claim | Verified from the diff: the statement of T9, T10 and S40 to S46 and every displayed formula of a proof are unchanged, except for renaming and the additions listed above. Every added sentence is correct. |
| Defects of the earlier reports: disposition | See table below. |
| Dependency assumptions | Unchanged: (GL), (W), (N), (D), (M) taken from the literature, and the identification `ℓ_T = Σ d_k x^k` from `lemmas.md`. |
| Counterexample attempts | None new (no mathematics changed); the earlier reports' exhaustive checks stand. |
| Formalization scope | None; not applicable to this review. |
| Novelty coverage | Not assessed; unchanged since the earlier reports (unknown). |
| Unresolved gaps | No mathematical gap. Defects of the revision, D1 to D4 below. |

### Disposition of the listed defects

| Defect | Disposition at `2037b18` |
| --- | --- |
| Opus D1 / Sonnet D1 (stored computation not in the revision) | Repaired: script, test and result are committed; the note cites the revision of commit and of the run. See the caveat D2 below (README). |
| Opus D2 / Sonnet D4 (wording of the last remark) | Repaired (checked above). |
| Opus D3 (overloaded symbols) | Repaired for `q`, `c`, `m`; `tr(H)` is left (it is defined in "Notation" as `tr G_H`, so it is not ambiguous). |
| Opus D4 / Sonnet D2 (Darroch cited, not checked at the source; Graham–Lovász, Graham–Pollak checked only numerically; "second route" unchecked; Merris eq. (2) not located) | **Neither repaired nor mentioned.** The revision paragraph does not list it as left. Not a mathematical gap (citations are classical and were tested numerically by both reviewers), but the instruction "repaired or explicitly left with a reason" is not met. See D1 below. |
| Sonnet D3 (closed form written out) | Repaired, correct. |
| Sonnet D5 (header) | Repaired, see D3 below for a residual point. |
| Sonnet D6 (`n = 1`) | Repaired, correct. |

### Defects of revision 1 (none affects the proof of T9)

- **D1 (bookkeeping).** The revision paragraph says "Changes, all of wording, notation or citation", and lists the
  repairs, but does not say that Opus D4 and Sonnet D2 (the citations of Darroch's rule, (GL) and Merris eq. (2)
  are not checked at their sources; the "second route" is unchecked) are left open. They should be recorded as
  left, with the reason (not resolved in this session), so that a later reader does not take them as repaired.
- **D2 (stale README).** The README of the experiments directory at `2037b18` (section "The trace of `(I+L)^{-1}` and the peak bound",
  "Command of the stored run" and "Provenance") still says the run took 293.2 s and that HEAD at the time of the run
  was `53421a6` with `tree_clean: false` (the earlier run, overwritten). The stored result file says 298.7 s at `917d657`, clean tree.
  The note itself agrees with the result file, not with the README; the README is the file the note's earlier text
  pointed to ("see the README"). The README heading also says "session 12" for a script the note dates to session 13.
  The README should be brought in line with `results/upper-bound.json`.
- **D3 (residual wording of the header).** The header says the proof of T9 "uses none of the cone machinery ...,
  only the classical facts listed under 'Tools'". S40 also uses the identification of the coefficients `d_k` of
  `ℓ_T` with the normalized coefficients of the source (project lemma `lemmas.md`, Observation 3.1 of the source),
  which is not under "Tools". The earlier text had the same imprecision; it is not cone machinery, so the
  substance of the sentence stands.
- **D4 (trivial).** The note names the block `provenance`; the key in the result file is `run` (with `sources`).

## Reproduction

All scratch (session scratchpad, not stored), run with `uv run --project d:/conjectura python …`.

- `git diff 53421a6 2037b18 -- research/active/CJ-0001-collins-shor-peak/notes/upper-bound.md` read in full; every hunk classified (header, revision paragraph, S44 closed form, S45/T10 renaming, `γ`, S46 `n = 1`, `m_q`, Corollary 2, remarks, exact-checks section).
- `sha256sum` of the files above; `git hash-object upper_bound.py` = `git rev-parse 917d657:…upper_bound.py` = `b62ebcd2e832cb2010e046d64e43f8d67c679948`.
- Result file read with Python `json`: keys, `run`, `sources`, `parameters`, `summary` (all failure counts 0; `completed: true`; `seconds` 298.7).
- Closed forms re-derived by hand (S44, S46) and the S46 formula evaluated at `n = 1` numerically (1.0000).
- The stored computation (`upper_bound.py`) was **not** re-run in full (about 5 minutes); its recorded result was inspected only.

## Verdict

`no gap found within stated scope`

Scope: revision 1 of `notes/upper-bound.md` at `2037b18`, as a recheck of the diff against `53421a6`: the changes are
wording, notation, citation and added elaborations; no statement and no step changed materially; every new sentence
is correct; the description of the stored computation agrees with `results/upper-bound.json` and the script at the
same blob. Defects D1 to D4 above are not gaps in the proof. It does not extend to the unchanged parts beyond what the two
earlier reports covered, to Corollary 1 (lower half, T6(c)), to the "second route" of T10, to novelty (unknown), or to
formalization (none). One AI review, by a model of the same vendor as the author; not human review.
