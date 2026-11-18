# Accounting: Supplier Portal Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#supplier-portal). Observed identity: [`liberusoftware/module-accounting-supplier-portal-livewire`](../../../modules/source/liberusoftware--module-accounting-supplier-portal-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-supplier-portal-livewire`  
**Matching domain module:** `accounting-supplier-portal`  
**Application:** Accounting  
**Source feature:** [Supplier Portal](../features/supplier-portal.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Profile/bank-change requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Purchase orders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payment status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Secure documents:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-supplier-portal-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-supplier-portal::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `profile-bank-change-requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `purchase-orders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payment-status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `secure-documents`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-supplier-portal` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/supplier-portal.md) · [API plan](../api/supplier-portal.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Profile/bank-change requests** | Expose a focused Livewire 4 component and namespaced Blade default view for `profile/bank-change requests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Purchase orders** | Expose a focused Livewire 4 component and namespaced Blade default view for `purchase orders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payment status** | Expose a focused Livewire 4 component and namespaced Blade default view for `payment status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Secure documents** | Expose a focused Livewire 4 component and namespaced Blade default view for `secure documents` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PortalResources.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-livewire/src/Livewire/PortalResources.php) · [SupplierPortalLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-livewire/src/SupplierPortalLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PortalResourceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Queries/PortalResourceQuery.php) | `public function paginate(?string $supplierId = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AttachPortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/AttachPortalDocument.php) | `public function handle(PortalResource $resource, array $attributes): PortalDocument` |
| [CreatePortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/CreatePortalResource.php) | `public function handle(array $attributes): PortalResource` |
| [TransitionPortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/TransitionPortalResource.php) | `public function handle(PortalResource $resource, PortalStatus\|string $status, ?string $reason = null): PortalResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalDocument.php) | `resource_id`, `path`, `original_name`, `mime_type`, `sha256`, `uploaded_by`, `metadata` |
| [PortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalResource.php) | `supplier_id`, `type`, `reference`, `status`, `currency`, `amount`, `payload`, `submitted_at`, `approved_at`, `rejected_reason`, `metadata` |
<!-- layer-implementation-plan:end -->
