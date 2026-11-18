# CMS: Module Cms Menus Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-menus). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-menus-livewire`  
**Matching domain module:** `module-cms-menus`  
**Application:** CMS  
**Source feature:** [Module Cms Menus](../features/module-cms-menus.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Menu locations and trees:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Internal and external link targets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Visibility and audience rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Breadcrumbs and active state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Localized navigation structures:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-menus-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsMenus::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `menu-locations-and-trees`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `internal-and-external-link-targets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `visibility-and-audience-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `breadcrumbs-and-active-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `localized-navigation-structures`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-menus` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-menus.md) · [API plan](../api/module-cms-menus.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Menu locations and trees** | Expose a focused Livewire 4 component and namespaced Blade default view for `menu locations and trees` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Internal and external link targets** | Expose a focused Livewire 4 component and namespaced Blade default view for `internal and external link targets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Visibility and audience rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `visibility and audience rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Breadcrumbs and active state** | Expose a focused Livewire 4 component and namespaced Blade default view for `breadcrumbs and active state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Localized navigation structures** | Expose a focused Livewire 4 component and namespaced Blade default view for `localized navigation structures` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MenuRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Contracts/MenuRepositoryInterface.php) | `public function find(int $id): ?Menu`<br>`public function forLocation(string $location, string $variant = 'default'): ?Menu` |
| [MenuService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Services/MenuService.php) | `public function createMenu(array $attributes): Menu`<br>`public function updateMenu(Menu $menu, array $attributes): Menu`<br>`public function saveItem(Menu $menu, array $attributes, ?MenuItem $item = null): MenuItem`<br>`public function deleteItem(MenuItem $item): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Menu.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Models/Menu.php) | `name`, `location`, `variant`, `settings`, `team_id` |
| [MenuItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Models/MenuItem.php) | `menu_id`, `parent_id`, `label`, `url`, `link_type`, `content_id`, `system_route`, `sort`, `permission`, `visibility`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
