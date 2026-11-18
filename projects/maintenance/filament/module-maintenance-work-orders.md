# Maintenance: Module Maintenance Work Orders Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-work-orders). Observed identity: [`liberusoftware/module-maintenance-work-orders-filament`](../../../modules/source/liberusoftware--module-maintenance-work-orders-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-work-orders-filament`  
**Matching domain module:** `module-maintenance-work-orders`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Work Orders](../features/module-maintenance-work-orders.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-work-orders` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Triage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Jobs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status machine:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Completion:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-work-orders-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `triage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `jobs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status-machine`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `completion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-work-orders` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-work-orders-filament`](https://github.com/liberusoftware/module-maintenance-work-orders-filament) (`liberusoftware/maintenance-work-orders-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-work-orders.md) · [API plan](../api/module-maintenance-work-orders.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Triage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `triage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Jobs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `jobs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tasks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tasks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status machine** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status machine`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Notes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `notes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Completion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `completion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WorkOrderResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/Resources/WorkOrderResource.php) · [CreateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/Resources/WorkOrderResource/Pages/CreateWorkOrder.php) · [EditWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/Resources/WorkOrderResource/Pages/EditWorkOrder.php) · [ListWorkOrders.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/Resources/WorkOrderResource/Pages/ListWorkOrders.php) · [WorkOrdersFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/WorkOrdersFilamentPlugin.php) · [WorkOrdersFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-filament/src/WorkOrdersFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderComment.php) | `public function handle(int $teamId, WorkOrder $workOrder, int $userId, string $comment, bool $internal = false): WorkOrderComment` |
| [AddWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrder $workOrder, WorkOrder $dependsOn): WorkOrderDependency` |
| [AddWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrderEvidence` |
| [CreateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/CreateWorkOrder.php) | `public function handle(int $teamId, array $attributes): WorkOrder` |
| [DeleteWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/DeleteWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder): void` |
| [RemoveWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrderDependency $dependency): void` |
| [RemoveWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrderEvidence $evidence): void` |
| [TransitionWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/TransitionWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, string $status, ?int $actorId = null): WorkOrder` |
| [UpdateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/UpdateWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrder` |
| [WorkOrderPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Policies/WorkOrderPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, WorkOrder $order): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, WorkOrder $order): bool`<br>`public function delete(object $user, WorkOrder $order): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrder.php) | `team_id`, `number`, `title`, `description`, `location`, `equipment_id`, `customer_id`, `vendor_id`, `assigned_to`, `due_date`, `started_at`, `estimated_minutes`, `actual_minutes`, `maintenance_plan_id`, `checklist_id`, `priority`, `status`, `requested_by`, `guest_name`, `guest_email`, `guest_phone`, `submitted_at`, `reviewed_by`, `reviewed_at`, `completed_at`, `notes`, `metadata` |
| [WorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderComment.php) | `team_id`, `work_order_id`, `user_id`, `comment`, `is_internal` |
| [WorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderDependency.php) | `team_id`, `work_order_id`, `depends_on_work_order_id` |
| [WorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderEvidence.php) | `team_id`, `work_order_id`, `added_by`, `kind`, `label`, `reference`, `metadata` |
<!-- layer-implementation-plan:end -->
