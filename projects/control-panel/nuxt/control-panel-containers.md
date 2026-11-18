# Control Panel: Control Panel Containers Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-containers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-containers-nuxt`
**Matching domain module:** `control-panel-containers`
**Application:** Control Panel
**Source feature:** [Control Panel Containers](../features/control-panel-containers.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-containers.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-containers` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Images:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Registries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Workloads:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Networks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Volumes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Secrets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Limits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-containers-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `images`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `registries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `workloads`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `networks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `volumes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `secrets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `limits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-containers` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-containers.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-containers-nuxt`](https://github.com/liberusoftware/module-control-panel-containers-nuxt) (`@liberusoftware/module-control-panel-containers-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Images** | Expose composable and Vue 3 component for `images` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Registries** | Expose composable and Vue 3 component for `registries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Workloads** | Expose composable and Vue 3 component for `workloads` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Networks** | Expose composable and Vue 3 component for `networks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Volumes** | Expose composable and Vue 3 component for `volumes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Secrets** | Expose composable and Vue 3 component for `secrets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Limits** | Expose composable and Vue 3 component for `limits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Lifecycle** | Expose composable and Vue 3 component for `lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-containers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkloadController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-api/src/Http/Controllers/WorkloadController.php) | `public function index(Request $request, ListWorkloads $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function assets(Request $request): JsonResponse`<br>`public function store(Request $request, RegisterWorkload $register): JsonResponse`<br>`public function start(Request $request, Workload $workload, StartWorkload $start): JsonResponse`<br>`public function stop(Request $request, Workload $workload, StopWorkload $stop): JsonResponse`<br>`public function delete(Request $request, Workload $workload, DeleteWorkload $delete): JsonResponse`<br>`public function resourceRecord(Request $request, RecordContainerResource $record): JsonResponse`<br>`public function asset(Request $request, RegisterContainerAsset $register): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-containers-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/containers')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [WorkloadController::class, 'index'])->name('control-panel.containers.index');
Route::post('/', [WorkloadController::class, 'store'])->name('control-panel.containers.store');
Route::get('/assets', [WorkloadController::class, 'assets'])->name('control-panel.containers.assets.index');
Route::post('/resources', [WorkloadController::class, 'resourceRecord'])->name('control-panel.containers.resources.store');
Route::post('/assets', [WorkloadController::class, 'asset'])->name('control-panel.containers.assets.store');
Route::post('{workload}/start', [WorkloadController::class, 'start'])->name('control-panel.containers.start');
Route::post('{workload}/stop', [WorkloadController::class, 'stop'])->name('control-panel.containers.stop');
Route::delete('{workload}', [WorkloadController::class, 'delete'])->name('control-panel.containers.delete');
Route::get('{workload}', [WorkloadController::class, 'show'])->name('control-panel.containers.show');
```
<!-- layer-implementation-plan:end -->
