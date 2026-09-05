# AI-Native Software Engineering Skill

A reusable, gated engineering workflow for AI coding agents.

## What it solves

AI coding is fast, but speed without engineering controls creates ambiguous requirements, architectural drift, weak tests, and false confidence. This skill adds explicit gates, role discipline, evidence standards, and traceability around the coding loop.

## Workflow

`Problem → Requirements → Architecture → Design → Tasks → Implementation → Review → Testing → Benchmark → Acceptance → Release`

The workflow uses gates **G0–G10** and keeps the traceability chain:

`Requirement → Design/ADR → Task → Code → Test → Acceptance`

Validation is a control loop: a failed review, test, benchmark, or acceptance check can send the work back to the appropriate earlier gate instead of allowing a defective change to proceed.

## Repository contract

- `SKILL.md` — core skill and engineering rules
- `AGENTS.md` — repository-level operating contract for AI agents
- `docs/WORKFLOW.md` — state machine, exit criteria, evidence model, and adversarial checklist
- `docs/COMMANDS.md` — portable command protocol
- `CHANGELOG.md` — version history and roadmap

## Templates

- `templates/requirements-template.md` — requirements
- `templates/architecture-template.md` — architecture
- `templates/adr-template.md` — architecture decision records
- `templates/review-template.md` — adversarial review
- `templates/acceptance-template.md` — acceptance
- `templates/traceability-template.md` — requirement-to-test traceability

## Core engineering rules

1. Requirements before implementation for non-trivial work.
2. Every important behavior has observable acceptance criteria.
3. Consequential architectural decisions are recorded as ADRs.
4. Tasks are small and independently verifiable.
5. Requirements are never changed silently.
6. Tests derive from requirements and risk, not merely implementation.
7. AI-generated code receives adversarial review.
8. Completion claims require evidence.
9. Unknowns are labeled instead of invented.
10. Secrets and credentials never enter source control.

## Agent commands

Where the host agent supports command aliases, use:

`/spec` `/clarify` `/plan` `/tasks` `/implement` `/review` `/test` `/benchmark` `/accept` `/release` `/status`

Commands are workflow intents and do not bypass gate requirements.

## Recommended use

Load `SKILL.md` as the core instruction and `AGENTS.md` as the repository-local operating contract. For small, low-risk changes, use Minimal Mode; it compresses documentation without removing verification or evidence requirements.

## Design principles

- Specification before implementation
- Explicit assumptions and unknowns
- Testable acceptance criteria
- Architecture decisions are recorded
- Small, verifiable tasks
- Adversarial review of AI-generated code
- Evidence-based completion
- Quantitative benchmarks when material
- No silent requirement changes
- Smallest architecture that satisfies the verified requirements

## Roadmap

- Tool-specific adapters for Codex, Claude Code, Cursor, and OpenCode
- End-to-end example project
- Optional CI checks for traceability and release hygiene

## License

MIT
