# Accounting: Accounting Workpapers Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-workpapers). Observed identity: [`liberusoftware/module-accounting-workpapers`](../../../modules/source/liberusoftware--module-accounting-workpapers.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-workpapers`
**Domain specification:** [Accounting Workpapers](../features/accounting-workpapers.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting Workpapers. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Lead schedules** | Model `lead schedules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **References** | Model `references` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attachments** | Model `attachments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Procedures** | Model `procedures` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Conclusions** | Model `conclusions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Preparer/reviewer** | Model `preparer/reviewer` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Rollover** | Model `rollover` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Export** | Model `export` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_29_000007_create_accounting_workpapers_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/database/migrations/2026_08_29_000007_create_accounting_workpapers_tables.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperAttachment.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperAttachment` |
| [AddWorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperProcedure.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperProcedure` |
| [AddWorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperReference.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperReference` |
| [AssignWorkpaperReviewer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AssignWorkpaperReviewer.php) | `public function handle(Workpaper $workpaper, int $reviewerId): Workpaper` |
| [ConcludeWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/ConcludeWorkpaper.php) | `public function handle(Workpaper $workpaper, string $conclusion): Workpaper` |
| [CreateWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/CreateWorkpaper.php) | `public function handle(array $attributes): Workpaper` |
| [RequestWorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RequestWorkpaperExport.php) | `public function handle(Workpaper $workpaper, string $format): WorkpaperExport` |
| [RolloverWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RolloverWorkpaper.php) | `public function handle(Workpaper $source, array $attributes = []): Workpaper` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Workpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/Workpaper.php) | `team_id`, `title`, `reference`, `status`, `period_start`, `period_end`, `preparer_id`, `reviewer_id`, `conclusion`, `metadata` |
| [WorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperAttachment.php) | `workpaper_id`, `name`, `disk`, `path`, `mime_type`, `size` |
| [WorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperExport.php) | `workpaper_id`, `format`, `status`, `path`, `error` |
| [WorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperProcedure.php) | `workpaper_id`, `description`, `status`, `performed_by`, `performed_at`, `evidence` |
| [WorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperReference.php) | `workpaper_id`, `label`, `target_type`, `target_id`, `notes` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-workpapers.md) · [Filament 5](../filament/accounting-workpapers.md) · [Livewire 4](../livewire/accounting-workpapers.md) · [React + Inertia](../react/accounting-workpapers.md) · [Vue + Inertia](../vue/accounting-workpapers.md) · [Nuxt 4](../nuxt/accounting-workpapers.md) · [Next.js](../nextjs/accounting-workpapers.md) · [React Native](../react-native/accounting-workpapers.md) · [Flutter & Dart](../flutter/accounting-workpapers.md)
<!-- core-implementation-plan:end -->
