# liberusoftware/module-accounting-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral legal entities, books, currencies, fiscal calendars, numbering, defaults, policies, and events.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 4 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-core` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\Core\\AccountingCoreServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\Core\\AccountingCoreServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/module.json).

**Declared capabilities:** accounting.core

**Declared features:** Legal entities, Books, Accounting basis, Currencies, Fiscal calendars, Numbering, Defaults, Policies, Domain events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AllocateNumber.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/AllocateNumber.php) | `public function handle(NumberingSequence $sequence): string` |
| [src/Actions/CreateLegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/CreateLegalEntity.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): LegalEntity` |
| [src/Actions/SaveAccountingSetting.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveAccountingSetting.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(string $modelClass, ?Model $setting, array $attributes): Model` |
| [src/Actions/SaveBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveBook.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?Book $book, array $attributes): Book` |
| [src/Actions/SaveFiscalCalendar.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveFiscalCalendar.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?FiscalCalendar $calendar, array $attributes): FiscalCalendar` |
| [src/Actions/SaveNumberingSequence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/SaveNumberingSequence.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?NumberingSequence $sequence, array $attributes): NumberingSequence` |
| [src/Actions/UpdateLegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Actions/UpdateLegalEntity.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(LegalEntity $entity, array $attributes): LegalEntity` |

Other non-legacy PHP sources: [src/AccountingCoreServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/AccountingCoreServiceProvider.php) · [src/Enums/AccountingBasis.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Enums/AccountingBasis.php) · [src/Events/AccountingSettingSaved.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Events/AccountingSettingSaved.php) · [src/Events/BookCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Events/BookCreated.php) · [src/Events/FiscalCalendarCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Events/FiscalCalendarCreated.php) · [src/Events/LegalEntityCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Events/LegalEntityCreated.php) · [src/Events/NumberingSequenceCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Events/NumberingSequenceCreated.php) · [src/Exceptions/InvalidFiscalCalendar.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Exceptions/InvalidFiscalCalendar.php) · [src/Models/AccountingDefault.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/AccountingDefault.php) · [src/Models/AccountingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/AccountingPolicy.php) · [src/Models/Book.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/Book.php) · [src/Models/FiscalCalendar.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/FiscalCalendar.php) · [src/Models/LegalEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/LegalEntity.php) · [src/Models/NumberingSequence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Models/NumberingSequence.php) · [src/ValueObjects/CurrencyCode.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/ValueObjects/CurrencyCode.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000000_create_accounting_legal_entities_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/database/migrations/2026_08_24_000000_create_accounting_legal_entities_table.php)
- [database/migrations/2026_08_24_000001_create_accounting_foundation_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/database/migrations/2026_08_24_000001_create_accounting_foundation_tables.php)

[src/Enums/AccountingBasis.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/src/Enums/AccountingBasis.php): `Accrual = 'accrual'`, `Cash = 'cash'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/tests/TestCase.php)
- [tests/Unit/AccountingCoreTest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/tests/Unit/AccountingCoreTest.php)
- [tests/Unit/CurrencyCodeTest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-core/tests/Unit/CurrencyCodeTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
