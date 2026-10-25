# OS Adapters: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-os-adapters`.

**Proposed design identifier:** `module-control-panel-os-adapters-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/os-adapters.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-os-adapters](../../../modules/source/liberusoftware--module-control-panel-os-adapters.md) |
| API | [liberusoftware/module-control-panel-os-adapters-api](../../../modules/source/liberusoftware--module-control-panel-os-adapters-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Detection | A focused authorized view or workflow section for detection; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Packages | A focused authorized view or workflow section for packages; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Services | A focused authorized view or workflow section for services; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Firewall | A focused authorized view or workflow section for firewall; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Users | A focused authorized view or workflow section for users; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Filesystems | A focused authorized view or workflow section for filesystems; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Repositories | A focused authorized view or workflow section for repositories; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Support matrix | A focused authorized view or workflow section for support matrix; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [InstallationCommandReport.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/InstallationCommandReport.php) | `public function execute(string\|int $teamId): array` |
| [ListOsAdapters.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ListOsAdapters.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ServiceStatusReport.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Queries/ServiceStatusReport.php) | `public function all(string\|int $teamId): Collection`<br>`public function missing(string\|int $teamId): Collection`<br>`public function stopped(string\|int $teamId): Collection`<br>`public function find(string\|int $teamId, string $name): ?OsService` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/CreateFirewallRule.php) | `public function execute(array $attributes): FirewallRule`<br>`public function validateSource(mixed $source): void` |
| [DeleteFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/DeleteFirewallRule.php) | `public function execute(FirewallRule $rule): void` |
| [RecordOsResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordOsResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [RecordSupportMatrix.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RecordSupportMatrix.php) | `public function execute(array $attributes): SupportMatrixEntry` |
| [RegisterOsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/RegisterOsAdapter.php) | `public function execute(array $attributes): OsAdapter` |
| [UpdateFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateFirewallRule.php) | `public function execute(FirewallRule $rule, array $attributes): FirewallRule` |
| [UpdateOsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Actions/UpdateOsService.php) | `public function execute(OsService $service, array $attributes): OsService` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [FilesystemMount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FilesystemMount.php) | `team_id`, `node_id`, `device`, `mount_path`, `filesystem`, `size_bytes`, `free_bytes`, `options`, `mounted` |
| [FirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/FirewallRule.php) | `team_id`, `node_id`, `direction`, `action`, `protocol`, `port`, `source`, `comment`, `active` |
| [OsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsAdapter.php) | `team_id`, `node_id`, `operating_system`, `version`, `capabilities`, `status`, `metadata` |
| [OsPackage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsPackage.php) | `team_id`, `node_id`, `name`, `version`, `architecture`, `status`, `metadata` |
| [OsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsService.php) | `team_id`, `node_id`, `name`, `version`, `status`, `enabled`, `metadata` |
| [OsUser.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/OsUser.php) | `team_id`, `node_id`, `username`, `uid`, `shell`, `home`, `sudo`, `status`, `metadata` |
| [PackageRepository.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/PackageRepository.php) | `team_id`, `node_id`, `name`, `url`, `distribution`, `enabled`, `trusted`, `metadata` |
| [SupportMatrixEntry.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters/src/Models/SupportMatrixEntry.php) | `operating_system`, `version`, `capability`, `supported`, `minimum_adapter_version`, `notes` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-os-adapters-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/routes/api.php)

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
