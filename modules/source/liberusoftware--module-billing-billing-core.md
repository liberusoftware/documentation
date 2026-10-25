# liberusoftware/module-billing-billing-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Framework-neutral billing accounts, contacts, currencies, tax profiles, sequences, terms, settings, and period primitives.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [billing-core](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 3 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-billing-core](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 3 |

Physical source locations: **2**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `billing-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-billing-core` |
| Composer version field | `0.1.3` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-billing-core` |
| Module version field | `0.1.3` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\Billing\\Core\\BillingCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/module.json).

**Declared capabilities:** billing.core

**Declared features:** Accounts, Contacts, Currencies, Currency conversion, Tax profiles, Tax calculation, Tax exemptions, Threshold tax rates, Sequences, Terms, Billing settings, Billing periods, Deterministic amounts

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CalculateTax.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [src/Actions/ConvertCurrency.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [src/Actions/CreateBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [src/Actions/CreateBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [src/Actions/DeleteBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [src/Actions/DeleteBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [src/Actions/TransitionBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [src/Actions/UpdateBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [src/Actions/UpdateBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [src/Policies/BillingAccountPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |
| [src/Policies/BillingCoreRecordPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingCoreRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Model $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Model $record): bool`<br>`public function delete(object $user, Model $record): bool` |
| [src/Queries/ListBillingAccounts.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListBillingRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/BillingCoreServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/BillingCoreServiceProvider.php) · [src/Enums/BillingAccountStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Enums/BillingAccountStatus.php) · [src/Events/BillingAccountCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingAccountCreated.php) · [src/Events/BillingAccountDeleted.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingAccountDeleted.php) · [src/Events/BillingAccountStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingAccountStatusChanged.php) · [src/Events/BillingAccountUpdated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingAccountUpdated.php) · [src/Events/BillingRecordCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingRecordCreated.php) · [src/Events/BillingRecordDeleted.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingRecordDeleted.php) · [src/Events/BillingRecordUpdated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Events/BillingRecordUpdated.php) · [src/Models/BillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) · [src/Models/BillingContact.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) · [src/Models/BillingCurrency.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) · [src/Models/BillingSequence.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) · [src/Models/BillingSetting.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) · [src/Models/BillingTaxExemption.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) · [src/Models/BillingTaxProfile.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) · [src/Models/BillingTerm.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) · [src/ValueObjects/BillingAmount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/ValueObjects/BillingAmount.php) · [src/ValueObjects/BillingPeriod.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/ValueObjects/BillingPeriod.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000000_create_billing_accounts_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/database/migrations/2026_08_23_000000_create_billing_accounts_table.php)
- [database/migrations/2026_08_24_140000_create_billing_core_records.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/database/migrations/2026_08_24_140000_create_billing_core_records.php)
- [database/migrations/2026_08_29_210000_add_tax_thresholds_and_exemptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/database/migrations/2026_08_29_210000_add_tax_thresholds_and_exemptions.php)

[src/Enums/BillingAccountStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Enums/BillingAccountStatus.php): `Active = 'active'`, `Suspended = 'suspended'`, `Closed = 'closed'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/tests/TestCase.php)
- [tests/Unit/BillingCoreTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/tests/Unit/BillingCoreTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: billing-laravel, `module-billing-billing-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-billing-core` |
| Composer version field | `0.1.3` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-billing-core` |
| Module version field | `0.1.3` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Core\\BillingCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/module.json).

**Declared capabilities:** billing.core

**Declared features:** Accounts, Contacts, Currencies, Currency conversion, Tax profiles, Tax calculation, Tax exemptions, Threshold tax rates, Sequences, Terms, Billing settings, Billing periods, Deterministic amounts

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CalculateTax.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [src/Actions/ConvertCurrency.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [src/Actions/CreateBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [src/Actions/CreateBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [src/Actions/DeleteBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [src/Actions/DeleteBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [src/Actions/TransitionBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [src/Actions/UpdateBillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [src/Actions/UpdateBillingRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [src/Policies/BillingAccountPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |
| [src/Policies/BillingCoreRecordPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Policies/BillingCoreRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Model $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Model $record): bool`<br>`public function delete(object $user, Model $record): bool` |
| [src/Queries/ListBillingAccounts.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListBillingRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/BillingCoreServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/BillingCoreServiceProvider.php) · [src/Enums/BillingAccountStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Enums/BillingAccountStatus.php) · [src/Events/BillingAccountCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingAccountCreated.php) · [src/Events/BillingAccountDeleted.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingAccountDeleted.php) · [src/Events/BillingAccountStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingAccountStatusChanged.php) · [src/Events/BillingAccountUpdated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingAccountUpdated.php) · [src/Events/BillingRecordCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingRecordCreated.php) · [src/Events/BillingRecordDeleted.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingRecordDeleted.php) · [src/Events/BillingRecordUpdated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Events/BillingRecordUpdated.php) · [src/Models/BillingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingAccount.php) · [src/Models/BillingContact.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingContact.php) · [src/Models/BillingCurrency.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingCurrency.php) · [src/Models/BillingSequence.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingSequence.php) · [src/Models/BillingSetting.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingSetting.php) · [src/Models/BillingTaxExemption.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingTaxExemption.php) · [src/Models/BillingTaxProfile.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingTaxProfile.php) · [src/Models/BillingTerm.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Models/BillingTerm.php) · [src/ValueObjects/BillingAmount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/ValueObjects/BillingAmount.php) · [src/ValueObjects/BillingPeriod.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/ValueObjects/BillingPeriod.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000000_create_billing_accounts_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/database/migrations/2026_08_23_000000_create_billing_accounts_table.php)
- [database/migrations/2026_08_24_140000_create_billing_core_records.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/database/migrations/2026_08_24_140000_create_billing_core_records.php)
- [database/migrations/2026_08_29_210000_add_tax_thresholds_and_exemptions.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/database/migrations/2026_08_29_210000_add_tax_thresholds_and_exemptions.php)

[src/Enums/BillingAccountStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/src/Enums/BillingAccountStatus.php): `Active = 'active'`, `Suspended = 'suspended'`, `Closed = 'closed'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/tests/TestCase.php)
- [tests/Unit/BillingCoreTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-billing-core/tests/Unit/BillingCoreTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
