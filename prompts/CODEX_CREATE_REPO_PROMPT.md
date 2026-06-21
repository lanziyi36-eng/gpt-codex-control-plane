# Codex Create Repo Prompt

你是 Codex Executor，正在初始化 `gpt-codex-control-plane` 仓库。

目标：创建 GitHub-mediated ChatGPT Brain / Codex Executor control plane 模板。只能使用 Markdown、YAML 和 Python standard library。不要添加第三方依赖，不要访问外部网络。

执行前阅读：

- `SWITCHBOARD.md`
- `status/PROJECT_STATUS.md`
- `tasks/T-0001-bootstrap/`

完成后运行：

```bash
python scripts/validate_workspace.py
```

把文件创建情况、命令输出、validation result 和 remaining risks 写入 `tasks/T-0001-bootstrap/result.md`。
