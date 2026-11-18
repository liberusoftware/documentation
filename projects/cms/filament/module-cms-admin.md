# CMS: Module Cms Admin Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-admin). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-admin-filament`  
**Matching domain module:** `module-cms-admin`  
**Application:** CMS  
**Source feature:** [Module Cms Admin](../features/module-cms-admin.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-admin` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Editorial workspaces:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Role-aware navigation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Saved views and filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bulk editorial actions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Activity and status widgets:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-admin-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `editorial-workspaces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `role-aware-navigation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `saved-views-and-filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bulk-editorial-actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `activity-and-status-widgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-admin` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-admin-filament`](https://github.com/liberusoftware/module-cms-admin-filament) (`liberusoftware/cms-admin-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-admin.md) · [API plan](../api/module-cms-admin.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Editorial workspaces** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `editorial workspaces`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Role-aware navigation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `role-aware navigation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Saved views and filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `saved views and filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bulk editorial actions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bulk editorial actions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Activity and status widgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `activity and status widgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CmsAdminPlugin.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-admin/src/Filament/CmsAdminPlugin.php) · [ModuleManagement.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-admin/src/Filament/Pages/ModuleManagement.php) · [ModuleView.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-admin/src/Filament/Support/ModuleView.php) · [ContentOverviewWidget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-admin/src/Filament/Widgets/ContentOverviewWidget.php) · [ModulesOverviewWidget.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-admin/src/Filament/Widgets/ModulesOverviewWidget.php).
<!-- layer-implementation-plan:end -->
