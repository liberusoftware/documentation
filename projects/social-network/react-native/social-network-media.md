# Social Network Media React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-media). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-media-react-native
**Matching core package:** module-social-network-social-network-media ([implementation](../core/social-network-media.md))
**Matching API package:** module-social-network-social-network-media-api ([contract](../api/social-network-media.md))

## Implementation plan

This adapter presents Social Network Media for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Media API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-media.md), and [API module](../api/social-network-media.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-media`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-media.md)) |
| Capability React Native module skeleton | [`module-social-network-media-react-native`](https://github.com/liberusoftware/module-social-network-media-react-native) (`@liberusoftware/module-social-network-media-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Images** | Progressive mobile list/detail/sheet flow for `images` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Video** | Progressive mobile list/detail/sheet flow for `video` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audio** | Progressive mobile list/detail/sheet flow for `audio` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Files** | Progressive mobile list/detail/sheet flow for `files` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Processing** | Progressive mobile list/detail/sheet flow for `processing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Alt text** | Progressive mobile list/detail/sheet flow for `alt text` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Captions** | Progressive mobile list/detail/sheet flow for `captions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rights** | Progressive mobile list/detail/sheet flow for `rights` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/CreateAlbum.php) | `public function handle(Profile $owner, array $attributes): Album` |
| [DeleteAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteAlbum.php) | `public function handle(Profile $owner, Album $album): void` |
| [DeleteMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteMediaAsset.php) | `public function handle(Profile $owner, MediaAsset $asset): void` |
| [MarkMediaReady.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/MarkMediaReady.php) | `public function handle(Profile $owner, MediaAsset $asset): MediaAsset` |
| [RegisterMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/RegisterMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): MediaAsset` |
| [UpdateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateAlbum.php) | `public function handle(Profile $owner, Album $album, array $attributes): Album` |
| [UpdateMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer)`<br>`public function handle(Profile $owner, MediaAsset $asset, array $attributes): MediaAsset` |
| [MediaAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Contracts/MediaAuthorizer.php) | `public function upload(Profile $owner): void`<br>`public function update(Profile $owner): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Album.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/Album.php) | `id`, `owner_profile_id`, `name`, `description`, `privacy`, `cover_path` |
| [MediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/MediaAsset.php) | `id`, `owner_profile_id`, `album_id`, `type`, `state`, `disk`, `path`, `mime_type`, `size`, `checksum`, `alt_text`, `captions`, `rights`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MediaController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-api/src/Http/Controllers/MediaController.php) | `public function store(Request $request, GetProfile $get, RegisterMediaAsset $register): JsonResponse`<br>`public function index(Request $request, GetProfile $get): JsonResponse`<br>`public function show(string $asset, Request $request, GetProfile $get): JsonResponse`<br>`public function update(string $asset, Request $request, GetProfile $get, UpdateMediaAsset $update): JsonResponse`<br>`public function ready(string $asset, Request $request, GetProfile $get, MarkMediaReady $ready): JsonResponse`<br>`public function destroy(string $asset, Request $request, GetProfile $get, DeleteMediaAsset $delete): JsonResponse`<br>`public function albums(Request $request, GetProfile $get): JsonResponse`<br>`public function storeAlbum(Request $request, GetProfile $get, CreateAlbum $create): JsonResponse`<br>`public function showAlbum(string $album, Request $request, GetProfile $get): JsonResponse`<br>`public function updateAlbum(string $album, Request $request, GetProfile $get, UpdateAlbum $update): JsonResponse`<br>`public function destroyAlbum(string $album, Request $request, GetProfile $get, DeleteAlbum $delete): JsonResponse` |

**Observed route declarations:**

[modules/social-network-media-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/media')->middleware(['auth:sanctum', 'throttle:30,1'])->name('social-network.media.api.')->group(function (): void {
Route::get('/', [MediaController::class, 'index'])->name('index');
Route::get('/albums', [MediaController::class, 'albums'])->name('albums.index');
Route::post('/albums', [MediaController::class, 'storeAlbum'])->name('albums.store');
Route::get('/albums/{album}', [MediaController::class, 'showAlbum'])->name('albums.show');
Route::patch('/albums/{album}', [MediaController::class, 'updateAlbum'])->name('albums.update');
Route::delete('/albums/{album}', [MediaController::class, 'destroyAlbum'])->name('albums.destroy');
Route::post('/', [MediaController::class, 'store'])->name('store');
Route::post('/{asset}/ready', [MediaController::class, 'ready'])->name('ready');
Route::get('/{asset}', [MediaController::class, 'show'])->name('show');
Route::patch('/{asset}', [MediaController::class, 'update'])->name('update');
Route::delete('/{asset}', [MediaController::class, 'destroy'])->name('destroy');
```
<!-- layer-implementation-plan:end -->
