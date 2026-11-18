# Social Network Engagement Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-engagement-flutter
**Matching core package:** module-social-network-social-network-engagement ([implementation](../core/social-network-engagement.md))
**Matching API package:** module-social-network-social-network-engagement-api ([contract](../api/social-network-engagement.md))

## Implementation plan

This adapter presents Social Network Engagement for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Engagement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/social-network-engagement.md), and [API module](../api/social-network-engagement.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `social-network-engagement`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-engagement-flutter`](https://github.com/liberusoftware/module-social-network-engagement-flutter) (`module_social_network_engagement_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-engagement-dart-mobile`](https://github.com/liberusoftware/module-social-network-engagement-dart-mobile) (`module_social_network_engagement_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-engagement-dart-desktop`](https://github.com/liberusoftware/module-social-network-engagement-dart-desktop) (`module_social_network_engagement_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/social-network-engagement.md) · [Core plan](../core/social-network-engagement.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Reactions** | Adaptive mobile cards/sheets for `reactions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reactions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Comments** | Adaptive mobile cards/sheets for `comments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `comments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Replies** | Adaptive mobile cards/sheets for `replies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `replies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sharing** | Adaptive mobile cards/sheets for `sharing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sharing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bookmarks** | Adaptive mobile cards/sheets for `bookmarks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bookmarks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Counters** | Adaptive mobile cards/sheets for `counters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `counters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Abuse limits** | Adaptive mobile cards/sheets for `abuse limits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `abuse limits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/CreateEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $actor, array $attributes): Engagement` |
| [DeleteEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/DeleteEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer)`<br>`public function handle(Profile $actor, Engagement $engagement): void` |
| [ListEngagements.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/ListEngagements.php) | `public function handle(string $targetType, string $targetId, ?string $kind = null, int $limit = 50): Collection`<br>`public function count(string $targetType, string $targetId, ?string $kind = null): int` |
| [UpdateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/UpdateEngagement.php) | `public function handle(Profile $actor, Engagement $engagement, string $body): Engagement` |
| [EngagementAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Contracts/EngagementAuthorizer.php) | `public function create(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Engagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Models/Engagement.php) | `id`, `actor_profile_id`, `target_type`, `target_id`, `kind`, `reaction_type`, `body` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/src/Http/Controllers/EngagementController.php) | `public function store(Request $request, GetProfile $get, CreateEngagement $create): JsonResponse`<br>`public function destroy(string $engagement, Request $request, GetProfile $get, DeleteEngagement $delete): JsonResponse`<br>`public function index(string $targetType, string $targetId, Request $request, ListEngagements $list): JsonResponse`<br>`public function update(string $engagement, Request $request, GetProfile $get, UpdateEngagement $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-engagement-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/engagement')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.engagement.api.')->group(function (): void {
Route::post('/', [EngagementController::class, 'store'])->name('store');
Route::get('/target/{targetType}/{targetId}', [EngagementController::class, 'index'])->name('index');
Route::patch('/{engagement}', [EngagementController::class, 'update'])->name('update');
Route::delete('/{engagement}', [EngagementController::class, 'destroy'])->name('destroy');
```
<!-- layer-implementation-plan:end -->
