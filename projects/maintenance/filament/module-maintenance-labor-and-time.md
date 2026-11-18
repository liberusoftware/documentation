# Maintenance: Module Maintenance Labor And Time Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-labor-and-time). Observed identity: [`liberusoftware/module-maintenance-labor-and-time-filament`](../../../modules/source/liberusoftware--module-maintenance-labor-and-time-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-labor-and-time-filament`  
**Matching domain module:** `module-maintenance-labor-and-time`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Labor And Time](../features/module-maintenance-labor-and-time.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-labor-and-time` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Engineer skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attendance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Time entries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expenses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-labor-and-time-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `engineer-skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attendance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `time-entries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expenses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-labor-and-time` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-labor-and-time-filament`](https://github.com/liberusoftware/module-maintenance-labor-and-time-filament) (`liberusoftware/maintenance-labor-and-time-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-labor-and-time.md) · [API plan](../api/module-maintenance-labor-and-time.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Engineer skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `engineer skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attendance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attendance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Time entries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `time entries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expenses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expenses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LaborAndTimeFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/LaborAndTimeFilamentPlugin.php) · [LaborAndTimeFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/LaborAndTimeFilamentServiceProvider.php) · [TimeEntryResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/Resources/TimeEntryResource.php) · [CreateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/Resources/TimeEntryResource/Pages/CreateTimeEntry.php) · [EditTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/Resources/TimeEntryResource/Pages/EditTimeEntry.php) · [ListTimeEntries.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-filament/src/Resources/TimeEntryResource/Pages/ListTimeEntries.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/ApproveTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/CreateTimeEntry.php) | `public function handle(int $teamId, array $attributes): TimeEntry` |
| [DeleteTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/DeleteTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry): void` |
| [RejectTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/RejectTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId, ?string $reason = null): TimeEntry` |
| [UpdateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/UpdateTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, array $attributes): TimeEntry` |
| [TimeEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Policies/TimeEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, TimeEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, TimeEntry $entry): bool`<br>`public function delete(object $user, TimeEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Models/TimeEntry.php) | `team_id`, `user_id`, `work_order_id`, `description`, `started_at`, `ended_at`, `minutes`, `rate`, `status`, `expense_amount`, `currency` |
<!-- layer-implementation-plan:end -->
