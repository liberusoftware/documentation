# Ecommerce: Promotions Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#promotions). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-promotions-livewire`  
**Matching domain module:** `ecommerce-promotions`  
**Application:** Ecommerce  
**Source feature:** [Promotions](../features/promotions.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Codes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Automatic discounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Buy-X-get-Y:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bundles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Free shipping/gifts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Customer/product eligibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Limits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fraud controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-promotions-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-promotions::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `codes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `automatic-discounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `buy-x-get-y`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bundles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `free-shipping-gifts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `customer-product-eligibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `limits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fraud-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-promotions` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/promotions.md) · [API plan](../api/promotions.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Codes** | Expose a focused Livewire 4 component and namespaced Blade default view for `codes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Automatic discounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `automatic discounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Buy-X-get-Y** | Expose a focused Livewire 4 component and namespaced Blade default view for `buy-x-get-y` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bundles** | Expose a focused Livewire 4 component and namespaced Blade default view for `bundles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Free shipping/gifts** | Expose a focused Livewire 4 component and namespaced Blade default view for `free shipping/gifts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Customer/product eligibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `customer/product eligibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Limits** | Expose a focused Livewire 4 component and namespaced Blade default view for `limits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fraud controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `fraud controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
