# Crm: Work Management Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#work-management). Observed identity: [`liberusoftware/module-crm-work-management`](../../../modules/source/liberusoftware--module-crm-work-management.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-work-management`
**Domain specification:** [Work Management](../features/work-management.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Work Management. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

## Domain-driven implementation plan

- Model the capability with small aggregates, entities, value objects, enums, domain services, and explicit lifecycle states. Enforce invariants inside the domain boundary and keep invalid transitions impossible or rejected with typed exceptions.
- Implement one application action per meaningful mutation/use case and purpose-built query/read-model classes for reads. Use typed immutable DTOs and stable identifiers at public boundaries; use repositories only where persistence abstraction adds value.
- Publish past-tense domain events after a successful local transaction. Use an outbox/inbox, idempotent handlers, sagas, or compensating actions for cross-module and distributed work; never mutate another module's private tables.

## Laravel and persistence plan

- Use PHP 8.5 strict types, PSR-compatible names, constructor injection, Laravel contracts, service providers, configuration, policies, validation, and route-independent application services. Format with the repository's Pint rules and keep static analysis clean.
- Keep Eloquent models as persistence mappings, not domain aggregates or API resources. The module owns migrations, constraints, indexes, casts, factories, seeders, retention, export, deletion, and upgrade behavior. Released migrations are immutable; production-safe follow-up migrations document locks, backfills, deployment order, and rollback limits.
- Queue work that exceeds the request budget or depends on external systems. Jobs carry authorized tenant/actor context, have explicit retry/backoff/timeout/idempotency rules, and emit structured logs, metrics, traces, correlation IDs, and operator-visible failure state.

## Security and user outcomes

- Apply policies consistently to HTTP, UI, console, queue, export, search, notification, and bulk paths. Enforce tenant/team/resource ownership, field sensitivity, consent, entitlement, and break-glass auditing; scopes never override domain authorization.
- Treat imports, files, webhooks, provider responses, and user input as untrusted. Redact credentials and protected data from logs, exceptions, events, snapshots, metrics, and test artifacts.
- Make normal workflows understandable for SMEs and personal users: actionable validation, safe defaults, reversible or previewable operations, clear status and recovery guidance, localization/timezone/currency support where relevant, accessibility in adapters, low operational overhead, and export/retention controls.

## Public boundary and adapters

Expose only stable contracts, actions, queries, events, resource data, and capability metadata needed by consumers. Keep provider SDKs, credentials, webhook mappings, and provider identifiers in separate adapter packages. Presentation packages may add validation at their boundary, but the core revalidates invariants and authorization and remains free of presentation dependencies.

## Verification and delivery plan

- Use unit tests for value objects, entities, aggregates, policies, and pure rules; feature/integration tests for actions, persistence, validation, tenancy, events, jobs, commands, migrations, upgrades, and recovery; and shared contract tests for adapters.
- Add architecture tests for forbidden App classes, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Test empty installs, supported upgrades, rollback policy, representative host composition, and compatibility across the declared Laravel/PHP/database matrix.
- Run the independent repository's Pest 5 suite through Composer scripts and the shared package testbench. Generate meaningful coverage, static-analysis, security, documentation/link, and performance evidence; coverage complements risk-based assertions and never replaces them.
- Release with Composer metadata, module manifest, service provider, changelog, migration notes, README, compatibility matrix, runbook, and safe install/enable/disable/upgrade/uninstall behavior. Disabling or removal never silently deletes user data.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Cross-record task boards** | Model `cross-record task boards` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Queues** | Model `queues` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Recurring work** | Model `recurring work` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Checklists** | Model `checklists` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Approvals** | Model `approvals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Workload** | Model `workload` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Dependencies** | Model `dependencies` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Personal/team views** | Model `personal/team views` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_010000_create_crm_work_management_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/database/migrations/2026_08_25_010000_create_crm_work_management_tables.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddChecklistItem.php) | `public function execute(WorkItem $item, ?int $actorId, string $title): ChecklistItem` |
| [AddDependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddDependency.php) | `public function execute(WorkItem $item, WorkItem $dependsOn, ?int $actorId): Dependency` |
| [CompleteWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CompleteWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, ?int $expectedVersion = null): WorkItem` |
| [CreateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkItem.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkItem` |
| [CreateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkQueue.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkQueue` |
| [ReviewApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/ReviewApproval.php) | `public function request(WorkItem $item, ?int $actorId, ?string $comment = null): Approval`<br>`public function review(Approval $approval, int $actorId, string $status, ?string $comment = null): Approval` |
| [UpdateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, array $attributes, ?int $expectedVersion = null): WorkItem` |
| [UpdateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkQueue.php) | `public function execute(WorkQueue $queue, ?int $actorId, array $attributes): WorkQueue` |
| [WorkAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkAudit.php) | `public function record(Model $item, ?int $actorId, string $event, array $details = []): void` |
| [WorkloadQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkloadQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Approval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Approval.php) | `work_item_id`, `team_id`, `requested_by`, `reviewed_by`, `status`, `comment`, `reviewed_at` |
| [ChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/ChecklistItem.php) | `work_item_id`, `team_id`, `actor_id`, `title`, `completed`, `position` |
| [Dependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Dependency.php) | `work_item_id`, `depends_on_id`, `team_id` |
| [WorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkItem.php) | `team_id`, `actor_id`, `assigned_to`, `queue_id`, `title`, `description`, `status`, `priority`, `subject_type`, `subject_id`, `due_at`, `recurrence`, `next_run_at`, `version`, `metadata` |
| [WorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkQueue.php) | `team_id`, `actor_id`, `name`, `description`, `status`, `rules` |

### Consuming adapter specifications

- [HTTP API contract](../api/work-management.md) · [Filament 5](../filament/work-management.md) · [Livewire 4](../livewire/work-management.md) · [React + Inertia](../react/work-management.md) · [Vue + Inertia](../vue/work-management.md) · [Nuxt 4](../nuxt/work-management.md) · [Next.js](../nextjs/work-management.md) · [React Native](../react-native/work-management.md) · [Flutter & Dart](../flutter/work-management.md)
<!-- core-implementation-plan:end -->
