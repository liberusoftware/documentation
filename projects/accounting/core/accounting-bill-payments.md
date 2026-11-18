# Accounting: Accounting Bill Payments Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bill-payments). Observed identity: [`liberusoftware/module-accounting-bill-payments`](../../../modules/source/liberusoftware--module-accounting-bill-payments.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-bill-payments`
**Domain specification:** [Accounting Bill Payments](../features/accounting-bill-payments.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting Bill Payments. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Payment proposals** | Model `payment proposals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Due-date/discount optimization** | Model `due-date/discount optimization` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Bank details validation** | Model `bank details validation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Maker-checker approval** | Model `maker-checker approval` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Files/APIs** | Model `files/apis` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Remittances** | Model `remittances` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Status** | Model `status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_30_130000_create_accounting_bill_payment_proposals_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/database/migrations/2026_08_30_130000_create_accounting_bill_payment_proposals_table.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BillPaymentOptimizationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Queries/BillPaymentOptimizationQuery.php) | `public function handle(BillPaymentProposal $payment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/ApproveBillPayment.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [CreateBillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/CreateBillPaymentProposal.php) | `public function handle(array $attributes): BillPaymentProposal` |
| [MarkBillPaymentPaid.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/MarkBillPaymentPaid.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [RejectBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RejectBillPayment.php) | `public function handle(BillPaymentProposal $payment, string $reason): BillPaymentProposal` |
| [RequestBillPaymentApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RequestBillPaymentApproval.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [SubmitBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/SubmitBillPayment.php) | `public function handle(BillPaymentProposal $payment, PaymentProviderAdapter $adapter): BillPaymentProposal` |
| [BillPaymentsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Policies/BillPaymentsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $payment): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $payment): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Models/BillPaymentProposal.php) | `team_id`, `supplier_id`, `bill_reference`, `amount`, `currency`, `due_date`, `discount_date`, `discount_rate`, `payment_date`, `bank_details`, `provider`, `provider_connection_id`, `payment_payload`, `idempotency_key`, `status`, `requested_by`, `approved_by`, `approved_at`, `submitted_at`, `paid_at`, `rejected_at`, `failure_code`, `failure_message`, `provider_reference`, `provider_result`, `remittance_reference`, `remittance_sent_at`, `metadata` |
| [Bill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/Bill.php) | `vendor_id`, `bill_number`, `bill_date`, `due_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `amount_paid`, `tax_rate_id`, `status`, `payment_status`, `purchase_order_id`, `reference_number`, `notes`, `document_path`, `approved_by`, `approved_at`, `approval_status`, `rejection_reason`, `team_id`, `is_recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
| [BillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/BillPayment.php) | `bill_id`, `payment_date`, `amount`, `payment_method`, `reference_number`, `bank_account_id`, `notes` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-bill-payments.md) · [Filament 5](../filament/accounting-bill-payments.md) · [Livewire 4](../livewire/accounting-bill-payments.md) · [React + Inertia](../react/accounting-bill-payments.md) · [Vue + Inertia](../vue/accounting-bill-payments.md) · [Nuxt 4](../nuxt/accounting-bill-payments.md) · [Next.js](../nextjs/accounting-bill-payments.md) · [React Native](../react-native/accounting-bill-payments.md) · [Flutter & Dart](../flutter/accounting-bill-payments.md)
<!-- core-implementation-plan:end -->
