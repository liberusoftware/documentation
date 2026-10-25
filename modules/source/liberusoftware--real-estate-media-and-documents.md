# liberusoftware/real-estate-media-and-documents: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral media and document records for Liberu real-estate applications.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-media-and-documents](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `real-estate-media-and-documents`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-media-and-documents` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-media-and-documents` |
| Module version field | `1.0.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\MediaAndDocuments\\MediaAndDocumentsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\MediaAndDocuments\\MediaAndDocumentsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/module.json).

**Declared capabilities:** real-estate.media-and-documents

**Declared features:** Photos, Floorplans, Site plans, Video, Certificates, Rights, Ordering, Brochures, Retention, Versioned templates, Localized demonstrations, Signing envelopes, Digital signatures, Signing audit trail

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/real-estate-properties` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\MediaAndDocuments\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0", "liberusoftware/real-estate-properties": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/MediaDocumentPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Policies/MediaDocumentPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function delete(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function forceDelete(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function reorder(AuthUser $authUser): bool` |

Other non-legacy PHP sources: [src/Application/CanAccessMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/CanAccessMediaDocument.php) · [src/Application/CreateDocumentEnvelope.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/CreateDocumentEnvelope.php) · [src/Application/CreateDocumentVersion.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/CreateDocumentVersion.php) · [src/Application/CreateHomeReport.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/CreateHomeReport.php) · [src/Application/CreateMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/CreateMediaDocument.php) · [src/Application/DeleteMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/DeleteMediaDocument.php) · [src/Application/DocumentTemplateCatalogue.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/DocumentTemplateCatalogue.php) · [src/Application/GeneratePropertyBrochure.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/GeneratePropertyBrochure.php) · [src/Application/ReorderMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/ReorderMediaDocument.php) · [src/Application/SetMediaDocumentRetention.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/SetMediaDocumentRetention.php) · [src/Application/SignDocumentEnvelope.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/SignDocumentEnvelope.php) · [src/Application/SignMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/SignMediaDocument.php) · [src/Application/UpdateHomeReportConditions.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/UpdateHomeReportConditions.php) · [src/Application/UpdateMediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/UpdateMediaDocument.php) · [src/Application/UpdateMediaRights.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/UpdateMediaRights.php) · [src/Application/UploadHomeReportFile.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/UploadHomeReportFile.php) · [src/Application/VerifyDigitalSignature.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Application/VerifyDigitalSignature.php) · [src/Domain/DocumentEnvelopeStatus.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Domain/DocumentEnvelopeStatus.php) · [src/Domain/DocumentParticipantStatus.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Domain/DocumentParticipantStatus.php) · [src/Domain/DocumentTemplateStatus.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Domain/DocumentTemplateStatus.php) · [src/Domain/MediaAndDocumentsCapabilityDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Domain/MediaAndDocumentsCapabilityDefinition.php) · [src/MediaAndDocumentsServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/MediaAndDocumentsServiceProvider.php) · [src/Models/DocumentCategory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentCategory.php) · [src/Models/DocumentEnvelope.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelope.php) · [src/Models/DocumentEnvelopeSignature.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelopeSignature.php) · [src/Models/DocumentParticipant.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentParticipant.php) · [src/Models/DocumentSignature.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentSignature.php) · [src/Models/DocumentTemplate.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentTemplate.php) · [src/Models/DocumentVersion.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentVersion.php) · [src/Models/HomeReport.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/HomeReport.php) · [src/Models/MediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/MediaDocument.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000004_create_real_estate_media_documents_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/database/migrations/2026_08_23_000004_create_real_estate_media_documents_table.php)
- [database/migrations/2026_08_30_000021_create_real_estate_document_support_tables.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/database/migrations/2026_08_30_000021_create_real_estate_document_support_tables.php)
- [database/migrations/2026_08_30_000024_create_real_estate_home_reports.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/database/migrations/2026_08_30_000024_create_real_estate_home_reports.php)
- [database/migrations/2026_09_06_000001_add_document_workflow_model.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/database/migrations/2026_09_06_000001_add_document_workflow_model.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
