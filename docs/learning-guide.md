# Learning guide

The project director is learning advanced mathematics while directing
AI-assisted research. Learning here is driven by the problems under
investigation; this is not a general course.

## How learning material is organised

Each problem that is selected for investigation gets one guide,
`learning/<id>-<slug>.md`, kept concise and updated as the investigation
proceeds. It contains:

1. **Prerequisites** — what one needs to know to read the statement and the
   first experiments.
2. **Definitions** — the objects of the problem, each with the smallest example.
3. **Fundamental theorems** — the known results the investigation leans on,
   with a pointer to a proof.
4. **Why the problem is difficult** — where the obvious approaches stop.
5. **How the concepts connect to the investigation** — which idea is used where.
6. **Reading** — specific sections of specific sources, in a suggested order.
7. **Exercises** — small problems taken from the actual investigation, most of
   them checkable with the code in `experiments/`.
8. **What worked and what did not** — an explanation, in plain mathematical
   language, of the successful and unsuccessful approaches recorded in
   `STATE.md`.

## Rules

- Educational examples are labelled as such and are never presented as results.
  Known theorems reproduced for learning are attributed to their sources.
- Exercises have answers that can be verified (by the provided code or by a
  short proof), so that the director can check understanding independently of
  an AI system.
- The guide should make the director able to explain, without assistance, what
  the conjecture says, what has been established, how it was verified, and
  what remains open. That ability is also what responsible authorship requires
  (`docs/attribution-policy.md`).
- When a session produces something the guide does not yet explain, the guide
  is updated in the same session or the gap is listed under *Open obligations*
  in `STATE.md`.

## Current guides

Guides accompany investigations and live on the `research` branch until the
corresponding work is promoted.

- `learning/CJ-0001-collins-shor-peak.md` — distance matrices of trees, their
  characteristic polynomials, and the peak of the coefficient sequence.
