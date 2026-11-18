# Maintenance: Module Maintenance Preventative Maintenance Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-preventative-maintenance). Observed identity: [`liberusoftware/module-maintenance-preventative-maintenance-filament`](../../../modules/source/liberusoftware--module-maintenance-preventative-maintenance-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-preventative-maintenance-filament`  
**Matching domain module:** `module-maintenance-preventative-maintenance`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Preventative Maintenance](../features/module-maintenance-preventative-maintenance.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-preventative-maintenance` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Triggers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Frequencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Meter rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forecasts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Generation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Optimization:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-preventative-maintenance-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `triggers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `frequencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `meter-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forecasts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `generation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `optimization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-preventative-maintenance` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-preventative-maintenance-filament`](https://github.com/liberusoftware/module-maintenance-preventative-maintenance-filament) (`liberusoftware/maintenance-preventative-maintenance-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-preventative-maintenance.md) · [API plan](../api/module-maintenance-preventative-maintenance.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Triggers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `triggers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Frequencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `frequencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Meter rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `meter rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forecasts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forecasts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Generation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `generation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Optimization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `optimization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PreventativeMaintenanceFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/PreventativeMaintenanceFilamentPlugin.php) · [PreventativeMaintenanceFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/PreventativeMaintenanceFilamentServiceProvider.php) · [MaintenancePlanResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/Resources/MaintenancePlanResource.php) · [CreateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/Resources/MaintenancePlanResource/Pages/CreateMaintenancePlan.php) · [EditMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/Resources/MaintenancePlanResource/Pages/EditMaintenancePlan.php) · [ListMaintenancePlans.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-filament/src/Resources/MaintenancePlanResource/Pages/ListMaintenancePlans.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CompleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, ?CarbonInterface $completedAt = null): MaintenancePlan` |
| [CreateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CreateMaintenancePlan.php) | `public function handle(int $teamId, array $attributes): MaintenancePlan` |
| [DeleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/DeleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan): void` |
| [UpdateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/UpdateMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, array $attributes): MaintenancePlan` |
| [MaintenancePlanPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Policies/MaintenancePlanPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, MaintenancePlan $plan): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, MaintenancePlan $plan): bool`<br>`public function delete(object $user, MaintenancePlan $plan): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Models/MaintenancePlan.php) | `team_id`, `name`, `code`, `description`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `frequency_unit`, `frequency_value`, `next_due_at`, `last_completed_at`, `is_active`, `rules` |
<!-- layer-implementation-plan:end -->
