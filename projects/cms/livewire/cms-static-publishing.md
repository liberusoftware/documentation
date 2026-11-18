# CMS: Cms Static Publishing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-static-publishing). Observed identity: [`liberusoftware/module-cms-static-publishing-livewire`](../../../modules/source/liberusoftware--module-cms-static-publishing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-static-publishing-livewire`  
**Matching domain module:** `cms-static-publishing`  
**Application:** CMS  
**Source feature:** [Cms Static Publishing](../features/cms-static-publishing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Full/incremental builds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Route manifests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cache invalidation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deployment adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preview builds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rollback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Build diagnostics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-static-publishing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsStaticPublishing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `full-incremental-builds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `route-manifests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cache-invalidation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deployment-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preview-builds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rollback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `build-diagnostics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-static-publishing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-static-publishing.md) · [API plan](../api/cms-static-publishing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Full/incremental builds** | Expose a focused Livewire 4 component and namespaced Blade default view for `full/incremental builds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Route manifests** | Expose a focused Livewire 4 component and namespaced Blade default view for `route manifests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cache invalidation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cache invalidation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deployment adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `deployment adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preview builds** | Expose a focused Livewire 4 component and namespaced Blade default view for `preview builds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rollback** | Expose a focused Livewire 4 component and namespaced Blade default view for `rollback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Build diagnostics** | Expose a focused Livewire 4 component and namespaced Blade default view for `build diagnostics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BuildMonitor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-static-publishing-livewire/src/Livewire/BuildMonitor.php) · [StaticPublishingLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-static-publishing-livewire/src/StaticPublishingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [StaticPublishingQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Queries/StaticPublishingQuery.php) | `public function builds(int $perPage = 15): LengthAwarePaginator`<br>`public function build(int\|string $id): ?StaticBuild` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DeploymentAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Contracts/DeploymentAdapterInterface.php) | `public function key(): string`<br>`public function deploy(StaticBuild $build): array` |
| [StaticPublishingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Services/StaticPublishingService.php) | `public function __construct(private DeploymentAdapterRegistry $deployments)`<br>`public function build(array $routes, ?string $siteKey = null, string $kind = 'full', string $deployment = 'local', ?StaticBuild $parent = null): StaticBuild`<br>`public function invalidate(StaticBuild $build, string $path, string $reason = 'content-changed'): StaticInvalidation`<br>`public function rollback(StaticBuild $build): StaticBuild`<br>`public function diagnostics(StaticBuild $build): array`<br>`public function deploy(StaticBuild $build, string $adapter): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StaticBuild.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticBuild.php) | `site_key`, `state`, `kind`, `deployment`, `manifest`, `diagnostics`, `parent_build_id`, `checksum`, `started_at`, `finished_at`, `team_id` |
| [StaticInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticInvalidation.php) | `build_id`, `path`, `reason`, `created_at` |
<!-- layer-implementation-plan:end -->
