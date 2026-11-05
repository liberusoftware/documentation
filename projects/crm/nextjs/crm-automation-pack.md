# CRM Automation Pack: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-automation-pack`.

**Proposed design identifier:** `module-crm-automation-pack-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/crm-automation-pack.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-automation-pack](../../../modules/source/liberusoftware--module-crm-automation-pack.md) |
| API | [liberusoftware/module-crm-automation-pack-api](../../../modules/source/liberusoftware--module-crm-automation-pack-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| CRM triggers/actions/conditions | A focused authorized view or workflow section for crm triggers/actions/conditions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Recipes | A focused authorized view or workflow section for recipes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Enrollment history | A focused authorized view or workflow section for enrollment history; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Versioning | A focused authorized view or workflow section for versioning; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Simulation | A focused authorized view or workflow section for simulation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approval gates | A focused authorized view or workflow section for approval gates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Generic Automation module adapters | A focused authorized view or workflow section for generic automation module adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
| [AutomationPackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Services/AutomationPackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [AutomationApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRecipe.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRun.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-automation-pack-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-automation-pack')->group(function (): void {
Route::get('recipes', [AutomationPackController::class, 'index']);
Route::post('recipes', [AutomationPackController::class, 'store']);
Route::post('recipes/{recipe}/publish', [AutomationPackController::class, 'publish']);
Route::post('recipes/{recipe}/simulate', [AutomationPackController::class, 'simulate']);
Route::post('recipes/{recipe}/approve', [AutomationPackController::class, 'approve']);
Route::post('recipes/{recipe}/enroll', [AutomationPackController::class, 'enroll']);
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
