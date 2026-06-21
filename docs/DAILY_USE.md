# Daily Use

这份手册面向 human。你可以把它当成每天打开仓库后照着做的操作卡片。仓库里的 Markdown 文件负责记录共享状态，真正的权限控制仍然要在 GitHub、ChatGPT、Codex、本地机器、CI 和 secret 设置里完成。

## 1. Starting A New Task With ChatGPT Brain

当你有一个新目标，先让 ChatGPT Brain 把它拆成可执行任务。建议先运行或查看：

```bash
python scripts/show_context.py
```

复制给 ChatGPT Brain 的提示：

```text
作为 ChatGPT Brain，请阅读 lanziyi36-eng/gpt-codex-control-plane 的 BRAIN.md、SWITCHBOARD.md、status/PROJECT_STATUS.md 和当前 active task。请基于下面目标创建下一个任务文件夹，写清 brief.md、codex_prompt.md、acceptance.md、result.md 和 review.md。不要声称执行命令或 push commits。

目标：
<在这里写你的目标>
```

Brain 产出的任务应该有明确 objective、allowed files、non-goals、acceptance criteria 和 validation commands。

## 2. Sending A Task To Codex

当任务已经是 `READY_FOR_CODEX`，把具体任务交给 Codex Executor。你可以复制：

```text
作为 Codex Executor，请阅读 AGENTS.md、SWITCHBOARD.md、status/PROJECT_STATUS.md 和 tasks/T-XXXX-...。只编辑任务允许的文件，执行 acceptance.md 中的 validation commands，完成后更新 result.md，并把 review.md 留给 ChatGPT Brain 或 human。不要放宽 safety switches，不要添加 secrets，不要访问外部网络。
```

如果需要先切换 active task：

```bash
python scripts/set_active_task.py T-XXXX-task-slug --dry-run
python scripts/set_active_task.py T-XXXX-task-slug
```

## 3. Reviewing A Codex Result With ChatGPT Brain

Codex 完成后，不要直接把结果当成可合并。先让 Brain review `result.md`、PR diff 和验证输出。

复制给 ChatGPT Brain 的提示：

```text
作为 ChatGPT Brain，请 review tasks/T-XXXX-.../result.md、acceptance.md、相关 PR diff 或文件变更摘要。请重点检查 correctness、安全、scope、权限和可复现性。最后必须推荐 MERGE、REQUEST_CHANGES、REJECT 或 BLOCKED_NEEDS_HUMAN_DECISION，并把结论写成 review.md 可使用的格式。
```

Brain 的 `MERGE` 仍然是建议。最终是否合并由 human 决定。

## 4. Asking Codex To Fix A PR

如果 Brain 或 human 要求修改，继续使用同一个 task，避免新开无关任务。

复制给 Codex 的提示：

```text
作为 Codex Executor，请阅读 tasks/T-XXXX-.../review.md、result.md 和 acceptance.md。只处理 review.md 中的 required changes，保留原任务 scope，运行 validation commands，并更新 result.md 的修复记录。不要直接 push 到 main。
```

如果修改扩大了 allowed files，先让 human 明确批准，并把批准记录到 `human_approvals/`。

## 5. Pausing ChatGPT Brain

如果你想暂时隔离 Brain：

1. 在真实权限设置中暂停 ChatGPT 或连接器的仓库读取能力。
2. 在 `SWITCHBOARD.md` 中记录 `GPT_READ = OFF` 的意图。
3. 保持 `GPT_WRITE = OFF`。
4. 只把你手动摘录的必要上下文发给 Brain。

注意：改 Markdown 不会自动限制权限，真实 enforcement 必须在平台设置中完成。

## 6. Pausing Codex Executor

如果你想暂停 Codex：

1. 在真实权限设置中暂停 Codex 的仓库读取、命令执行或 push 权限。
2. 在 `SWITCHBOARD.md` 中记录 `CODEX_READ = OFF`、`CODEX_EXECUTE = OFF` 或 `CODEX_CAN_PUSH = OFF` 的意图。
3. 确认 `SECRET_ACCESS = OFF`。
4. 不要把 tokens、private keys、browser sessions 或本地 auth files 放进仓库。

如果只是想让 Codex 不 push，可以保留读取权限，但把 GitHub 权限和 branch protection 设置好。

## 7. Recovering When PROJECT_STATUS.md And Task Files Disagree

如果 `PROJECT_STATUS.md` 说 active task 是一个任务，但文件夹不存在，或者任务文件不完整，先运行：

```bash
python scripts/show_context.py
python scripts/validate_workspace.py
```

如果 active task 写错了，先 dry run：

```bash
python scripts/set_active_task.py T-XXXX-correct-task --dry-run
```

确认输出正确后再写入：

```bash
python scripts/set_active_task.py T-XXXX-correct-task
```

如果 task 文件缺失，不要硬切 active task。先让 Brain 或 human 补齐 `brief.md`、`codex_prompt.md`、`acceptance.md`、`result.md` 和 `review.md`。

## 8. What Not To Put In This Repository

不要放入 secrets、API keys、tokens、private keys、browser cookies、session files、本地 auth files、`.env`、客户隐私数据、未脱敏日志、个人证件信息或任何不能公开给当前仓库协作者的材料。

不要把这个仓库当作自动执行系统。它是 GitHub-mediated control plane，主要用于任务拆解、状态同步、审计和 human approval。
