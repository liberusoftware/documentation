# liberusoftware/module-billing-provisioning: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral billing service provisioning and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-provisioning](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-billing-laravel-filament, `module-billing-provisioning`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-provisioning` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-provisioning` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Provisioning\\ProvisioningServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/module.json).

**Declared capabilities:** billing.provisioning

**Declared features:** Service state machine, Provider drivers, Queued operations, Rollback, Polling, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Provisioning\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/CreateProvisionedService.php) | `public function execute(array $attributes): ProvisionedService` |
| [src/Actions/QueueProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/QueueProvisioningOperation.php) | `public function execute(ProvisionedService $service, string $operation, array $payload = []): ProvisioningOperation` |
| [src/Actions/ReconcileProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/ReconcileProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service): ProvisionedService` |
| [src/Actions/RunProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/RunProvisioningOperation.php) | `public function __construct(private DatabaseManager $database, private ProvisioningDriverRegistry $drivers)`<br>`public function execute(ProvisioningOperation $operation): ProvisioningOperation` |
| [src/Actions/TransitionProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/TransitionProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service, ProvisioningState $state, ?string $error = null): ProvisionedService` |
| [src/Contracts/ProvisioningDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Contracts/ProvisioningDriver.php) | `public function provision(ProvisionedService $service): string`<br>`public function deprovision(ProvisionedService $service): void`<br>`public function poll(ProvisionedService $service): array` |
| [src/Policies/ProvisioningPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Policies/ProvisioningPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [src/Queries/ListProvisionedServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Queries/ListProvisionedServices.php) | `public function execute(?int $teamId = null): Collection` |
| [src/Services/ProvisioningDriverRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Services/ProvisioningDriverRegistry.php) | `public function register(string $provider, ProvisioningDriver $driver): void`<br>`public function resolve(string $provider): ProvisioningDriver` |
| [src/Support/CustomerReference.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Support/CustomerReference.php) | `public static function assertBelongsToTeam(DatabaseManager $database, mixed $customerId, mixed $teamId): ?int` |

Other non-legacy PHP sources: [src/Enums/ProvisioningState.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Enums/ProvisioningState.php) · [src/Events/ProvisionedServiceCreated.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisionedServiceCreated.php) · [src/Events/ProvisionedServiceReconciled.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisionedServiceReconciled.php) · [src/Events/ProvisionedServiceStateChanged.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisionedServiceStateChanged.php) · [src/Events/ProvisioningOperationCompleted.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisioningOperationCompleted.php) · [src/Events/ProvisioningOperationFailed.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisioningOperationFailed.php) · [src/Events/ProvisioningOperationQueued.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Events/ProvisioningOperationQueued.php) · [src/Models/ProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisionedService.php) · [src/Models/ProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisioningOperation.php) · [src/ProvisioningServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/ProvisioningServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_080000_create_billing_provisioning_tables.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/database/migrations/2026_08_24_080000_create_billing_provisioning_tables.php)
- [database/migrations/2026_08_24_220000_create_billing_provisioning_operations_table.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/database/migrations/2026_08_24_220000_create_billing_provisioning_operations_table.php)

[src/Enums/ProvisioningState.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Enums/ProvisioningState.php): `Pending = 'pending'`, `Provisioning = 'provisioning'`, `Active = 'active'`, `Suspended = 'suspended'`, `Failed = 'failed'`, `Deprovisioning = 'deprovisioning'`, `Deprovisioned = 'deprovisioned'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
