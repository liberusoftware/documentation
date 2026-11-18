# Forecasts React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#forecasts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-forecasts-react-native
**Matching core package:** module-accounting-forecasts ([implementation](../core/forecasts.md))
**Matching API package:** module-accounting-forecasts-api ([contract](../api/forecasts.md))

## Implementation plan

This adapter presents Forecasts for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Forecasts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/forecasts.md), and [API module](../api/forecasts.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `forecasts`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/forecasts.md)) |
| Capability React Native module skeleton | [`module-accounting-forecasts-react-native`](https://github.com/liberusoftware/module-accounting-forecasts-react-native) (`@liberusoftware/module-accounting-forecasts-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Driver/manual forecasts** | Progressive mobile list/detail/sheet flow for `driver/manual forecasts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Scenarios** | Progressive mobile list/detail/sheet flow for `scenarios` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rolling periods** | Progressive mobile list/detail/sheet flow for `rolling periods` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Actual replacement** | Progressive mobile list/detail/sheet flow for `actual replacement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assumptions** | Progressive mobile list/detail/sheet flow for `assumptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variance** | Progressive mobile list/detail/sheet flow for `variance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Queries/ForecastQuery.php) | `public function paginate(?int $teamId = null, ?ForecastStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Forecast $forecast): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastAssumption.php) | `public function handle(Forecast $forecast, array $attributes): ForecastAssumption` |
| [AddForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastLine.php) | `public function handle(Forecast $forecast, array $a): ForecastLine` |
| [CreateForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecast.php) | `public function handle(array $a): Forecast` |
| [CreateForecastPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecastPeriods.php) | `public function handle(Forecast $forecast, ?string $startsOn = null): array` |
| [DecideForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/DecideForecast.php) | `public function handle(Forecast $forecast, string $actor, bool $approved, ?string $comment = null): Forecast` |
| [ReplaceActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/ReplaceActual.php) | `public function handle(Forecast $forecast, array $a): ForecastActual` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/SubmitForecast.php) | `public function handle(Forecast $forecast): Forecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/Forecast.php) | `team_id`, `forecast_ref`, `name`, `currency`, `method`, `status`, `base_period`, `horizon_periods`, `scenario_ref`, `metadata` |
| [ForecastActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastActual.php) | `forecast_id`, `line_id`, `period_ref`, `actual_value`, `source_ref`, `replaced_at`, `metadata` |
| [ForecastApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastApproval.php) | `forecast_id`, `actor_ref`, `approved`, `comment`, `decided_at`, `metadata` |
| [ForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastAssumption.php) | `forecast_id`, `assumption_ref`, `name`, `value`, `unit`, `source`, `effective_from`, `effective_to`, `metadata` |
| [ForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastLine.php) | `forecast_id`, `period_ref`, `account_ref`, `dimension_ref`, `description`, `driver_ref`, `forecast_value`, `actual_value`, `variance_value`, `metadata` |
| [ForecastPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastPeriod.php) | `forecast_id`, `period_ref`, `starts_on`, `ends_on`, `status`, `is_rolling`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ForecastsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-api/src/Http/Controllers/ForecastsController.php) | `public function __construct(private readonly ForecastQuery $query)`<br>`public function index(Request $request): ForecastResource`<br>`public function store(Request $request, CreateForecast $action): ForecastResource`<br>`public function show(Forecast $forecast): ForecastResource`<br>`public function line(Request $request, Forecast $forecast, AddForecastLine $action): ForecastResource`<br>`public function assumption(Request $request, Forecast $forecast, AddForecastAssumption $action): ForecastResource`<br>`public function periods(Request $request, Forecast $forecast, CreateForecastPeriods $action): ForecastResource`<br>`public function submit(Forecast $forecast, SubmitForecast $action): ForecastResource`<br>`public function decide(Request $request, Forecast $forecast, DecideForecast $action): ForecastResource`<br>`public function actual(Request $request, Forecast $forecast, ReplaceActual $action): ForecastResource`<br>`public function variance(Forecast $forecast): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
