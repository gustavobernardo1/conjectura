# Autoresearch — the session protocol

This is the operational procedure for one bounded research session. It is
written so that a newly started agent with no conversation history can continue
the project's mathematics from the repository alone. Read
[`AGENTS.md`](AGENTS.md) first; its rules govern everything here.

A session aims at something durable and independently checkable: a lemma with
proof, an exact computation, a counterexample with an independent check, a new
conjecture with its evidence, a formalized statement, an audit, a refuted
approach, or a precise handoff. Resolving the conjecture an investigation
started from is not required, and a contribution does not need it to matter.
Ending with "no durable progress" is a legitimate, recorded outcome.

**Default budget:** one session of at most about 120 minutes of agent work, of
which approximately the last 20 minutes are reserved for verification,
documentation and persistence; computations capped at 30 minutes of wall-clock
time in total unless the director has approved a larger campaign in the
investigation's `STATE.md`. A limit set by the director or by the user who
started the session is binding in every mode.

**The time budget is a maximum, not a target.** A session that has reached its
objective, met a stopping condition, or has no idea left that justifies the
effort stops early and says so ([Stopping cleanly](#stopping-cleanly)). Time
that remains is not filled with work of low value, and the length of a session
is never a measure of its worth. How the time is spent — continue, redirect,
suspend — is the mathematical judgment of the agent running the session.

**Checkpoints.** A session leaves a light checkpoint about every 30 minutes, so
that an interruption, a compaction of the agent's context or a usage limit
costs at most that much work ([Checkpoints](#checkpoints)).

## Two modes

Say at the start of the session's record which mode it is. A session may
switch; record the switch.

- **Exploration** — for an idea that does not yet have an exact objective.
  Free, lightly recorded, bounded only by its budget and by the integrity
  rules. See [Exploration](#exploration).
- **Focused work** — for proving, refuting, computing or formalizing one exact
  statement. The twelve steps below are its default procedure.

Promoting a finding to an established result always goes through focused work
and the requirements of `AGENTS.md` sections 4 to 6, whatever mode found it.

## Exploration

Use it for an unusual angle on an active problem, a pattern noticed in data, a
connection to another area, a conjecture of your own, a new technique, a
question outside the catalogue, or a doubt about the project's own methods.

**Before.** Write the budget (time and computation), the time the session
starts, and one line saying what the session is curious about. Nothing else is
required in advance: no exact objective, no catalogue entry, no literature
review.

**During.** Follow the mathematics. Change direction, drop what is not
working, compute, guess, and try to break your own guesses. No independent
review and no formalization is required. Floating-point and heuristic output
is labelled exploratory, and nothing is reported as checked that was not.
[Checkpoints](#checkpoints) apply as in focused work: a few lines in the note,
about every 30 minutes.

**After.** Leave a dated note: model identifier, budget used, what was tried,
what was seen, what looks worth pursuing. It goes in the investigation's
`journal.md` when the exploration belongs to one, otherwise in
`research/explorations/<topic>.md`. A dead end takes two lines; it is recorded,
not hidden.

**When something is worth keeping:**

- A statement worth an identity — a lemma, an identity, a bound, a
  counterexample, a conjecture, a computational finding — gets a minimal record
  in `research/discoveries.json` with the status it honestly has
  ([research policy](docs/research-policy.md#mathematical-contributions)).
  Not every observation deserves one.
- A conjecture of the project that deserves a sustained attack becomes a
  catalogued problem that points to its registry record.
- A claim to be relied on or published goes through focused work and promotion.

## Focused work: the twelve steps

The steps are a default, not a ritual. Reorder them or drop one that does not
serve the objective, and say so in the journal. Three are never dropped for
anything that will be claimed: the budget (8), verification (10) and
persistence (11).

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
two entries of `journal.md`. If the last entry is still marked `in progress`,
the session that wrote it was interrupted: resume it as described under
[Checkpoints](#checkpoints) before choosing anything new. The sections *Open obligations* and *Next step* of
`STATE.md` say what is owed. Unfinished obligations (an unreviewed candidate
proof, an unverified computation, a stale receipt) come first by default. A
session may defer them for a more promising idea: record the deferral in the
journal. A claim that depends on an open obligation is not promoted until the
obligation is met.

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
problem" is not an objective for focused work; it is what exploration is for.

### 6. Verify eligibility and novelty of the target

The target is a statement that is open as far as the record shows: a catalogued
problem, a step toward one, or a statement formulated by the project (a
registered conjecture or a result suggested by exploration). Check the
catalogue and the registry for the same statement under another name. If the
exact statement turns out to be resolved, record the source, set the status to
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

Write the time budget, the time the session starts, the computational budget
(wall-clock limit, memory, the largest instance size to attempt) and, when
relevant, the model/token budget. Do not exceed it without recording why.

The time budget is a ceiling. Plan the work so that its last 20 minutes or so
are free for steps 10 to 12: the investigation stops when the working part of
the budget is spent, not when the whole of it is. Open the journal entry now,
marked `in progress`, with the fields written so far; the first
[checkpoint](#checkpoints) is due about 30 minutes later.

### 9. Investigate

Follow the discovery protocol in [`docs/methodology.md`](docs/methodology.md#discovery-protocol).
Keep exploratory floating-point work separate from exact certificates. Put
reusable code in `experiments/<id>-<slug>/` with a README giving inputs,
algorithm, command, seeds, dependency versions and expected output. Never alter
the mathematical statement to make a computation easier.

**Formalize progressively** (director's instruction, 2026-11-26). Lean is not
kept for the end of an investigation. When the statement of a lemma has
stabilised and it is within reach of Mathlib — an inequality, an identity, a
combinatorial lemma that several results use — state it in Lean and prove it
while the mathematics around it is still moving, within the session's budget.
A lemma formalized this way gives its record the formal status `partial`,
with the scope stated; it is registered in `formalization/registry.json` only
after its Lean statement has been compared with the written one, and it
changes nothing about the mathematical, novelty or review status of the
result that uses it.

### 10. Verify

- Re-derive each new lemma from its statement; check boundary cases explicitly.
- Re-run every computation that supports a claim from a clean command line and
  compare against an independent implementation where practical.
- For a counterexample: independent checker, all hypotheses, exact conclusion.
- For Lean: `uv run python scripts/verify_lean.py`.
- For tooling or catalogue changes: `uv run pytest`.
- For a candidate proof or counterexample of a catalogued statement, or a
  contribution that is to be promoted: request an independent adversarial
  review (see `AGENTS.md` section 6). Do not promote the status yourself in the
  session that produced the claim.

### 11. Persist

Update `STATE.md` (lemmas, failed approaches, observations, dependency map,
obligations), complete the journal entry and replace its mark `in progress` by
the outcome, register or update the contributions
that deserve an identity in `research/discoveries.json`, update the catalogue
status if it changed, regenerate the generated views, and commit:

```sh
uv run python scripts/catalogue.py validate && uv run python scripts/catalogue.py render
git add -A && git commit
```

Commit only when there is something durable. Record the model that did the work
in the journal entry and in the commit trailer.

`research/summary.json` names the commit it was generated from. Generated
before the commit, it says so (`sources_committed: false`); running `render`
once more after the commit binds it to that commit, and the rebound file is
committed on its own.

### 12. Document the next concrete step

The *Next step* section of `STATE.md` must name one specific action that a new
agent can start immediately, with the file or lemma it concerns.

## Checkpoints

A session can be cut off without warning: an interruption, a usage limit, a
compaction of the agent's context. About every 30 minutes of work, and before a
step that may not return (a long computation, a large delegation), leave a
checkpoint. The interval is approximate: finish the argument or the command in
hand first.

A checkpoint is a few lines, not a report, and takes a couple of minutes:

1. **In the journal.** The entry of the session is opened when the session
   starts, marked `in progress`. A checkpoint is appended under its heading
   *Checkpoints*: the time elapsed (from a clock reading where the environment
   gives one, otherwise an estimate labelled as an estimate); what has been
   established since the last checkpoint, each item with its level of
   evidence; what is unfinished and where it is (files, running commands,
   delegated work); and the immediate next action. Exploration outside an
   investigation writes the same lines in its note under
   `research/explorations/`.
2. **In `STATE.md`,** only if the current truth changed: a lemma established, an
   approach refuted, a different next step.
3. **In Git.** If files changed, commit them on `research` (or the session's
   branch) with a message that says it is a checkpoint. A checkpoint commit is
   a save point. It promotes nothing: no status changes at a checkpoint, and
   work recorded there as unfinished or unchecked stays so until step 10.
   Pushing follows the director's authorization, as for any commit.

A checkpoint does not replace steps 10 to 12, and it is not a reason to
continue: a session that should stop, stops at once and closes its entry.

**Resuming an interrupted session.** An entry still marked `in progress` was
not closed. Read `STATE.md` and that entry; check that what the last checkpoint
describes is there (`git status --short`, the files it names); then either
continue within what remains of the budget — the budget written in the entry
less the time recorded at the last checkpoint — or close the entry with the
outcome `interrupted` and what was lost. The same applies to an agent whose own
context was compacted in the middle of a session: the journal entry, not its
memory of the conversation, is the record. Earlier lines of the entry are not
rewritten; the continuation is appended.

## Stopping cleanly

Stop the session — and record why in the journal — when any of these holds: the
working part of the budget is spent (what remains is the reserve for
verification, documentation and persistence); the objective is reached; the
falsification test fails; a required tool or source is unavailable; no approach
with a new idea remains; or the mathematics no longer justifies the effort.
Stopping early is not failure and needs no justification beyond the reason
itself; leaving an inaccurate record is the failure.

## Journal entry format

Use `research/templates/journal-entry.md`. Telemetry fields that the
environment does not expose are written as `unavailable`, never estimated
silently.

## Resuming research

From a terminal in the repository, with any capable coding agent:

> Read `AGENTS.md` and `autoresearch.md`. Run one research session on the active
> investigation with the highest priority, in the mode that suits what you
> find there. Stay within the default budget, verify what you claim, update
> `STATE.md` and the journal, and stop cleanly.

In Claude Code the same procedure is available as the skill `/research-session`.
