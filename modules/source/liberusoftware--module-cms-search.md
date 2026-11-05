# liberusoftware/module-cms-search: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Search module for Liberu CMS: full-text search over published content across every content type, exposed on the Delivery API.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-search](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-search`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-search` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-search` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Search\\CmsSearchServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Search\\CmsSearchServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/http` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `laravel/scout` | `^11.0` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Search\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/SearchController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Http/Controllers/SearchController.php) | `public function __construct( private SearchIndexInterface $index, private Container $container, )`<br>`public function index(SearchRequest $request): AnonymousResourceCollection` |
| [src/Services/ContentSearchService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Services/ContentSearchService.php) | `public function __construct(private SearchIndexInterface $index)`<br>`public function search(string $query, ?int $teamId = null, string $source = 'api'): array`<br>`public function analytics(?int $teamId, int $perPage = 25): LengthAwarePaginator`<br>`public function autocomplete(string $prefix, ?int $teamId = null): array` |

Other non-legacy PHP sources: [src/CmsSearchModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/CmsSearchModule.php) · [src/CmsSearchServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/CmsSearchServiceProvider.php) · [src/Health/SearchHealthCheck.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Health/SearchHealthCheck.php) · [src/Http/Requests/SearchRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Http/Requests/SearchRequest.php) · [src/Http/Resources/SearchResultResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Http/Resources/SearchResultResource.php) · [src/Index/DatabaseSearchIndex.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Index/DatabaseSearchIndex.php) · [src/Index/ScoutSearchIndex.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Index/ScoutSearchIndex.php) · [src/Models/SearchAnalytic.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/Models/SearchAnalytic.php) · [src/SearchRegistry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/src/SearchRegistry.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_001000_create_cms_search_analytics_table.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-search/database/migrations/2026_08_25_001000_create_cms_search_analytics_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
