# Isolation And Permissions

## Principle

`SWITCHBOARD.md` 记录意图；实际权限必须在系统设置中执行。不要把 Markdown 文件当作安全边界。

## Isolating ChatGPT Brain

如果需要隔离 Brain：

1. 在 `SWITCHBOARD.md` 中将 `GPT_READ` 改为 `OFF`。
2. 保持 `GPT_WRITE = OFF`。
3. 在 GitHub 或连接器设置中撤销 ChatGPT 的仓库读取能力。
4. 只向 Brain 提供 human 手动摘录的上下文。

## Isolating Codex Executor

如果需要隔离 Codex：

1. 将 `CODEX_READ` 改为 `OFF`。
2. 将 `CODEX_EXECUTE` 改为 `OFF`。
3. 将 `CODEX_CAN_PUSH` 改为 `OFF`。
4. 在 GitHub、本地机器和 CI 中撤销读取、执行、push 或 secret 权限。

## Secrets

默认 `SECRET_ACCESS = OFF`。只有 human 明确批准、任务确实需要、并且有最小权限和过期策略时，才可以开放 secret access。

## Network

默认 `NETWORK_ACCESS_FOR_CODEX = OFF_BY_DEFAULT`。Codex 不应在任务没有批准时访问外部网络。

## Branch Protection

推荐设置：

- `main` 禁止直接 push。
- 所有变更通过 PR。
- 必要检查必须通过。
- Human approval required before merge。
