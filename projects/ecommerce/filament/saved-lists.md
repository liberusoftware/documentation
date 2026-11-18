# Ecommerce: Saved Lists Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#saved-lists). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-saved-lists-filament`  
**Matching domain module:** `ecommerce-saved-lists`  
**Application:** Ecommerce  
**Source feature:** [Saved Lists](../features/saved-lists.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-saved-lists` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Wishlists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Favorites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gift registries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Requisition lists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repeat-order lists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sharing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cart conversion:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-saved-lists-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `wishlists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `favorites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gift-registries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `requisition-lists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repeat-order-lists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cart-conversion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-saved-lists` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-saved-lists-filament`](https://github.com/liberusoftware/module-ecommerce-saved-lists-filament) (`liberusoftware/ecommerce-saved-lists-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/saved-lists.md) · [API plan](../api/saved-lists.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Wishlists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `wishlists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Favorites** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `favorites`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gift registries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gift registries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Requisition lists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requisition lists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Repeat-order lists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `repeat-order lists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sharing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sharing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alerts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alerts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cart conversion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cart conversion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
