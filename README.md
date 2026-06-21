# gpt-codex-control-plane

这是一个 GitHub-mediated ChatGPT Brain / Codex Executor 工作流模板。它采用 GitHub 仓库作为共享状态和 control plane，而不是 ChatGPT web 与 Codex 之间的直接原生实时耦合。 

## Architecture

ChatGPT web = Brain。Brain 负责规划、任务拆解、撰写 task brief、定义 acceptance criteria、审查 Codex 输出，并向 human 建议下一步决策。

Codex = Executor。Executor 负责在本地或 PR 分支中编辑文件、运行检查、提交结果报告，并把实现状态写回任务文件。

GitHub repo = shared state/control plane。仓库保存任务、决策、状态、review、PR 模板和审批记录，让 Brain、Executor 和 human 使用同一套可审计上下文。

Human = final approval and isolation gatekeeper。Human 决定是否合并、是否授权更多权限、是否隔离任一侧，以及是否允许访问 secrets、network 或 protected branches。

这个设计不提供 ChatGPT 与 Codex 的 direct native real-time coupling。所有交接都通过 GitHub issue、task folder、PR、review 文件和人类审批完成。

## File Tree Overview

```text
AGENTS.md
BRAIN.md
SWITCHBOARD.md
README.md
.gitignore
status/PROJECT_STATUS.md
decisions/decision_log.md
reviews/README.md
codex_outputs/README.md
human_approvals/README.md
docs/SETUP.md
docs/OPERATING_PROTOCOL.md
docs/ISOLATION_AND_PERMISSIONS.md
docs/COMMANDS.md
prompts/CODEX_CREATE_REPO_PROMPT.md
prompts/GPT_BRAIN_START_PROMPT.md
prompts/CODEX_TASK_PROMPT.md
prompts/GPT_REVIEW_PROMPT.md
tasks/TEMPLATE/
tasks/T-0001-bootstrap/
scripts/new_task.py
scripts/validate_workspace.py
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
```

## Quickstart

1. Human 先阅读 `SWITCHBOARD.md`，确认 isolation 和 permission 设置符合预期。
2. ChatGPT Brain 阅读 `BRAIN.md`、`status/PROJECT_STATUS.md` 和 `tasks/TEMPLATE/`，创建或完善任务。
3. Codex Executor 阅读 `AGENTS.md`、`SWITCHBOARD.md`、`status/PROJECT_STATUS.md` 和 active task folder。
4. Codex 按 task acceptance criteria 执行，并更新 `tasks/<TASK_ID>/result.md`。
5. ChatGPT Brain 或 human 阅读 `result.md`、PR diff 和 `review.md`，给出下一步建议。

## Daily Operation

日常使用请优先阅读：

- `docs/DAILY_USE.md`
- `docs/TASK_LIFECYCLE.md`
- `docs/BRAIN_CODEX_HANDOFF.md`

## Validation

运行：

```bash
python scripts/validate_workspace.py
```

如果需要创建新任务：

```bash
python scripts/new_task.py short-task-slug
```

## Standard Loop

```text
Human -> ChatGPT Brain -> task folder -> Codex -> result/PR -> ChatGPT review -> Human decision
```

Human 可以在任何步骤隔离 Brain 或 Executor。隔离意图记录在 `SWITCHBOARD.md`，实际权限必须在 GitHub、ChatGPT、Codex、本地机器和 CI 设置中执行。
