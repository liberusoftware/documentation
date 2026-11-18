# Accounting: Financial Statements Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-statements). Observed identity: [`liberusoftware/module-accounting-financial-statements`](../../../modules/source/liberusoftware--module-accounting-financial-statements.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-financial-statements`
**Domain specification:** [Financial Statements](../features/financial-statements.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Financial Statements. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Profit and loss** | Model `profit and loss` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Balance sheet** | Model `balance sheet` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cash flow** | Model `cash flow` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Changes in equity** | Model `changes in equity` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Comparative periods** | Model `comparative periods` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Dimensions** | Model `dimensions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Drill-through** | Model `drill-through` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinancialStatementsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Policies/FinancialStatementsPolicy.php) | `public function view(?Authenticatable $user): bool` |

### Consuming adapter specifications

- [HTTP API contract](../api/financial-statements.md) · [Filament 5](../filament/financial-statements.md) · [Livewire 4](../livewire/financial-statements.md) · [React + Inertia](../react/financial-statements.md) · [Vue + Inertia](../vue/financial-statements.md) · [Nuxt 4](../nuxt/financial-statements.md) · [Next.js](../nextjs/financial-statements.md) · [React Native](../react-native/financial-statements.md) · [Flutter & Dart](../flutter/financial-statements.md)
<!-- core-implementation-plan:end -->
