# liberusoftware/module-billing-customer-portal-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Api adapter for Billing Customer Portal.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-customer-portal-api](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-billing-laravel-filament, `module-billing-customer-portal-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-customer-portal-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-customer-portal-api` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Billing\\CustomerPortal\\Api\\CustomerPortalApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/module.json).

**Declared capabilities:** billing.customer-portal.api

**Declared features:** Customer Portal Api integration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/module-billing-customer-portal` | `^0.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\CustomerPortal\\Api\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/module-billing-customer-portal": "^0.1", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/CustomerBillingController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/CustomerBillingController.php) | `public function show(Request $request, int $customer, GetCustomerBillingSummary $summary): JsonResponse` |
| [src/Http/Controllers/PortalItemController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/PortalItemController.php) | `public function index(Request $request, ListPortalItems $list): JsonResponse`<br>`public function store(Request $request, CreatePortalItem $create): JsonResponse`<br>`public function transition(Request $request, int $item, TransitionPortalItem $transition): JsonResponse` |
| [src/Http/Controllers/PortalRequestController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Http/Controllers/PortalRequestController.php) | `public function index(Request $request, ListCustomerPortalRecords $list): JsonResponse`<br>`public function store(Request $request, CreatePortalRequest $create): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionPortalRequest $transition): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse` |

Other non-legacy PHP sources: [src/CustomerPortalApiServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/CustomerPortalApiServiceProvider.php) · [src/Models/Customer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Models/Customer.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/billing-customer-portal.yaml](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/openapi/v1/billing-customer-portal.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
