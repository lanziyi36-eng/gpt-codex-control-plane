# T-0002-operational-loop Brief

## Objective

Upgrade the control plane so that human, ChatGPT Brain, and Codex Executor can run a repeatable day-to-day loop without copying large amounts of context manually.

## Background

T-0001-bootstrap 已经创建 Scheme A GitHub-mediated control plane 的基础结构。现在需要把静态模板升级为日常可用的操作流程：明确 task lifecycle、提供 Brain/Codex handoff 格式、增加上下文摘要脚本、增强 workspace validation，并给 human 一份可以照着使用的中文手册。

## Inputs

- `AGENTS.md`
- `BRAIN.md`
- `SWITCHBOARD.md`
- `status/PROJECT_STATUS.md`
- `docs/OPERATING_PROTOCOL.md`
- `tasks/T-0001-bootstrap/result.md`
- 用户提供的 T-0002-operational-loop 任务说明

## Outputs

- `docs/TASK_LIFECYCLE.md`
- `docs/DAILY_USE.md`
- `docs/BRAIN_CODEX_HANDOFF.md`
- `scripts/show_context.py`
- `scripts/set_active_task.py`
- 更新后的 `scripts/validate_workspace.py`
- 更新后的 `status/PROJECT_STATUS.md`
- 更新后的 `docs/COMMANDS.md`
- 如有需要，更新 `README.md` 的 Daily operation 链接
- `decisions/decision_log.md` 中新增 D-0002
- 完成后的 `tasks/T-0002-operational-loop/result.md`

## Allowed Files

- `docs/TASK_LIFECYCLE.md`
- `docs/DAILY_USE.md`
- `docs/BRAIN_CODEX_HANDOFF.md`
- `docs/COMMANDS.md`
- `README.md`
- `status/PROJECT_STATUS.md`
- `decisions/decision_log.md`
- `scripts/show_context.py`
- `scripts/set_active_task.py`
- `scripts/validate_workspace.py`
- `tasks/T-0002-operational-loop/*`

## Non-goals

- Do not build a web app.
- Do not add OpenAI API automation.
- Do not add GitHub Actions.
- Do not add third-party packages.
- Do not alter repository permissions.
- Do not enable network or secrets.

## Risks

- Markdown 文件只能表达流程和意图，不能替代 GitHub、Codex、ChatGPT、CI 或本地系统的真实权限设置。
- 如果 human 或 Brain 手动编辑 `PROJECT_STATUS.md` 而没有同步 task 文件，active task 可能失真，需要使用 `scripts/show_context.py` 和 `scripts/set_active_task.py` 修复。
- 本任务不创建线上 PR，因为执行约束要求不使用外部网络访问。

## Human Notes

本任务使用中文编写 human-facing 操作文档，同时保留 task state、switch、command、decision value 等英文技术标签。
