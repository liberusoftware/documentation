# Competition React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#competition). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-competition-react-native
**Matching core package:** module-browser-game-competition ([implementation](../core/competition.md))
**Matching API package:** module-browser-game-competition-api ([contract](../api/competition.md))

## Implementation plan

This adapter presents Competition for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Competition API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/competition.md), and [API module](../api/competition.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `competition`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/competition.md)) |
| Capability React Native module skeleton | [`module-browser-game-competition-react-native`](https://github.com/liberusoftware/module-browser-game-competition-react-native) (`@liberusoftware/module-browser-game-competition-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **PvP modes** | Progressive mobile list/detail/sheet flow for `pvp modes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Matchmaking** | Progressive mobile list/detail/sheet flow for `matchmaking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Seasons** | Progressive mobile list/detail/sheet flow for `seasons` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rankings** | Progressive mobile list/detail/sheet flow for `rankings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Leaderboards** | Progressive mobile list/detail/sheet flow for `leaderboards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rewards** | Progressive mobile list/detail/sheet flow for `rewards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Anti-collusion** | Progressive mobile list/detail/sheet flow for `anti-collusion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CompetitionQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Queries/CompetitionQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CompetitionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionFlag.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionMatch.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionMatch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionReward.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionReward.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CompetitionController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-api/src/Http/Controllers/CompetitionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function queue(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function match(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function resolve(Request $request, CompetitionMatch $match): JsonResponse`<br>`public function leaderboard(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function rewards(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function claimReward(Request $request, CompetitionReward $reward): JsonResponse`<br>`public function flag(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function show(Request $request, CompetitionRecord $competition): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-competition-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/competition')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CompetitionController::class, 'index'])->name('browser-game.competition.index');
Route::post('/', [CompetitionController::class, 'store'])->name('browser-game.competition.store');
Route::post('/{competition}/queue', [CompetitionController::class, 'queue'])->name('browser-game.competition.queue');
Route::post('/{competition}/matches', [CompetitionController::class, 'match'])->name('browser-game.competition.match');
Route::get('/{competition}/leaderboard', [CompetitionController::class, 'leaderboard'])->name('browser-game.competition.leaderboard');
Route::get('/{competition}/rewards', [CompetitionController::class, 'rewards'])->name('browser-game.competition.rewards');
Route::post('/{competition}/flags', [CompetitionController::class, 'flag'])->name('browser-game.competition.flag');
Route::post('/rewards/{reward}/claim', [CompetitionController::class, 'claimReward'])->name('browser-game.competition.reward.claim');
Route::post('/matches/{match}/resolve', [CompetitionController::class, 'resolve'])->name('browser-game.competition.resolve');
Route::get('/{competition}', [CompetitionController::class, 'show'])->name('browser-game.competition.show');
```
<!-- layer-implementation-plan:end -->
