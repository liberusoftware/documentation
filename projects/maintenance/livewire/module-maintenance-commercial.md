# Maintenance: Module Maintenance Commercial Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-commercial). Observed identity: [`liberusoftware/module-maintenance-commercial-livewire`](../../../modules/source/liberusoftware--module-maintenance-commercial-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-module-maintenance-commercial-livewire`  
**Matching domain module:** `module-maintenance-commercial`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Commercial](../features/module-maintenance-commercial.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Quotes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Covered assets/services:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Renewals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SLA:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Billable lines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-module-maintenance-commercial-livewire` component namespace and service provider; use explicit aliases such as `<livewire:maintenanceModuleMaintenanceCommercial::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `quotes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `covered-assets-services`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `renewals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sla`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `billable-lines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-maintenance-commercial` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-maintenance-commercial.md) · [API plan](../api/module-maintenance-commercial.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Quotes** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Covered assets/services** | Expose a focused Livewire 4 component and namespaced Blade default view for `covered assets/services` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rates** | Expose a focused Livewire 4 component and namespaced Blade default view for `rates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Renewals** | Expose a focused Livewire 4 component and namespaced Blade default view for `renewals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SLA** | Expose a focused Livewire 4 component and namespaced Blade default view for `sla` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Billable lines** | Expose a focused Livewire 4 component and namespaced Blade default view for `billable lines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CommercialLivewireServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-livewire/src/CommercialLivewireServiceProvider.php) · [CommercialList.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-livewire/src/Components/CommercialList.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/CreateCommercialRecord.php) | `public function handle(int $teamId, array $attributes): CommercialRecord` |
| [DeleteCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/DeleteCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record): void` |
| [TransitionCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/TransitionCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, string $status): CommercialRecord` |
| [UpdateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/UpdateCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, array $attributes): CommercialRecord` |
| [CommercialRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Policies/CommercialRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CommercialRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CommercialRecord $record): bool`<br>`public function delete(object $user, CommercialRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Models/CommercialRecord.php) | `kind`, `title`, `description`, `amount`, `currency`, `status`, `metadata`, `team_id` |
<!-- layer-implementation-plan:end -->
