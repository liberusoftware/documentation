# Accounting: Product and Service Items Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-and-service-items). Observed identity: [`liberusoftware/module-accounting-product-and-service-items-livewire`](../../../modules/source/liberusoftware--module-accounting-product-and-service-items-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-product-and-service-items-livewire`  
**Matching domain module:** `accounting-product-and-service-items`  
**Application:** Accounting  
**Source feature:** [Product and Service Items](../features/product-and-service-items.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Items/services:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Codes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Purchase/sales descriptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Accounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax defaults:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Units:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Costs/prices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ecommerce references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-product-and-service-items-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-product-and-service-items::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `items-services`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `codes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `purchase-sales-descriptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `accounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax-defaults`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `units`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `costs-prices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ecommerce-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-product-and-service-items` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/product-and-service-items.md) · [API plan](../api/product-and-service-items.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Items/services** | Expose a focused Livewire 4 component and namespaced Blade default view for `items/services` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Codes** | Expose a focused Livewire 4 component and namespaced Blade default view for `codes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Purchase/sales descriptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `purchase/sales descriptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Accounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `accounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax defaults** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax defaults` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Units** | Expose a focused Livewire 4 component and namespaced Blade default view for `units` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Costs/prices** | Expose a focused Livewire 4 component and namespaced Blade default view for `costs/prices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ecommerce references** | Expose a focused Livewire 4 component and namespaced Blade default view for `ecommerce references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-livewire/src/Livewire/AccountingItems.php) · [ProductAndServiceItemsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-livewire/src/ProductAndServiceItemsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FindAccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Queries/FindAccountingItems.php) | `public function search(?string $term = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SaveAccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Actions/SaveAccountingItem.php) | `public function handle(array $attributes): AccountingItem` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Models/AccountingItem.php) | `team_id`, `code`, `name`, `kind`, `purchase_description`, `sales_description`, `sales_account_ref`, `purchase_account_ref`, `tax_default_ref`, `unit`, `purchase_price`, `sales_price`, `currency`, `status`, `ecommerce_refs`, `metadata` |
<!-- layer-implementation-plan:end -->
