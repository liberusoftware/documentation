# liberusoftware/module-accounting-sales-invoicing-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Authenticated API adapter for accounting sales invoicing.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-sales-invoicing-api](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-sales-invoicing-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-sales-invoicing-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-sales-invoicing-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\SalesInvoicingApi\\SalesInvoicingApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\SalesInvoicingApi\\SalesInvoicingApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/module.json).

**Declared capabilities:** accounting.sales-invoicing.api

**Declared features:** Invoice CRUD, Approval, Finalization, Deposits, Delivery

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/module-accounting-sales-invoicing` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\SalesInvoicingApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-sales-invoicing": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/SalesInvoicingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Http/Controllers/SalesInvoicingController.php) | `public function index(Request $request)`<br>`public function show(string $invoice): SalesInvoiceResource`<br>`public function store(Request $request, CreateInvoice $create)`<br>`public function approve(string $invoice, ApproveInvoice $approve): SalesInvoiceResource`<br>`public function finalize(Request $request, string $invoice, FinalizeInvoice $finalize): SalesInvoiceResource`<br>`public function deposit(Request $request, string $invoice, RecordDeposit $deposit): SalesInvoiceResource`<br>`public function deliver(string $invoice, MarkInvoiceDelivered $deliver): SalesInvoiceResource`<br>`public function destroy(string $invoice): Response` |
| [src/Policies/SalesInvoicingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Policies/SalesInvoicingPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function delete(?Authenticatable $u, SalesInvoice $i): bool` |

Other non-legacy PHP sources: [src/Http/Resources/SalesInvoiceResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Http/Resources/SalesInvoiceResource.php) · [src/SalesInvoicingApiServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/SalesInvoicingApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-sales-invoicing.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/openapi/v1/accounting-sales-invoicing.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
