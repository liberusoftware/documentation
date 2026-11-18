# Browser Game Economy Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-economy). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-economy-flutter
**Matching core package:** module-browser-game-browser-game-economy ([implementation](../core/browser-game-economy.md))
**Matching API package:** module-browser-game-browser-game-economy-api ([contract](../api/browser-game-economy.md))

## Implementation plan

This adapter presents Browser Game Economy for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Economy API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/browser-game-economy.md), and [API module](../api/browser-game-economy.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `browser-game-economy`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-browser-game-economy-flutter`](https://github.com/liberusoftware/module-browser-game-economy-flutter) (`module_browser_game_economy_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-browser-game-economy-dart-mobile`](https://github.com/liberusoftware/module-browser-game-economy-dart-mobile) (`module_browser_game_economy_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-browser-game-economy-dart-desktop`](https://github.com/liberusoftware/module-browser-game-economy-dart-desktop) (`module_browser_game_economy_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/browser-game-economy.md) · [Core plan](../core/browser-game-economy.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Currencies** | Adaptive mobile cards/sheets for `currencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `currencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Faucets/sinks** | Adaptive mobile cards/sheets for `faucets/sinks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `faucets/sinks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Vendors** | Adaptive mobile cards/sheets for `vendors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `vendors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Pricing** | Adaptive mobile cards/sheets for `pricing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pricing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Trading** | Adaptive mobile cards/sheets for `trading` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `trading` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Auction house** | Adaptive mobile cards/sheets for `auction house` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `auction house` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fees** | Adaptive mobile cards/sheets for `fees` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fees` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Anti-abuse controls** | Adaptive mobile cards/sheets for `anti-abuse controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `anti-abuse controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
