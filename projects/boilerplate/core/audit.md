# Boilerplate: Audit domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#audit). Observed identity: [`liberusoftware/audit`](../../../modules/source/liberusoftware--audit.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-audit`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Actor, tenant, request context, material changes, privileged actions, retention, and tamper evidence.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Audit. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, and Nuxt consumers use only this package's public contracts. See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md) and [testing](../../../standards/TESTING.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Actor** | Model `actor` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tenant** | Model `tenant` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Request context** | Model `request context` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Material changes** | Model `material changes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Privileged actions** | Model `privileged actions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Retention** | Model `retention` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tamper evidence** | Model `tamper evidence` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_06_29_124053_create_activity_log_table.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/database/migrations/2026_06_29_124053_create_activity_log_table.php) · [2026_08_01_064100_add_tamper_evidence_to_activity_log.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/database/migrations/2026_08_01_064100_add_tamper_evidence_to_activity_log.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AuditRecorder.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/src/Contracts/AuditRecorder.php) | `public function record(string $event, string $subjectType, string\|int\|null $subjectId, array $before, array $after, AuditContext $context): void` |

### Consuming adapter specifications

- [HTTP API contract](../api/audit.md) · [Filament 5](../filament/audit.md) · [Livewire 4](../livewire/audit.md) · [React + Inertia](../react/audit.md) · [Vue + Inertia](../vue/audit.md) · [Nuxt 4](../nuxt/audit.md) · [Next.js](../nextjs/audit.md) · [React Native](../react-native/audit.md) · [Flutter & Dart](../flutter/audit.md)
<!-- core-implementation-plan:end -->
