# Ecommerce: Point of Sale Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#point-of-sale). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-point-of-sale-filament`  
**Matching domain module:** `ecommerce-point-of-sale`  
**Application:** Ecommerce  
**Source feature:** [Point of Sale](../features/point-of-sale.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-point-of-sale` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Registers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Carts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Discounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tenders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Returns/exchanges:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Holds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Staff actions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-point-of-sale-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `registers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `carts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `discounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tenders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `returns-exchanges`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `holds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `staff-actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-point-of-sale` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-point-of-sale-filament`](https://github.com/liberusoftware/module-ecommerce-point-of-sale-filament) (`liberusoftware/ecommerce-point-of-sale-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/point-of-sale.md) · [API plan](../api/point-of-sale.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Registers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Carts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `carts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Products** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `products`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Taxes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `taxes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Discounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `discounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tenders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tenders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Receipts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receipts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Returns/exchanges** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `returns/exchanges`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Holds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `holds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Staff actions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `staff actions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
