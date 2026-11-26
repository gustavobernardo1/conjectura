# Publication policy

Nothing leaves the repository — no push to a new remote, release, DOI, preprint,
submission or message to a researcher — without the director's explicit
authorization for that specific action.

## Branches

- `main`: stable infrastructure and reviewed results.
- `research`: ongoing investigations, including candidates, drafts and failed
  approaches.
- Short-lived branches (`work/<topic>`, `review/<topic>`) for isolated tasks.

`research` is ahead of `main`: the catalogue on `research` is authoritative for
work in progress, and the catalogue on `main` reflects the last promoted state.
All meaningful history is preserved; published history is never rewritten.
`research` is not merged into `main` wholesale. A result or an infrastructure
change is promoted as a narrowly scoped change whose content has been checked.

## Result package

A result is publishable when `results/<id>-<slug>/` contains
(`research/templates/result-package.md`):

1. the theorem exactly as stated in the source, and exactly as proved, with any
   difference spelled out;
2. a self-contained written proof, or the counterexample with its verification;
3. the literature and novelty assessment, with search coverage and limitations;
4. the formal proof and its receipt, when a formalization exists, and the scope
   of what is formalized;
5. the commands and data that reproduce every computation;
6. the independent review report for the packaged revision;
7. the attribution record and the AI-use disclosure;
8. known limitations;
9. citation metadata (`CITATION.cff` at the root is updated for releases);
10. manuscript-ready LaTeX under `manuscripts/<id>-<slug>/`.

The four status dimensions are reported separately in the package. Typical
honest summaries look like: "written proof, AI-reviewed, not human-reviewed, no
prior resolution found within the documented search, not formalized".

## Pre-publication checklist

Run on the exact candidate revision:

- [ ] `uv run pytest` passes; `scripts/catalogue.py validate` and
      `render --check` pass.
- [ ] If Lean is involved: `scripts/verify_lean.py` passes on a clean tree and
      the receipt is committed.
- [ ] Every computation cited by the result was rerun from its documented
      command on this revision.
- [ ] The review report refers to this revision.
- [ ] The novelty search was refreshed within the last 30 days.
- [ ] Catalogue statuses match the package.
- [ ] Attribution record and AI-use disclosure are complete.
- [ ] No credentials, private files or irrelevant personal data are present.
- [ ] The director has read the result and authorized publication.

## Releases, DOIs, preprints

The repository is kept compatible with GitHub releases, Zenodo DOI registration
(via `CITATION.cff` and tagged releases) and arXiv (plain LaTeX, standard
packages, sources under `manuscripts/`). None of these is performed
automatically. An arXiv submission additionally requires the director to check
the venue's current policy on AI-assisted work and, where needed, endorsement.

## Corrections

If an error is found in something already published, the correction is
published with the same visibility: the status is changed, the package states
what was wrong and who found it, and the history is kept.
