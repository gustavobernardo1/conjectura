# Autoresearch — the session protocol

This is the operational procedure for one bounded research session. It is
written so that a newly started agent with no conversation history can continue
the project's mathematics from the repository alone. Read
[`AGENTS.md`](AGENTS.md) first; its rules govern everything here.

A session's goal is one durable, independently checkable contribution: a lemma
with proof, an exact computation, a counterexample with an independent check, a
formalized statement, an audit, a refuted approach, or a precise handoff. A
complete proof is not required. Ending with "no durable progress" is a
legitimate, recorded outcome.

**Default budget:** one session of about 60 minutes of agent work, of which the
last quarter is reserved for verification and persistence; computations capped
at 30 minutes of wall-clock time in total unless the director has approved a
larger campaign in the investigation's `STATE.md`.

## The twelve steps

### 1. Inspect the repository state

```sh
git status --short && git branch --show-current && git log --oneline -5
uv run python scripts/catalogue.py validate
uv run python scripts/catalogue.py rank
```

Work on `research` or a short-lived branch created from it, never directly on
`main`. If the tree has uncommitted changes you did not make, do not discard
them; find out what they are.

### 2. Read the applicable instructions

`AGENTS.md`, this file, and — only as needed — the policy in `docs/` that
governs what you are about to do (verification, attribution, publication).

### 3. Inspect active investigations and unresolved obligations

```sh
ls research/active/
```

For the investigation you will work on, read `STATE.md` in full, then the last
two entries of `journal.md`. The sections *Open obligations* and *Next step* of
`STATE.md` say what is owed. Unfinished obligations (an unreviewed candidate
proof, an unverified computation, a stale receipt) take precedence over new
exploration.

### 4. Refresh sources and check existing work

Re-open the primary source of the statement if its exact wording matters for
today's objective. Search for work that appeared since the dossier's
`novelty_search.as_of` date when that date is more than 30 days old or when you
are about to claim a result. Record new findings in the dossier
(`research/candidates/`) and update the dates in the catalogue. If web access
is unavailable, say so in the journal and do not update the dates.

### 5. Select one exact objective

Write it in the journal entry before starting: the precise statement to prove,
refute, compute or formalize, with all hypotheses and quantifiers. "Explore the
problem" is not an objective.

### 6. Verify eligibility and novelty of the target

The target must be an open, published statement or a step toward one. Check the
catalogue for the same statement under another name. If the exact statement
turns out to be resolved, record the source, set the status to
`previously-resolved`, and stop working on it.

### 7. Define approach, falsification strategy and stopping conditions

In the journal entry, before the work:

- **Approach:** the method and why it might succeed where recorded attempts did not.
- **Falsification:** the cheapest test that would show the objective is false or
  the approach is hopeless — run that first.
- **Stopping conditions:** what counts as done, and what counts as "stop, this is
  not working".

If the approach repeats one listed under *Failed approaches* in `STATE.md`,
state what is different this time, or choose another.

### 8. Establish the budget

Write the time budget, the computational budget (wall-clock limit, memory, the
largest instance size to attempt) and, when relevant, the model/token budget.
Do not exceed it without recording why.

### 9. Investigate

Follow the discovery protocol in [`docs/methodology.md`](docs/methodology.md#discovery-protocol).
Keep exploratory floating-point work separate from exact certificates. Put
reusable code in `experiments/<id>-<slug>/` with a README giving inputs,
algorithm, command, seeds, dependency versions and expected output. Never alter
the mathematical statement to make a computation easier.

### 10. Verify

- Re-derive each new lemma from its statement; check boundary cases explicitly.
- Re-run every computation that supports a claim from a clean command line and
  compare against an independent implementation where practical.
- For a counterexample: independent checker, all hypotheses, exact conclusion.
- For Lean: `uv run python scripts/verify_lean.py`.
- For tooling or catalogue changes: `uv run pytest`.
- For a candidate proof or counterexample of a catalogued statement: request an
  independent adversarial review (see `AGENTS.md` section 6). Do not promote the
  status yourself in the session that produced the claim.

### 11. Persist

Update `STATE.md` (lemmas, failed approaches, observations, dependency map,
obligations), append the journal entry, update the catalogue status if it
changed, regenerate the index, and commit:

```sh
uv run python scripts/catalogue.py validate && uv run python scripts/catalogue.py render
git add -A && git commit
```

Commit only when there is something durable. Record the model that did the work
in the journal entry and in the commit trailer.

### 12. Document the next concrete step

The *Next step* section of `STATE.md` must name one specific action that a new
agent can start immediately, with the file or lemma it concerns.

## Stopping cleanly

Stop the session — and record why in the journal — when any of these holds: the
budget is spent; the falsification test fails; a required tool or source is
unavailable; no approach with a new idea remains; or the mathematics no longer
justifies the effort. Stopping is not failure; leaving an inaccurate record is.

## Journal entry format

Use `research/templates/journal-entry.md`. Telemetry fields that the
environment does not expose are written as `unavailable`, never estimated
silently.

## Resuming research

From a terminal in the repository, with any capable coding agent:

> Read `AGENTS.md` and `autoresearch.md`. Run one research session on the active
> investigation with the highest priority, following the twelve steps. Stay
> within the default budget, verify what you claim, update `STATE.md` and the
> journal, and stop cleanly.

In Claude Code the same procedure is available as the skill `/research-session`.
