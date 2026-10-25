# Multi-Currency: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-multi-currency`.

**Proposed design identifier:** `module-accounting-multi-currency-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/multi-currency.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-multi-currency](../../../modules/source/liberusoftware--module-accounting-multi-currency.md) |
| API | [liberusoftware/module-accounting-multi-currency-api](../../../modules/source/liberusoftware--module-accounting-multi-currency-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Transaction/functional/reporting currencies | A focused authorized view or workflow section for transaction/functional/reporting currencies; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rates | A focused authorized view or workflow section for rates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Revaluation | A focused authorized view or workflow section for revaluation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Realized/unrealized gains | A focused authorized view or workflow section for realized/unrealized gains; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Historical rates | A focused authorized view or workflow section for historical rates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reconciliation | A focused authorized view or workflow section for reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CurrencyQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Queries/CurrencyQuery.php) | `public function rates(?int $teamId = null, ?string $from = null, ?string $to = null, int $perPage = 25): LengthAwarePaginator`<br>`public function revaluations(?int $teamId = null): LengthAwarePaginator`<br>`public function report(RevaluationRun $run): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConfigureCurrency.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/ConfigureCurrency.php) | `public function handle(array $attributes): CurrencyProfile` |
| [CreateRevaluation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/CreateRevaluation.php) | `public function handle(array $attributes, array $positions): RevaluationRun` |
| [RecordExchangeRate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/RecordExchangeRate.php) | `public function handle(array $attributes): ExchangeRate` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CurrencyProfile.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyProfile.php) | `team_id`, `scope_ref`, `currency`, `role`, `is_active`, `metadata` |
| [CurrencyReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_gain_loss`, `actual_gain_loss`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ExchangeRate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/ExchangeRate.php) | `team_id`, `from_currency`, `to_currency`, `rate_date`, `rate`, `source`, `rate_type`, `is_historical`, `metadata` |
| [RevaluationPosition.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationPosition.php) | `run_id`, `reference_type`, `reference_id`, `currency`, `foreign_amount`, `book_rate`, `closing_rate`, `book_value`, `closing_value`, `gain_loss`, `gain_status`, `metadata` |
| [RevaluationRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationRun.php) | `team_id`, `run_ref`, `scope_ref`, `as_of_date`, `functional_currency`, `status`, `source_hash`, `realized_gain`, `realized_loss`, `unrealized_gain`, `unrealized_loss`, `summary`, `failure_message`, `requested_by`, `posted_by`, `posted_at`, `metadata` |
| [Currency.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Models/Currency.php) | `code`, `name`, `symbol`, `is_default` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-multi-currency-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/multi-currency')->group(function (): void {
Route::get('/rates', [MultiCurrencyController::class, 'rates'])->name('accounting.multi-currency.rates');
Route::post('/profiles', [MultiCurrencyController::class, 'profile'])->name('accounting.multi-currency.profile');
Route::post('/rates', [MultiCurrencyController::class, 'rate'])->name('accounting.multi-currency.rate');
Route::post('/revaluations', [MultiCurrencyController::class, 'revaluation'])->name('accounting.multi-currency.revaluation');
Route::get('/revaluations/{revaluationRun}', [MultiCurrencyController::class, 'show'])->name('accounting.multi-currency.show');
Route::get('/revaluations/{revaluationRun}/report', [MultiCurrencyController::class, 'report'])->name('accounting.multi-currency.report');
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
