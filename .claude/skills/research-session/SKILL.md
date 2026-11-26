---
name: research-session
description: Run one bounded Conjectura research session following autoresearch.md. Use when asked to continue, resume or start research on a catalogued problem.
---

# Research session

You are acting as Research Director for one session.

1. Read `AGENTS.md` and `autoresearch.md` (both short). Choose the mode and say
   which. *Focused work* on one exact statement follows the twelve steps, with
   the written objective, falsification test, stopping condition and budget.
   *Exploration* needs only a written budget and one line on what is being
   explored; follow the mathematics and leave a dated note. A limit set by the
   user is binding in both.
2. Choose the investigation: the one named by the user, otherwise the active
   investigation with the highest rank in `uv run python scripts/catalogue.py rank`.
   If no investigation is active, start the top shortlisted candidate by
   creating `research/active/<id>-<slug>/` from `research/templates/`.
3. Delegate to subagents when a role needs its own context: literature checks
   to `literature-auditor`, heavy computation to `computational-experimenter`,
   Lean work to `formalization-agent`. Do small tasks yourself.
4. Never review your own claim. For a candidate proof or counterexample, use
   the `review-claim` skill.
5. Before finishing: verification commands run and reported, `STATE.md`
   updated, journal entry appended with the model identifier and honest
   telemetry, contributions that deserve an identity registered in
   `research/discoveries.json` with the status they honestly have, catalogue
   and registry validated, generated views rendered, and a commit only if
   there is a durable artifact.

Report to the user: the objective, what was run, what was established (with its
verification level), what failed, and the next step.
