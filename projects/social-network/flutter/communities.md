# Communities Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-communities-flutter
**Matching core package:** module-social-network-communities ([implementation](../core/communities.md))
**Matching API package:** module-social-network-communities-api ([contract](../api/communities.md))

## Implementation plan

This adapter presents Communities for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Communities API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/communities.md), and [API module](../api/communities.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `communities`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-communities-flutter`](https://github.com/liberusoftware/module-social-network-communities-flutter) (`module_social_network_communities_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-communities-dart-mobile`](https://github.com/liberusoftware/module-social-network-communities-dart-mobile) (`module_social_network_communities_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-communities-dart-desktop`](https://github.com/liberusoftware/module-social-network-communities-dart-desktop) (`module_social_network_communities_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/communities.md) · [Core plan](../core/communities.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Groups/pages** | Adaptive mobile cards/sheets for `groups/pages` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `groups/pages` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Memberships** | Adaptive mobile cards/sheets for `memberships` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `memberships` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Roles** | Adaptive mobile cards/sheets for `roles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `roles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rules** | Adaptive mobile cards/sheets for `rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Feeds** | Adaptive mobile cards/sheets for `feeds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `feeds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Files** | Adaptive mobile cards/sheets for `files` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `files` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Questions** | Adaptive mobile cards/sheets for `questions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `questions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Moderation** | Adaptive mobile cards/sheets for `moderation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `moderation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/CreateCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): Community` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/JoinCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer)`<br>`public function handle(Profile $member, Community $community): Membership` |
| [LeaveCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/LeaveCommunity.php) | `public function handle(Profile $member, Community $community): void` |
| [ListCommunities.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/ListCommunities.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [CommunityAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Contracts/CommunityAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function join(Profile $member): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Community.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Community.php) | `id`, `owner_profile_id`, `name`, `slug`, `description`, `visibility`, `rules` |
| [Membership.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Membership.php) | `community_id`, `profile_id`, `role`, `status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunitiesController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-api/src/Http/Controllers/CommunitiesController.php) | `public function store(Request $request, GetProfile $get, CreateCommunity $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListCommunities $list): JsonResponse`<br>`public function join(string $community, Request $request, GetProfile $get, JoinCommunity $join): JsonResponse`<br>`public function leave(string $community, Request $request, GetProfile $get, LeaveCommunity $leave): JsonResponse` |

**Observed route declarations:**

[modules/social-network-communities-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/communities')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.communities.api.')->group(function (): void {
Route::get('/', [CommunitiesController::class, 'index'])->name('index');
Route::post('/', [CommunitiesController::class, 'store'])->name('store');
Route::post('/{community}/join', [CommunitiesController::class, 'join'])->name('join');
Route::delete('/{community}/leave', [CommunitiesController::class, 'leave'])->name('leave');
```
<!-- layer-implementation-plan:end -->
