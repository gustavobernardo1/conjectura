# Contributing

Conjectura is a research repository. Contributions from people and from AI
agents follow the same rules, which are in [`AGENTS.md`](AGENTS.md); the
session procedure is in [`autoresearch.md`](autoresearch.md).

## Setup

Requirements: Git, [uv](https://docs.astral.sh/uv/), Python 3.12 or later, and
for formal work [elan](https://github.com/leanprover/elan) (which installs the
pinned Lean toolchain automatically).

```sh
uv sync                                   # Python environment from uv.lock
cd formalization && lake exe cache get    # prebuilt Mathlib (several GB)
lake build && cd ..
```

## Checks

```sh
uv run pytest -m "not lean"               # fast: catalogue, tooling, computations
uv run pytest                             # everything, including Lean negative tests (minutes)
uv run python scripts/catalogue.py validate
uv run python scripts/catalogue.py render --check
uv run python scripts/verify_lean.py      # full Lean verification; writes a receipt
```

Lean tests are skipped, with the reason printed, when the toolchain or the
Mathlib build is missing. A skipped test is not a passed test; say so when
reporting.

## What a contribution looks like

- **A new candidate problem:** a catalogue record and a dossier
  (`research/templates/candidate-dossier.md`), with every score justified and
  every unverified item listed.
- **Research on an active problem:** an update to its `STATE.md`, a journal
  entry, and whatever supports the update — a proof in a note, an experiment
  with its result file, a Lean module.
- **A mathematical contribution:** a record in `research/discoveries.json`
  pointing to the proof, computation or note that supports it, with the status
  it honestly has (`docs/research-policy.md`).
- **A review:** a report from `research/templates/review.md`, bound to a
  revision.
- **Infrastructure:** code with tests. A change to `scripts/verify_lean.py`,
  the audit template, the registry or any Lean source requires a new
  verification receipt.

Negative results are contributions: a refuted hypothesis, a failed approach
with the reason, a counterexample to an intermediate lemma.

## Conventions

- Work on `research` or a short-lived branch; `main` receives only reviewed,
  narrowly scoped changes.
- Commits made with AI assistance carry a `Co-Authored-By:` trailer naming the
  model. Journal entries name the model that did the work.
- State claims at the level of evidence they have
  (`docs/verification-policy.md`).
- Contribute only material you may license under Apache-2.0. Cite external
  papers; do not copy their text or include their PDFs.
- No credentials or private data.

## Reporting an error

An error in a statement, proof, computation or citation is the most valuable
report this repository can receive. Open an issue naming the file and the
exact step, with a counterexample or a reproducible failure where possible.
Corrections are credited to whoever found the error.
