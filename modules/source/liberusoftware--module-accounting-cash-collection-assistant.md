# liberusoftware/module-accounting-cash-collection-assistant: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting cash collection assistant domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-cash-collection-assistant](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-cash-collection-assistant`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-cash-collection-assistant` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-cash-collection-assistant` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\CashCollectionAssistant\\CashCollectionAssistantServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\CashCollectionAssistant\\CashCollectionAssistantServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/module.json).

**Declared capabilities:** accounting.cash-collection-assistant

**Declared features:** Invoice-risk prioritization, Reminder drafts and timing, Promise tracking, Collection policy, Approval workflow, Outcome feedback

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\CashCollectionAssistant\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/CreateCashCollectionAssistant.php) | `public function handle(array $attributes): CashCollectionAssistant` |
| [src/Actions/RecordCollectionPromise.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/RecordCollectionPromise.php) | `public function handle(CashCollectionAssistant $assistant, string $date, string\|float $amount): CashCollectionAssistant` |
| [src/Actions/ScheduleCollectionReminder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/ScheduleCollectionReminder.php) | `public function handle(CashCollectionAssistant $assistant, string $at, ?string $draft = null): CashCollectionAssistant` |
| [src/Actions/SetCollectionDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/SetCollectionDecision.php) | `public function handle(CashCollectionAssistant $assistant, string $field, string $value): CashCollectionAssistant` |
| [src/Actions/UpdateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/UpdateCashCollectionAssistant.php) | `public function handle(CashCollectionAssistant $assistant, array $attributes): CashCollectionAssistant` |
| [src/Queries/CashCollectionAssistantQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Queries/CashCollectionAssistantQuery.php) | `public function forTeam(int $teamId): Collection` |

Other non-legacy PHP sources: [src/CashCollectionAssistantServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/CashCollectionAssistantServiceProvider.php) · [src/Exceptions/InvalidCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Exceptions/InvalidCashCollectionAssistant.php) · [src/Models/CashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Models/CashCollectionAssistant.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000030_create_accounting_cash_collection_assistants_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/database/migrations/2026_08_29_000030_create_accounting_cash_collection_assistants_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
