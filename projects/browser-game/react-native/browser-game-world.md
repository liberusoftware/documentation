# Browser Game World React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-world). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-world-react-native
**Matching core package:** module-browser-game-browser-game-world ([implementation](../core/browser-game-world.md))
**Matching API package:** module-browser-game-browser-game-world-api ([contract](../api/browser-game-world.md))

## Implementation plan

This adapter presents Browser Game World for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game World API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/browser-game-world.md), and [API module](../api/browser-game-world.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `browser-game-world`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-world.md)) |
| Capability React Native module skeleton | [`module-browser-game-world-react-native`](https://github.com/liberusoftware/module-browser-game-world-react-native) (`@liberusoftware/module-browser-game-world-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Regions** | Progressive mobile list/detail/sheet flow for `regions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locations** | Progressive mobile list/detail/sheet flow for `locations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Maps** | Progressive mobile list/detail/sheet flow for `maps` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Travel** | Progressive mobile list/detail/sheet flow for `travel` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Encounters** | Progressive mobile list/detail/sheet flow for `encounters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **NPCs** | Progressive mobile list/detail/sheet flow for `npcs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Resources** | Progressive mobile list/detail/sheet flow for `resources` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Weather** | Progressive mobile list/detail/sheet flow for `weather` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Unlocks** | Progressive mobile list/detail/sheet flow for `unlocks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorldQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Queries/WorldQuery.php) | `public function visible(?string $tenantId, ?string $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WorldPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Policies/WorldPolicy.php) | `public function view(?string $tenantId, ?string $teamId, WorldEntity $entity): bool`<br>`public function manage(?string $actorId, ?string $tenantId, ?string $teamId, WorldEntity $entity): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldEntity.php) | `tenant_id`, `team_id`, `world_id`, `kind`, `name`, `slug`, `status`, `attributes`, `coordinates`, `unlock_key` |
| [WorldTravel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldTravel.php) | `tenant_id`, `team_id`, `actor_id`, `origin_id`, `destination_id`, `idempotency_key`, `metadata` |
| [WorldUnlock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldUnlock.php) | `tenant_id`, `team_id`, `actor_id`, `entity_id`, `unlock_key`, `status`, `metadata`, `idempotency_key`, `granted_at`, `revoked_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorldController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/src/Http/Controllers/WorldController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function travel(Request $request): JsonResponse`<br>`public function unlock(Request $request, WorldEntity $entity): JsonResponse`<br>`public function revokeUnlock(Request $request, WorldUnlock $unlock): JsonResponse`<br>`public function show(Request $request, WorldEntity $entity): JsonResponse`<br>`public function update(Request $request, WorldEntity $entity): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-world-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/world')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [WorldController::class, 'index'])->name('browser-game.world.index');
Route::post('/', [WorldController::class, 'store'])->name('browser-game.world.store');
Route::post('/travel', [WorldController::class, 'travel'])->name('browser-game.world.travel');
Route::post('/{entity}/unlock', [WorldController::class, 'unlock'])->name('browser-game.world.unlock');
Route::delete('/unlocks/{unlock}', [WorldController::class, 'revokeUnlock'])->name('browser-game.world.unlock.revoke');
Route::patch('/{entity}', [WorldController::class, 'update'])->name('browser-game.world.update');
Route::get('/{entity}', [WorldController::class, 'show'])->name('browser-game.world.show');
```
<!-- layer-implementation-plan:end -->
