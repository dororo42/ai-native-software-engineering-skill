# AI-Native Software Engineering Skill

## Purpose

A gated, spec-driven workflow for AI coding agents. It treats requirements, architecture, design, implementation, review, testing, benchmarking, and acceptance as explicit engineering artifacts rather than relying on conversational intent.

## Core Rules

1. Clarify the problem before proposing implementation.
2. Convert requirements into observable and testable acceptance criteria.
3. Establish architecture and record consequential decisions as ADRs.
4. Decompose implementation into small, verifiable tasks.
5. Do not silently change requirements; surface conflicts and obtain confirmation.
6. Derive tests from requirements and risk, not only from implementation details.
7. Review AI-generated code adversarially for correctness, security, maintainability, performance, and hidden assumptions.
8. Do not claim completion without evidence: tests, benchmarks, inspection results, or acceptance checks.
9. Preserve traceability: Requirement -> Design -> Task -> Code -> Test -> Acceptance.
10. Prefer the smallest architecture that satisfies the requirements; avoid speculative complexity.

## Standard Workflow

### G0 — Problem Definition
- State the problem, users, context, constraints, and desired outcome.
- Identify unknowns and assumptions.
- Define what is explicitly out of scope.

### G1 — Requirements
- Produce functional and non-functional requirements.
- Assign each requirement a stable identifier.
- Define acceptance criteria for each externally meaningful behavior.
- Resolve ambiguity before implementation.

### G2 — Architecture
- Identify components, boundaries, interfaces, data flow, dependencies, and operational concerns.
- Evaluate major alternatives.
- Record consequential choices as ADRs.

### G3 — Detailed Design
- Define APIs, schemas, state transitions, algorithms, error handling, concurrency, security boundaries, and observability as applicable.
- Explicitly identify edge cases.

### G4 — Task Decomposition
- Convert design into independently verifiable tasks.
- Each task should have a clear input, output, affected area, and validation method.
- Order tasks according to dependency and risk.

### G5 — Implementation
- Implement one coherent task at a time.
- Keep changes aligned with the approved specification and architecture.
- Add or update tests with behavior changes.
- Avoid unrelated refactoring.

### G6 — Adversarial Code Review
Review from at least these perspectives when relevant:
- Correctness: Does it actually satisfy the requirement?
- Boundary conditions: What happens at empty, invalid, extreme, concurrent, or partial states?
- Security: Can untrusted input cross a trust boundary incorrectly?
- Reliability: What happens after failure, restart, timeout, or dependency outage?
- Performance: Are there unnecessary hot paths, allocations, I/O, or algorithmic regressions?
- Maintainability: Is the abstraction justified and understandable?
- Compatibility: Does it preserve existing behavior and interfaces?
- Test quality: Could the implementation pass weak tests while still being wrong?

### G7 — Testing
- Run unit, integration, system, regression, static, and security checks as appropriate.
- Test both happy paths and failure paths.
- Map important tests back to requirements.

### G8 — Benchmark
Use quantitative evidence when performance, quality, accuracy, latency, memory, resource usage, or UX is a material requirement.
- Define baseline.
- Define measurement methodology.
- Record environment and sample size.
- Compare before/after results.
- State uncertainty and limitations.

### G9 — Acceptance
- Execute the acceptance criteria against the implemented system.
- Confirm requirement coverage.
- Record known deviations, limitations, and unresolved risks.

### G10 — Release
- Verify documentation and operational instructions.
- Confirm reproducibility.
- Produce release notes when appropriate.
- Ensure no secrets, debug artifacts, or unintended files are included.

## Agent Communication Protocol

At each phase, the agent should explicitly state:

- Current phase and gate.
- What is known.
- What is assumed.
- What is still unknown.
- Proposed next action.
- Evidence required to pass the gate.

When information is missing, ask focused questions rather than inventing requirements.

## Role Switching

An AI coding agent may switch roles deliberately:

- Product Analyst — requirements and acceptance.
- Software Architect — boundaries and architecture.
- Designer — detailed technical design.
- Implementer — code changes.
- Reviewer — adversarial review.
- Test Engineer — verification strategy and execution.
- Benchmark Engineer — quantitative evaluation.
- Release Engineer — reproducibility and release readiness.

The same agent may perform multiple roles, but should not implicitly treat implementation as proof of correctness.

## Traceability Matrix

Maintain a lightweight matrix for non-trivial work:

| Requirement | Design | Task | Code | Test | Acceptance |
|---|---|---|---|---|---|
| REQ-001 | DES-001 | TASK-001 | path/to/code | TEST-001 | AC-001 |

Every important requirement should have a validation path.

## ADR Guidance

Create an ADR when a decision has meaningful consequences for architecture, compatibility, security, performance, data, operations, or long-term maintenance.

Minimum ADR structure:
- Context
- Decision
- Alternatives considered
- Consequences
- Status

## Minimal Mode

For a small, low-risk change, compress the workflow to:

1. Restate requirement and acceptance criteria.
2. Inspect relevant code and dependencies.
3. State implementation approach and risks.
4. Implement.
5. Run targeted tests.
6. Perform adversarial review.
7. Report evidence and remaining limitations.

Do not force heavyweight architecture documents onto trivial changes.

## Definition of Done

A task is done only when:

- Requirements are explicit.
- Acceptance criteria are testable.
- Architecture decisions are understood.
- Implementation is complete.
- Relevant tests pass.
- AI-generated changes have been reviewed adversarially.
- Performance/quality claims have evidence where applicable.
- Known limitations are disclosed.
- Documentation is sufficient for another engineer or agent to reproduce and maintain the result.
