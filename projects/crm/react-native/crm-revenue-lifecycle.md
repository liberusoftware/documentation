# Crm Revenue Lifecycle React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-revenue-lifecycle). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-revenue-lifecycle-react-native
**Matching core package:** module-crm-crm-revenue-lifecycle ([implementation](../core/crm-revenue-lifecycle.md))
**Matching API package:** module-crm-crm-revenue-lifecycle-api ([contract](../api/crm-revenue-lifecycle.md))

## Implementation plan

This adapter presents Crm Revenue Lifecycle for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Revenue Lifecycle API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-revenue-lifecycle.md), and [API module](../api/crm-revenue-lifecycle.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-revenue-lifecycle`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-revenue-lifecycle.md)) |
| Capability React Native module skeleton | [`module-crm-revenue-lifecycle-react-native`](https://github.com/liberusoftware/module-crm-revenue-lifecycle-react-native) (`@liberusoftware/module-crm-revenue-lifecycle-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Opportunity-to-order orchestration** | Progressive mobile list/detail/sheet flow for `opportunity-to-order orchestration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assets/installed products** | Progressive mobile list/detail/sheet flow for `assets/installed products` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Entitlements** | Progressive mobile list/detail/sheet flow for `entitlements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Renewals** | Progressive mobile list/detail/sheet flow for `renewals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Upgrades** | Progressive mobile list/detail/sheet flow for `upgrades` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Downgrades** | Progressive mobile list/detail/sheet flow for `downgrades` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cancellation** | Progressive mobile list/detail/sheet flow for `cancellation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage signals** | Progressive mobile list/detail/sheet flow for `usage signals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fallout queues** | Progressive mobile list/detail/sheet flow for `fallout queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Queries/RevenueQuery.php) | `public function assets(int $teamId)`<br>`public function orders(int $teamId)`<br>`public function fallout(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/CreateOrder.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueOrder` |
| [ManageAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ManageAsset.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueAsset` |
| [RecordUsageSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/RecordUsageSignal.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assetId, array $input): RevenueAsset` |
| [ResolveFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ResolveFallout.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $falloutId, array $input): RevenueFallout` |
| [RevenuePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Services/RevenuePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueFallout.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueOrder.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueLifecycleController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-api/src/Http/Controllers/RevenueLifecycleController.php) | `public function assets(Request $request, RevenueQuery $query)`<br>`public function asset(Request $request, ManageAsset $action)`<br>`public function order(Request $request, CreateOrder $action)`<br>`public function usage(Request $request, int $asset, RecordUsageSignal $action)`<br>`public function fallout(Request $request, RevenueQuery $query)`<br>`public function resolveFallout(Request $request, int $fallout, ResolveFallout $action)` |

**Observed route declarations:**

[modules/crm-revenue-lifecycle-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-lifecycle')->group(function (): void {
Route::get('/assets', [RevenueLifecycleController::class, 'assets']);
Route::post('/assets', [RevenueLifecycleController::class, 'asset']);
Route::post('/assets/{asset}/usage', [RevenueLifecycleController::class, 'usage']);
Route::post('/orders', [RevenueLifecycleController::class, 'order']);
Route::get('/fallout', [RevenueLifecycleController::class, 'fallout']);
Route::post('/fallout/{fallout}/resolve', [RevenueLifecycleController::class, 'resolveFallout']);
```
<!-- layer-implementation-plan:end -->
