# Billing: Module Billing Communications Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-communications). Observed identity: [`liberusoftware/module-billing-communications`](../../../modules/source/liberusoftware--module-billing-communications.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-billing-module-billing-communications`
**Domain specification:** [Module Billing Communications](../features/module-billing-communications.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Module Billing Communications. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **VoIP/SMS service inventory** | Model `voip/sms service inventory` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Number lifecycle** | Model `number lifecycle` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Usage/rating imports** | Model `usage/rating imports` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Provider adapters** | Model `provider adapters` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_130000_create_billing_communications_records_table.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/database/migrations/2026_08_24_130000_create_billing_communications_records_table.php) · [2026_08_24_160000_create_billing_communications_capabilities.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/database/migrations/2026_08_24_160000_create_billing_communications_capabilities.php) · [2026_08_29_200000_create_billing_voice_tables.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/database/migrations/2026_08_29_200000_create_billing_voice_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListCommunicationRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationRecords.php) | `public function handle(string $model, int $teamId): Collection` |
| [ListCommunicationsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationsRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCallRateRule.php) | `public function handle(int $teamId, array $attributes): CallRateRule` |
| [CreateCommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationProvider.php) | `public function handle(int $teamId, array $attributes): CommunicationProvider` |
| [CreateCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationService.php) | `public function handle(int $teamId, array $attributes): CommunicationService` |
| [CreateVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateVoipAccount.php) | `public function handle(int $teamId, array $attributes): VoipAccount` |
| [ImportCommunicationUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ImportCommunicationUsage.php) | `public function handle(int $teamId, array $attributes): CommunicationUsageImport` |
| [IngestCallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/IngestCallDetailRecord.php) | `public function handle(VoipAccount $account, array $attributes): CallDetailRecord` |
| [ProvisionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionCommunicationNumber.php) | `public function handle(int $teamId, array $attributes): CommunicationNumber` |
| [ProvisionVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionVoipAccount.php) | `public function __construct(private VoiceProviderRegistry $providers)`<br>`public function handle(VoipAccount $account): VoipAccount` |
| [TransitionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationNumber.php) | `public function handle(CommunicationNumber $number, string $status): CommunicationNumber` |
| [TransitionCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationService.php) | `public function handle(CommunicationService $service, string $status): CommunicationService` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallDetailRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallRateRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationProvider.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationService.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationUsageImport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationUsageImport.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipFraudAlert.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipFraudAlert.php) | No literal fillable array detected; inspect the model and API schema. |

### Consuming adapter specifications

- [HTTP API contract](../api/module-billing-communications.md) · [Filament 5](../filament/module-billing-communications.md) · [Livewire 4](../livewire/module-billing-communications.md) · [React + Inertia](../react/module-billing-communications.md) · [Vue + Inertia](../vue/module-billing-communications.md) · [Nuxt 4](../nuxt/module-billing-communications.md) · [Next.js](../nextjs/module-billing-communications.md) · [React Native](../react-native/module-billing-communications.md) · [Flutter & Dart](../flutter/module-billing-communications.md)
<!-- core-implementation-plan:end -->
