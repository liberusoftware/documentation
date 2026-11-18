# CMS: Image Processing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#image-processing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-image-processing-livewire`  
**Matching domain module:** `cms-image-processing`  
**Application:** CMS  
**Source feature:** [Image Processing](../features/image-processing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Orientation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Crops/focal points:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Responsive variants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Format conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quality:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Optimization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CDN URLs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-image-processing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-image-processing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `orientation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `crops-focal-points`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `responsive-variants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `format-conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quality`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `optimization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cdn-urls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-image-processing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/image-processing.md) · [API plan](../api/image-processing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Orientation** | Expose a focused Livewire 4 component and namespaced Blade default view for `orientation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Crops/focal points** | Expose a focused Livewire 4 component and namespaced Blade default view for `crops/focal points` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Responsive variants** | Expose a focused Livewire 4 component and namespaced Blade default view for `responsive variants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Format conversion** | Expose a focused Livewire 4 component and namespaced Blade default view for `format conversion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quality** | Expose a focused Livewire 4 component and namespaced Blade default view for `quality` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Optimization** | Expose a focused Livewire 4 component and namespaced Blade default view for `optimization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CDN URLs** | Expose a focused Livewire 4 component and namespaced Blade default view for `cdn urls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
