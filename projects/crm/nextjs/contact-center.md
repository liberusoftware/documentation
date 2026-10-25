# Contact Center: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-contact-center`.

**Proposed design identifier:** `module-crm-contact-center-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/contact-center.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-contact-center](../../../modules/source/liberusoftware--module-crm-contact-center.md) |
| API | [liberusoftware/module-crm-contact-center-api](../../../modules/source/liberusoftware--module-crm-contact-center-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Agent presence | A focused authorized view or workflow section for agent presence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Capacity | A focused authorized view or workflow section for capacity; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Skills | A focused authorized view or workflow section for skills; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Routing | A focused authorized view or workflow section for routing; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Supervisor views | A focused authorized view or workflow section for supervisor views; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Whisper/barge policy | A focused authorized view or workflow section for whisper/barge policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Quality review | A focused authorized view or workflow section for quality review; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Workforce demand | A focused authorized view or workflow section for workforce demand; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Queue SLA | A focused authorized view or workflow section for queue sla; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Overflow | A focused authorized view or workflow section for overflow; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ContactCenterQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Queries/ContactCenterQuery.php) | `public function agents(int $teamId): Builder`<br>`public function supervisorView(int $teamId): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ReviewQuality.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/ReviewQuality.php) | `public function execute(int $teamId, int $eventId, int $reviewerId, array $scorecard): ContactCenterEvent` |
| [RouteInteraction.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/RouteInteraction.php) | `public function execute(int $teamId, string $queueKey, string $requiredSkill, int $slaSeconds = 300): ContactCenterEvent` |
| [SetAgentPresence.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/SetAgentPresence.php) | `public function execute(int $teamId, int $userId, string $presence, int $capacity = 1, array $skills = []): ContactCenterAgent` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ContactCenterAgent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactCenterEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterEvent.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-contact-center-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/contact-center')->group(function (): void {
Route::get('agents', [ContactCenterController::class, 'agents']);
Route::post('presence', [ContactCenterController::class, 'presence']);
Route::post('route', [ContactCenterController::class, 'route']);
Route::get('supervisor', [ContactCenterController::class, 'supervisor']);
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
