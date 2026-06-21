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
