# CMS: Cms Collections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-collections-filament`  
**Matching domain module:** `cms-collections`  
**Application:** CMS  
**Source feature:** [Cms Collections](../features/cms-collections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-collections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Custom collections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hierarchical and flat taxonomies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Term assignments and ordering:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filterable archive queries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Localized term slugs:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-collections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `custom-collections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hierarchical-and-flat-taxonomies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `term-assignments-and-ordering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filterable-archive-queries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `localized-term-slugs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-collections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-collections-filament`](https://github.com/liberusoftware/module-cms-collections-filament) (`liberusoftware/cms-collections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-collections.md) · [API plan](../api/cms-collections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Custom collections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `custom collections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hierarchical and flat taxonomies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hierarchical and flat taxonomies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Term assignments and ordering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `term assignments and ordering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filterable archive queries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filterable archive queries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Localized term slugs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `localized term slugs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CollectionItemResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Filament/CollectionItemResource.php) · [CollectionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Filament/CollectionResource.php) · [ListCollectionItems.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Filament/Pages/ListCollectionItems.php) · [ListCollections.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Filament/Pages/ListCollections.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Queries/CollectionQuery.php) | `public function paginate(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function published(string $slug, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function publishedCollection(string $slug): ?Collection`<br>`public function item(string $collection, string $slug): ?CollectionItem` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CollectionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Actions/CollectionMutationService.php) | `public function create(array $attributes): Collection`<br>`public function update(Collection $collection, array $attributes): Collection`<br>`public function delete(Collection $collection): void`<br>`public function createItem(Collection $collection, array $attributes): CollectionItem`<br>`public function updateItem(CollectionItem $item, array $attributes): CollectionItem`<br>`public function deleteItem(CollectionItem $item): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Collection.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Models/Collection.php) | `name`, `slug`, `type`, `description`, `schema`, `team_id` |
| [CollectionItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-collections/src/Models/CollectionItem.php) | `title`, `slug`, `content`, `excerpt`, `data`, `metadata`, `status`, `published_at`, `collection_id`, `user_id`, `team_id` |
<!-- layer-implementation-plan:end -->
