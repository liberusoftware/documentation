# liberusoftware/module-accounting-journal-approvals: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Journal approval requests, thresholds, evidence, decisions, posting and emergency controls.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-journal-approvals](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-journal-approvals`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-journal-approvals` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-journal-approvals` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\JournalApprovals\\JournalApprovalsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\JournalApprovals\\JournalApprovalsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/module.json).

**Declared capabilities:** accounting.journal-approvals

**Declared features:** Approval requests and thresholds, Reviewer evidence and rejection, Posting and emergency controls

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\JournalApprovals\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/AddEvidence.php) | `public function handle(JournalApproval $approval, array $attributes): JournalEvidence` |
| [src/Actions/ConfigureThreshold.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): ApprovalThreshold` |
| [src/Actions/DecideJournal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/DecideJournal.php) | `public function handle(JournalApproval $approval, string $actor, bool $approved, ?string $comment = null): JournalApproval` |
| [src/Actions/PostJournal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/PostJournal.php) | `public function handle(JournalApproval $approval, bool $emergency = false, ?string $reason = null): JournalApproval` |
| [src/Actions/SubmitJournal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Actions/SubmitJournal.php) | `public function handle(array $attributes, array $evidence = []): JournalApproval` |
| [src/Queries/JournalApprovalQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Queries/JournalApprovalQuery.php) | `public function paginate(?int $teamId = null, ?ApprovalStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/ApprovalStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Enums/ApprovalStatus.php) · [src/Enums/DecisionType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Enums/DecisionType.php) · [src/Events/JournalApproved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Events/JournalApproved.php) · [src/Exceptions/InvalidApproval.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Exceptions/InvalidApproval.php) · [src/JournalApprovalsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/JournalApprovalsServiceProvider.php) · [src/Models/ApprovalThreshold.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/ApprovalThreshold.php) · [src/Models/JournalApproval.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalApproval.php) · [src/Models/JournalDecision.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalDecision.php) · [src/Models/JournalEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Models/JournalEvidence.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_016000_create_accounting_journal_approval_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/database/migrations/2026_08_26_016000_create_accounting_journal_approval_tables.php)

[src/Enums/ApprovalStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Enums/ApprovalStatus.php): `Draft = 'draft'`, `Pending = 'pending'`, `Approved = 'approved'`, `Rejected = 'rejected'`, `Posted = 'posted'`, `EmergencyPosted = 'emergency_posted'`.

[src/Enums/DecisionType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-journal-approvals/src/Enums/DecisionType.php): `Approved = 'approved'`, `Rejected = 'rejected'`, `Requested = 'requested'`, `Emergency = 'emergency'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
