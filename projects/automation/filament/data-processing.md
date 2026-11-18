# Automation: Data Processing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-processing). Observed identity: [`liberusoftware/automation-data-processing-filament`](../../../modules/source/liberusoftware--automation-data-processing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-data-processing-filament`  
**Matching domain module:** `automation-data-processing`  
**Application:** Automation  
**Source feature:** [Data Processing](../features/data-processing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `automation-data-processing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Classification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Extraction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Summarization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Translation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enrichment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redaction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Batch processing:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-data-processing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `classification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `extraction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `summarization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `translation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enrichment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redaction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `batch-processing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `automation-data-processing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-automation-data-processing-filament`](https://github.com/liberusoftware/module-automation-data-processing-filament) (`liberusoftware/automation-data-processing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/data-processing.md) · [API plan](../api/data-processing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Classification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `classification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Extraction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `extraction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Summarization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `summarization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Translation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `translation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enrichment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enrichment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redaction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redaction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Batch processing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `batch processing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DataProcessingFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/DataProcessingFilamentPlugin.php) · [DataProcessingFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/DataProcessingFilamentServiceProvider.php) · [DataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/Resources/DataProcessingResource.php) · [CreateDataProcessing.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/Resources/DataProcessingResource/Pages/CreateDataProcessing.php) · [EditDataProcessing.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/Resources/DataProcessingResource/Pages/EditDataProcessing.php) · [ListDataProcessing.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-filament/src/Resources/DataProcessingResource/Pages/ListDataProcessing.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Actions/CreateDataProcessingResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): DataProcessingResource` |
| [TransitionDataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Actions/TransitionDataProcessingResource.php) | `public function execute(DataProcessingResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): DataProcessingResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Models/DataProcessingResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
