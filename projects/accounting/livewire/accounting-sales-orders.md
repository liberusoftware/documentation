# Accounting: Accounting Sales Orders Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-sales-orders). Observed identity: [`liberusoftware/module-accounting-sales-orders-livewire`](../../../modules/source/liberusoftware--module-accounting-sales-orders-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-sales-orders-livewire`  
**Matching domain module:** `accounting-sales-orders`  
**Application:** Accounting  
**Source feature:** [Accounting Sales Orders](../features/accounting-sales-orders.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Accepted demand:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocation/fulfillment references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deposits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Partial invoicing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cancellation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Billing/Ecommerce integration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-sales-orders-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingSalesOrders::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `accepted-demand`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocation-fulfillment-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deposits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `partial-invoicing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cancellation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `billing-ecommerce-integration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-sales-orders` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-sales-orders.md) · [API plan](../api/accounting-sales-orders.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Accepted demand** | Expose a focused Livewire 4 component and namespaced Blade default view for `accepted demand` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocation/fulfillment references** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocation/fulfillment references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deposits** | Expose a focused Livewire 4 component and namespaced Blade default view for `deposits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Partial invoicing** | Expose a focused Livewire 4 component and namespaced Blade default view for `partial invoicing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Status** | Expose a focused Livewire 4 component and namespaced Blade default view for `status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cancellation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cancellation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Billing/Ecommerce integration** | Expose a focused Livewire 4 component and namespaced Blade default view for `billing/ecommerce integration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SalesOrders.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-livewire/src/Livewire/SalesOrders.php) · [SalesOrdersLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-livewire/src/SalesOrdersLivewireServiceProvider.php).

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
<!-- layer-implementation-plan:end -->
