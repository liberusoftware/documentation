# CMS: Video and Audio Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video-and-audio). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-cms-video-and-audio-vue-inertia`
**Matching domain module:** `cms-video-and-audio`
**Application:** CMS
**Source feature:** [Video and Audio](../features/video-and-audio.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/video-and-audio.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Upload/remote media:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transcoding adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Posters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Chapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Captions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transcripts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Streaming:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Playback metadata:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-cms-video-and-audio-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `upload-remote-media`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `transcoding-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `posters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `chapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `captions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `transcripts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `streaming`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `playback-metadata`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `cms-video-and-audio` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-cms-laravel-inertia-vue`](https://github.com/liberusoftware/project-cms-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-cms-video-and-audio-vue-inertia`](https://github.com/liberusoftware/module-cms-video-and-audio-vue-inertia) (`@liberusoftware/module-cms-video-and-audio-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/video-and-audio.md) · [Core plan](../core/video-and-audio.md) · [API plan](../api/video-and-audio.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Upload/remote media** | Render `upload/remote media` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Transcoding adapters** | Render `transcoding adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Posters** | Render `posters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Chapters** | Render `chapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Captions** | Render `captions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Transcripts** | Render `transcripts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Streaming** | Render `streaming` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Playback metadata** | Render `playback metadata` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
