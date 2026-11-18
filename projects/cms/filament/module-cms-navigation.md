# CMS: Module Cms Navigation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-navigation). Observed identity: [`liberusoftware/module-cms-navigation-filament`](../../../modules/source/liberusoftware--module-cms-navigation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-navigation-filament`  
**Matching domain module:** `module-cms-navigation`  
**Application:** CMS  
**Source feature:** [Module Cms Navigation](../features/module-cms-navigation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-navigation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Unlimited menus:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Nested items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content/custom/system links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Menu variants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Visibility rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Active trails:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-navigation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `unlimited-menus`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nested-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-custom-system-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `menu-variants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `visibility-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `active-trails`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-navigation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-module-cms-navigation-filament`](https://github.com/liberusoftware/module-cms-module-cms-navigation-filament) (`liberusoftware/cms-module-cms-navigation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-navigation.md) · [API plan](../api/module-cms-navigation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Unlimited menus** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unlimited menus`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Nested items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nested items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content/custom/system links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content/custom/system links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Menu variants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `menu variants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Visibility rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `visibility rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Active trails** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `active trails`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [NavigationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-navigation-filament/src/NavigationFilamentServiceProvider.php) · [NavigationItemResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-navigation-filament/src/Resources/NavigationItemResource.php) · [NavigationResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-navigation-filament/src/Resources/NavigationResource.php) · [ListNavigation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-navigation-filament/src/Resources/NavigationResource/Pages/ListNavigation.php).
<!-- layer-implementation-plan:end -->
