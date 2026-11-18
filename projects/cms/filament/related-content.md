# CMS: Related Content Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#related-content). Observed identity: [`liberusoftware/module-cms-related-content-filament`](../../../modules/source/liberusoftware--module-cms-related-content-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-related-content-filament`  
**Matching domain module:** `cms-related-content`  
**Application:** CMS  
**Source feature:** [Related Content](../features/related-content.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-related-content` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Manual/rule/search-driven relationships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Similarity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recency:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxonomy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exclusions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Explainability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fallback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-related-content-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `manual-rule-search-driven-relationships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `similarity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recency`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxonomy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exclusions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `explainability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fallback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-related-content` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-related-content-filament`](https://github.com/liberusoftware/module-cms-related-content-filament) (`liberusoftware/cms-related-content-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/related-content.md) · [API plan](../api/related-content.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Manual/rule/search-driven relationships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `manual/rule/search-driven relationships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Similarity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `similarity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recency** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recency`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Taxonomy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `taxonomy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exclusions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exclusions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Explainability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `explainability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fallback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fallback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RelatedContentFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-related-content-filament/src/RelatedContentFilamentServiceProvider.php) · [ListRelatedContent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-related-content-filament/src/Resources/Pages/ListRelatedContent.php) · [RelatedContentResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-related-content-filament/src/Resources/RelatedContentResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RelatedContentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Services/RelatedContentService.php) | `public function relate(string $sourceType, int $sourceId, string $targetType, int $targetId, string $mode = 'manual', float $score = 1, array $taxonomy = [], ?int $teamId = null): RelatedContent`<br>`public function exclude(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): RelatedContent`<br>`public function remove(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): int`<br>`public function related(string $sourceType, int $sourceId, int $limit = 10, array $taxonomy = [], ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RelatedContent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Models/RelatedContent.php) | `source_type`, `source_id`, `target_type`, `target_id`, `mode`, `score`, `explanation`, `taxonomy`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
