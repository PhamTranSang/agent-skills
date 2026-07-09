# Opinionated Planning Rules

Use these rules to keep phase plans strict, consistent, and execution-first.

## File Roles

- `README.md` is summary only.
- Ticket files contain the executable work.
- Spike files are used when a decision is unresolved.

## Priority Discipline

- `p0` means must unblock or fix first.
- `p1` means core delivery for the phase.
- `p2` means important but not blocking.
- `p3` means nice-to-have or can slip.

## Split Discipline

- One file should represent one concern.
- Do not mix user-facing work and unrelated technical work in the same file.
- Do not mix multiple user outcomes in the same story.
- If a ticket still feels broad after breakdown, split it again.

## Decision Discipline

- If a choice affects scope, sequencing, or feasibility and remains unresolved, create a spike.
- Do not leave execution-critical uncertainty only in open questions.
- Open questions are for product ambiguity that does not need a separate investigative ticket.

## Handoff Discipline

- `engineering-mentor` validates feasibility, sequencing, and implementation risk.
- The planner owns the ticket shape and execution order.
- If the plan is too loose to hand to dev, tighten it before presenting it.
