# CRM: Crm Work Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-work-management). Observed identity: [`liberusoftware/module-crm-work-management-filament`](../../../modules/source/liberusoftware--module-crm-work-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-work-management-filament`  
**Matching domain module:** `crm-work-management`  
**Application:** CRM  
**Source feature:** [Crm Work Management](../features/crm-work-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-work-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Cross-record task boards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurring work:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Checklists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workload:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Personal/team views:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-work-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `cross-record-task-boards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurring-work`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `checklists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workload`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `personal-team-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-work-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-work-management-filament`](https://github.com/liberusoftware/module-crm-work-management-filament) (`liberusoftware/crm-work-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-work-management.md) · [API plan](../api/crm-work-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Cross-record task boards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cross-record task boards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurring work** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurring work`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Checklists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `checklists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workload** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workload`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Personal/team views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personal/team views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WorkItemResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkItemResource.php) · [CreateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkItemResource/Pages/CreateWorkItem.php) · [EditWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkItemResource/Pages/EditWorkItem.php) · [ListWorkItems.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkItemResource/Pages/ListWorkItems.php) · [WorkQueueResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkQueueResource.php) · [CreateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkQueueResource/Pages/CreateWorkQueue.php) · [EditWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkQueueResource/Pages/EditWorkQueue.php) · [ListWorkQueues.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/Resources/WorkQueueResource/Pages/ListWorkQueues.php) · [WorkManagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/WorkManagementFilamentPlugin.php) · [WorkManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-filament/src/WorkManagementFilamentServiceProvider.php).

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
