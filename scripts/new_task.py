#!/usr/bin/env python3
"""Create the next task folder from tasks/TEMPLATE."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"
TEMPLATE_DIR = TASKS_DIR / "TEMPLATE"
PLACEHOLDER = "T-XXXX-short-name"
REQUIRED_TEMPLATE_FILES = [
    "brief.md",
    "codex_prompt.md",
    "acceptance.md",
    "result.md",
    "review.md",
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    slug = slug.strip("-")
    return slug or "new-task"


def existing_task_numbers() -> list[int]:
    numbers: list[int] = []
    if not TASKS_DIR.exists():
        return numbers
    for path in TASKS_DIR.iterdir():
        if not path.is_dir():
            continue
        match = re.fullmatch(r"T-(\d{4})-.+", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return numbers


def next_task_id(slug: str) -> str:
    next_number = max(existing_task_numbers(), default=0) + 1
    return f"T-{next_number:04d}-{slug}"


def validate_template() -> None:
    missing = [
        name for name in REQUIRED_TEMPLATE_FILES if not (TEMPLATE_DIR / name).is_file()
    ]
    if missing:
        joined = ", ".join(missing)
        raise FileNotFoundError(f"Template is missing required files: {joined}")


def replace_placeholder(path: Path, task_id: str) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace(PLACEHOLDER, task_id), encoding="utf-8", newline="\n")


def create_task(slug: str) -> Path:
    validate_template()
    task_id = next_task_id(slug)
    destination = TASKS_DIR / task_id
    if destination.exists():
        raise FileExistsError(f"Task already exists: {destination}")
    shutil.copytree(TEMPLATE_DIR, destination)
    for path in destination.rglob("*"):
        if path.is_file():
            replace_placeholder(path, task_id)
    return destination


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the next tasks/T-XXXX-slug folder from tasks/TEMPLATE."
    )
    parser.add_argument(
        "slug",
        help="Short task slug, for example update-docs or fix-validation.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        created = create_task(slugify(args.slug))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(created.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
