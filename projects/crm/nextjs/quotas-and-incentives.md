# Quotas and Incentives: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-quotas-and-incentives`.

**Proposed design identifier:** `module-crm-quotas-and-incentives-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/quotas-and-incentives.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-quotas-and-incentives](../../../modules/source/liberusoftware--module-crm-quotas-and-incentives.md) |
| API | [liberusoftware/module-crm-quotas-and-incentives-api](../../../modules/source/liberusoftware--module-crm-quotas-and-incentives-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Quotas | A focused authorized view or workflow section for quotas; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Ramps | A focused authorized view or workflow section for ramps; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Crediting | A focused authorized view or workflow section for crediting; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Splits | A focused authorized view or workflow section for splits; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Territories | A focused authorized view or workflow section for territories; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Attainment | A focused authorized view or workflow section for attainment; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Commission plans | A focused authorized view or workflow section for commission plans; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Accelerators | A focused authorized view or workflow section for accelerators; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Adjustments | A focused authorized view or workflow section for adjustments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Disputes | A focused authorized view or workflow section for disputes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Payroll/export adapters | A focused authorized view or workflow section for payroll/export adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [QuotaQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Queries/QuotaQuery.php) | `public function quotas(int $teamId)`<br>`public function plans(int $teamId)`<br>`public function credits(int $teamId)`<br>`public function disputes(int $teamId)`<br>`public function exports(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateCommissionPlan.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateCommissionPlan.php) | `public function execute(int $teamId, int $userId, array $input): CommissionPlan` |
| [CreateQuota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateQuota.php) | `public function execute(int $teamId, int $userId, array $input): Quota` |
| [CreditCommission.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreditCommission.php) | `public function execute(int $teamId, int $userId, array $input): CommissionCredit` |
| [ExportCommissions.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ExportCommissions.php) | `public function execute(int $teamId, int $userId, array $input): CommissionExport` |
| [OpenDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/OpenDispute.php) | `public function execute(int $teamId, int $userId, array $input): CommissionDispute` |
| [ResolveDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ResolveDispute.php) | `public function execute(int $teamId, int $userId, int $disputeId, array $input): CommissionDispute` |
| [UpdateQuota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/UpdateQuota.php) | `public function execute(int $teamId, int $userId, int $quotaId, array $input): Quota` |
| [QuotaPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Services/QuotaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CommissionCredit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionPlan.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Quota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/Quota.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-quotas-and-incentives-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/quotas-and-incentives')->group(function (): void {
Route::get('/quotas', [QuotasAndIncentivesController::class, 'quotas']);
Route::post('/quotas', [QuotasAndIncentivesController::class, 'quota']);
Route::get('/plans', [QuotasAndIncentivesController::class, 'plans']);
Route::post('/plans', [QuotasAndIncentivesController::class, 'plan']);
Route::get('/credits', [QuotasAndIncentivesController::class, 'credits']);
Route::post('/credits', [QuotasAndIncentivesController::class, 'credit']);
Route::post('/disputes', [QuotasAndIncentivesController::class, 'dispute']);
Route::post('/disputes/{dispute}/resolve', [QuotasAndIncentivesController::class, 'resolve']);
Route::post('/exports', [QuotasAndIncentivesController::class, 'export']);
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
