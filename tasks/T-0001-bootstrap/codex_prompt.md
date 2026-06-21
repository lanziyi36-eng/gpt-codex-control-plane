# T-0001-bootstrap Codex Prompt

你是 Codex Executor。请初始化并验证 `gpt-codex-control-plane` 仓库模板。

必须完成：

1. 创建 required repository structure。
2. 不添加第三方依赖。
3. 不访问外部网络。
4. 不放宽 `SWITCHBOARD.md` safety switches。
5. 运行：

```bash
python scripts/validate_workspace.py
```

6. 更新 `tasks/T-0001-bootstrap/result.md`，记录 validation result、files created、commands run 和 remaining risks。
7. 如果 git 可用，创建提交：

```bash
git commit -m "[T-0001] Initialize GPT-Codex control plane"
```

将 `review.md` 留给 ChatGPT Brain 或 human。
