# Attribution policy

Conjectura uses AI systems as an active means of mathematical discovery. The
record of who contributed what must therefore be exact, in both directions: no
hidden AI participation, no inflated human contribution.

## Contribution categories

Every result package and every manuscript carries an attribution record
(`research/templates/attribution.md`) with one entry per category:

| Category | What is recorded |
| --- | --- |
| Research direction | Who chose the problem, set objectives and budgets, and decided what to pursue or stop. |
| Human mathematical contribution | Ideas, lemmas, proofs, corrections or checks contributed by a person, described specifically. "None" is a valid entry. |
| AI-generated proof strategies | Which strategies came from an AI system, with the model named. |
| AI-generated mathematical discoveries | Conjectures, lemmas, constructions or counterexamples first produced by an AI system. |
| Computational contribution | Who or what wrote and ran the code; hardware; software versions. |
| Formalization | Who or what wrote the Lean statements and proofs. |
| Independent verification | Each review: reviewer (person or model), how independence was obtained, revision reviewed. |
| External mathematical results | Every theorem, technique, dataset or piece of software relied on, with citation. |

## Rules

1. **Name the models.** Record exact model identifiers when the environment
   reports them (for example `claude-fable-5-2`), and the date. If the
   identifier is unknown, write "unknown model" — do not guess.
2. **Record at the time of work.** Each journal entry names the model that did
   the session's work; each commit made with AI assistance carries a
   `Co-Authored-By:` trailer. The attribution record of a result is assembled
   from these, not reconstructed from memory.
3. **Authorship is earned by contribution and responsibility.** Operating an AI
   model does not by itself confer scientific authorship of a mathematical
   result. Authorship of a manuscript requires a substantive intellectual
   contribution and the ability to take responsibility for the correctness of
   the work; the director's actual role (direction, verification,
   understanding, exposition) is stated as it was.
4. **AI systems are not listed as authors** where venue policy forbids it;
   their role is disclosed in full in the AI-use statement instead. Venue
   policies are checked at submission time.
5. **Credit prior work.** External results are cited to their primary sources.
   A conjecture is attributed to its original authors and source, with the
   statement number.
6. **Methodological credit.** The workflow of this project is informed by the
   projects listed in `docs/methodology.md`; that credit stays in the
   repository.
7. **Corrections are attributed too.** If a person or a reviewing model finds
   an error, the record says who found it.

## AI-use disclosure

Every publishable result includes a disclosure paragraph stating: which AI
systems were used and for what (literature search, conjecturing, proof
strategy, proof writing, computation, formalization, review, exposition); which
parts were checked by a human and how; which parts were verified formally or
computationally; and what was not independently checked.
