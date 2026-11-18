# Ecommerce: Reviews and Ratings Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reviews-and-ratings). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-reviews-and-ratings-filament`  
**Matching domain module:** `ecommerce-reviews-and-ratings`  
**Application:** Ecommerce  
**Source feature:** [Reviews and Ratings](../features/reviews-and-ratings.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-reviews-and-ratings` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Verified purchase:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ratings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Text/media reviews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions/answers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Merchant replies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Syndication:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Incentives disclosure:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-reviews-and-ratings-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `verified-purchase`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ratings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `text-media-reviews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions-answers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `merchant-replies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `syndication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `incentives-disclosure`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-reviews-and-ratings` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-reviews-and-ratings-filament`](https://github.com/liberusoftware/module-ecommerce-reviews-and-ratings-filament) (`liberusoftware/ecommerce-reviews-and-ratings-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/reviews-and-ratings.md) · [API plan](../api/reviews-and-ratings.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Verified purchase** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verified purchase`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ratings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ratings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Text/media reviews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `text/media reviews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Questions/answers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `questions/answers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Moderation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `moderation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Merchant replies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `merchant replies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Syndication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `syndication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Incentives disclosure** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `incentives disclosure`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
