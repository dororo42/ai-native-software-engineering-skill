# AI-Native Software Engineering Skill

A reusable, gated engineering workflow for AI coding agents.

## What it solves

AI coding is fast, but speed without engineering controls creates ambiguous requirements, architectural drift, weak tests, and false confidence. This skill adds explicit gates, role discipline, evidence standards, and traceability around the coding loop.

## Workflow

`Explore → Specify → Design → Tasks → Implement → Review → Test → Verify → Benchmark → Accept → Archive/Release`

The workflow uses gates **G0–G10** and keeps the traceability chain:

`Requirement → Acceptance → Design/ADR → Task → Code → Test → Verify → Acceptance`

Validation is a control loop: a failed review, test, verification, or benchmark can send work back to the appropriate earlier gate.

## Repository contract

- `SKILL.md` — Agent Skills-compatible core skill and engineering rules
- `AGENTS.md` — repository-level operating contract for AI agents
- `docs/WORKFLOW.md` — state machine, exit criteria, evidence model, and adversarial checklist
- `docs/COMMANDS.md` — portable command protocol
- `docs/RESEARCH.md` — comparative study of Superpowers, Spec Kit, and OpenSpec
- `CHANGELOG.md` — version history
- `VERSION` — current version

## Templates

- `templates/requirements-template.md` — requirements
- `templates/architecture-template.md` — architecture
- `templates/adr-template.md` — architecture decision records
- `templates/review-template.md` — adversarial review
- `templates/acceptance-template.md` — acceptance
- `templates/traceability-template.md` — requirement-to-test traceability
- `templates/change-template.md` — change workspace

## Validation

Run the deterministic package check before publishing or changing the skill:

```bash
python scripts/validate_skill.py
```

The validator checks required files, frontmatter, description length, and critical sections. It intentionally remains small and dependency-free.

## Core engineering rules

1. Requirements before implementation for non-trivial work.
2. Every important behavior has observable acceptance criteria.
3. Consequential architectural decisions are recorded as ADRs.
4. Tasks are small and independently verifiable.
5. Requirements are never changed silently.
6. Prefer TDD for behavior changes when practical.
7. AI-generated code receives two-pass adversarial review.
8. Implementation is verified against its artifacts before acceptance.
9. Completion claims require evidence.
10. Unknowns are labeled instead of invented.
11. Secrets and credentials never enter source control.
12. Use the smallest architecture that satisfies verified requirements.

## Agent commands

Where the host agent supports command aliases:

`/explore` `/spec` `/clarify` `/plan` `/tasks` `/implement` `/review` `/test` `/verify` `/benchmark` `/accept` `/archive` `/release` `/status`

Commands are workflow intents and do not bypass gate requirements.

## Change workspace

For medium/large work, keep the current behavioral specification clean and put proposed work in a separate change workspace:

```text
specs/                         # current source of truth
changes/<change-name>/
├── proposal.md
├── specs/<capability>/spec.md # delta requirements
├── design.md
└── tasks.md
```

After verification and acceptance, merge the accepted delta and archive the complete change context.

## Design principles

- Specification before implementation
- Explicit assumptions and unknowns
- Testable acceptance criteria
- TDD where practical
- Two-pass adversarial review
- Artifact-to-code verification
- Evidence-based completion
- Quantitative benchmarks when material
- No silent requirement changes
- Smallest architecture that satisfies verified requirements

## Research basis

v0.3 was informed by three high-signal open-source projects:

- urlobra/superpowershttps://github.com/obra/superpowers — composable agent skills, TDD, verification, review, and multi-agent workflows.
- urlGitHub Spec Kithttps://github.com/github/spec-kit — spec-driven development, modular commands, agent integrations, and skill validation.
- urlFission-AI OpenSpechttps://github.com/Fission-AI/OpenSpec — lightweight change workspaces, delta specs, verification, synchronization, and archival.

See `docs/RESEARCH.md` for the design lessons and observed issue/PR signals.

## Roadmap

- Tool-specific adapters for Codex, Claude Code, Cursor, OpenCode, and other Agent Skills hosts
- End-to-end example project
- Skill behavior evaluation suite
- Optional CI checks for traceability and release hygiene

## License

MIT
