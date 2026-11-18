# Cash Flow Forecasting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-flow-forecasting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-cash-flow-forecasting-react-native
**Matching core package:** module-accounting-cash-flow-forecasting ([implementation](../core/cash-flow-forecasting.md))
**Matching API package:** module-accounting-cash-flow-forecasting-api ([contract](../api/cash-flow-forecasting.md))

## Implementation plan

This adapter presents Cash Flow Forecasting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cash Flow Forecasting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cash-flow-forecasting.md), and [API module](../api/cash-flow-forecasting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cash-flow-forecasting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cash-flow-forecasting.md)) |
| Capability React Native module skeleton | [`module-accounting-cash-flow-forecasting-react-native`](https://github.com/liberusoftware/module-accounting-cash-flow-forecasting-react-native) (`@liberusoftware/module-accounting-cash-flow-forecasting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Direct forecast** | Progressive mobile list/detail/sheet flow for `direct forecast` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opening cash** | Progressive mobile list/detail/sheet flow for `opening cash` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receivable/payable timing** | Progressive mobile list/detail/sheet flow for `receivable/payable timing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recurring items** | Progressive mobile list/detail/sheet flow for `recurring items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scenarios** | Progressive mobile list/detail/sheet flow for `scenarios` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Manual assumptions** | Progressive mobile list/detail/sheet flow for `manual assumptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variance** | Progressive mobile list/detail/sheet flow for `variance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Confidence** | Progressive mobile list/detail/sheet flow for `confidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashFlowForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Queries/CashFlowForecastQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/AddForecastItem.php) | `public function receivable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function payable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function recurring(CashFlowForecast $forecast, array $item): CashFlowForecast` |
| [CreateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/CreateCashFlowForecast.php) | `public function handle(array $attributes): CashFlowForecast` |
| [SetForecastScenario.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/SetForecastScenario.php) | `public function handle(CashFlowForecast $forecast, array $scenario): CashFlowForecast` |
| [UpdateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/UpdateCashFlowForecast.php) | `public function handle(CashFlowForecast $forecast, array $data): CashFlowForecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Models/CashFlowForecast.php) | `team_id`, `forecast_ref`, `currency`, `starts_on`, `ends_on`, `opening_cash`, `forecast_cash`, `variance`, `confidence`, `receivables`, `payables`, `recurring_items`, `scenarios`, `assumptions` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashFlowForecastsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-api/src/Http/Controllers/CashFlowForecastsController.php) | `public function index(CashFlowForecastQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCashFlowForecast $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-cash-flow-forecasting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-flow-forecasting')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.cash-flow-forecasting.read')->get('/', [CashFlowForecastsController::class, 'index']);
Route::middleware('ability:accounting.cash-flow-forecasting.write')->post('/', [CashFlowForecastsController::class, 'store']);
```
<!-- layer-implementation-plan:end -->
