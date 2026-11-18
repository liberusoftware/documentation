# Maintenance: Preventative Maintenance Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#preventative-maintenance). Observed identity: [`liberusoftware/module-maintenance-preventative-maintenance-livewire`](../../../modules/source/liberusoftware--module-maintenance-preventative-maintenance-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-preventative-maintenance-livewire`  
**Matching domain module:** `maintenance-preventative-maintenance`  
**Application:** Maintenance  
**Source feature:** [Preventative Maintenance](../features/preventative-maintenance.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Triggers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Frequencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Meter rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forecasts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Generation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Optimization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-preventative-maintenance-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-maintenance-preventative-maintenance::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `triggers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `frequencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `meter-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forecasts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `generation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `optimization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `maintenance-preventative-maintenance` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/preventative-maintenance.md) · [API plan](../api/preventative-maintenance.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Triggers** | Expose a focused Livewire 4 component and namespaced Blade default view for `triggers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Frequencies** | Expose a focused Livewire 4 component and namespaced Blade default view for `frequencies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Meter rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `meter rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Forecasts** | Expose a focused Livewire 4 component and namespaced Blade default view for `forecasts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Generation** | Expose a focused Livewire 4 component and namespaced Blade default view for `generation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Optimization** | Expose a focused Livewire 4 component and namespaced Blade default view for `optimization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MaintenancePlanList.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-livewire/src/Components/MaintenancePlanList.php) · [PreventativeMaintenanceLivewireServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-livewire/src/PreventativeMaintenanceLivewireServiceProvider.php).

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
