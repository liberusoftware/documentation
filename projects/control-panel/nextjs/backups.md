# Backups: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-backups`.

**Proposed design identifier:** `module-control-panel-backups-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/backups.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-backups](../../../modules/source/liberusoftware--module-control-panel-backups.md) |
| API | [liberusoftware/module-control-panel-backups-api](../../../modules/source/liberusoftware--module-control-panel-backups-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Policies | A focused authorized view or workflow section for policies; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Snapshots | A focused authorized view or workflow section for snapshots; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Application-consistent backup | A focused authorized view or workflow section for application-consistent backup; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Encryption | A focused authorized view or workflow section for encryption; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Off-site storage | A focused authorized view or workflow section for off-site storage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Restore | A focused authorized view or workflow section for restore; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Verification | A focused authorized view or workflow section for verification; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListSnapshots.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Queries/ListSnapshots.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateDestination.php) | `public function execute(array $attributes): BackupDestination` |
| [CreatePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreatePolicy.php) | `public function execute(array $attributes): BackupPolicy` |
| [CreateSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSchedule.php) | `public function execute(BackupPolicy $policy, string $cron, string $timezone = 'UTC'): BackupSchedule` |
| [CreateSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSnapshot.php) | `public function execute(BackupPolicy $policy, array $attributes = []): BackupSnapshot` |
| [DeleteDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteDestination.php) | `public function execute(BackupDestination $destination): void` |
| [DeletePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeletePolicy.php) | `public function execute(BackupPolicy $policy): void` |
| [DeleteSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSchedule.php) | `public function execute(BackupSchedule $schedule): void` |
| [DeleteSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSnapshot.php) | `public function execute(BackupSnapshot $snapshot): void` |
| [RecordBackupFeature.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordBackupFeature.php) | `public function execute(array $a): Model` |
| [RecordDestinationHealth.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordDestinationHealth.php) | `public function execute(BackupDestination $destination, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): BackupDestination` |
| [RequestRestore.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RequestRestore.php) | `public function execute(BackupSnapshot $snapshot, string $teamId, string $target, array $options = []): BackupRestore` |
| [UpdateDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateDestination.php) | `public function execute(BackupDestination $destination, array $attributes): BackupDestination` |
| [UpdatePolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdatePolicy.php) | `public function execute(BackupPolicy $policy, array $attributes): BackupPolicy` |
| [UpdateSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateSchedule.php) | `public function execute(BackupSchedule $schedule, array $attributes): BackupSchedule` |
| [VerifySnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/VerifySnapshot.php) | `public function execute(BackupSnapshot $snapshot, string $checksum): BackupSnapshot` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [BackupDestination.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupDestination.php) | `team_id`, `name`, `driver`, `config`, `retention_days`, `default`, `active`, `last_checked_at`, `health` |
| [BackupEncryption.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupEncryption.php) | `id`, `team_id`, `policy_id`, `algorithm`, `key_reference`, `active`, `rotated_at` |
| [BackupExecution.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupExecution.php) | `id`, `team_id`, `policy_id`, `type`, `consistency`, `status`, `started_at`, `completed_at`, `error`, `metadata` |
| [BackupPolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupPolicy.php) | `team_id`, `name`, `schedule`, `retention_days`, `storage_driver`, `storage_config`, `encrypted`, `active` |
| [BackupRestore.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupRestore.php) | `team_id`, `snapshot_id`, `target`, `status`, `options`, `error`, `started_at`, `finished_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSchedule.php) | `team_id`, `policy_id`, `cron`, `timezone`, `active`, `next_run_at`, `last_run_at` |
| [BackupSnapshot.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSnapshot.php) | `team_id`, `policy_id`, `location`, `status`, `size_bytes`, `checksum`, `verified_at`, `metadata` |
| [OffsiteTransfer.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/OffsiteTransfer.php) | `id`, `team_id`, `snapshot_id`, `destination_id`, `status`, `attempts`, `transferred_at`, `error`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-backups-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/routes/api.php)

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
