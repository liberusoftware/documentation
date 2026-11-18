# Accounting: Accounting Forecasts Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-forecasts). Observed identity: [`liberusoftware/module-accounting-forecasts`](../../../modules/source/liberusoftware--module-accounting-forecasts.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-forecasts`
**Domain specification:** [Accounting Forecasts](../features/accounting-forecasts.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting Forecasts. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Driver/manual forecasts** | Model `driver/manual forecasts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Scenarios** | Model `scenarios` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Rolling periods** | Model `rolling periods` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Actual replacement** | Model `actual replacement` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Assumptions** | Model `assumptions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Approvals** | Model `approvals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Variance** | Model `variance` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_021000_create_accounting_forecast_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/database/migrations/2026_08_25_021000_create_accounting_forecast_tables.php) · [2026_08_26_021000_create_accounting_forecast_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/database/migrations/2026_08_26_021000_create_accounting_forecast_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Queries/ForecastQuery.php) | `public function paginate(?int $teamId = null, ?ForecastStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Forecast $forecast): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastAssumption.php) | `public function handle(Forecast $forecast, array $attributes): ForecastAssumption` |
| [AddForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastLine.php) | `public function handle(Forecast $forecast, array $a): ForecastLine` |
| [CreateForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecast.php) | `public function handle(array $a): Forecast` |
| [CreateForecastPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecastPeriods.php) | `public function handle(Forecast $forecast, ?string $startsOn = null): array` |
| [DecideForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/DecideForecast.php) | `public function handle(Forecast $forecast, string $actor, bool $approved, ?string $comment = null): Forecast` |
| [ReplaceActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/ReplaceActual.php) | `public function handle(Forecast $forecast, array $a): ForecastActual` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/SubmitForecast.php) | `public function handle(Forecast $forecast): Forecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/Forecast.php) | `team_id`, `forecast_ref`, `name`, `currency`, `method`, `status`, `base_period`, `horizon_periods`, `scenario_ref`, `metadata` |
| [ForecastActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastActual.php) | `forecast_id`, `line_id`, `period_ref`, `actual_value`, `source_ref`, `replaced_at`, `metadata` |
| [ForecastApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastApproval.php) | `forecast_id`, `actor_ref`, `approved`, `comment`, `decided_at`, `metadata` |
| [ForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastAssumption.php) | `forecast_id`, `assumption_ref`, `name`, `value`, `unit`, `source`, `effective_from`, `effective_to`, `metadata` |
| [ForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastLine.php) | `forecast_id`, `period_ref`, `account_ref`, `dimension_ref`, `description`, `driver_ref`, `forecast_value`, `actual_value`, `variance_value`, `metadata` |
| [ForecastPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastPeriod.php) | `forecast_id`, `period_ref`, `starts_on`, `ends_on`, `status`, `is_rolling`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-forecasts.md) · [Filament 5](../filament/accounting-forecasts.md) · [Livewire 4](../livewire/accounting-forecasts.md) · [React + Inertia](../react/accounting-forecasts.md) · [Vue + Inertia](../vue/accounting-forecasts.md) · [Nuxt 4](../nuxt/accounting-forecasts.md) · [Next.js](../nextjs/accounting-forecasts.md) · [React Native](../react-native/accounting-forecasts.md) · [Flutter & Dart](../flutter/accounting-forecasts.md)
<!-- core-implementation-plan:end -->
