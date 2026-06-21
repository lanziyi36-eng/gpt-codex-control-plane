#!/usr/bin/env python3
"""Set the active task row in status/PROJECT_STATUS.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_TASK_FILES = [
    "brief.md",
    "codex_prompt.md",
    "acceptance.md",
    "result.md",
    "review.md",
]


def find_root() -> Path:
    current = Path(__file__).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / "status" / "PROJECT_STATUS.md").is_file():
            return candidate
    return Path(__file__).resolve().parents[1]


ROOT = find_root()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update the Active task row in status/PROJECT_STATUS.md."
    )
    parser.add_argument("task_id", help="Task directory name, for example T-0002-work.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the change without writing status/PROJECT_STATUS.md.",
    )
    return parser.parse_args(argv)


def validate_task_id(task_id: str) -> str | None:
    if "/" in task_id or "\\" in task_id:
        return "Task ID must be a directory name, not a path."
    if not re.fullmatch(r"T-\d{4}-[A-Za-z0-9][A-Za-z0-9_-]*", task_id):
        return "Task ID must look like T-0002-short-slug."
    return None


def validate_task_folder(task_id: str) -> list[str]:
    errors: list[str] = []
    task_dir = ROOT / "tasks" / task_id
    if not task_dir.is_dir():
        return [f"Task directory does not exist: tasks/{task_id}"]
    for name in REQUIRED_TASK_FILES:
        if not (task_dir / name).is_file():
            errors.append(f"Task is missing required file: tasks/{task_id}/{name}")
    return errors


def update_active_task_line(text: str, task_id: str) -> tuple[str, str | None]:
    current_value: str | None = None
    updated_lines: list[str] = []
    replaced = False

    for line in text.splitlines():
        if line.strip().startswith("|"):
            parts = line.split("|")
            if len(parts) >= 4 and parts[1].strip().lower() == "active task":
                current_value = parts[2].strip()
                parts[2] = f" {task_id} "
                line = "|".join(parts)
                replaced = True
        updated_lines.append(line)

    if not replaced:
        raise ValueError("Active task row was not found in status/PROJECT_STATUS.md")

    return "\n".join(updated_lines) + "\n", current_value


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    task_id_error = validate_task_id(args.task_id)
    if task_id_error:
        print(f"ERROR: {task_id_error}", file=sys.stderr)
        return 1

    errors = validate_task_folder(args.task_id)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    status_path = ROOT / "status" / "PROJECT_STATUS.md"
    if not status_path.is_file():
        print("ERROR: status/PROJECT_STATUS.md is missing", file=sys.stderr)
        return 1

    try:
        original = status_path.read_text(encoding="utf-8")
        updated, current_value = update_active_task_line(original, args.task_id)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Current active task: {current_value or 'UNKNOWN'}")
    print(f"Requested active task: {args.task_id}")
    if args.dry_run:
        if updated == original:
            print("Dry run: no change needed.")
        else:
            print("Dry run: status/PROJECT_STATUS.md would be updated.")
        return 0

    status_path.write_text(updated, encoding="utf-8", newline="\n")
    print("Updated status/PROJECT_STATUS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
