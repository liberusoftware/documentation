# liberusoftware/module-accounting-three-way-matching: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Three-Way Matching domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-three-way-matching](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-three-way-matching`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-three-way-matching` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-three-way-matching` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\ThreeWayMatching\\ThreeWayMatchingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\ThreeWayMatching\\ThreeWayMatchingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/module.json).

**Declared capabilities:** accounting.three-way-matching

**Declared features:** PO/receipt/bill matching, Quantity/price/tax tolerances, Exceptions, Approval, Partial matching, Evidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\ThreeWayMatching\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApproveMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ApproveMatch.php) | `public function handle(MatchRecord $match, int $actorId, ?string $overrideReason = null): MatchRecord` |
| [src/Actions/CaptureMatchEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/CaptureMatchEvidence.php) | `public function handle(MatchRecord $match, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): MatchEvidence` |
| [src/Actions/EvaluateMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/EvaluateMatch.php) | `public function handle(array $attributes): MatchRecord` |
| [src/Actions/RejectMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/RejectMatch.php) | `public function handle(MatchRecord $match, string $reason): MatchRecord` |
| [src/Actions/ResolveMatchException.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ResolveMatchException.php) | `public function handle(MatchException $exception, int $actorId, string $resolution, bool $waive = false): MatchException` |
| [src/Queries/ExceptionQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/ExceptionQuery.php) | `public function open(?int $matchId = null): Collection` |
| [src/Queries/MatchQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/MatchQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/ExceptionSeverity.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/ExceptionSeverity.php) · [src/Enums/ExceptionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/ExceptionStatus.php) · [src/Enums/MatchStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/MatchStatus.php) · [src/Events/MatchApproved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Events/MatchApproved.php) · [src/Events/MatchEvaluated.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Events/MatchEvaluated.php) · [src/Events/MatchExceptionResolved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Events/MatchExceptionResolved.php) · [src/Exceptions/InvalidMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Exceptions/InvalidMatch.php) · [src/Models/MatchEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchEvidence.php) · [src/Models/MatchException.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchException.php) · [src/Models/MatchRecord.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchRecord.php) · [src/ThreeWayMatchingServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/ThreeWayMatchingServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_110000_create_accounting_three_way_matching_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/database/migrations/2026_08_25_110000_create_accounting_three_way_matching_tables.php)

[src/Enums/ExceptionSeverity.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/ExceptionSeverity.php): `Warning = 'warning'`, `Blocking = 'blocking'`.

[src/Enums/ExceptionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/ExceptionStatus.php): `Open = 'open'`, `Resolved = 'resolved'`, `Waived = 'waived'`.

[src/Enums/MatchStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Enums/MatchStatus.php): `Matched = 'matched'`, `Partial = 'partial'`, `Exception = 'exception'`, `Approved = 'approved'`, `Rejected = 'rejected'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
