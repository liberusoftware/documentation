# liberusoftware/module-genealogy-import-export: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-import-export module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-import-export](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-genealogy-laravel-filament, `genealogy-import-export`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-import-export` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-import-export` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\ImportExport\\ImportExportServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/module.json).

**Declared capabilities:** genealogy.import-export, genealogy.import-export.gedcom, genealogy.import-export.gedcom-7, genealogy.import-export.gedcom-x, genealogy.import-export.gramps, genealogy.import-export.validation, genealogy.import-export.dry-run, genealogy.import-export.duplicates, genealogy.import-export.reports, genealogy.import-export.round-trip, genealogy.import-export.lifecycle

**Declared features:** genealogy import export, genealogy import export gedcom, genealogy GEDCOM 7 export, genealogy GEDCOM X export, genealogy import export gramps, genealogy import export validation, genealogy import export dry-run, genealogy import export duplicates, genealogy import export reports, genealogy import export round-trip, genealogy import export lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/audit` | `^1.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `liberusoftware/module-genealogy-people` | `^1.0` |
| `liberusoftware/module-genealogy-relationships` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\ImportExport\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/audit": "^1.0", "liberusoftware/module-genealogy-core": "^1.0", "liberusoftware/module-genealogy-people": "^1.0", "liberusoftware/module-genealogy-relationships": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateDataTransfer.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Actions/CreateDataTransfer.php) | `public function execute(array $attributes): DataTransfer`<br>`public function validate(array $values): void` |
| [src/Actions/DeleteDataTransfer.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Actions/DeleteDataTransfer.php) | `public function execute(DataTransfer $transfer): void` |
| [src/Actions/ExportGenealogyData.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Actions/ExportGenealogyData.php) | `public function __construct( private readonly CreateDataTransfer $create, private readonly UpdateDataTransfer $update, private readonly GedcomExporter $gedcom, private readonly GedcomXExporter $gedcomX, private readonly GrampsExporter $gramps, )`<br>`public function execute(string $format = 'gedcom', string $name = 'Genealogy export'): ExportedGenealogyData` |
| [src/Actions/UndoDataTransfer.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Actions/UndoDataTransfer.php) | `public function execute(DataTransfer $transfer): DataTransfer` |
| [src/Actions/UpdateDataTransfer.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Actions/UpdateDataTransfer.php) | `public function execute(DataTransfer $transfer, array $attributes): DataTransfer` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Capability.php) · [src/Data/ExportedGenealogyData.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Data/ExportedGenealogyData.php) · [src/Events/DataTransferCreated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Events/DataTransferCreated.php) · [src/Events/DataTransferDeleted.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Events/DataTransferDeleted.php) · [src/Events/DataTransferUndone.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Events/DataTransferUndone.php) · [src/Events/DataTransferUpdated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Events/DataTransferUpdated.php) · [src/Exporters/GedcomExporter.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Exporters/GedcomExporter.php) · [src/Exporters/GedcomXExporter.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Exporters/GedcomXExporter.php) · [src/Exporters/GrampsExporter.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Exporters/GrampsExporter.php) · [src/ImportExportServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/ImportExportServiceProvider.php) · [src/Importers/GenealogyDocumentParser.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Importers/GenealogyDocumentParser.php) · [src/Importers/GenealogyImportService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Importers/GenealogyImportService.php) · [src/Models/DataTransfer.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/src/Models/DataTransfer.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_data_transfers_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/database/migrations/2026_08_24_010000_create_genealogy_data_transfers_table.php)
- [database/migrations/2026_08_24_020000_add_transfer_details.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/database/migrations/2026_08_24_020000_add_transfer_details.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-import-export/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
