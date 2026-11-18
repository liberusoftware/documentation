# Module Cms Video And Audio Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-video-and-audio). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-video-and-audio-flutter
**Matching core package:** module-cms-module-cms-video-and-audio ([implementation](../core/module-cms-video-and-audio.md))
**Matching API package:** module-cms-module-cms-video-and-audio-api ([contract](../api/module-cms-video-and-audio.md))

## Implementation plan

This adapter presents Module Cms Video And Audio for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Video And Audio API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-cms-video-and-audio.md), and [API module](../api/module-cms-video-and-audio.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-cms-video-and-audio`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-video-and-audio-flutter`](https://github.com/liberusoftware/module-cms-video-and-audio-flutter) (`module_cms_video_and_audio_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-video-and-audio-dart-mobile`](https://github.com/liberusoftware/module-cms-video-and-audio-dart-mobile) (`module_cms_video_and_audio_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-video-and-audio-dart-desktop`](https://github.com/liberusoftware/module-cms-video-and-audio-dart-desktop) (`module_cms_video_and_audio_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/module-cms-video-and-audio.md) · [Core plan](../core/module-cms-video-and-audio.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Upload/remote media** | Adaptive mobile cards/sheets for `upload/remote media` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `upload/remote media` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Transcoding adapters** | Adaptive mobile cards/sheets for `transcoding adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `transcoding adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Posters** | Adaptive mobile cards/sheets for `posters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `posters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Chapters** | Adaptive mobile cards/sheets for `chapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `chapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Captions** | Adaptive mobile cards/sheets for `captions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `captions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Transcripts** | Adaptive mobile cards/sheets for `transcripts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `transcripts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Streaming** | Adaptive mobile cards/sheets for `streaming` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `streaming` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Playback metadata** | Adaptive mobile cards/sheets for `playback metadata` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `playback metadata` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
