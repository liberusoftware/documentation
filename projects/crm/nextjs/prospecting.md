# Prospecting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-prospecting`.

**Proposed design identifier:** `module-crm-prospecting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/prospecting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-prospecting](../../../modules/source/liberusoftware--module-crm-prospecting.md) |
| API | [liberusoftware/module-crm-prospecting-api](../../../modules/source/liberusoftware--module-crm-prospecting-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Ideal-customer profiles | A focused authorized view or workflow section for ideal-customer profiles; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Prospect searches | A focused authorized view or workflow section for prospect searches; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| List building | A focused authorized view or workflow section for list building; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Research queues | A focused authorized view or workflow section for research queues; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Contact reveal/credits | A focused authorized view or workflow section for contact reveal/credits; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Provider provenance | A focused authorized view or workflow section for provider provenance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Compliant export/outreach handoff | A focused authorized view or workflow section for compliant export/outreach handoff; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ProspectingQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateIdealCustomerProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [CreateProspectSearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [ImportProspect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function execute(int $teamId, int $userId, array $input): Prospect` |
| [QueueExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [QueueResearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [RevealContact.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [UpdateProspect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [ProspectingPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [IdealCustomerProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prospect.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectCredit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectResearchItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectSearch.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-prospecting-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/prospecting')->group(function (): void {
Route::get('/profiles', [ProspectingController::class, 'profiles']);
Route::post('/profiles', [ProspectingController::class, 'profile']);
Route::get('/searches', [ProspectingController::class, 'searches']);
Route::post('/searches', [ProspectingController::class, 'search']);
Route::get('/prospects', [ProspectingController::class, 'prospects']);
Route::post('/prospects', [ProspectingController::class, 'prospect']);
Route::post('/research', [ProspectingController::class, 'research']);
Route::post('/reveal', [ProspectingController::class, 'reveal']);
Route::post('/exports', [ProspectingController::class, 'export']);
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
