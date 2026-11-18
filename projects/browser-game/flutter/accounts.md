# Accounts Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-accounts-flutter
**Matching core package:** module-browser-game-accounts ([implementation](../core/accounts.md))
**Matching API package:** module-browser-game-accounts-api ([contract](../api/accounts.md))

## Implementation plan

This adapter presents Accounts for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounts.md), and [API module](../api/accounts.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounts`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-browser-game-accounts-flutter`](https://github.com/liberusoftware/module-browser-game-accounts-flutter) (`module_browser_game_accounts_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-browser-game-accounts-dart-mobile`](https://github.com/liberusoftware/module-browser-game-accounts-dart-mobile) (`module_browser_game_accounts_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-browser-game-accounts-dart-desktop`](https://github.com/liberusoftware/module-browser-game-accounts-dart-desktop) (`module_browser_game_accounts_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/accounts.md) · [Core plan](../core/accounts.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Player identity** | Adaptive mobile cards/sheets for `player identity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `player identity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sessions** | Adaptive mobile cards/sheets for `sessions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sessions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Age/region policy** | Adaptive mobile cards/sheets for `age/region policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `age/region policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bans** | Adaptive mobile cards/sheets for `bans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recovery** | Adaptive mobile cards/sheets for `recovery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recovery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Privacy** | Adaptive mobile cards/sheets for `privacy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `privacy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Account lifecycle** | Adaptive mobile cards/sheets for `account lifecycle` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `account lifecycle` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
