# Control Panel: Containers Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#containers). Observed identity: [`liberusoftware/module-control-panel-containers-livewire`](../../../modules/source/liberusoftware--module-control-panel-containers-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-containers-livewire`  
**Matching domain module:** `control-panel-containers`  
**Application:** Control Panel  
**Source feature:** [Containers](../features/containers.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Images:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Registries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Workloads:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Networks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Volumes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Secrets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Limits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-containers-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-control-panel-containers::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `images`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `registries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `workloads`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `networks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `volumes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `secrets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `limits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-containers` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/containers.md) · [API plan](../api/containers.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Images** | Expose a focused Livewire 4 component and namespaced Blade default view for `images` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Registries** | Expose a focused Livewire 4 component and namespaced Blade default view for `registries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Workloads** | Expose a focused Livewire 4 component and namespaced Blade default view for `workloads` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Networks** | Expose a focused Livewire 4 component and namespaced Blade default view for `networks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Volumes** | Expose a focused Livewire 4 component and namespaced Blade default view for `volumes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Secrets** | Expose a focused Livewire 4 component and namespaced Blade default view for `secrets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Limits** | Expose a focused Livewire 4 component and namespaced Blade default view for `limits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ContainerAssetInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-livewire/src/Components/ContainerAssetInventory.php) · [WorkloadInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-livewire/src/Components/WorkloadInventory.php) · [ContainersLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-livewire/src/ContainersLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListWorkloads.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Queries/ListWorkloads.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DeleteWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/DeleteWorkload.php) | `public function execute(Workload $workload): void` |
| [RecordContainerResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RecordContainerResource.php) | `public function execute(array $a): ContainerResource` |
| [RegisterContainerAsset.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterContainerAsset.php) | `public function execute(array $attributes): Model` |
| [RegisterWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterWorkload.php) | `public function execute(array $attributes): Workload` |
| [StartWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StartWorkload.php) | `public function execute(Workload $workload): Workload` |
| [StopWorkload.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StopWorkload.php) | `public function execute(Workload $workload): Workload` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContainerImage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerImage.php) | `id`, `team_id`, `repository`, `tag`, `digest`, `size_bytes`, `architecture`, `status`, `metadata` |
| [ContainerLifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLifecycle.php) | `id`, `team_id`, `workload_id`, `operation`, `status`, `idempotency_key`, `requested_at`, `completed_at`, `details` |
| [ContainerLimit.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLimit.php) | `id`, `team_id`, `workload_id`, `cpu_millis`, `memory_bytes`, `pids`, `restart_policy` |
| [ContainerNetwork.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerNetwork.php) | `id`, `team_id`, `name`, `driver`, `subnet`, `gateway`, `options`, `status` |
| [ContainerRegistry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerRegistry.php) | `id`, `team_id`, `name`, `endpoint`, `username`, `credential`, `tls_verify`, `active` |
| [ContainerResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerResource.php) | `id`, `team_id`, `workload_id`, `kind`, `name`, `status`, `spec` |
| [ContainerSecret.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerSecret.php) | `id`, `team_id`, `name`, `value`, `metadata`, `active` |
| [ContainerVolume.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerVolume.php) | `id`, `team_id`, `name`, `driver`, `mount_path`, `size_bytes`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
