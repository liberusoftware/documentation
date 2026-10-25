# liberusoftware/module-accounting-accounts-payable-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Accounts Payable.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-accounts-payable-api](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-accounts-payable-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-accounts-payable-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-accounts-payable-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\AccountsPayableApi\\AccountsPayableApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\AccountsPayableApi\\AccountsPayableApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/module.json).

**Declared capabilities:** accounting.accounts-payable.api

**Declared features:** Open items, Payments, Aging, Balances, Disputes, Payment holds, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-accounting-accounts-payable` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\AccountsPayableApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-accounts-payable": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/PayableOpenItemController.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Controllers/PayableOpenItemController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateOpenItem $action): PayableOpenItemResource`<br>`public function show(string $payableOpenItem): PayableOpenItemResource`<br>`public function aging(Request $request, AgingQuery $query): JsonResponse`<br>`public function balances(string $party, SupplierSubledgerQuery $query): JsonResponse`<br>`public function payment(Request $request, RecordPayment $action): JsonResponse`<br>`public function apply(Request $request, string $payment, ApplyPayment $action): JsonResponse`<br>`public function dispute(Request $request, OpenDispute $action): JsonResponse`<br>`public function resolve(Request $request, string $dispute, ResolveDispute $action): JsonResponse`<br>`public function paymentControl(Request $request, string $party, SetPaymentControl $action): JsonResponse`<br>`public function reconcile(ControlAccountReconciliationQuery $query): JsonResponse` |
| [src/Policies/AccountingAccountsPayablePolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Policies/AccountingAccountsPayablePolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $item): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $item): bool` |

Other non-legacy PHP sources: [src/AccountsPayableApiServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/AccountsPayableApiServiceProvider.php) · [src/Http/Resources/PayableDisputeResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Resources/PayableDisputeResource.php) · [src/Http/Resources/PayableOpenItemResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Resources/PayableOpenItemResource.php) · [src/Http/Resources/PayablePaymentResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Resources/PayablePaymentResource.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-accounts-payable.yaml](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/openapi/v1/accounting-accounts-payable.yaml)
- [routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
