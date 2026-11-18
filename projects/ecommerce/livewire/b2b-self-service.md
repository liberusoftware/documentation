# Ecommerce: B2B Self-Service Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#b2b-self-service). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-b2b-self-service-livewire`  
**Matching domain module:** `ecommerce-b2b-self-service`  
**Application:** Ecommerce  
**Source feature:** [B2B Self-Service](../features/b2b-self-service.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Company/location switching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Users/roles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared addresses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Catalogs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Orders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Returns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reordering:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-b2b-self-service-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-b2b-self-service::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `company-location-switching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `users-roles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-addresses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `catalogs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `orders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `returns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reordering`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-b2b-self-service` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/b2b-self-service.md) · [API plan](../api/b2b-self-service.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Company/location switching** | Expose a focused Livewire 4 component and namespaced Blade default view for `company/location switching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Users/roles** | Expose a focused Livewire 4 component and namespaced Blade default view for `users/roles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared addresses** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared addresses` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Catalogs** | Expose a focused Livewire 4 component and namespaced Blade default view for `catalogs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotes** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Orders** | Expose a focused Livewire 4 component and namespaced Blade default view for `orders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices references** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Returns** | Expose a focused Livewire 4 component and namespaced Blade default view for `returns` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reordering** | Expose a focused Livewire 4 component and namespaced Blade default view for `reordering` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
