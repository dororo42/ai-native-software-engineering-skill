# Changelog

## v0.3.1 — 2026-09-05

### Added
- External project and community research as an explicit part of the Skill methodology.
- GitHub evaluation criteria covering activity, maturity, issue/PR health, releases, tests, documentation, and ecosystem signals.
- Reddit/community evaluation guidance for real-world workflow feedback and recurring failure modes.
- Evidence classes for external research: `FACT`, `METRIC`, `COMMUNITY`, `INFERENCE`, `UNKNOWN`.
- `docs/RESEARCH-PROTOCOL.md` with a repeatable research, scoring, corroboration, and adoption process.

### Changed
- Expanded Skill routing metadata to include evidence-driven evaluation of external projects and community feedback.
- Added research anti-hallucination rules: volatile metrics require observation dates, community anecdotes cannot be treated as universal facts, and external patterns should be locally validated before adoption.

## v0.3.0 — 2026-09-05

### Added
- Agent Skills-compatible frontmatter in `SKILL.md`.
- TDD guidance using RED → GREEN → REFACTOR.
- Two-pass adversarial review: specification compliance and code quality/risk.
- Explicit Verify gate before acceptance.
- Change-oriented workspace with proposal, delta spec, design, and tasks artifacts.
- Archive lifecycle preserving completed change context.
- Deterministic dependency-free validator at `scripts/validate_skill.py`.
- `docs/RESEARCH.md` documenting comparative study of Superpowers, Spec Kit, and OpenSpec.
- `templates/change-template.md`.
- `VERSION` file.

### Changed
- Lifecycle expanded to `Explore → Specify → Design → Tasks → Implement → Review → Test → Verify → Benchmark → Accept → Archive/Release`.
- Portable command protocol expanded with `/explore`, `/verify`, and `/archive`.

## Unreleased — v0.2

### Added
- `AGENTS.md` as the repository-level operating contract for AI coding agents.
- Explicit workflow state machine and gate exit criteria.
- Evidence classification: Verified, Supported, Assumed, Unknown, Blocked.
- Portable command protocol for `/spec`, `/clarify`, `/plan`, `/tasks`, `/implement`, `/review`, `/test`, `/benchmark`, `/accept`, `/release`, and `/status`.
- AI-specific anti-hallucination rules.
- Traceability matrix template.
- Adversarial review checklist covering correctness, security, reliability, performance, compatibility, and test quality.

### Changed
- Expanded the original G0–G10 workflow into an enforceable control loop: failed validation can move work backward to the appropriate gate.
- Clarified that implementation, compilation, or generated output is not evidence of correctness by itself.
