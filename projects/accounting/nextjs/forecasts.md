# Forecasts: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-forecasts`.

**Proposed design identifier:** `module-accounting-forecasts-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/forecasts.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-forecasts](../../../modules/source/liberusoftware--module-accounting-forecasts.md) |
| API | [liberusoftware/module-accounting-forecasts-api](../../../modules/source/liberusoftware--module-accounting-forecasts-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Driver/manual forecasts | A focused authorized view or workflow section for driver/manual forecasts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Scenarios | A focused authorized view or workflow section for scenarios; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rolling periods | A focused authorized view or workflow section for rolling periods; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Actual replacement | A focused authorized view or workflow section for actual replacement; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Assumptions | A focused authorized view or workflow section for assumptions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Variance | A focused authorized view or workflow section for variance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Queries/ForecastQuery.php) | `public function paginate(?int $teamId = null, ?ForecastStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Forecast $forecast): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastAssumption.php) | `public function handle(Forecast $forecast, array $attributes): ForecastAssumption` |
| [AddForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastLine.php) | `public function handle(Forecast $forecast, array $a): ForecastLine` |
| [CreateForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecast.php) | `public function handle(array $a): Forecast` |
| [CreateForecastPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecastPeriods.php) | `public function handle(Forecast $forecast, ?string $startsOn = null): array` |
| [DecideForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/DecideForecast.php) | `public function handle(Forecast $forecast, string $actor, bool $approved, ?string $comment = null): Forecast` |
| [ReplaceActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/ReplaceActual.php) | `public function handle(Forecast $forecast, array $a): ForecastActual` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/SubmitForecast.php) | `public function handle(Forecast $forecast): Forecast` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/Forecast.php) | `team_id`, `forecast_ref`, `name`, `currency`, `method`, `status`, `base_period`, `horizon_periods`, `scenario_ref`, `metadata` |
| [ForecastActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastActual.php) | `forecast_id`, `line_id`, `period_ref`, `actual_value`, `source_ref`, `replaced_at`, `metadata` |
| [ForecastApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastApproval.php) | `forecast_id`, `actor_ref`, `approved`, `comment`, `decided_at`, `metadata` |
| [ForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastAssumption.php) | `forecast_id`, `assumption_ref`, `name`, `value`, `unit`, `source`, `effective_from`, `effective_to`, `metadata` |
| [ForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastLine.php) | `forecast_id`, `period_ref`, `account_ref`, `dimension_ref`, `description`, `driver_ref`, `forecast_value`, `actual_value`, `variance_value`, `metadata` |
| [ForecastPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastPeriod.php) | `forecast_id`, `period_ref`, `starts_on`, `ends_on`, `status`, `is_rolling`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-forecasts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/forecasts')->group(function (): void {
Route::middleware('ability:accounting.forecasts.read')->group(function (): void {
Route::get('/', [ForecastsController::class, 'index'])->name('accounting.forecasts.list');
Route::get('/{forecast}', [ForecastsController::class, 'show'])->name('accounting.forecasts.show');
Route::get('/{forecast}/variance', [ForecastsController::class, 'variance'])->name('accounting.forecasts.variance');
Route::middleware('ability:accounting.forecasts.write')->group(function (): void {
Route::post('/', [ForecastsController::class, 'store'])->name('accounting.forecasts.create');
Route::post('/{forecast}/lines', [ForecastsController::class, 'line'])->name('accounting.forecasts.line');
Route::post('/{forecast}/assumptions', [ForecastsController::class, 'assumption'])->name('accounting.forecasts.assumption');
Route::post('/{forecast}/periods', [ForecastsController::class, 'periods'])->name('accounting.forecasts.periods');
Route::post('/{forecast}/submit', [ForecastsController::class, 'submit'])->name('accounting.forecasts.submit');
Route::post('/{forecast}/decide', [ForecastsController::class, 'decide'])->name('accounting.forecasts.decide');
Route::post('/{forecast}/actuals', [ForecastsController::class, 'actual'])->name('accounting.forecasts.actual');
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
