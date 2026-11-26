# Claude Code entry point

The permanent research rules are in `AGENTS.md`, imported below. Do not
duplicate or override them here.

@AGENTS.md

## Claude Code specifics

- **Session procedure:** `autoresearch.md`, also available as the skill
  `/research-session`. Independent review of a claim: skill `/review-claim`.
- **Roles:** the main session acts as Research Director. The other roles are
  subagents in `.claude/agents/` (`problem-scout`, `literature-auditor`,
  `mathematical-researcher`, `computational-experimenter`,
  `formalization-agent`, `adversarial-reviewer`, `publication-agent`). Delegate
  when a role needs an independent context or parallel work; do small tasks
  directly.
- **Review independence:** always run `adversarial-reviewer` as a fresh
  subagent, and give it the primary source and the claimed proof — not your own
  reasoning or conclusion.
- **Environment:** Python through `uv run ...`; Lean through `lake` inside
  `formalization/` (the wrapper `scripts/verify_lean.py` locates the toolchain).
  On Windows, `elan` installs to `%USERPROFILE%\.elan\bin`.
- **Telemetry:** record the model identifier in each journal entry. Token and
  cost figures are recorded only when the environment actually reports them.
