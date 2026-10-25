# liberusoftware/module-billing-hosting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Billing Hosting domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-hosting](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-hosting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-hosting` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-hosting` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Hosting\\HostingServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/module.json).

**Declared capabilities:** billing.hosting

**Declared features:** accounts, plans, control-panel-adapters, ssl, resources, lifecycle-operations

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `guzzlehttp/guzzle` | `^7.8` |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Hosting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateHostingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingAccount.php) | `public function handle(int $teamId, array $attributes): HostingAccount` |
| [src/Actions/CreateHostingCapability.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingCapability.php) | `public function handle(int $teamId, array $attributes): HostingCapability` |
| [src/Actions/CreateHostingServer.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingServer.php) | `public function handle(int $teamId, array $attributes): HostingServer` |
| [src/Actions/PerformHostingOperation.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/PerformHostingOperation.php) | `public function __construct(private HostingDriverRegistry $drivers)`<br>`public function handle(HostingAccount $account, string $operation): HostingAccount` |
| [src/Actions/TransitionHostingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingAccount.php) | `public function handle(HostingAccount $account, string $status): HostingAccount` |
| [src/Actions/TransitionHostingCapability.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingCapability.php) | `public function handle(HostingCapability $capability, string $status): HostingCapability` |
| [src/Contracts/ControlPanelDriver.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/ControlPanelDriver.php) | `public function unsuspend(array $attributes): array`<br>`public function changePackage(array $attributes): array`<br>`public function addAddon(array $attributes): array`<br>`public function removeAddon(array $attributes): array` |
| [src/Contracts/HostingDriver.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/HostingDriver.php) | `public function key(): string`<br>`public function provision(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function terminate(array $attributes): array` |
| [src/Policies/HostingAccountPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingAccountPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, HostingAccount $record): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, HostingAccount $record): bool` |
| [src/Policies/HostingCapabilityPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [src/Queries/ListHostingRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Queries/ListHostingRecords.php) | `public function handle(int $teamId): Collection` |
| [src/Services/HostingDriverRegistry.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Services/HostingDriverRegistry.php) | `public function register(HostingDriver $driver): void`<br>`public function resolve(string $key): HostingDriver`<br>`public function keys(): array` |
| [src/Support/AbstractControlPanelDriver.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Support/AbstractControlPanelDriver.php) | `public function __construct(?ClientInterface $client = null)` |

Other non-legacy PHP sources: [src/Events/HostingAccountCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingAccountCreated.php) · [src/Events/HostingAccountStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingAccountStatusChanged.php) · [src/Events/HostingCapabilityCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingCapabilityCreated.php) · [src/Events/HostingCapabilityStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingCapabilityStatusChanged.php) · [src/Events/HostingOperationPerformed.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingOperationPerformed.php) · [src/Events/HostingServerCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Events/HostingServerCreated.php) · [src/HostingServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/HostingServiceProvider.php) · [src/Models/HostingAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingAccount.php) · [src/Models/HostingCapability.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingCapability.php) · [src/Models/HostingServer.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingServer.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_130000_create_billing_hosting_records_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/database/migrations/2026_08_24_130000_create_billing_hosting_records_table.php)
- [database/migrations/2026_08_24_190000_create_billing_hosting_capabilities_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/database/migrations/2026_08_24_190000_create_billing_hosting_capabilities_table.php)
- [database/migrations/2026_08_30_020000_create_billing_hosting_servers_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/database/migrations/2026_08_30_020000_create_billing_hosting_servers_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/HostingAccountActionTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/tests/Unit/HostingAccountActionTest.php)
- [tests/Unit/HostingLifecycleTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/tests/Unit/HostingLifecycleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
