# CMS: Module Cms Seo Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-seo). Observed identity: [`liberusoftware/module-cms-seo-livewire`](../../../modules/source/liberusoftware--module-cms-seo-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-seo-livewire`  
**Matching domain module:** `module-cms-seo`  
**Application:** CMS  
**Source feature:** [Module Cms Seo](../features/module-cms-seo.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Titles/descriptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Canonical URLs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Robots:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Structured data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Social cards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hreflang:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Index controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Content checks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-seo-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsSeo::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `titles-descriptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `canonical-urls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `robots`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `structured-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `social-cards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hreflang`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `index-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `content-checks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-seo` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-seo.md) · [API plan](../api/module-cms-seo.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Titles/descriptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `titles/descriptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Canonical URLs** | Expose a focused Livewire 4 component and namespaced Blade default view for `canonical urls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Robots** | Expose a focused Livewire 4 component and namespaced Blade default view for `robots` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Structured data** | Expose a focused Livewire 4 component and namespaced Blade default view for `structured data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Social cards** | Expose a focused Livewire 4 component and namespaced Blade default view for `social cards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hreflang** | Expose a focused Livewire 4 component and namespaced Blade default view for `hreflang` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Index controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `index controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Content checks** | Expose a focused Livewire 4 component and namespaced Blade default view for `content checks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SeoCheck.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-seo-livewire/src/Livewire/SeoCheck.php) · [SeoLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-seo-livewire/src/SeoLivewireServiceProvider.php).

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SeoMetadata.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-seo/src/Models/SeoMetadata.php) | `seoable_type`, `seoable_id`, `title`, `description`, `canonical_url`, `robots`, `structured_data`, `social_cards`, `hreflang`, `noindex`, `noarchive`, `team_id` |
<!-- layer-implementation-plan:end -->
