# Genealogy: Media Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#media). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-media-nuxt`
**Matching domain module:** `genealogy-media`
**Application:** Genealogy
**Source feature:** [Media](../features/media.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/media.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-media` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Documents:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Photographs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audio/video:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transcription:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rights:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preservation metadata:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-media-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `photographs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audio-video`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transcription`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rights`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preservation-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-media` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/media.md)) |
| Capability Nuxt module skeleton | [`module-genealogy-media-nuxt`](https://github.com/liberusoftware/module-genealogy-media-nuxt) (`@liberusoftware/module-genealogy-media-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Documents** | Expose composable and Vue 3 component for `documents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Photographs** | Expose composable and Vue 3 component for `photographs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Audio/video** | Expose composable and Vue 3 component for `audio/video` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Transcription** | Expose composable and Vue 3 component for `transcription` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Rights** | Expose composable and Vue 3 component for `rights` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Links** | Expose composable and Vue 3 component for `links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Preservation metadata** | Expose composable and Vue 3 component for `preservation metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MediaLibrary.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Queries/MediaLibrary.php) | `public function execute(?string $kind = null, ?string $term = null, bool $publicOnly = false, int $limit = 50): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AnalyzeMediaFaces.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/AnalyzeMediaFaces.php) | `public function __construct(private readonly ?FaceRecognitionProvider $provider = null)`<br>`public function execute(MediaAsset $asset): array` |
| [CorrectMediaTranscription.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CorrectMediaTranscription.php) | `public function execute(MediaAsset $asset, string $correctedText, ?string $actorId = null): MediaTranscriptionCorrection` |
| [CreateMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaAsset.php) | `public function execute(array $attributes): MediaAsset`<br>`public function validate(array $values): void` |
| [CreateMediaLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaLink.php) | `public function execute(array $attributes): MediaLink` |
| [DeleteMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/DeleteMediaAsset.php) | `public function execute(MediaAsset $asset): void` |
| [ReviewMediaFaceTag.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/ReviewMediaFaceTag.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(MediaFaceTag $tag, string $status, ?string $personId = null, ?string $actorId = null): MediaFaceTag` |
| [StoreMediaUpload.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/StoreMediaUpload.php) | `public function execute(UploadedFile $file, array $attributes = []): MediaAsset` |
| [TranscribeMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/TranscribeMediaAsset.php) | `public function __construct(private readonly ?TranscriptionProvider $provider = null)`<br>`public function execute(MediaAsset $asset): array` |
| [UpdateMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/UpdateMediaAsset.php) | `public function execute(MediaAsset $asset, array $attributes): MediaAsset` |
| [FaceRecognitionProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Contracts/FaceRecognitionProvider.php) | `public function isAvailable(): bool`<br>`public function detect(string $absolutePath): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaAsset.php) | `team_id`, `kind`, `name`, `storage_disk`, `storage_path`, `mime_type`, `byte_size`, `checksum`, `captured_at`, `captured_place_id`, `transcription`, `transcription_status`, `transcription_language`, `rights_holder`, `rights_status`, `license_url`, `rights_expires_at`, `is_public`, `preservation_metadata`, `status`, `metadata` |
| [MediaFaceTag.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaFaceTag.php) | `team_id`, `media_asset_id`, `person_id`, `confidence`, `bounding_box`, `status`, `confirmed_by`, `confirmed_at`, `metadata` |
| [MediaLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaLink.php) | `team_id`, `media_asset_id`, `linkable_type`, `linkable_id`, `role`, `metadata` |
| [MediaTranscriptionCorrection.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaTranscriptionCorrection.php) | `team_id`, `media_asset_id`, `original_text`, `corrected_text`, `actor_id`, `metadata` |
<!-- layer-implementation-plan:end -->
