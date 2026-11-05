# liberusoftware/module-accounting-accounts-receivable-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Accounts Receivable.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-accounts-receivable-api](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-accounts-receivable-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-accounts-receivable-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-accounts-receivable-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\AccountsReceivableApi\\AccountsReceivableApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\AccountsReceivableApi\\AccountsReceivableApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/module.json).

**Declared capabilities:** accounting.accounts-receivable.api

**Declared features:** Open-item listing, Open-item creation, Statements, Aging, Balances, Receipts, Receipt applications, Disputes, Credit control, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-accounting-accounts-receivable` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\AccountsReceivableApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-accounts-receivable": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/AccountsReceivableController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Controllers/AccountsReceivableController.php) | `public function index(Request $request): JsonResponse`<br>`public function receipts(Request $request): JsonResponse`<br>`public function disputes(Request $request): JsonResponse`<br>`public function show(ReceivableOpenItem $openItem): ReceivableOpenItemResource`<br>`public function store(Request $request): ReceivableOpenItemResource`<br>`public function statement(Request $request, int $party): JsonResponse`<br>`public function aging(Request $request): JsonResponse`<br>`public function balances(Request $request, int $party): JsonResponse`<br>`public function receipt(Request $request): JsonResponse`<br>`public function apply(Request $request, ReceivableReceipt $receipt): JsonResponse`<br>`public function dispute(Request $request): JsonResponse`<br>`public function resolve(Request $request, ReceivableDispute $dispute): JsonResponse`<br>`public function credit(Request $request, int $party): JsonResponse`<br>`public function reconcile(Request $request): JsonResponse` |
| [src/Policies/AccountsReceivablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Policies/AccountsReceivablePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $model): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $model): bool` |

Other non-legacy PHP sources: [src/AccountsReceivableApiServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/AccountsReceivableApiServiceProvider.php) · [src/Http/Resources/ReceivableDisputeResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Resources/ReceivableDisputeResource.php) · [src/Http/Resources/ReceivableOpenItemResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Resources/ReceivableOpenItemResource.php) · [src/Http/Resources/ReceivableReceiptResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Resources/ReceivableReceiptResource.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-accounts-receivable.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/openapi/v1/accounting-accounts-receivable.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
