# Conjectura

AI-driven mathematical discovery through computational experimentation,
autonomous research agents, symbolic reasoning, and formal verification.

**Status: research infrastructure with one investigation in progress. This
repository does not contain any solved conjecture or claimed new theorem.**
The `main` branch holds stable infrastructure and reviewed results; work in
progress is on the `research` branch.
The [`results/`](results/) directory is empty by design until a result has
passed the review process described below.

Project director: Gustavo Bernardo Brito, undergraduate student in Applied and
Computational Mathematics, Universidade Federal de Goiás (UFG), Brazil.

## Aim

Mathematical discovery, with reproducible evidence for every claim. Proving and
disproving published open conjectures is a central objective, and it is not the
only one: lemmas, theorems, identities, inequalities, bounds, counterexamples,
new conjectures, new proofs, methods, structural results and significant
computational findings are recorded as contributions in their own right,
whether or not the conjecture they came from is resolved. A conjecture is a
starting point; mathematical discovery is the objective. AI systems are
used as an active means of discovery — for literature work, conjecturing, proof
search, computation, formalization and review — and their participation is
documented alongside the human contribution
([attribution policy](docs/attribution-policy.md)). A second aim is the
director's own understanding of the mathematics involved
([learning guide](docs/learning-guide.md)).

## Principles

Correctness over apparent productivity; originality over counts of results;
reproducibility over persuasion; exact computation over approximation;
stated uncertainty over premature claims; independent verification over
self-confirmation; usefulness over administration; human understanding
alongside AI-driven discovery. No fabricated results, citations, logs,
receipts or novelty claims — see [`AGENTS.md`](AGENTS.md).

## What is here

| | |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Permanent rules for all research agents (authoritative). |
| [`autoresearch.md`](autoresearch.md) | The protocol for one bounded research session: free exploration, or focused work in twelve steps. |
| [`research/INDEX.md`](research/INDEX.md) | Generated view: the 15 catalogued problems, ranked, and the registered contributions. |
| [`research/catalogue.json`](research/catalogue.json) | The single authoritative record of problems (`CJ-XXXX`), statuses and scores. |
| [`research/discoveries.json`](research/discoveries.json) | The single authoritative record of mathematical contributions (`MD-XXXX`). An identifier establishes identity, not correctness or novelty. |
| [`research/summary.json`](research/summary.json) | Generated machine-readable summary of the project, with explicit nulls where nothing qualifies. Its block `public` is the interface for display elsewhere ([contract](docs/public-summary.md)). |
| `research/active/` | Working state of investigations in progress (on the `research` branch). |
| [`research/scouting-log.md`](research/scouting-log.md) | How candidates were found, what was set aside, and which conjectures were found to have reported resolutions. |
| `experiments/` | Reproducible exact computations (on the `research` branch). |
| [`formalization/`](formalization/) | Lean 4 + Mathlib project: calibration proofs and negative tests. |
| [`verification/`](verification/) | Machine-written verification receipts. |
| [`docs/`](docs/) | Methodology, research, verification, attribution, publication and learning policies. |
| `learning/` | Problem-driven learning guides (on the `research` branch). |

## Current research

The scoring model ([`research/priorities.json`](research/priorities.json)) is a
transparent weighted sum used to order a queue; it is not a probability of
success. The current shortlist:

1. **`CJ-0001` — Collins–Shor conjecture** on the location of the peak of the
   normalized coefficients of the distance characteristic polynomial of a tree
   (Collins 1989; stated as Conjecture 1.2 in arXiv:1507.02341). *Active on the
   `research` branch.* The state of the investigation — what has been verified,
   one refuted hypothesis, and the next step — is in
   `research/active/CJ-0001-collins-shor-peak/STATE.md` on that branch.
2. **`CJ-0002` — Chollet's permanent conjecture**, `per(A∘B) ≤ per(A) per(B)`
   for positive semidefinite matrices.
3. **`CJ-0007` — Ellis–Filmus–Friedgut spectral conjectures** on Kneser graphs
   of downsets (2026).

Every claim about a problem's status is qualified by its recorded evidence:
open-status evidence and novelty-search coverage are stored with dates and
limitations, and "no prior resolution found" always means "within the
documented search".

## How claims are classified

Four independent dimensions, never merged: **mathematical status**, **formal
verification status**, **novelty status**, **external review status**
([research policy](docs/research-policy.md)). A Lean proof establishes a formal
theorem under its actual dependencies; it does not by itself establish novelty
or agreement with the published statement. AI review is recorded as AI review
and is never presented as human or peer review.

## Verification

```sh
uv sync
uv run pytest -m "not lean"              # catalogue, tooling, computations
cd formalization && lake exe cache get && lake build && cd ..
uv run pytest                            # adds the Lean positive and negative tests
uv run python scripts/verify_lean.py     # build, source scan, transitive axiom audit,
                                         # statement registry, kernel replay; writes a receipt
```

The Lean pipeline permits only the axioms `propext`, `Classical.choice` and
`Quot.sound`, and is tested against deliberately deficient proofs (`sorry`,
custom axioms, `native_decide`, a false statement, a vacuous theorem, an unsafe
definition, a kernel bypass), each of which must be rejected by the intended
check ([verification policy](docs/verification-policy.md)). Pinned versions:
Lean 4.36.0, Mathlib v4.36.0, Python dependencies in `uv.lock`.

## Resuming research

With any capable coding agent, from the repository root:

> Read `AGENTS.md` and `autoresearch.md`. Run one research session on the active
> investigation with the highest priority, in the mode that suits what you
> find there. Stay within the default budget, verify what you claim, update
> `STATE.md` and the journal, and stop cleanly.

In Claude Code: `/research-session`.

## Acknowledgements

The workflow is informed by the public projects
[solved-conjectures](https://github.com/1337isnot1337/solved-conjectures),
[erdos-99](https://github.com/1337isnot1337/erdos-99),
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures) and
[Mathlib](https://github.com/leanprover-community/mathlib4); what was adopted
and what was changed is recorded in [`docs/methodology.md`](docs/methodology.md).
No text or code was copied from the first three, and their mathematical claims
are not relied upon. Problem sources include <https://www.erdosproblems.com/>
and <https://oeis.org/>.

## Licence and citation

Apache License 2.0 ([`LICENSE`](LICENSE)). Citation metadata:
[`CITATION.cff`](CITATION.cff).
