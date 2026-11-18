# CMS: WordPress Migration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#wordpress-migration). Observed identity: [`liberusoftware/module-cms-wordpress-migration-filament`](../../../modules/source/liberusoftware--module-cms-wordpress-migration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-wordpress-migration-filament`  
**Matching domain module:** `cms-wordpress-migration`  
**Application:** CMS  
**Source feature:** [WordPress Migration](../features/wordpress-migration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-wordpress-migration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Posts/pages/custom types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxonomies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Users/authors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Media:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Menus:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source identifiers:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-wordpress-migration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `posts-pages-custom-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxonomies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `users-authors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `media`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `menus`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-identifiers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-wordpress-migration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-wordpress-migration-filament`](https://github.com/liberusoftware/module-cms-wordpress-migration-filament) (`liberusoftware/cms-wordpress-migration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/wordpress-migration.md) · [API plan](../api/wordpress-migration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Posts/pages/custom types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posts/pages/custom types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Taxonomies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `taxonomies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Users/authors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `users/authors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Comments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `comments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Media** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `media`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Menus** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `menus`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source identifiers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source identifiers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListWordPressMigrations.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-wordpress-migration-filament/src/Resources/Pages/ListWordPressMigrations.php) · [WordPressMigrationResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-wordpress-migration-filament/src/Resources/WordPressMigrationResource.php) · [WordPressMigrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-wordpress-migration-filament/src/WordPressMigrationFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WordPressMigrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Queries/WordPressMigrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function migrations(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function migration(int\|string $id, ?int $teamId = null): ?WordPressMigration`<br>`public function migrationByPublicId(string $publicId, ?int $teamId = null): ?WordPressMigration`<br>`public function records(WordPressMigration $migration, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WordPressImporterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Contracts/WordPressImporterInterface.php) | `public function records(WordPressMigration $migration): iterable` |
| [WordPressMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Services/WordPressMigrationService.php) | `public function start(?string $sourceUrl = null, array $options = [], ?int $teamId = null): WordPressMigration`<br>`public function addRecord(WordPressMigration $migration, string $recordType, string $sourceId, array $payload = [], array $sourceIdentifiers = [], ?string $sourceParentId = null): WordPressMigrationRecord`<br>`public function processRecord(WordPressMigrationRecord $record, bool $success = true, ?string $failureReason = null): WordPressMigrationRecord`<br>`public function complete(WordPressMigration $migration): WordPressMigration`<br>`public function fail(WordPressMigration $migration, string $reason): WordPressMigration` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WordPressMigration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigration.php) | `public_id`, `source_url`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `metadata`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [WordPressMigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigrationRecord.php) | `migration_id`, `record_type`, `source_id`, `source_parent_id`, `status`, `payload`, `source_identifiers`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
