# CRM: Prospecting Agent Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#prospecting-agent). Observed identity: [`liberusoftware/module-crm-prospecting-agent-livewire`](../../../modules/source/liberusoftware--module-crm-prospecting-agent-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-prospecting-agent-livewire`  
**Matching domain module:** `crm-prospecting-agent`  
**Application:** CRM  
**Source feature:** [Prospecting Agent](../features/prospecting-agent.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Approved research:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Target selection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Personalization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sequence preparation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Engagement monitoring:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy-based review/dispatch:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-prospecting-agent-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-prospecting-agent::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `approved-research`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `target-selection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `personalization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sequence-preparation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `engagement-monitoring`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy-based-review-dispatch`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-prospecting-agent` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/prospecting-agent.md) · [API plan](../api/prospecting-agent.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Approved research** | Expose a focused Livewire 4 component and namespaced Blade default view for `approved research` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Target selection** | Expose a focused Livewire 4 component and namespaced Blade default view for `target selection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Personalization** | Expose a focused Livewire 4 component and namespaced Blade default view for `personalization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sequence preparation** | Expose a focused Livewire 4 component and namespaced Blade default view for `sequence preparation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Engagement monitoring** | Expose a focused Livewire 4 component and namespaced Blade default view for `engagement monitoring` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Policy-based review/dispatch** | Expose a focused Livewire 4 component and namespaced Blade default view for `policy-based review/dispatch` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProspectingAgentDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-livewire/src/Components/ProspectingAgentDashboard.php) · [ProspectingAgentLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-livewire/src/ProspectingAgentLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingAgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Queries/ProspectingAgentQuery.php) | `public function runs(int $teamId)`<br>`public function targets(int $teamId)`<br>`public function sequences(int $teamId)`<br>`public function engagements(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/ApproveAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId): AgentRun` |
| [CreateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/CreateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentRun` |
| [DispatchSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/DispatchSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $sequenceId): AgentSequence` |
| [PrepareSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/PrepareSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentSequence` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/RecordEngagement.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentEngagement` |
| [SelectTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/SelectTarget.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentTarget` |
| [UpdateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/UpdateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId, array $input): AgentRun` |
| [ProspectingAgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Services/ProspectingAgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentEngagement.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentRun.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentTarget.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
