# liberusoftware/module-accounting-payment-reconciliation: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral payment settlement reconciliation domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-payment-reconciliation](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-payment-reconciliation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-payment-reconciliation` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-payment-reconciliation` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\PaymentReconciliation\\PaymentReconciliationServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\PaymentReconciliation\\PaymentReconciliationServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/module.json).

**Declared capabilities:** accounting.payment-reconciliation

**Declared features:** Settlement imports, Fees, refunds, and disputes, Matching, Missing items, Provider drift, Audit evidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\PaymentReconciliation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/IdentifyMissingItems.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/IdentifyMissingItems.php) | `public function handle(SettlementRun $run, array $expected): array` |
| [src/Actions/ImportSettlement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ImportSettlement.php) | `public function handle(array $attributes, array $items): SettlementRun` |
| [src/Actions/MatchSettlementItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/MatchSettlementItem.php) | `public function handle(SettlementItem $item, string $referenceType, string $referenceId, float $amount, ?int $actorId = null, ?string $idempotencyKey = null): SettlementMatch` |
| [src/Actions/RecordProviderDrift.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/RecordProviderDrift.php) | `public function handle(SettlementRun $run, string $field, mixed $expected, mixed $actual, string $severity = 'warning'): ProviderDrift` |
| [src/Actions/ResolveReconciliationException.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ResolveReconciliationException.php) | `public function handle(ReconciliationException $exception, int $actorId, string $resolution, bool $waive = false): ReconciliationException` |
| [src/Queries/SettlementQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Queries/SettlementQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(?int $teamId = null): array` |

Other non-legacy PHP sources: [src/Enums/DriftStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/DriftStatus.php) · [src/Enums/ReconciliationExceptionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/ReconciliationExceptionStatus.php) · [src/Enums/SettlementItemStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementItemStatus.php) · [src/Enums/SettlementItemType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementItemType.php) · [src/Enums/SettlementStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementStatus.php) · [src/Events/ReconciliationExceptionResolved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Events/ReconciliationExceptionResolved.php) · [src/Events/SettlementImported.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Events/SettlementImported.php) · [src/Events/SettlementMatched.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Events/SettlementMatched.php) · [src/Exceptions/InvalidReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Exceptions/InvalidReconciliation.php) · [src/Models/AuditEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/AuditEvidence.php) · [src/Models/ProviderDrift.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ProviderDrift.php) · [src/Models/ReconciliationException.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ReconciliationException.php) · [src/Models/SettlementItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementItem.php) · [src/Models/SettlementMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementMatch.php) · [src/Models/SettlementRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementRun.php) · [src/PaymentReconciliationServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/PaymentReconciliationServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_001000_create_accounting_payment_reconciliation_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/database/migrations/2026_08_26_001000_create_accounting_payment_reconciliation_tables.php)

[src/Enums/DriftStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/DriftStatus.php): `Open = 'open'`, `Resolved = 'resolved'`, `Accepted = 'accepted'`.

[src/Enums/ReconciliationExceptionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/ReconciliationExceptionStatus.php): `Open = 'open'`, `Resolved = 'resolved'`, `Waived = 'waived'`.

[src/Enums/SettlementItemStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementItemStatus.php): `Unmatched = 'unmatched'`, `PartiallyMatched = 'partially_matched'`, `Matched = 'matched'`, `Exception = 'exception'`.

[src/Enums/SettlementItemType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementItemType.php): `Charge = 'charge'`, `Fee = 'fee'`, `Refund = 'refund'`, `Dispute = 'dispute'`, `Adjustment = 'adjustment'`.

[src/Enums/SettlementStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Enums/SettlementStatus.php): `Imported = 'imported'`, `PartiallyMatched = 'partially_matched'`, `Matched = 'matched'`, `Exception = 'exception'`, `Reconciled = 'reconciled'`, `Failed = 'failed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
