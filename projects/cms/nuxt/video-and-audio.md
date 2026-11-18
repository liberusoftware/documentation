# CMS: Video and Audio Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video-and-audio). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-video-and-audio-nuxt`
**Matching domain module:** `cms-video-and-audio`
**Application:** CMS
**Source feature:** [Video and Audio](../features/video-and-audio.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/video-and-audio.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-video-and-audio` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Upload/remote media:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transcoding adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Posters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Chapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Captions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transcripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Streaming:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Playback metadata:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-video-and-audio-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `upload-remote-media`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transcoding-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `posters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `chapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `captions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transcripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `streaming`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `playback-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `cms-video-and-audio` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/video-and-audio.md)) |
| Capability Nuxt module skeleton | [`module-cms-video-and-audio-nuxt`](https://github.com/liberusoftware/module-cms-video-and-audio-nuxt) (`@liberusoftware/module-cms-video-and-audio-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Upload/remote media** | Expose composable and Vue 3 component for `upload/remote media` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Transcoding adapters** | Expose composable and Vue 3 component for `transcoding adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Posters** | Expose composable and Vue 3 component for `posters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Chapters** | Expose composable and Vue 3 component for `chapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Captions** | Expose composable and Vue 3 component for `captions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Transcripts** | Expose composable and Vue 3 component for `transcripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Streaming** | Expose composable and Vue 3 component for `streaming` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Playback metadata** | Expose composable and Vue 3 component for `playback metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video-and-audio.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

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
