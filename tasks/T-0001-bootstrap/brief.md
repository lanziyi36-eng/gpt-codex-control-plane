# T-0001-bootstrap Brief

## Objective

验证 `gpt-codex-control-plane` 仓库模板结构完整，基础任务文件存在，mandatory switch names 可被脚本检查。

## Background

这是初始化任务，用来确认 Scheme A GitHub-mediated workflow 的核心文件、任务模板、GitHub issue forms、PR template 和本地验证脚本已经创建。

## Inputs

- 用户提供的 bootstrap repository requirements。
- `SWITCHBOARD.md`
- `status/PROJECT_STATUS.md`
- `tasks/TEMPLATE/`

## Outputs

- 完整仓库模板文件。
- 可运行的 `scripts/validate_workspace.py`。
- 更新后的 `tasks/T-0001-bootstrap/result.md`。
- 本地 git commit（如果 git 可用）。

## Allowed Files

- `AGENTS.md`
- `BRAIN.md`
- `SWITCHBOARD.md`
- `README.md`
- `.gitignore`
- `status/PROJECT_STATUS.md`
- `decisions/decision_log.md`
- `reviews/README.md`
- `codex_outputs/README.md`
- `human_approvals/README.md`
- `docs/**`
- `prompts/**`
- `tasks/TEMPLATE/**`
- `tasks/T-0001-bootstrap/**`
- `scripts/new_task.py`
- `scripts/validate_workspace.py`
- `.github/ISSUE_TEMPLATE/**`
- `.github/pull_request_template.md`

## Non-goals

- 不实现 ChatGPT 与 Codex 的 direct native real-time coupling。
- 不添加第三方依赖。
- 不访问外部网络。
- 不放宽 `SWITCHBOARD.md` 中的 safety switches。

## Risks

- Markdown switchboard 不是实际安全边界，需要 human 在真实平台权限中执行 enforcement。
- 当前模板只能检查结构，不验证 GitHub branch protection 或外部连接器权限。

## Human Notes

除必要英文文件、字段、命令和固定枚举值外，工作说明与总结使用中文。
