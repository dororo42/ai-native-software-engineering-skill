# Comparative Research Notes

Updated: 2026-09-05

This document records the design lessons used for v0.3/v0.3.1. It does not copy implementation text from the referenced projects.

## Selection

| Project | Stars* | Forks* | Issue/PR signal | Why selected |
|---|---:|---:|---|---|
| obra/superpowers | ~270k | ~24k | 100+ active issues; 200+ open PRs in recent GitHub views | Closest match to a complete agent methodology and composable skills |
| github/spec-kit | ~120k+ | ~10k+ | hundreds of issues and active PR/discussion ecosystem | Strongest reference for SDD, command decomposition, integrations, and validation |
| Fission-AI/OpenSpec | ~60k | ~4k+ | 100+ issues; 100+ PRs in recent views | Strongest reference for lightweight change lifecycle and spec evolution |

*GitHub counters change continuously; values are approximate observations from September 2026 research, not permanent rankings.

## Research method

Project selection does not use stars alone. We compare:

`activity + maturity + issue/PR health + technical relevance + community evidence + ecosystem + transparency`

GitHub is the primary source for implementation and maintenance facts. Reddit/community discussions are used as qualitative evidence about real-world experience, friction, and recurring failure modes. Claims are labeled internally as `FACT`, `METRIC`, `COMMUNITY`, `INFERENCE`, or `UNKNOWN`.

## Lessons adopted

### Superpowers

Observed strengths include TDD, systematic debugging, verification-before-completion, explicit planning/execution skills, subagent-driven development, and two-stage review. Its repository also describes skill-behavior tests and plugin-infrastructure tests. These ideas motivated:

- RED → GREEN → REFACTOR guidance
- separate specification-compliance and code-quality review passes
- explicit verification before completion
- future skill behavior evaluation

Community/issue feedback also exposes real operational failure modes: model selection for subagents, context growth, harness portability, and workflow steps being skipped. The Skill therefore treats role switching and gate transitions as explicit controls rather than implicit prose.

### GitHub Spec Kit

Spec Kit separates workflow actions such as specify, clarify, plan, tasks, implement, analyze, checklist, and converge, and tests integration-generated skill structure and frontmatter. Its evolution also demonstrates the value of extensions and agent integrations.

Adopted lessons:

- Agent Skills-compatible frontmatter
- explicit command granularity
- deterministic package validation
- clear separation of user-facing requirements from implementation details
- integration/adaptation as a first-class concern

Its July 2026 project newsletter reported substantial growth in stars, forks, contributors, releases, community extensions, agent integrations, and discussions. The same newsletter also records community criticism around credit consumption, over-production of documentation, and single-source-of-truth concerns. This is a useful example of why adoption metrics and negative feedback should both be tracked.

### OpenSpec

OpenSpec's current workflow emphasizes a lightweight change workspace: proposal, delta specifications, design, tasks, implementation, verification/sync, and archive. It maintains a clean current specification and preserves completed change context.

Adopted lessons:

- change-oriented workspace
- current spec as source of truth
- delta requirements for proposed changes
- verify before archive
- preserve completed change history
- fast path for small/medium changes without forcing a heavyweight process

Recent issue/discussion feedback also reveals an important design lesson for this Skill: deterministic tooling should own deterministic filesystem/spec operations where possible. OpenSpec users have reported discrepancies between canonical CLI behavior and generated agent skills around archive/sync, as well as terminology and early-sync edge cases. These are not reasons to reject OpenSpec; they are evidence that semantic agent steps and deterministic state transitions should have clear ownership boundaries.

## Community evidence

Recent Reddit discussions about agentic coding provide independent experiential signals that reinforce several controls in this Skill.

A July 2026 r/LocalLLaMA discussion described agents exceeding methodology constraints, ignoring instructions as context grows, producing superficial tests, and generating excessive code. This is a single community thread, not proof of universal behavior, but the failure modes are directly relevant to context budgeting, scoped tasks, independent review, and verification.

A June 2026 r/LocalLLaMA discussion described a practical loop of small task → tests → diff review → fix → repeat, with users emphasizing continued human supervision. This supports the Skill's preference for small independently verifiable tasks rather than assuming full autonomous handoff.

A March 2026 r/ClaudeAI discussion described Skills, agents, spec-driven workflows, MCPs, and plugins as complementary layers. This supports keeping the core methodology tool-agnostic while allowing adapters/integrations to sit around it.

Community evidence is intentionally not treated as authoritative technical documentation. Recurring signals should be corroborated with repository evidence or local experiments before becoming normative rules.

## Design decision for this project

This project intentionally combines the strongest complementary ideas rather than cloning any one framework:

`Explore → Specify → Design → Tasks → Implement → Review → Test → Verify → Benchmark → Accept → Archive/Release`

The distinguishing focus is the **evidence contract** and **gate state machine**: the agent must state what is known, assumed, unknown, and verified, and must move backward when evidence invalidates an earlier decision.

A second distinguishing principle is **evidence-driven prior-art research**:

`Discover → Measure → Inspect → Corroborate → Prototype → Verify → Adopt/Reject`

This prevents the Skill itself from becoming static dogma. External projects, issue trackers, releases, and community feedback become inputs to engineering judgment, not unquestioned authorities.

## Primary research references

- Superpowers: https://github.com/obra/superpowers
- GitHub Spec Kit: https://github.com/github/spec-kit
- OpenSpec: https://github.com/Fission-AI/OpenSpec
- Agent Skills specification: https://agentskills.io/specification

See `docs/RESEARCH-PROTOCOL.md` for the reusable evaluation procedure and scoring model.
