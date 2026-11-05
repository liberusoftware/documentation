# liberusoftware/module-accounting-core-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Liberu Accounting Core.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-core-api](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 3 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-core-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-core-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-core-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\CoreApi\\AccountingCoreApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\CoreApi\\AccountingCoreApiServiceProvider"]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/module.json).

**Declared capabilities:** accounting.core.api

**Declared features:** Versioned legal-entity API, Sanctum authentication, OpenAPI 3.1 contract

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `laravel/framework` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/module-accounting-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\CoreApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/FoundationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/FoundationController.php) | `public function books(Request $request)`<br>`public function book(string $book): BookResource`<br>`public function storeBook(Request $request, SaveBook $save): BookResource`<br>`public function calendars(Request $request, string $book)`<br>`public function storeCalendar(Request $request, string $book, SaveFiscalCalendar $save): FiscalCalendarResource`<br>`public function sequences(Request $request, string $book)`<br>`public function storeSequence(Request $request, string $book, SaveNumberingSequence $save): NumberingSequenceResource`<br>`public function allocateSequence(string $book, string $sequence, AllocateNumber $allocate): JsonResponse` |
| [src/Http/Controllers/LegalEntityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/LegalEntityController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(LegalEntity $legalEntity): LegalEntityResource`<br>`public function store(StoreLegalEntityRequest $request, CreateLegalEntity $create): JsonResponse`<br>`public function update(UpdateLegalEntityRequest $request, string $legalEntity, UpdateLegalEntity $update): LegalEntityResource`<br>`public function destroy(string $legalEntity): Response` |
| [src/Http/Controllers/SettingsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Controllers/SettingsController.php) | `public function index(Request $request, string $book, string $setting)`<br>`public function store(Request $request, string $book, string $setting, SaveAccountingSetting $save): AccountingSettingResource`<br>`public function show(string $book, string $setting, string $record): AccountingSettingResource`<br>`public function update(Request $request, string $book, string $setting, string $record, SaveAccountingSetting $save): AccountingSettingResource`<br>`public function destroy(string $book, string $setting, string $record): Response` |
| [src/Policies/AccountingCorePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Policies/AccountingCorePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user): bool`<br>`public function delete(?Authenticatable $user): bool` |
| [src/Policies/LegalEntityPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Policies/LegalEntityPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, LegalEntity $entity): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, LegalEntity $entity): bool`<br>`public function delete(?Authenticatable $user, LegalEntity $entity): bool` |

Other non-legacy PHP sources: [src/AccountingCoreApiServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/AccountingCoreApiServiceProvider.php) · [src/Http/Requests/StoreAccountingSettingRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/StoreAccountingSettingRequest.php) · [src/Http/Requests/StoreBookRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/StoreBookRequest.php) · [src/Http/Requests/StoreFiscalCalendarRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/StoreFiscalCalendarRequest.php) · [src/Http/Requests/StoreLegalEntityRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/StoreLegalEntityRequest.php) · [src/Http/Requests/StoreNumberingSequenceRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/StoreNumberingSequenceRequest.php) · [src/Http/Requests/UpdateLegalEntityRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Requests/UpdateLegalEntityRequest.php) · [src/Http/Resources/AccountingSettingResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Resources/AccountingSettingResource.php) · [src/Http/Resources/BookResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Resources/BookResource.php) · [src/Http/Resources/FiscalCalendarResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Resources/FiscalCalendarResource.php) · [src/Http/Resources/LegalEntityResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Resources/LegalEntityResource.php) · [src/Http/Resources/NumberingSequenceResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/src/Http/Resources/NumberingSequenceResource.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-core.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/openapi/v1/accounting-core.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/tests/TestCase.php)
- [tests/Unit/ApiContractTest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core-api/tests/Unit/ApiContractTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
