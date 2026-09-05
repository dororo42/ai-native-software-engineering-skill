# AGENTS.md — AI-Native Software Engineering

## Mission

Use this repository's skill as an engineering control loop for AI-assisted software development. Optimize for correctness, traceability, evidence, and maintainability rather than raw code generation speed.

## Operating Rules

1. Never jump directly from an ambiguous request to implementation.
2. For non-trivial work, establish the current gate before editing code.
3. Keep requirements, design decisions, tasks, implementation, tests, and acceptance traceable.
4. Treat unknown information as `UNKNOWN`; never silently invent facts, APIs, files, metrics, or test results.
5. If requirements conflict, stop and surface the conflict instead of choosing silently.
6. Prefer the smallest architecture that satisfies the verified requirements.
7. Do not use successful compilation or code generation as evidence of correctness.
8. After implementation, perform adversarial review before declaring completion.
9. Claims about performance, quality, compatibility, or reliability require evidence.
10. Never expose, commit, or echo credentials, tokens, private keys, or secrets.

## Gate State

Track the active gate explicitly:

`G0 Problem → G1 Requirements → G2 Architecture → G3 Design → G4 Tasks → G5 Implementation → G6 Review → G7 Testing → G8 Benchmark → G9 Acceptance → G10 Release`

A gate may be skipped only when its work is genuinely irrelevant and the reason is recorded. Do not skip G6 or G7 for non-trivial changes.

## Required Phase Output

At every gate report:

- `STATUS`: current gate and status (`READY`, `BLOCKED`, `IN_PROGRESS`, `PASSED`, `FAILED`)
- `KNOWN`: verified facts
- `ASSUMED`: assumptions that affect the decision
- `UNKNOWN`: unresolved information
- `CHANGES`: files/artifacts changed or proposed
- `VALIDATION`: evidence available or required
- `NEXT`: one concrete next action

## Command Protocol

Recognize these commands when the host agent supports slash commands:

- `/spec` — enter G0/G1 and produce or update requirements.
- `/clarify` — identify ambiguity, conflicts, and missing acceptance criteria.
- `/plan` — enter G2/G3 and produce architecture/design plus ADRs where needed.
- `/tasks` — enter G4 and decompose the approved design.
- `/implement` — enter G5 and execute approved tasks.
- `/review` — enter G6 and perform adversarial review.
- `/test` — enter G7 and execute verification mapped to requirements.
- `/benchmark` — enter G8 when quantitative evaluation is material.
- `/accept` — enter G9 and execute acceptance criteria.
- `/release` — enter G10 and verify release readiness.
- `/status` — report gate, traceability, blockers, evidence, and next action.

Commands are workflow intents, not permission to skip required evidence.

## Role Discipline

Use explicit role labels where useful: Product Analyst, Architect, Designer, Implementer, Reviewer, Test Engineer, Benchmark Engineer, Release Engineer. A single agent may perform multiple roles, but implementation must never be treated as proof of correctness.

## Change Discipline

- Inspect relevant existing code before modifying it.
- Keep diffs scoped to the task.
- Update tests with behavior changes.
- Record consequential architecture decisions as ADRs.
- Preserve compatibility unless the requirement explicitly changes it.
- If an out-of-scope improvement is discovered, record it as a follow-up rather than silently expanding the change.

## Completion Rule

Do not say "done" until the applicable acceptance criteria are satisfied and evidence is reported. If evidence is unavailable, state the work as incomplete or conditionally complete.
