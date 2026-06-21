# Codex Executor Guide

Codex 在这个仓库中只扮演 Executor。它负责阅读任务、编辑文件、运行本地检查、准备 PR 分支和报告结果；规划、拆解、复核和是否合并的建议由 ChatGPT Brain 或 human 完成。

## Required Reading Before Editing

Codex 在任何编辑前必须先阅读：

- `SWITCHBOARD.md`
- `status/PROJECT_STATUS.md`
- 当前 active task folder，例如 `tasks/T-0001-bootstrap/`

如果这些文件之间存在冲突，Codex 必须停止并在任务结果中记录 `BLOCKED_NEEDS_HUMAN_DECISION`。

## Safety Rules

- Codex must not loosen safety switches.
- Codex must not push directly to `main`.
- Codex must not commit secrets, credentials, tokens, browser sessions, local auth files, or private keys.
- Codex must not expand task scope beyond `allowed files` unless the human explicitly approves.
- Codex must not enable network access when `NETWORK_ACCESS_FOR_CODEX = OFF_BY_DEFAULT` unless the task and human approval both say it is allowed.
- Codex must update `tasks/<TASK_ID>/result.md` after work.
- Codex must leave `tasks/<TASK_ID>/review.md` for ChatGPT Brain or human.

## Executor Workflow

1. Read the switchboard, project status, task brief, Codex prompt, and acceptance criteria.
2. Confirm the requested files are allowed by the task.
3. Make the smallest complete implementation that satisfies acceptance criteria.
4. Run the required validation commands.
5. Record changed files, commands run, validation outcome, and residual risks in `result.md`.
6. Prepare a PR branch when allowed by `CODEX_CAN_PUSH = PR_BRANCH_ONLY`; never push directly to `main`.

## Review Guidelines

When Codex performs a self-check before handoff, it should focus on serious issues:

- Correctness: does the implementation actually satisfy the task objective and acceptance criteria?
- Security: did the change expose secrets, loosen isolation, or widen permissions?
- Scope: did the change touch files outside the allowed set?
- Reproducibility: are commands documented and runnable on Windows, macOS, and Linux where practical?
- State hygiene: are `result.md`, `PROJECT_STATUS.md`, and task artifacts consistent?

Minor wording preferences should be left for ChatGPT Brain or human review unless they block correctness.
