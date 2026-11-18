# Accounting: Accounting Sales Orders Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-sales-orders). Observed identity: [`liberusoftware/module-accounting-sales-orders`](../../../modules/source/liberusoftware--module-accounting-sales-orders.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-accounting-accounting-sales-orders`
**Domain specification:** [Accounting Sales Orders](../features/accounting-sales-orders.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Accounting Sales Orders. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Accepted demand** | Model `accepted demand` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Allocation/fulfillment references** | Model `allocation/fulfillment references` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Deposits** | Model `deposits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Partial invoicing** | Model `partial invoicing` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Status** | Model `status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cancellation** | Model `cancellation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Billing/Ecommerce integration** | Model `billing/ecommerce integration` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_160000_create_accounting_sales_order_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/database/migrations/2026_08_25_160000_create_accounting_sales_order_tables.php) · [2026_08_29_000001_add_team_id_to_accounting_sales_orders.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/database/migrations/2026_08_29_000001_add_team_id_to_accounting_sales_orders.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SalesOrderQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Queries/SalesOrderQuery.php) | `public function paginate(?string $customer = null, ?string $status = null, int $perPage = 25, ?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFulfillmentReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddFulfillmentReference.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderAllocation` |
| [AddSalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddSalesOrderDeposit.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderDeposit` |
| [CreateSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/CreateSalesOrder.php) | `public function handle(array $attributes, array $lines): SalesOrder` |
| [RecordPartialInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/RecordPartialInvoice.php) | `public function handle(SalesOrder $order, float $amount, string $invoiceReference): SalesOrder` |
| [TransitionSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/TransitionSalesOrder.php) | `public function handle(SalesOrder $order, OrderStatus\|string $status): SalesOrder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrder.php) | `team_id`, `customer_id`, `estimate_id`, `order_number`, `order_date`, `status`, `currency`, `subtotal`, `tax_total`, `total`, `invoiced_total`, `notes`, `metadata` |
| [SalesOrderAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderAllocation.php) | `sales_order_id`, `item_id`, `fulfillment_type`, `fulfillment_id`, `quantity`, `status`, `metadata` |
| [SalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderDeposit.php) | `sales_order_id`, `reference`, `amount`, `currency`, `status`, `metadata` |
| [SalesOrderItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderItem.php) | `sales_order_id`, `sku`, `description`, `quantity`, `unit_price`, `amount`, `tax_rate`, `tax_amount`, `invoiced_quantity`, `metadata` |
| [SalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-api/src/Models/SalesOrder.php) | `customer_id`, `estimate_id`, `sales_order_number`, `order_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `status`, `notes`, `team_id` |

### Consuming adapter specifications

- [HTTP API contract](../api/accounting-sales-orders.md) · [Filament 5](../filament/accounting-sales-orders.md) · [Livewire 4](../livewire/accounting-sales-orders.md) · [React + Inertia](../react/accounting-sales-orders.md) · [Vue + Inertia](../vue/accounting-sales-orders.md) · [Nuxt 4](../nuxt/accounting-sales-orders.md) · [Next.js](../nextjs/accounting-sales-orders.md) · [React Native](../react-native/accounting-sales-orders.md) · [Flutter & Dart](../flutter/accounting-sales-orders.md)
<!-- core-implementation-plan:end -->
