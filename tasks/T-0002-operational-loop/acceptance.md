# T-0002-operational-loop Acceptance

## Checklist Criteria

- [ ] `python scripts/validate_workspace.py` exits with code 0.
- [ ] `python scripts/show_context.py` exits with code 0.
- [ ] `python scripts/set_active_task.py T-0002-operational-loop --dry-run` exits with code 0.
- [ ] All non-template task folders contain `brief.md`, `codex_prompt.md`, `acceptance.md`, `result.md`, and `review.md`.
- [ ] `status/PROJECT_STATUS.md` points to an existing active task.
- [ ] `SWITCHBOARD.md` still contains all mandatory switches and their values are not made less restrictive.
- [ ] No third-party dependencies are added.
- [ ] `docs/TASK_LIFECYCLE.md` defines all canonical task states and transition expectations.
- [ ] `docs/DAILY_USE.md` gives human-facing Chinese workflows and copy-paste prompts.
- [ ] `docs/BRAIN_CODEX_HANDOFF.md` defines Brain -> Codex, Codex -> Brain, and Brain review formats.
- [ ] `tasks/T-0002-operational-loop/result.md` is updated after implementation.

## Validation Commands

```bash
python scripts/validate_workspace.py
python scripts/show_context.py
python scripts/set_active_task.py T-0002-operational-loop --dry-run
```
