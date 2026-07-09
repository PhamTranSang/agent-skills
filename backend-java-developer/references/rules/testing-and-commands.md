# Testing and Commands

Design the tests or validation steps that should be run. Do not run shell commands, scripts, test suites, or validation scripts unless the user's current preferences permit command execution or the user explicitly grants permission for this task.

Use this together with `references/tech/testing.md` for framework-specific testing patterns and tool choices.

When command execution is restricted, state the exact commands the user may allow, such as:

```bash
./gradlew clean test
mvn clean test
```
