---
name: ai-native-software-engineering
description: A gated, spec-driven software engineering workflow for AI coding agents. Use when developing features, fixing bugs, refactoring, reviewing AI-generated code, planning architecture, defining requirements, testing, benchmarking, or preparing a release. Enforces requirements, design, task decomposition, TDD where appropriate, adversarial review, evidence-based verification, traceability, and explicit acceptance.
license: MIT
metadata:
  version: "0.3.0"
  methodology: "spec-driven-ai-engineering"
---

# AI-Native Software Engineering Skill

## Purpose

Run AI-assisted software development as an evidence-driven engineering control loop rather than a code-generation conversation.

The default lifecycle is:

`Explore → Specify → Design → Tasks → Implement → Review → Test → Verify → Benchmark → Accept → Archive/Release`

Use the smallest workflow that preserves correctness. For trivial changes, use Minimal Mode.

## Non-Negotiable Rules

1. Clarify the problem before implementation.
2. Convert important behavior into observable acceptance criteria.
3. Record consequential architectural decisions as ADRs.
4. Decompose non-trivial work into independently verifiable tasks.
5. Never silently change requirements, scope, interfaces, or constraints.
6. Treat `UNKNOWN` as a valid state; never invent repository facts, APIs, outputs, metrics, or test results.
7. Prefer TDD for behavior-changing code when practical: RED → GREEN → REFACTOR.
8. Review AI-generated changes adversarially; implementation is not proof of correctness.
9. Verify the implementation against the approved artifacts before acceptance.
10. Quantitative claims require reproducible measurements.
11. Never expose or commit credentials, tokens, private keys, or other secrets.
12. Prefer the smallest architecture that satisfies verified requirements.

## Workflow Gates

### G0 — Explore / Problem Definition

Identify:
- user and business problem
- desired outcome
- context and existing system
- constraints
- in-scope and out-of-scope behavior
- assumptions and unknowns

If the problem is unclear, investigate first. Do not manufacture certainty.

### G1 — Specify

Produce stable requirement IDs and testable acceptance criteria.

For each important requirement define:
- actor/context
- observable behavior
- success criteria
- failure/edge scenarios
- priority

Keep product behavior in the specification. Put implementation mechanisms in design artifacts unless the mechanism itself is part of the contract.

### G2 — Architecture

Define:
- components and boundaries
- interfaces
- data flow
- dependencies
- security/trust boundaries
- reliability and operational concerns
- performance constraints
- alternatives

Create an ADR for consequential choices.

### G3 — Detailed Design

Define APIs, schemas, state transitions, algorithms, error handling, concurrency, security, observability, migration/compatibility behavior, and edge cases as applicable.

The design must be sufficiently concrete that implementation does not require guessing.

### G4 — Tasks

Create dependency-ordered tasks. Each task should specify:
- requirement IDs
- input/preconditions
- expected output
- affected area
- validation method
- dependencies

Prefer small tasks that can be reviewed and reverted independently.

### G5 — Implementation

Implement only approved tasks.

For behavior changes, prefer:

`RED: write a failing test → GREEN: minimal implementation → REFACTOR: improve without changing behavior`

Keep changes scoped. Update tests and documentation when behavior changes. Do not perform unrelated cleanup unless explicitly approved.

### G6 — Adversarial Review

Perform two distinct passes for non-trivial changes:

**Pass A — Specification compliance**
- Does the implementation satisfy every requirement and acceptance criterion?
- Are scope and compatibility preserved?
- Are edge/failure scenarios covered?

**Pass B — Code quality / risk**
- correctness and boundary conditions
- security and trust boundaries
- reliability and recovery
- performance and resource use
- maintainability and abstraction quality
- compatibility and migrations
- test quality and false-positive risk

Findings must have severity, evidence, disposition, and owner/follow-up where applicable.

### G7 — Testing

Run the applicable verification layers:
- unit
- integration
- system/end-to-end
- regression
- static/type/lint
- security

Include happy paths and failure paths. Map important tests to requirements.

### G8 — Verify / Benchmark

First verify artifact-to-implementation consistency:
- requirements ↔ code
- design/ADR ↔ implementation
- tasks ↔ completed work
- tests ↔ acceptance criteria

When performance, quality, accuracy, latency, memory, throughput, or UX is material, benchmark using:
- baseline
- methodology
- environment
- sample size
- measurements
- comparison
- uncertainty/limitations

### G9 — Acceptance

Execute acceptance criteria against the implemented system. Record:
- requirement coverage
- evidence
- deviations
- known limitations
- residual risks
- acceptance decision

### G10 — Archive / Release

For completed changes, preserve the context needed to understand why and how the change happened. A useful change record contains:

`proposal → delta requirements/spec → design → tasks → implementation evidence → verification → acceptance`

Then merge the accepted specification into the current source of truth and archive the change record, or prepare the release when the project uses a release-oriented workflow.

Before release verify reproducibility, documentation, clean configuration, and absence of secrets/debug artifacts.

## Change-Oriented Workflow

For medium/large feature work, prefer a change workspace rather than editing the permanent specification directly:

```text
specs/                         # current behavioral source of truth
changes/<change-name>/
├── proposal.md               # why / what / impact
├── specs/<capability>/
│   └── spec.md               # delta requirements + scenarios
├── design.md                 # how
└── tasks.md                  # implementation checklist
```

After acceptance:

```text
changes/<change-name>/ → changes/archive/YYYY-MM-DD-<change-name>/
```

Merge accepted deltas into the current `specs/` source of truth before or during archival. Conflicting or missing requirement sections must stop the archive rather than being silently overwritten.

## Evidence Model

Use exact evidence labels:

- **Verified** — directly observed by an executed check or measurement.
- **Supported** — strongly supported by inspection but not executed.
- **Assumed** — working assumption.
- **Unknown** — insufficient information.
- **Blocked** — cannot proceed without a missing dependency/decision.

Never upgrade evidence merely through wording.

## Agent Status Protocol

At every gate report:

```text
STATUS: Gx — READY|IN_PROGRESS|BLOCKED|PASSED|FAILED
KNOWN:
ASSUMED:
UNKNOWN:
CHANGES:
VALIDATION:
NEXT:
```

## Portable Commands

When the host agent supports command aliases:

- `/explore` — investigate an unclear problem
- `/spec` — create/update requirements and acceptance criteria
- `/clarify` — resolve ambiguity and conflicts
- `/plan` — architecture, ADRs, and detailed design
- `/tasks` — task decomposition
- `/implement` — execute approved tasks
- `/review` — two-pass adversarial review
- `/test` — execute mapped verification
- `/verify` — compare implementation with artifacts
- `/benchmark` — quantitative evaluation
- `/accept` — execute acceptance
- `/archive` — merge accepted specs and preserve change history
- `/release` — release readiness
- `/status` — report state and evidence

Commands are intents, not bypasses. `/implement` cannot skip specification; `/accept` cannot substitute for verification.

## Role Discipline

Use explicit roles when useful:

- Product Analyst
- Architect
- Designer
- Implementer
- Reviewer
- Test Engineer
- Benchmark Engineer
- Release Engineer

One agent may perform several roles, but implementation and review should remain conceptually separate.

## Traceability

For non-trivial work maintain:

`REQ → AC → DESIGN/ADR → TASK → CODE → TEST → VERIFY → ACCEPT`

Every important requirement needs a validation path. If a requirement is intentionally non-testable, document why and define another acceptance mechanism.

## Anti-Hallucination / AI Failure Controls

The agent must:

1. Inspect the repository before describing its structure.
2. Inspect dependency versions before relying on version-sensitive APIs.
3. Never invent command output or claim a test passed without executing it.
4. Never claim a benchmark result without measurement.
5. Never claim external facts without an appropriate source.
6. Surface contradictions instead of selecting silently.
7. Maintain unresolved `UNKNOWN` items until resolved or explicitly accepted as risk.
8. Treat generated code, compiled code, and tested code as three different evidence levels.

## Minimal Mode

For a low-risk change:

```text
Requirement
Acceptance criteria
Inspection
Approach + risks
Test first when practical
Implementation
Targeted tests
Two-pass review
Verification
Evidence + limitations
```

Do not force a large artifact set onto trivial work, but do not remove verification.

## Definition of Done

A change is done only when:

- requirements are explicit
- acceptance criteria are testable
- consequential design decisions are understood
- implementation is complete
- relevant tests/checks have executed
- adversarial review is complete
- artifact-to-code verification is complete
- quantitative claims have evidence where applicable
- deviations and limitations are disclosed
- documentation is sufficient for another engineer/agent to reproduce and maintain the change
