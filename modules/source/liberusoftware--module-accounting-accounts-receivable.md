# liberusoftware/module-accounting-accounts-receivable: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Independent Accounts Receivable domain module for Liberu Accounting.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-accounts-receivable](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-accounts-receivable`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-accounts-receivable` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-accounts-receivable` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\AccountsReceivable\\AccountsReceivableServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\AccountsReceivable\\AccountsReceivableServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/module.json).

**Declared capabilities:** accounting.accounts-receivable

**Declared features:** Customer subledger, Open items, Statements, Aging, Balances, Unapplied cash, Disputes, Credit limits and holds, Control-account reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-accounting-core` | `^1.0` |
| `liberusoftware/module-accounting-financial-master-data` | `^1.0` |
| `liberusoftware/module-accounting-sales-invoicing` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\AccountsReceivable\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-core": "^1.0", "liberusoftware/module-accounting-financial-master-data": "^1.0", "liberusoftware/module-accounting-sales-invoicing": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApplyReceipt.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ApplyReceipt.php) | `public function handle(ReceivableReceipt $receipt, ReceivableOpenItem $item, float $amount): ReceivableReceipt` |
| [src/Actions/CreateOpenItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): ReceivableOpenItem` |
| [src/Actions/EnsureAccount.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): ReceivableAccount` |
| [src/Actions/OpenDispute.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/OpenDispute.php) | `public function handle(ReceivableOpenItem $item, string $reason, ?float $amount = null): ReceivableDispute` |
| [src/Actions/RecalculateAccountBalance.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): ReceivableAccount` |
| [src/Actions/RecordReceipt.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecordReceipt.php) | `public function handle(array $attributes): ReceivableReceipt` |
| [src/Actions/ResolveDispute.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ResolveDispute.php) | `public function handle(ReceivableDispute $dispute, string $resolution, bool $accepted = false): ReceivableDispute` |
| [src/Actions/SetCreditControl.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SetCreditControl.php) | `public function handle(int $partyId, ?float $creditLimit = null, ?bool $hold = null, ?string $reason = null): ReceivableAccount` |
| [src/Actions/SyncFinalizedInvoice.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SyncFinalizedInvoice.php) | `public function handle(SalesInvoice $invoice): ReceivableOpenItem` |
| [src/Queries/AgingQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [src/Queries/ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(?float $controlBalance = null): array` |
| [src/Queries/CustomerSubledgerQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/CustomerSubledgerQuery.php) | `public function handle(int $partyId): array` |
| [src/Queries/StatementQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/StatementQuery.php) | `public function handle(int $partyId, ?\DateTimeInterface $from = null, ?\DateTimeInterface $to = null): array` |

Other non-legacy PHP sources: [src/AccountsReceivableServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/AccountsReceivableServiceProvider.php) · [src/Enums/DisputeStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Enums/DisputeStatus.php) · [src/Enums/ReceivableStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Enums/ReceivableStatus.php) · [src/Events/CreditControlChanged.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/CreditControlChanged.php) · [src/Events/DisputeOpened.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/DisputeOpened.php) · [src/Events/DisputeResolved.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/DisputeResolved.php) · [src/Events/OpenItemCreated.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/OpenItemCreated.php) · [src/Events/ReceiptApplied.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/ReceiptApplied.php) · [src/Events/ReceiptRecorded.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Events/ReceiptRecorded.php) · [src/Exceptions/InvalidReceivable.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Exceptions/InvalidReceivable.php) · [src/Listeners/SyncFinalizedInvoiceListener.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Listeners/SyncFinalizedInvoiceListener.php) · [src/Models/ReceiptApplication.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceiptApplication.php) · [src/Models/ReceivableAccount.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableAccount.php) · [src/Models/ReceivableDispute.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableDispute.php) · [src/Models/ReceivableOpenItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableOpenItem.php) · [src/Models/ReceivableReceipt.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableReceipt.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_090000_create_accounting_receivables_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/database/migrations/2026_08_24_090000_create_accounting_receivables_tables.php)

[src/Enums/DisputeStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Enums/DisputeStatus.php): `Open = 'open'`, `Resolved = 'resolved'`, `Rejected = 'rejected'`.

[src/Enums/ReceivableStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Enums/ReceivableStatus.php): `Open = 'open'`, `Partial = 'partial'`, `Settled = 'settled'`, `Unapplied = 'unapplied'`, `Applied = 'applied'`, `Disputed = 'disputed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
