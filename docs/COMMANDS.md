# Commands

## Validate Workspace

```bash
python scripts/validate_workspace.py
```

用途：检查 required files、task template 文件和 mandatory switch names。

## Create New Task

```bash
python scripts/new_task.py short-task-slug
```

用途：扫描已有 `tasks/T-*` 目录，创建下一个 `T-XXXX-short-task-slug` 文件夹，并从 `tasks/TEMPLATE/` 复制五个任务文件。

## Git Status

```bash
git status --short --branch
```

用途：查看当前分支和未提交变更。

## Commit Bootstrap

```bash
git add AGENTS.md BRAIN.md SWITCHBOARD.md README.md .gitignore status decisions reviews codex_outputs human_approvals docs prompts tasks scripts .github
git commit -m "[T-0001] Initialize GPT-Codex control plane"
```

用途：提交模板初始化结果。不要把 secrets、sessions、auth artifacts 或无关本地文件加入提交。
