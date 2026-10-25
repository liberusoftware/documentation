# liberusoftware/module-cms-translation-management: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CMS translation jobs, assignments, vendors, review, memory, and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-translation-management](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `cms-translation-management`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-translation-management` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-translation-management` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\TranslationManagement\\TranslationManagementServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\TranslationManagement\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/TranslationManagementService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Actions/TranslationManagementService.php) | `public function __construct(private TranslationVendorRegistry $vendors)`<br>`public function createJob(array $attributes): TranslationJob`<br>`public function addSourceChange(TranslationJob $job, array $attributes): TranslationSourceChange`<br>`public function queue(TranslationJob $job): TranslationJob`<br>`public function cancel(TranslationJob $job): TranslationJob`<br>`public function translate(TranslationSourceChange $change, string $vendorKey, array $context = []): TranslationSourceChange`<br>`public function assign(TranslationSourceChange $change, string $assigneeType, int\|string $assigneeId, string $role, ?string $dueAt = null): TranslationAssignment`<br>`public function review(TranslationSourceChange $change, string $decision, ?string $notes = null): TranslationSourceChange`<br>`public function addVendor(array $attributes): TranslationVendor`<br>`public function remember(string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, array $metadata = [], int\|string\|null $teamId = null): TranslationMemory`<br>`public function glossary(array $attributes): TranslationGlossary`<br>`public function reconcile(TranslationJob $job): TranslationJob` |
| [src/Contracts/TranslationVendorInterface.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Contracts/TranslationVendorInterface.php) | `public function key(): string`<br>`public function translate(string $source, string $sourceLocale, string $targetLocale, array $context = []): TranslationResult` |
| [src/Queries/TranslationJobQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Queries/TranslationJobQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?TranslationJob` |
| [src/Support/TranslationResult.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Support/TranslationResult.php) | `public function __construct( public string $text, public string $provider, public string $model, public float $cost = 0.0, public array $provenance = [], )` |
| [src/Support/TranslationVendorRegistry.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Support/TranslationVendorRegistry.php) | `public function register(TranslationVendorInterface $vendor): void`<br>`public function resolve(string $key): TranslationVendorInterface` |

Other non-legacy PHP sources: [src/Events/SourceChangeTranslated.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Events/SourceChangeTranslated.php) · [src/Events/TranslationJobCreated.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Events/TranslationJobCreated.php) · [src/Events/TranslationJobReconciled.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Events/TranslationJobReconciled.php) · [src/Events/TranslationReviewed.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Events/TranslationReviewed.php) · [src/Models/TranslationAssignment.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationAssignment.php) · [src/Models/TranslationGlossary.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationGlossary.php) · [src/Models/TranslationJob.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationJob.php) · [src/Models/TranslationMemory.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationMemory.php) · [src/Models/TranslationSourceChange.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationSourceChange.php) · [src/Models/TranslationVendor.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationVendor.php) · [src/TranslationManagementModule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/TranslationManagementModule.php) · [src/TranslationManagementServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/TranslationManagementServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_020000_create_cms_translation_management_tables.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/database/migrations/2026_08_25_020000_create_cms_translation_management_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
