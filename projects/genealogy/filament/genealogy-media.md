# Genealogy: Genealogy Media Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-media). Observed identity: [`liberusoftware/module-genealogy-media-filament`](../../../modules/source/liberusoftware--module-genealogy-media-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-media-filament`  
**Matching domain module:** `genealogy-media`  
**Application:** Genealogy  
**Source feature:** [Genealogy Media](../features/genealogy-media.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-media` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Documents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Photographs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audio/video:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transcription:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rights:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preservation metadata:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-media-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `photographs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audio-video`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transcription`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rights`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preservation-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-media` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-media-filament`](https://github.com/liberusoftware/module-genealogy-media-filament) (`liberusoftware/genealogy-media-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-media.md) · [API plan](../api/genealogy-media.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Photographs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `photographs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audio/video** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audio/video`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transcription** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transcription`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rights** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rights`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preservation metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preservation metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MediaFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media-filament/src/MediaFilamentServiceProvider.php) · [MediaAssetResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media-filament/src/Resources/MediaAssetResource.php) · [CreateMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media-filament/src/Resources/MediaAssetResource/Pages/CreateMediaAsset.php) · [EditMediaAsset.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media-filament/src/Resources/MediaAssetResource/Pages/EditMediaAsset.php) · [ListMediaAssets.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media-filament/src/Resources/MediaAssetResource/Pages/ListMediaAssets.php).

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
