# Scouting log

A record of problem-discovery campaigns: how they were run, what was catalogued,
what was set aside, and which well-known conjectures were found to have reported
resolutions. Negative information is kept so that it is not rediscovered.

## Campaign 1 — 2026-11-26

**Method.** Four literature-scout subagents (Claude, model `claude-fable-5-2`,
separate contexts) covered spectral graph theory and matrix analysis; graph
theory and combinatorics; elementary number theory and integer sequences;
numerical analysis, inequalities and discrete optimisation. Each was asked for
five published conjectures with positive evidence of being open, quoted
statements, recorded search coverage, and an explicit list of unverified items,
within a budget of about 30 web requests. The coordinating agent (same model)
selected, scored and catalogued the candidates, and re-read the primary source
of the top-ranked one.

**Telemetry reported by the environment.** Subagent tokens: 171,732 (spectral),
153,179 (combinatorics), 319,614 (number theory), 190,191 (analysis). Tool
calls: 37, 46, 70, 34. The number-theory scout exceeded its request budget
(about 35 web operations and 70 tool calls in total).

**Limits of this campaign.** Searches were general web searches and arXiv
listings; Google Scholar citation trails, MathOverflow and
<https://www.erdosproblems.com/> (HTTP 403 to automated fetches) were not
covered. Most statements were read from secondary sources. Every dossier lists
what was not verified. The campaign establishes a *preliminary* search only.

### Catalogued

Fifteen problems, `CJ-0001` to `CJ-0015`; see [`INDEX.md`](INDEX.md).

### Considered and not catalogued

| Problem | Reason |
| --- | --- |
| Marcus–de Oliveira determinantal conjecture | The statement was read only from Wikipedia and a garbled rendering; the 2025 survey that documents its status returned HTTP 403. Catalogue after reading a primary source. |
| Sun's conjecture on det C_p(x) (Conjecture 1.1 in Ren–Sun, arXiv:2507.18589) | The statement was reconstructed from garbled PDF text; at least seven papers settled neighbouring conjectures between May and November 2026. |
| Radcliffe's question on OEIS A004290 | Posed as a question, not as a conjecture; nineteen recorded AI attempts in the OEIS Open benchmark failed. Could be catalogued as a question later. |
| 4/3 conjecture for the subtour relaxation of metric TSP | The computational frontier (n = 14 general, n = 16 half-integral, arXiv:2603.12995) was reached with a 96-core machine; not feasible on the available hardware. |
| Ryser, Alon–Tarsi and Rota basis conjectures | No resolution found, but small-case frontiers are far beyond desktop computation. |
| Written on the Wall II, entries 61, 72, 84, 96, 133, 189, 372 | Tagged open in formal-conjectures on 2026-11-26; not yet examined individually. Natural additions if `CJ-0005` or `CJ-0006` prove productive. |

### Starting points reported as resolved

The scouts found resolution claims for the following conjectures. **These are
claims in preprints, most of them unrefereed and several seen only as search
snippets; this project has not verified any of them.** They are listed so that
the status of each is checked properly before anyone works on it.

| Conjecture | Reported resolution | How it was seen |
| --- | --- | --- |
| Brouwer's conjecture (Laplacian eigenvalue sums) | Kothari–Tudose, arXiv:2606.12197 | Abstract fetched |
| Signless Laplacian version of Brouwer's conjecture | Yuan–Zhang, arXiv:2609.31355 | Abstract fetched |
| Bollobás–Nikiforov conjecture | Coutinho, Liu, Spier, Tang, Zhang (2026), per arXiv:2610.36912 | Search snippet |
| Elphick–Farber–Goldberg–Wocjan conjecture | Liu–Tang–Zhang, arXiv:2607.18031 | Search snippet |
| Elphick–Wocjan clique bound | arXiv:2607.18044 | Search snippet |
| Crouzeix's conjecture | Jin (preprints.org 202607.1919); Lorist–Schwenninger, arXiv:2608.03841 | Search snippet |
| Chvátal's conjecture | Chang–Liu–Liu, arXiv:2609.19123 | Cited in a fetched abstract |
| Courtade–Kumar conjecture | Three September 2026 preprints, one fetched (arXiv:2609.24184) | Abstract fetched |
| Gaussian product inequality | arXiv:2609.20234 | Abstract fetched |
| Sendov's conjecture | Claimed August 2026 with a Lean formalization | Search summary only |
| Smale's mean value conjecture | Conflicting 2026 claims | Search summary only |
| Seymour's second neighbourhood conjecture | Unrefereed claimed proof, arXiv:2501.00614 | Abstract fetched |
| Casas-Alvero conjecture (general) | Claimed proof arXiv:2501.09272 retitled "A conditional proof" on 2026-11-10 | Abstract fetched |
| Several OEIS conjectures (A001818, A053175, A296056, A277060) | Proved in papers from 2018 to 2026 | Entries and abstracts fetched |
| Written on the Wall II, entries 19, 34, 58, 200 | Tagged solved in formal-conjectures | Lean files fetched |

**Lesson recorded.** Many widely known conjectures in the project's priority
fields acquired resolution claims during 2026, and lists of "open" problems
(including the OEIS Open benchmark and the formal-conjectures README) lag
behind. Membership of such a list is not evidence that a problem is open; the
eligibility check must be repeated immediately before work starts and again
before any claim.
