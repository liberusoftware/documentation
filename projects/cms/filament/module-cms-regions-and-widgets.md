# CMS: Module Cms Regions And Widgets Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-regions-and-widgets). Observed identity: [`liberusoftware/module-cms-regions-and-widgets-filament`](../../../modules/source/liberusoftware--module-cms-regions-and-widgets-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-regions-and-widgets-filament`  
**Matching domain module:** `module-cms-regions-and-widgets`  
**Application:** CMS  
**Source feature:** [Module Cms Regions And Widgets](../features/module-cms-regions-and-widgets.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-regions-and-widgets` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Theme regions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reusable widgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Placement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ordering:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Visibility by route/context/audience:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Caching:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-regions-and-widgets-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `theme-regions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reusable-widgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `placement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ordering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `visibility-by-route-context-audience`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `caching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-regions-and-widgets` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-regions-and-widgets-filament`](https://github.com/liberusoftware/module-cms-regions-and-widgets-filament) (`liberusoftware/cms-regions-and-widgets-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-regions-and-widgets.md) · [API plan](../api/module-cms-regions-and-widgets.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Theme regions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `theme regions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reusable widgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reusable widgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Placement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `placement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ordering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ordering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Visibility by route/context/audience** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `visibility by route/context/audience`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Caching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `caching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RegionsAndWidgetsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-regions-and-widgets-filament/src/RegionsAndWidgetsFilamentServiceProvider.php) · [ListRegions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-regions-and-widgets-filament/src/Resources/Pages/ListRegions.php) · [RegionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-regions-and-widgets-filament/src/Resources/RegionResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RegionWidgetService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Services/RegionWidgetService.php) | `public function region(string $key, ?int $teamId = null): Region`<br>`public function createRegion(string $key, string $label, ?string $theme = null, ?int $teamId = null): Region`<br>`public function createWidget(string $key, string $type, array $configuration = [], ?string $title = null, ?int $teamId = null): Widget`<br>`public function place(Region $region, Widget $widget, int $position = 0, array $visibility = [], ?string $startsAt = null, ?string $endsAt = null): WidgetPlacement`<br>`public function render(string $regionKey, array $context = [], ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Region.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Region.php) | `key`, `label`, `theme`, `team_id` |
| [Widget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/Widget.php) | `key`, `type`, `title`, `configuration`, `active`, `team_id` |
| [WidgetPlacement.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-regions-and-widgets/src/Models/WidgetPlacement.php) | `region_id`, `widget_id`, `position`, `visibility`, `starts_at`, `ends_at`, `active` |
<!-- layer-implementation-plan:end -->
