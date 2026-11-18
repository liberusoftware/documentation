# CMS: Module Cms Regions And Widgets Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-regions-and-widgets). Observed identity: [`liberusoftware/module-cms-regions-and-widgets-livewire`](../../../modules/source/liberusoftware--module-cms-regions-and-widgets-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-regions-and-widgets-livewire`  
**Matching domain module:** `module-cms-regions-and-widgets`  
**Application:** CMS  
**Source feature:** [Module Cms Regions And Widgets](../features/module-cms-regions-and-widgets.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Theme regions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reusable widgets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Placement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ordering:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Visibility by route/context/audience:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Caching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-regions-and-widgets-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsRegionsAndWidgets::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `theme-regions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reusable-widgets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `placement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ordering`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `visibility-by-route-context-audience`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `caching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-regions-and-widgets` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-regions-and-widgets.md) · [API plan](../api/module-cms-regions-and-widgets.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Theme regions** | Expose a focused Livewire 4 component and namespaced Blade default view for `theme regions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reusable widgets** | Expose a focused Livewire 4 component and namespaced Blade default view for `reusable widgets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Placement** | Expose a focused Livewire 4 component and namespaced Blade default view for `placement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ordering** | Expose a focused Livewire 4 component and namespaced Blade default view for `ordering` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Visibility by route/context/audience** | Expose a focused Livewire 4 component and namespaced Blade default view for `visibility by route/context/audience` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Caching** | Expose a focused Livewire 4 component and namespaced Blade default view for `caching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RegionRenderer.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-regions-and-widgets-livewire/src/Livewire/RegionRenderer.php) · [RegionsAndWidgetsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-regions-and-widgets-livewire/src/RegionsAndWidgetsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RegionWidgetService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Services/RegionWidgetService.php) | `public function region(string $key, ?int $teamId = null): Region`<br>`public function createRegion(string $key, string $label, ?string $theme = null, ?int $teamId = null): Region`<br>`public function createWidget(string $key, string $type, array $configuration = [], ?string $title = null, ?int $teamId = null): Widget`<br>`public function place(Region $region, Widget $widget, int $position = 0, array $visibility = [], ?string $startsAt = null, ?string $endsAt = null): WidgetPlacement`<br>`public function render(string $regionKey, array $context = [], ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Region.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Region.php) | `key`, `label`, `theme`, `team_id` |
| [Widget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Widget.php) | `key`, `type`, `title`, `configuration`, `active`, `team_id` |
| [WidgetPlacement.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/WidgetPlacement.php) | `region_id`, `widget_id`, `position`, `visibility`, `starts_at`, `ends_at`, `active` |
<!-- layer-implementation-plan:end -->
