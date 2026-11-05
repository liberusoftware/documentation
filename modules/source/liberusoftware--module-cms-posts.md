# liberusoftware/module-cms-posts: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Posts module for Liberu CMS: blog posts with taxonomy (categories & tags), workflow, versioning, and featured media.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-posts](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-posts`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-posts` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-posts` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Posts\\PostsServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Posts\\PostsServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/module.json).

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

PSR-4 mappings: `{"Liberu\\Cms\\Posts\\": "src/", "Liberu\\Cms\\Posts\\Database\\Factories\\": "database/factories/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/PostRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Contracts/PostRepositoryInterface.php) | `public function find(int $id): ?Post`<br>`public function findBySlug(string $slug): ?Post`<br>`public function published(): array`<br>`public function featured(): array`<br>`public function byCategory(string $categorySlug): array`<br>`public function byTag(string $tagSlug): array`<br>`public function search(string $query, int $limit): array` |
| [src/Filament/Pages/ListPosts.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Filament/Pages/ListPosts.php) | No named public method detected by the static index. |
| [src/Filament/PostResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Filament/PostResource.php) | `public static function form(Schema $schema): Schema`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Http/Controllers/PostApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Http/Controllers/PostApiController.php) | `public function __construct(private PostRepositoryInterface $posts)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $slug): PostResource` |
| [src/Http/Controllers/PostWriteController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Http/Controllers/PostWriteController.php) | `public function __construct(private PostRepositoryInterface $posts)`<br>`public function store(StorePostRequest $request): JsonResponse`<br>`public function update(UpdatePostRequest $request, int $id): PostResource`<br>`public function destroy(int $id): Response` |

Other non-legacy PHP sources: [src/Http/Requests/StorePostRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Http/Requests/StorePostRequest.php) · [src/Http/Requests/UpdatePostRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Http/Requests/UpdatePostRequest.php) · [src/Http/Resources/PostResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Http/Resources/PostResource.php) · [src/Models/Category.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Category.php) · [src/Models/Post.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Post.php) · [src/Models/Tag.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Tag.php) · [src/PostsModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/PostsModule.php) · [src/PostsServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/PostsServiceProvider.php) · [src/Preview/PostPreviewSource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Preview/PostPreviewSource.php) · [src/Repositories/PostRepository.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Repositories/PostRepository.php) · [src/Search/PostSearchSource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Search/PostSearchSource.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_01_05_000000_create_cms_posts_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/database/migrations/2026_01_05_000000_create_cms_posts_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
