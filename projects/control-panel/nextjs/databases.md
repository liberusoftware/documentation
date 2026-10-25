# Databases: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-databases`.

**Proposed design identifier:** `module-control-panel-databases-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/databases.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-databases](../../../modules/source/liberusoftware--module-control-panel-databases.md) |
| API | [liberusoftware/module-control-panel-databases-api](../../../modules/source/liberusoftware--module-control-panel-databases-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Engines | A focused authorized view or workflow section for engines; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Databases | A focused authorized view or workflow section for databases; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Users | A focused authorized view or workflow section for users; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Privileges | A focused authorized view or workflow section for privileges; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Backups | A focused authorized view or workflow section for backups; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Upgrades | A focused authorized view or workflow section for upgrades; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Health | A focused authorized view or workflow section for health; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Remote access | A focused authorized view or workflow section for remote access; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListDatabaseBackups.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabaseBackups.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListDatabases.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabases.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ActivateDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ActivateDatabase.php) | `public function execute(Database $database): Database` |
| [ArchiveDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ArchiveDatabase.php) | `public function execute(Database $database): Database` |
| [ConfigureRemoteAccess.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ConfigureRemoteAccess.php) | `public function execute(Database $database, array $attributes): DatabaseRemoteAccess` |
| [CreateDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabase.php) | `public function execute(array $attributes): Database` |
| [CreateDatabaseBackup.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseBackup.php) | `public function execute(Database $database, array $attributes): DatabaseBackup` |
| [CreateDatabaseUser.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseUser.php) | `public function execute(Database $database, array $attributes): DatabaseUser` |
| [DeleteDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/DeleteDatabase.php) | `public function execute(Database $database): void` |
| [GrantDatabasePrivilege.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/GrantDatabasePrivilege.php) | `public function execute(DatabaseUser $user, string $privilege, string $objectName = '*'): DatabasePrivilege` |
| [RecordDatabaseHealth.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RecordDatabaseHealth.php) | `public function execute(Database $database, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): DatabaseHealthCheck` |
| [RequestDatabaseUpgrade.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RequestDatabaseUpgrade.php) | `public function execute(Database $database, string $toVersion): DatabaseUpgrade` |
| [SuspendDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/SuspendDatabase.php) | `public function execute(Database $database): Database` |
| [UpdateDatabase.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/UpdateDatabase.php) | `public function execute(Database $database, array $attributes): Database` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Database.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/Database.php) | `team_id`, `engine_id`, `account_id`, `name`, `status`, `charset`, `collation`, `metadata` |
| [DatabaseBackup.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseBackup.php) | `team_id`, `database_id`, `destination`, `type`, `path`, `size`, `status`, `error`, `started_at`, `completed_at`, `automated` |
| [DatabaseEngine.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseEngine.php) | `team_id`, `name`, `driver`, `version`, `host`, `port`, `active`, `metadata` |
| [DatabaseHealthCheck.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseHealthCheck.php) | `team_id`, `database_id`, `healthy`, `latency_ms`, `message`, `details`, `checked_at` |
| [DatabasePrivilege.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabasePrivilege.php) | `team_id`, `database_id`, `database_user_id`, `privilege`, `object_name` |
| [DatabaseRemoteAccess.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseRemoteAccess.php) | `team_id`, `database_id`, `source_cidr`, `port`, `tls_required`, `active`, `expires_at`, `metadata` |
| [DatabaseUpgrade.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUpgrade.php) | `team_id`, `database_id`, `from_version`, `to_version`, `status`, `error`, `started_at`, `finished_at`, `metadata` |
| [DatabaseUser.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUser.php) | `team_id`, `database_id`, `username`, `host`, `password`, `active` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-databases-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/databases')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [DatabaseController::class, 'index'])->name('control-panel.databases.index');
Route::post('/', [DatabaseController::class, 'store'])->name('control-panel.databases.store');
Route::patch('{database}', [DatabaseController::class, 'update'])->name('control-panel.databases.update');
Route::post('{database}/users', [DatabaseController::class, 'user'])->name('control-panel.databases.users.store');
Route::post('users/{user}/privileges', [DatabaseController::class, 'privilege'])->name('control-panel.databases.privileges.store');
Route::post('{database}/backups', [DatabaseController::class, 'backup'])->name('control-panel.databases.backups.store');
Route::post('{database}/health-checks', [DatabaseController::class, 'health'])->name('control-panel.databases.health.store');
Route::post('{database}/upgrades', [DatabaseController::class, 'upgrade'])->name('control-panel.databases.upgrades.store');
Route::post('{database}/remote-access', [DatabaseController::class, 'remoteAccess'])->name('control-panel.databases.remote-access.store');
Route::post('{database}/suspend', [DatabaseController::class, 'suspend'])->name('control-panel.databases.suspend');
Route::post('{database}/archive', [DatabaseController::class, 'archive'])->name('control-panel.databases.archive');
Route::delete('{database}', [DatabaseController::class, 'delete'])->name('control-panel.databases.delete');
Route::get('{database}', [DatabaseController::class, 'show'])->name('control-panel.databases.show');
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
