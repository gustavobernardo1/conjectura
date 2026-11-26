# Public summary: integration contract

`research/summary.json` carries a block named `public`, intended for
presentation outside the repository — in the first place on the director's
GitHub profile (`gustavobernardo1/gustavobernardo1`). This page is the contract
between that block and whatever reads it. It was requested by the director on
2026-11-26.

The block is produced by the existing generator
(`scripts/catalogue.py render`, function `public_summary`) from the same
authoritative records as the rest of the summary. It introduces no new record,
identifier or status: it selects from `research/catalogue.json` and
`research/discoveries.json` under the rules below.

## Location

| | |
| --- | --- |
| File | `research/summary.json`, on the branch `research` |
| Raw URL | <https://raw.githubusercontent.com/gustavobernardo1/conjectura/research/research/summary.json> |
| Pinned to a commit | `https://raw.githubusercontent.com/gustavobernardo1/conjectura/<commit>/research/summary.json` |
| Schema of the block | [`research/schema/public-summary.schema.json`](../research/schema/public-summary.schema.json) |

The repository is public, so the file is read without credentials. GitHub
serves raw files through a cache; a change may take a few minutes to appear.

**Why `research`.** Investigations, the registry of contributions and the
summary itself live on `research`; `main` holds stable infrastructure and
promoted results and at present contains neither the registry nor the summary.
`research` is ahead of `main` and contains everything `main` does, so one file
on `research` describes both the work in progress and the established results.
The separation of the two kinds of information is made by the counting rules,
not by the branch: an investigation is listed because the catalogue says it is
active, and a result is counted only after it has been promoted under
`AGENTS.md` section 4. Should the registry tooling be promoted to `main`, the
same path on `main` will hold the summary of the last promoted state; this
contract does not depend on it.

## What a reader should use

A reader should rely on exactly these fields and ignore the rest of the file,
which describes work in progress in more detail and may change shape.

| Field | Type | Meaning |
| --- | --- | --- |
| `public.schema_version` | integer | Version of this contract, currently `1`. It changes only when a field below is removed, renamed or changes meaning. New fields may be added without a change of version. |
| `generated.revision` | string or null | Git commit that was checked out when the summary was generated. |
| `generated.sources_committed` | boolean or null | `true` when that commit contains the source records exactly as summarized. `false`: the summary was generated before its sources were committed, and `revision` is the commit that preceded them. `null`: Git was not available. |
| `generated.sources` | object | Git blob identifier of each source record; identifies the summarized content exactly. |
| `public.active_investigations` | array | The catalogued problems in an active status, highest priority first. Each: `id` (`CJ-XXXX`), `title`, `url` (the problem's dossier), `status` (the four dimensions). Empty when there is none. |
| `public.primary_investigation` | object or null | The first element of `active_investigations`. |
| `public.established_original_discoveries` | object | Counts of established original contributions: `lemmas`, `theorems`, `counterexamples`, `other`, and `total` (their sum). |
| `public.resolved_conjectures` | object | Counts of catalogued conjectures settled by the project: `proved`, `disproved`, and `total` (their sum). |
| `public.latest_established_original_discovery` | object or null | The counted contribution with the latest `established_on`: `id` (`MD-XXXX`), `title`, `type`, `established_on` (date), `url` (its result package), `status`. |
| `public.latest_formally_verified_original_contribution` | object or null | The counted contribution with formal status `complete` and the latest receipt: `id`, `title`, `type`, `verified_utc` (creation time of the receipt), `url`, `status`. |
| `public.research_catalogue_url` | string or null | The generated index of problems and contributions. |
| `public.reviewed_results_url` | string or null | The directory of reviewed result packages. |

`status` is always the object
`{"mathematical", "formal", "novelty", "external_review"}` with the values of
`AGENTS.md` section 4. The four dimensions are independent and should be shown
as such: `ai-reviewed` is not human or peer review, and
`no-prior-resolution-found` means "within the documented search coverage",
never "novel".

Every URL points to the branch `research` of this repository, where the file it
names exists whenever the summary does.

## Counting rules

A contribution (`MD-XXXX`) is counted as an **established original discovery**
when both of the following hold.

1. Its mathematical status is `proved` or `disproved`. Validation
   (`scripts/catalogue.py validate`) admits these statuses only with a result
   package under `results/`, a review bound to the statement as it reads now,
   a recorded novelty search, a date `resolved_on`, and proof dependencies that
   are themselves `proved` or `previously-resolved`.
2. Its novelty status is `no-prior-resolution-found`, that is, a thorough
   search with documented coverage. A result promoted on a search that is only
   `preliminary-search-completed` is established in the repository and is not
   counted here until the search is completed.

Consequently the counts exclude:

- candidates, open conjectures, partial results, candidate proofs and candidate
  counterexamples (rule 1);
- rediscovered results, whose novelty is `prior-resolution-identified` and
  whose mathematical status is `previously-resolved` (rules 1 and 2), and known
  results, which are cited and have no record;
- rejected and superseded records (rule 1);
- calibration theorems, which exist only in the Lean registry and have no
  `MD-XXXX` record;
- contributions whose originality has not been assessed by a thorough search
  (rule 2).

Each counted contribution is counted once, under its recorded `type`: `lemma`
under `lemmas`, `theorem` under `theorems`, `counterexample` under
`counterexamples`, and every other type (`proposition`, `corollary`,
`identity`, `inequality`, `bound`, `proof`, `method`, `structural-result`,
`computational-finding`, `conjecture`) under `other`.

A **resolved conjecture** is a problem of the catalogue (`CJ-XXXX`) that
satisfies the same two rules, counted under `proved` or `disproved`. A problem
that the project formulated itself (catalogue field `discovery`) is not counted
here: its resolution is a contribution, not the resolution of a published
conjecture. Resolved conjectures and discoveries are separate dimensions. A
theorem that settles a catalogued conjecture has its own `MD-XXXX` record and
is counted once as a theorem, and the conjecture is counted once as resolved.

"Latest" means the latest date, and among equal dates the highest identifier.

No count is entered by hand. All of them are zero today, which is the accurate
state of the project.

## Update mechanism

- The summary is a committed file. It is regenerated by
  `uv run python scripts/catalogue.py render`, which the session protocol
  (`autoresearch.md`, step 11) runs after every change to the records, and
  which rewrites the file only when its content changes.
- The date, branch and revision of the `generated` block are kept from the
  committed file as long as nothing else changes, so regenerating produces no
  difference and no commit. The one exception is the existing rebinding step: a
  summary generated before its sources were committed is regenerated once after
  that commit, so that `revision` names a commit containing them.
- Continuous integration (`.github/workflows/ci.yml`) runs
  `scripts/catalogue.py validate` and `render --check` on every push to `main`
  and `research` and fails when the committed summary does not match the
  records. No workflow in this repository commits, pushes or writes to another
  repository.
- The published file changes when the director pushes `research`. A reader
  polls the raw URL on its own schedule; `generated.sources` or
  `generated.revision` tells it whether anything changed. Nothing here notifies
  the reader, and no token or cross-repository permission is involved.

## Missing or unavailable data

| Situation | Meaning | What the reader should do |
| --- | --- | --- |
| A field is `null`, an array is empty, a count is `0` | No record qualifies. | Present it as "none yet", not as an error. |
| A `url` is `null` | The repository address is not recorded in `CITATION.cff`. | Omit the link. |
| The request fails, the body is not JSON, the block `public` is absent, or `public.schema_version` is not a version the reader knows | The summary is unavailable or its contract changed. | Keep what was last displayed. Never replace it with zeros. |
| `generated.sources_committed` is `false` | The summary is ahead of the commit it names. | The content is usable; `generated.sources` identifies it. |

## Example

The block as generated from the records at revision `0ff2fad` (2026-11-26),
with the `generated` block of the same file. The rest of the file is omitted.

```json
{
  "public": {
    "schema_version": 1,
    "active_investigations": [
      {
        "id": "CJ-0001",
        "title": "Collins–Shor conjecture on the peak of the distance characteristic polynomial of a tree",
        "url": "https://github.com/gustavobernardo1/conjectura/blob/research/research/candidates/CJ-0001-collins-shor-peak.md",
        "status": {
          "mathematical": "active-investigation",
          "formal": "not-started",
          "novelty": "preliminary-search-completed",
          "external_review": "not-reviewed"
        }
      }
    ],
    "primary_investigation": {
      "id": "CJ-0001",
      "title": "Collins–Shor conjecture on the peak of the distance characteristic polynomial of a tree",
      "url": "https://github.com/gustavobernardo1/conjectura/blob/research/research/candidates/CJ-0001-collins-shor-peak.md",
      "status": {
        "mathematical": "active-investigation",
        "formal": "not-started",
        "novelty": "preliminary-search-completed",
        "external_review": "not-reviewed"
      }
    },
    "established_original_discoveries": {
      "lemmas": 0,
      "theorems": 0,
      "counterexamples": 0,
      "other": 0,
      "total": 0
    },
    "resolved_conjectures": {
      "proved": 0,
      "disproved": 0,
      "total": 0
    },
    "latest_established_original_discovery": null,
    "latest_formally_verified_original_contribution": null,
    "research_catalogue_url": "https://github.com/gustavobernardo1/conjectura/blob/research/research/INDEX.md",
    "reviewed_results_url": "https://github.com/gustavobernardo1/conjectura/tree/research/results"
  },
  "generated": {
    "date": "2026-11-26",
    "branch": "research",
    "revision": "0ff2fad07274eea57f3ec6ddf39e74205ba5948b",
    "sources_committed": true,
    "sources": {
      "research/catalogue.json": "23afc1f259224590e5f0eea346418241bc68a497",
      "research/discoveries.json": "be0e5c92d8e7c24805577378e1d0fee22d57419c",
      "research/priorities.json": "a0ae5525b59b7535ee2b7ba0418273d476246622",
      "formalization/registry.json": "fc4c60c169c8a99eadb96fd631d6ac3c0a96b22f"
    }
  }
}
```

The six contributions registered at that revision (`MD-0001` to `MD-0006`) are
candidates or rediscovered results, so none is counted.

## Scope

Generating the summary publishes nothing. Writing to the profile repository,
or to any other repository, is an outside action under
[`docs/publication-policy.md`](publication-policy.md) and is not performed by
any script here. The profile-side reader is implemented separately.
