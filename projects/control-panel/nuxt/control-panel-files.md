# Control Panel: Control Panel Files Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-files). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-files-nuxt`
**Matching domain module:** `control-panel-files`
**Application:** Control Panel
**Source feature:** [Control Panel Files](../features/control-panel-files.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-files.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-files` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Home directories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Permissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SFTP:** page/component/composable/API-action behavior for this module's authorized workflow.
- **File operations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quotas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scanning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retention:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-files-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `home-directories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `permissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sftp`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `file-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quotas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scanning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-files` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-files.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-files-nuxt`](https://github.com/liberusoftware/module-control-panel-files-nuxt) (`@liberusoftware/module-control-panel-files-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Home directories** | Expose composable and Vue 3 component for `home directories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Permissions** | Expose composable and Vue 3 component for `permissions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **SFTP** | Expose composable and Vue 3 component for `sftp` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **File operations** | Expose composable and Vue 3 component for `file operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Quotas** | Expose composable and Vue 3 component for `quotas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Scanning** | Expose composable and Vue 3 component for `scanning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-files.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

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
