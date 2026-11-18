# CMS: Content Search Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-search). Observed identity: [`liberusoftware/module-cms-content-search-filament`](../../../modules/source/liberusoftware--module-cms-content-search-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-search-filament`  
**Matching domain module:** `cms-content-search`  
**Application:** CMS  
**Source feature:** [Content Search](../features/content-search.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-search` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Authorized indexing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Facets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spelling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Synonyms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relevance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Autocomplete:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Federated sources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reindex:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Search analytics:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-search-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `authorized-indexing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `facets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spelling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `synonyms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relevance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `autocomplete`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `federated-sources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reindex`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `search-analytics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-search` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-search-filament`](https://github.com/liberusoftware/module-cms-content-search-filament) (`liberusoftware/cms-content-search-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-search.md) · [API plan](../api/content-search.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Authorized indexing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authorized indexing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Facets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `facets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Spelling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `spelling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Synonyms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `synonyms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relevance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relevance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Autocomplete** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `autocomplete`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Federated sources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `federated sources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reindex** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reindex`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Search analytics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `search analytics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentSearchFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-search-filament/src/ContentSearchFilamentServiceProvider.php) · [SearchAnalyticResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-search-filament/src/Resources/SearchAnalyticResource.php).
<!-- layer-implementation-plan:end -->
