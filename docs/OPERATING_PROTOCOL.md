# Operating Protocol

## Roles

Human 是最终审批者和 isolation gatekeeper。ChatGPT web 是 Brain。Codex 是 Executor。GitHub repository 是 shared state/control plane。

## Standard Loop

```text
Human -> ChatGPT Brain -> task folder -> Codex -> result/PR -> ChatGPT review -> Human decision
```

## Task Creation

Brain 或 human 使用 `tasks/TEMPLATE/` 创建任务。任务必须包含：

- `brief.md`
- `codex_prompt.md`
- `acceptance.md`
- `result.md`
- `review.md`

也可以运行：

```bash
python scripts/new_task.py short-task-slug
```

## Execution

Codex 在执行前读取 `AGENTS.md`、`SWITCHBOARD.md`、`status/PROJECT_STATUS.md` 和 active task folder。Codex 只编辑 task 允许的文件，运行 acceptance 中列出的 validation commands，并把结果写入 `result.md`。

## Review

ChatGPT Brain 或 human 阅读 `result.md`、PR diff 和检查输出，然后在 `review.md` 中给出建议：

- `MERGE`
- `REQUEST_CHANGES`
- `REJECT`
- `BLOCKED_NEEDS_HUMAN_DECISION`

## Human Decision

Human 根据 review、风险和权限状态决定是否合并、要求修改、拒绝、扩大权限或隔离任一侧。
