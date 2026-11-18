# Automation: Module Automation Automation Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-automation-automation-core). Observed identity: [`liberusoftware/automation-automation-core-livewire`](../../../modules/source/liberusoftware--automation-automation-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-automation-module-automation-automation-core-livewire`  
**Matching domain module:** `module-automation-automation-core`  
**Application:** Automation  
**Source feature:** [Module Automation Automation Core](../features/module-automation-automation-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Workflow definitions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Triggers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **State:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Runs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Variables:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cancellation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compensation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-automation-module-automation-automation-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:automationModuleAutomationAutomationCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `workflow-definitions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `triggers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `runs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `variables`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cancellation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compensation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-automation-automation-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-automation-automation-core.md) · [API plan](../api/module-automation-automation-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Workflow definitions** | Expose a focused Livewire 4 component and namespaced Blade default view for `workflow definitions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Triggers** | Expose a focused Livewire 4 component and namespaced Blade default view for `triggers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **State** | Expose a focused Livewire 4 component and namespaced Blade default view for `state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Runs** | Expose a focused Livewire 4 component and namespaced Blade default view for `runs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Variables** | Expose a focused Livewire 4 component and namespaced Blade default view for `variables` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retries** | Expose a focused Livewire 4 component and namespaced Blade default view for `retries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cancellation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cancellation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Compensation** | Expose a focused Livewire 4 component and namespaced Blade default view for `compensation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AutomationCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-livewire/src/AutomationCoreLivewireServiceProvider.php).

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
