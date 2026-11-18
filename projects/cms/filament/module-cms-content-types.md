# CMS: Module Cms Content Types Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-content-types). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-content-types-filament`  
**Matching domain module:** `module-cms-content-types`  
**Application:** CMS  
**Source feature:** [Module Cms Content Types](../features/module-cms-content-types.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-content-types` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Content type definitions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Typed field groups and repeaters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation and reference rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schema versioning and migrations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **API projection rules:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-content-types-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `content-type-definitions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `typed-field-groups-and-repeaters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation-and-reference-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schema-versioning-and-migrations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `api-projection-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-content-types` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-types-filament`](https://github.com/liberusoftware/module-cms-content-types-filament) (`liberusoftware/cms-content-types-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-content-types.md) · [API plan](../api/module-cms-content-types.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Content type definitions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content type definitions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Typed field groups and repeaters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `typed field groups and repeaters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation and reference rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation and reference rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schema versioning and migrations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schema versioning and migrations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **API projection rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `api projection rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentEntryResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Filament/ContentEntryResource.php) · [ContentTypeResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Filament/ContentTypeResource.php) · [ListContentEntries.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Filament/Pages/ListContentEntries.php) · [ListContentTypes.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Filament/Pages/ListContentTypes.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FieldSchemaQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Queries/FieldSchemaQuery.php) | `public function find(string $key): ?array` |
| [PublishedEntityQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Queries/PublishedEntityQuery.php) | `public function find(string $type, string $slug): ?ContentEntry`<br>`public function forType(string $type, int $perPage = 15, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentEntryMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Actions/ContentEntryMutationService.php) | `public function clone(ContentEntry $entry, ?string $title = null): ContentEntry` |
| [ContentEntryRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Contracts/ContentEntryRepositoryInterface.php) | `public function find(int $id): ?ContentEntry`<br>`public function findBySlug(string $slug): ?ContentEntry`<br>`public function ofType(string $typeKey): array`<br>`public function published(): array`<br>`public function search(string $query, int $limit): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Models/ContentEntry.php) | `content_type_id`, `title`, `slug`, `data`, `status`, `published_at`, `author_id`, `team_id` |
| [ContentType.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Models/ContentType.php) | `key`, `name`, `singular_label`, `plural_label`, `fields`, `schema_version`, `schema_history` |
<!-- layer-implementation-plan:end -->
