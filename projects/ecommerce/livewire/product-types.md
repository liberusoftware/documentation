# Ecommerce: Product Types Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-types). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-product-types-livewire`  
**Matching domain module:** `ecommerce-product-types`  
**Application:** Ecommerce  
**Source feature:** [Product Types](../features/product-types.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Simple:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configurable/variant:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grouped:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bundle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Kit:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Virtual:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Downloadable:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Service:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Subscription:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gift card:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Custom type contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-product-types-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-product-types::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `simple`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configurable-variant`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grouped`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bundle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `kit`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `virtual`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `downloadable`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `service`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `subscription`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gift-card`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `custom-type-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-product-types` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/product-types.md) · [API plan](../api/product-types.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Simple** | Expose a focused Livewire 4 component and namespaced Blade default view for `simple` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Configurable/variant** | Expose a focused Livewire 4 component and namespaced Blade default view for `configurable/variant` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grouped** | Expose a focused Livewire 4 component and namespaced Blade default view for `grouped` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bundle** | Expose a focused Livewire 4 component and namespaced Blade default view for `bundle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Kit** | Expose a focused Livewire 4 component and namespaced Blade default view for `kit` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Virtual** | Expose a focused Livewire 4 component and namespaced Blade default view for `virtual` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Downloadable** | Expose a focused Livewire 4 component and namespaced Blade default view for `downloadable` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Service** | Expose a focused Livewire 4 component and namespaced Blade default view for `service` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Subscription** | Expose a focused Livewire 4 component and namespaced Blade default view for `subscription` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gift card** | Expose a focused Livewire 4 component and namespaced Blade default view for `gift card` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Custom type contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `custom type contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
