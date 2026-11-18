# Maintenance: Scheduling Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#scheduling). Observed identity: [`liberusoftware/module-maintenance-scheduling-filament`](../../../modules/source/liberusoftware--module-maintenance-scheduling-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-scheduling-filament`  
**Matching domain module:** `maintenance-scheduling`  
**Application:** Maintenance  
**Source feature:** [Scheduling](../features/scheduling.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `maintenance-scheduling` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shifts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Availability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Travel:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dispatch:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflict handling:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-scheduling-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shifts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `availability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `travel`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dispatch`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflict-handling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `maintenance-scheduling` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-scheduling-filament`](https://github.com/liberusoftware/module-maintenance-scheduling-filament) (`liberusoftware/maintenance-scheduling-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/scheduling.md) · [API plan](../api/scheduling.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Calendars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calendars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Territories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `territories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shifts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shifts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Availability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `availability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Travel** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `travel`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dispatch** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dispatch`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conflict handling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conflict handling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ScheduleEntryResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/Resources/ScheduleEntryResource.php) · [CreateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/Resources/ScheduleEntryResource/Pages/CreateScheduleEntry.php) · [EditScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/Resources/ScheduleEntryResource/Pages/EditScheduleEntry.php) · [ListScheduleEntries.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/Resources/ScheduleEntryResource/Pages/ListScheduleEntries.php) · [SchedulingFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/SchedulingFilamentPlugin.php) · [SchedulingFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-filament/src/SchedulingFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/CreateScheduleEntry.php) | `public function handle(int $teamId, array $attributes): ScheduleEntry` |
| [DeleteScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/DeleteScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry): void` |
| [TransitionScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/TransitionScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, string $status): ScheduleEntry` |
| [UpdateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/UpdateScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, array $attributes): ScheduleEntry` |
| [ScheduleEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Policies/ScheduleEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ScheduleEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ScheduleEntry $entry): bool`<br>`public function delete(object $user, ScheduleEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Models/ScheduleEntry.php) | `team_id`, `title`, `description`, `resource_key`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `starts_at`, `ends_at`, `status`, `territory`, `metadata`, `recurrence_type`, `recurrence_value`, `next_due_at`, `last_completed_at`, `priority` |
<!-- layer-implementation-plan:end -->
