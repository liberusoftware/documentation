# Ecommerce: Multi-Source Inventory Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-source-inventory). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-multi-source-inventory-filament`  
**Matching domain module:** `ecommerce-multi-source-inventory`  
**Application:** Ecommerce  
**Source feature:** [Multi-Source Inventory](../features/multi-source-inventory.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-multi-source-inventory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sources/warehouses/stores/drop shippers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel assignment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aggregated salable quantity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Priority/distance rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source health:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-multi-source-inventory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sources-warehouses-stores-drop-shippers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-assignment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aggregated-salable-quantity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `priority-distance-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-multi-source-inventory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-multi-source-inventory-filament`](https://github.com/liberusoftware/module-ecommerce-multi-source-inventory-filament) (`liberusoftware/ecommerce-multi-source-inventory-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/multi-source-inventory.md) · [API plan](../api/multi-source-inventory.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Sources/warehouses/stores/drop shippers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sources/warehouses/stores/drop shippers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel assignment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel assignment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aggregated salable quantity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aggregated salable quantity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Priority/distance rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `priority/distance rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
