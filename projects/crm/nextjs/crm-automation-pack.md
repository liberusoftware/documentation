# CRM Automation Pack: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-automation-pack`.<br>
**Matching domain module:** `crm-automation-pack`

**Proposed design identifier:** `module-crm-automation-pack-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/crm-automation-pack.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-automation-pack.md)) |
| Capability Next.js module skeleton | [module-crm-automation-pack-nextjs](https://github.com/liberusoftware/module-crm-automation-pack-nextjs) (`@liberusoftware/module-crm-automation-pack-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-automation-pack](../../../modules/source/liberusoftware--module-crm-automation-pack.md) |
| API | [liberusoftware/module-crm-automation-pack-api](../../../modules/source/liberusoftware--module-crm-automation-pack-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **CRM triggers/actions/conditions** | Server Component loads authorized `crm triggers/actions/conditions` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Recipes** | Server Component loads authorized `recipes` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Enrollment history** | Server Component loads authorized `enrollment history` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Versioning** | Server Component loads authorized `versioning` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Simulation** | Server Component loads authorized `simulation` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Approval gates** | Server Component loads authorized `approval gates` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Generic Automation module adapters** | Server Component loads authorized `generic automation module adapters` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
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
