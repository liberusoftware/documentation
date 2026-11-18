# Social Network Communities React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-communities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-communities-react-native
**Matching core package:** module-social-network-social-network-communities ([implementation](../core/social-network-communities.md))
**Matching API package:** module-social-network-social-network-communities-api ([contract](../api/social-network-communities.md))

## Implementation plan

This adapter presents Social Network Communities for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Communities API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-communities.md), and [API module](../api/social-network-communities.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-communities`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-communities.md)) |
| Capability React Native module skeleton | [`module-social-network-communities-react-native`](https://github.com/liberusoftware/module-social-network-communities-react-native) (`@liberusoftware/module-social-network-communities-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Groups/pages** | Progressive mobile list/detail/sheet flow for `groups/pages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Memberships** | Progressive mobile list/detail/sheet flow for `memberships` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Roles** | Progressive mobile list/detail/sheet flow for `roles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rules** | Progressive mobile list/detail/sheet flow for `rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feeds** | Progressive mobile list/detail/sheet flow for `feeds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Files** | Progressive mobile list/detail/sheet flow for `files` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Questions** | Progressive mobile list/detail/sheet flow for `questions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Moderation** | Progressive mobile list/detail/sheet flow for `moderation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
