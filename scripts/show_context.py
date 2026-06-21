#!/usr/bin/env python3
"""Print the current GPT-Codex control plane context."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_TASK_FILES = [
    "brief.md",
    "codex_prompt.md",
    "acceptance.md",
    "result.md",
    "review.md",
]

SWITCH_NAMES = [
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


def find_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "status" / "PROJECT_STATUS.md").is_file() and (
            candidate / "SWITCHBOARD.md"
        ).is_file():
            return candidate
    return Path(__file__).resolve().parents[1]


ROOT = find_root()


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


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def main() -> int:
    status_path = ROOT / "status" / "PROJECT_STATUS.md"
    switchboard_path = ROOT / "SWITCHBOARD.md"
    if not status_path.is_file():
        return fail("status/PROJECT_STATUS.md is missing")
    if not switchboard_path.is_file():
        return fail("SWITCHBOARD.md is missing")

    status = parse_markdown_table(status_path.read_text(encoding="utf-8"))
    active_task = status.get("Active task", "").strip()
    if not active_task:
        return fail("Active task is missing from status/PROJECT_STATUS.md")

    task_dir = ROOT / "tasks" / active_task
    if not task_dir.is_dir():
        return fail(f"Active task folder does not exist: tasks/{active_task}")

    switches = parse_markdown_table(switchboard_path.read_text(encoding="utf-8"))
    missing_task_files = [
        name for name in REQUIRED_TASK_FILES if not (task_dir / name).is_file()
    ]

    print("GPT-Codex Control Plane Context")
    print()
    print(f"Project name: {status.get('Project name', 'UNKNOWN')}")
    print(f"Active task: {active_task}")
    print(f"Current mode: {status.get('Current mode', 'UNKNOWN')}")
    print(f"Next expected action: {status.get('Next expected action', 'UNKNOWN')}")
    print()
    print("Switchboard:")
    for name in SWITCH_NAMES:
        print(f"- {name}: {switches.get(name, 'MISSING')}")
    print()
    print(f"Active task folder exists: YES ({task_dir.relative_to(ROOT).as_posix()})")
    if missing_task_files:
        print("Active task required files: MISSING")
        for name in missing_task_files:
            print(f"- missing: {name}")
    else:
        print("Active task required files: OK")

    return 0 if not missing_task_files else 1


if __name__ == "__main__":
    raise SystemExit(main())
