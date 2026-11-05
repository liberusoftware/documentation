# liberusoftware/module-accounting-tax-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting tax core domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-tax-core](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-tax-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-tax-core` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-tax-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\TaxCore\\TaxCoreServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\TaxCore\\TaxCoreServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/module.json).

**Declared capabilities:** accounting.tax-core

**Declared features:** Tax types/codes/rates, Inclusive/exclusive treatment, Jurisdictions, Effective dates, Exemptions, Rounding, Evidence, Control accounts

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\TaxCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ActivateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ActivateTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [src/Actions/ArchiveTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ArchiveTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [src/Actions/CalculateTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CalculateTax.php) | `public function handle(TaxRule $rule, float $amount): array` |
| [src/Actions/CaptureTaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CaptureTaxEvidence.php) | `public function handle(TaxRule $rule, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): TaxEvidence` |
| [src/Actions/CreateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CreateTaxRule.php) | `public function handle(array $attributes): TaxRule` |
| [src/Actions/UpdateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/UpdateTaxRule.php) | `public function handle(TaxRule $rule, array $attributes): TaxRule` |
| [src/Queries/ActiveTaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/ActiveTaxRuleQuery.php) | `public function handle(string $code, ?string $jurisdiction = null, ?string $on = null): ?TaxRule` |
| [src/Queries/TaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/TaxRuleQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/TaxRuleStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Enums/TaxRuleStatus.php) · [src/Enums/TaxTreatment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Enums/TaxTreatment.php) · [src/Events/TaxEvidenceCaptured.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Events/TaxEvidenceCaptured.php) · [src/Events/TaxRuleCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Events/TaxRuleCreated.php) · [src/Events/TaxRuleUpdated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Events/TaxRuleUpdated.php) · [src/Exceptions/InvalidTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Exceptions/InvalidTaxRule.php) · [src/Models/TaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxEvidence.php) · [src/Models/TaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxRule.php) · [src/TaxCoreServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/TaxCoreServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_120000_create_accounting_tax_core_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/database/migrations/2026_08_25_120000_create_accounting_tax_core_tables.php)

[src/Enums/TaxRuleStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Enums/TaxRuleStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Archived = 'archived'`.

[src/Enums/TaxTreatment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Enums/TaxTreatment.php): `Exclusive = 'exclusive'`, `Inclusive = 'inclusive'`, `Exempt = 'exempt'`, `ZeroRated = 'zero_rated'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
