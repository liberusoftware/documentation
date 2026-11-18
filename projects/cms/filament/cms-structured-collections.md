# CMS: Cms Structured Collections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-structured-collections). Observed identity: [`liberusoftware/module-cms-structured-collections-filament`](../../../modules/source/liberusoftware--module-cms-structured-collections-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-structured-collections-filament`  
**Matching domain module:** `cms-structured-collections`  
**Application:** CMS  
**Source feature:** [Cms Structured Collections](../features/cms-structured-collections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-structured-collections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reusable records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Directories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **FAQs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Testimonials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Datasets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Custom collection types:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-structured-collections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reusable-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `directories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `faqs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `testimonials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `datasets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `custom-collection-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-structured-collections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-structured-collections-filament`](https://github.com/liberusoftware/module-cms-structured-collections-filament) (`liberusoftware/cms-structured-collections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-structured-collections.md) · [API plan](../api/cms-structured-collections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reusable records** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reusable records`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Directories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `directories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **FAQs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `faqs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Testimonials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `testimonials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Datasets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `datasets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Custom collection types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `custom collection types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListStructuredCollectionRecords.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-filament/src/Resources/Pages/ListStructuredCollectionRecords.php) · [ListStructuredCollections.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-filament/src/Resources/Pages/ListStructuredCollections.php) · [StructuredCollectionRecordResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-filament/src/Resources/StructuredCollectionRecordResource.php) · [StructuredCollectionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-filament/src/Resources/StructuredCollectionResource.php) · [StructuredCollectionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-filament/src/StructuredCollectionsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [StructuredCollectionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Queries/StructuredCollectionQuery.php) | `public function __construct(private CollectionQuery $legacy)`<br>`public function paginate(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function collection(string $slug): ?Collection`<br>`public function records(string $slug, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function record(string $collection, string $slug): ?CollectionItem`<br>`public function recordForMutation(string $collection, string $slug): ?CollectionItem` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [StructuredCollectionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Actions/StructuredCollectionMutationService.php) | `public function __construct(private CollectionMutationService $legacy)`<br>`public function create(array $attributes): Collection`<br>`public function update(Collection $collection, array $attributes): Collection`<br>`public function delete(Collection $collection): void`<br>`public function createRecord(Collection $collection, array $attributes): CollectionItem`<br>`public function updateRecord(CollectionItem $record, array $attributes): CollectionItem`<br>`public function deleteRecord(CollectionItem $record): void` |
<!-- layer-implementation-plan:end -->
