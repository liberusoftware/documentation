# liberusoftware/module-accounting-withholding-tax: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting withholding tax domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-withholding-tax](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-withholding-tax`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-withholding-tax` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-withholding-tax` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\WithholdingTax\\WithholdingTaxServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\WithholdingTax\\WithholdingTaxServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/module.json).

**Declared capabilities:** accounting.withholding-tax

**Declared features:** Rules, Certificates, Deductions, Liabilities, Remittance, Statements, Regional filing adapters

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\WithholdingTax\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CalculateWithholdingTax.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [src/Actions/CreateWithholdingTaxRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [src/Actions/RemitWithholdingTax.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

Other non-legacy PHP sources: [src/Enums/WithholdingStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Enums/WithholdingStatus.php) · [src/Exceptions/InvalidWithholdingTax.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Exceptions/InvalidWithholdingTax.php) · [src/Models/WithholdingTaxCertificate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) · [src/Models/WithholdingTaxDeduction.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) · [src/Models/WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) · [src/Models/WithholdingTaxLiability.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) · [src/Models/WithholdingTaxRemittance.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) · [src/Models/WithholdingTaxRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) · [src/Models/WithholdingTaxStatement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) · [src/WithholdingTaxServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/WithholdingTaxServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000001_create_accounting_withholding_tax_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/database/migrations/2026_08_29_000001_create_accounting_withholding_tax_tables.php)

[src/Enums/WithholdingStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Enums/WithholdingStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Calculated = 'calculated'`, `Open = 'open'`, `Submitted = 'submitted'`, `Remitted = 'remitted'`, `Filed = 'filed'`, `Cancelled = 'cancelled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
