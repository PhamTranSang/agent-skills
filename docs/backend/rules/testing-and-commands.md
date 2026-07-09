# Backend Testing and Commands Addendum

Extend the shared testing rules with backend-specific command examples and validation expectations.

When command execution is restricted, state the exact commands the user may allow, such as:

```bash
./gradlew clean test
mvn clean test
```

If the project uses another wrapper or build tool, keep the example aligned with the actual repo.
