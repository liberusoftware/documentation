# liberusoftware/module-billing-customer-portal: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Billing Customer Portal domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-customer-portal](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-customer-portal`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-customer-portal` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-customer-portal` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\CustomerPortal\\CustomerPortalServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/module.json).

**Declared capabilities:** billing.customer-portal

**Declared features:** profile, orders, services, usage, invoices, payments, tickets, changes, cancellation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\CustomerPortal\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreatePortalItem.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalItem.php) | `public function handle(int $teamId, array $attributes): PortalItem` |
| [src/Actions/CreatePortalRequest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalRequest.php) | `public function handle(int $teamId, array $attributes): PortalRequest` |
| [src/Actions/TransitionPortalItem.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalItem.php) | `public function handle(PortalItem $item, string $status): PortalItem` |
| [src/Actions/TransitionPortalRequest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalRequest.php) | `public function handle(PortalRequest $request, string $status): PortalRequest` |
| [src/Policies/PortalItemPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalItemPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $item): bool`<br>`public function view(?object $user, object $item): bool` |
| [src/Policies/PortalRequestPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalRequestPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, PortalRequest $record): bool`<br>`public function update(?Authenticatable $user, PortalRequest $record): bool` |
| [src/Queries/GetCustomerBillingSummary.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/GetCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function handle(int $teamId, int $customerId, ?CarbonInterface $startAt = null, ?CarbonInterface $endAt = null): array` |
| [src/Queries/ListCustomerPortalRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListCustomerPortalRecords.php) | `public function handle(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListPortalItems.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListPortalItems.php) | `public function handle(int $teamId, ?string $type = null, int $perPage = 25): LengthAwarePaginator` |
| [src/Support/CustomerReference.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Support/CustomerReference.php) | `public static function assertBelongsToTeam(DatabaseManager $database, mixed $customerId, int $teamId): ?int` |

Other non-legacy PHP sources: [src/CustomerPortalServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/CustomerPortalServiceProvider.php) · [src/Events/PortalItemCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Events/PortalItemCreated.php) · [src/Events/PortalItemStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Events/PortalItemStatusChanged.php) · [src/Events/PortalRequestCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Events/PortalRequestCreated.php) · [src/Events/PortalRequestStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Events/PortalRequestStatusChanged.php) · [src/Models/PortalItem.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalItem.php) · [src/Models/PortalRequest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalRequest.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_130000_create_billing_customer_portal_records_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/database/migrations/2026_08_24_130000_create_billing_customer_portal_records_table.php)
- [database/migrations/2026_08_24_170000_create_billing_customer_portal_items_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/database/migrations/2026_08_24_170000_create_billing_customer_portal_items_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/PortalRequestActionTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/tests/Unit/PortalRequestActionTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
