# T-0002-operational-loop Codex Prompt

你是 Codex Executor，请把仓库从静态模板升级为可日常使用的 GitHub-mediated Brain/Codex control plane。

执行前必须阅读 `AGENTS.md`、`BRAIN.md`、`SWITCHBOARD.md`、`status/PROJECT_STATUS.md`、`docs/OPERATING_PROTOCOL.md` 和 `tasks/T-0001-bootstrap/result.md`。

必须完成：

1. 创建 `tasks/T-0002-operational-loop/` 的五个任务文件。
2. 新增 `docs/TASK_LIFECYCLE.md`、`docs/DAILY_USE.md` 和 `docs/BRAIN_CODEX_HANDOFF.md`。
3. 新增 `scripts/show_context.py` 和 `scripts/set_active_task.py`。
4. 增强 `scripts/validate_workspace.py`，检查所有非模板任务、active task 一致性和 switch safety。
5. 更新 `status/PROJECT_STATUS.md`、`docs/COMMANDS.md`、`README.md` 和 `decisions/decision_log.md`。
6. 运行验收命令并更新 `result.md`。

约束：

- 只编辑 `brief.md` 中列出的 allowed files。
- 不放宽 `SWITCHBOARD.md` safety switches。
- 不添加第三方依赖。
- 不访问外部网络。
- 不提交 secrets、sessions、tokens、auth artifacts 或本地私密配置。
- `review.md` 必须留给 ChatGPT Brain 或 human。
