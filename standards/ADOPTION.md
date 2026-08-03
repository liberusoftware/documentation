# Progressive delivery standard

Enterprise quality means reliable behavior, secure boundaries, recoverable data, clear documentation, and useful evidence. It does not require every user to run a cluster. This standard defines the smallest safe implementation for personal users and SMEs while preserving a direct path to enterprise operation.

## Quality baseline for every installation

- Use the supported PHP 8.5/Laravel 13 baseline, locked dependencies, strict server-side validation, authorization policies, secure secret handling, HTTPS in production, and documented updates.
- Keep modules independently installable and use their public contracts; do not copy domain logic into an application or presentation adapter.
- Own migrations, constraints, indexes, retention, export, deletion, backups, and recovery in the module that owns the data.
- Log actionable failures without credentials or unnecessary personal data, expose health information safely, and provide a tested backup/restore procedure.
- Test public actions, permissions, invalid input, tenant boundaries where applicable, jobs/events, migrations, and the highest-risk failure paths.

## Progressive operating profiles

| Profile    | Minimum practical setup                                                                                                                                                        | Quality evidence                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Personal   | One application host, one supported database, local or compatible object storage, scheduled backup, and database/sync queue for modest workloads                               | Successful fresh install, update, backup restore, export, authentication/authorization checks, and documented limits                                           |
| SME        | Managed database/storage where practical, separate staging, supervised worker/scheduler, TLS, monitoring, rate limits, team roles, and routine restore tests                   | CI, dependency/security scans, migration smoke test, queue failure/retry test, health checks, support runbook, and release verification                        |
| Enterprise | Protected production environments, centralized identity, service identities, immutable audit, HA/DR according to risk, observability, change control, and compatibility matrix | SLOs, RPO/RTO evidence, failover/restore rehearsal, architecture/security/compliance review, incident runbook, rollback rehearsal, and signed release evidence |

## Implementation rules

1. Keep the same domain model, module package, API contracts, policies, and data formats across profiles.
2. Make optional infrastructure capability-based: bind a queue, storage, mail, search, identity, or observability contract at composition time.
3. Use feature flags for controlled rollout, not as a substitute for authorization, installation, entitlement, or migration safety.
4. Scale only after measuring bottlenecks. Add workers, replicas, caches, queues, or regional separation behind documented contracts and operational tests.
5. Give users understandable errors, safe defaults, previews or confirmation for destructive work, accessibility, localization, timezone/currency handling, and export/retention controls.
6. Document what a simpler profile does not provide: throughput, uptime, retention, support hours, integrations, compliance scope, and recovery guarantees.

## Delivery checklist

Before release, record the chosen profile and verify formatting, static analysis, architecture checks, security checks, tests, migrations, backups/restores, documentation, compatibility, and the smallest representative user journey. Enterprise controls are additive; they must not change the public behavior of the core package or make personal/SME installations second-class forks.

See [GUIDELINES.md](GUIDELINES.md), [LARAVEL.md](LARAVEL.md), [DATABASE.md](DATABASE.md), [TESTING.md](TESTING.md), [CI.md](CI.md), [DOCUMENTATION.md](DOCUMENTATION.md), and [../architecture/ADOPTION.md](../architecture/ADOPTION.md).
