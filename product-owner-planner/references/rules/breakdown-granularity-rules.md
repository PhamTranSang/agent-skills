# Breakdown Granularity Rules

Use these rules to decide when to create milestone folders, story files, and task breakdowns.

## Milestone as Folder

Create a milestone folder when:

- the phase has more than one distinct delivery slice
- the slice crosses multiple concerns or workstreams
- the slice needs its own execution order
- the slice will contain multiple stories or tasks

Do not create a milestone folder if the work is a single small story.

## Story as File

Create a story file when:

- the work has a user-visible outcome
- the work can be completed and validated independently
- the story would be too large or too noisy inside another story file
- the story needs its own scenario and acceptance criteria

Keep multiple user outcomes out of the same story file.

## Story to Task Split

Split a story into tasks when:

- the story requires multiple implementation steps
- the work spans backend, frontend, infra, test, or migration concerns
- the story has hidden dependencies
- the story needs explicit wiring, config, test, or regression coverage

Do not add tasks if the story is already simple enough to execute directly.

## Threshold Heuristics

- If one item would take more than one meaningful implementation step, split it.
- If a ticket mixes user-facing behavior with unrelated technical work, split it.
- If a story needs a spike to answer a blocking question, create the spike first or alongside it.
- If a milestone only contains one small story, collapse the milestone into the story file.

## Preferred Shape

- Small phase: `README.md` + 1-2 story files
- Medium phase: `README.md` + milestone folders + story files + tasks
- Large phase: `README.md` + multiple priority folders + story files + tasks + spikes
