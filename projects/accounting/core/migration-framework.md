# Accounting: Migration Framework Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). Observed identity: [`liberusoftware/module-accounting-migration-framework`](../../../modules/source/liberusoftware--module-accounting-migration-framework.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-migration-framework`
**Domain specification:** [Migration Framework](../features/migration-framework.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Migration Framework. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Source inventory** | Model `source inventory` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Mapping** | Model `mapping` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Dry run** | Model `dry run` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Transforms** | Model `transforms` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Validation** | Model `validation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Batches** | Model `batches` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Resume** | Model `resume` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attachments** | Model `attachments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Errors** | Model `errors` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Counts** | Model `counts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reconciliation** | Model `reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_26_011000_create_accounting_migration_framework_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/database/migrations/2026_08_26_011000_create_accounting_migration_framework_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MigrationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Queries/MigrationQuery.php) | `public function sources(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function batches(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function counts(MigrationBatch $batch): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateBatch.php) | `public function handle(MigrationSource $source, MigrationMapping $mapping, array $attributes, array $rows = []): MigrationBatch` |
| [CreateMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateMapping.php) | `public function handle(MigrationSource $source, array $attributes): MigrationMapping` |
| [ReconcileBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/ReconcileBatch.php) | `public function handle(MigrationBatch $batch, array $attributes = []): MigrationReconciliation` |
| [RegisterSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RegisterSource.php) | `public function handle(array $attributes): MigrationSource` |
| [RunBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RunBatch.php) | `public function handle(MigrationBatch $batch, bool $dryRun = false, int $limit = 100): MigrationBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationAttachment.php) | `batch_id`, `file_ref`, `name`, `mime_type`, `size_bytes`, `checksum`, `metadata` |
| [MigrationBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationBatch.php) | `team_id`, `batch_ref`, `source_id`, `mapping_id`, `status`, `dry_run`, `resume_token`, `total_count`, `processed_count`, `success_count`, `error_count`, `skipped_count`, `started_at`, `completed_at`, `paused_at`, `failure_message`, `metadata` |
| [MigrationMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationMapping.php) | `source_id`, `mapping_ref`, `entity_type`, `field_map`, `transforms`, `validation_rules`, `version`, `active`, `metadata` |
| [MigrationReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationReconciliation.php) | `batch_id`, `source_count`, `imported_count`, `failed_count`, `source_total`, `destination_total`, `variance`, `status`, `notes`, `metadata` |
| [MigrationRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationRow.php) | `batch_id`, `row_ref`, `source_key`, `destination_key`, `payload`, `transformed_payload`, `status`, `error_code`, `error_message`, `attempts`, `processed_at`, `metadata` |
| [MigrationSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationSource.php) | `team_id`, `source_ref`, `provider`, `source_type`, `name`, `record_count`, `checksum`, `status`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/migration-framework.md) · [Filament 5](../filament/migration-framework.md) · [Livewire 4](../livewire/migration-framework.md) · [React + Inertia](../react/migration-framework.md) · [Vue + Inertia](../vue/migration-framework.md) · [Nuxt 4](../nuxt/migration-framework.md) · [Next.js](../nextjs/migration-framework.md) · [React Native](../react-native/migration-framework.md) · [Flutter & Dart](../flutter/migration-framework.md)
<!-- core-implementation-plan:end -->
