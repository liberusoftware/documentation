# Automation: Automation Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#automation-core). Observed identity: [`liberusoftware/automation-automation-core-filament`](../../../modules/source/liberusoftware--automation-automation-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-core-filament`  
**Matching domain module:** `automation-core`  
**Application:** Automation  
**Source feature:** [Automation Core](../features/automation-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `automation-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Workflow definitions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Triggers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **State:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Runs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Variables:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cancellation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compensation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `workflow-definitions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `triggers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `runs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `variables`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cancellation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compensation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `automation-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-automation-automation-core-filament`](https://github.com/liberusoftware/module-automation-automation-core-filament) (`liberusoftware/automation-automation-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/automation-core.md) · [API plan](../api/automation-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Workflow definitions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workflow definitions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Triggers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `triggers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **State** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Runs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `runs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Variables** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `variables`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cancellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cancellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compensation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compensation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AutomationCoreFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/AutomationCoreFilamentPlugin.php) · [AutomationCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/AutomationCoreFilamentServiceProvider.php) · [AutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/Resources/AutomationCoreResource.php) · [CreateAutomationCore.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/Resources/AutomationCoreResource/Pages/CreateAutomationCore.php) · [EditAutomationCore.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/Resources/AutomationCoreResource/Pages/EditAutomationCore.php) · [ListAutomationCore.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-filament/src/Resources/AutomationCoreResource/Pages/ListAutomationCore.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelWorkflowRun.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CancelWorkflowRun.php) | `public function execute(WorkflowRunRecord $run, string $teamId, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [CreateAutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CreateAutomationCoreResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |
| [PublishWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/PublishWorkflow.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, WorkflowDefinition $definition, ?string $actorId = null, ?string $correlationId = null): WorkflowVersion` |
| [StartWorkflowRun.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/StartWorkflowRun.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, array $variables = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [TransitionAutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/TransitionAutomationCoreResource.php) | `public function execute(AutomationCoreResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/AutomationCoreResource.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkflowRunRecord.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowRunRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkflowVersion.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowVersion.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
