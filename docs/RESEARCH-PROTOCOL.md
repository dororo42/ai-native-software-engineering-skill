# External Project & Community Research Protocol

## Purpose

Use this protocol when the project needs to learn from existing AI engineering frameworks, coding-agent workflows, libraries, tools, or community practice.

The goal is not to copy a popular repository. The goal is to identify practices that are:

1. technically credible,
2. actively maintained,
3. validated by real users,
4. relevant to the current problem,
5. compatible with this Skill's evidence and gate model.

## Source hierarchy

Use sources according to the question being answered.

| Question | Preferred evidence |
|---|---|
| What does the project implement? | Current GitHub source/docs/tests |
| Is it maintained? | Recent commits, releases, PRs, issue activity |
| Is it mature? | Release history, tests/CI, documentation, compatibility, ecosystem |
| What breaks in practice? | GitHub issues/PR reviews + recurring community reports |
| How do users actually use it? | Reddit/community discussions, examples, discussions |
| Is a pattern suitable here? | Cross-source synthesis + local prototype/verification |

No single signal is sufficient for a maturity judgment.

## GitHub evaluation

For each candidate repository, collect when relevant:

- stars and forks, with observation date
- recent commit activity
- release frequency and latest release
- contributor activity
- open/closed issue and PR signals
- age of unresolved issues
- recurring issue themes
- maintainer response patterns
- tests, CI, documentation, examples
- integrations/extensions/ecosystem
- breaking changes and migration history

### Activity

Activity is a time-series property, not a star count. Prefer recent commits/releases and sustained issue/PR handling over lifetime popularity.

### Maturity

Treat maturity as a composite judgment based on:

`release stability + test/CI coverage + documentation + compatibility + maintenance + ecosystem + issue resolution`

Do not label a project "mature" solely because it has many stars.

### Issue analysis

Do not count issues mechanically. Classify them:

- bug / regression
- usability / documentation
- architecture / design
- compatibility
- performance
- security
- installation / integration
- feature request
- duplicate / stale / invalid

Look for repeated failure modes. A single severe issue may matter more than dozens of cosmetic requests.

## Reddit and community evaluation

Use Reddit and comparable forums primarily for experiential evidence:

- Does the workflow work outside the author's examples?
- What setup friction appears repeatedly?
- Which failure modes do users report?
- Does the workflow create excessive context/documentation overhead?
- Does it require constant human supervision?
- Are model/tool combinations important to success?
- Are there disagreements that expose boundary conditions?

Classify community evidence as:

`single anecdote → repeated reports → cross-community pattern → repository corroboration`

A highly upvoted post is still not equivalent to a controlled experiment or project documentation.

## Scoring model

For comparative research, use a 0–5 score for each dimension:

| Dimension | Weight | Guidance |
|---|---:|---|
| Activity | 15% | Recent commits/releases and sustained maintenance |
| Maturity | 20% | Stability, tests, docs, compatibility, release history |
| Issue/PR health | 15% | Responsiveness, resolution, recurring defects |
| Technical relevance | 20% | Similarity to the problem being solved |
| Community evidence | 15% | Quality and recurrence of real-world feedback |
| Ecosystem/adoption | 10% | Integrations, extensions, contributors, usage signals |
| Transparency | 5% | Clear docs, changelog, issue/discussion visibility |

The weighted score is a decision aid, not an objective truth. Explain material qualitative exceptions.

## Research record

For every important external lesson record:

```text
PROJECT:
SOURCE:
OBSERVED_AT:
FACTS:
METRICS:
COMMUNITY_SIGNALS:
RECURRING_FAILURES:
INFERENCE:
LESSON:
APPLICABILITY:
DECISION: ADOPT | ADAPT | REJECT | WATCH
LOCAL_VALIDATION:
```

## Adoption rule

Do not adopt an external pattern directly because it is popular.

Use this sequence:

`Discover → Measure → Inspect → Corroborate → Prototype → Verify → Adopt/Reject`

If the external pattern conflicts with this project's requirements, evidence model, or safety/security constraints, reject it even if the source project is highly popular.

## Volatile metrics

Stars, forks, open issues, open PRs, release counts, and contributor counts change continuously. Always attach an observation date when reporting them.

Prefer statements such as:

> "Observed on 2026-09-05: approximately X stars and Y forks."

Avoid presenting a live counter as a permanent property of the project.

## Example: current research basis

The v0.3 design compared Superpowers, GitHub Spec Kit, and OpenSpec. The selection combined repository scale with workflow relevance and active issue/PR signals. The resulting Skill adopted complementary ideas rather than cloning any repository.

Community feedback also influenced the design. For example, recent coding-agent discussions repeatedly describe failure modes such as agents exceeding scope, producing superficial tests, ignoring methodology as context grows, and requiring human review of diffs. These reports support keeping tasks small, verification explicit, and review independent from implementation. Community reports are treated as qualitative signals rather than proof of universal behavior.

## Research anti-patterns

Avoid:

- ranking projects by stars alone
- treating GitHub issue count as project quality
- quoting one Reddit post as consensus
- using stale metrics without dates
- confusing popularity with technical maturity
- copying implementation details without understanding constraints
- citing an issue without checking whether it was fixed
- ignoring closed issues and release notes
- relying on AI-generated summaries instead of inspecting primary sources
- adopting a pattern without local validation
