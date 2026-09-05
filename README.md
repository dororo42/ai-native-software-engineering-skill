# AI-Native Software Engineering Skill

A reusable engineering workflow for AI coding agents.

## What it solves

AI coding is fast, but speed without engineering controls creates ambiguous requirements, architectural drift, weak tests, and false confidence. This skill adds explicit gates and traceability around the coding loop.

## Workflow

`Problem -> Requirements -> Architecture -> Design -> Tasks -> Implementation -> Review -> Testing -> Benchmark -> Acceptance -> Release`

The workflow uses gates G0–G10 and keeps the chain:

`Requirement -> Design -> Task -> Code -> Test -> Acceptance`

## Included

- `SKILL.md` — core skill and agent protocol
- `templates/requirements-template.md` — requirements template
- `templates/architecture-template.md` — architecture template
- `templates/adr-template.md` — ADR template
- `templates/review-template.md` — adversarial review template
- `templates/acceptance-template.md` — acceptance template

## Recommended use

Load `SKILL.md` as an instruction/skill for an AI coding agent. For small changes, use the Minimal Mode defined in the skill instead of producing heavyweight artifacts.

## Design principles

- Specification before implementation
- Explicit assumptions
- Testable acceptance criteria
- Architecture decisions are recorded
- Small, verifiable tasks
- Adversarial review of AI-generated code
- Evidence-based completion
- Quantitative benchmarks when claims require them
- No silent requirement changes

## License

MIT
