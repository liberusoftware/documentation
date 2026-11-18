# Control Panel Os Adapters React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-os-adapters). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-os-adapters-react-native
**Matching core package:** module-control-panel-control-panel-os-adapters ([implementation](../core/control-panel-os-adapters.md))
**Matching API package:** module-control-panel-control-panel-os-adapters-api ([contract](../api/control-panel-os-adapters.md))

## Implementation plan

This adapter presents Control Panel Os Adapters for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Os Adapters API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/control-panel-os-adapters.md), and [API module](../api/control-panel-os-adapters.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `control-panel-os-adapters`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-os-adapters.md)) |
| Capability React Native module skeleton | [`module-control-panel-os-adapters-react-native`](https://github.com/liberusoftware/module-control-panel-os-adapters-react-native) (`@liberusoftware/module-control-panel-os-adapters-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Detection** | Progressive mobile list/detail/sheet flow for `detection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Packages** | Progressive mobile list/detail/sheet flow for `packages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Services** | Progressive mobile list/detail/sheet flow for `services` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Firewall** | Progressive mobile list/detail/sheet flow for `firewall` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Users** | Progressive mobile list/detail/sheet flow for `users` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Filesystems** | Progressive mobile list/detail/sheet flow for `filesystems` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Repositories** | Progressive mobile list/detail/sheet flow for `repositories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Support matrix** | Progressive mobile list/detail/sheet flow for `support matrix` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [InstallationCommandReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/InstallationCommandReport.php) | `public function __construct(private readonly ServiceStatusReport $serviceStatusReport)`<br>`public function execute(string\|int $teamId): array` |
| [ListOsAdapters.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ListOsAdapters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ServiceStatusReport.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ServiceStatusReport.php) | `public function all(string\|int $teamId): Collection`<br>`public function missing(string\|int $teamId): Collection`<br>`public function stopped(string\|int $teamId): Collection`<br>`public function find(string\|int $teamId, string $name): ?OsService` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/CreateFirewallRule.php) | `public function execute(array $attributes): FirewallRule`<br>`public function validateSource(mixed $source): void` |
| [DeleteFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/DeleteFirewallRule.php) | `public function execute(FirewallRule $rule): void` |
| [RecordOsResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordOsResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [RecordSupportMatrix.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordSupportMatrix.php) | `public function execute(array $attributes): SupportMatrixEntry` |
| [RegisterOsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RegisterOsAdapter.php) | `public function execute(array $attributes): OsAdapter` |
| [UpdateFirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateFirewallRule.php) | `public function execute(FirewallRule $rule, array $attributes): FirewallRule` |
| [UpdateOsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateOsService.php) | `public function execute(OsService $service, array $attributes): OsService` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FilesystemMount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FilesystemMount.php) | `team_id`, `node_id`, `device`, `mount_path`, `filesystem`, `size_bytes`, `free_bytes`, `options`, `mounted` |
| [FirewallRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FirewallRule.php) | `team_id`, `node_id`, `direction`, `action`, `protocol`, `port`, `source`, `comment`, `active` |
| [OsAdapter.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsAdapter.php) | `team_id`, `node_id`, `operating_system`, `version`, `capabilities`, `status`, `metadata` |
| [OsPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsPackage.php) | `team_id`, `node_id`, `name`, `version`, `architecture`, `status`, `metadata` |
| [OsService.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsService.php) | `team_id`, `node_id`, `name`, `version`, `status`, `enabled`, `metadata` |
| [OsUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsUser.php) | `team_id`, `node_id`, `username`, `uid`, `shell`, `home`, `sudo`, `status`, `metadata` |
| [PackageRepository.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/PackageRepository.php) | `team_id`, `node_id`, `name`, `url`, `distribution`, `enabled`, `trusted`, `metadata` |
| [SupportMatrixEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/SupportMatrixEntry.php) | `operating_system`, `version`, `capability`, `supported`, `minimum_adapter_version`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [OsAdapterController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/src/Http/Controllers/OsAdapterController.php) | `public function index(Request $request, ListOsAdapters $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function serviceStatuses(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function missingServices(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function stoppedServices(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function installationCommands(Request $request, InstallationCommandReport $report): JsonResponse`<br>`public function checkService(Request $request, string $service, ServiceStatusReport $report): JsonResponse`<br>`public function store(Request $request, RegisterOsAdapter $register): JsonResponse`<br>`public function package(Request $request, RecordOsResource $record): JsonResponse`<br>`public function service(Request $request, RecordOsResource $record): JsonResponse`<br>`public function updateService(Request $request, string $service, UpdateOsService $update): JsonResponse`<br>`public function firewall(Request $request, CreateFirewallRule $create): JsonResponse`<br>`public function updateFirewall(Request $request, string $rule, UpdateFirewallRule $update): JsonResponse`<br>`public function deleteFirewall(Request $request, string $rule, DeleteFirewallRule $delete): JsonResponse`<br>`public function user(Request $request, RecordOsResource $record): JsonResponse`<br>`public function filesystem(Request $request, RecordOsResource $record): JsonResponse`<br>`public function repository(Request $request, RecordOsResource $record): JsonResponse`<br>`public function supportMatrix(Request $request, RecordSupportMatrix $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-os-adapters-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/os-adapters')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [OsAdapterController::class, 'index'])->name('control-panel.os-adapters.index');
Route::post('/', [OsAdapterController::class, 'store'])->name('control-panel.os-adapters.store');
Route::get('services/status', [OsAdapterController::class, 'serviceStatuses'])->name('control-panel.os-adapters.services.status');
Route::get('services/missing', [OsAdapterController::class, 'missingServices'])->name('control-panel.os-adapters.services.missing');
Route::get('services/stopped', [OsAdapterController::class, 'stoppedServices'])->name('control-panel.os-adapters.services.stopped');
Route::get('services/install-commands', [OsAdapterController::class, 'installationCommands'])->name('control-panel.os-adapters.services.install-commands');
Route::get('services/{service}/check', [OsAdapterController::class, 'checkService'])->name('control-panel.os-adapters.services.check');
Route::post('packages', [OsAdapterController::class, 'package'])->name('control-panel.os-adapters.packages.store');
Route::post('services', [OsAdapterController::class, 'service'])->name('control-panel.os-adapters.services.store');
Route::patch('services/{service}', [OsAdapterController::class, 'updateService'])->name('control-panel.os-adapters.services.update');
Route::post('firewall-rules', [OsAdapterController::class, 'firewall'])->name('control-panel.os-adapters.firewall.store');
Route::patch('firewall-rules/{rule}', [OsAdapterController::class, 'updateFirewall'])->name('control-panel.os-adapters.firewall.update');
Route::delete('firewall-rules/{rule}', [OsAdapterController::class, 'deleteFirewall'])->name('control-panel.os-adapters.firewall.delete');
Route::post('users', [OsAdapterController::class, 'user'])->name('control-panel.os-adapters.users.store');
Route::post('filesystems', [OsAdapterController::class, 'filesystem'])->name('control-panel.os-adapters.filesystems.store');
Route::post('repositories', [OsAdapterController::class, 'repository'])->name('control-panel.os-adapters.repositories.store');
Route::post('support-matrix', [OsAdapterController::class, 'supportMatrix'])->name('control-panel.os-adapters.support-matrix.store');
Route::get('{adapter}', [OsAdapterController::class, 'show'])->name('control-panel.os-adapters.show');
```
<!-- layer-implementation-plan:end -->
