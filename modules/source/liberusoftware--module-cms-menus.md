# liberusoftware/module-cms-menus: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Menu & navigation for Liberu CMS: multi-level menus by location with permission-aware rendering.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-menus](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-menus`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-menus` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-menus` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Menus\\MenusServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Menus\\MenusServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Menus\\": "src/", "Liberu\\Cms\\Menus\\Database\\Factories\\": "database/factories/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/MenuRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Contracts/MenuRepositoryInterface.php) | `public function find(int $id): ?Menu`<br>`public function forLocation(string $location, string $variant = 'default'): ?Menu` |
| [src/Filament/MenuItemResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Filament/MenuItemResource.php) | `public static function form(Schema $schema): Schema`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/MenuResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Filament/MenuResource.php) | `public static function form(Schema $schema): Schema`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/Pages/ListMenuItems.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Filament/Pages/ListMenuItems.php) | No named public method detected by the static index. |
| [src/Filament/Pages/ListMenus.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Filament/Pages/ListMenus.php) | No named public method detected by the static index. |
| [src/Http/Controllers/MenuApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Http/Controllers/MenuApiController.php) | `public function __construct(private MenuRepositoryInterface $menus)`<br>`public function show(string $location): MenuResource` |
| [src/Services/MenuService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Services/MenuService.php) | `public function createMenu(array $attributes): Menu`<br>`public function updateMenu(Menu $menu, array $attributes): Menu`<br>`public function saveItem(Menu $menu, array $attributes, ?MenuItem $item = null): MenuItem`<br>`public function deleteItem(MenuItem $item): void` |

Other non-legacy PHP sources: [src/Http/Resources/MenuResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Http/Resources/MenuResource.php) · [src/MenuBuilder.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/MenuBuilder.php) · [src/MenuNode.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/MenuNode.php) · [src/MenusModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/MenusModule.php) · [src/MenusServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/MenusServiceProvider.php) · [src/Models/Menu.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Models/Menu.php) · [src/Models/MenuItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Models/MenuItem.php) · [src/Repositories/MenuRepository.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/src/Repositories/MenuRepository.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_01_08_000000_create_cms_menus_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/database/migrations/2026_01_08_000000_create_cms_menus_tables.php)
- [database/migrations/2026_07_24_000000_add_team_id_to_cms_menus_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/database/migrations/2026_07_24_000000_add_team_id_to_cms_menus_tables.php)
- [database/migrations/2026_08_25_000000_add_navigation_contract_to_cms_menus.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-menus/database/migrations/2026_08_25_000000_add_navigation_contract_to_cms_menus.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
