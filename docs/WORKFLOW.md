# AI-Native Workflow

## 1. State Machine

```text
G0 Problem
   ↓
G1 Requirements
   ↓
G2 Architecture
   ↓
G3 Detailed Design
   ↓
G4 Tasks
   ↓
G5 Implementation
   ↓
G6 Adversarial Review
   ↓
G7 Testing
   ↓
G8 Benchmark (when applicable)
   ↓
G9 Acceptance
   ↓
G10 Release
```

### Transition rule

A transition requires evidence that the current gate's exit criteria are satisfied. If not, remain in the current gate or move backward to resolve the defect.

Examples:

- Ambiguous requirement discovered during implementation → return to G1.
- Architectural conflict discovered during coding → return to G2/G3 and record an ADR if needed.
- Review finding affecting behavior → return to G5, then repeat G6/G7.
- Benchmark regression → return to G5/G6/G7 until accepted or explicitly waived.

## 2. Gate Exit Criteria

| Gate | Exit criteria |
|---|---|
| G0 | Problem, users, outcome, constraints, scope, assumptions identified |
| G1 | Stable requirement IDs and testable acceptance criteria exist; ambiguity resolved |
| G2 | Components, boundaries, interfaces, dependencies, risks, and consequential ADRs established |
| G3 | APIs/data/state/error/concurrency/security details are sufficient to implement without guessing |
| G4 | Tasks are independently verifiable, ordered by dependency/risk, and mapped to requirements |
| G5 | Approved tasks implemented with scoped changes and relevant tests added/updated |
| G6 | Correctness/security/reliability/performance/compatibility/test-quality review completed; findings dispositioned |
| G7 | Applicable tests/checks executed and results recorded; important requirements have validation evidence |
| G8 | Baseline, methodology, environment, sample size, results, and limitations recorded when applicable |
| G9 | Acceptance criteria executed; deviations and residual risks explicitly recorded |
| G10 | Documentation, reproducibility, release notes, and secret/debug-artifact checks completed |

## 3. Evidence Levels

Use precise evidence language:

- **Verified** — directly observed or produced by an executed check.
- **Supported** — strongly supported by inspected code/docs but not directly executed.
- **Assumed** — necessary working assumption, not verified.
- **Unknown** — insufficient evidence.
- **Blocked** — cannot proceed without missing information or access.

Never convert `Assumed`, `Unknown`, or `Supported` into `Verified` by wording alone.

## 4. Traceability

For non-trivial work maintain:

```text
REQ → DES/ADR → TASK → CODE → TEST → AC
```

A requirement without a test or acceptance path is incomplete unless it is explicitly documented as non-testable and justified.

## 5. Adversarial Review Checklist

Before acceptance, ask:

### Correctness
- Does behavior match every applicable requirement?
- Are boundary and failure states handled?
- Are defaults and units unambiguous?

### Security
- Can untrusted input cross a trust boundary?
- Are authentication, authorization, secrets, file paths, serialization, and injection risks addressed where relevant?

### Reliability
- What happens after timeout, restart, partial failure, duplicate execution, or dependency outage?
- Is state recoverable or intentionally disposable?

### Performance
- What is the hot path?
- Are complexity, I/O, memory, latency, concurrency, and resource limits acceptable?
- Is a benchmark needed?

### Compatibility
- Are public APIs, data formats, configuration, CLI behavior, and existing workflows preserved?

### Tests
- Could weak tests pass while the implementation is wrong?
- Are negative, edge, regression, and integration cases covered where material?

## 6. AI-Specific Anti-Hallucination Rules

The agent must:

1. Inspect before assuming repository structure.
2. Inspect dependency versions before relying on APIs that may vary by version.
3. Never invent command output, test results, benchmark numbers, file contents, or external facts.
4. Clearly distinguish generated code from executed code.
5. Report failed or skipped checks rather than hiding them.
6. Ask focused questions when a missing decision materially affects implementation.
7. Keep a list of unresolved `UNKNOWN` items for non-trivial work.

## 7. Minimal Mode

For low-risk changes, use a compressed record:

```text
Requirement
Acceptance criteria
Inspection
Approach + risks
Implementation
Targeted tests
Adversarial review
Evidence
Limitations
```

Minimal Mode reduces documentation overhead; it does not remove the requirement for verification or honest evidence.
