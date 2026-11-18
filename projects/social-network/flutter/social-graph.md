# Social Graph Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-graph). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-graph-flutter
**Matching core package:** module-social-network-social-graph ([implementation](../core/social-graph.md))
**Matching API package:** module-social-network-social-graph-api ([contract](../api/social-graph.md))

## Implementation plan

This adapter presents Social Graph for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Graph API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/social-graph.md), and [API module](../api/social-graph.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `social-graph`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-social-graph-flutter`](https://github.com/liberusoftware/module-social-network-social-graph-flutter) (`module_social_network_social_graph_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-social-graph-dart-mobile`](https://github.com/liberusoftware/module-social-network-social-graph-dart-mobile) (`module_social_network_social_graph_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-social-graph-dart-desktop`](https://github.com/liberusoftware/module-social-network-social-graph-dart-desktop) (`module_social_network_social_graph_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/social-graph.md) · [Core plan](../core/social-graph.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Follow/friend models** | Adaptive mobile cards/sheets for `follow/friend models` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `follow/friend models` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Requests** | Adaptive mobile cards/sheets for `requests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `requests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Lists** | Adaptive mobile cards/sheets for `lists` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lists` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Suggestions** | Adaptive mobile cards/sheets for `suggestions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `suggestions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Blocks** | Adaptive mobile cards/sheets for `blocks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `blocks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Relationship visibility** | Adaptive mobile cards/sheets for `relationship visibility` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `relationship visibility` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AcceptFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [AddProfileToList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AddProfileToList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, GraphList $list, Profile $profile): GraphList` |
| [BlockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/BlockProfile.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $source, Profile $target): Block` |
| [CancelFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CancelFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [CreateList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, array $attributes): GraphList` |
| [CreateRelationship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateRelationship.php) | `public function __construct(private GraphAuthorizer $authorizer, private Dispatcher $events)`<br>`public function follow(Profile $source, Profile $target): Relationship`<br>`public function friend(Profile $source, Profile $target): Relationship` |
| [ListOwnedBlocks.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedBlocks.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [ListOwnedLists.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedLists.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [ListRelationships.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListRelationships.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, ?string $type = null, ?string $status = null, int $limit = 100): Collection` |
| [RejectFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/RejectFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Block.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Block.php) | `id`, `source_profile_id`, `target_profile_id` |
| [GraphList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/GraphList.php) | `id`, `owner_profile_id`, `name`, `visibility` |
| [Relationship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Relationship.php) | `id`, `source_profile_id`, `target_profile_id`, `relationship_type`, `status`, `visibility` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialGraphController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/src/Http/Controllers/SocialGraphController.php) | `public function follow(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function friend(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListRelationships $list): JsonResponse`<br>`public function suggestions(Request $request, GetProfile $get, SuggestProfiles $suggest): JsonResponse`<br>`public function block(string $profile, Request $request, GetProfile $get, BlockProfile $block): JsonResponse`<br>`public function unblock(string $profile, Request $request, GetProfile $get, UnblockProfile $unblock): JsonResponse`<br>`public function accept(Relationship $relationship, Request $request, GetProfile $get, AcceptFriendship $accept): JsonResponse`<br>`public function reject(Relationship $relationship, Request $request, GetProfile $get, RejectFriendship $reject): JsonResponse`<br>`public function cancel(Relationship $relationship, Request $request, GetProfile $get, CancelFriendship $cancel): JsonResponse`<br>`public function visibility(Relationship $relationship, Request $request, GetProfile $get, UpdateRelationshipVisibility $update): JsonResponse`<br>`public function lists(Request $request, GetProfile $get, ListOwnedLists $lists): JsonResponse`<br>`public function createList(Request $request, GetProfile $get, CreateList $create): JsonResponse`<br>`public function addListMember(GraphList $list, string $profile, Request $request, GetProfile $get, AddProfileToList $add): JsonResponse`<br>`public function removeListMember(GraphList $list, string $profile, Request $request, GetProfile $get, RemoveProfileFromList $remove): JsonResponse` |

**Observed route declarations:**

[modules/social-network-social-graph-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/social-graph')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.social-graph.api.')->group(function (): void {
Route::post('/me/following/{profile}', [SocialGraphController::class, 'follow'])->name('follow');
Route::post('/me/friend-requests/{profile}', [SocialGraphController::class, 'friend'])->name('friend');
Route::get('/me/relationships', [SocialGraphController::class, 'index'])->name('index');
Route::get('/me/suggestions', [SocialGraphController::class, 'suggestions'])->name('suggestions');
Route::put('/me/blocks/{profile}', [SocialGraphController::class, 'block'])->name('block');
Route::delete('/me/blocks/{profile}', [SocialGraphController::class, 'unblock'])->name('unblock');
Route::post('/me/relationships/{relationship}/accept', [SocialGraphController::class, 'accept'])->name('accept');
Route::post('/me/relationships/{relationship}/reject', [SocialGraphController::class, 'reject'])->name('reject');
Route::post('/me/relationships/{relationship}/cancel', [SocialGraphController::class, 'cancel'])->name('cancel');
Route::patch('/me/relationships/{relationship}/visibility', [SocialGraphController::class, 'visibility'])->name('visibility');
Route::get('/me/lists', [SocialGraphController::class, 'lists'])->name('lists');
Route::post('/me/lists', [SocialGraphController::class, 'createList'])->name('lists.create');
Route::put('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'addListMember'])->name('lists.profiles.add');
Route::delete('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'removeListMember'])->name('lists.profiles.remove');
```
<!-- layer-implementation-plan:end -->
