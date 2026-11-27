---
name: research-session
description: Run one bounded Conjectura research session following autoresearch.md. Use when asked to continue, resume or start research on a catalogued problem.
effort: high
---

# Research session

You are acting as Research Director for one session.

1. Read `AGENTS.md` and `autoresearch.md` (both short). Choose the mode and say
   which. *Focused work* on one exact statement follows the twelve steps, with
   the written objective, falsification test, stopping condition and budget.
   *Exploration* needs only a written budget and one line on what is being
   explored; follow the mathematics and leave a dated note. A limit set by the
   user is binding in both.
2. Budget, unless the user set another: at most about 120 minutes of agent
   work, approximately the last 20 minutes reserved for verification,
   documentation and persistence; computations capped at 30 minutes of
   wall-clock time. The time is a maximum, not a target: stop early when the
   objective is reached or the mathematics no longer justifies the effort, and
   use your own judgment on whether to continue, redirect or suspend. Record
   the start time (`date`) and open the journal entry marked `in progress`.
3. Leave a checkpoint about every 30 minutes, as `autoresearch.md` describes:
   a few lines under *Checkpoints* in the journal entry (time elapsed, what is
   established and at what level, what is unfinished and where, next action),
   `STATE.md` if the current truth changed, and a checkpoint commit if files
   changed. If your context was compacted or the session was interrupted, the
   journal entry in progress and `STATE.md` are where you resume from.
4. Choose the investigation: the one named by the user, otherwise the active
   investigation with the highest rank in `uv run python scripts/catalogue.py rank`.
   If no investigation is active, start the top shortlisted candidate by
   creating `research/active/<id>-<slug>/` from `research/templates/`.
5. The session runs on the model the user selected (the principal
   investigator); this skill does not change it. Subagent models are set in
   `.claude/agents/`: Sonnet for computation and scouting, Opus for
   adversarial review and literature audits, the principal's model for
   mathematical research, formalization and publication.
6. Subagents are the most expensive part of a session. Spawn one only when a
   role needs its own context: literature checks to `literature-auditor`
   (before a claim is promoted), computations longer than about ten minutes
   to `computational-experimenter`, Lean work to `formalization-agent`; do
   everything else yourself, and prefer these agents to the built-in
   general-purpose one. As a default, about three subagents per session; use
   more when the work is scientifically justified, and say why in the journal.
7. Never review your own claim. For a candidate proof or counterexample, use
   the `review-claim` skill. One independent review per claim by default. A
   significant result — one that settles a catalogued problem or one of its
   halves, or one that is to be promoted — keeps the full validation of
   `AGENTS.md` sections 4 to 6, with at least two independent reviews, one by
   a model other than the author's whenever such a model is available.
8. Before finishing (this is what the reserved time is for): verification
   commands run and reported, `STATE.md` updated, journal entry completed and
   closed with the model identifier and honest telemetry, contributions that deserve an identity registered in
   `research/discoveries.json` with the status they honestly have, catalogue
   and registry validated, generated views rendered, and a commit only if
   there is a durable artifact.

Report to the user: the objective, what was run, what was established (with its
verification level), what failed, and the next step.
