# liberusoftware/module-cms-web-delivery: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CMS canonical web delivery, preview, redirects, metadata, and edge invalidation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-web-delivery](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `cms-web-delivery`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-web-delivery` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-web-delivery` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\WebDelivery\\WebDeliveryServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\WebDelivery\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/WebDeliveryService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Actions/WebDeliveryService.php) | `public function __construct(private EdgeInvalidationRegistry $edge)`<br>`public function registerRoute(array $attributes): DeliveryRoute`<br>`public function updateRoute(DeliveryRoute $route, array $attributes): DeliveryRoute`<br>`public function deleteRoute(DeliveryRoute $route): void`<br>`public function render(string $path, ?string $previewToken = null): DeliveryResult`<br>`public function issuePreviewToken(DeliveryRoute $route): string`<br>`public function setMaintenance(DeliveryRoute $route, bool $enabled): DeliveryRoute`<br>`public function invalidate(array $cacheTags, string $idempotencyKey, ?string $provider = null, int\|string\|null $teamId = null): DeliveryInvalidation` |
| [src/Queries/DeliveryRouteQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Queries/DeliveryRouteQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $path): ?DeliveryRoute` |
| [src/Support/DeliveryResult.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Support/DeliveryResult.php) | `public function __construct( public int $status, public string $path, public ?string $body, public array $metadata, public array $cacheTags, public ?string $canonicalUrl = null, public ?string $redirectUrl = null, public bool $preview = false, )` |
| [src/Support/EdgeInvalidationRegistry.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Support/EdgeInvalidationRegistry.php) | `public function invalidate(DeliveryInvalidation $invalidation): void` |
| [src/Support/NullEdgeInvalidationRegistry.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Support/NullEdgeInvalidationRegistry.php) | `public function invalidate(DeliveryInvalidation $invalidation): void` |

Other non-legacy PHP sources: [src/Events/DeliveryCacheInvalidated.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Events/DeliveryCacheInvalidated.php) · [src/Events/DeliveryRouteRegistered.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Events/DeliveryRouteRegistered.php) · [src/Models/DeliveryInvalidation.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryInvalidation.php) · [src/Models/DeliveryRoute.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryRoute.php) · [src/WebDeliveryModule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/WebDeliveryModule.php) · [src/WebDeliveryServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/WebDeliveryServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_030000_create_cms_web_delivery_tables.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/database/migrations/2026_08_25_030000_create_cms_web_delivery_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
