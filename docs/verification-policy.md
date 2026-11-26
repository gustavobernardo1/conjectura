# Verification policy

A claim in this repository is only as strong as the check that was actually run
on it. This document defines the checks, what each one establishes, and what it
does not.

## Levels of evidence

| Level | Meaning | Example wording |
| --- | --- | --- |
| Conjectured | Suggested by reasoning or data. | "We conjecture …" |
| Verified computationally | Exact computation over a stated finite range. | "Holds for all trees of order at most 23 (exact integer arithmetic)." |
| Sampled | Exact computation on a stated random sample with a recorded seed. | "No violation among 10,000 sampled trees (seed …)." |
| Proved (written) | A complete written proof exists; review status stated separately. | "Proved in `notes/…`; not yet reviewed." |
| Formally verified | A Lean theorem with a passing receipt; correspondence with the published statement reviewed separately. | "Lean theorem `…`, receipt `…`." |

Floating-point computation never supports a claim above "conjectured".

## Lean 4 and Mathlib

- Toolchain: pinned in `formalization/lean-toolchain`; Mathlib pinned by tag in
  `formalization/lakefile.toml` and by commit in `lake-manifest.json`. Build
  system: Lake. Changing either pin is a deliberate, separately committed change.
- Calibration proofs (`Conjectura/Calibration/`) are known results used to test
  the pipeline. Research statements live under `Conjectura/Research/`. The
  registry check rejects a theorem registered under the wrong kind.

### Axiom policy

Permitted: `propext`, `Classical.choice`, `Quot.sound` — the standard axioms of
Lean 4 on which Mathlib is built. Everything else is rejected, in particular
`sorryAx`, any axiom declared by the project, and the axioms introduced by
`native_decide` and other compiler-trusting tactics. The policy lives in
`ALLOWED_AXIOMS` in `scripts/verify_lean.py`.

### What `scripts/verify_lean.py` checks

| Required detection | Mechanism | Automated? |
| --- | --- | --- |
| `sorry`, `admit` | Source scan; `sorryAx` in the transitive axiom audit. | Yes |
| Unjustified custom axioms | Axiom audit of every project-owned declaration; project-declared axioms rejected outright. | Yes |
| Untrusted or unsafe mechanisms | Rejects `native_decide`, `unsafe`, `implemented_by`, `extern`, `debug.skipKernelTC`, opaque and partial declarations. | Yes |
| Incomplete theorem dependencies | The audit follows dependencies transitively, through Mathlib; the kernel replay re-checks every declaration of the project modules. | Yes |
| Circular reasoning | Impossible inside the kernel; replay guarantees the environment was built by the kernel. Circularity between a *written* proof and a cited source is a review item. | Kernel: yes. Written: review |
| Vacuous implications | Every registered theorem needs a non-vacuity witness theorem, or a stated reason why none is needed. | Presence: yes. Adequacy: review |
| Hidden assumptions | The receipt records the fully elaborated statement of each registered theorem (all hypotheses and instance arguments visible). | Recorded: yes. Judgement: review |
| Incorrect domains, incorrect quantifiers | Statement review against the source before the fingerprint is set. | Review |
| Mismatch between published conjecture and formal theorem | Statement fingerprint: set only after comparison with the source; any change to the statement fails verification until re-reviewed. | Change detection: yes. Comparison: review |

The script prints each check as `passed`, `failed` or `not-run`. The verdict is
`passed` only if every check ran and passed. A skipped check makes the verdict
`failed`.

The kernel replay uses `leanchecker`, shipped with the pinned toolchain, on each
project module. The negative test `NegativeTests/KernelBypass.lean` shows why
it is needed: a false theorem inserted with kernel checking disabled depends on
no axioms and passes the axiom audit, and is rejected only by the replay.

### What a passing verification does and does not establish

It establishes that the registered Lean theorems are accepted by the Lean
kernel under the pinned toolchain and Mathlib, using only the permitted axioms.

It does not establish that a Lean statement says what the published conjecture
says (that is the statement review), that the result is new (novelty status),
or that anyone other than the project has checked it (external review status).
It also trusts the Lean kernel, the toolchain binaries and the hardware.

### Receipts

`verification/receipts/<UTC time>-<commit>[-dirty]-<verdict>.json` records: the
Git commit and whether the working tree was clean; toolchain and Mathlib
revisions; the SHA-256 (line endings normalised to LF) of every verified input,
including the registry, the audit template and the verification script itself;
every command with exit status and duration; each check with details; the
registered theorems with their elaborated statements, fingerprints and axioms.

- A receipt from a dirty tree is not evidence for the recorded commit.
- Receipts are written by the script and never edited.
- `tests/test_lean_scan.py` fails when the verified inputs differ from the
  latest passing receipt. After any change to them, rerun the verification and
  commit the new receipt.

### Negative tests

`formalization/NegativeTests/` contains deliberately deficient modules — a
`sorry` proof, a custom axiom, `native_decide`, a false statement, a vacuous
theorem, an unsafe definition, a kernel bypass. `tests/test_lean_verification.py`
asserts that each is rejected by the intended check. A verification pipeline
that has never been seen to fail is not trusted.

## Computational evidence

- Exact arithmetic for anything that supports a claim.
- The code is validated on known cases and, where practical, against an
  independent implementation that shares no code (for example
  `experiments/CJ-0001-collins-shor-peak/independent_check.py` on the
  `research` branch).
- The result file states the exact range covered, the counts, the versions and
  the command. Enumeration counts are compared with independent reference
  values (for example OEIS).
- A counterexample is accepted only after an independent checker confirms all
  hypotheses of the original statement and the violation of its exact
  conclusion.

## Independent adversarial review

Review is stronger than asking another model whether a proof looks correct.

1. **Fresh context.** The reviewer has not seen the author's reasoning. It
   receives the primary source, the claimed statement and proof, and the
   checklist. Where possible it is a different capable model.
2. **Source first.** The reviewer reads the primary statement and writes down
   hypotheses, quantifiers and definitions before reading the proof.
3. **Reconstruction.** The reviewer reconstructs the essential argument and
   tests each lemma on boundary cases, rather than checking plausibility.
4. **Explicit findings** on: hypotheses; quantifiers; definitions; boundary
   cases; each intermediate lemma; each logical implication; dependency
   assumptions; counterexample attempts; formalization scope; novelty coverage;
   unresolved gaps.
5. **Bound to a revision.** The report names the Git commit and the hashes of
   the files reviewed. A material change to the proof or statement invalidates
   the review until it is repeated.
6. **Honest labelling.** Several personas inside one reasoning context are not
   independent reviewers. An AI review is recorded as `ai-reviewed`, with the
   model named; it is never described as human or peer review.

Template: `research/templates/review.md`. Procedure for Claude Code: skill
`review-claim`.
