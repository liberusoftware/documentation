# Core: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/real-estate-core`.

**Proposed design identifier:** `module-real-estate-core-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/core.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/real-estate-core](../../../modules/source/liberusoftware--real-estate-core.md) |
| API | [liberusoftware/real-estate-core-api](../../../modules/source/liberusoftware--real-estate-core-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Core | A focused authorized view or workflow section for core; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

No concrete action/query signatures were established in the indexed source roots for this design. Use its source reference and owning application routes/contracts to resolve the integration, rather than inventing create/update/delete operations from the module name.

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Agency.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Agency.php) | No literal fillable array detected; inspect the model and API schema. |
| [AuditEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/AuditEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Branch.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Branch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CalendarEntry.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/CalendarEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Communication.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Communication.php) | No literal fillable array detected; inspect the model and API schema. |
| [NumberSequence.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/NumberSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [StatusDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/StatusDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
| [Terminology.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Terminology.php) | No literal fillable array detected; inspect the model and API schema. |
| [Territory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Territory.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/real-estate-core-api/routes/api.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/routes/api.php)

```php
Route::get('api/v1/public/territories', [PublicTerritoryController::class, 'index'])
Route::prefix('api/v1/real-estate/calendar-entries')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CalendarEntryController::class, 'store']);
Route::delete('/{calendarEntry}', [CalendarEntryController::class, 'destroy']);
Route::prefix('api/v1/real-estate/communications')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CommunicationController::class, 'store']);
Route::delete('/{communication}', [CommunicationController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('api/v1/real-estate/core/{kind}', [CoreConfigurationController::class, 'list'])->whereIn('kind', ['terminology', 'statuses', 'audit']);
Route::put('api/v1/real-estate/core/terminology/{key}', [CoreConfigurationController::class, 'terminology']);
Route::post('api/v1/real-estate/core/statuses', [CoreConfigurationController::class, 'status']);
Route::post('api/v1/real-estate/core/audit', [CoreConfigurationController::class, 'audit']);
Route::post('api/v1/real-estate/numbering/{key}/next', [NumberingController::class, 'next'])
Route::prefix('api/v1/real-estate/branches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->name('real-estate.branches.index');
Route::post('/', [BranchController::class, 'store'])->name('real-estate.branches.store');
Route::get('/{branch}', [BranchController::class, 'show'])->name('real-estate.branches.show');
Route::delete('/{branch}', [BranchController::class, 'destroy'])->name('real-estate.branches.destroy');
Route::prefix('api/v1/real-estate/agencies')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [AgencyController::class, 'index']);
Route::post('/', [AgencyController::class, 'store']);
Route::get('/{agency}', [AgencyController::class, 'show']);
Route::delete('/{agency}', [AgencyController::class, 'destroy']);
Route::prefix('api/v1/real-estate/territories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [TerritoryController::class, 'index']);
Route::post('/', [TerritoryController::class, 'store']);
Route::get('/{territory}', [TerritoryController::class, 'show']);
Route::delete('/{territory}', [TerritoryController::class, 'destroy']);
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
