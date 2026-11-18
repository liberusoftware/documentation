# Ecommerce: Product Types Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-types). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-product-types-filament`  
**Matching domain module:** `ecommerce-product-types`  
**Application:** Ecommerce  
**Source feature:** [Product Types](../features/product-types.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-product-types` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Simple:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configurable/variant:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouped:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bundle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Kit:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Virtual:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Downloadable:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Service:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Subscription:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gift card:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Custom type contracts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-product-types-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `simple`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configurable-variant`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouped`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bundle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `kit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `virtual`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `downloadable`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `service`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `subscription`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gift-card`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `custom-type-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-product-types` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-product-types-filament`](https://github.com/liberusoftware/module-ecommerce-product-types-filament) (`liberusoftware/ecommerce-product-types-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/product-types.md) · [API plan](../api/product-types.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Simple** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `simple`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configurable/variant** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configurable/variant`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouped** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouped`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bundle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bundle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Kit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `kit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Virtual** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `virtual`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Downloadable** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `downloadable`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Service** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Subscription** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `subscription`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gift card** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gift card`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Custom type contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `custom type contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
