# CMS: Module Cms Search Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-search). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-search-livewire`  
**Matching domain module:** `module-cms-search`  
**Application:** CMS  
**Source feature:** [Module Cms Search](../features/module-cms-search.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Authorized indexing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Search contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Filters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pagination:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reindexing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-search-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsSearch::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `authorized-indexing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `search-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `filters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pagination`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reindexing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-search` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-search.md) · [API plan](../api/module-cms-search.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Authorized indexing** | Expose a focused Livewire 4 component and namespaced Blade default view for `authorized indexing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Search contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `search contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Filters** | Expose a focused Livewire 4 component and namespaced Blade default view for `filters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pagination** | Expose a focused Livewire 4 component and namespaced Blade default view for `pagination` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reindexing** | Expose a focused Livewire 4 component and namespaced Blade default view for `reindexing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentSearchService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Services/ContentSearchService.php) | `public function __construct(private SearchIndexInterface $index)`<br>`public function search(string $query, ?int $teamId = null, string $source = 'api'): array`<br>`public function analytics(?int $teamId, int $perPage = 25): LengthAwarePaginator`<br>`public function autocomplete(string $prefix, ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SearchAnalytic.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Models/SearchAnalytic.php) | `team_id`, `query`, `result_count`, `duration_ms`, `source` |
<!-- layer-implementation-plan:end -->
