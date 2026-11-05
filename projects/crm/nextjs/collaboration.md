# Collaboration: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-collaboration`.

**Proposed design identifier:** `module-crm-collaboration-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/collaboration.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-collaboration](../../../modules/source/liberusoftware--module-crm-collaboration.md) |
| API | [liberusoftware/module-crm-collaboration-api](../../../modules/source/liberusoftware--module-crm-collaboration-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Record comments | A focused authorized view or workflow section for record comments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Mentions | A focused authorized view or workflow section for mentions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Followers | A focused authorized view or workflow section for followers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Shared work queues | A focused authorized view or workflow section for shared work queues; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Handoffs | A focused authorized view or workflow section for handoffs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Internal channels | A focused authorized view or workflow section for internal channels; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Collaboration-provider adapters | A focused authorized view or workflow section for collaboration-provider adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CollaborationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Queries/CollaborationQuery.php) | `public function records(int $teamId, string $recordKey): Builder`<br>`public function queue(int $teamId, string $queueKey): Builder` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddCollaborationRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/AddCollaborationRecord.php) | `public function execute(int $teamId, string $recordKey, string $authorKey, string $body, string $kind = 'comment', array $mentions = []): CollaborationRecord` |
| [AssignCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/AssignCollaborationWork.php) | `public function execute(int $teamId, string $queueKey, string $subjectKey, ?string $assigneeKey = null, array $metadata = []): CollaborationWork` |
| [HandoffCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/HandoffCollaborationWork.php) | `public function execute(int $teamId, CollaborationWork $work, string $assigneeKey, string $reason): CollaborationWork` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CollaborationRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Models/CollaborationRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Models/CollaborationWork.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-collaboration-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/collaboration')->group(function (): void {
Route::get('records/{recordKey}', [CollaborationController::class, 'records']);
Route::post('records', [CollaborationController::class, 'record']);
Route::post('work', [CollaborationController::class, 'assign']);
Route::post('work/{work}/handoff', [CollaborationController::class, 'handoff']);
Route::get('queues/{queueKey}', [CollaborationController::class, 'queue']);
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
