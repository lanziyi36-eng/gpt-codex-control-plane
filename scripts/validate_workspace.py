#!/usr/bin/env python3
"""Validate the GPT-Codex control plane workspace structure."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "BRAIN.md",
    "SWITCHBOARD.md",
    "README.md",
    ".gitignore",
    "status/PROJECT_STATUS.md",
    "decisions/decision_log.md",
    "reviews/README.md",
    "codex_outputs/README.md",
    "human_approvals/README.md",
    "docs/SETUP.md",
    "docs/OPERATING_PROTOCOL.md",
    "docs/ISOLATION_AND_PERMISSIONS.md",
    "docs/COMMANDS.md",
    "prompts/CODEX_CREATE_REPO_PROMPT.md",
    "prompts/GPT_BRAIN_START_PROMPT.md",
    "prompts/CODEX_TASK_PROMPT.md",
    "prompts/GPT_REVIEW_PROMPT.md",
    "tasks/TEMPLATE/brief.md",
    "tasks/TEMPLATE/codex_prompt.md",
    "tasks/TEMPLATE/acceptance.md",
    "tasks/TEMPLATE/result.md",
    "tasks/TEMPLATE/review.md",
    "tasks/T-0001-bootstrap/brief.md",
    "tasks/T-0001-bootstrap/codex_prompt.md",
    "tasks/T-0001-bootstrap/acceptance.md",
    "tasks/T-0001-bootstrap/result.md",
    "tasks/T-0001-bootstrap/review.md",
    "scripts/new_task.py",
    "scripts/validate_workspace.py",
    ".github/ISSUE_TEMPLATE/codex_task.yml",
    ".github/ISSUE_TEMPLATE/brain_review.yml",
    ".github/pull_request_template.md",
]

REQUIRED_TEMPLATE_FILES = [
    "brief.md",
    "codex_prompt.md",
    "acceptance.md",
    "result.md",
    "review.md",
]

MANDATORY_SWITCHES = [
    "GPT_READ",
    "GPT_WRITE",
    "CODEX_READ",
    "CODEX_EXECUTE",
    "CODEX_CAN_PUSH",
    "AUTO_REVIEW",
    "HUMAN_APPROVAL_REQUIRED",
    "NETWORK_ACCESS_FOR_CODEX",
    "SECRET_ACCESS",
]


def report_line(ok: bool, message: str) -> str:
    status = "OK" if ok else "FAIL"
    return f"[{status}] {message}"


def validate_required_files() -> list[str]:
    errors: list[str] = []
    print("Required files:")
    for relative in REQUIRED_FILES:
        exists = (ROOT / relative).is_file()
        print(report_line(exists, relative))
        if not exists:
            errors.append(f"Missing required file: {relative}")
    return errors


def validate_template_files() -> list[str]:
    errors: list[str] = []
    print("\nTask template:")
    for name in REQUIRED_TEMPLATE_FILES:
        relative = f"tasks/TEMPLATE/{name}"
        exists = (ROOT / relative).is_file()
        print(report_line(exists, relative))
        if not exists:
            errors.append(f"Missing task template file: {relative}")
    return errors


def validate_switchboard() -> list[str]:
    errors: list[str] = []
    switchboard = ROOT / "SWITCHBOARD.md"
    print("\nSwitchboard:")
    if not switchboard.is_file():
        print(report_line(False, "SWITCHBOARD.md exists"))
        return ["Missing SWITCHBOARD.md"]
    text = switchboard.read_text(encoding="utf-8", errors="replace")
    for switch_name in MANDATORY_SWITCHES:
        present = switch_name in text
        print(report_line(present, switch_name))
        if not present:
            errors.append(f"Missing mandatory switch: {switch_name}")
    return errors


def main() -> int:
    print("GPT-Codex control plane workspace validation\n")
    errors: list[str] = []
    errors.extend(validate_required_files())
    errors.extend(validate_template_files())
    errors.extend(validate_switchboard())

    if errors:
        print("\nValidation result: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nValidation result: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
