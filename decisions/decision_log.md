# Decision Log

## Decision Entry Format

```text
ID:
Date:
Status:
Decision:
Context:
Options considered:
Consequences:
Owner:
Review date:
```

## D-0001

ID: D-0001  
Date: 2026-06-21  
Status: Accepted  
Decision: Adopt Scheme A GitHub-mediated workflow.  
Context: Human needs a controllable workflow where ChatGPT web acts as Brain, Codex acts as Executor, and GitHub stores shared task state, review state, and approval state.  
Options considered: Direct native real-time coupling; ad hoc chat handoff; Scheme A GitHub-mediated workflow.  
Consequences: Brain and Executor can be isolated independently, all work is auditable through files and PRs, and human approval remains the final gate. The tradeoff is slower handoff compared with direct coupling.  
Owner: Human  
Review date: After the first complete Brain -> Codex -> Review -> Human decision loop.

## D-0002

ID: D-0002
Date: 2026-06-21
Status: Accepted
Decision: Adopt an explicit task lifecycle and operational handoff protocol before using the control plane for real project work.
Context: The bootstrap repository proves the structure exists, but daily use requires state transitions, active-task consistency checks, and a repeatable Brain-Codex handoff format.
Options considered: Continue with static template files; rely on ad hoc chat-only instructions; add explicit lifecycle, handoff, and validation tooling.
Consequences: Future work should be routed through task folders, result files, review files, and PRs rather than ad hoc chat-only instructions. This adds a small amount of process, but makes state recoverable and reviewable.
Owner: Human
Review date: After the first real project task completes through the full lifecycle.
