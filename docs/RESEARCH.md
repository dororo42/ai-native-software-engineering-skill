# Comparative Research Notes

Updated: 2026-09-05

This document records the design lessons used for v0.3. It does not copy implementation text from the referenced projects.

## Selection

| Project | Stars* | Forks* | Issue/PR signal | Why selected |
|---|---:|---:|---|---|
| obra/superpowers | ~270k | ~24k | 100+ active issues; 200+ open PRs in recent GitHub views | Closest match to a complete agent methodology and composable skills |
| github/spec-kit | ~120k+ | ~10k+ | hundreds of issues and active PR/discussion ecosystem | Strongest reference for SDD, command decomposition, integrations, and validation |
| Fission-AI/OpenSpec | ~60k+ | ~4k+ | 200+ issues; 100+ open PRs in recent views | Strongest reference for lightweight change lifecycle and spec evolution |

*GitHub counters change continuously; values are approximate observations from September 2026 web research, not permanent rankings.

## Lessons adopted

### Superpowers

Observed strengths include TDD, systematic debugging, verification-before-completion, explicit planning/execution skills, subagent-driven development, and two-stage review. Its repository also describes skill-behavior tests and plugin-infrastructure tests. These ideas motivated:

- RED → GREEN → REFACTOR guidance
- separate specification-compliance and code-quality review passes
- explicit verification before completion
- future skill behavior evaluation

Community issues also expose real operational failure modes: model selection for subagents, context growth, harness portability, and workflow steps being skipped. The skill therefore treats role switching and gate transitions as explicit controls rather than implicit prose.

### GitHub Spec Kit

Spec Kit separates workflow actions such as specify, clarify, plan, tasks, implement, analyze, checklist, and converge, and tests integration-generated skill structure and frontmatter. Its evolution also demonstrates the value of extensions and agent integrations.

Adopted lessons:

- Agent Skills-compatible frontmatter
- explicit command granularity
- deterministic package validation
- clear separation of user-facing requirements from implementation details
- integration/adaptation as a first-class concern

### OpenSpec

OpenSpec's current workflow emphasizes a lightweight change workspace: proposal, delta specifications, design, tasks, implementation, verification/sync, and archive. It maintains a clean current specification and preserves completed change context.

Adopted lessons:

- change-oriented workspace
- current spec as source of truth
- delta requirements for proposed changes
- verify before archive
- preserve completed change history
- fast path for small/medium changes without forcing a heavyweight process

## Design decision for this project

This project intentionally combines the strongest complementary ideas rather than cloning any one framework:

`Explore → Specify → Design → Tasks → Implement → Review → Test → Verify → Benchmark → Accept → Archive/Release`

The distinguishing focus is the **evidence contract** and **gate state machine**: the agent must state what is known, assumed, unknown, and verified, and must move backward when evidence invalidates an earlier decision.
