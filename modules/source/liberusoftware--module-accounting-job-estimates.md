# liberusoftware/module-accounting-job-estimates: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Job estimates, versions, approvals, actual comparison and estimate at completion.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-job-estimates](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-job-estimates`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-job-estimates` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-job-estimates` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\JobEstimates\\JobEstimatesServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\JobEstimates\\JobEstimatesServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/module.json).

**Declared capabilities:** accounting.job-estimates

**Declared features:** Cost and revenue estimates, Quantities and rates, Version approvals, Actual comparison, Estimate at completion

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\JobEstimates\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddEstimateLine.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/AddEstimateLine.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateLine` |
| [src/Actions/CreateEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateEstimate.php) | `public function handle(array $attributes): JobEstimate` |
| [src/Actions/CreateVersion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateVersion.php) | `public function handle(JobEstimate $estimate, ?string $notes = null): EstimateVersion` |
| [src/Actions/DecideEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/DecideEstimate.php) | `public function handle(JobEstimate $estimate, string $actor, bool $approved, ?string $comment = null): JobEstimate` |
| [src/Actions/RecordActual.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/RecordActual.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateActual` |
| [src/Actions/SubmitEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/SubmitEstimate.php) | `public function handle(JobEstimate $estimate): JobEstimate` |
| [src/Queries/JobEstimateQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Queries/JobEstimateQuery.php) | `public function paginate(?int $teamId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function comparison(JobEstimate $estimate): array`<br>`public function estimateAtCompletion(JobEstimate $estimate): array` |

Other non-legacy PHP sources: [src/Enums/DecisionType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/DecisionType.php) · [src/Enums/EstimateStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/EstimateStatus.php) · [src/Enums/LineType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/LineType.php) · [src/Events/EstimateApproved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Events/EstimateApproved.php) · [src/Exceptions/InvalidEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Exceptions/InvalidEstimate.php) · [src/JobEstimatesServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/JobEstimatesServiceProvider.php) · [src/Models/EstimateActual.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateActual.php) · [src/Models/EstimateApproval.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateApproval.php) · [src/Models/EstimateLine.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateLine.php) · [src/Models/EstimateVersion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateVersion.php) · [src/Models/JobEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/JobEstimate.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_017000_create_accounting_job_estimate_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/database/migrations/2026_08_26_017000_create_accounting_job_estimate_tables.php)

[src/Enums/DecisionType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/DecisionType.php): `Approved = 'approved'`, `Rejected = 'rejected'`.

[src/Enums/EstimateStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/EstimateStatus.php): `Draft = 'draft'`, `Submitted = 'submitted'`, `Approved = 'approved'`, `Rejected = 'rejected'`, `Archived = 'archived'`.

[src/Enums/LineType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Enums/LineType.php): `Cost = 'cost'`, `Revenue = 'revenue'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
