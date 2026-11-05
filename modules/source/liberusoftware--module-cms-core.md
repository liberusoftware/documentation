# liberusoftware/module-cms-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

The Liberu CMS kernel: module registry, lifecycle manager, event bus, base module classes, and the module generator.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-core](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-core` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-core` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Core\\CmsCoreServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Core\\CmsCoreServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/console` | `^13.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Core\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CoreMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Actions/CoreMutationService.php) | `public function createSite(array $attributes): Site`<br>`public function createChannel(Site\|int\|string $site, array $attributes): Channel`<br>`public function updateSite(Site $site, array $attributes): Site`<br>`public function updateChannel(Channel $channel, array $attributes): Channel`<br>`public function deleteSite(Site $site): void`<br>`public function deleteChannel(Channel $channel): void`<br>`public function createIdentity(Site\|int\|string $site, array $attributes): ContentIdentity`<br>`public function createAlias(Site\|int\|string $site, array $attributes): ContentAlias`<br>`public function putSetting(?Site $site, string $key, array $value, string $environment = 'production'): Setting` |
| [src/Filament/Concerns/AuthorizesWithPermissions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Filament/Concerns/AuthorizesWithPermissions.php) | `public static function canViewAny(): bool`<br>`public static function canView(Model $record): bool`<br>`public static function canCreate(): bool`<br>`public static function canEdit(Model $record): bool`<br>`public static function canDelete(Model $record): bool`<br>`public static function canDeleteAny(): bool` |
| [src/Queries/CoreQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Queries/CoreQueryService.php) | `public function sites(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function site(string $key): ?Site`<br>`public function channels(string $siteKey, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function alias(string $siteKey, string $alias): ?ContentAlias`<br>`public function aliases(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function identities(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function settings(string $siteKey, int $perPage = 15, string $environment = 'production'): LengthAwarePaginator` |
| [src/Support/ApiPagination.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Support/ApiPagination.php) | `public static function fromArray(array $items): LengthAwarePaginator` |
| [src/Support/SearchScoring.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Support/SearchScoring.php) | `public static function perSourceLimit(): int`<br>`public static function score(string $title, string $query): float` |

Other non-legacy PHP sources: [src/CmsCoreServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/CmsCoreServiceProvider.php) · [src/Console/AbstractMakeArtifactCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Console/AbstractMakeArtifactCommand.php) · [src/Console/MakeBlockCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Console/MakeBlockCommand.php) · [src/Console/MakeFieldTypeCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Console/MakeFieldTypeCommand.php) · [src/Console/MakeHookCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Console/MakeHookCommand.php) · [src/Console/MakeModuleCommand.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Console/MakeModuleCommand.php) · [src/Database/Concerns/FiltersContentQueries.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Database/Concerns/FiltersContentQueries.php) · [src/Events/EventBus.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Events/EventBus.php) · [src/Exceptions/ModuleDependencyException.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Exceptions/ModuleDependencyException.php) · [src/Hooks/HookBus.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Hooks/HookBus.php) · [src/Http/Concerns/EmbedsFeaturedMedia.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Http/Concerns/EmbedsFeaturedMedia.php) · [src/Http/Concerns/FiltersApiResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Http/Concerns/FiltersApiResource.php) · [src/Http/Concerns/WritesWorkflowContent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Http/Concerns/WritesWorkflowContent.php) · [src/Models/Channel.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Channel.php) · [src/Models/ContentAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentAlias.php) · [src/Models/ContentIdentity.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentIdentity.php) · [src/Models/Setting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Setting.php) · [src/Models/Site.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Site.php) · [src/Module/AbstractModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/AbstractModule.php) · [src/Module/ArrayModuleStateRepository.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/ArrayModuleStateRepository.php) · [src/Module/DatabaseModuleStateRepository.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/DatabaseModuleStateRepository.php) · [src/Module/ModuleManager.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/ModuleManager.php) · [src/Module/ModuleRegistry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/ModuleRegistry.php) · [src/Module/ModuleServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Module/ModuleServiceProvider.php) · [src/Tenant/HasTenant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Tenant/HasTenant.php) · [src/Tenant/NullTenantResolver.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Tenant/NullTenantResolver.php) · [src/Tenant/RequestTenantContext.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Tenant/RequestTenantContext.php) · [src/Tenant/TenantScope.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Tenant/TenantScope.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_01_01_000000_create_cms_modules_table.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/database/migrations/2026_01_01_000000_create_cms_modules_table.php)
- [database/migrations/2026_08_24_010000_create_cms_core_domain_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/database/migrations/2026_08_24_010000_create_cms_core_domain_tables.php)
- [database/migrations/2026_08_29_020000_add_tenancy_to_cms_content_aliases.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/database/migrations/2026_08_29_020000_add_tenancy_to_cms_content_aliases.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
