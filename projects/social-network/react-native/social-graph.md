# Social Graph React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-graph). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-graph-react-native
**Matching core package:** module-social-network-social-graph ([implementation](../core/social-graph.md))
**Matching API package:** module-social-network-social-graph-api ([contract](../api/social-graph.md))

## Implementation plan

This adapter presents Social Graph for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Graph API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-graph.md), and [API module](../api/social-graph.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-graph`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-graph.md)) |
| Capability React Native module skeleton | [`module-social-network-social-graph-react-native`](https://github.com/liberusoftware/module-social-network-social-graph-react-native) (`@liberusoftware/module-social-network-social-graph-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Follow/friend models** | Progressive mobile list/detail/sheet flow for `follow/friend models` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Requests** | Progressive mobile list/detail/sheet flow for `requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lists** | Progressive mobile list/detail/sheet flow for `lists` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suggestions** | Progressive mobile list/detail/sheet flow for `suggestions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Blocks** | Progressive mobile list/detail/sheet flow for `blocks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationship visibility** | Progressive mobile list/detail/sheet flow for `relationship visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
