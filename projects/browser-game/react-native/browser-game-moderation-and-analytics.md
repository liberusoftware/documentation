# Browser Game Moderation And Analytics React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-moderation-and-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-moderation-and-analytics-react-native
**Matching core package:** module-browser-game-browser-game-moderation-and-analytics ([implementation](../core/browser-game-moderation-and-analytics.md))
**Matching API package:** module-browser-game-browser-game-moderation-and-analytics-api ([contract](../api/browser-game-moderation-and-analytics.md))

## Implementation plan

This adapter presents Browser Game Moderation And Analytics for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Moderation And Analytics API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-moderation-and-analytics.md), and [API module](../api/browser-game-moderation-and-analytics.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-moderation-and-analytics`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-moderation-and-analytics.md)) |
| Capability React Native module skeleton | [`module-browser-game-moderation-and-analytics-react-native`](https://github.com/liberusoftware/module-browser-game-moderation-and-analytics-react-native) (`@liberusoftware/module-browser-game-moderation-and-analytics-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Reports** | Progressive mobile list/detail/sheet flow for `reports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sanctions** | Progressive mobile list/detail/sheet flow for `sanctions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Appeals** | Progressive mobile list/detail/sheet flow for `appeals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Telemetry** | Progressive mobile list/detail/sheet flow for `telemetry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Funnels** | Progressive mobile list/detail/sheet flow for `funnels` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Balance** | Progressive mobile list/detail/sheet flow for `balance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Economy** | Progressive mobile list/detail/sheet flow for `economy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fraud** | Progressive mobile list/detail/sheet flow for `fraud` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Health** | Progressive mobile list/detail/sheet flow for `health` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ModerationAndAnalyticsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/src/Http/Controllers/ModerationAndAnalyticsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function report(Request $request): JsonResponse`<br>`public function sanction(Request $request): JsonResponse`<br>`public function appeal(Request $request): JsonResponse`<br>`public function telemetry(Request $request): JsonResponse`<br>`public function funnel(Request $request): JsonResponse`<br>`public function balance(Request $request): JsonResponse`<br>`public function economy(Request $request): JsonResponse`<br>`public function fraud(Request $request): JsonResponse`<br>`public function health(Request $request): JsonResponse`<br>`public function resolve(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse`<br>`public function show(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-moderation-and-analytics-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/moderation-and-analytics')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ModerationAndAnalyticsController::class, 'index'])->name('browser-game.moderation-and-analytics.index');
Route::post('/', [ModerationAndAnalyticsController::class, 'store'])->name('browser-game.moderation-and-analytics.store');
Route::post('/reports', [ModerationAndAnalyticsController::class, 'report'])->name('browser-game.moderation-and-analytics.reports');
Route::post('/sanctions', [ModerationAndAnalyticsController::class, 'sanction'])->name('browser-game.moderation-and-analytics.sanctions');
Route::post('/appeals', [ModerationAndAnalyticsController::class, 'appeal'])->name('browser-game.moderation-and-analytics.appeals');
Route::post('/telemetry', [ModerationAndAnalyticsController::class, 'telemetry'])->name('browser-game.moderation-and-analytics.telemetry');
Route::post('/funnels', [ModerationAndAnalyticsController::class, 'funnel'])->name('browser-game.moderation-and-analytics.funnels');
Route::post('/balance', [ModerationAndAnalyticsController::class, 'balance'])->name('browser-game.moderation-and-analytics.balance');
Route::post('/economy', [ModerationAndAnalyticsController::class, 'economy'])->name('browser-game.moderation-and-analytics.economy');
Route::post('/fraud', [ModerationAndAnalyticsController::class, 'fraud'])->name('browser-game.moderation-and-analytics.fraud');
Route::post('/health', [ModerationAndAnalyticsController::class, 'health'])->name('browser-game.moderation-and-analytics.health');
Route::post('/{moderationAndAnalytics}/resolve', [ModerationAndAnalyticsController::class, 'resolve'])->name('browser-game.moderation-and-analytics.resolve');
Route::get('/{moderationAndAnalytics}', [ModerationAndAnalyticsController::class, 'show'])->name('browser-game.moderation-and-analytics.show');
```
<!-- layer-implementation-plan:end -->
