# Browser Game Quests Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-quests). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-browser-game-quests-flutter
**Matching core package:** module-browser-game-browser-game-quests ([implementation](../core/browser-game-quests.md))
**Matching API package:** module-browser-game-browser-game-quests-api ([contract](../api/browser-game-quests.md))

## Implementation plan

This adapter presents Browser Game Quests for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Browser Game Quests API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/browser-game-quests.md), and [API module](../api/browser-game-quests.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `browser-game-quests`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-browser-game-quests-flutter`](https://github.com/liberusoftware/module-browser-game-quests-flutter) (`module_browser_game_quests_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-browser-game-quests-dart-mobile`](https://github.com/liberusoftware/module-browser-game-quests-dart-mobile) (`module_browser_game_quests_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-browser-game-quests-dart-desktop`](https://github.com/liberusoftware/module-browser-game-quests-dart-desktop) (`module_browser_game_quests_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/browser-game-quests.md) · [Core plan](../core/browser-game-quests.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Storylines** | Adaptive mobile cards/sheets for `storylines` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `storylines` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Objectives** | Adaptive mobile cards/sheets for `objectives` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `objectives` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Prerequisites** | Adaptive mobile cards/sheets for `prerequisites` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `prerequisites` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branching** | Adaptive mobile cards/sheets for `branching` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branching` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dialogue** | Adaptive mobile cards/sheets for `dialogue` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dialogue` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rewards** | Adaptive mobile cards/sheets for `rewards` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rewards` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Repeatability** | Adaptive mobile cards/sheets for `repeatability` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `repeatability` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Progress** | Adaptive mobile cards/sheets for `progress` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `progress` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
