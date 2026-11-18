# Competition Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#competition). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-competition-flutter
**Matching core package:** module-browser-game-competition ([implementation](../core/competition.md))
**Matching API package:** module-browser-game-competition-api ([contract](../api/competition.md))

## Implementation plan

This adapter presents Competition for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Competition API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/competition.md), and [API module](../api/competition.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `competition`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-browser-game-competition-flutter`](https://github.com/liberusoftware/module-browser-game-competition-flutter) (`module_browser_game_competition_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-browser-game-competition-dart-mobile`](https://github.com/liberusoftware/module-browser-game-competition-dart-mobile) (`module_browser_game_competition_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-browser-game-competition-dart-desktop`](https://github.com/liberusoftware/module-browser-game-competition-dart-desktop) (`module_browser_game_competition_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/competition.md) · [Core plan](../core/competition.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **PvP modes** | Adaptive mobile cards/sheets for `pvp modes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pvp modes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Matchmaking** | Adaptive mobile cards/sheets for `matchmaking` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `matchmaking` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Seasons** | Adaptive mobile cards/sheets for `seasons` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `seasons` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rankings** | Adaptive mobile cards/sheets for `rankings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rankings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Leaderboards** | Adaptive mobile cards/sheets for `leaderboards` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `leaderboards` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rewards** | Adaptive mobile cards/sheets for `rewards` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rewards` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Anti-collusion** | Adaptive mobile cards/sheets for `anti-collusion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `anti-collusion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
