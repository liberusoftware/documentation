# CMS: Cms Widgets Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-widgets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-widgets-filament`  
**Matching domain module:** `cms-widgets`  
**Application:** CMS  
**Source feature:** [Cms Widgets](../features/cms-widgets.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-widgets` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reusable widget areas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dynamic query and callout widgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Placement and visibility rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cache tags and invalidation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Theme-safe widget templates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-widgets-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reusable-widget-areas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dynamic-query-and-callout-widgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `placement-and-visibility-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cache-tags-and-invalidation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `theme-safe-widget-templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-widgets` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-widgets-filament`](https://github.com/liberusoftware/module-cms-widgets-filament) (`liberusoftware/cms-widgets-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-widgets.md) · [API plan](../api/cms-widgets.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reusable widget areas** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reusable widget areas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dynamic query and callout widgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dynamic query and callout widgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Placement and visibility rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `placement and visibility rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cache tags and invalidation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cache tags and invalidation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Theme-safe widget templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `theme-safe widget templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WidgetOverview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-widgets/src/Filament/Pages/WidgetOverview.php) · [SearchWidget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-widgets/src/Widgets/SearchWidget.php) · [SocialLinksWidget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-widgets/src/Widgets/SocialLinksWidget.php).
<!-- layer-implementation-plan:end -->
