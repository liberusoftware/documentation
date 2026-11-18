# CMS: Module Cms Views And Query Builder Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-views-and-query-builder). Observed identity: [`liberusoftware/module-cms-views-and-query-builder-filament`](../../../modules/source/liberusoftware--module-cms-views-and-query-builder-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-views-and-query-builder-filament`  
**Matching domain module:** `module-cms-views-and-query-builder`  
**Application:** CMS  
**Source feature:** [Module Cms Views And Query Builder](../features/module-cms-views-and-query-builder.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-views-and-query-builder` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-safe listings from content/fields/relationships with filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sorting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exposed filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pagination:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Displays:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-views-and-query-builder-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `permission-safe-listings-from-content-fields-relationships-with-filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sorting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exposed-filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pagination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `displays`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-views-and-query-builder` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-views-and-query-builder-filament`](https://github.com/liberusoftware/module-cms-views-and-query-builder-filament) (`liberusoftware/cms-views-and-query-builder-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-views-and-query-builder.md) · [API plan](../api/module-cms-views-and-query-builder.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Permission-safe listings from content/fields/relationships with filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permission-safe listings from content/fields/relationships with filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sorting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sorting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exposed filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exposed filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pagination** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pagination`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feeds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feeds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Displays** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `displays`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListViewDefinitions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-filament/src/Resources/Pages/ListViewDefinitions.php) · [ViewDefinitionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-filament/src/Resources/ViewDefinitionResource.php) · [ViewsAndQueryBuilderFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-filament/src/ViewsAndQueryBuilderFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListingQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ListingQueryService.php) | `public function execute(ViewDefinition $view, int $perPage = 15, array $input = []): LengthAwarePaginator` |
| [ViewDefinitionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ViewDefinitionQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $slug): ?ViewDefinition`<br>`public function publishedList(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function findPublished(string $slug): ?ViewDefinition` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewDefinitionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Actions/ViewDefinitionMutationService.php) | `public function create(array $attributes): ViewDefinition`<br>`public function update(ViewDefinition $view, array $attributes): ViewDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ViewDefinition.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Models/ViewDefinition.php) | `name`, `slug`, `source`, `description`, `definition`, `visibility`, `status`, `published_at`, `user_id`, `team_id` |
<!-- layer-implementation-plan:end -->
