# Setup

## 1. Create Repository

创建一个 GitHub repository，例如 `gpt-codex-control-plane`。初始化后保留 `main` 作为 protected branch，并要求通过 PR 合并。

## 2. Configure Permissions

在 GitHub、ChatGPT、Codex、本地机器和 CI 中分别设置权限。`SWITCHBOARD.md` 是共享状态说明，不是实际 enforcement。

推荐初始状态：

- ChatGPT Brain 可以读取任务和 PR 摘要，但不能直接写仓库。
- Codex 可以读取仓库并在 PR branch 执行任务。
- Codex 不能直接 push 到 `main`。
- Secrets 和 network 默认关闭。

## 3. Validate Workspace

运行：

```bash
python scripts/validate_workspace.py
```

验证通过后，Human 可以让 Brain 创建下一项任务，或让 Codex 执行 active task。

## 4. First Loop

初始 active task 是 `T-0001-bootstrap`。它的目标是验证仓库结构和基础脚本可用。
