# Backups Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#backups). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-backups-flutter
**Matching core package:** module-control-panel-backups ([implementation](../core/backups.md))
**Matching API package:** module-control-panel-backups-api ([contract](../api/backups.md))

## Implementation plan

This adapter presents Backups for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Backups API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/backups.md), and [API module](../api/backups.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `backups`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-backups-flutter`](https://github.com/liberusoftware/module-control-panel-backups-flutter) (`module_control_panel_backups_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-backups-dart-mobile`](https://github.com/liberusoftware/module-control-panel-backups-dart-mobile) (`module_control_panel_backups_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-backups-dart-desktop`](https://github.com/liberusoftware/module-control-panel-backups-dart-desktop) (`module_control_panel_backups_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/backups.md) · [Core plan](../core/backups.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Policies** | Adaptive mobile cards/sheets for `policies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `policies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Snapshots** | Adaptive mobile cards/sheets for `snapshots` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `snapshots` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Application-consistent backup** | Adaptive mobile cards/sheets for `application-consistent backup` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `application-consistent backup` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Encryption** | Adaptive mobile cards/sheets for `encryption` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `encryption` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Off-site storage** | Adaptive mobile cards/sheets for `off-site storage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `off-site storage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Restore** | Adaptive mobile cards/sheets for `restore` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `restore` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Verification** | Adaptive mobile cards/sheets for `verification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `verification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListSnapshots.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Queries/ListSnapshots.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateDestination.php) | `public function execute(array $attributes): BackupDestination` |
| [CreatePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreatePolicy.php) | `public function execute(array $attributes): BackupPolicy` |
| [CreateSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSchedule.php) | `public function execute(BackupPolicy $policy, string $cron, string $timezone = 'UTC'): BackupSchedule` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupPolicy $policy, array $attributes = []): BackupSnapshot` |
| [DeleteDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteDestination.php) | `public function execute(BackupDestination $destination): void` |
| [DeletePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeletePolicy.php) | `public function execute(BackupPolicy $policy): void` |
| [DeleteSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSchedule.php) | `public function execute(BackupSchedule $schedule): void` |
| [DeleteSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSnapshot.php) | `public function execute(BackupSnapshot $snapshot): void` |
| [RecordBackupFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordBackupFeature.php) | `public function execute(array $a): Model` |
| [RecordDestinationHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordDestinationHealth.php) | `public function execute(BackupDestination $destination, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): BackupDestination` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BackupDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupDestination.php) | `team_id`, `name`, `driver`, `config`, `retention_days`, `default`, `active`, `last_checked_at`, `health` |
| [BackupEncryption.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupEncryption.php) | `id`, `team_id`, `policy_id`, `algorithm`, `key_reference`, `active`, `rotated_at` |
| [BackupExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupExecution.php) | `id`, `team_id`, `policy_id`, `type`, `consistency`, `status`, `started_at`, `completed_at`, `error`, `metadata` |
| [BackupPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupPolicy.php) | `team_id`, `name`, `schedule`, `retention_days`, `storage_driver`, `storage_config`, `encrypted`, `active` |
| [BackupRestore.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupRestore.php) | `team_id`, `snapshot_id`, `target`, `status`, `options`, `error`, `started_at`, `finished_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSchedule.php) | `team_id`, `policy_id`, `cron`, `timezone`, `active`, `next_run_at`, `last_run_at` |
| [BackupSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSnapshot.php) | `team_id`, `policy_id`, `location`, `status`, `size_bytes`, `checksum`, `verified_at`, `metadata` |
| [OffsiteTransfer.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/OffsiteTransfer.php) | `id`, `team_id`, `snapshot_id`, `destination_id`, `status`, `attempts`, `transferred_at`, `error`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SnapshotController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/src/Http/Controllers/SnapshotController.php) | `public function index(Request $request, ListSnapshots $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateSnapshot $create): JsonResponse`<br>`public function destination(Request $request, CreateDestination $create): JsonResponse`<br>`public function updatePolicy(Request $request, string $id, UpdatePolicy $update): JsonResponse`<br>`public function updateDestination(Request $request, string $id, UpdateDestination $update): JsonResponse`<br>`public function destinationHealth(Request $request, string $id, RecordDestinationHealth $record): JsonResponse`<br>`public function deleteDestination(Request $request, string $id, DeleteDestination $delete): JsonResponse`<br>`public function updateSchedule(Request $request, string $id, UpdateSchedule $update): JsonResponse`<br>`public function deleteSchedule(Request $request, string $id, DeleteSchedule $delete): JsonResponse`<br>`public function deletePolicy(Request $request, string $id, DeletePolicy $delete): JsonResponse`<br>`public function deleteSnapshot(Request $request, string $id, DeleteSnapshot $delete): JsonResponse`<br>`public function schedule(Request $request, CreateSchedule $create): JsonResponse`<br>`public function restore(Request $request, string $snapshot, RequestRestore $restore): JsonResponse`<br>`public function verify(Request $request, string $snapshot, VerifySnapshot $verify): JsonResponse`<br>`public function feature(Request $request, RecordBackupFeature $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-backups-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/backups')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/snapshots', [SnapshotController::class, 'index'])->name('control-panel.backups.snapshots.index');
Route::post('/snapshots', [SnapshotController::class, 'store'])->name('control-panel.backups.snapshots.store');
Route::patch('/policies/{policy}', [SnapshotController::class, 'updatePolicy'])->name('control-panel.backups.policies.update');
Route::delete('/policies/{policy}', [SnapshotController::class, 'deletePolicy'])->name('control-panel.backups.policies.delete');
Route::post('/snapshots/{snapshot}/verify', [SnapshotController::class, 'verify'])->name('control-panel.backups.snapshots.verify');
Route::post('/snapshots/{snapshot}/restore', [SnapshotController::class, 'restore'])->name('control-panel.backups.snapshots.restore');
Route::post('/destinations', [SnapshotController::class, 'destination'])->name('control-panel.backups.destinations.store');
Route::patch('/destinations/{destination}', [SnapshotController::class, 'updateDestination'])->name('control-panel.backups.destinations.update');
Route::post('/destinations/{destination}/health', [SnapshotController::class, 'destinationHealth'])->name('control-panel.backups.destinations.health');
Route::delete('/destinations/{destination}', [SnapshotController::class, 'deleteDestination'])->name('control-panel.backups.destinations.delete');
Route::post('/schedules', [SnapshotController::class, 'schedule'])->name('control-panel.backups.schedules.store');
Route::patch('/schedules/{schedule}', [SnapshotController::class, 'updateSchedule'])->name('control-panel.backups.schedules.update');
Route::delete('/schedules/{schedule}', [SnapshotController::class, 'deleteSchedule'])->name('control-panel.backups.schedules.delete');
Route::delete('/snapshots/{snapshot}', [SnapshotController::class, 'deleteSnapshot'])->name('control-panel.backups.snapshots.delete');
Route::post('/features', [SnapshotController::class, 'feature'])->name('control-panel.backups.features.store');
Route::get('snapshots/{snapshot}', [SnapshotController::class, 'show'])->name('control-panel.backups.show');
```
<!-- layer-implementation-plan:end -->
