# liberusoftware/module-cms-regions-and-widgets: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CMS regions and widgets domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-regions-and-widgets](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `cms-regions-and-widgets`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-regions-and-widgets` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-regions-and-widgets` |
| Module version field | `0.1.0` |
| Category / layers | `["domain"]` |
| Manifest provider(s) | `["Liberu\\Cms\\RegionsAndWidgets\\RegionsAndWidgetsServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\RegionsAndWidgets\\RegionsAndWidgetsServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\RegionsAndWidgets\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Services/RegionWidgetService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Services/RegionWidgetService.php) | `public function region(string $key, ?int $teamId = null): Region`<br>`public function createRegion(string $key, string $label, ?string $theme = null, ?int $teamId = null): Region`<br>`public function createWidget(string $key, string $type, array $configuration = [], ?string $title = null, ?int $teamId = null): Widget`<br>`public function place(Region $region, Widget $widget, int $position = 0, array $visibility = [], ?string $startsAt = null, ?string $endsAt = null): WidgetPlacement`<br>`public function render(string $regionKey, array $context = [], ?int $teamId = null): array` |

Other non-legacy PHP sources: [src/Models/Region.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Region.php) · [src/Models/Widget.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Widget.php) · [src/Models/WidgetPlacement.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/WidgetPlacement.php) · [src/RegionsAndWidgetsModule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/RegionsAndWidgetsModule.php) · [src/RegionsAndWidgetsServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/RegionsAndWidgetsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_100000_create_cms_regions_and_widgets_tables.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/database/migrations/2026_08_24_100000_create_cms_regions_and_widgets_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
