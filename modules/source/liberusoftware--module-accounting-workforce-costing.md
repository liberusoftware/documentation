# liberusoftware/module-accounting-workforce-costing: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting workforce costing domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-workforce-costing](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-workforce-costing`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-workforce-costing` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-workforce-costing` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\WorkforceCosting\\WorkforceCostingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\WorkforceCosting\\WorkforceCostingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/module.json).

**Declared capabilities:** accounting.workforce-costing

**Declared features:** Time and payroll cost allocation, Department, Class and location, Capitalization rules, Profitability reporting

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\WorkforceCosting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AllocateWorkforceCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/AllocateWorkforceCost.php) | `public function handle(WorkforceCost $cost, string\|WorkforceAllocationType $allocationType, string $allocationRef): WorkforceCost` |
| [src/Actions/CapitalizeWorkforceCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CapitalizeWorkforceCost.php) | `public function handle(WorkforceCost $cost): WorkforceCost` |
| [src/Actions/CreateWorkforceCostingRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CreateWorkforceCostingRule.php) | `public function handle(array $attributes): WorkforceCostingRule` |
| [src/Actions/RecordWorkforceCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/RecordWorkforceCost.php) | `public function handle(array $attributes): WorkforceCost` |
| [src/Queries/WorkforceProfitability.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Queries/WorkforceProfitability.php) | `public function handle(int $teamId, ?string $from = null, ?string $to = null): array` |

Other non-legacy PHP sources: [src/Enums/WorkforceAllocationType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Enums/WorkforceAllocationType.php) · [src/Enums/WorkforceCostStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Enums/WorkforceCostStatus.php) · [src/Exceptions/InvalidWorkforceCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Exceptions/InvalidWorkforceCost.php) · [src/Models/WorkforceCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCost.php) · [src/Models/WorkforceCostingRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCostingRule.php) · [src/WorkforceCostingServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/WorkforceCostingServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000009_create_accounting_workforce_costing_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/database/migrations/2026_08_29_000009_create_accounting_workforce_costing_tables.php)

[src/Enums/WorkforceAllocationType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Enums/WorkforceAllocationType.php): `Project = 'project'`, `Department = 'department'`, `ClassDimension = 'class'`, `Location = 'location'`.

[src/Enums/WorkforceCostStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Enums/WorkforceCostStatus.php): `Draft = 'draft'`, `Allocated = 'allocated'`, `Posted = 'posted'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
