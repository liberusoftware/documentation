# Control Panel: OS Adapters Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#os-adapters). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-os-adapters-nuxt`
**Matching domain module:** `control-panel-os-adapters`
**Application:** Control Panel
**Source feature:** [OS Adapters](../features/os-adapters.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/os-adapters.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-os-adapters` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Detection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Packages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Services:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Firewall:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Users:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Filesystems:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Repositories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Support matrix:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-os-adapters-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `detection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `packages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `services`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `firewall`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `users`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `filesystems`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `repositories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `support-matrix`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-os-adapters` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/os-adapters.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-os-adapters-nuxt`](https://github.com/liberusoftware/module-control-panel-os-adapters-nuxt) (`@liberusoftware/module-control-panel-os-adapters-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Detection** | Expose composable and Vue 3 component for `detection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Packages** | Expose composable and Vue 3 component for `packages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Services** | Expose composable and Vue 3 component for `services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Firewall** | Expose composable and Vue 3 component for `firewall` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Users** | Expose composable and Vue 3 component for `users` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Filesystems** | Expose composable and Vue 3 component for `filesystems` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Repositories** | Expose composable and Vue 3 component for `repositories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Support matrix** | Expose composable and Vue 3 component for `support matrix` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/os-adapters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

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
