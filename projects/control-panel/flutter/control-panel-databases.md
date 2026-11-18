# Control Panel Databases Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-databases). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-databases-flutter
**Matching core package:** module-control-panel-control-panel-databases ([implementation](../core/control-panel-databases.md))
**Matching API package:** module-control-panel-control-panel-databases-api ([contract](../api/control-panel-databases.md))

## Implementation plan

This adapter presents Control Panel Databases for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Databases API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/control-panel-databases.md), and [API module](../api/control-panel-databases.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `control-panel-databases`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-databases-flutter`](https://github.com/liberusoftware/module-control-panel-databases-flutter) (`module_control_panel_databases_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-databases-dart-mobile`](https://github.com/liberusoftware/module-control-panel-databases-dart-mobile) (`module_control_panel_databases_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-databases-dart-desktop`](https://github.com/liberusoftware/module-control-panel-databases-dart-desktop) (`module_control_panel_databases_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/control-panel-databases.md) · [Core plan](../core/control-panel-databases.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Engines** | Adaptive mobile cards/sheets for `engines` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `engines` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Databases** | Adaptive mobile cards/sheets for `databases` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `databases` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Users** | Adaptive mobile cards/sheets for `users` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `users` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Privileges** | Adaptive mobile cards/sheets for `privileges` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `privileges` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Backups** | Adaptive mobile cards/sheets for `backups` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `backups` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Upgrades** | Adaptive mobile cards/sheets for `upgrades` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `upgrades` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Health** | Adaptive mobile cards/sheets for `health` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `health` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Remote access** | Adaptive mobile cards/sheets for `remote access` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `remote access` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListDatabaseBackups.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabaseBackups.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListDatabases.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabases.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ActivateDatabase.php) | `public function execute(Database $database): Database` |
| [ArchiveDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ArchiveDatabase.php) | `public function execute(Database $database): Database` |
| [ConfigureRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ConfigureRemoteAccess.php) | `public function execute(Database $database, array $attributes): DatabaseRemoteAccess` |
| [CreateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabase.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Database` |
| [CreateDatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseBackup.php) | `public function execute(Database $database, array $attributes): DatabaseBackup` |
| [CreateDatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseUser.php) | `public function execute(Database $database, array $attributes): DatabaseUser` |
| [DeleteDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/DeleteDatabase.php) | `public function execute(Database $database): void` |
| [GrantDatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/GrantDatabasePrivilege.php) | `public function execute(DatabaseUser $user, string $privilege, string $objectName = '*'): DatabasePrivilege` |
| [RecordDatabaseHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RecordDatabaseHealth.php) | `public function execute(Database $database, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): DatabaseHealthCheck` |
| [RequestDatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RequestDatabaseUpgrade.php) | `public function execute(Database $database, string $toVersion): DatabaseUpgrade` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Database.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/Database.php) | `team_id`, `engine_id`, `account_id`, `name`, `status`, `charset`, `collation`, `metadata` |
| [DatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseBackup.php) | `team_id`, `database_id`, `destination`, `type`, `path`, `size`, `status`, `error`, `started_at`, `completed_at`, `automated` |
| [DatabaseEngine.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseEngine.php) | `team_id`, `name`, `driver`, `version`, `host`, `port`, `active`, `metadata` |
| [DatabaseHealthCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseHealthCheck.php) | `team_id`, `database_id`, `healthy`, `latency_ms`, `message`, `details`, `checked_at` |
| [DatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabasePrivilege.php) | `team_id`, `database_id`, `database_user_id`, `privilege`, `object_name` |
| [DatabaseRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseRemoteAccess.php) | `team_id`, `database_id`, `source_cidr`, `port`, `tls_required`, `active`, `expires_at`, `metadata` |
| [DatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUpgrade.php) | `team_id`, `database_id`, `from_version`, `to_version`, `status`, `error`, `started_at`, `finished_at`, `metadata` |
| [DatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUser.php) | `team_id`, `database_id`, `username`, `host`, `password`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DatabaseController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/src/Http/Controllers/DatabaseController.php) | `public function index(Request $request, ListDatabases $list): JsonResponse`<br>`public function user(Request $request, Database $database, CreateDatabaseUser $create): JsonResponse`<br>`public function privilege(Request $request, DatabaseUser $user, GrantDatabasePrivilege $grant): JsonResponse`<br>`public function backup(Request $request, Database $database, CreateDatabaseBackup $create): JsonResponse`<br>`public function health(Request $request, Database $database, RecordDatabaseHealth $record): JsonResponse`<br>`public function upgrade(Request $request, Database $database, RequestDatabaseUpgrade $requestUpgrade): JsonResponse`<br>`public function remoteAccess(Request $request, Database $database, ConfigureRemoteAccess $configure): JsonResponse`<br>`public function suspend(Request $request, Database $database, SuspendDatabase $suspend): JsonResponse`<br>`public function archive(Request $request, Database $database, ArchiveDatabase $archive): JsonResponse`<br>`public function delete(Request $request, Database $database, DeleteDatabase $delete): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateDatabase $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateDatabase $update): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-databases-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/routes/api.php)

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
<!-- layer-implementation-plan:end -->
