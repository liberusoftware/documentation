# Browser Game Quests React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-quests). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-quests-react-native
**Matching core package:** module-browser-game-browser-game-quests ([implementation](../core/browser-game-quests.md))
**Matching API package:** module-browser-game-browser-game-quests-api ([contract](../api/browser-game-quests.md))

## Implementation plan

This adapter presents Browser Game Quests for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Quests API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-quests.md), and [API module](../api/browser-game-quests.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-quests`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-quests.md)) |
| Capability React Native module skeleton | [`module-browser-game-quests-react-native`](https://github.com/liberusoftware/module-browser-game-quests-react-native) (`@liberusoftware/module-browser-game-quests-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Storylines** | Progressive mobile list/detail/sheet flow for `storylines` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Objectives** | Progressive mobile list/detail/sheet flow for `objectives` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Prerequisites** | Progressive mobile list/detail/sheet flow for `prerequisites` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Branching** | Progressive mobile list/detail/sheet flow for `branching` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dialogue** | Progressive mobile list/detail/sheet flow for `dialogue` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rewards** | Progressive mobile list/detail/sheet flow for `rewards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Repeatability** | Progressive mobile list/detail/sheet flow for `repeatability` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Progress** | Progressive mobile list/detail/sheet flow for `progress` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [QuestQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Queries/QuestQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function activeFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function completedFor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Quest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/Quest.php) | No literal fillable array detected; inspect the model and API schema. |
| [QuestProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/QuestProgress.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [QuestsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/src/Http/Controllers/QuestsController.php) | `public function index(Request $request): JsonResponse`<br>`public function available(Request $request): JsonResponse`<br>`public function active(Request $request): JsonResponse`<br>`public function completed(Request $request): JsonResponse`<br>`public function show(Request $request, Quest $quest): JsonResponse`<br>`public function progress(Request $request, Quest $quest): JsonResponse`<br>`public function accept(Request $request, Quest $quest): JsonResponse`<br>`public function complete(Request $request, Quest $quest): JsonResponse`<br>`public function abandon(Request $request, Quest $quest): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-quests-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/quests')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [QuestsController::class, 'index'])->name('browser-game.quests.index');
Route::get('/available', [QuestsController::class, 'available'])->name('browser-game.quests.available');
Route::get('/active', [QuestsController::class, 'active'])->name('browser-game.quests.active');
Route::get('/completed', [QuestsController::class, 'completed'])->name('browser-game.quests.completed');
Route::post('/{quest}/accept', [QuestsController::class, 'accept'])->name('browser-game.quests.accept');
Route::post('/{quest}/complete', [QuestsController::class, 'complete'])->name('browser-game.quests.complete');
Route::post('/{quest}/abandon', [QuestsController::class, 'abandon'])->name('browser-game.quests.abandon');
Route::get('/{quest}', [QuestsController::class, 'show'])->name('browser-game.quests.show');
Route::post('/{quest}/progress', [QuestsController::class, 'progress'])->name('browser-game.quests.progress');
```
<!-- layer-implementation-plan:end -->
