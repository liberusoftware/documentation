# liberusoftware/module-accounting-document-capture: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Document capture, extraction, supplier matching, confidence, duplicate checks, review and retention.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-document-capture](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-document-capture`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-document-capture` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-document-capture` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\DocumentCapture\\DocumentCaptureServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\DocumentCapture\\DocumentCaptureServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/module.json).

**Declared capabilities:** accounting.document-capture

**Declared features:** Upload channels, OCR extraction, Supplier matching, Line and tax capture, Confidence and duplicates, Review and retention

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\DocumentCapture\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ArchiveDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ArchiveDocument.php) | `public function handle(CapturedDocument $d, ?string $actor = null): CapturedDocument` |
| [src/Actions/ExtractDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ExtractDocument.php) | `public function handle(CapturedDocument $d, array $extracted, float $confidence, string $adapter, ?string $actor = null): CapturedDocument` |
| [src/Actions/MarkDuplicateDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/MarkDuplicateDocument.php) | `public function handle(CapturedDocument $d, CapturedDocument $original, ?string $actor = null): CapturedDocument` |
| [src/Actions/ReviewDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ReviewDocument.php) | `public function handle(CapturedDocument $d, bool $approved, ?string $reason = null, ?string $actor = null): CapturedDocument` |
| [src/Actions/UploadDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/UploadDocument.php) | `public function handle(array $a): CapturedDocument` |
| [src/Queries/CaptureQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Queries/CaptureQuery.php) | `public function paginate(?int $teamId = null, ?CaptureStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/DocumentCaptureServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/DocumentCaptureServiceProvider.php) · [src/Enums/CaptureStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Enums/CaptureStatus.php) · [src/Events/CaptureStatusChanged.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Events/CaptureStatusChanged.php) · [src/Exceptions/InvalidCapture.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Exceptions/InvalidCapture.php) · [src/Models/CaptureEvent.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CaptureEvent.php) · [src/Models/CapturedDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CapturedDocument.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_026000_create_accounting_capture_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/database/migrations/2026_08_25_026000_create_accounting_capture_tables.php)

[src/Enums/CaptureStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Enums/CaptureStatus.php): `Uploaded = 'uploaded'`, `Extracted = 'extracted'`, `InReview = 'in_review'`, `Approved = 'approved'`, `Rejected = 'rejected'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
