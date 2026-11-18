# CMS: Module Cms Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-filament`  
**Matching domain module:** `module-cms`  
**Application:** CMS  
**Source feature:** [Module Cms](../features/module-cms.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sites and locales:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content lifecycle primitives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing and slug resolution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Editorial policy hooks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domain events and audit context:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sites-and-locales`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-lifecycle-primitives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing-and-slug-resolution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `editorial-policy-hooks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domain-events-and-audit-context`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-module-cms-filament`](https://github.com/liberusoftware/module-cms-module-cms-filament) (`liberusoftware/cms-module-cms-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms.md) · [API plan](../api/module-cms.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Sites and locales** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sites and locales`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content lifecycle primitives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content lifecycle primitives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing and slug resolution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing and slug resolution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Editorial policy hooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `editorial policy hooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domain events and audit context** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domain events and audit context`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ApiTokenResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Filament/ApiTokenResource.php) · [ListApiTokens.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-api/src/Filament/Pages/ListApiTokens.php).
<!-- layer-implementation-plan:end -->
