# Switchboard

这个文件是 human、ChatGPT Brain、Codex Executor 共享的可见控制面。它表达当前意图和约束，但本身不是安全边界。

| Switch | Initial Value |
| --- | --- |
| GPT_READ | ON |
| GPT_WRITE | OFF |
| CODEX_READ | ON |
| CODEX_EXECUTE | ON |
| CODEX_CAN_PUSH | PR_BRANCH_ONLY |
| AUTO_REVIEW | OFF |
| HUMAN_APPROVAL_REQUIRED | YES |
| NETWORK_ACCESS_FOR_CODEX | OFF_BY_DEFAULT |
| SECRET_ACCESS | OFF |

## Isolation Controls

要隔离 ChatGPT Brain：

- 将 `GPT_READ` 设为 `OFF`，并在 ChatGPT/GitHub 权限设置中撤销或暂停其仓库读取能力。
- 保持 `GPT_WRITE = OFF`，不要让 Brain 直接修改仓库状态。
- 让 Brain 只通过 human 提供的摘录、PR diff 或 review request 工作。

要隔离 Codex Executor：

- 将 `CODEX_READ` 设为 `OFF`，并在 Codex/GitHub 权限设置中撤销或暂停仓库读取能力。
- 将 `CODEX_EXECUTE` 设为 `OFF`，并停止本地命令执行或 CI 执行权限。
- 将 `CODEX_CAN_PUSH` 设为 `OFF`，并在 GitHub 分支保护中阻止 Codex push。
- 保持 `SECRET_ACCESS = OFF`，不要向 Codex 暴露 secrets。

## Enforcement Note

实际 enforcement 需要在 GitHub、ChatGPT、Codex、本地机器、CI 和 secret manager 的权限设置中完成。这个文件只提供共享状态、审计线索和人工操作指南，不能替代真实权限控制。
