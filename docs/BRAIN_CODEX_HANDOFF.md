# Brain Codex Handoff

这个文件定义 Brain、Codex 和 human 之间的最小交接格式。交接内容可以写在 task folder、GitHub issue、PR description 或聊天消息中，但结构应保持一致。

## Brain -> Codex Handoff

Required sections:

```text
Task ID:
Objective:
Files to read first:
Allowed files:
Acceptance criteria:
Constraints:
Expected result.md content:
```

`Task ID` 必须匹配 `tasks/<TASK_ID>/`。`Files to read first` 至少包括 `AGENTS.md`、`SWITCHBOARD.md`、`status/PROJECT_STATUS.md` 和当前 task folder。`Allowed files` 应尽量窄。`Acceptance criteria` 必须包含可运行的 validation commands。`Constraints` 应明确 network、secrets、dependencies、branch 和 permission 限制。

Expected `result.md` content:

- Status
- Summary
- Files changed
- Commands run
- Validation result
- Remaining risks

## Codex -> Brain Handoff

Required sections:

```text
Task ID:
Summary:
Files changed:
Commands run:
Validation output:
PR or branch:
Risks:
Questions for Brain/human:
```

Codex 必须说明自己实际运行了哪些命令，以及验证是否通过。若没有创建线上 PR，应明确写出原因，例如 no network access、no remote permission 或 local branch only。Codex 不应声称 Brain review 已完成。

## Brain Review Format

Required decision:

- `MERGE`
- `REQUEST_CHANGES`
- `REJECT`
- `BLOCKED_NEEDS_HUMAN_DECISION`

Recommended review body:

```text
Task ID:
Decision:
Rationale:
Required changes:
Optional suggestions:
Human approval needed:
```

Brain 应优先检查 correctness、安全、scope、权限和可复现性。Human approval required 的事项包括合并 PR、放宽 switches、访问 secrets、启用 network、直接 push 到 protected branch 或跳过验收命令。
