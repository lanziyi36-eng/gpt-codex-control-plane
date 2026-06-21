# T-0001-bootstrap Acceptance

## Checklist Criteria

- [ ] Required repository structure 已创建。
- [ ] `README.md` 解释 ChatGPT Brain、Codex Executor、GitHub control plane、Human gatekeeper 和 Scheme A。
- [ ] `AGENTS.md` 包含 Codex Executor 规则和 review guidelines。
- [ ] `BRAIN.md` 包含 Brain 责任和四种 review recommendation。
- [ ] `SWITCHBOARD.md` 包含所有 mandatory switch names 和初始值。
- [ ] `status/PROJECT_STATUS.md` 的 active task 是 `T-0001-bootstrap`。
- [ ] `tasks/TEMPLATE/` 包含五个 required task files。
- [ ] `scripts/new_task.py` 只使用 Python standard library，并能从 template 创建下一个 task folder。
- [ ] `scripts/validate_workspace.py` 只使用 Python standard library，并能检查 required files、template files 和 switch names。
- [ ] `tasks/T-0001-bootstrap/result.md` 已更新。
- [ ] 未添加第三方依赖。
- [ ] 未访问外部网络。
- [ ] 未放宽 `SWITCHBOARD.md` safety switches。

## Validation Commands

```bash
python scripts/validate_workspace.py
```
