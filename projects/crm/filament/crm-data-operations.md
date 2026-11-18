# CRM: Crm Data Operations Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-data-operations). Observed identity: [`liberusoftware/module-crm-data-operations-filament`](../../../modules/source/liberusoftware--module-crm-data-operations-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-data-operations-filament`  
**Matching domain module:** `crm-data-operations`  
**Application:** CRM  
**Source feature:** [Crm Data Operations](../features/crm-data-operations.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-data-operations` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Imports/exports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Field mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Normalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enrichment orchestration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate detection/merge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Formatting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exception queues:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-data-operations-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `imports-exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `field-mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `normalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enrichment-orchestration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-detection-merge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `formatting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exception-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-data-operations` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-data-operations-filament`](https://github.com/liberusoftware/module-crm-data-operations-filament) (`liberusoftware/crm-data-operations-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-data-operations.md) · [API plan](../api/crm-data-operations.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Imports/exports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `imports/exports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Field mapping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `field mapping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Normalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `normalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enrichment orchestration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enrichment orchestration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate detection/merge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate detection/merge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Formatting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `formatting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exception queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exception queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DataOperationsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/DataOperationsFilamentPlugin.php) · [DataOperationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/DataOperationsFilamentServiceProvider.php) · [DataOperationResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/Resources/DataOperationResource.php) · [CreateDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/Resources/DataOperationResource/Pages/CreateDataOperation.php) · [EditDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/Resources/DataOperationResource/Pages/EditDataOperation.php) · [ListDataOperations.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-filament/src/Resources/DataOperationResource/Pages/ListDataOperations.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/CreateDataOperation.php) | `public function execute(int $teamId, ?int $actorId, array $attributes, array $mappings = []): DataOperation` |
| [ResolveException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/ResolveException.php) | `public function execute(OperationException $exception, int $actorId): OperationException` |
| [TransitionDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/TransitionDataOperation.php) | `public function execute(DataOperation $operation, string $status, ?string $reason = null): DataOperation` |
| [DataOperationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Services/DataOperationService.php) | `public function mapAndNormalize(array $row, array $mapping): array`<br>`public function duplicateConfidence(array $left, array $right, array $fields): float` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DataOperation.php) | `team_id`, `actor_id`, `kind`, `status`, `source`, `target`, `options`, `total_rows`, `processed_rows`, `failed_rows`, `failure_reason`, `started_at`, `completed_at` |
| [DuplicateMatch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DuplicateMatch.php) | `team_id`, `operation_id`, `left_record_id`, `right_record_id`, `confidence`, `status` |
| [FieldMapping.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/FieldMapping.php) | `operation_id`, `source_field`, `target_field`, `transform`, `required` |
| [OperationException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationException.php) | `team_id`, `operation_id`, `row_number`, `payload`, `reason`, `status`, `resolved_by`, `resolved_at` |
| [OperationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationRule.php) | `team_id`, `name`, `kind`, `definition`, `active` |
| [OperationSchedule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationSchedule.php) | `team_id`, `operation_id`, `cron`, `timezone`, `active`, `next_run_at` |
<!-- layer-implementation-plan:end -->
