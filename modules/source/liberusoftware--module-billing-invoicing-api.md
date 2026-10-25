# liberusoftware/module-billing-invoicing-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Liberu Billing Invoicing.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-invoicing-api](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-invoicing-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-invoicing-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-invoicing-api` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Billing\\Invoicing\\Api\\InvoicingApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/module.json).

**Declared capabilities:** billing.invoicing.api

**Declared features:** Invoice collection, Creation, Line generation, Finalization

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/module-billing-invoicing` | `^0.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Invoicing\\Api\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/module-billing-invoicing": "^0.1", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/InvoiceController.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceController.php) | `public function index(Request $request, ListInvoices $query): JsonResponse`<br>`public function store(Request $request, CreateInvoice $create): JsonResponse`<br>`public function line(Request $request, Invoice $invoice, AddInvoiceLine $add): JsonResponse`<br>`public function finalize(Request $request, Invoice $invoice, FinalizeInvoice $finalize): JsonResponse`<br>`public function schedule(Request $request, CreateInvoiceSchedule $create): JsonResponse`<br>`public function runSchedule(Request $request, InvoiceSchedule $schedule, RunInvoiceSchedule $run): JsonResponse`<br>`public function paymentPlan(Request $request, CreatePaymentPlan $create): JsonResponse`<br>`public function runPaymentPlan(Request $request, PaymentPlan $paymentPlan, RunPaymentPlan $run): JsonResponse`<br>`public function adjust(Request $request, Invoice $invoice, ApplyInvoiceAdjustment $adjust): JsonResponse`<br>`public function lateFee(Request $request, Invoice $invoice, ApplyInvoiceLateFee $lateFee): JsonResponse`<br>`public function document(Request $request, Invoice $invoice, GenerateInvoiceDocument $document): JsonResponse`<br>`public function deliver(Request $request, Invoice $invoice, DeliverInvoice $deliver): JsonResponse` |
| [src/Http/Controllers/InvoiceSupportController.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceSupportController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInvoiceSupport $create): JsonResponse` |

Other non-legacy PHP sources: [src/InvoicingApiServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/InvoicingApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/billing-invoicing.yaml](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/openapi/v1/billing-invoicing.yaml)
- [routes/api.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
