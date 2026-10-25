# liberusoftware/module-accounting-intercompany-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API for intercompany accounting.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-intercompany-api](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-intercompany-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-intercompany-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-intercompany-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\IntercompanyApi\\IntercompanyApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\IntercompanyApi\\IntercompanyApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/module.json).

**Declared capabilities:** accounting.intercompany.api

**Declared features:** Counterparties and rules, Confirmations and settlement, Evidence and reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-accounting-intercompany` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\IntercompanyApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-intercompany": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/IntercompanyController.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/src/Http/Controllers/IntercompanyController.php) | `public function __construct(private readonly IntercompanyQuery $query)`<br>`public function index(Request $r): IntercompanyTransactionResource`<br>`public function counterparty(Request $r, CreateCounterparty $a): JsonResponse`<br>`public function rule(Request $r, IntercompanyCounterparty $counterparty, ConfigureTradingRule $a): JsonResponse`<br>`public function store(Request $r, IntercompanyCounterparty $counterparty, CreateTransaction $a): IntercompanyTransactionResource`<br>`public function show(IntercompanyTransaction $transaction): IntercompanyTransactionResource`<br>`public function confirm(Request $r, IntercompanyTransaction $transaction, ConfirmTransaction $a): IntercompanyTransactionResource`<br>`public function settle(Request $r, IntercompanyTransaction $transaction, SettleTransaction $a): IntercompanyTransactionResource`<br>`public function difference(Request $r, IntercompanyTransaction $transaction, RecordDifference $a): JsonResponse`<br>`public function evidence(Request $r, IntercompanyTransaction $transaction, AddTransferPricingEvidence $a): JsonResponse`<br>`public function summary(IntercompanyTransaction $transaction): JsonResponse`<br>`public function reconcile(Request $r, ReconcileIntercompany $a): JsonResponse` |

Other non-legacy PHP sources: [src/Http/Resources/IntercompanyTransactionResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/src/Http/Resources/IntercompanyTransactionResource.php) · [src/IntercompanyApiServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/src/IntercompanyApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-intercompany.yaml](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/openapi/v1/accounting-intercompany.yaml)
- [routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
