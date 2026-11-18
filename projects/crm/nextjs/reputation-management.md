# Reputation Management: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-reputation-management`.<br>
**Matching domain module:** `reputation-management`

**Proposed design identifier:** `module-crm-reputation-management-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/reputation-management.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/reputation-management.md)) |
| Capability Next.js module skeleton | [module-crm-reputation-management-nextjs](https://github.com/liberusoftware/module-crm-reputation-management-nextjs) (`@liberusoftware/module-crm-reputation-management-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-reputation-management](../../../modules/source/liberusoftware--module-crm-reputation-management.md) |
| API | [liberusoftware/module-crm-reputation-management-api](../../../modules/source/liberusoftware--module-crm-reputation-management-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Review requests** | Server Component loads authorized `review requests` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Review-site connections** | Server Component loads authorized `review-site connections` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Monitoring** | Server Component loads authorized `monitoring` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Response workflow** | Server Component loads authorized `response workflow` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Templates** | Server Component loads authorized `templates` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Escalation** | Server Component loads authorized `escalation` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Sentiment** | Server Component loads authorized `sentiment` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Location rollups** | Server Component loads authorized `location rollups` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Reputation reporting** | Server Component loads authorized `reputation reporting` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-crm-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ReputationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Queries/ReputationQuery.php) | `public function connections(int $teamId)`<br>`public function requests(int $teamId)`<br>`public function reviews(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function rollups(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConnectReviewSite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/ConnectReviewSite.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationConnection` |
| [CreateReviewRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/CreateReviewRequest.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationRequest` |
| [EscalateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/EscalateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId): ReputationReview` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RecordReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationReview` |
| [RespondToReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RespondToReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [SaveTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/SaveTemplate.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationTemplate` |
| [UpdateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/UpdateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [ReputationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Services/ReputationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ReputationConnection.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationConnection.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRollup.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRollup.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-reputation-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/reputation-management')->group(function (): void {
Route::get('/connections', [ReputationManagementController::class, 'connections']);
Route::post('/connections', [ReputationManagementController::class, 'connection']);
Route::get('/requests', [ReputationManagementController::class, 'requests']);
Route::post('/requests', [ReputationManagementController::class, 'request']);
Route::get('/reviews', [ReputationManagementController::class, 'reviews']);
Route::post('/reviews', [ReputationManagementController::class, 'review']);
Route::post('/reviews/{review}/respond', [ReputationManagementController::class, 'respond']);
Route::post('/templates', [ReputationManagementController::class, 'template']);
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
