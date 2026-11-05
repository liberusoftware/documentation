# Sandbox and Release Management: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-sandbox-and-release-management`.

**Proposed design identifier:** `module-crm-sandbox-and-release-management-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/sandbox-and-release-management.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-sandbox-and-release-management](../../../modules/source/liberusoftware--module-crm-sandbox-and-release-management.md) |
| API | [liberusoftware/module-crm-sandbox-and-release-management-api](../../../modules/source/liberusoftware--module-crm-sandbox-and-release-management-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Configuration snapshots | A focused authorized view or workflow section for configuration snapshots; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Test data policy | A focused authorized view or workflow section for test data policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Change sets | A focused authorized view or workflow section for change sets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Validation | A focused authorized view or workflow section for validation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dependency analysis | A focused authorized view or workflow section for dependency analysis; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Promotion | A focused authorized view or workflow section for promotion; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rollback | A focused authorized view or workflow section for rollback; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Environment comparison | A focused authorized view or workflow section for environment comparison; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ReleaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Queries/ReleaseQuery.php) | `public function snapshots(int $teamId)`<br>`public function changesets(int $teamId)`<br>`public function deployments(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateChangeset.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseChangeset` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseSnapshot` |
| [PromoteChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/PromoteChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [RollbackChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/RollbackChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [ValidateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/ValidateChangeset.php) | `public function execute(int $teamId, int $actorId, int $id): ReleaseChangeset` |
| [ReleaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleaseAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ReleasePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleasePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ReleaseChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseChangeset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseDeployment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseDeployment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-sandbox-and-release-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sandbox-and-release-management')->group(function (): void {
Route::get('/snapshots', [ReleaseController::class, 'snapshots']);
Route::post('/snapshots', [ReleaseController::class, 'snapshot']);
Route::get('/changesets', [ReleaseController::class, 'changesets']);
Route::post('/changesets', [ReleaseController::class, 'changeset']);
Route::post('/changesets/{set}/validate', [ReleaseController::class, 'validateSet']);
Route::post('/changesets/{set}/promote', [ReleaseController::class, 'promote']);
Route::post('/changesets/{set}/rollback', [ReleaseController::class, 'rollback']);
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
