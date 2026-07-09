# Phase Plan Structure

When the user asks for a phase plan, roadmap, or delivery plan:

- Use `README.md` as the summary file for the phase.
- Put ticket breakdown into separate files under priority folders.
- Do not place full user stories, tasks, bugs, or spikes inside the summary file.
- Keep the summary focused on:
  - problem summary
  - goals
  - scope
  - non-goals
  - assumptions
  - dependencies
  - risks and mitigations
  - open questions
  - handoff notes for `engineering-mentor`

## Required Folder Layout

Use a structure like:

- `phase-x/README.md`
- `phase-x/p0-.../`
- `phase-x/p1-.../`
- `phase-x/p2-.../`
- `phase-x/p3-.../`

Use priority folders to group tickets and show execution order.

Priority meaning:

- `p0`: must unblock or fix first
- `p1`: core delivery for the phase
- `p2`: important but not blocking
- `p3`: nice-to-have or can slip

## Ticket Breakdown Rule

Each ticket file should contain one of:

- user story
- task
- spike
- bug

For large features:

- milestone / epic -> folder
- user story -> file
- implementation task -> file or section under the story file
- spike -> separate file

Use the breakdown granularity rules to decide when a milestone should become a folder, when a story should become a file, and when a story should split into tasks.

## Split Rule

If a phase contains real implementation work:

- do not stop at milestone summary
- always break down to executable tickets
- if a decision is unresolved, create a spike file instead of keeping it in open questions

## Naming Rule

- Summary file must be `README.md`
- Ticket filenames should be short, descriptive, and priority-aware
- Example:
  - `story-1-authenticate-user-from-db.md`
  - `task-protect-admin-user-endpoints.md`
  - `spike-default-vs-custom-login-page.md`

## Content Rule

- `Open Questions` must contain only unresolved product questions.
- `Handoff Notes` must contain only validation points for `engineering-mentor`.
- Do not duplicate ticket content in those sections.
