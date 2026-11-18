# CMS: Module Cms Analytics Integration Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-analytics-integration). Observed identity: [`liberusoftware/module-cms-analytics-integration`](../../../modules/source/liberusoftware--module-cms-analytics-integration.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-cms-module-cms-analytics-integration`
**Domain specification:** [Module Cms Analytics Integration](../features/module-cms-analytics-integration.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Module Cms Analytics Integration. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Canonical content/view/conversion events** | Model `canonical content/view/conversion events` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Consent-aware analytics mappings** | Model `consent-aware analytics mappings` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Dashboards** | Model `dashboards` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Boilerplate analytics adapters** | Model `boilerplate analytics adapters` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_29_000200_create_cms_analytics_integration_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/database/migrations/2026_08_29_000200_create_cms_analytics_integration_tables.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AnalyticsAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Contracts/AnalyticsAdapterInterface.php) | `public function key(): string`<br>`public function payload(AnalyticsEvent $event, array $mapping): array` |
| [AnalyticsIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Services/AnalyticsIntegrationService.php) | `public function recordEvent(?int $teamId, array $data): AnalyticsEvent`<br>`public function saveMapping(?int $teamId, array $data): AnalyticsMapping`<br>`public function dashboard(?int $teamId, ?string $from = null, ?string $to = null): array`<br>`public function registerAdapter(AnalyticsAdapterInterface $adapter): void`<br>`public function adapterPayload(string $provider, AnalyticsEvent $event, AnalyticsMapping $mapping): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsEvent.php) | `team_id`, `event_type`, `event_name`, `subject_type`, `subject_id`, `consent_category`, `consent_granted`, `status`, `idempotency_key`, `payload`, `occurred_at` |
| [AnalyticsMapping.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsMapping.php) | `team_id`, `event_type`, `provider`, `measurement_key`, `consent_category`, `config`, `enabled` |

### Consuming adapter specifications

- [HTTP API contract](../api/module-cms-analytics-integration.md) · [Filament 5](../filament/module-cms-analytics-integration.md) · [Livewire 4](../livewire/module-cms-analytics-integration.md) · [React + Inertia](../react/module-cms-analytics-integration.md) · [Vue + Inertia](../vue/module-cms-analytics-integration.md) · [Nuxt 4](../nuxt/module-cms-analytics-integration.md) · [Next.js](../nextjs/module-cms-analytics-integration.md) · [React Native](../react-native/module-cms-analytics-integration.md) · [Flutter & Dart](../flutter/module-cms-analytics-integration.md)
<!-- core-implementation-plan:end -->
