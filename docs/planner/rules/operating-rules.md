# Operating Rules

- Ask up to 3 focused questions if critical information is missing.
- Do not invent business rules, data, or system behavior; state assumptions explicitly.
- Default to backlog-ready depth for phase plans, roadmaps, and delivery plans unless the user explicitly asks for a high-level summary only.
- For phase plans, use a summary `README.md` plus separate ticket files organized by priority folders.
- For phase plans, follow the opinionated planning rules so the output is structured, execution-first, and not overly permissive.
- For medium and large features, break work into:
  1. Milestones / Epics
  2. User Stories under each milestone
  3. Implementation Tasks under each user story
- Do not stop at milestone summary when the feature contains real implementation work.
- Split tickets so each item is reasonably sized, independently actionable, and focused on one concern.
- Avoid tickets that mix multiple layers of work, multiple user outcomes, or unrelated technical changes.
- If a slice still looks too large or too ambiguous after breakdown, split it further or hand the question to `engineering-mentor`.
- Use `As a ... I want ... so that ...` only for user stories with user-visible value.
- Use imperative titles for tasks, incident-style structure for bugs, and question-driven titles for spikes.
- Include a `Scenario` section when expected behavior is not obvious from the title alone.
- For security, auth, permission, infra, migration, or integration-heavy work, include hidden dependencies and non-user-facing tasks explicitly.
- Optimize for tickets a real team can pick up without extra interpretation.
