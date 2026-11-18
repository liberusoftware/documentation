# Accounting: Supplier Bills Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#supplier-bills). Observed identity: [`liberusoftware/module-accounting-supplier-bills`](../../../modules/source/liberusoftware--module-accounting-supplier-bills.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-supplier-bills`
**Domain specification:** [Supplier Bills](../features/supplier-bills.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Supplier Bills. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Draft/approved/posted bills** | Model `draft/approved/posted bills` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Capture sources** | Model `capture sources` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Line coding** | Model `line coding` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tax** | Model `tax` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Due dates** | Model `due dates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Duplicate detection** | Model `duplicate detection` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Matching** | Model `matching` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Credits** | Model `credits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Documents** | Model `documents` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_100000_create_accounting_supplier_bills_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/database/migrations/2026_08_25_100000_create_accounting_supplier_bills_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DuplicateSupplierBillQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/DuplicateSupplierBillQuery.php) | `public function handle(int $partyId, string $billNumber, ?int $exceptId = null): Collection` |
| [SupplierBillAgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/SupplierBillAgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddSupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AddSupplierBillCredit.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [ApproveSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/ApproveSupplierBill.php) | `public function handle(SupplierBill $bill, ?int $actorId = null): SupplierBill` |
| [AttachSupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AttachSupplierBillDocument.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBillDocument` |
| [CreateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/CreateSupplierBill.php) | `public function handle(array $attributes, array $lines): SupplierBill` |
| [MatchSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/MatchSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [PostSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/PostSupplierBill.php) | `public function __construct(private readonly CreateOpenItem $createOpenItem)`<br>`public function handle(SupplierBill $bill): SupplierBill` |
| [RejectSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/RejectSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [UpdateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/UpdateSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes, array $lines): SupplierBill` |
| [VoidSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/VoidSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [SupplierBillsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Policies/SupplierBillsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $bill): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $bill): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBill.php) | `party_id`, `bill_number`, `bill_date`, `due_on`, `status`, `payment_status`, `subtotal`, `tax_total`, `total`, `amount_paid`, `currency`, `capture_source`, `purchase_order_reference`, `reference_number`, `notes`, `approval_status`, `approved_by`, `approved_at`, `rejection_reason`, `recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `external_ids`, `metadata` |
| [SupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillCredit.php) | `bill_id`, `amount`, `currency`, `reason`, `reference`, `metadata` |
| [SupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillDocument.php) | `bill_id`, `path`, `original_name`, `mime_type`, `sha256`, `metadata` |
| [SupplierBillLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillLine.php) | `bill_id`, `account_code`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |
| [SupplierBillMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillMatch.php) | `bill_id`, `match_type`, `matched_type`, `matched_id`, `quantity`, `amount`, `status`, `metadata` |
| [Supplier.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Models/Supplier.php) | `payment_term_id`, `supplier_first_name`, `supplier_last_name`, `supplier_email`, `supplier_address`, `supplier_phone_number`, `supplier_limit_credit`, `supplier_tin` |

### Consuming adapter specifications

- [HTTP API contract](../api/supplier-bills.md) · [Filament 5](../filament/supplier-bills.md) · [Livewire 4](../livewire/supplier-bills.md) · [React + Inertia](../react/supplier-bills.md) · [Vue + Inertia](../vue/supplier-bills.md) · [Nuxt 4](../nuxt/supplier-bills.md) · [Next.js](../nextjs/supplier-bills.md) · [React Native](../react-native/supplier-bills.md) · [Flutter & Dart](../flutter/supplier-bills.md)
<!-- core-implementation-plan:end -->
