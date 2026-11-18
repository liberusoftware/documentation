# CRM: CRM Copilot Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-copilot). Observed identity: [`liberusoftware/module-crm-copilot-livewire`](../../../modules/source/liberusoftware--module-crm-copilot-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-copilot-livewire`  
**Matching domain module:** `crm-copilot`  
**Application:** CRM  
**Source feature:** [CRM Copilot](../features/crm-copilot.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Permission-bounded search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Summaries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preparation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drafting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Record updates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Task creation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Action confirmation using the Automation AI Gateway:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-copilot-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-copilot::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `permission-bounded-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `summaries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preparation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drafting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `record-updates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `task-creation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `action-confirmation-using-the-automation-ai-gateway`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-copilot` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-copilot.md) · [API plan](../api/crm-copilot.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Permission-bounded search** | Expose a focused Livewire 4 component and namespaced Blade default view for `permission-bounded search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Summaries** | Expose a focused Livewire 4 component and namespaced Blade default view for `summaries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preparation** | Expose a focused Livewire 4 component and namespaced Blade default view for `preparation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drafting** | Expose a focused Livewire 4 component and namespaced Blade default view for `drafting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Record updates** | Expose a focused Livewire 4 component and namespaced Blade default view for `record updates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Task creation** | Expose a focused Livewire 4 component and namespaced Blade default view for `task creation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Action confirmation using the Automation AI Gateway** | Expose a focused Livewire 4 component and namespaced Blade default view for `action confirmation using the automation ai gateway` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CopilotDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-livewire/src/Livewire/CopilotDashboard.php) · [CopilotLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-livewire/src/CopilotLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CopilotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Queries/CopilotQuery.php) | `public function requests(int $teamId, int $userId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AskCopilot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/AskCopilot.php) | `public function __construct(private readonly CopilotPolicy $policy, private readonly AutomationGateway $gateway)`<br>`public function execute(int $teamId, int $userId, array $input): CopilotRequest` |
| [ConfirmCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ConfirmCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotAction $action): CopilotAction` |
| [ProposeCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ProposeCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotRequest $request, array $input): CopilotAction` |
| [AutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Contracts/AutomationGateway.php) | `public function complete(string $instruction, array $context): array` |
| [CopilotPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/CopilotPolicy.php) | `public function canUse(int $teamId, int $userId): bool` |
| [NullAutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/NullAutomationGateway.php) | `public function complete(string $instruction, array $context): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CopilotRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotRequest.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
