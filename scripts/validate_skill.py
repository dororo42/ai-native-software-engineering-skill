#!/usr/bin/env python3
"""Deterministic structural validator for this Agent Skill package."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED_FILES = [
    "SKILL.md",
    "AGENTS.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "docs/WORKFLOW.md",
    "docs/COMMANDS.md",
    "templates/requirements-template.md",
    "templates/architecture-template.md",
    "templates/adr-template.md",
    "templates/review-template.md",
    "templates/acceptance-template.md",
    "templates/traceability-template.md",
    "templates/change-template.md",
]


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))

    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return fail("SKILL.md must start with YAML frontmatter")

    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return fail("invalid YAML frontmatter delimiters")

    frontmatter = match.group(1)
    if not re.search(r"^name:\s*[a-z0-9-]+\s*$", frontmatter, re.MULTILINE):
        return fail("frontmatter requires a kebab-case name")
    if not re.search(r"^description:\s*.+$", frontmatter, re.MULTILINE):
        return fail("frontmatter requires description")

    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE).group(1).strip()
    if len(description) > 1024:
        return fail(f"description exceeds 1024 characters: {len(description)}")

    required_sections = [
        "## Purpose",
        "## Non-Negotiable Rules",
        "## Workflow Gates",
        "## Evidence Model",
        "## Traceability",
        "## Anti-Hallucination / AI Failure Controls",
        "## Definition of Done",
    ]
    for section in required_sections:
        if section not in text:
            return fail(f"missing section: {section}")

    print("PASS: AI-Native Software Engineering Skill structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
