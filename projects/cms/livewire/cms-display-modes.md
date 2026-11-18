# CMS: Cms Display Modes Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-display-modes). Observed identity: [`liberusoftware/module-cms-display-modes-livewire`](../../../modules/source/liberusoftware--module-cms-display-modes-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-display-modes-livewire`  
**Matching domain module:** `cms-display-modes`  
**Application:** CMS  
**Source feature:** [Cms Display Modes](../features/cms-display-modes.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Named view/form modes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Field formatters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Per-type display configuration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Responsive variants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **API projections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-display-modes-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsDisplayModes::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `named-view-form-modes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `field-formatters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `per-type-display-configuration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `responsive-variants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `api-projections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-display-modes` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-display-modes.md) · [API plan](../api/cms-display-modes.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Named view/form modes** | Expose a focused Livewire 4 component and namespaced Blade default view for `named view/form modes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Field formatters** | Expose a focused Livewire 4 component and namespaced Blade default view for `field formatters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Per-type display configuration** | Expose a focused Livewire 4 component and namespaced Blade default view for `per-type display configuration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Responsive variants** | Expose a focused Livewire 4 component and namespaced Blade default view for `responsive variants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **API projections** | Expose a focused Livewire 4 component and namespaced Blade default view for `api projections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ModePicker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-display-modes-livewire/src/Livewire/ModePicker.php) · [DisplayModesLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-display-modes-livewire/src/DisplayModesLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DisplayModesService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-display-modes/src/Services/DisplayModesService.php) | `public function modes(?int $teamId, ?string $contentType = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $teamId = null): DisplayMode`<br>`public function select(string $contentType, ?int $teamId, string $slug = 'default', ?string $variant = null): ?DisplayMode` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DisplayMode.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-display-modes/src/Models/DisplayMode.php) | `team_id`, `name`, `slug`, `content_type`, `mode_type`, `formatters`, `configuration`, `responsive_variants`, `projection`, `active` |
<!-- layer-implementation-plan:end -->
