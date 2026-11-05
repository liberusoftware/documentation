# liberusoftware/module-cms-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Delivery API for Liberu CMS: a versioned, read-only, Sanctum-authenticated JSON API that serves published content to decoupled frontends.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-api](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-api` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Api\\CmsApiServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Api\\CmsApiServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `illuminate/console` | `^13.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Api\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Filament/ApiTokenResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Filament/ApiTokenResource.php) | `public static function canViewAny(): bool`<br>`public static function canCreate(): bool`<br>`public static function getEloquentQuery(): Builder`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/Pages/ListApiTokens.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Filament/Pages/ListApiTokens.php) | No named public method detected by the static index. |
| [src/Http/Controllers/OpenApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Http/Controllers/OpenApiController.php) | `public function __construct(private OpenApiGenerator $generator)`<br>`public function __invoke(): JsonResponse` |
| [src/Http/Controllers/PreviewController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Http/Controllers/PreviewController.php) | `public function __construct( private PreviewRegistryInterface $registry, private TenantContextInterface $tenant, )`<br>`public function __invoke(Request $request, string $type, int $id): JsonResource` |
| [src/Support/PreviewLink.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Support/PreviewLink.php) | `public function for(string $type, int $id, int\|string\|null $team, ?int $ttlMinutes = null): string` |

Other non-legacy PHP sources: [src/ApiResourceRegistry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/ApiResourceRegistry.php) · [src/CmsApiModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/CmsApiModule.php) · [src/CmsApiServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/CmsApiServiceProvider.php) · [src/Console/IssueTokenCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Console/IssueTokenCommand.php) · [src/Console/PreviewLinkCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Console/PreviewLinkCommand.php) · [src/Http/Middleware/ForceJsonResponse.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Http/Middleware/ForceJsonResponse.php) · [src/Http/Middleware/SetApiTenant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Http/Middleware/SetApiTenant.php) · [src/OpenApi/OpenApiGenerator.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/OpenApi/OpenApiGenerator.php) · [src/PreviewRegistry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/PreviewRegistry.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
