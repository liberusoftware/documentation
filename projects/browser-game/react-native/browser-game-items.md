# Browser Game Items React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-items). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-items-react-native
**Matching core package:** module-browser-game-browser-game-items ([implementation](../core/browser-game-items.md))
**Matching API package:** module-browser-game-browser-game-items-api ([contract](../api/browser-game-items.md))

## Implementation plan

This adapter presents Browser Game Items for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Items API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-items.md), and [API module](../api/browser-game-items.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-items`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-items.md)) |
| Capability React Native module skeleton | [`module-browser-game-items-react-native`](https://github.com/liberusoftware/module-browser-game-items-react-native) (`@liberusoftware/module-browser-game-items-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Definitions** | Progressive mobile list/detail/sheet flow for `definitions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Inventory** | Progressive mobile list/detail/sheet flow for `inventory` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Equipment** | Progressive mobile list/detail/sheet flow for `equipment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Durability** | Progressive mobile list/detail/sheet flow for `durability` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Binding** | Progressive mobile list/detail/sheet flow for `binding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Containers** | Progressive mobile list/detail/sheet flow for `containers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Stack rules** | Progressive mobile list/detail/sheet flow for `stack rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provenance** | Progressive mobile list/detail/sheet flow for `provenance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ItemsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Queries/ItemsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InventoryEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/InventoryEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [ItemsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/ItemsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ItemsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-api/src/Http/Controllers/ItemsController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, ItemsRecord $items): JsonResponse`<br>`public function inventory(Request $request): JsonResponse`<br>`public function addToInventory(Request $request, ItemsRecord $item): JsonResponse`<br>`public function removeFromInventory(Request $request, ItemsRecord $item): JsonResponse`<br>`public function equip(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function unequip(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function bind(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function durability(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function container(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function provenance(Request $request, InventoryEntry $entry): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-items-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/items')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ItemsController::class, 'index'])->name('browser-game.items.index');
Route::get('/inventory/me', [ItemsController::class, 'inventory'])->name('browser-game.items.inventory');
Route::post('/inventory/{item}/add', [ItemsController::class, 'addToInventory'])->name('browser-game.items.inventory.add');
Route::post('/inventory/{item}/remove', [ItemsController::class, 'removeFromInventory'])->name('browser-game.items.inventory.remove');
Route::post('/inventory/entries/{entry}/equip', [ItemsController::class, 'equip'])->name('browser-game.items.inventory.equip');
Route::post('/inventory/entries/{entry}/unequip', [ItemsController::class, 'unequip'])->name('browser-game.items.inventory.unequip');
Route::post('/inventory/entries/{entry}/bind', [ItemsController::class, 'bind'])->name('browser-game.items.inventory.bind');
Route::post('/inventory/entries/{entry}/durability', [ItemsController::class, 'durability'])->name('browser-game.items.inventory.durability');
Route::post('/inventory/entries/{entry}/container', [ItemsController::class, 'container'])->name('browser-game.items.inventory.container');
Route::post('/inventory/entries/{entry}/provenance', [ItemsController::class, 'provenance'])->name('browser-game.items.inventory.provenance');
Route::get('/{items}', [ItemsController::class, 'show'])->name('browser-game.items.show');
```
<!-- layer-implementation-plan:end -->
