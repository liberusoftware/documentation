# Control Panel Files React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-files). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-files-react-native
**Matching core package:** module-control-panel-control-panel-files ([implementation](../core/control-panel-files.md))
**Matching API package:** module-control-panel-control-panel-files-api ([contract](../api/control-panel-files.md))

## Implementation plan

This adapter presents Control Panel Files for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Files API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/control-panel-files.md), and [API module](../api/control-panel-files.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `control-panel-files`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-files.md)) |
| Capability React Native module skeleton | [`module-control-panel-files-react-native`](https://github.com/liberusoftware/module-control-panel-files-react-native) (`@liberusoftware/module-control-panel-files-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Home directories** | Progressive mobile list/detail/sheet flow for `home directories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Permissions** | Progressive mobile list/detail/sheet flow for `permissions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **SFTP** | Progressive mobile list/detail/sheet flow for `sftp` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **File operations** | Progressive mobile list/detail/sheet flow for `file operations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quotas** | Progressive mobile list/detail/sheet flow for `quotas` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scanning** | Progressive mobile list/detail/sheet flow for `scanning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retention** | Progressive mobile list/detail/sheet flow for `retention` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListFiles.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Queries/ListFiles.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateHomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateHomeDirectory.php) | `public function execute(array $attributes): HomeDirectory` |
| [CreateSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateSftpAccount.php) | `public function execute(array $attributes): SftpAccount` |
| [DeleteFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteFile.php) | `public function execute(FileEntry $file): FileEntry` |
| [DeleteSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteSftpAccount.php) | `public function execute(SftpAccount $account): void` |
| [GrantFilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/GrantFilePermission.php) | `public function execute(array $attributes): FilePermission` |
| [MarkFileScanned.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/MarkFileScanned.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(FileEntry $file, bool $clean): FileEntry` |
| [RecordFileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RecordFileOperation.php) | `public function execute(array $a): FileOperation` |
| [RegenerateSftpKeyPair.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegenerateSftpKeyPair.php) | `public function execute(SftpAccount $account, ?int $bits = null): array` |
| [RegisterFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegisterFile.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): FileEntry` |
| [SetFileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/SetFileQuota.php) | `public function execute(array $attributes): FileQuota` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FileEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileEntry.php) | `team_id`, `owner_id`, `path`, `disk`, `mime_type`, `size_bytes`, `checksum`, `status`, `scanned_at`, `retention_until`, `metadata` |
| [FileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileOperation.php) | `id`, `team_id`, `file_id`, `operation`, `status`, `details` |
| [FilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FilePermission.php) | `id`, `team_id`, `file_id`, `home_directory_id`, `subject_id`, `subject_type`, `mode`, `recursive` |
| [FileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileQuota.php) | `id`, `team_id`, `owner_id`, `limit_bytes`, `used_bytes`, `files_count` |
| [FileRetention.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileRetention.php) | `id`, `team_id`, `file_id`, `retention_until`, `policy`, `active` |
| [HomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/HomeDirectory.php) | `id`, `team_id`, `owner_id`, `path`, `disk`, `mode`, `status`, `metadata` |
| [SftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/SftpAccount.php) | `id`, `team_id`, `owner_id`, `username`, `password`, `home_directory`, `quota_mb`, `bandwidth_limit_mb`, `active`, `last_login_at`, `ssh_key_auth_enabled`, `ssh_public_key`, `ssh_private_key`, `ssh_key_type`, `ssh_key_bits` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FileController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-api/src/Http/Controllers/FileController.php) | `public function index(Request $request, ListFiles $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function delete(Request $request, string $id, DeleteFile $delete): JsonResponse`<br>`public function store(Request $request, RegisterFile $register): JsonResponse`<br>`public function operation(Request $request, RecordFileOperation $record): JsonResponse`<br>`public function home(Request $request, CreateHomeDirectory $create): JsonResponse`<br>`public function permission(Request $request, GrantFilePermission $grant): JsonResponse`<br>`public function sftp(Request $request, CreateSftpAccount $create): JsonResponse`<br>`public function deleteSftp(Request $request, string $id, DeleteSftpAccount $delete): JsonResponse`<br>`public function regenerateSftpKeys(Request $request, string $id, RegenerateSftpKeyPair $regenerate): JsonResponse`<br>`public function retention(Request $request, SetFileRetention $set): JsonResponse`<br>`public function quota(Request $request, SetFileQuota $set): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-files-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/files')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [FileController::class, 'index'])->name('control-panel.files.index');
Route::post('/', [FileController::class, 'store'])->name('control-panel.files.store');
Route::post('/operations', [FileController::class, 'operation'])->name('control-panel.files.operations.store');
Route::post('/home-directories', [FileController::class, 'home'])->name('control-panel.files.home-directories.store');
Route::post('/permissions', [FileController::class, 'permission'])->name('control-panel.files.permissions.store');
Route::post('/sftp-accounts', [FileController::class, 'sftp'])->name('control-panel.files.sftp-accounts.store');
Route::delete('/sftp-accounts/{sftpAccount}', [FileController::class, 'deleteSftp'])->name('control-panel.files.sftp-accounts.delete');
Route::post('/sftp-accounts/{sftpAccount}/regenerate-keys', [FileController::class, 'regenerateSftpKeys'])->name('control-panel.files.sftp-accounts.regenerate-keys');
Route::post('/retention', [FileController::class, 'retention'])->name('control-panel.files.retention.store');
Route::post('/quotas', [FileController::class, 'quota'])->name('control-panel.files.quotas.store');
Route::delete('/{file}', [FileController::class, 'delete'])->name('control-panel.files.delete');
Route::get('{file}', [FileController::class, 'show'])->name('control-panel.files.show');
```
<!-- layer-implementation-plan:end -->
