# Accounting Kpi And Goals React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-kpi-and-goals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-kpi-and-goals-react-native
**Matching core package:** module-accounting-accounting-kpi-and-goals ([implementation](../core/accounting-kpi-and-goals.md))
**Matching API package:** module-accounting-accounting-kpi-and-goals-api ([contract](../api/accounting-kpi-and-goals.md))

## Implementation plan

This adapter presents Accounting Kpi And Goals for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Kpi And Goals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-kpi-and-goals.md), and [API module](../api/accounting-kpi-and-goals.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-kpi-and-goals`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-kpi-and-goals.md)) |
| Capability React Native module skeleton | [`module-accounting-kpi-and-goals-react-native`](https://github.com/liberusoftware/module-accounting-kpi-and-goals-react-native) (`@liberusoftware/module-accounting-kpi-and-goals-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Governed metrics** | Progressive mobile list/detail/sheet flow for `governed metrics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Targets** | Progressive mobile list/detail/sheet flow for `targets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Owners** | Progressive mobile list/detail/sheet flow for `owners` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Thresholds** | Progressive mobile list/detail/sheet flow for `thresholds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Periods** | Progressive mobile list/detail/sheet flow for `periods` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Alerts** | Progressive mobile list/detail/sheet flow for `alerts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Commentary** | Progressive mobile list/detail/sheet flow for `commentary` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **History** | Progressive mobile list/detail/sheet flow for `history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [KpiQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Queries/KpiQuery.php) | `public function goals(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function progress(KpiGoal $goal): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/AddCommentary.php) | `public function handle(KpiGoal $goal, string $actor, string $body, ?string $period = null): KpiCommentary` |
| [CreateGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateGoal.php) | `public function handle(KpiMetric $metric, array $attributes): KpiGoal` |
| [CreateMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateMetric.php) | `public function handle(array $attributes): KpiMetric` |
| [RecordMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/RecordMeasurement.php) | `public function handle(KpiGoal $goal, array $attributes): KpiMeasurement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [KpiAlert.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiAlert.php) | `team_id`, `goal_id`, `measurement_id`, `severity`, `status`, `message`, `triggered_at`, `acknowledged_by`, `resolved_at`, `metadata` |
| [KpiCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiCommentary.php) | `goal_id`, `actor_ref`, `body`, `period_ref`, `metadata` |
| [KpiGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiGoal.php) | `team_id`, `metric_id`, `goal_ref`, `name`, `owner_ref`, `period_start`, `period_end`, `baseline`, `target`, `warning_threshold`, `critical_threshold`, `status`, `metadata` |
| [KpiMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMeasurement.php) | `team_id`, `metric_id`, `goal_id`, `period_ref`, `measured_on`, `value`, `progress`, `source_ref`, `metadata` |
| [KpiMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMetric.php) | `team_id`, `metric_ref`, `name`, `description`, `unit`, `direction`, `source_contract`, `formula`, `owner_ref`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [KpiController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/src/Http/Controllers/KpiController.php) | `public function index(Request $request, KpiQuery $query): mixed`<br>`public function metric(Request $request, CreateMetric $action): JsonResponse`<br>`public function goal(Request $request, KpiMetric $metric, CreateGoal $action): KpiGoalResource`<br>`public function show(KpiGoal $goal, KpiQuery $query): array`<br>`public function measurement(Request $request, KpiGoal $goal, RecordMeasurement $action): JsonResponse`<br>`public function commentary(Request $request, KpiGoal $goal, AddCommentary $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-kpi-and-goals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/kpi-and-goals')->group(function (): void {
Route::get('/goals', [KpiController::class, 'index'])->name('accounting.kpi-and-goals.list');
Route::post('/metrics', [KpiController::class, 'metric'])->name('accounting.kpi-and-goals.metric');
Route::post('/metrics/{metric}/goals', [KpiController::class, 'goal'])->name('accounting.kpi-and-goals.goal');
Route::get('/goals/{goal}', [KpiController::class, 'show'])->name('accounting.kpi-and-goals.show');
Route::post('/goals/{goal}/measurements', [KpiController::class, 'measurement'])->name('accounting.kpi-and-goals.measurement');
Route::post('/goals/{goal}/commentary', [KpiController::class, 'commentary'])->name('accounting.kpi-and-goals.commentary');
```
<!-- layer-implementation-plan:end -->
