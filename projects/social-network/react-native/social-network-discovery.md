# Social Network Discovery React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-discovery). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-discovery-react-native
**Matching core package:** module-social-network-social-network-discovery ([implementation](../core/social-network-discovery.md))
**Matching API package:** module-social-network-social-network-discovery-api ([contract](../api/social-network-discovery.md))

## Implementation plan

This adapter presents Social Network Discovery for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Discovery API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-discovery.md), and [API module](../api/social-network-discovery.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-discovery`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-discovery.md)) |
| Capability React Native module skeleton | [`module-social-network-discovery-react-native`](https://github.com/liberusoftware/module-social-network-discovery-react-native) (`@liberusoftware/module-social-network-discovery-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Search** | Progressive mobile list/detail/sheet flow for `search` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hashtags** | Progressive mobile list/detail/sheet flow for `hashtags` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trends** | Progressive mobile list/detail/sheet flow for `trends` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recommendations** | Progressive mobile list/detail/sheet flow for `recommendations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Directories** | Progressive mobile list/detail/sheet flow for `directories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Privacy-aware indexing** | Progressive mobile list/detail/sheet flow for `privacy-aware indexing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IndexResource.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/IndexResource.php) | `public function __construct(private DiscoveryAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): DiscoveryIndex` |
| [ListTrends.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/ListTrends.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, int $limit = 20): array` |
| [SearchDiscovery.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/SearchDiscovery.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, string $query, int $limit = 25): Collection` |
| [DiscoveryAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Contracts/DiscoveryAuthorizer.php) | `public function search(Profile $viewer): void`<br>`public function index(Profile $owner): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DiscoveryIndex.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Models/DiscoveryIndex.php) | `id`, `resource_type`, `resource_id`, `owner_profile_id`, `visibility`, `body`, `terms`, `engagement_score`, `published_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DiscoveryController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-api/src/Http/Controllers/DiscoveryController.php) | `public function search(Request $request, GetProfile $get, SearchDiscovery $search): JsonResponse`<br>`public function trends(Request $request, GetProfile $get, ListTrends $trends): JsonResponse`<br>`public function index(Request $request, GetProfile $get, IndexResource $index): JsonResponse` |

**Observed route declarations:**

[modules/social-network-discovery-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/discovery')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.discovery.api.')->group(function (): void {
Route::get('/search', [DiscoveryController::class, 'search'])->name('search');
Route::get('/trends', [DiscoveryController::class, 'trends'])->name('trends');
Route::post('/index', [DiscoveryController::class, 'index'])->name('index');
```
<!-- layer-implementation-plan:end -->
