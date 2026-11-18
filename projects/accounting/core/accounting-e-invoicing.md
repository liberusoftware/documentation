# Accounting: Accounting E Invoicing Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-e-invoicing). Observed identity: [`liberusoftware/module-accounting-e-invoicing`](../../../modules/source/liberusoftware--module-accounting-e-invoicing.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-e-invoicing`
**Domain specification:** [Accounting E Invoicing](../features/accounting-e-invoicing.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting E Invoicing. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Structured invoice/credit formats** | Model `structured invoice/credit formats` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tax-ID validation** | Model `tax-id validation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Network/provider routing** | Model `network/provider routing` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Signatures** | Model `signatures` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delivery/receipt status** | Model `delivery/receipt status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Archival** | Model `archival` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reconciliation** | Model `reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_025000_create_accounting_e_invoice_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/database/migrations/2026_08_25_025000_create_accounting_e_invoice_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EInvoiceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Queries/EInvoiceQuery.php) | `public function paginate(?int $legalEntityId = null, ?DocumentStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ArchiveEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [CreateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/CreateEInvoice.php) | `public function handle(array $a): EInvoiceDocument` |
| [ReconcileEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ReconcileEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [RecordEInvoiceReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/RecordEInvoiceReceipt.php) | `public function handle(EInvoiceDocument $d, bool $accepted, ?string $message = null, ?string $actor = null): EInvoiceDocument` |
| [SignEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SignEInvoice.php) | `public function handle(EInvoiceDocument $d, string $signature, ?string $actor = null): EInvoiceDocument` |
| [SubmitEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SubmitEInvoice.php) | `public function handle(EInvoiceDocument $d, string $provider, ?string $actor = null): EInvoiceDocument` |
| [ValidateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ValidateEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EInvoiceDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceDocument.php) | `legal_entity_id`, `document_ref`, `document_type`, `format`, `status`, `tax_id`, `counterparty_ref`, `currency`, `provider_ref`, `payload`, `signature`, `submitted_at`, `received_at`, `archived_at`, `metadata` |
| [EInvoiceEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceEvent.php) | `document_id`, `event`, `provider_ref`, `actor_ref`, `message`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-e-invoicing.md) · [Filament 5](../filament/accounting-e-invoicing.md) · [Livewire 4](../livewire/accounting-e-invoicing.md) · [React + Inertia](../react/accounting-e-invoicing.md) · [Vue + Inertia](../vue/accounting-e-invoicing.md) · [Nuxt 4](../nuxt/accounting-e-invoicing.md) · [Next.js](../nextjs/accounting-e-invoicing.md) · [React Native](../react-native/accounting-e-invoicing.md) · [Flutter & Dart](../flutter/accounting-e-invoicing.md)
<!-- core-implementation-plan:end -->
