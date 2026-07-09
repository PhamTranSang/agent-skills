# Spring Cloud Guidance

Use this file when the task is about distributed Spring setups such as config, discovery, gateway, or resilience tooling.

## Distributed Concerns

- Use Spring Cloud only when the project truly needs distributed-system support.
- Keep the local application design working well before introducing cloud coordination.
- Prefer explicit integration boundaries around config, discovery, routing, and resilience features.

## Practical Triggers

- Use this file when the project needs centralized configuration, service discovery, gateway behavior, or distributed resilience patterns.
- Avoid loading this file for a monolith unless the task explicitly introduces cloud-style infrastructure.
