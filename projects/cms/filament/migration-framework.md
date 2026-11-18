# CMS: Migration Framework Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). Observed identity: [`liberusoftware/module-cms-migration-framework-filament`](../../../modules/source/liberusoftware--module-cms-migration-framework-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-migration-framework-filament`  
**Matching domain module:** `cms-migration-framework`  
**Application:** CMS  
**Source feature:** [Migration Framework](../features/migration-framework.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-migration-framework` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Source adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inventories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dry run:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transforms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity/media/link resolution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Batches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resume:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-migration-framework-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `source-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inventories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dry-run`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transforms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-media-link-resolution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `batches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resume`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-migration-framework` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-migration-framework-filament`](https://github.com/liberusoftware/module-cms-migration-framework-filament) (`liberusoftware/cms-migration-framework-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/migration-framework.md) · [API plan](../api/migration-framework.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Source adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inventories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inventories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mapping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mapping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dry run** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dry run`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transforms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transforms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identity/media/link resolution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identity/media/link resolution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Batches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `batches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resume** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resume`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MigrationFrameworkFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-migration-framework-filament/src/MigrationFrameworkFilamentServiceProvider.php) · [MigrationJobResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-migration-framework-filament/src/Resources/MigrationJobResource.php) · [ListMigrationJobs.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-migration-framework-filament/src/Resources/Pages/ListMigrationJobs.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MigrationFrameworkService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Services/MigrationFrameworkService.php) | `public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $recordType, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $failureReason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationJob.php) | `public_id`, `source`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [MigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationRecord.php) | `job_id`, `record_type`, `source_id`, `status`, `payload`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
