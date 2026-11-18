# CMS: Module Cms Layout Builder Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-layout-builder). Observed identity: [`liberusoftware/module-cms-layout-builder-filament`](../../../modules/source/liberusoftware--module-cms-layout-builder-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-layout-builder-filament`  
**Matching domain module:** `module-cms-layout-builder`  
**Application:** CMS  
**Source feature:** [Module Cms Layout Builder](../features/module-cms-layout-builder.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-layout-builder` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Regions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grids:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drag/drop composition:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Type defaults:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Per-record overrides:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responsive settings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Permissions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-layout-builder-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `regions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drag-drop-composition`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `type-defaults`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `per-record-overrides`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responsive-settings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `permissions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-layout-builder` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-layout-builder-filament`](https://github.com/liberusoftware/module-cms-layout-builder-filament) (`liberusoftware/cms-layout-builder-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-layout-builder.md) · [API plan](../api/module-cms-layout-builder.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Regions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grids** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drag/drop composition** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drag/drop composition`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Type defaults** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `type defaults`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Per-record overrides** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `per-record overrides`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Responsive settings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `responsive settings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Permissions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permissions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LayoutBuilderFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-layout-builder-filament/src/LayoutBuilderFilamentServiceProvider.php) · [LayoutResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-layout-builder-filament/src/Resources/LayoutResource.php) · [ListLayouts.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-layout-builder-filament/src/Resources/Pages/ListLayouts.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LayoutBuilderService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-layout-builder/src/Services/LayoutBuilderService.php) | `public function create(array $attributes): Layout`<br>`public function update(Layout $layout, array $attributes): Layout`<br>`public function publish(Layout $layout): Layout`<br>`public function resolve(string $targetType, int\|string $targetId, ?string $slug = null): ?Layout` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Layout.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-layout-builder/src/Models/Layout.php) | `name`, `slug`, `target_type`, `target_id`, `definition`, `status`, `published_at`, `user_id`, `team_id` |
<!-- layer-implementation-plan:end -->
