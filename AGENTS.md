# Conjectura — permanent instructions for research agents

This file is the authoritative rule set for every AI agent working in this
repository, whatever the model or tool (Claude Code, Codex, or others). Other
instruction files (`CLAUDE.md`, `.claude/agents/*`, `.claude/skills/*`) refer to
this one and must not contradict it. If they do, this file wins and the
contradiction is a bug to fix.

Conjectura is a mathematical research project: its aim is to prove, disprove or
make rigorous partial progress on published open conjectures, and to leave
reproducible evidence for every claim. The project director is Gustavo Bernardo
Brito (UFG). The director decides what is published and what is contacted or
submitted outside the repository.

## 1. Integrity rules (never overridden)

1. **Never fabricate.** No invented results, citations, quotations, execution
   logs, verification receipts, literature coverage, telemetry or novelty
   claims. If something was not run, read or checked, say so.
2. **Report what happened.** A check that was not run, was skipped, timed out or
   failed is reported as exactly that. Only a check that ran and passed is a pass.
3. **Keep the statement fixed.** Work on the exact published statement. Never
   weaken, strengthen, re-quantify or re-domain a statement silently to make a
   proof or computation easier. A changed statement is a *different* statement,
   recorded as such with the difference spelled out.
4. **Finite evidence is not a universal proof.** A search that finds no
   counterexample up to a bound establishes the statement up to that bound and
   nothing more.
5. **A failed proof attempt is not evidence of falsity**, and a failed
   counterexample search is not evidence of truth beyond its exact coverage.
6. **Unknown novelty stays unknown.** An unsuccessful literature search never
   establishes originality. Record what was searched and what was not.
7. **Keep the four status dimensions separate** (section 4). A Lean proof
   establishes the formal theorem under its actual dependencies; it does not
   establish novelty, nor that the formal theorem matches the published one.
8. **Preserve negative results.** Failed approaches, counterexamples to
   intermediate lemmas, corrected statements and dead ends are recorded, not
   deleted.
9. **No outside action without authorization.** Do not push, publish, open
   issues or pull requests on other repositories, submit manuscripts, or contact
   researchers unless the director has explicitly authorized that specific
   action.
10. **No secrets or personal data** in commits, logs or outbound requests.
11. **Bounded work only.** Every session and every expensive computation has an
    explicit budget and stopping condition written down before it starts. No
    unbounded loops, no open-ended spending.

## 2. Repository map

| Path | Content |
| --- | --- |
| `autoresearch.md` | The operational session protocol. Start here for research work. |
| `research/catalogue.json` | The single authoritative record of every problem considered, with status and scores. |
| `research/priorities.json` | The scoring model and the current shortlist. |
| `research/INDEX.md` | Generated ranking view. Never edited by hand. |
| `research/candidates/` | One prose dossier per catalogued problem (literature, open-status evidence, approaches). |
| `research/active/<id>-<slug>/` | Working memory of an investigation: `STATE.md`, `journal.md`, `reviews/`, notes. |
| `research/archive/` | Closed investigations, moved here intact. |
| `research/templates/` | Templates for dossiers, state files, journal entries, reviews, result packages. |
| `experiments/<id>-<slug>/` | Reproducible computations for a problem. |
| `formalization/` | The Lean 4 + Mathlib project (`lake`), including calibration proofs and negative tests. |
| `verification/receipts/` | Machine-written verification receipts. Never edited by hand. |
| `results/` | Reviewed result packages only. Empty until a result passes review. |
| `learning/` | Problem-driven learning guides for the project director. |
| `manuscripts/` | LaTeX sources for write-ups. |
| `docs/` | Policies: methodology, research, verification, attribution, publication, learning. |
| `scripts/`, `tests/` | Tooling and its tests. |

Load only what the current objective needs. Do not read the whole repository
into context; `research/active/<id>-<slug>/STATE.md` is designed to be the one
file that restores an investigation.

## 3. How to work

Follow [`autoresearch.md`](autoresearch.md) for every research session. In
short: inspect the repository state, read the active investigation's
`STATE.md`, pick one exact objective, write down approach, falsification test,
stopping condition and budget, do the work, verify it, persist it, and record
the next concrete step. A session may end with "no durable progress" — record
that honestly in the journal and stop. Do not create commits, files or reports
merely to look productive.

Research roles are described in [`docs/methodology.md`](docs/methodology.md#research-roles).
One agent may play several roles in a session, with one exception: **the
adversarial reviewer of a claim must not be the context that produced it**
(section 6).

Do not repeat a failed approach unless a new hypothesis, tool, observation or
reformulation justifies it; name what changed in the journal.

## 4. Claim classification

Every problem carries four independent status fields in `research/catalogue.json`.

| Dimension | Allowed values |
| --- | --- |
| Mathematical | `candidate`, `active-investigation`, `partial-result`, `candidate-proof`, `candidate-counterexample`, `proved`, `disproved`, `previously-resolved`, `rejected`, `superseded` |
| Formal verification | `not-started`, `partial`, `failed`, `complete`, `not-applicable` |
| Novelty | `unknown`, `preliminary-search-completed`, `no-prior-resolution-found`, `prior-resolution-identified` |
| External review | `not-reviewed`, `ai-reviewed`, `human-reviewed`, `submitted`, `peer-reviewed` |

Transition requirements (enforced where possible by `scripts/catalogue.py validate`):

- `candidate-proof` / `candidate-counterexample`: a complete written argument or
  an explicit object exists in the working directory. It is still a *candidate*.
- `proved` / `disproved`: requires a self-contained written proof or a verified
  counterexample, an independent adversarial review of the exact revision
  (section 6), a documented novelty search, and a package under `results/`.
  `external_review` must be at least `ai-reviewed`, and the package must say
  plainly which kind of review it had. AI review is not human peer review.
- Formal `complete`: requires a passing receipt under `verification/receipts/`
  that covers a registered theorem for that problem, and a recorded review that
  the Lean statement matches the published statement.
- `no-prior-resolution-found` always means "within the documented search
  coverage". It is never shortened to "novel".
- `previously-resolved`: record the resolving source; stop work on that exact
  statement; do not re-prove or formalize it as a project result.

## 5. Verification rules

Details: [`docs/verification-policy.md`](docs/verification-policy.md).

- Run `uv run pytest` before committing changes to tooling, the catalogue or
  Lean sources. Run `uv run python scripts/catalogue.py validate` and
  `render --check` after any catalogue change.
- Lean: `uv run python scripts/verify_lean.py` builds the library, scans the
  sources, audits the transitive axioms of every project declaration, checks
  the theorem registry, replays the kernel check, and writes a receipt. The
  only permitted axioms are `propext`, `Classical.choice` and `Quot.sound`. No
  `sorry`, `admit`, project axioms, `native_decide`, `unsafe`, or disabled
  kernel checks in the verified library.
- Computations that support a claim use exact arithmetic (integers, rationals,
  algebraic numbers, or rigorous interval bounds). Floating-point output is
  exploratory only and is labelled as such.
- A counterexample is accepted only when a checker independent of the search
  code confirms (a) every hypothesis of the original statement and (b) the
  violation of its exact conclusion.
- Say "verified" only with the command that was run, its result, and the
  revision it ran on.

## 6. Independent review

A claim is reviewed by a **fresh context** that receives the primary source and
the claimed proof, not the author's reasoning trail, and that tries to break
it. Where possible use a different capable model. The review report
(`research/templates/review.md`) records the exact Git revision and file hashes
reviewed, the reviewer's model, how independence was obtained, and an explicit
assessment of hypotheses, quantifiers, definitions, boundary cases, each lemma,
each implication, dependencies, counterexample attempts, formalization scope,
novelty coverage and remaining gaps.

- A review applies to one revision. Any material change to the statement or
  proof invalidates it until rechecked.
- Role-play of several "reviewers" inside one reasoning context is not
  independent review and must not be described as such.
- A reviewer who cannot reconstruct a step reports a gap. "Looks right" is not
  a review finding.

## 7. Research memory

All durable knowledge lives in the repository, not in conversation history.

- `STATE.md` (per investigation) is the current truth: exact statement,
  definitions, established lemmas with their verification level, failed
  approaches, counterexamples and observations, dependency map, decisions,
  open obligations, next step. Keep it current and compact (aim for under 400
  lines; move detail to notes and link it).
- `journal.md` is append-only: one entry per session with date, agent model,
  objective, budget, what was run, what was found, and telemetry where it is
  actually available (write `unavailable` otherwise).
- Before ending a session, make sure a newly started agent could continue from
  `STATE.md` alone.

## 8. Attribution

Record who did what: human direction, human mathematics, AI-generated
strategies and discoveries, computation, formalization, review, and external
results that were used. Record exact model names when known. Do not inflate
human contribution or hide AI participation; operating an AI model is not by
itself scientific authorship. See [`docs/attribution-policy.md`](docs/attribution-policy.md).

## 9. Git

- `main`: stable infrastructure and reviewed results. `research`: ongoing
  investigations. Short-lived branches for isolated tasks and reviews.
- Never merge `research` into `main` wholesale; promote narrowly scoped,
  reviewed changes.
- Never force-push, rewrite published history, or overwrite a remote.
- Commit when there is a durable artifact. Commits made with AI assistance carry
  a `Co-Authored-By:` trailer naming the model.
- Publication steps are in [`docs/publication-policy.md`](docs/publication-policy.md).

## 10. Style

Public text is professional academic English: direct, precise, and free of
promotional language. State theorems with all hypotheses and quantifiers.
Distinguish clearly between calibration examples, educational examples and
research results.
