# Task Lifecycle

这个仓库使用显式 task state 来减少 Brain、Codex 和 human 之间的猜测。状态应该写在对应任务文件的顶部，例如 `tasks/<TASK_ID>/result.md` 或 `tasks/<TASK_ID>/review.md`，并在必要时同步 `status/PROJECT_STATUS.md` 的 active task。

## Canonical States

| State | Who May Set It | Record In | Required Evidence | Human Approval |
| --- | --- | --- | --- | --- |
| `PLANNED` | ChatGPT Brain or human | `brief.md` | Objective、background、allowed files 和 non-goals 已写清 | Not required |
| `READY_FOR_CODEX` | ChatGPT Brain or human | `brief.md` or issue | `codex_prompt.md` 和 `acceptance.md` 已可执行 | Required if permissions expand |
| `IN_PROGRESS` | Codex Executor | `result.md` | Codex 已读取 required context 并开始执行 | Not required |
| `COMPLETED_BY_CODEX` | Codex Executor | `result.md` | Summary、files changed、commands run、validation result 和 risks 已记录 | Not sufficient for merge |
| `FAILED_BY_CODEX` | Codex Executor | `result.md` | 失败命令、错误原因、未完成项和建议下一步已记录 | Human decides recovery |
| `PENDING_BRAIN_REVIEW` | Codex Executor, ChatGPT Brain, or human | `review.md` | Codex result 或 PR 已准备好 review | Not required |
| `REQUEST_CHANGES` | ChatGPT Brain or human | `review.md` | 必须修改项清单和理由 | Human may override |
| `MERGE_APPROVED` | Human, or Brain as recommendation only | `review.md` and approval note if needed | 验收通过、风险可接受、权限未被放宽 | Human approval required before merge |
| `REJECTED` | Human, or Brain as recommendation only | `review.md` | 拒绝理由和替代方向 | Human decision required |
| `BLOCKED_NEEDS_HUMAN_DECISION` | Codex Executor, ChatGPT Brain, or human | `result.md` or `review.md` | 阻塞条件、需要 human 决策的问题和可选路径 | Human decision required |
| `CLOSED` | Human | `review.md` or task note | 已合并、拒绝或无需继续，后续任务已指明 | Human decision required |

## State Ownership

Codex 只能声明自己的执行状态，例如 `IN_PROGRESS`、`COMPLETED_BY_CODEX`、`FAILED_BY_CODEX` 或 `BLOCKED_NEEDS_HUMAN_DECISION`。Codex 不应把 Brain review 写成完成，也不应自行宣称 merge 已获最终批准。

ChatGPT Brain 可以规划任务、提出 review decision，并建议 `MERGE`、`REQUEST_CHANGES`、`REJECT` 或 `BLOCKED_NEEDS_HUMAN_DECISION`。如果 Brain 写 `MERGE_APPROVED`，它仍然只是建议，除非 human 明确批准。

Human 可以设置任何最终性状态，包括授权权限变化、合并、拒绝、关闭任务和隔离 Brain 或 Codex。

## Evidence Rules

每个任务至少应保留五个文件：`brief.md`、`codex_prompt.md`、`acceptance.md`、`result.md` 和 `review.md`。Codex 完成后，`result.md` 必须包含执行摘要、文件变更、命令、验证结果和剩余风险。Brain review 后，`review.md` 必须包含明确 decision 和理由。

如果任务涉及 secrets、network、branch protection、直接写入 main、自动 review 或其他权限扩大，human approval 必须记录在 `human_approvals/`，并在相关 task 或 PR 中链接。

## Moving To The Next Task

当前任务完成后，human 或 Brain 先确认 `review.md`。如果结果是 `REQUEST_CHANGES`，active task 保持不变，Codex 继续修复同一任务或同一 PR。如果结果是 `MERGE` 或 human 批准关闭任务，human 或 Brain 创建下一项任务，并运行：

```bash
python scripts/set_active_task.py T-XXXX-next-task
```

切换 active task 后，运行：

```bash
python scripts/show_context.py
python scripts/validate_workspace.py
```

确认 `PROJECT_STATUS.md`、task folder 和 switchboard 仍然一致。
