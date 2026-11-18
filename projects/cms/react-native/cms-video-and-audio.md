# Cms Video And Audio React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-video-and-audio). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-video-and-audio-react-native
**Matching core package:** module-cms-cms-video-and-audio ([implementation](../core/cms-video-and-audio.md))
**Matching API package:** module-cms-cms-video-and-audio-api ([contract](../api/cms-video-and-audio.md))

## Implementation plan

This adapter presents Cms Video And Audio for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Video And Audio API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-video-and-audio.md), and [API module](../api/cms-video-and-audio.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-video-and-audio`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-video-and-audio.md)) |
| Capability React Native module skeleton | [`module-cms-video-and-audio-react-native`](https://github.com/liberusoftware/module-cms-video-and-audio-react-native) (`@liberusoftware/module-cms-video-and-audio-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Upload/remote media** | Progressive mobile list/detail/sheet flow for `upload/remote media` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transcoding adapters** | Progressive mobile list/detail/sheet flow for `transcoding adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Posters** | Progressive mobile list/detail/sheet flow for `posters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Chapters** | Progressive mobile list/detail/sheet flow for `chapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Captions** | Progressive mobile list/detail/sheet flow for `captions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transcripts** | Progressive mobile list/detail/sheet flow for `transcripts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Streaming** | Progressive mobile list/detail/sheet flow for `streaming` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Playback metadata** | Progressive mobile list/detail/sheet flow for `playback metadata` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MediaAssetQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Queries/MediaAssetQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $kind = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?MediaAsset` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MediaManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Actions/MediaManagementService.php) | `public function __construct(private TranscodingAdapterRegistry $adapters)`<br>`public function createAsset(array $attributes): MediaAsset`<br>`public function addTrack(MediaAsset $asset, array $attributes): MediaTrack`<br>`public function updateTrack(MediaTrack $track, array $attributes): MediaTrack`<br>`public function deleteTrack(MediaTrack $track): void`<br>`public function updateAsset(MediaAsset $asset, array $attributes): MediaAsset`<br>`public function archive(MediaAsset $asset): MediaAsset`<br>`public function transcode(MediaAsset $asset, string $adapter, string $profile, string $idempotencyKey, array $context = []): MediaVariant`<br>`public function playback(MediaAsset $asset): PlaybackMetadata` |
| [TranscodingAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Contracts/TranscodingAdapterInterface.php) | `public function key(): string`<br>`public function transcode(string $sourceUri, string $profile, array $context = []): TranscodeResult` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MediaAsset.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Models/MediaAsset.php) | `public_id`, `title`, `kind`, `source_type`, `source_uri`, `mime_type`, `bytes`, `duration_seconds`, `stream_uri`, `poster_uri`, `status`, `metadata`, `checksum`, `team_id` |
| [MediaTrack.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Models/MediaTrack.php) | `asset_id`, `track_type`, `language`, `label`, `uri`, `content`, `start_seconds`, `end_seconds`, `metadata`, `status`, `team_id` |
| [MediaVariant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-video-and-audio/src/Models/MediaVariant.php) | `asset_id`, `idempotency_key`, `adapter`, `profile`, `uri`, `status`, `bytes`, `metadata`, `failure_reason`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [VideoAndAudioController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-video-and-audio-api/src/Http/Controllers/VideoAndAudioController.php) | `public function __construct(private MediaAssetQuery $assets, private MediaManagementService $service)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $publicId): MediaAssetResource`<br>`public function create(Request $request): MediaAssetResource`<br>`public function update(Request $request, string $publicId): MediaAssetResource`<br>`public function archive(string $publicId): MediaAssetResource`<br>`public function track(Request $request, string $publicId): MediaTrackResource`<br>`public function updateTrack(Request $request, int $track): MediaTrackResource`<br>`public function deleteTrack(int $track): JsonResponse`<br>`public function playback(string $publicId): JsonResponse`<br>`public function transcode(Request $request, string $publicId): JsonResponse` |
<!-- layer-implementation-plan:end -->
