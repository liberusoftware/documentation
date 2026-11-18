# Ecommerce: Cart Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cart). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-cart-filament`  
**Matching domain module:** `ecommerce-cart`  
**Application:** Ecommerce  
**Source feature:** [Cart](../features/cart.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-cart` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guest/customer/company carts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quantity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Persistence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Merge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sharing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Estimates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recalculation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-cart-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `guest-customer-company-carts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quantity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `persistence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `merge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `estimates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recalculation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-cart` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-cart-filament`](https://github.com/liberusoftware/module-ecommerce-cart-filament) (`liberusoftware/ecommerce-cart-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cart.md) · [API plan](../api/cart.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Guest/customer/company carts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guest/customer/company carts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quantity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quantity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Persistence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `persistence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Merge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `merge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sharing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sharing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Estimates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `estimates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recalculation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recalculation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
