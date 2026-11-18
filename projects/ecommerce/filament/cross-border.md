# Ecommerce: Cross-Border Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cross-border). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-cross-border-filament`  
**Matching domain module:** `ecommerce-cross-border`  
**Application:** Ecommerce  
**Source feature:** [Cross-Border](../features/cross-border.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-cross-border` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Duties/import taxes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Landed cost estimates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restrictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Harmonized codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Origin:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Importer policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customs documents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-cross-border-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `duties-import-taxes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `landed-cost-estimates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restrictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `harmonized-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `origin`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `importer-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customs-documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-cross-border` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-cross-border-filament`](https://github.com/liberusoftware/module-ecommerce-cross-border-filament) (`liberusoftware/ecommerce-cross-border-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cross-border.md) · [API plan](../api/cross-border.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Duties/import taxes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duties/import taxes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Landed cost estimates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `landed cost estimates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Restrictions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `restrictions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Harmonized codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `harmonized codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Origin** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `origin`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Importer policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `importer policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customs documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customs documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
