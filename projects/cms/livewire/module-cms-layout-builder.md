# CMS: Module Cms Layout Builder Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-layout-builder). Observed identity: [`liberusoftware/module-cms-layout-builder-livewire`](../../../modules/source/liberusoftware--module-cms-layout-builder-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-layout-builder-livewire`  
**Matching domain module:** `module-cms-layout-builder`  
**Application:** CMS  
**Source feature:** [Module Cms Layout Builder](../features/module-cms-layout-builder.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Regions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grids:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drag/drop composition:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Type defaults:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Per-record overrides:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Responsive settings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Permissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-layout-builder-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsLayoutBuilder::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `regions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grids`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drag-drop-composition`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `type-defaults`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `per-record-overrides`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `responsive-settings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `permissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-layout-builder` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-layout-builder.md) · [API plan](../api/module-cms-layout-builder.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Regions** | Expose a focused Livewire 4 component and namespaced Blade default view for `regions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grids** | Expose a focused Livewire 4 component and namespaced Blade default view for `grids` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sections** | Expose a focused Livewire 4 component and namespaced Blade default view for `sections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drag/drop composition** | Expose a focused Livewire 4 component and namespaced Blade default view for `drag/drop composition` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Type defaults** | Expose a focused Livewire 4 component and namespaced Blade default view for `type defaults` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Per-record overrides** | Expose a focused Livewire 4 component and namespaced Blade default view for `per-record overrides` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Responsive settings** | Expose a focused Livewire 4 component and namespaced Blade default view for `responsive settings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Permissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `permissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [LayoutBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-layout-builder-livewire/src/Livewire/LayoutBrowser.php) · [LayoutBuilderLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-layout-builder-livewire/src/LayoutBuilderLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LayoutBuilderService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-layout-builder/src/Services/LayoutBuilderService.php) | `public function create(array $attributes): Layout`<br>`public function update(Layout $layout, array $attributes): Layout`<br>`public function publish(Layout $layout): Layout`<br>`public function resolve(string $targetType, int\|string $targetId, ?string $slug = null): ?Layout` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Layout.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-layout-builder/src/Models/Layout.php) | `name`, `slug`, `target_type`, `target_id`, `definition`, `status`, `published_at`, `user_id`, `team_id` |
<!-- layer-implementation-plan:end -->
