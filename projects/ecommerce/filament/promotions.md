# Ecommerce: Promotions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#promotions). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-promotions-filament`  
**Matching domain module:** `ecommerce-promotions`  
**Application:** Ecommerce  
**Source feature:** [Promotions](../features/promotions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-promotions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Automatic discounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Buy-X-get-Y:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bundles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Free shipping/gifts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customer/product eligibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Limits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fraud controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-promotions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `automatic-discounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `buy-x-get-y`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bundles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `free-shipping-gifts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customer-product-eligibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `limits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraud-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-promotions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-promotions-filament`](https://github.com/liberusoftware/module-ecommerce-promotions-filament) (`liberusoftware/ecommerce-promotions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/promotions.md) · [API plan](../api/promotions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Automatic discounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `automatic discounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Buy-X-get-Y** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `buy-x-get-y`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bundles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bundles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Free shipping/gifts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `free shipping/gifts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customer/product eligibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer/product eligibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Limits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `limits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fraud controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraud controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
