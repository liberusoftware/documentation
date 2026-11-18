# CRM: Crm Reputation Management Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-reputation-management). Observed identity: [`liberusoftware/module-crm-reputation-management`](../../../modules/source/liberusoftware--module-crm-reputation-management.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-reputation-management`
**Domain specification:** [Crm Reputation Management](../features/crm-reputation-management.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Reputation Management. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Review requests** | Model `review requests` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Review-site connections** | Model `review-site connections` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Monitoring** | Model `monitoring` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Response workflow** | Model `response workflow` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Templates** | Model `templates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Escalation** | Model `escalation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Sentiment** | Model `sentiment` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Location rollups** | Model `location rollups` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reputation reporting** | Model `reputation reporting` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_230000_create_crm_reputation_management_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/database/migrations/2026_08_25_230000_create_crm_reputation_management_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReputationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Queries/ReputationQuery.php) | `public function connections(int $teamId)`<br>`public function requests(int $teamId)`<br>`public function reviews(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function rollups(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectReviewSite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/ConnectReviewSite.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationConnection` |
| [CreateReviewRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/CreateReviewRequest.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationRequest` |
| [EscalateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/EscalateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId): ReputationReview` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RecordReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationReview` |
| [RespondToReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RespondToReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [SaveTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/SaveTemplate.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationTemplate` |
| [UpdateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/UpdateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [ReputationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Services/ReputationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReputationConnection.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationConnection.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRollup.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRollup.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-reputation-management.md) · [Filament 5](../filament/crm-reputation-management.md) · [Livewire 4](../livewire/crm-reputation-management.md) · [React + Inertia](../react/crm-reputation-management.md) · [Vue + Inertia](../vue/crm-reputation-management.md) · [Nuxt 4](../nuxt/crm-reputation-management.md) · [Next.js](../nextjs/crm-reputation-management.md) · [React Native](../react-native/crm-reputation-management.md) · [Flutter & Dart](../flutter/crm-reputation-management.md)
<!-- core-implementation-plan:end -->
