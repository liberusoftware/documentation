# CRM: Business Process Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#business-process-management). Observed identity: [`liberusoftware/module-crm-business-process-management-livewire`](../../../modules/source/liberusoftware--module-crm-business-process-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-business-process-management-livewire`  
**Matching domain module:** `crm-business-process-management`  
**Application:** CRM  
**Source feature:** [Business Process Management](../features/business-process-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Guided stages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Required steps/data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Validations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Service processes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exception routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Process versioning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-business-process-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-business-process-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `guided-stages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `required-steps-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `validations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `service-processes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exception-routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `process-versioning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-business-process-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/business-process-management.md) · [API plan](../api/business-process-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Guided stages** | Expose a focused Livewire 4 component and namespaced Blade default view for `guided stages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Required steps/data** | Expose a focused Livewire 4 component and namespaced Blade default view for `required steps/data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Validations** | Expose a focused Livewire 4 component and namespaced Blade default view for `validations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Service processes** | Expose a focused Livewire 4 component and namespaced Blade default view for `service processes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exception routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `exception routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Process versioning** | Expose a focused Livewire 4 component and namespaced Blade default view for `process versioning` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BusinessProcessManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-livewire/src/BusinessProcessManagementLivewireServiceProvider.php) · [ProcessBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-livewire/src/Components/ProcessBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProcessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Queries/ProcessQuery.php) | `public function processes(int $teamId): Builder`<br>`public function runs(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/AdvanceProcess.php) | `public function execute(int $teamId, int $actorId, ProcessRun $run, array $context = []): ProcessRun` |
| [CreateProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/CreateProcess.php) | `public function execute(int $teamId, int $ownerId, array $input): Process` |
| [PublishProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/PublishProcess.php) | `public function execute(int $teamId, int $actorId, Process $process): Process` |
| [StartProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/StartProcess.php) | `public function execute(int $teamId, int $actorId, Process $process, array $context = []): ProcessRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Process.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/Process.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessRun.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
