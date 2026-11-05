# Sales Pipelines: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-sales-pipelines`.

**Proposed design identifier:** `module-crm-sales-pipelines-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/sales-pipelines.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-sales-pipelines](../../../modules/source/liberusoftware--module-crm-sales-pipelines.md) |
| API | [liberusoftware/module-crm-sales-pipelines-api](../../../modules/source/liberusoftware--module-crm-sales-pipelines-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Multiple pipelines | A focused authorized view or workflow section for multiple pipelines; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Stages | A focused authorized view or workflow section for stages; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Opportunities | A focused authorized view or workflow section for opportunities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Products | A focused authorized view or workflow section for products; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Values | A focused authorized view or workflow section for values; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Probabilities | A focused authorized view or workflow section for probabilities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Close dates | A focused authorized view or workflow section for close dates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Competitors | A focused authorized view or workflow section for competitors; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dependencies | A focused authorized view or workflow section for dependencies; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Stage history | A focused authorized view or workflow section for stage history; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rotting | A focused authorized view or workflow section for rotting; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Loss reasons | A focused authorized view or workflow section for loss reasons; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [PipelineQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php) | `public function pipelines(int $teamId)`<br>`public function stages(int $teamId, int $pipelineId)`<br>`public function opportunities(int $teamId)`<br>`public function rottingOpportunities(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CloseOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, string $status, ?string $reason = null): Opportunity` |
| [CreateOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php) | `public function execute(int $teamId, int $actorId, array $data): Opportunity` |
| [CreatePipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php) | `public function execute(int $teamId, int $actorId, array $data): SalesPipeline` |
| [CreateStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php) | `public function execute(int $teamId, int $actorId, array $data): SalesStage` |
| [MoveOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): Opportunity` |
| [PipelineAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelineAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [PipelinePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Opportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/Opportunity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesPipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesPipeline.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesStage.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/StageHistory.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-sales-pipelines-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-pipelines')->group(function (): void {
Route::get('/pipelines', [PipelineController::class, 'pipelines']);
Route::post('/pipelines', [PipelineController::class, 'pipeline']);
Route::post('/stages', [PipelineController::class, 'stage']);
Route::get('/opportunities', [PipelineController::class, 'opportunities']);
Route::get('/opportunities/rotting', [PipelineController::class, 'rottingOpportunities']);
Route::post('/opportunities', [PipelineController::class, 'opportunity']);
Route::post('/opportunities/{opportunity}/move', [PipelineController::class, 'move']);
Route::post('/opportunities/{opportunity}/close/{status}', [PipelineController::class, 'close'])->whereIn('status', ['won', 'lost']);
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

Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) before relying on the API pagination, move retry behavior, close rules or current UI parity.
