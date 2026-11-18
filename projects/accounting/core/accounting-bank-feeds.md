# Accounting: Accounting Bank Feeds Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-feeds). Observed identity: [`liberusoftware/module-accounting-bank-feeds`](../../../modules/source/liberusoftware--module-accounting-bank-feeds.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-bank-feeds`
**Domain specification:** [Accounting Bank Feeds](../features/accounting-bank-feeds.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting Bank Feeds. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Consent/connections** | Model `consent/connections` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Institutions** | Model `institutions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Account mapping** | Model `account mapping` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cursors** | Model `cursors` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Imports** | Model `imports` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Duplicates** | Model `duplicates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Pending/posted state** | Model `pending/posted state` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Health** | Model `health` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Provider adapters** | Model `provider adapters` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_30_110000_create_accounting_bank_feeds_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/database/migrations/2026_08_30_110000_create_accounting_bank_feeds_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankFeedQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Queries/BankFeedQuery.php) | `public function connections(?int $teamId = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/CreateBankFeedConnection.php) | `public function handle(array $attributes): BankFeedConnection` |
| [ImportBankFeedTransactions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/ImportBankFeedTransactions.php) | `public function handle(BankFeedConnection $connection, array $batch): array` |
| [MapBankFeedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/MapBankFeedAccount.php) | `public function handle(BankFeedConnection $connection, array $attributes): BankFeedAccountMapping` |
| [SetBankFeedTransactionStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/SetBankFeedTransactionStatus.php) | `public function handle(BankFeedTransaction $transaction, FeedTransactionStatus $status): BankFeedTransaction` |
| [UpdateBankFeedHealth.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpdateBankFeedHealth.php) | `public function handle(BankFeedConnection $connection, ?string $error = null): BankFeedConnection` |
| [UpsertBankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpsertBankFeedInstitution.php) | `public function handle(array $attributes): BankFeedInstitution` |
| [BankFeedAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Contracts/BankFeedAdapter.php) | `public function fetch(BankFeedConnection $connection): array` |
| [BankFeedsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/src/Policies/BankFeedsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $connection): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $connection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankFeedAccountMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedAccountMapping.php) | `team_id`, `connection_id`, `bank_account_id`, `external_account_id`, `name`, `currency`, `metadata` |
| [BankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedConnection.php) | `team_id`, `user_id`, `institution_id`, `provider`, `name`, `external_reference`, `access_token`, `credentials`, `cursor`, `status`, `last_synced_at`, `last_error`, `last_error_at`, `metadata` |
| [BankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedInstitution.php) | `provider`, `external_id`, `name`, `country`, `logo_url`, `metadata` |
| [BankFeedTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedTransaction.php) | `team_id`, `connection_id`, `mapping_id`, `external_id`, `transaction_date`, `posted_date`, `description`, `amount`, `currency`, `status`, `category`, `raw_data`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-bank-feeds.md) · [Filament 5](../filament/accounting-bank-feeds.md) · [Livewire 4](../livewire/accounting-bank-feeds.md) · [React + Inertia](../react/accounting-bank-feeds.md) · [Vue + Inertia](../vue/accounting-bank-feeds.md) · [Nuxt 4](../nuxt/accounting-bank-feeds.md) · [Next.js](../nextjs/accounting-bank-feeds.md) · [React Native](../react-native/accounting-bank-feeds.md) · [Flutter & Dart](../flutter/accounting-bank-feeds.md)
<!-- core-implementation-plan:end -->
