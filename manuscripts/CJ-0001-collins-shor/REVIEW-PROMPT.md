# Prompt for an independent review of `main.tex`

Give the reviewer this text, the file `main.tex` (or its compiled PDF) at a
named revision, and, if the reviewer can read it, arXiv:1507.02341. Nothing
else.

---

You are asked to review a mathematical manuscript as an independent referee
whose task is to find errors. The manuscript claims a complete proof of the
following conjecture (Conjecture 1.2 of Aalipour, Abiad, Berikkyzy, Hogben,
Kenter, Lin and Tait, arXiv:1507.02341; originally Conjecture 9 of
K. L. Collins, Discrete Appl. Math. 25 (1989) 27–35):

> For every tree `T` with `n ≥ 3` vertices and distance matrix `D`, let
> `δ_k` be the coefficient of `x^k` in `det(D − xI)` and
> `d_k = 2^{k−(n−2)} |δ_k|` for `0 ≤ k ≤ n−2`. Every index `p` with
> `d_p = max_k d_k` satisfies `⌊n/2⌋ ≤ p ≤ ⌈n − n/√5⌉`.

The manuscript was written with the help of AI systems. Treat every claim in
it, including its statements about what was checked, as unverified.

Please:

1. For each lemma, proposition, corollary and theorem, check every step of
   its proof. Reconstruct computations yourself. Pay attention to hypotheses,
   quantifiers, boundary cases (one vertex, `n = 2, 3, 4`, a root with one
   neighbour, empty sums and products, cones `K_d` with `d ≤ 0`), signs,
   degrees of polynomials, and the arithmetic of the cone memberships.
2. Check that each cited classical result is stated correctly and used
   within its hypotheses (Graham–Lovász inverse, Graham–Pollak determinant,
   log-concavity from arXiv:1507.02341, Weyl interlacing, Newton's
   inequalities, Darroch's rule, M-matrix facts, the spectrum of the path,
   Collins's formula for the path).
3. Check that the Main Theorem follows, for every maximizing index (ties
   included).
4. If you can run code, test any step you doubt on small trees in exact
   arithmetic, and try to construct counterexamples to intermediate
   statements.
5. Assess whether the sections on literature, novelty and status overstate
   anything.

Report: (a) the revision or hash of the file you read; (b) your model or
name; (c) a verdict, either "gap found" or "no gap found within the scope of
this review"; (d) a numbered list of findings, each classified as **gap**
(a step that you could not reconstruct or that is false), **error** (a false
statement that does not break the proof, or a fixable one), **wording**, or
**citation**, with its location (section and statement number); (e) what you
did not check. A step you cannot reconstruct is a gap; do not report "looks
right" as a finding.
