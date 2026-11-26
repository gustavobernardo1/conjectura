# Methodology

This document records how Conjectura works and why it is built this way: the
reference projects that were studied, the architectural decisions taken, the
research roles, the discovery protocol, the standards for computation, and the
prioritization model. The binding rules are in [`AGENTS.md`](../AGENTS.md);
this document explains them.

## Reference audit

The following public projects were examined on 2026-11-26 by reading their
repository contents at the commits listed, not only their READMEs.

| Project | URL | Commit read | Licence |
| --- | --- | --- | --- |
| solved-conjectures | <https://github.com/1337isnot1337/solved-conjectures> | `da3b848c55e3d5bdb8e9864b6b9ac369b6269e20` (2026-11-25) | MIT |
| erdos-99 | <https://github.com/1337isnot1337/erdos-99> | `e5ca7c87d9d48bb0ccc9a7ff820f5ce2fefc6902` (2026-11-22) | Apache-2.0 |
| formal-conjectures | <https://github.com/google-deepmind/formal-conjectures> | `9097e2f90e66d2f6244209cb1c07f7120d17ec53` (2026-11-24) | Apache-2.0 |
| mathlib4 | <https://github.com/leanprover-community/mathlib4> | tag `v4.36.0` (`fc4f59e577feb1a4956671bc04ac18aaaf8cd842`) | Apache-2.0 |

Files read in the first two projects: `AGENTS.md`, `autoresearch.md`,
`auto-research.md`, `docs/REVIEW_POLICY.md` (erdos-99); `AGENTS.md`,
`docs/verification.md`, `docs/lean-status.md` (opening sections),
`scripts/verify_lean.sh`, `lean/ProofAudit.lean`, and the directory layout
(solved-conjectures). Their mathematical claims were **not** examined and are
not endorsed or relied upon here. <https://www.erdosproblems.com/> and
<https://oeis.org/> were consulted as problem sources by the literature scouts
(erdosproblems.com returned HTTP 403 to automated fetches on that date).

No text or code was copied from these projects. The practices below are
adopted as ideas, with credit.

### Practices adopted

- **A session protocol that survives loss of context** (erdos-99
  `autoresearch.md`): one bounded session, an exact objective with
  falsification test and stopping condition written before the work, the final
  part of the session reserved for verification, "a PR is not a quota".
- **Separation of working and published branches** (solved-conjectures
  `AGENTS.md`): `main` for reviewed material, `research` for work in progress,
  no wholesale merges.
- **An eligibility gate before any work** (solved-conjectures): check that the
  exact statement is open, under alternative names and as a consequence of
  known theorems, and record what was searched.
- **Transitive axiom audit and kernel replay** (solved-conjectures
  `ProofAudit.lean`, `verify_lean.sh`): only `propext`, `Classical.choice`,
  `Quot.sound`; no `sorry`; no `native_decide`; replay the compiled modules with
  an independent checker.
- **"Not run" is never "passed"** (both projects): deferred or skipped checks
  are reported as such.
- **Review bound to an exact revision** (erdos-99 `REVIEW_POLICY.md`).
- **Machine-readable statements of open problems with status tags**
  (formal-conjectures): used as a source of candidate problems and as a
  cross-check of open status.

### Weaknesses observed, and what Conjectura does instead

| Observation in the reference projects | Decision here |
| --- | --- |
| Review is performed exclusively by AI agents, and the policy states that no human mathematical review is required (erdos-99 `REVIEW_POLICY.md`). | External review is a separate status dimension with distinct values for AI and human review. AI review can never be reported as human or peer review, and `proved`/`disproved` always states which review it had. |
| A standing instruction assumes an external, unverified result as a premise for all research (solved-conjectures `AGENTS.md`, "Standing research assumption"). | No result is assumed by policy. A result that depends on an unverified claim is recorded as conditional, with the dependency named. |
| Very large instruction and status files (verification and Lean-status documents above 100 KiB, a 270 KiB history file), and more than 200 one-off scripts. | One authoritative JSON catalogue with generated views; one compact `STATE.md` per investigation; two infrastructure scripts. |
| Hand-maintained lists of modules and theorem names inside the verification script and the audit file. | The audit enumerates every declaration owned by the project automatically; a small registry lists only the theorems that back claims. |
| Substantial rules about README layout, ranking tables and website synchronization. | None. Administrative structure is added only when a result needs it. |
| Counts of "solved conjectures" as a headline. | No counts. A repository with zero results is an acceptable state and is described as such. |
| Novelty and open status are asserted in prose. | Open-status evidence and novelty-search coverage are separate structured fields with dates and stated limitations. |
| Formal statements are trusted to match the published conjectures. | Each registered theorem carries a statement fingerprint that is set only after comparison with the source and invalidated by any change, and a non-vacuity witness. |

## Architectural decisions

1. **Single source of truth.** `research/catalogue.json` holds every structured
   fact about a problem. Prose that does not fit a structured field lives in
   one dossier per problem. No fact is stored in both places. `research/INDEX.md`
   is generated.
2. **Deviations from the proposed directory layout.** `benchmarks/` is not
   created: calibration material lives with the tool it calibrates
   (`formalization/Conjectura/Calibration/`, `formalization/NegativeTests/`,
   `tests/`). `research/archive/` is created when the first investigation is
   archived. A `research/templates/` directory and a `research/schema/`
   directory were added.
3. **Native tooling only.** Roles are Claude Code subagents and skills plus
   model-independent Markdown instructions. There is no orchestration
   framework and no background service.
4. **Verification decisions in one place.** The Lean audit prints facts
   (declarations, axioms, statements); the Python script applies the policy.
   Changing the policy means changing one file, and the receipt records its hash.
5. **Receipts are hashes plus commands.** A receipt lists the SHA-256 of every
   verified input (line endings normalised), the toolchain, the Git commit and
   whether the tree was clean, each command with its exit status, and the
   result of each check. A test fails when the inputs no longer match the
   latest passing receipt.
6. **Python with `uv`, Lean with `lake`.** Both environments are pinned
   (`uv.lock`, `lean-toolchain`, `lake-manifest.json`).
7. **Licence.** Apache-2.0, matching Mathlib and formal-conjectures so that
   Lean code can be exchanged with them.

## Research roles

| Role | Responsibility | Implementation |
| --- | --- | --- |
| Research Director | Chooses objectives, sets budgets, keeps priorities, judges progress. | The main agent session, following `autoresearch.md` (skill `research-session`), under the human director. |
| Problem Scout | Finds published open problems and drafts candidate records. | `.claude/agents/problem-scout.md` |
| Literature Auditor | Verifies sources, statements, prior resolutions and prior formalizations. | `.claude/agents/literature-auditor.md` |
| Mathematical Researcher | Proof strategies, lemmas, reformulations. | `.claude/agents/mathematical-researcher.md` |
| Computational Experimenter | Exact experiments and counterexample searches. | `.claude/agents/computational-experimenter.md` |
| Formalization Agent | Lean 4 statements and proofs, registry, receipts. | `.claude/agents/formalization-agent.md` |
| Adversarial Reviewer | Tries to break a claim, from the source, in a fresh context. | `.claude/agents/adversarial-reviewer.md` (skill `review-claim`) |
| Publication Agent | Assembles reviewed result packages. | `.claude/agents/publication-agent.md` |

Agents that are not Claude Code read the same role descriptions as plain
Markdown. A single agent may combine roles, except that a claim is never
reviewed by the context that produced it.

## Discovery protocol

For every active problem, in roughly this order, returning to earlier steps as
needed:

- **A. Exact statement.** Establish the original statement from the primary source.
- **B. Anatomy.** List definitions, quantifiers, domains, boundary cases and
  hidden assumptions.
- **C. Equivalent formulations.** Look for restatements that expose structure.
- **D. Known theorems.** Check whether the statement already follows from
  published results.
- **E. Small experiments.** Compute small cases exactly.
- **F. Counterexample search.** Search systematically, and try to break every
  sharper hypothesis that the experiments suggest.
- **G. Structure.** Identify recurring extremal objects, invariants and patterns.
- **H. Strategies.** Develop more than one line of proof.
- **I. Lemmas.** Decompose a promising approach into independently verifiable lemmas.
- **J. Dependency map.** Keep a map of which results the argument rests on.
- **K. Symbolic and formal proofs.** Attempt them for the lemmas that are ready.
- **L. Adversarial review.** Independent review of anything to be claimed.
- **M. Obstacles.** Record exactly what remains unproved and why.

A failed strategy is recorded and is not retried unless a new hypothesis, tool,
observation or reformulation justifies it. A sequence of small verified steps is
preferred to a long unstructured reasoning session.

## Computational experimentation

- Python is the default language. External tools are introduced when an
  experiment needs them: SymPy (symbolic algebra), NetworkX (graphs), SageMath
  (advanced computation), Z3 and SAT solvers (finite combinatorial search),
  integer programming (discrete optimisation), exact rational or integer
  arithmetic, interval arithmetic when rigorous real bounds are needed.
  Currently in use: `networkx` (tree enumeration) and `python-flint` (exact
  integer characteristic polynomials).
- Each experiment documents its inputs, algorithm, outputs, seeds, dependency
  versions and command line, and stores its result in a small machine-readable
  file.
- Exploratory floating-point computation is kept apart from exact certificates
  and is labelled.
- Code is validated against cases with known answers before its output is
  trusted, and where practical against an independent implementation.
- A counterexample is checked for (1) every hypothesis of the original
  statement and (2) violation of its exact conclusion, by a checker that does
  not share code with the search.
- The mathematical statement is never altered to make a computation easier.

## Prioritization model

`research/priorities.json` defines twelve criteria, each scored 0–4 with a
written justification, and integer weights. The score of a problem is the
weighted sum scaled to 0–100. Two gates apply before ranking: a problem needs at
least 2 on `open_evidence` and on `statement_precision` to be eligible.

The model is deliberately simple and explainable. Its output orders a queue; it
is not a probability of success, and differences of a few points are not
meaningful. The shortlist is a recorded decision that cites the ranking and may
depart from it with a stated reason (`priority_override`). More refined
multi-criteria methods can replace the weighted sum once the project has data on
how its own scores related to outcomes.
