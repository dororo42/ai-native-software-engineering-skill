# Agent Command Protocol

These commands are portable workflow intents. The host agent may map them to its own command or skill mechanism.

| Command | Gate | Output |
|---|---|---|
| `/spec` | G0→G1 | problem statement, scope, requirements, acceptance criteria |
| `/clarify` | G1 | ambiguity/conflict list and focused questions |
| `/plan` | G2→G3 | architecture, interfaces, risks, ADRs, detailed design |
| `/tasks` | G4 | dependency-ordered implementation tasks |
| `/implement` | G5 | code/config/docs changes plus local validation |
| `/review` | G6 | adversarial findings, severity, disposition, verdict |
| `/test` | G7 | executed checks and requirement mapping |
| `/benchmark` | G8 | methodology, baseline, results, comparison, limitations |
| `/accept` | G9 | acceptance evidence, deviations, residual risks, decision |
| `/release` | G10 | release-readiness checklist and reproducibility evidence |
| `/status` | any | current gate, blockers, evidence, next action |

## `/status` format

```text
STATUS: Gx — READY|BLOCKED|IN_PROGRESS|PASSED|FAILED
KNOWN:
ASSUMED:
UNKNOWN:
CHANGES:
VALIDATION:
NEXT:
```

## Command safety

A command does not override gate requirements. `/implement` cannot substitute for requirements or design; `/accept` cannot substitute for tests; `/release` cannot erase unresolved risks.

When a command conflicts with an approved requirement, stop and report the conflict.
