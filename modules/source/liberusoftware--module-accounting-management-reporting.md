# liberusoftware/module-accounting-management-reporting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Management report packs, narratives, charts, schedules, review, delivery and archive.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-management-reporting](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-management-reporting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-management-reporting` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-management-reporting` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\ManagementReporting\\ManagementReportingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\ManagementReporting\\ManagementReportingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/module.json).

**Declared capabilities:** accounting.management-reporting

**Declared features:** Report packs, Narratives and charts, Schedules and review, PDF/spreadsheet delivery, Archive

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\ManagementReporting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddReportContent.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/AddReportContent.php) | `public function narrative(ReportPack $report, array $attributes): ReportNarrative`<br>`public function chart(ReportPack $report, array $attributes): ReportChart` |
| [src/Actions/ArchiveReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ArchiveReport.php) | `public function handle(ReportPack $report): ReportPack` |
| [src/Actions/CreateReportPack.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/CreateReportPack.php) | `public function handle(array $attributes): ReportPack` |
| [src/Actions/DeliverReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/DeliverReport.php) | `public function handle(ReportPack $report, string $format, array $attributes = []): ReportDelivery` |
| [src/Actions/ReviewReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ReviewReport.php) | `public function handle(ReportPack $report, string $actor, string $decision, ?string $comment = null): ReportPack` |
| [src/Queries/ReportQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Queries/ReportQuery.php) | `public function packs(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(ReportPack $report): array` |

Other non-legacy PHP sources: [src/Enums/ReportStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Enums/ReportStatus.php) · [src/Enums/ReviewDecision.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Enums/ReviewDecision.php) · [src/Events/ReportApproved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Events/ReportApproved.php) · [src/Exceptions/InvalidReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Exceptions/InvalidReport.php) · [src/ManagementReportingServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/ManagementReportingServiceProvider.php) · [src/Models/ReportChart.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportChart.php) · [src/Models/ReportDelivery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportDelivery.php) · [src/Models/ReportNarrative.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportNarrative.php) · [src/Models/ReportPack.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportPack.php) · [src/Models/ReportReview.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportReview.php) · [src/Models/ReportSchedule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportSchedule.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_013000_create_accounting_management_reporting_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/database/migrations/2026_08_26_013000_create_accounting_management_reporting_tables.php)

[src/Enums/ReportStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Enums/ReportStatus.php): `Draft = 'draft'`, `InReview = 'in_review'`, `Approved = 'approved'`, `Delivered = 'delivered'`, `Archived = 'archived'`, `Failed = 'failed'`.

[src/Enums/ReviewDecision.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Enums/ReviewDecision.php): `Approved = 'approved'`, `Rejected = 'rejected'`, `Requested = 'requested'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
