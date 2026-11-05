# ISP: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-isp`.

**Proposed design identifier:** `module-billing-isp-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/isp.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-isp](../../../modules/source/liberusoftware--module-billing-isp.md) |
| API | [liberusoftware/module-billing-isp-api](../../../modules/source/liberusoftware--module-billing-isp-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Access services | A focused authorized view or workflow section for access services; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Coverage | A focused authorized view or workflow section for coverage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Installation | A focused authorized view or workflow section for installation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| RADIUS/AAA | A focused authorized view or workflow section for radius/aaa; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Usage | A focused authorized view or workflow section for usage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Equipment | A focused authorized view or workflow section for equipment; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Network adapters | A focused authorized view or workflow section for network adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListIspRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Queries/ListIspRecords.php) | `public function handle(int $teamId): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateAccessService.php) | `public function handle(int $teamId, array $attributes): AccessService` |
| [CreateIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateIspCapability.php) | `public function handle(int $teamId, array $attributes): IspCapability` |
| [RecordRadiusAccounting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/RecordRadiusAccounting.php) | `public function execute(AccessService $service, array $accounting): RadiusSession` |
| [ResetUsagePeriod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/ResetUsagePeriod.php) | `public function execute(AccessService $service): AccessService` |
| [SynchronizeAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/SynchronizeAccessService.php) | `public function execute(AccessService $service, string $adapter): AccessService` |
| [TransitionAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionAccessService.php) | `public function handle(AccessService $service, string $status): AccessService` |
| [TransitionIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionIspCapability.php) | `public function handle(IspCapability $capability, string $status): IspCapability` |
| [NetworkAdapterRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Services/NetworkAdapterRegistry.php) | `public function register(NetworkAdapter $adapter): void`<br>`public function resolve(string $key): NetworkAdapter`<br>`public function keys(): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [AccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/AccessService.php) | No literal fillable array detected; inspect the model and API schema. |
| [IspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/IspCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [RadiusSession.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/RadiusSession.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-billing-isp-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'index'])->name('billing.isp.capabilities.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'store'])->name('billing.isp.capabilities.store');
Route::patch('/{capability}/lifecycle', [IspCapabilityController::class, 'transition'])->whereNumber('capability')->name('billing.isp.capabilities.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'storeAccessService'])->name('billing.isp.store');
Route::patch('/{service}/lifecycle', [IspCapabilityController::class, 'transitionAccessService'])->whereNumber('service')->name('billing.isp.services.lifecycle');
Route::post('/{service}/synchronize', [IspCapabilityController::class, 'synchronizeAccessService'])->whereNumber('service')->name('billing.isp.services.synchronize');
Route::post('/{service}/accounting', [IspCapabilityController::class, 'recordAccounting'])->whereNumber('service')->name('billing.isp.services.accounting');
Route::post('/{service}/usage/reset', [IspCapabilityController::class, 'resetUsage'])->whereNumber('service')->name('billing.isp.services.usage.reset');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'accounts'])->name('billing.isp.services.index');
Route::get('/{record}', [IspCapabilityController::class, 'showAccount'])->whereNumber('record')->name('billing.isp.services.show');
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
