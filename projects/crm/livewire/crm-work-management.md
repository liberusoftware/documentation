# CRM: Crm Work Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-work-management). Observed identity: [`liberusoftware/module-crm-work-management-livewire`](../../../modules/source/liberusoftware--module-crm-work-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-work-management-livewire`  
**Matching domain module:** `crm-work-management`  
**Application:** CRM  
**Source feature:** [Crm Work Management](../features/crm-work-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Cross-record task boards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recurring work:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Checklists:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Workload:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dependencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Personal/team views:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-work-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmWorkManagement::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `cross-record-task-boards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recurring-work`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `checklists`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `workload`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dependencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `personal-team-views`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-work-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-work-management.md) · [API plan](../api/crm-work-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Cross-record task boards** | Expose a focused Livewire 4 component and namespaced Blade default view for `cross-record task boards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recurring work** | Expose a focused Livewire 4 component and namespaced Blade default view for `recurring work` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Checklists** | Expose a focused Livewire 4 component and namespaced Blade default view for `checklists` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Workload** | Expose a focused Livewire 4 component and namespaced Blade default view for `workload` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dependencies** | Expose a focused Livewire 4 component and namespaced Blade default view for `dependencies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Personal/team views** | Expose a focused Livewire 4 component and namespaced Blade default view for `personal/team views` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [WorkBoard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-livewire/src/Components/WorkBoard.php) · [WorkManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-livewire/src/WorkManagementLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddChecklistItem.php) | `public function execute(WorkItem $item, ?int $actorId, string $title): ChecklistItem` |
| [AddDependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddDependency.php) | `public function execute(WorkItem $item, WorkItem $dependsOn, ?int $actorId): Dependency` |
| [CompleteWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CompleteWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, ?int $expectedVersion = null): WorkItem` |
| [CreateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkItem.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkItem` |
| [CreateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkQueue.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkQueue` |
| [ReviewApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/ReviewApproval.php) | `public function request(WorkItem $item, ?int $actorId, ?string $comment = null): Approval`<br>`public function review(Approval $approval, int $actorId, string $status, ?string $comment = null): Approval` |
| [UpdateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, array $attributes, ?int $expectedVersion = null): WorkItem` |
| [UpdateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkQueue.php) | `public function execute(WorkQueue $queue, ?int $actorId, array $attributes): WorkQueue` |
| [WorkAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkAudit.php) | `public function record(Model $item, ?int $actorId, string $event, array $details = []): void` |
| [WorkloadQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkloadQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Approval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Approval.php) | `work_item_id`, `team_id`, `requested_by`, `reviewed_by`, `status`, `comment`, `reviewed_at` |
| [ChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/ChecklistItem.php) | `work_item_id`, `team_id`, `actor_id`, `title`, `completed`, `position` |
| [Dependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Dependency.php) | `work_item_id`, `depends_on_id`, `team_id` |
| [WorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkItem.php) | `team_id`, `actor_id`, `assigned_to`, `queue_id`, `title`, `description`, `status`, `priority`, `subject_type`, `subject_id`, `due_at`, `recurrence`, `next_run_at`, `version`, `metadata` |
| [WorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkQueue.php) | `team_id`, `actor_id`, `name`, `description`, `status`, `rules` |
<!-- layer-implementation-plan:end -->
