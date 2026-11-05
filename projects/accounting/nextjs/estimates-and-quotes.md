# Estimates and Quotes: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-estimates-and-quotes`.

**Proposed design identifier:** `module-accounting-estimates-and-quotes-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/estimates-and-quotes.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-estimates-and-quotes](../../../modules/source/liberusoftware--module-accounting-estimates-and-quotes.md) |
| API | [liberusoftware/module-accounting-estimates-and-quotes-api](../../../modules/source/liberusoftware--module-accounting-estimates-and-quotes-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Branded estimates/quotes | A focused authorized view or workflow section for branded estimates/quotes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Items | A focused authorized view or workflow section for items; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Terms | A focused authorized view or workflow section for terms; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Versions | A focused authorized view or workflow section for versions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery | A focused authorized view or workflow section for delivery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Acceptance/decline | A focused authorized view or workflow section for acceptance/decline; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Expiry | A focused authorized view or workflow section for expiry; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Conversion | A focused authorized view or workflow section for conversion; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| History | A focused authorized view or workflow section for history; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [EstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Queries/EstimateQuery.php) | `public function paginate(?int $legalEntityId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(Estimate $e): float` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddEstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/AddEstimateItem.php) | `public function handle(Estimate $e, array $a): EstimateItem` |
| [ConvertEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ConvertEstimate.php) | `public function handle(Estimate $e, string $convertedRef, ?string $actor = null): Estimate` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/CreateEstimate.php) | `public function handle(array $a): Estimate` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/DecideEstimate.php) | `public function handle(Estimate $e, bool $accepted, ?string $reason = null, ?string $actor = null): Estimate` |
| [ExpireEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ExpireEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |
| [SendEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/SendEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Estimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/Estimate.php) | `legal_entity_id`, `customer_ref`, `quote_ref`, `name`, `currency`, `status`, `issue_date`, `expires_on`, `version`, `terms`, `brand`, `accepted_at`, `declined_reason`, `converted_ref`, `metadata` |
| [EstimateHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateHistory.php) | `estimate_id`, `event`, `actor_ref`, `metadata` |
| [EstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateItem.php) | `estimate_id`, `item_ref`, `description`, `quantity`, `unit_price`, `tax_rate`, `amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateVersion.php) | `estimate_id`, `version`, `snapshot`, `created_by` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-estimates-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/estimates-and-quotes')->group(function (): void {
Route::middleware('ability:accounting.estimates-and-quotes.read')->group(function (): void {
Route::get('/', [EstimatesController::class, 'index']);
Route::get('/{estimate}', [EstimatesController::class, 'show']);
Route::middleware('ability:accounting.estimates-and-quotes.write')->group(function (): void {
Route::post('/', [EstimatesController::class, 'store']);
Route::post('/{estimate}/items', [EstimatesController::class, 'item']);
Route::post('/{estimate}/send', [EstimatesController::class, 'send']);
Route::post('/{estimate}/decide', [EstimatesController::class, 'decide']);
Route::post('/{estimate}/expire', [EstimatesController::class, 'expire']);
Route::post('/{estimate}/convert', [EstimatesController::class, 'convert']);
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
