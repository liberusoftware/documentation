# Media: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-genealogy-media`.

**Proposed design identifier:** `module-genealogy-media-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/media.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-genealogy-media](../../../modules/source/liberusoftware--module-genealogy-media.md) |
| API | [liberusoftware/module-genealogy-media-api](../../../modules/source/liberusoftware--module-genealogy-media-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Documents | A focused authorized view or workflow section for documents; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Photographs | A focused authorized view or workflow section for photographs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Audio/video | A focused authorized view or workflow section for audio/video; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Transcription | A focused authorized view or workflow section for transcription; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rights | A focused authorized view or workflow section for rights; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Links | A focused authorized view or workflow section for links; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Preservation metadata | A focused authorized view or workflow section for preservation metadata; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [MediaLibrary.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Queries/MediaLibrary.php) | `public function execute(?string $kind = null, ?string $term = null, bool $publicOnly = false, int $limit = 50): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AnalyzeMediaFaces.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/AnalyzeMediaFaces.php) | `public function execute(MediaAsset $asset): array` |
| [CorrectMediaTranscription.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CorrectMediaTranscription.php) | `public function execute(MediaAsset $asset, string $correctedText, ?string $actorId = null): MediaTranscriptionCorrection` |
| [CreateMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaAsset.php) | `public function execute(array $attributes): MediaAsset`<br>`public function validate(array $values): void` |
| [CreateMediaLink.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaLink.php) | `public function execute(array $attributes): MediaLink` |
| [DeleteMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/DeleteMediaAsset.php) | `public function execute(MediaAsset $asset): void` |
| [ReviewMediaFaceTag.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/ReviewMediaFaceTag.php) | `public function execute(MediaFaceTag $tag, string $status, ?string $personId = null, ?string $actorId = null): MediaFaceTag` |
| [StoreMediaUpload.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/StoreMediaUpload.php) | `public function execute(UploadedFile $file, array $attributes = []): MediaAsset` |
| [TranscribeMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/TranscribeMediaAsset.php) | `public function execute(MediaAsset $asset): array` |
| [UpdateMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/UpdateMediaAsset.php) | `public function execute(MediaAsset $asset, array $attributes): MediaAsset` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [MediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaAsset.php) | `team_id`, `kind`, `name`, `storage_disk`, `storage_path`, `mime_type`, `byte_size`, `checksum`, `captured_at`, `captured_place_id`, `transcription`, `transcription_status`, `transcription_language`, `rights_holder`, `rights_status`, `license_url`, `rights_expires_at`, `is_public`, `preservation_metadata`, `status`, `metadata` |
| [MediaFaceTag.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaFaceTag.php) | `team_id`, `media_asset_id`, `person_id`, `confidence`, `bounding_box`, `status`, `confirmed_by`, `confirmed_at`, `metadata` |
| [MediaLink.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaLink.php) | `team_id`, `media_asset_id`, `linkable_type`, `linkable_id`, `role`, `metadata` |
| [MediaTranscriptionCorrection.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaTranscriptionCorrection.php) | `team_id`, `media_asset_id`, `original_text`, `corrected_text`, `actor_id`, `metadata` |

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
