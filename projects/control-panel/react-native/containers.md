# Containers React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#containers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-containers-react-native
**Matching core package:** module-control-panel-containers ([implementation](../core/containers.md))
**Matching API package:** module-control-panel-containers-api ([contract](../api/containers.md))

## Implementation plan

This adapter presents Containers for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Containers API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/containers.md), and [API module](../api/containers.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `containers`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/containers.md)) |
| Capability React Native module skeleton | [`module-control-panel-containers-react-native`](https://github.com/liberusoftware/module-control-panel-containers-react-native) (`@liberusoftware/module-control-panel-containers-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Images** | Progressive mobile list/detail/sheet flow for `images` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Registries** | Progressive mobile list/detail/sheet flow for `registries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Workloads** | Progressive mobile list/detail/sheet flow for `workloads` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Networks** | Progressive mobile list/detail/sheet flow for `networks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Volumes** | Progressive mobile list/detail/sheet flow for `volumes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Secrets** | Progressive mobile list/detail/sheet flow for `secrets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Limits** | Progressive mobile list/detail/sheet flow for `limits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lifecycle** | Progressive mobile list/detail/sheet flow for `lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
