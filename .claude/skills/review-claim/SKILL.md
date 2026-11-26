---
name: review-claim
description: Obtain an independent adversarial review of a claimed proof, counterexample, computation or formalization at a specific Git revision.
---

# Independent review of a claim

1. Make sure the claim is committed. Record the revision (`git rev-parse HEAD`)
   and the list of files that constitute the claim.
2. Launch the `adversarial-reviewer` subagent as a fresh context. Give it only:
   the catalogue id, the primary source reference, the paths of the files to
   review, the revision, and the checklist in `research/templates/review.md`.
   Do **not** give it your reasoning, your confidence, or your summary of why
   the proof works.
3. When a different capable model is available, prefer it for the reviewer and
   record which model was used.
4. Save the report to `research/active/<id>-<slug>/reviews/<date>-<model>.md`.
5. If the verdict is `gap found`: record the gap in `STATE.md` under *Open
   obligations*; the status stays or returns to `active-investigation`.
   If `no gap found within stated scope`: the director may set
   `external_review` to `ai-reviewed`. This is AI review, not human or peer
   review, and it covers only the reviewed revision.
6. Any later material change to the statement or proof requires a new review.
