# liberusoftware/module-billing-domains-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Api adapter for Billing Domains.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-domains-api](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-billing-laravel-filament, `module-billing-domains-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-domains-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-domains-api` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Billing\\Domains\\Api\\DomainsApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/module.json).

**Declared capabilities:** billing.domains.api

**Declared features:** Domains Api integration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/module-billing-domains` | `^0.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Domains\\Api\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/module-billing-domains": "^0.1", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/DomainController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/src/Http/Controllers/DomainController.php) | `public function tlds(Request $request): JsonResponse`<br>`public function syncTlds(Request $request, DomainPricingService $pricing): JsonResponse`<br>`public function storeTld(Request $request, UpsertDomainTld $upsert): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Domain $domain): JsonResponse`<br>`public function store(Request $request, CreateDomain $create): JsonResponse`<br>`public function update(Request $request, Domain $domain, UpdateDomain $update): JsonResponse`<br>`public function destroy(Request $request, Domain $domain, DeleteDomain $delete): JsonResponse`<br>`public function search(Request $request, SearchDomains $search): JsonResponse`<br>`public function register(Request $request, Domain $domain, RegisterDomain $register): JsonResponse`<br>`public function renew(Request $request, Domain $domain, RenewDomain $renew): JsonResponse`<br>`public function transfer(Request $request, Domain $domain, TransferDomain $transfer): JsonResponse`<br>`public function contacts(Request $request): JsonResponse`<br>`public function eppOperations(Request $request): JsonResponse`<br>`public function storeContact(Request $request, CreateDomainContact $create): JsonResponse`<br>`public function dns(Request $request, Domain $domain): JsonResponse`<br>`public function storeDns(Request $request, Domain $domain, UpsertDnsRecord $upsert): JsonResponse`<br>`public function redeem(Request $request, Domain $domain, RedeemDomain $redeem): JsonResponse` |

Other non-legacy PHP sources: [src/DomainsApiServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/src/DomainsApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/billing-domains.yaml](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/openapi/v1/billing-domains.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
