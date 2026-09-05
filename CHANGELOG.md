# Changelog

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

### Planned
- Tool-specific adapters for Codex, Claude Code, Cursor, and OpenCode.
- A complete example project demonstrating the workflow from natural-language requirement to acceptance.
- Optional CI checks for traceability and release hygiene.
