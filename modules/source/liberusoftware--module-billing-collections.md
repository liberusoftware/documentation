# liberusoftware/module-billing-collections: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral collections, dunning, credit control, suspension, write-off, and recovery.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-collections](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-collections`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-collections` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-collections` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Collections\\CollectionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/module.json).

**Declared capabilities:** billing.collections

**Declared features:** Retries, Dunning, Reminders, Promises, Credit control, Suspension, Write-off, Recovery

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Collections\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApplyCreditControl.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ApplyCreditControl.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $level, ?string $reason = null): CollectionCase` |
| [src/Actions/OpenCollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/OpenCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): CollectionCase` |
| [src/Actions/PromisePayment.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/PromisePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $dueAt): CollectionCase` |
| [src/Actions/RecoverCollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RecoverCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case): CollectionCase` |
| [src/Actions/RetryCollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RetryCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [src/Actions/ScheduleDunning.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleDunning.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [src/Actions/ScheduleReminder.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleReminder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [src/Actions/SuspendCollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/SuspendCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [src/Actions/WriteOffCollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/WriteOffCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [src/Policies/CollectionCasePolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Policies/CollectionCasePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, CollectionCase $case): bool` |
| [src/Queries/ListCollectionCases.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Queries/ListCollectionCases.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Support/CustomerReference.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Support/CustomerReference.php) | `public static function assertBelongsToTeam(DatabaseManager $database, mixed $customerId, mixed $teamId): ?int` |

Other non-legacy PHP sources: [src/CollectionsServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/CollectionsServiceProvider.php) · [src/Enums/CollectionStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Enums/CollectionStatus.php) · [src/Events/CollectionCaseOpened.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CollectionCaseOpened.php) · [src/Events/CollectionCaseRecovered.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CollectionCaseRecovered.php) · [src/Events/CollectionCaseRetried.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CollectionCaseRetried.php) · [src/Events/CollectionCaseSuspended.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CollectionCaseSuspended.php) · [src/Events/CollectionCaseWrittenOff.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CollectionCaseWrittenOff.php) · [src/Events/CreditControlApplied.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/CreditControlApplied.php) · [src/Events/DunningScheduled.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/DunningScheduled.php) · [src/Events/PaymentPromised.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/PaymentPromised.php) · [src/Events/ReminderScheduled.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Events/ReminderScheduled.php) · [src/Models/CollectionCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Models/CollectionCase.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_060000_create_billing_collection_cases_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/database/migrations/2026_08_24_060000_create_billing_collection_cases_table.php)

[src/Enums/CollectionStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Enums/CollectionStatus.php): `Open = 'open'`, `Promised = 'promised'`, `Suspended = 'suspended'`, `WrittenOff = 'written_off'`, `Recovered = 'recovered'`, `Closed = 'closed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
