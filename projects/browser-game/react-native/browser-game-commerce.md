# Browser Game Commerce React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-commerce). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-commerce-react-native
**Matching core package:** module-browser-game-browser-game-commerce ([implementation](../core/browser-game-commerce.md))
**Matching API package:** module-browser-game-browser-game-commerce-api ([contract](../api/browser-game-commerce.md))

## Implementation plan

This adapter presents Browser Game Commerce for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Commerce API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-commerce.md), and [API module](../api/browser-game-commerce.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-commerce`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-commerce.md)) |
| Capability React Native module skeleton | [`module-browser-game-commerce-react-native`](https://github.com/liberusoftware/module-browser-game-commerce-react-native) (`@liberusoftware/module-browser-game-commerce-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Premium membership** | Progressive mobile list/detail/sheet flow for `premium membership` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Entitlements** | Progressive mobile list/detail/sheet flow for `entitlements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Store** | Progressive mobile list/detail/sheet flow for `store` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Regional pricing** | Progressive mobile list/detail/sheet flow for `regional pricing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receipts** | Progressive mobile list/detail/sheet flow for `receipts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Refunds** | Progressive mobile list/detail/sheet flow for `refunds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Parental controls** | Progressive mobile list/detail/sheet flow for `parental controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CommerceQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Queries/CommerceQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommerceEntitlement.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrder.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrderLine.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrderLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceProduct.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommerceController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-api/src/Http/Controllers/CommerceController.php) | `public function index(Request $request): JsonResponse`<br>`public function products(Request $request): JsonResponse`<br>`public function checkout(Request $request): JsonResponse`<br>`public function complete(Request $request, CommerceOrder $order): JsonResponse`<br>`public function refund(Request $request, CommerceOrder $order): JsonResponse`<br>`public function show(Request $request, CommerceRecord $commerce): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-commerce-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/commerce')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CommerceController::class, 'index'])->name('browser-game.commerce.index');
Route::get('/products', [CommerceController::class, 'products'])->name('browser-game.commerce.products');
Route::post('/checkout', [CommerceController::class, 'checkout'])->name('browser-game.commerce.checkout');
Route::post('/orders/{order}/complete', [CommerceController::class, 'complete'])->name('browser-game.commerce.orders.complete');
Route::post('/orders/{order}/refund', [CommerceController::class, 'refund'])->name('browser-game.commerce.orders.refund');
Route::get('/{commerce}', [CommerceController::class, 'show'])->name('browser-game.commerce.show');
```
<!-- layer-implementation-plan:end -->
