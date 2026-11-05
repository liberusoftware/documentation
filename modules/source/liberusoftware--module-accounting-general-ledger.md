# liberusoftware/module-accounting-general-ledger: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Journals, balanced postings, reversals, corrections, allocations, accruals, prepayments, and balances.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-general-ledger](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-general-ledger`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-general-ledger` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-general-ledger` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\GeneralLedger\\GeneralLedgerServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\GeneralLedger\\GeneralLedgerServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/module.json).

**Declared capabilities:** accounting.general-ledger

**Declared features:** Journals, Balanced postings, Recurring journals, Reversals, Corrections, Allocations, Accruals, Prepayments, Balances

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-accounting-chart-of-accounts` | `^1.0` |
| `liberusoftware/module-accounting-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\GeneralLedger\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-chart-of-accounts": "^1.0", "liberusoftware/module-accounting-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAccrual.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [src/Actions/CreateAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAllocation.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [src/Actions/CreateCorrection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateCorrection.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [src/Actions/CreateJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateJournal.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [src/Actions/CreatePrepayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreatePrepayment.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [src/Actions/CreateTypedJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateTypedJournal.php) | `public function handle(JournalType $type, array $attributes, array $lines): JournalEntry` |
| [src/Actions/GenerateRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/GenerateRecurringJournal.php) | `public function handle(RecurringJournal $template, ?string $actor = null): JournalEntry` |
| [src/Actions/PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/PostJournal.php) | `public function handle(JournalEntry $journal, ?string $actor = null): JournalEntry` |
| [src/Actions/ReverseJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/ReverseJournal.php) | `public function handle(JournalEntry $journal, array $attributes = [], ?string $actor = null): JournalEntry` |
| [src/Actions/SaveRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/SaveRecurringJournal.php) | `public function handle(array $attributes, ?RecurringJournal $template = null): RecurringJournal` |
| [src/Queries/AccountBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Queries/AccountBalances.php) | `public function handle(int $bookId, ?string $through = null): array` |

Other non-legacy PHP sources: [src/Enums/JournalStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Enums/JournalStatus.php) · [src/Enums/JournalType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Enums/JournalType.php) · [src/Events/JournalCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Events/JournalCreated.php) · [src/Events/JournalPosted.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Events/JournalPosted.php) · [src/Events/JournalReversed.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Events/JournalReversed.php) · [src/Exceptions/InvalidJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Exceptions/InvalidJournal.php) · [src/GeneralLedgerServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/GeneralLedgerServiceProvider.php) · [src/Models/JournalEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalEntry.php) · [src/Models/JournalLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalLine.php) · [src/Models/RecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/RecurringJournal.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_050000_create_accounting_general_ledger_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/database/migrations/2026_08_24_050000_create_accounting_general_ledger_tables.php)
- [database/migrations/2026_08_24_070000_create_accounting_recurring_journals_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/database/migrations/2026_08_24_070000_create_accounting_recurring_journals_table.php)

[src/Enums/JournalStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Enums/JournalStatus.php): `Draft = 'draft'`, `Posted = 'posted'`, `Reversed = 'reversed'`.

[src/Enums/JournalType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Enums/JournalType.php): `General = 'general'`, `Recurring = 'recurring'`, `Correction = 'correction'`, `Allocation = 'allocation'`, `Accrual = 'accrual'`, `Prepayment = 'prepayment'`, `Reversal = 'reversal'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
