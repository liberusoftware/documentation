# CRM: Crm Usage Wallet And Rebilling Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-usage-wallet-and-rebilling). Observed identity: [`liberusoftware/module-crm-usage-wallet-and-rebilling`](../../../modules/source/liberusoftware--module-crm-usage-wallet-and-rebilling.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-usage-wallet-and-rebilling`
**Domain specification:** [Crm Usage Wallet And Rebilling](../features/crm-usage-wallet-and-rebilling.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Usage Wallet And Rebilling. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Provider usage imports** | Model `provider usage imports` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Wallets/credits** | Model `wallets/credits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Threshold reloads** | Model `threshold reloads` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cost/markup rules** | Model `cost/markup rules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Client charges** | Model `client charges` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Exceptions** | Model `exceptions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reconciliation** | Model `reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Billing/Accounting handoff** | Model `billing/accounting handoff` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_040000_create_crm_usage_wallet_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/database/migrations/2026_08_25_040000_create_crm_usage_wallet_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [UsageWalletQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Queries/UsageWalletQuery.php) | `public function wallet(int $teamId): ?UsageWallet`<br>`public function imports(int $teamId)`<br>`public function charges(int $teamId)`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/CreateCharge.php) | `public function execute(int $teamId, int $actorId, array $data): UsageCharge` |
| [ImportProviderUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ImportProviderUsage.php) | `public function execute(int $teamId, int $actorId, array $data): UsageImport` |
| [ResolveUsageException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ResolveUsageException.php) | `public function execute(int $teamId, int $actorId, int $exceptionId): void` |
| [UpsertWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/UpsertWallet.php) | `public function execute(int $teamId, int $actorId, array $data): UsageWallet` |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsageAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsagePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageAudit.php) | `team_id`, `actor_id`, `event`, `details`, `request_id` |
| [UsageCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageCharge.php) | `team_id`, `usage_import_id`, `wallet_id`, `client_reference`, `cost`, `charge`, `currency`, `status` |
| [UsageImport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageImport.php) | `team_id`, `provider`, `external_id`, `amount`, `currency`, `status`, `failure_reason`, `payload` |
| [UsageWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageWallet.php) | `team_id`, `currency`, `balance`, `threshold`, `reload_amount`, `status`, `version` |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-usage-wallet-and-rebilling.md) · [Filament 5](../filament/crm-usage-wallet-and-rebilling.md) · [Livewire 4](../livewire/crm-usage-wallet-and-rebilling.md) · [React + Inertia](../react/crm-usage-wallet-and-rebilling.md) · [Vue + Inertia](../vue/crm-usage-wallet-and-rebilling.md) · [Nuxt 4](../nuxt/crm-usage-wallet-and-rebilling.md) · [Next.js](../nextjs/crm-usage-wallet-and-rebilling.md) · [React Native](../react-native/crm-usage-wallet-and-rebilling.md) · [Flutter & Dart](../flutter/crm-usage-wallet-and-rebilling.md)
<!-- core-implementation-plan:end -->
