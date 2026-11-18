# CRM: Crm Sales Pipelines Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-pipelines). Observed identity: [`liberusoftware/module-crm-sales-pipelines-filament`](../../../modules/source/liberusoftware--module-crm-sales-pipelines-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-sales-pipelines-filament`  
**Matching domain module:** `crm-sales-pipelines`  
**Application:** CRM  
**Source feature:** [Crm Sales Pipelines](../features/crm-sales-pipelines.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sales-pipelines` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multiple pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opportunities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Values:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Probabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Close dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Competitors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stage history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rotting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Loss reasons:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-sales-pipelines-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `multiple-pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opportunities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `values`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `probabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `close-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `competitors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stage-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rotting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `loss-reasons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sales-pipelines` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-sales-pipelines-filament`](https://github.com/liberusoftware/module-crm-sales-pipelines-filament) (`liberusoftware/crm-sales-pipelines-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-sales-pipelines.md) · [API plan](../api/crm-sales-pipelines.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Multiple pipelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `multiple pipelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opportunities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opportunities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Products** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `products`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Values** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `values`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Probabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `probabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Close dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `close dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Competitors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `competitors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stage history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stage history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rotting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rotting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Loss reasons** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `loss reasons`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OpportunityResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource.php) · [CreateOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource/Pages/CreateOpportunity.php) · [EditOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource/Pages/EditOpportunity.php) · [ListOpportunities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/OpportunityResource/Pages/ListOpportunities.php) · [PipelineResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/PipelineResource.php) · [CreatePipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/PipelineResource/Pages/CreatePipeline.php) · [EditPipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/PipelineResource/Pages/EditPipeline.php) · [ListPipelines.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/PipelineResource/Pages/ListPipelines.php) · [StageResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/StageResource.php) · [CreateStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/StageResource/Pages/CreateStage.php) · [EditStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/StageResource/Pages/EditStage.php) · [ListStages.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/Resources/StageResource/Pages/ListStages.php) · [SalesPipelinesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/SalesPipelinesFilamentPlugin.php) · [SalesPipelinesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-filament/src/SalesPipelinesFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PipelineQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php) | `public function pipelines(int $teamId)`<br>`public function stages(int $teamId, int $pipelineId)`<br>`public function opportunities(int $teamId)`<br>`public function rottingOpportunities(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CloseOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, string $status, ?string $reason = null): Opportunity` |
| [CreateOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php) | `public function execute(int $teamId, int $actorId, array $data): Opportunity` |
| [CreatePipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php) | `public function execute(int $teamId, int $actorId, array $data): SalesPipeline` |
| [CreateStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php) | `public function execute(int $teamId, int $actorId, array $data): SalesStage` |
| [MoveOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): Opportunity` |
| [PipelineAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelineAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [PipelinePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Opportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/Opportunity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesPipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesPipeline.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesStage.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/StageHistory.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->

Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) for actual actions, routes, permissions, UI behavior and differences from the target design.
