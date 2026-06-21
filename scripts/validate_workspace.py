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
    "docs/TASK_LIFECYCLE.md",
    "docs/DAILY_USE.md",
    "docs/BRAIN_CODEX_HANDOFF.md",
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
    "tasks/T-0002-operational-loop/brief.md",
    "tasks/T-0002-operational-loop/codex_prompt.md",
    "tasks/T-0002-operational-loop/acceptance.md",
    "tasks/T-0002-operational-loop/result.md",
    "tasks/T-0002-operational-loop/review.md",
    "scripts/new_task.py",
    "scripts/show_context.py",
    "scripts/set_active_task.py",
    "scripts/validate_workspace.py",
    ".github/ISSUE_TEMPLATE/codex_task.yml",
    ".github/ISSUE_TEMPLATE/brain_review.yml",
    ".github/pull_request_template.md",
]

REQUIRED_TASK_FILES = [
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

APPROVAL_REQUIRED_SAFE_VALUES = {
    "GPT_WRITE": "OFF",
    "AUTO_REVIEW": "OFF",
    "SECRET_ACCESS": "OFF",
}


def report_line(ok: bool, message: str) -> str:
    status = "OK" if ok else "FAIL"
    return f"[{status}] {message}"


def parse_markdown_table(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and cells[1]:
            values[cells[0]] = cells[1]
    return values


def human_approval_documents() -> list[Path]:
    approvals_dir = ROOT / "human_approvals"
    if not approvals_dir.is_dir():
        return []
    return sorted(path for path in approvals_dir.rglob("*.md") if path.is_file())


def has_human_approval_for(switch_name: str) -> bool:
    for path in human_approval_documents():
        text = path.read_text(encoding="utf-8", errors="replace")
        if switch_name in text and "approval" in text.lower():
            return True
    return False


def validate_required_files() -> list[str]:
    errors: list[str] = []
    print("Required files:")
    for relative in REQUIRED_FILES:
        exists = (ROOT / relative).is_file()
        print(report_line(exists, relative))
        if not exists:
            errors.append(f"Missing required file: {relative}")
    return errors


def validate_task_template() -> list[str]:
    errors: list[str] = []
    print("\nTask template:")
    for name in REQUIRED_TASK_FILES:
        relative = f"tasks/TEMPLATE/{name}"
        exists = (ROOT / relative).is_file()
        print(report_line(exists, relative))
        if not exists:
            errors.append(f"Missing task template file: {relative}")
    return errors


def validate_task_folders() -> list[str]:
    errors: list[str] = []
    print("\nTask folders:")
    tasks_dir = ROOT / "tasks"
    if not tasks_dir.is_dir():
        print(report_line(False, "tasks directory exists"))
        return ["Missing tasks directory"]

    task_dirs = sorted(path for path in tasks_dir.glob("T-*") if path.is_dir())
    if not task_dirs:
        print(report_line(False, "at least one tasks/T-* directory exists"))
        return ["No non-template task folders found"]

    for task_dir in task_dirs:
        missing = [
            name for name in REQUIRED_TASK_FILES if not (task_dir / name).is_file()
        ]
        ok = not missing
        relative = task_dir.relative_to(ROOT).as_posix()
        print(report_line(ok, f"{relative} has required task files"))
        for name in missing:
            errors.append(f"Missing task file: {relative}/{name}")
    return errors


def validate_project_status() -> tuple[list[str], str | None]:
    errors: list[str] = []
    print("\nProject status:")
    status_path = ROOT / "status" / "PROJECT_STATUS.md"
    if not status_path.is_file():
        print(report_line(False, "status/PROJECT_STATUS.md exists"))
        return ["Missing status/PROJECT_STATUS.md"], None

    values = parse_markdown_table(status_path.read_text(encoding="utf-8"))
    active_task = values.get("Active task", "").strip()
    has_active_task = bool(active_task)
    print(report_line(has_active_task, "Active task row is present"))
    if not has_active_task:
        errors.append("status/PROJECT_STATUS.md is missing an Active task row")
        return errors, None

    task_dir = ROOT / "tasks" / active_task
    exists = task_dir.is_dir()
    print(report_line(exists, f"Active task exists: tasks/{active_task}"))
    if not exists:
        errors.append(f"Active task directory does not exist: tasks/{active_task}")
    return errors, active_task


def validate_switchboard() -> list[str]:
    errors: list[str] = []
    print("\nSwitchboard:")
    switchboard = ROOT / "SWITCHBOARD.md"
    if not switchboard.is_file():
        print(report_line(False, "SWITCHBOARD.md exists"))
        return ["Missing SWITCHBOARD.md"]

    values = parse_markdown_table(switchboard.read_text(encoding="utf-8"))
    for switch_name in MANDATORY_SWITCHES:
        present = switch_name in values
        value = values.get(switch_name, "MISSING")
        print(report_line(present, f"{switch_name} = {value}"))
        if not present:
            errors.append(f"Missing mandatory switch: {switch_name}")

    for switch_name, expected in APPROVAL_REQUIRED_SAFE_VALUES.items():
        value = values.get(switch_name)
        if value is None:
            continue
        if value != expected and not has_human_approval_for(switch_name):
            errors.append(
                f"{switch_name} is {value}; expected {expected} unless human approval is documented"
            )

    codex_can_push = values.get("CODEX_CAN_PUSH")
    if codex_can_push == "MAIN_DIRECT":
        errors.append("CODEX_CAN_PUSH must not be MAIN_DIRECT")

    if errors:
        for error in errors:
            print(report_line(False, error))
    else:
        print(report_line(True, "switch safety values are acceptable"))
    return errors


def main() -> int:
    print("GPT-Codex control plane workspace validation\n")
    errors: list[str] = []
    errors.extend(validate_required_files())
    errors.extend(validate_task_template())
    errors.extend(validate_task_folders())
    status_errors, _active_task = validate_project_status()
    errors.extend(status_errors)
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
