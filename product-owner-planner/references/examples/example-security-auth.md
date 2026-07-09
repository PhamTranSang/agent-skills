# Example: Security / Auth Planning

## User input

> Plan phase 2 for login, token refresh, and permission checks.

## Expected shape

- Hidden dependencies
- Security / infra guidance
- Milestones / Epics
- User Stories
- Implementation Tasks
- Scenarios
- Acceptance criteria
- Handoff notes for `engineering-mentor`

## Good example

### Milestone 1: Auth session handling

#### Story 1

As a signed-in user, I want my session to refresh automatically so that I can continue without being logged out.

#### Scenario

- Happy path: access token expires and refresh succeeds
- Failure path: refresh token is invalid and user is redirected to login

#### Acceptance criteria

- Refresh flow retries once
- Invalid refresh sends user to login
- 401 and 403 behavior is defined

#### Tasks

- Add refresh endpoint integration
- Define redirect behavior on expired session
- Add regression tests for token expiry and permission denial
