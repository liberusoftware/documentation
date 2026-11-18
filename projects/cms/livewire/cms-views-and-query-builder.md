# CMS: Cms Views And Query Builder Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-views-and-query-builder). Observed identity: [`liberusoftware/module-cms-views-and-query-builder-livewire`](../../../modules/source/liberusoftware--module-cms-views-and-query-builder-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-views-and-query-builder-livewire`  
**Matching domain module:** `cms-views-and-query-builder`  
**Application:** CMS  
**Source feature:** [Cms Views And Query Builder](../features/cms-views-and-query-builder.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Permission-safe listings from content/fields/relationships with filters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sorting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grouping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exposed filters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pagination:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feeds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Displays:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-views-and-query-builder-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsViewsAndQueryBuilder::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `permission-safe-listings-from-content-fields-relationships-with-filters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sorting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grouping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exposed-filters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pagination`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feeds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `displays`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-views-and-query-builder` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-views-and-query-builder.md) · [API plan](../api/cms-views-and-query-builder.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Permission-safe listings from content/fields/relationships with filters** | Expose a focused Livewire 4 component and namespaced Blade default view for `permission-safe listings from content/fields/relationships with filters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sorting** | Expose a focused Livewire 4 component and namespaced Blade default view for `sorting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grouping** | Expose a focused Livewire 4 component and namespaced Blade default view for `grouping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exposed filters** | Expose a focused Livewire 4 component and namespaced Blade default view for `exposed filters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pagination** | Expose a focused Livewire 4 component and namespaced Blade default view for `pagination` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feeds** | Expose a focused Livewire 4 component and namespaced Blade default view for `feeds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Displays** | Expose a focused Livewire 4 component and namespaced Blade default view for `displays` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ViewBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-livewire/src/Livewire/ViewBrowser.php) · [ViewsAndQueryBuilderLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-livewire/src/ViewsAndQueryBuilderLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListingQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ListingQueryService.php) | `public function execute(ViewDefinition $view, int $perPage = 15, array $input = []): LengthAwarePaginator` |
| [ViewDefinitionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ViewDefinitionQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $slug): ?ViewDefinition`<br>`public function publishedList(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function findPublished(string $slug): ?ViewDefinition` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewDefinitionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Actions/ViewDefinitionMutationService.php) | `public function create(array $attributes): ViewDefinition`<br>`public function update(ViewDefinition $view, array $attributes): ViewDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ViewDefinition.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Models/ViewDefinition.php) | `name`, `slug`, `source`, `description`, `definition`, `visibility`, `status`, `published_at`, `user_id`, `team_id` |
<!-- layer-implementation-plan:end -->
