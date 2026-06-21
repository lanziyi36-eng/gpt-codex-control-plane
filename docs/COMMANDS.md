# Commands

## Validate Workspace

```bash
python scripts/validate_workspace.py
```

用途：检查 required files、task template 文件和 mandatory switch names。

在日常使用中，它还会检查所有非模板 task folder 是否包含五个任务文件、`status/PROJECT_STATUS.md` 是否指向真实 active task，以及 `SWITCHBOARD.md` 的关键 safety values 是否没有被放宽。

## Show Current Context

```bash
python scripts/show_context.py
```

用途：快速打印 project name、active task、current mode、next expected action、关键 switch 值，以及 active task 文件夹是否完整。把任务交给 Brain 或 Codex 前，建议先运行这个命令。

## Dry Run Active Task Change

```bash
python scripts/set_active_task.py T-0002-operational-loop --dry-run
```

用途：检查某个 task folder 是否存在且包含五个必需文件，并预览会如何修改 `status/PROJECT_STATUS.md`。这一步不会写文件。

## Set Active Task

```bash
python scripts/set_active_task.py T-0002-operational-loop
```

用途：在确认 dry-run 无误后，把 `status/PROJECT_STATUS.md` 的 `Active task` 行切换到指定任务。

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
