# Research policy

## Principles

1. Mathematical correctness over apparent productivity.
2. Originality over the number of claimed discoveries.
3. Reproducibility over persuasive explanation.
4. Exact computation over approximate evidence whenever practical.
5. Transparent uncertainty over premature claims.
6. Independent verification over self-confirmation.
7. Scientific usefulness over administrative complexity.
8. Human understanding alongside AI-driven discovery.

The project never fabricates results, citations, execution logs, verification
receipts, literature coverage or novelty claims. Negative results — failed
approaches, counterexamples, corrected conjectures, refuted hypotheses — are
kept, together with useful intermediate lemmas.

Two inferences are forbidden everywhere in the repository:

- from "we could not prove it" to "it is probably false";
- from "it holds in every case we computed" to "it is proved".

## Scope of the research

Resolving published open conjectures is a central objective. It is not the
only one. Lemmas, theorems, propositions, corollaries, identities,
inequalities, improved bounds, counterexamples, newly formulated conjectures,
new proofs, methods, structural results and significant computational findings
are contributions in their own right. An investigation that does not resolve
its conjecture may still produce them, and they are recorded, reviewed and
published on their own merits ([Mathematical contributions](#mathematical-contributions)).

Exploration is unrestricted in subject: it may leave the catalogue, follow a
connection to another area, or start from a question of the agent's own
(`AGENTS.md` section 3). What is restricted is what may be *claimed*.

## Eligible problems

A problem enters the catalogue when it is a precisely stated statement for
which there is positive, dated evidence that it is open, and for which a
search for resolutions has been recorded. Two origins are eligible:

- a published statement (paper, preprint, problem list, OEIS entry, formal
  problem repository);
- a conjecture formulated by the project, already registered as a contribution
  of type `conjecture`. Its catalogue record names that contribution in the
  field `discovery`, gives the project as its source, and records under
  `open_status` and `novelty_search` the search made for the statement in the
  literature. A statement of the project is not known to be new merely because
  the project formulated it.

Partial progress toward such a statement — special cases, sharper hypotheses,
corrected statements — is eligible work.

Re-proving or formalizing a result that is already established is not a
research result of this project. It may be done as *calibration* (to test
tools) or as *learning* (for the director), and is labelled accordingly.

## Sources and priority fields

Sources: published papers, arXiv, <https://www.erdosproblems.com/>,
<https://oeis.org/>, MathOverflow, google-deepmind/formal-conjectures, surveys,
journals, public research databases.

Priority fields: graph theory, combinatorics, matrix analysis, linear algebra,
mathematical inequalities, discrete optimisation, numerical analysis,
elementary number theory. Other fields are welcome when a problem is unusually
promising.

## Candidate records

Every catalogued problem has, between its JSON record and its dossier:

| Requirement | Where |
| --- | --- |
| Stable internal identifier | `id` (`CJ-0001`, never reused) |
| Original conjecture name, original authors | `name`, `authors` |
| Primary source and statement number, publication date | `source` |
| Exact mathematical statement | `statement` |
| Mathematical field | `fields` |
| Definitions and hypotheses | dossier |
| Known partial results, relevant literature | dossier |
| Evidence of current open status | `open_status` and dossier |
| Novelty search coverage and limitations | `novelty_search` and dossier |
| Potential computational and mathematical approaches | dossier |
| Formalization feasibility, prerequisite knowledge | dossier |
| Research priority | computed from `scores` by `scripts/catalogue.py rank` |
| Current status | `status` (four dimensions) |

`source.statement_checked_against` records honestly whether the statement was
compared with the primary source, a secondary source, or nothing. A problem
cannot leave the `candidate` status until its statement has been checked
against a source.

## Status dimensions

The four dimensions and their values are listed in `AGENTS.md` section 4 and
enforced by `research/schema/catalogue.schema.json`, for problems and for
contributions alike. Their meanings for a problem:

**Mathematical.** `candidate`: catalogued, not started. `active-investigation`:
has a working directory. `partial-result`: something precise and verified has
been established short of the full statement. `candidate-proof` /
`candidate-counterexample`: a complete argument or object exists and awaits
review. `proved` / `disproved`: reviewed and packaged under `results/`.
`previously-resolved`: a prior resolution was found. `rejected`: not a suitable
target (ill-posed, trivial, out of scope). `superseded`: replaced by another
catalogue entry.

**Formal verification.** `not-started`, `partial` (some statements or lemmas
verified; scope stated), `failed` (attempt abandoned, reason recorded),
`complete` (a passing receipt covers a registered theorem whose statement was
reviewed against the source), `not-applicable`.

**Novelty.** `unknown`; `preliminary-search-completed` (a bounded search was
done and recorded); `no-prior-resolution-found` (a thorough search was done,
with its coverage documented — never abbreviated to "novel");
`prior-resolution-identified`.

**External review.** `not-reviewed`; `ai-reviewed` (an independent adversarial
AI review of the exact revision, see the verification policy); `human-reviewed`
(a named mathematician read the proof); `submitted`; `peer-reviewed`.

## Mathematical contributions

`research/discoveries.json` is the registry of contributions. It is separate
from the catalogue of problems and connected to it by references.

**Identifiers.** `CJ-XXXX` names a research problem; `MD-XXXX` names a
mathematical contribution. Both are permanent, never reused and independent of
category: the `type` of a contribution is a separate field
(`lemma`, `theorem`, `proposition`, `corollary`, `identity`, `inequality`,
`bound`, `counterexample`, `conjecture`, `proof`, `method`,
`structural-result`, `computational-finding`). An identifier establishes
identity. It does not establish correctness, novelty or verification.

**What is registered.** A finding that is worth referring to on its own: it
has a precise statement and would matter to someone who does not care about
the investigation it came from. Not every observation qualifies. Routine
consequences, restatements of the problem, and results taken from the
literature are not registered: the first two stay in `STATE.md` under their
local identifiers, the last are cited. Local identifiers (E1, L3, A(ii), …) are
never renumbered; a registry record names the local identifier it corresponds
to.

**Minimal record.** Identifier, type, title, exact statement, registration
date, provenance (who contributed what, with exact model identifiers, and the
journal or note where it arose), the evidence that exists, and the four status
fields. Nothing else is required of an exploratory record. Limitations,
dependencies, relations, the novelty search, the review, the receipt, the
result package and the manuscript are added when they exist.

**No duplication.** Proofs, computations, reviews and receipts stay where they
are; the record points to them (`evidence[].path`, `formal_receipt`, `result`).
The registry holds the statement and the metadata, nothing else.

**Status.** The four dimensions below apply unchanged. For a contribution the
mathematical dimension describes the record's own statement:

| Value | Meaning for a contribution |
| --- | --- |
| `candidate` | Stated; no complete argument. Open conjectures and observed patterns stay here. |
| `partial-result` | Part of the statement is established; the record says which. |
| `candidate-proof` | A complete written argument, or an exact computation covering the whole statement, exists. Not promoted. |
| `candidate-counterexample` | An explicit object refuting the statement exists. Not promoted. |
| `proved`, `disproved` | Promoted: independent review of the exact revision, documented novelty search, result package. |
| `previously-resolved` | Found in the literature after it was derived here; the source is recorded. |
| `rejected`, `superseded` | Withdrawn, or replaced by the record that `supersedes` it. The record is kept. |

A record of type `counterexample` states "the object X violates the statement
H", so a verified counterexample is on the way to `proved`, not `disproved`.

**Standing.** Four kinds of result stay distinguishable, without a fifth status
field: a *known result* is cited and has no record; a *rediscovered* result has
a record with novelty `prior-resolution-identified` and its source; an
*original candidate* has a record that is not yet promoted; an *established*
contribution is `proved` or `disproved`. The generated index shows this as the
column *Standing*, derived from the status.

**Dependencies and relations.** `depends_on` lists proof dependencies only:
other contributions, by identifier, and external results, by citation.
`relations` lists everything else, with one of the types `originated_from`,
`contributes_to`, `generalizes`, `implies`, `equivalent_to`, `refutes`,
`supersedes`, pointing to a contribution or to a problem. One contribution may
originate from one investigation and contribute to several; a contribution
found outside every investigation simply has no `originated_from`.

**Statements, fingerprints and reassessment.** The fingerprint of a
contribution is the SHA-256 of its statement
(`python scripts/catalogue.py fingerprint MD-XXXX`). A review recorded as
evidence carries the Git revision reviewed and the fingerprint of the
statement it covers, set after comparing the two. A proof dependency on
another contribution carries the fingerprint of the statement that was relied
on; it is required once the dependent record claims a complete argument. When
a statement changes materially, its fingerprint changes, and validation then
fails for every status that rested on the old one — a review status without a
current review, a dependent pinned to the old statement — until the claim is
reassessed and the status or the pin is updated. Old evidence stays in the
record as history and is reported as covering an earlier statement.

**Promotion.** As for a problem (`AGENTS.md` section 4), without waiting for
the parent conjecture, and with one more condition: every contribution the
proof depends on is itself `proved` or `previously-resolved`.

## Research memory

Durable knowledge is stored in the repository:

| Kind of knowledge | Location |
| --- | --- |
| Active conjecture, definitions, established lemmas, failed approaches, counterexamples, observations, proof dependencies, decisions, obstacles, next steps | `research/active/<id>-<slug>/STATE.md` |
| What each session did, with which model and budget | `research/active/<id>-<slug>/journal.md` |
| Each contribution worth an identity: statement, status, relations, references to its evidence | `research/discoveries.json` |
| Exploration that belongs to no catalogued problem | `research/explorations/<topic>.md` |
| Verification results | `verification/receipts/`, experiment result files, review reports |
| Source references, literature, novelty coverage | `research/candidates/<id>-<slug>.md` |
| AI model participation | journal entries, review reports, commit trailers, attribution records |
| Problems considered and rejected, resolved conjectures met during scouting | `research/scouting-log.md` |

`STATE.md` is written for a reader with no other context and is kept short.
Long derivations go to separate notes linked from it.

## Budgets and efficiency

- A session has a written time budget, computation budget and stopping
  condition before it starts (`autoresearch.md`). The default is about one hour
  of agent work and 30 minutes of computation. This holds in exploration too:
  what exploration is spared is the predefined objective, not the budget.
- A larger campaign (long searches, many parallel agents, paid API use) needs
  an explicit budget approved by the director and recorded in `STATE.md`.
- No unbounded autonomous loops.
- Journal entries record, where the environment provides them: model,
  wall-clock runtime of computations, token usage, number of iterations, proof
  attempts, counterexamples found, formalization attempts, successful
  verifications, and cost estimates with their assumptions. Anything not
  provided is written as `unavailable`.
- Before repeating a search or a literature check, read what the repository
  already records about it.
