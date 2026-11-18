# Live Ops Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#live-ops). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-browser-game-live-ops-flutter
**Matching core package:** module-browser-game-live-ops ([implementation](../core/live-ops.md))
**Matching API package:** module-browser-game-live-ops-api ([contract](../api/live-ops.md))

## Implementation plan

This adapter presents Live Ops for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Live Ops API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/live-ops.md), and [API module](../api/live-ops.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `live-ops`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-browser-game-mobile-flutter`](https://github.com/liberusoftware/project-browser-game-mobile-flutter) | [`module-browser-game-live-ops-flutter`](https://github.com/liberusoftware/module-browser-game-live-ops-flutter) (`module_browser_game_live_ops_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-browser-game-dart-mobile`](https://github.com/liberusoftware/project-browser-game-dart-mobile) | [`module-browser-game-live-ops-dart-mobile`](https://github.com/liberusoftware/module-browser-game-live-ops-dart-mobile) (`module_browser_game_live_ops_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-browser-game-dart-desktop`](https://github.com/liberusoftware/project-browser-game-dart-desktop) | [`module-browser-game-live-ops-dart-desktop`](https://github.com/liberusoftware/module-browser-game-live-ops-dart-desktop) (`module_browser_game_live_ops_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [API plan](../api/live-ops.md) · [Core plan](../core/live-ops.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Daily activities** | Adaptive mobile cards/sheets for `daily activities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `daily activities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Events** | Adaptive mobile cards/sheets for `events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Seasons** | Adaptive mobile cards/sheets for `seasons` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `seasons` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Content schedules** | Adaptive mobile cards/sheets for `content schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `content schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Announcements** | Adaptive mobile cards/sheets for `announcements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `announcements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Grants** | Adaptive mobile cards/sheets for `grants` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `grants` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rollback** | Adaptive mobile cards/sheets for `rollback` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rollback` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-browser-game-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LiveOpsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Queries/LiveOpsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LiveOpsClaim.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsClaim.php) | No literal fillable array detected; inspect the model and API schema. |
| [LiveOpsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [LiveOpsRollback.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsRollback.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LiveOpsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops-api/src/Http/Controllers/LiveOpsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function publish(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function claim(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function dailyStatus(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function dailyClaim(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function rollback(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function show(Request $request, LiveOpsRecord $liveOps): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-live-ops-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/live-ops')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [LiveOpsController::class, 'index'])->name('browser-game.live-ops.index');
Route::post('/', [LiveOpsController::class, 'store'])->name('browser-game.live-ops.store');
Route::post('/{liveOps}/publish', [LiveOpsController::class, 'publish'])->name('browser-game.live-ops.publish');
Route::post('/{liveOps}/claim', [LiveOpsController::class, 'claim'])->name('browser-game.live-ops.claim');
Route::get('/daily/{liveOps}/status', [LiveOpsController::class, 'dailyStatus'])->name('browser-game.live-ops.daily.status');
Route::post('/daily/{liveOps}/claim', [LiveOpsController::class, 'dailyClaim'])->name('browser-game.live-ops.daily.claim');
Route::post('/{liveOps}/rollback', [LiveOpsController::class, 'rollback'])->name('browser-game.live-ops.rollback');
Route::get('/{liveOps}', [LiveOpsController::class, 'show'])->name('browser-game.live-ops.show');
```
<!-- layer-implementation-plan:end -->
