# Economy React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#economy). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-economy-react-native
**Matching core package:** module-browser-game-economy ([implementation](../core/economy.md))
**Matching API package:** module-browser-game-economy-api ([contract](../api/economy.md))

## Implementation plan

This adapter presents Economy for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Economy API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/economy.md), and [API module](../api/economy.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `economy`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/economy.md)) |
| Capability React Native module skeleton | [`module-browser-game-economy-react-native`](https://github.com/liberusoftware/module-browser-game-economy-react-native) (`@liberusoftware/module-browser-game-economy-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Currencies** | Progressive mobile list/detail/sheet flow for `currencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Faucets/sinks** | Progressive mobile list/detail/sheet flow for `faucets/sinks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Vendors** | Progressive mobile list/detail/sheet flow for `vendors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pricing** | Progressive mobile list/detail/sheet flow for `pricing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trading** | Progressive mobile list/detail/sheet flow for `trading` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Auction house** | Progressive mobile list/detail/sheet flow for `auction house` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fees** | Progressive mobile list/detail/sheet flow for `fees` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Anti-abuse controls** | Progressive mobile list/detail/sheet flow for `anti-abuse controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EconomyQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Queries/EconomyQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EconomyLedgerEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyLedgerEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyListing.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyListing.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendor.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendor.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendorOffer.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendorOffer.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyWallet.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyWallet.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EconomyController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/src/Http/Controllers/EconomyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, EconomyRecord $economy): JsonResponse`<br>`public function wallet(Request $request): JsonResponse`<br>`public function transfer(Request $request): JsonResponse`<br>`public function credit(Request $request): JsonResponse`<br>`public function debit(Request $request): JsonResponse`<br>`public function vendors(Request $request): JsonResponse`<br>`public function createVendor(Request $request): JsonResponse`<br>`public function addOffer(Request $request, EconomyVendor $vendor): JsonResponse`<br>`public function purchaseOffer(Request $request, EconomyVendorOffer $offer): JsonResponse`<br>`public function listings(Request $request): JsonResponse`<br>`public function createListing(Request $request): JsonResponse`<br>`public function purchaseListing(Request $request, EconomyListing $listing): JsonResponse`<br>`public function cancelListing(Request $request, EconomyListing $listing): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-economy-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/economy')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [EconomyController::class, 'index'])->name('browser-game.economy.index');
Route::get('/wallet', [EconomyController::class, 'wallet'])->name('browser-game.economy.wallet');
Route::post('/transfer', [EconomyController::class, 'transfer'])->name('browser-game.economy.transfer');
Route::post('/wallet/credit', [EconomyController::class, 'credit'])->name('browser-game.economy.wallet.credit');
Route::post('/wallet/debit', [EconomyController::class, 'debit'])->name('browser-game.economy.wallet.debit');
Route::get('/vendors', [EconomyController::class, 'vendors'])->name('browser-game.economy.vendors');
Route::post('/vendors', [EconomyController::class, 'createVendor'])->name('browser-game.economy.vendors.create');
Route::post('/vendors/{vendor}/offers', [EconomyController::class, 'addOffer'])->name('browser-game.economy.vendors.offers.create');
Route::post('/offers/{offer}/purchase', [EconomyController::class, 'purchaseOffer'])->name('browser-game.economy.offers.purchase');
Route::get('/listings', [EconomyController::class, 'listings'])->name('browser-game.economy.listings');
Route::post('/listings', [EconomyController::class, 'createListing'])->name('browser-game.economy.listings.create');
Route::post('/listings/{listing}/purchase', [EconomyController::class, 'purchaseListing'])->name('browser-game.economy.listings.purchase');
Route::post('/listings/{listing}/cancel', [EconomyController::class, 'cancelListing'])->name('browser-game.economy.listings.cancel');
Route::get('/{economy}', [EconomyController::class, 'show'])->name('browser-game.economy.show');
```
<!-- layer-implementation-plan:end -->
