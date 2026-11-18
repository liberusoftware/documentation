# Control Panel: Control Panel Files Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-files). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-control-panel-files-vue-inertia`
**Matching domain module:** `control-panel-files`
**Application:** Control Panel
**Source feature:** [Control Panel Files](../features/control-panel-files.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-files.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Home directories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Permissions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SFTP:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **File operations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quotas:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scanning:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Retention:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-control-panel-files-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `home-directories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `permissions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sftp`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `file-operations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `quotas`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `scanning`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `retention`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-files` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-files-vue-inertia`](https://github.com/liberusoftware/module-control-panel-files-vue-inertia) (`@liberusoftware/module-control-panel-files-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/control-panel-files.md) · [Core plan](../core/control-panel-files.md) · [API plan](../api/control-panel-files.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Home directories** | Render `home directories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Permissions** | Render `permissions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **SFTP** | Render `sftp` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **File operations** | Render `file operations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Quotas** | Render `quotas` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Scanning** | Render `scanning` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Retention** | Render `retention` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
