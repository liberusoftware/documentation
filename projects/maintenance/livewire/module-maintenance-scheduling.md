# Maintenance: Module Maintenance Scheduling Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-scheduling). Observed identity: [`liberusoftware/module-maintenance-scheduling-livewire`](../../../modules/source/liberusoftware--module-maintenance-scheduling-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-module-maintenance-scheduling-livewire`  
**Matching domain module:** `module-maintenance-scheduling`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Scheduling](../features/module-maintenance-scheduling.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Calendars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Skills:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Territories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shifts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Availability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Travel:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dispatch:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conflict handling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-module-maintenance-scheduling-livewire` component namespace and service provider; use explicit aliases such as `<livewire:maintenanceModuleMaintenanceScheduling::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `calendars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `skills`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `territories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shifts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `availability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `travel`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dispatch`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conflict-handling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-maintenance-scheduling` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-maintenance-scheduling.md) · [API plan](../api/module-maintenance-scheduling.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Calendars** | Expose a focused Livewire 4 component and namespaced Blade default view for `calendars` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Skills** | Expose a focused Livewire 4 component and namespaced Blade default view for `skills` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Territories** | Expose a focused Livewire 4 component and namespaced Blade default view for `territories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shifts** | Expose a focused Livewire 4 component and namespaced Blade default view for `shifts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Availability** | Expose a focused Livewire 4 component and namespaced Blade default view for `availability` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Travel** | Expose a focused Livewire 4 component and namespaced Blade default view for `travel` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dispatch** | Expose a focused Livewire 4 component and namespaced Blade default view for `dispatch` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conflict handling** | Expose a focused Livewire 4 component and namespaced Blade default view for `conflict handling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ScheduleList.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-livewire/src/Components/ScheduleList.php) · [SchedulingLivewireServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-livewire/src/SchedulingLivewireServiceProvider.php).

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
