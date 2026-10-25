# Customer Data Platform: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-customer-data-platform`.

**Proposed design identifier:** `module-crm-customer-data-platform-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/customer-data-platform.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-customer-data-platform](../../../modules/source/liberusoftware--module-crm-customer-data-platform.md) |
| API | [liberusoftware/module-crm-customer-data-platform-api](../../../modules/source/liberusoftware--module-crm-customer-data-platform-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Source profiles | A focused authorized view or workflow section for source profiles; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Identity resolution | A focused authorized view or workflow section for identity resolution; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Unified profiles | A focused authorized view or workflow section for unified profiles; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Audience activation | A focused authorized view or workflow section for audience activation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Event ingestion | A focused authorized view or workflow section for event ingestion; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Consent-aware calculated attributes | A focused authorized view or workflow section for consent-aware calculated attributes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Profile lineage | A focused authorized view or workflow section for profile lineage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CdpQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Queries/CdpQuery.php) | `public function profiles(int $teamId)`<br>`public function audiences(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ActivateCdpAudience.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/ActivateCdpAudience.php) | `public function execute(int $teamId, int $userId, CdpAudience $audience, string $destination): CdpAudience` |
| [CreateCdpAudience.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/CreateCdpAudience.php) | `public function execute(int $teamId, int $userId, array $input): CdpAudience` |
| [IngestCdpEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/IngestCdpEvent.php) | `public function execute(int $teamId, CdpProfile $profile, array $input): CdpEvent` |
| [UpsertCdpProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/UpsertCdpProfile.php) | `public function execute(int $teamId, int $userId, array $input): CdpProfile` |
| [CdpPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Services/CdpPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CdpAudience.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpAudience.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpIdentity.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpIdentity.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpProfile.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-customer-data-platform-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-data-platform')->group(function (): void {
Route::get('profiles', [CdpController::class, 'profiles']);
Route::post('profiles', [CdpController::class, 'storeProfile']);
Route::post('profiles/{profile}/events', [CdpController::class, 'event']);
Route::get('audiences', [CdpController::class, 'audiences']);
Route::post('audiences', [CdpController::class, 'storeAudience']);
Route::post('audiences/{audience}/activate', [CdpController::class, 'activate']);
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
