# Accounts React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-accounts-react-native
**Matching core package:** module-browser-game-accounts ([implementation](../core/accounts.md))
**Matching API package:** module-browser-game-accounts-api ([contract](../api/accounts.md))

## Implementation plan

This adapter presents Accounts for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounts.md), and [API module](../api/accounts.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounts`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-browser-game-mobile-react`](https://github.com/liberusoftware/project-browser-game-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounts.md)) |
| Capability React Native module skeleton | [`module-browser-game-accounts-react-native`](https://github.com/liberusoftware/module-browser-game-accounts-react-native) (`@liberusoftware/module-browser-game-accounts-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Player identity** | Progressive mobile list/detail/sheet flow for `player identity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sessions** | Progressive mobile list/detail/sheet flow for `sessions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Age/region policy** | Progressive mobile list/detail/sheet flow for `age/region policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bans** | Progressive mobile list/detail/sheet flow for `bans` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recovery** | Progressive mobile list/detail/sheet flow for `recovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Privacy** | Progressive mobile list/detail/sheet flow for `privacy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Account lifecycle** | Progressive mobile list/detail/sheet flow for `account lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-browser-game-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Queries/AccountsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountBan.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountBan.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountPrivacy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountPrivacy.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountRecovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountRecovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountSession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountSession.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/src/Http/Controllers/AccountsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function show(Request $request, AccountsRecord $account): JsonResponse`<br>`public function update(Request $request, AccountsRecord $account): JsonResponse`<br>`public function ageRegion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function verifyEmail(Request $request, AccountsRecord $account): JsonResponse`<br>`public function suspend(Request $request, AccountsRecord $account): JsonResponse`<br>`public function reactivate(Request $request, AccountsRecord $account): JsonResponse`<br>`public function ban(Request $request, AccountsRecord $account): JsonResponse`<br>`public function liftBan(Request $request, AccountsRecord $account, AccountBan $ban): JsonResponse`<br>`public function privacy(Request $request, AccountsRecord $account): JsonResponse`<br>`public function requestDeletion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function completeDeletion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function revokeSession(Request $request, AccountsRecord $account, AccountSession $session): JsonResponse`<br>`public function sessions(Request $request, AccountsRecord $account): JsonResponse`<br>`public function revokeAllSessions(Request $request, AccountsRecord $account): JsonResponse`<br>`public function issueRecovery(Request $request, AccountsRecord $account): JsonResponse`<br>`public function consumeRecovery(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-accounts-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/accounts')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [AccountsController::class, 'index'])->name('browser-game.accounts.index');
Route::post('/', [AccountsController::class, 'store'])->name('browser-game.accounts.store');
Route::patch('/{account}', [AccountsController::class, 'update'])->name('browser-game.accounts.update');
Route::post('/{account}/verify-email', [AccountsController::class, 'verifyEmail'])->name('browser-game.accounts.verify-email');
Route::post('/{account}/suspend', [AccountsController::class, 'suspend'])->name('browser-game.accounts.suspend');
Route::post('/{account}/reactivate', [AccountsController::class, 'reactivate'])->name('browser-game.accounts.reactivate');
Route::post('/{account}/ban', [AccountsController::class, 'ban'])->name('browser-game.accounts.ban');
Route::post('/{account}/bans/{ban}/lift', [AccountsController::class, 'liftBan'])->name('browser-game.accounts.bans.lift');
Route::post('/{account}/age-region', [AccountsController::class, 'ageRegion'])->name('browser-game.accounts.age-region');
Route::put('/{account}/privacy', [AccountsController::class, 'privacy'])->name('browser-game.accounts.privacy');
Route::post('/{account}/deletion-request', [AccountsController::class, 'requestDeletion'])->name('browser-game.accounts.deletion-request');
Route::post('/{account}/deletion-complete', [AccountsController::class, 'completeDeletion'])->name('browser-game.accounts.deletion-complete');
Route::get('/{account}/sessions', [AccountsController::class, 'sessions'])->name('browser-game.accounts.sessions');
Route::post('/{account}/recovery', [AccountsController::class, 'issueRecovery'])->name('browser-game.accounts.recovery.issue');
Route::post('/{account}/sessions/{session}/revoke', [AccountsController::class, 'revokeSession'])->name('browser-game.accounts.sessions.revoke');
Route::post('/{account}/sessions/revoke-all', [AccountsController::class, 'revokeAllSessions'])->name('browser-game.accounts.sessions.revoke-all');
Route::get('/{account}', [AccountsController::class, 'show'])->name('browser-game.accounts.show');
Route::post('api/v1/browser-game/accounts/recovery/consume', [AccountsController::class, 'consumeRecovery'])
```
<!-- layer-implementation-plan:end -->
