# Containers: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-containers`.

**Proposed design identifier:** `module-control-panel-containers-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/containers.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-containers](../../../modules/source/liberusoftware--module-control-panel-containers.md) |
| API | [liberusoftware/module-control-panel-containers-api](../../../modules/source/liberusoftware--module-control-panel-containers-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Images | A focused authorized view or workflow section for images; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Registries | A focused authorized view or workflow section for registries; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Workloads | A focused authorized view or workflow section for workloads; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Networks | A focused authorized view or workflow section for networks; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Volumes | A focused authorized view or workflow section for volumes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Secrets | A focused authorized view or workflow section for secrets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Limits | A focused authorized view or workflow section for limits; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Lifecycle | A focused authorized view or workflow section for lifecycle; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListWorkloads.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Queries/ListWorkloads.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [DeleteWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/DeleteWorkload.php) | `public function execute(Workload $workload): void` |
| [RecordContainerResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RecordContainerResource.php) | `public function execute(array $a): ContainerResource` |
| [RegisterContainerAsset.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterContainerAsset.php) | `public function execute(array $attributes): Model` |
| [RegisterWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/RegisterWorkload.php) | `public function execute(array $attributes): Workload` |
| [StartWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StartWorkload.php) | `public function execute(Workload $workload): Workload` |
| [StopWorkload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Actions/StopWorkload.php) | `public function execute(Workload $workload): Workload` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ContainerImage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerImage.php) | `id`, `team_id`, `repository`, `tag`, `digest`, `size_bytes`, `architecture`, `status`, `metadata` |
| [ContainerLifecycle.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLifecycle.php) | `id`, `team_id`, `workload_id`, `operation`, `status`, `idempotency_key`, `requested_at`, `completed_at`, `details` |
| [ContainerLimit.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerLimit.php) | `id`, `team_id`, `workload_id`, `cpu_millis`, `memory_bytes`, `pids`, `restart_policy` |
| [ContainerNetwork.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerNetwork.php) | `id`, `team_id`, `name`, `driver`, `subnet`, `gateway`, `options`, `status` |
| [ContainerRegistry.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerRegistry.php) | `id`, `team_id`, `name`, `endpoint`, `username`, `credential`, `tls_verify`, `active` |
| [ContainerResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerResource.php) | `id`, `team_id`, `workload_id`, `kind`, `name`, `status`, `spec` |
| [ContainerSecret.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerSecret.php) | `id`, `team_id`, `name`, `value`, `metadata`, `active` |
| [ContainerVolume.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/ContainerVolume.php) | `id`, `team_id`, `name`, `driver`, `mount_path`, `size_bytes`, `status`, `metadata` |
| [Workload.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers/src/Models/Workload.php) | `team_id`, `node_id`, `name`, `image`, `status`, `specification` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-containers-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-containers-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
