# Adoption profiles and progressive architecture

Liberu uses one domain and package architecture for personal users, small and medium businesses, and enterprise organizations. Adoption profiles change deployment topology, operational automation, and optional integrations; they do not fork domain rules, weaken authorization, expose private data, or create incompatible package contracts.

## Non-negotiable baseline

Every profile uses the same core module boundaries, public contracts, migrations, policies, tenant/team checks where applicable, validation, audit semantics, safe defaults, backups, recovery guidance, and versioned APIs. Authentication, authorization, input validation, secret handling, encryption in transit, dependency updates, data ownership, and privacy obligations are never downgraded because an installation is small.

## Profiles

| Profile    | Appropriate deployment                                                                                     | Required capabilities                                                                                                                                                                                                                              | Add when needed                                                                                                                                        |
| ---------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Personal   | One maintained host or local/private deployment with a single application process                          | HTTPS, authenticated access, least privilege, automated backups, restore test, queued work through a database/sync driver, error logging, updates, export, and documented recovery                                                                 | Managed database, object storage, a worker, stronger audit retention, or external identity when usage grows                                            |
| SME        | One or a few production instances with managed database/storage, a worker, staging, and routine monitoring | Separate environments, team roles, tenant isolation, scheduled backups, restore verification, queue supervision, health checks, rate limits, audit events, dependency scanning, and support runbook                                                | SSO/SCIM, dedicated workers, read replicas, centralized logs, formal SLOs, private networking, or a tested standby                                     |
| Enterprise | Protected multi-service or multi-region topology selected by risk and SLO                                  | SSO/MFA, centralized identity, least-privilege service identities, immutable audit retention, HA where required, disaster recovery objectives, observability, vulnerability response, change control, compatibility matrix, and rehearsed rollback | Regional isolation, active/standby or active/active operation, data residency, dedicated compliance controls, and organization-wide policy integration |

## Progressive design rules

1. Start with the smallest safe topology that satisfies the user's data, availability, and recovery needs.
2. Keep scaling decisions in application composition and infrastructure configuration, not in domain code or presentation forks.
3. Prefer interfaces and explicit registries for optional mail, storage, search, identity, payment, AI, queue, and observability providers.
4. Make upgrades additive and reversible where practical. Document migration duration, locking, backfill, rollback limits, and the next profile's prerequisites.
5. Measure real usage before adding distributed systems. A local queue, single worker, or synchronous path is acceptable when its limits and failure behavior are documented; slow or failure-prone work must still be bounded and recoverable.
6. Preserve export and portability. A personal user must be able to leave with their data, and an enterprise must be able to migrate or regionally operate it without proprietary domain assumptions.

## Decision record

Every project records its chosen profile, data classification, availability target, recovery point/time objectives, expected users and workload, hosting constraints, support owner, backup/restore evidence, and upgrade path. A profile change requires evidence and an ADR when it changes trust boundaries, data residency, public contracts, or recovery guarantees.

See [MODULES.md](MODULES.md), [SECURITY.md](SECURITY.md), [TENANCY.md](TENANCY.md), [POLICY.md](POLICY.md), and the matching standards in [standards/ADOPTION.md](../standards/ADOPTION.md).
