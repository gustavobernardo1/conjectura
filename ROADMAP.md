# Roadmap

Dated intentions, not promises. Research direction follows what the
mathematics shows.

## Done (2026-11-26, initial version)

- Repository instructions, policies, role definitions, templates.
- Research catalogue with 15 candidate problems, a transparent ranking model
  and a shortlist of three.
- Lean 4.36.0 + Mathlib v4.36.0 project with two calibration proofs.
- Verification script (build, source scan, transitive axiom audit, statement
  registry, kernel replay, receipts) with seven negative tests.
- First investigation opened: `CJ-0001`, the Collins–Shor conjecture.

## Next (research)

1. `CJ-0001`: pursue the next step recorded in
   `research/active/CJ-0001-collins-shor-peak/STATE.md`.
2. `CJ-0001`: literature audit of the forward citations of arXiv:1507.02341 and
   arXiv:2206.07561, and of Collins (1989), before any result is claimed.
3. `CJ-0002` and `CJ-0007`: read the primary sources and bring the statements
   to `primary-source` status (required before either can become active).
4. First independent adversarial review, as soon as there is a candidate lemma
   with a complete written proof.

## Next (infrastructure, only when needed)

- Run the CI workflow for the first time after the repository is published
  (it has not been executed yet).
- A problem-specific Lean calibration for `CJ-0001` (distance matrix of a tree;
  Graham–Pollak for small cases) once a lemma is ready to formalize.
- SageMath or nauty for graph enumeration if an investigation needs them
  (neither is installed; WSL is not installed on the development machine).
- Zenodo integration and a first tagged release when there is a result to cite.

## Open decisions for the director

- Licence for mathematical text: the repository is Apache-2.0 throughout; a
  Creative Commons licence for expository text and manuscripts can be added.
- Whether to invite a human mathematician to review the first result before it
  is published.
- Compute budget for campaigns larger than the default session budget.

## Not planned

- A custom multi-agent orchestration framework.
- A website, result counters or leaderboards.
- Formalizing results that are already established, except as calibration or
  as learning material labelled as such.
