# CMS: Cms Translation Management Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-translation-management). Observed identity: [`liberusoftware/module-cms-translation-management`](../../../modules/source/liberusoftware--module-cms-translation-management.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-cms-cms-translation-management`
**Domain specification:** [Cms Translation Management](../features/cms-translation-management.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Cms Translation Management. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Jobs** | Model `jobs` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Source changes** | Model `source changes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Assignments** | Model `assignments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Vendor adapters** | Model `vendor adapters` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Machine translation** | Model `machine translation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Review** | Model `review` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Memory/glossaries** | Model `memory/glossaries` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Status** | Model `status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cost** | Model `cost` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reconciliation** | Model `reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_020000_create_cms_translation_management_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/database/migrations/2026_08_25_020000_create_cms_translation_management_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TranslationJobQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Queries/TranslationJobQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?TranslationJob` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TranslationManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Actions/TranslationManagementService.php) | `public function __construct(private TranslationVendorRegistry $vendors)`<br>`public function createJob(array $attributes): TranslationJob`<br>`public function addSourceChange(TranslationJob $job, array $attributes): TranslationSourceChange`<br>`public function queue(TranslationJob $job): TranslationJob`<br>`public function cancel(TranslationJob $job): TranslationJob`<br>`public function translate(TranslationSourceChange $change, string $vendorKey, array $context = []): TranslationSourceChange`<br>`public function assign(TranslationSourceChange $change, string $assigneeType, int\|string $assigneeId, string $role, ?string $dueAt = null): TranslationAssignment`<br>`public function review(TranslationSourceChange $change, string $decision, ?string $notes = null): TranslationSourceChange`<br>`public function addVendor(array $attributes): TranslationVendor`<br>`public function remember(string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, array $metadata = [], int\|string\|null $teamId = null): TranslationMemory`<br>`public function glossary(array $attributes): TranslationGlossary`<br>`public function reconcile(TranslationJob $job): TranslationJob` |
| [TranslationVendorInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Contracts/TranslationVendorInterface.php) | `public function key(): string`<br>`public function translate(string $source, string $sourceLocale, string $targetLocale, array $context = []): TranslationResult` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TranslationAssignment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationAssignment.php) | `job_id`, `source_change_id`, `assignee_type`, `assignee_id`, `role`, `status`, `due_at`, `completed_at`, `team_id` |
| [TranslationGlossary.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationGlossary.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [TranslationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationJob.php) | `public_id`, `external_key`, `name`, `source_locale`, `target_locale`, `status`, `vendor_key`, `total_units`, `completed_units`, `estimated_cost`, `actual_cost`, `currency`, `metadata`, `queued_at`, `completed_at`, `team_id` |
| [TranslationMemory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationMemory.php) | `source_locale`, `target_locale`, `source_hash`, `source_text`, `translated_text`, `status`, `metadata`, `team_id` |
| [TranslationSourceChange.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationSourceChange.php) | `job_id`, `subject_type`, `subject_id`, `field`, `source_text`, `source_hash`, `source_version`, `translated_text`, `translated_hash`, `status`, `provider`, `model`, `cost`, `provenance`, `review_notes`, `translated_at`, `reviewed_at`, `team_id` |
| [TranslationVendor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationVendor.php) | `key`, `name`, `driver`, `settings`, `status`, `team_id` |

### Consuming adapter specifications

- [HTTP API contract](../api/cms-translation-management.md) · [Filament 5](../filament/cms-translation-management.md) · [Livewire 4](../livewire/cms-translation-management.md) · [React + Inertia](../react/cms-translation-management.md) · [Vue + Inertia](../vue/cms-translation-management.md) · [Nuxt 4](../nuxt/cms-translation-management.md) · [Next.js](../nextjs/cms-translation-management.md) · [React Native](../react-native/cms-translation-management.md) · [Flutter & Dart](../flutter/cms-translation-management.md)
<!-- core-implementation-plan:end -->
