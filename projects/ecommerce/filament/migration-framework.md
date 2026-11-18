# Ecommerce: Migration Framework Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-migration-framework-filament`  
**Matching domain module:** `ecommerce-migration-framework`  
**Application:** Ecommerce  
**Source feature:** [Migration Framework](../features/migration-framework.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-migration-framework` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **WooCommerce:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Magento/Adobe Commerce:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shopify:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Generic source adapters with mappings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dry run:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Batches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resume:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Media:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-migration-framework-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `woocommerce`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `magento-adobe-commerce`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shopify`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `generic-source-adapters-with-mappings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dry-run`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `batches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resume`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `media`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-migration-framework` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-migration-framework-filament`](https://github.com/liberusoftware/module-ecommerce-migration-framework-filament) (`liberusoftware/ecommerce-migration-framework-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/migration-framework.md) · [API plan](../api/migration-framework.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **WooCommerce** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `woocommerce`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Magento/Adobe Commerce** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `magento/adobe commerce`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shopify** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shopify`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Generic source adapters with mappings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `generic source adapters with mappings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dry run** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dry run`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Batches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `batches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resume** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resume`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Media** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `media`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
