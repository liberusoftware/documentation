# liberusoftware/module-maintenance-procurement: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Procurement domain module for Liberu Maintenance

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-procurement](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: maintenance-laravel, `module-maintenance-procurement`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-procurement` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-procurement` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\Procurement\\ProcurementServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/composer.json) · [module.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/module.json).

**Declared capabilities:** maintenance.procurement

**Declared features:** Suppliers, Requests, Approvals, Purchase orders, Receipts, Returns, Cost allocation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\Procurement\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApprovePurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/ApprovePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId): PurchaseRequest` |
| [src/Actions/CreatePurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreatePurchaseRequest.php) | `public function handle(int $teamId, array $attributes): PurchaseRequest` |
| [src/Actions/CreateVendorContract.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorContract.php) | `public function handle(int $teamId, array $attributes): VendorContract` |
| [src/Actions/CreateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, array $attributes): VendorPerformanceEvaluation` |
| [src/Actions/DeletePurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeletePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request): void` |
| [src/Actions/DeleteVendorContract.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorContract.php) | `public function handle(int $teamId, VendorContract $contract): void` |
| [src/Actions/DeleteVendorPerformanceEvaluation.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation): void` |
| [src/Actions/RejectPurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/RejectPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId, ?string $reason = null): PurchaseRequest` |
| [src/Actions/TransitionPurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, string $status, ?int $actorId = null): PurchaseRequest` |
| [src/Actions/TransitionVendorContract.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, string $status): VendorContract` |
| [src/Actions/UpdatePurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdatePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, array $attributes): PurchaseRequest` |
| [src/Actions/UpdateVendorContract.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdateVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, array $attributes): VendorContract` |
| [src/Actions/UpdateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/UpdateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation, array $attributes): VendorPerformanceEvaluation` |
| [src/Policies/PurchaseRequestPolicy.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Policies/PurchaseRequestPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, PurchaseRequest $request): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, PurchaseRequest $request): bool`<br>`public function delete(object $user, PurchaseRequest $request): bool` |
| [src/Policies/VendorContractPolicy.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Policies/VendorContractPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, VendorContract $contract): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, VendorContract $contract): bool`<br>`public function delete(object $user, VendorContract $contract): bool` |
| [src/Policies/VendorPerformanceEvaluationPolicy.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Policies/VendorPerformanceEvaluationPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, VendorPerformanceEvaluation $evaluation): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, VendorPerformanceEvaluation $evaluation): bool`<br>`public function delete(object $user, VendorPerformanceEvaluation $evaluation): bool` |

Other non-legacy PHP sources: [src/Models/PurchaseRequest.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/PurchaseRequest.php) · [src/Models/VendorContract.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorContract.php) · [src/Models/VendorPerformanceEvaluation.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorPerformanceEvaluation.php) · [src/ProcurementServiceProvider.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/ProcurementServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_080000_create_maintenance_purchase_requests_table.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/database/migrations/2026_08_25_080000_create_maintenance_purchase_requests_table.php)
- [database/migrations/2026_08_29_200000_create_maintenance_vendor_contracts_table.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/database/migrations/2026_08_29_200000_create_maintenance_vendor_contracts_table.php)
- [database/migrations/2026_08_29_201500_create_maintenance_vendor_evaluations_table.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/database/migrations/2026_08_29_201500_create_maintenance_vendor_evaluations_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
