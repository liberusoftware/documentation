# CMS: Cms Content Intelligence Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-content-intelligence). Observed identity: [`liberusoftware/module-cms-content-intelligence-filament`](../../../modules/source/liberusoftware--module-cms-content-intelligence-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-content-intelligence-filament`  
**Matching domain module:** `cms-content-intelligence`  
**Application:** CMS  
**Source feature:** [Cms Content Intelligence](../features/cms-content-intelligence.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Inventory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Readability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accessibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SEO:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Freshness:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplication:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gaps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Performance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Improvement queues:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-content-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `inventory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `readability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accessibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `seo`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `freshness`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gaps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `performance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `improvement-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-intelligence-filament`](https://github.com/liberusoftware/module-cms-content-intelligence-filament) (`liberusoftware/cms-content-intelligence-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-content-intelligence.md) · [API plan](../api/cms-content-intelligence.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Inventory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inventory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Readability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `readability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accessibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accessibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SEO** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `seo`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Freshness** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `freshness`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gaps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gaps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Performance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `performance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Improvement queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `improvement queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentIntelligenceFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-intelligence-filament/src/ContentIntelligenceFilamentServiceProvider.php) · [ContentInsightResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-intelligence-filament/src/Resources/ContentInsightResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentIntelligenceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Services/ContentIntelligenceService.php) | `public function insights(?int $teamId, ?string $metric = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function analyze(array $data, ?int $teamId = null): ContentInsight`<br>`public function review(ContentInsight $insight, string $status): ContentInsight` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentInsight.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Models/ContentInsight.php) | `team_id`, `subject_type`, `subject_key`, `metric`, `score`, `severity`, `summary`, `rationale`, `context`, `status`, `reviewed_at` |
<!-- layer-implementation-plan:end -->
