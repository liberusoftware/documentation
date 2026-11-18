# Accounting: Sales Tax and GST Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-tax-and-gst). Observed identity: [`liberusoftware/module-accounting-sales-tax-and-gst-livewire`](../../../modules/source/liberusoftware--module-accounting-sales-tax-and-gst-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-sales-tax-and-gst-livewire`  
**Matching domain module:** `accounting-sales-tax-and-gst`  
**Application:** Accounting  
**Source feature:** [Sales Tax and GST](../features/sales-tax-and-gst.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Registrations/nexus:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Destination/origin rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Taxable bases:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Liabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Return periods:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calculation adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-sales-tax-and-gst-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-sales-tax-and-gst::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `registrations-nexus`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `destination-origin-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `taxable-bases`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `liabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `return-periods`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calculation-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-sales-tax-and-gst` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/sales-tax-and-gst.md) · [API plan](../api/sales-tax-and-gst.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Registrations/nexus** | Expose a focused Livewire 4 component and namespaced Blade default view for `registrations/nexus` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Destination/origin rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `destination/origin rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Taxable bases** | Expose a focused Livewire 4 component and namespaced Blade default view for `taxable bases` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Liabilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `liabilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Adjustments** | Expose a focused Livewire 4 component and namespaced Blade default view for `adjustments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Return periods** | Expose a focused Livewire 4 component and namespaced Blade default view for `return periods` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calculation adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `calculation adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SalesTaxRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-livewire/src/Livewire/SalesTaxRecords.php) · [SalesTaxAndGstLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-livewire/src/SalesTaxAndGstLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SalesTaxRecordQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Queries/SalesTaxRecordQuery.php) | `public function paginate(?string $context = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/ActivateSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CloseSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CloseSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CreateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CreateSalesTaxRecord.php) | `public function handle(array $attributes): SalesTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Models/SalesTaxRecord.php) | `context_id`, `type`, `jurisdiction`, `origin`, `destination`, `rate`, `taxable_base`, `liability`, `status`, `period_start`, `period_end`, `metadata` |
<!-- layer-implementation-plan:end -->
