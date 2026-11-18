# Browser Game Crafting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-crafting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-crafting-react-native
**Matching core package:** module-browser-game-browser-game-crafting ([implementation](../core/browser-game-crafting.md))
**Matching API package:** module-browser-game-browser-game-crafting-api ([contract](../api/browser-game-crafting.md))

## Implementation plan

This adapter presents Browser Game Crafting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Crafting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-crafting.md), and [API module](../api/browser-game-crafting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-crafting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-crafting.md)) |
| Capability React Native module skeleton | [`module-browser-game-crafting-react-native`](https://github.com/liberusoftware/module-browser-game-crafting-react-native) (`@liberusoftware/module-browser-game-crafting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Recipes** | Progressive mobile list/detail/sheet flow for `recipes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Professions** | Progressive mobile list/detail/sheet flow for `professions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Resources** | Progressive mobile list/detail/sheet flow for `resources` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quality** | Progressive mobile list/detail/sheet flow for `quality` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queues** | Progressive mobile list/detail/sheet flow for `queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Discovery** | Progressive mobile list/detail/sheet flow for `discovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Salvage** | Progressive mobile list/detail/sheet flow for `salvage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Outputs** | Progressive mobile list/detail/sheet flow for `outputs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CraftingQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Queries/CraftingQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CraftingDiscovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingDiscovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingOutput.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingOutput.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingProfession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingProfession.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingQueue.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CraftingController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-api/src/Http/Controllers/CraftingController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CraftingRecord $crafting): JsonResponse`<br>`public function queue(Request $request): JsonResponse`<br>`public function queues(Request $request): JsonResponse`<br>`public function complete(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function cancel(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function salvage(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function discover(Request $request, CraftingRecord $crafting): JsonResponse`<br>`public function professions(Request $request): JsonResponse`<br>`public function resources(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-crafting-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/crafting')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CraftingController::class, 'index'])->name('browser-game.crafting.index');
Route::post('/queue', [CraftingController::class, 'queue'])->name('browser-game.crafting.queue');
Route::get('/queue', [CraftingController::class, 'queues'])->name('browser-game.crafting.queues');
Route::post('/queue/{queue}/complete', [CraftingController::class, 'complete'])->name('browser-game.crafting.queue.complete');
Route::post('/queue/{queue}/cancel', [CraftingController::class, 'cancel'])->name('browser-game.crafting.queue.cancel');
Route::post('/queue/{queue}/salvage', [CraftingController::class, 'salvage'])->name('browser-game.crafting.queue.salvage');
Route::get('/professions', [CraftingController::class, 'professions'])->name('browser-game.crafting.professions');
Route::get('/resources', [CraftingController::class, 'resources'])->name('browser-game.crafting.resources');
Route::post('/{crafting}/discover', [CraftingController::class, 'discover'])->name('browser-game.crafting.discover');
Route::get('/{crafting}', [CraftingController::class, 'show'])->name('browser-game.crafting.show');
```
<!-- layer-implementation-plan:end -->
