# liberusoftware/module-accounting-payment-reconciliation-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Payment reconciliation API adapter.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-payment-reconciliation-api](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-payment-reconciliation-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-payment-reconciliation-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-payment-reconciliation-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\PaymentReconciliationApi\\PaymentReconciliationApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\PaymentReconciliationApi\\PaymentReconciliationApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/module.json).

**Declared capabilities:** accounting.payment-reconciliation.api

**Declared features:** Settlement listing, Settlement import, Item matching, Missing-item detection, Provider drift, Summary

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-accounting-payment-reconciliation` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\PaymentReconciliationApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-payment-reconciliation": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/PaymentReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Http/Controllers/PaymentReconciliationController.php) | `public function index(Request $request, SettlementQuery $query): mixed`<br>`public function store(Request $request, ImportSettlement $action): JsonResponse`<br>`public function show(SettlementRun $settlementRun): SettlementResource`<br>`public function match(Request $request, SettlementItem $settlementItem, MatchSettlementItem $action): JsonResponse`<br>`public function missing(Request $request, SettlementRun $settlementRun, IdentifyMissingItems $action): JsonResponse`<br>`public function drift(Request $request, SettlementRun $settlementRun, RecordProviderDrift $action): JsonResponse`<br>`public function summary(Request $request, SettlementQuery $query): array` |

Other non-legacy PHP sources: [src/Http/Resources/SettlementResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Http/Resources/SettlementResource.php) · [src/Models/Payment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Models/Payment.php) · [src/PaymentReconciliationApiServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/PaymentReconciliationApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-payment-reconciliation.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/openapi/v1/accounting-payment-reconciliation.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
