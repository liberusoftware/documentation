# Real Estate Onthemarket React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-onthemarket). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-onthemarket-react-native
**Matching core package:** module-real-estate-real-estate-onthemarket ([implementation](../core/real-estate-onthemarket.md))
**Matching API package:** module-real-estate-real-estate-onthemarket-api ([contract](../api/real-estate-onthemarket.md))

## Implementation plan

This adapter presents Real Estate Onthemarket for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Onthemarket API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-onthemarket.md), and [API module](../api/real-estate-onthemarket.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-onthemarket`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-onthemarket.md)) |
| Capability React Native module skeleton | [`module-real-estate-onthemarket-react-native`](https://github.com/liberusoftware/module-real-estate-onthemarket-react-native) (`@liberusoftware/module-real-estate-onthemarket-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **OnTheMarket sync state** | Progressive mobile list/detail/sheet flow for `onthemarket sync state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider payload boundary** | Progressive mobile list/detail/sheet flow for `provider payload boundary` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retry and error state** | Progressive mobile list/detail/sheet flow for `retry and error state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OnTheMarketTransport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket/src/Contracts/OnTheMarketTransport.php) | `public function sendProperty(string $reference, array $payload, array $credentials): array`<br>`public function removeProperty(string $reference, array $credentials): array`<br>`public function branchPropertyList(array $credentials): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OnTheMarketSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket/src/Models/OnTheMarketSync.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OnTheMarketSyncController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket-api/src/Http/Controllers/OnTheMarketSyncController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateOnTheMarketSync $create): JsonResponse`<br>`public function show(Request $request, OnTheMarketSync $onTheMarketSync): JsonResponse`<br>`public function sync(Request $request, OnTheMarketSync $onTheMarketSync, SyncOnTheMarketListing $sync): JsonResponse`<br>`public function update(Request $request, OnTheMarketSync $onTheMarketSync, UpdateOnTheMarketSync $update): JsonResponse`<br>`public function destroy(Request $request, OnTheMarketSync $onTheMarketSync, DeleteOnTheMarketSync $delete): Response` |

**Observed route declarations:**

[modules/real-estate-onthemarket-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/integrations/onthemarket/syncs')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [OnTheMarketSyncController::class, 'index']);
Route::post('/', [OnTheMarketSyncController::class, 'store']);
Route::post('/{onTheMarketSync}/sync', [OnTheMarketSyncController::class, 'sync']);
Route::get('/{onTheMarketSync}', [OnTheMarketSyncController::class, 'show']);
Route::delete('/{onTheMarketSync}', [OnTheMarketSyncController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
