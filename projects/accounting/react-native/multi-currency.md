# Multi Currency React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-currency). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-multi-currency-react-native
**Matching core package:** module-accounting-multi-currency ([implementation](../core/multi-currency.md))
**Matching API package:** module-accounting-multi-currency-api ([contract](../api/multi-currency.md))

## Implementation plan

This adapter presents Multi Currency for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Multi Currency API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/multi-currency.md), and [API module](../api/multi-currency.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `multi-currency`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/multi-currency.md)) |
| Capability React Native module skeleton | [`module-accounting-multi-currency-react-native`](https://github.com/liberusoftware/module-accounting-multi-currency-react-native) (`@liberusoftware/module-accounting-multi-currency-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Transaction/functional/reporting currencies** | Progressive mobile list/detail/sheet flow for `transaction/functional/reporting currencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rates** | Progressive mobile list/detail/sheet flow for `rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revaluation** | Progressive mobile list/detail/sheet flow for `revaluation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Realized/unrealized gains** | Progressive mobile list/detail/sheet flow for `realized/unrealized gains` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Historical rates** | Progressive mobile list/detail/sheet flow for `historical rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CurrencyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Queries/CurrencyQuery.php) | `public function rates(?int $teamId = null, ?string $from = null, ?string $to = null, int $perPage = 25): LengthAwarePaginator`<br>`public function revaluations(?int $teamId = null): LengthAwarePaginator`<br>`public function report(RevaluationRun $run): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureCurrency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/ConfigureCurrency.php) | `public function handle(array $attributes): CurrencyProfile` |
| [CreateRevaluation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/CreateRevaluation.php) | `public function handle(array $attributes, array $positions): RevaluationRun` |
| [RecordExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/RecordExchangeRate.php) | `public function handle(array $attributes): ExchangeRate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CurrencyProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyProfile.php) | `team_id`, `scope_ref`, `currency`, `role`, `is_active`, `metadata` |
| [CurrencyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_gain_loss`, `actual_gain_loss`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/ExchangeRate.php) | `team_id`, `from_currency`, `to_currency`, `rate_date`, `rate`, `source`, `rate_type`, `is_historical`, `metadata` |
| [RevaluationPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationPosition.php) | `run_id`, `reference_type`, `reference_id`, `currency`, `foreign_amount`, `book_rate`, `closing_rate`, `book_value`, `closing_value`, `gain_loss`, `gain_status`, `metadata` |
| [RevaluationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationRun.php) | `team_id`, `run_ref`, `scope_ref`, `as_of_date`, `functional_currency`, `status`, `source_hash`, `realized_gain`, `realized_loss`, `unrealized_gain`, `unrealized_loss`, `summary`, `failure_message`, `requested_by`, `posted_by`, `posted_at`, `metadata` |
| [Currency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Models/Currency.php) | `code`, `name`, `symbol`, `is_default` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MultiCurrencyController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Http/Controllers/MultiCurrencyController.php) | `public function rates(Request $request, CurrencyQuery $query): mixed`<br>`public function profile(Request $request, ConfigureCurrency $action): JsonResponse`<br>`public function rate(Request $request, RecordExchangeRate $action): JsonResponse`<br>`public function revaluation(Request $request, CreateRevaluation $action): JsonResponse`<br>`public function show(RevaluationRun $revaluationRun): RevaluationResource`<br>`public function report(RevaluationRun $revaluationRun, CurrencyQuery $query): array` |

**Observed route declarations:**

[modules/accounting-multi-currency-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/multi-currency')->group(function (): void {
Route::get('/rates', [MultiCurrencyController::class, 'rates'])->name('accounting.multi-currency.rates');
Route::post('/profiles', [MultiCurrencyController::class, 'profile'])->name('accounting.multi-currency.profile');
Route::post('/rates', [MultiCurrencyController::class, 'rate'])->name('accounting.multi-currency.rate');
Route::post('/revaluations', [MultiCurrencyController::class, 'revaluation'])->name('accounting.multi-currency.revaluation');
Route::get('/revaluations/{revaluationRun}', [MultiCurrencyController::class, 'show'])->name('accounting.multi-currency.show');
Route::get('/revaluations/{revaluationRun}/report', [MultiCurrencyController::class, 'report'])->name('accounting.multi-currency.report');
```
<!-- layer-implementation-plan:end -->
