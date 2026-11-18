# Billing: Invoicing Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#invoicing). Observed identity: [`liberusoftware/module-billing-invoicing`](../../../modules/source/liberusoftware--module-billing-invoicing.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-billing-invoicing`
**Domain specification:** [Invoicing](../features/invoicing.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Invoicing. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Schedules** | Model `schedules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Line generation** | Model `line generation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tax** | Model `tax` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Credits** | Model `credits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Adjustments** | Model `adjustments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **PDFs** | Model `pdfs` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delivery** | Model `delivery` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Finalization** | Model `finalization` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_050000_create_billing_invoicing_tables.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_24_050000_create_billing_invoicing_tables.php) · [2026_08_24_200000_create_billing_invoice_support_table.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_24_200000_create_billing_invoice_support_table.php) · [2026_08_29_010000_create_billing_payment_plans_table.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_29_010000_create_billing_payment_plans_table.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListInvoices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Queries/ListInvoices.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddInvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/AddInvoiceLine.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $description, int $quantity, int $unitAmountMinor, float $taxRate = 0): InvoiceLine` |
| [ApplyInvoiceAdjustment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceAdjustment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, string $reason, string $type = 'adjustment'): Invoice` |
| [ApplyInvoiceLateFee.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceLateFee.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, ?CarbonInterface $at = null): Invoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Invoice` |
| [CreateInvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSchedule.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): InvoiceSchedule` |
| [CreateInvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSupport.php) | `public function execute(int $teamId, array $attributes): InvoiceSupport` |
| [CreatePaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreatePaymentPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $totalInstallments, string $frequency = 'monthly', ?CarbonInterface $startAt = null): PaymentPlan` |
| [DeliverInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/DeliverInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $destination, ?int $documentId = null): InvoiceSupport` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/FinalizeInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice): Invoice` |
| [GenerateInvoiceDocument.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/GenerateInvoiceDocument.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $format = 'pdf'): InvoiceSupport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Invoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/Invoice.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSchedule.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSupport.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/PaymentPlan.php) | No literal fillable array detected; inspect the model and API schema. |

### Consuming adapter specifications

- [HTTP API contract](../api/invoicing.md) · [Filament 5](../filament/invoicing.md) · [Livewire 4](../livewire/invoicing.md) · [React + Inertia](../react/invoicing.md) · [Vue + Inertia](../vue/invoicing.md) · [Nuxt 4](../nuxt/invoicing.md) · [Next.js](../nextjs/invoicing.md) · [React Native](../react-native/invoicing.md) · [Flutter & Dart](../flutter/invoicing.md)
<!-- core-implementation-plan:end -->
