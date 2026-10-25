# liberusoftware/module-genealogy-media: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-media module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-media](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-media`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-media` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-media` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Media\\MediaServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/module.json).

**Declared capabilities:** genealogy.media, genealogy.media.documents, genealogy.media.photographs, genealogy.media.audio-video, genealogy.media.transcription, genealogy.media.rights, genealogy.media.links, genealogy.media.preservation, genealogy.media.lifecycle

**Declared features:** genealogy media, genealogy media documents, genealogy media photographs, genealogy media audio-video, genealogy media transcription, genealogy media rights, genealogy media links, genealogy media preservation, genealogy media lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Media\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AnalyzeMediaFaces.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/AnalyzeMediaFaces.php) | `public function __construct(private readonly ?FaceRecognitionProvider $provider = null)`<br>`public function execute(MediaAsset $asset): array` |
| [src/Actions/CorrectMediaTranscription.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CorrectMediaTranscription.php) | `public function execute(MediaAsset $asset, string $correctedText, ?string $actorId = null): MediaTranscriptionCorrection` |
| [src/Actions/CreateMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaAsset.php) | `public function execute(array $attributes): MediaAsset`<br>`public function validate(array $values): void` |
| [src/Actions/CreateMediaLink.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/CreateMediaLink.php) | `public function execute(array $attributes): MediaLink` |
| [src/Actions/DeleteMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/DeleteMediaAsset.php) | `public function execute(MediaAsset $asset): void` |
| [src/Actions/ReviewMediaFaceTag.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/ReviewMediaFaceTag.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(MediaFaceTag $tag, string $status, ?string $personId = null, ?string $actorId = null): MediaFaceTag` |
| [src/Actions/StoreMediaUpload.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/StoreMediaUpload.php) | `public function execute(UploadedFile $file, array $attributes = []): MediaAsset` |
| [src/Actions/TranscribeMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/TranscribeMediaAsset.php) | `public function __construct(private readonly ?TranscriptionProvider $provider = null)`<br>`public function execute(MediaAsset $asset): array` |
| [src/Actions/UpdateMediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Actions/UpdateMediaAsset.php) | `public function execute(MediaAsset $asset, array $attributes): MediaAsset` |
| [src/Contracts/FaceRecognitionProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Contracts/FaceRecognitionProvider.php) | `public function isAvailable(): bool`<br>`public function detect(string $absolutePath): array` |
| [src/Contracts/TranscriptionProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Contracts/TranscriptionProvider.php) | `public function isAvailable(): bool`<br>`public function transcribe(string $absolutePath): array` |
| [src/Queries/MediaLibrary.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Queries/MediaLibrary.php) | `public function execute(?string $kind = null, ?string $term = null, bool $publicOnly = false, int $limit = 50): array` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Capability.php) · [src/Events/MediaAssetCreated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Events/MediaAssetCreated.php) · [src/Events/MediaAssetDeleted.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Events/MediaAssetDeleted.php) · [src/Events/MediaAssetUpdated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Events/MediaAssetUpdated.php) · [src/Events/MediaLinkCreated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Events/MediaLinkCreated.php) · [src/MediaServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/MediaServiceProvider.php) · [src/Models/MediaAsset.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaAsset.php) · [src/Models/MediaFaceTag.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaFaceTag.php) · [src/Models/MediaLink.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaLink.php) · [src/Models/MediaTranscriptionCorrection.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/src/Models/MediaTranscriptionCorrection.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_media_assets_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/database/migrations/2026_08_24_010000_create_genealogy_media_assets_table.php)
- [database/migrations/2026_08_24_020000_add_media_semantics.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/database/migrations/2026_08_24_020000_add_media_semantics.php)
- [database/migrations/2026_08_24_030000_create_genealogy_media_face_tags_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/database/migrations/2026_08_24_030000_create_genealogy_media_face_tags_table.php)
- [database/migrations/2026_08_24_040000_create_genealogy_media_transcription_corrections_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/database/migrations/2026_08_24_040000_create_genealogy_media_transcription_corrections_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-media/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
