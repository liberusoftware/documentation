# liberusoftware/module-cms-pages: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Pages module for Liberu CMS: hierarchical pages with editorial workflow, versioning, slugs, and featured media.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-pages](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `cms-pages`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-pages` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-pages` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Pages\\PagesServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Pages\\PagesServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-cms-content` | `^0.1` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Pages\\": "src/", "Liberu\\Cms\\Pages\\Database\\Factories\\": "database/factories/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/PageRepositoryInterface.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Contracts/PageRepositoryInterface.php) | `public function find(int $id): ?Page`<br>`public function findBySlug(string $slug): ?Page`<br>`public function findByPath(string $path): ?Page`<br>`public function redirectForPath(string $path): ?PageRedirect`<br>`public function published(): array`<br>`public function roots(): array`<br>`public function search(string $query, int $limit): array` |
| [src/Filament/PageResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Filament/PageResource.php) | `public static function form(Schema $schema): Schema`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/Pages/ListPages.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Filament/Pages/ListPages.php) | No named public method detected by the static index. |
| [src/Http/Controllers/PageApiController.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageApiController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function index(): AnonymousResourceCollection`<br>`public function show(string $slug): PageResource` |
| [src/Http/Controllers/PageWriteController.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageWriteController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function store(StorePageRequest $request): JsonResponse`<br>`public function update(UpdatePageRequest $request, int $id): PageResource`<br>`public function destroy(int $id): Response` |
| [src/Queries/PageTreeQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Queries/PageTreeQuery.php) | `public function roots(string $search = ''): Collection` |
| [src/Services/PageRoutingService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Services/PageRoutingService.php) | `public function addAlias(Page $page, string $path): PageAlias`<br>`public function createRedirect(array $attributes): PageRedirect`<br>`public function updateRedirect(PageRedirect $redirect, array $attributes): PageRedirect`<br>`public function deleteRedirect(PageRedirect $redirect): void` |

Other non-legacy PHP sources: [src/Http/Requests/StorePageRequest.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Requests/StorePageRequest.php) · [src/Http/Requests/UpdatePageRequest.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Requests/UpdatePageRequest.php) · [src/Http/Resources/PageResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Resources/PageResource.php) · [src/Models/Page.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/Page.php) · [src/Models/PageAlias.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageAlias.php) · [src/Models/PageRedirect.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageRedirect.php) · [src/PagesModule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/PagesModule.php) · [src/PagesServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/PagesServiceProvider.php) · [src/Preview/PagePreviewSource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Preview/PagePreviewSource.php) · [src/Repositories/PageRepository.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Repositories/PageRepository.php) · [src/Search/PageSearchSource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Search/PageSearchSource.php) · [src/Seo/PageSitemapProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Seo/PageSitemapProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_01_04_000000_create_cms_pages_table.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/database/migrations/2026_01_04_000000_create_cms_pages_table.php)
- [database/migrations/2026_08_24_040000_add_page_routing_features.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/database/migrations/2026_08_24_040000_add_page_routing_features.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
