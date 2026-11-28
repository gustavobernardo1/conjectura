# CJ-0024 — exact checks of the drastic-boundary examples

**Input.** None. The script tests Theorems A and B of
`research/active/CJ-0024-sn-r-nonborder-intersection/notes/weber-uniqueness.md`
for c in {6/5, 3/2, 7/4, 101/100, 199/100}.

**Algorithm.** Exact `fractions.Fraction` arithmetic on the grid
{k/40 : 0 <= k <= 40} plus the points c-1, (c-1)/2, c/2, 2-c, 1-10^-6.
Checks: t-norm / t-conorm / negation / fuzzy-implication axioms on the grid
(associativity on all triples); the residual sup{t : T(x,t) <= y} bracketed by
60 steps of exact bisection on the sublevel set (independent of the closed
form) and compared with the closed form; the (S,N) and QL identities
pointwise; failure of (OP) at (c-1, 0); difference from the Weber implication;
the jump of T(x, .) at 1.

**Status of the evidence.** A finite grid check, exact at each grid point. It
supports, but does not prove, identities on [0,1]; the proofs are in the note.

**Command.** `uv run python check_examples.py` (from this directory).

**Dependencies.** Python >= 3.12 standard library only.

**Expected output.** One line per c ending in `all checks passed`, then
`residual/(S,N)/QL identities checked at 19048 grid pairs` and
`ALL CHECKS PASSED`. Run time about 50 s on a desktop (2026-11-27).
