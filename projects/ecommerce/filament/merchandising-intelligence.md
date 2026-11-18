# Ecommerce: Merchandising Intelligence Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#merchandising-intelligence). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-merchandising-intelligence-filament`  
**Matching domain module:** `ecommerce-merchandising-intelligence`  
**Application:** Ecommerce  
**Source feature:** [Merchandising Intelligence](../features/merchandising-intelligence.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-merchandising-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Search gaps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Zero results:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Affinity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trends:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recommendations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inventory-aware ranking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experiment analysis:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-merchandising-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `search-gaps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `zero-results`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `affinity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trends`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recommendations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inventory-aware-ranking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experiment-analysis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-merchandising-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-ecommerce-merchandising-intelligence-filament`](https://github.com/liberusoftware/module-ecommerce-merchandising-intelligence-filament) (`liberusoftware/ecommerce-merchandising-intelligence-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/merchandising-intelligence.md) · [API plan](../api/merchandising-intelligence.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Search gaps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `search gaps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Zero results** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `zero results`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conversion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conversion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Affinity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `affinity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trends** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trends`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recommendations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recommendations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inventory-aware ranking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inventory-aware ranking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experiment analysis** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experiment analysis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
