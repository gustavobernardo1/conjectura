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

## Eligible problems

A problem is eligible when it is a precisely stated, published statement
(paper, preprint, problem list, OEIS entry, formal problem repository) for which
there is positive, dated evidence that it is open, and for which a search for
resolutions has been recorded. Partial progress toward such a statement —
special cases, sharper hypotheses, corrected statements — is eligible work.

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
enforced by `research/schema/catalogue.schema.json`. Their meanings:

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

## Research memory

Durable knowledge is stored in the repository:

| Kind of knowledge | Location |
| --- | --- |
| Active conjecture, definitions, established lemmas, failed approaches, counterexamples, observations, proof dependencies, decisions, obstacles, next steps | `research/active/<id>-<slug>/STATE.md` |
| What each session did, with which model and budget | `research/active/<id>-<slug>/journal.md` |
| Verification results | `verification/receipts/`, experiment result files, review reports |
| Source references, literature, novelty coverage | `research/candidates/<id>-<slug>.md` |
| AI model participation | journal entries, review reports, commit trailers, attribution records |
| Problems considered and rejected, resolved conjectures met during scouting | `research/scouting-log.md` |

`STATE.md` is written for a reader with no other context and is kept short.
Long derivations go to separate notes linked from it.

## Budgets and efficiency

- A session has a written time budget, computation budget and stopping
  condition before it starts (`autoresearch.md`). The default is about one hour
  of agent work and 30 minutes of computation.
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
