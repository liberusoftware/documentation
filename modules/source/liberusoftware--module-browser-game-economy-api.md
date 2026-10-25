# liberusoftware/module-browser-game-economy-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Browser Game Economy.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-economy-api](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-economy-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-economy-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-economy-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\EconomyApi\\EconomyApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/module.json).

**Declared capabilities:** browser-game.economy.api

**Declared features:** Economy catalog, Resource listing, OpenAPI contract

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-browser-game-economy` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\EconomyApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-browser-game-economy": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/EconomyController.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/src/Http/Controllers/EconomyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, EconomyRecord $economy): JsonResponse`<br>`public function wallet(Request $request): JsonResponse`<br>`public function transfer(Request $request): JsonResponse`<br>`public function credit(Request $request): JsonResponse`<br>`public function debit(Request $request): JsonResponse`<br>`public function vendors(Request $request): JsonResponse`<br>`public function createVendor(Request $request): JsonResponse`<br>`public function addOffer(Request $request, EconomyVendor $vendor): JsonResponse`<br>`public function purchaseOffer(Request $request, EconomyVendorOffer $offer): JsonResponse`<br>`public function listings(Request $request): JsonResponse`<br>`public function createListing(Request $request): JsonResponse`<br>`public function purchaseListing(Request $request, EconomyListing $listing): JsonResponse`<br>`public function cancelListing(Request $request, EconomyListing $listing): JsonResponse` |

Other non-legacy PHP sources: [src/EconomyApiServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/src/EconomyApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1-browser-game-economy.yaml](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/openapi/v1-browser-game-economy.yaml)
- [routes/api.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/tests/Pest.php)
- [tests/Unit/PackageBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/tests/Unit/PackageBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
