# Accounting: Accounting Time Tracking Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-time-tracking). Observed identity: [`liberusoftware/module-accounting-time-tracking-filament`](../../../modules/source/liberusoftware--module-accounting-time-tracking-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-time-tracking-filament`  
**Matching domain module:** `accounting-time-tracking`  
**Application:** Accounting  
**Source feature:** [Accounting Time Tracking](../features/accounting-time-tracking.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-time-tracking` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Timesheets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Employees/contractors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customers/projects/tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billable/cost rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payroll/invoice export:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrections:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-time-tracking-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `timesheets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `employees-contractors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customers-projects-tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billable-cost-rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payroll-invoice-export`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-time-tracking` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-time-tracking-filament`](https://github.com/liberusoftware/module-accounting-time-tracking-filament) (`liberusoftware/accounting-time-tracking-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-time-tracking.md) · [API plan](../api/accounting-time-tracking.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Timesheets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timesheets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Employees/contractors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `employees/contractors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customers/projects/tasks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customers/projects/tasks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billable/cost rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billable/cost rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payroll/invoice export** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payroll/invoice export`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListTimeEntries.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-filament/src/Resources/Pages/ListTimeEntries.php) · [TimeEntryResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-filament/src/Resources/TimeEntryResource.php) · [TimeTrackingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-filament/src/TimeTrackingFilamentPlugin.php) · [TimeTrackingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-filament/src/TimeTrackingFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/ApproveTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/CreateTimeEntry.php) | `public function handle(array $attributes): TimeEntry` |
| [StartTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StartTimer.php) | `public function handle(array $attributes): TimeTimer` |
| [StopTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StopTimer.php) | `public function handle(TimeTimer $timer): TimeTimer` |
| [SubmitTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/SubmitTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeEntry.php) | `team_id`, `worker_ref`, `customer_ref`, `project_ref`, `task_ref`, `worked_on`, `hours`, `billable_rate`, `cost_rate`, `currency`, `billable`, `status`, `description`, `metadata` |
| [TimeExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeExport.php) | `team_id`, `destination`, `period_start`, `period_end`, `entry_count`, `status`, `exported_at`, `metadata` |
| [TimeTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeTimer.php) | `team_id`, `worker_ref`, `project_ref`, `started_at`, `stopped_at`, `status` |
<!-- layer-implementation-plan:end -->
