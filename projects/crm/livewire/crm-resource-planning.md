# CRM: Crm Resource Planning Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-resource-planning). Observed identity: [`liberusoftware/module-crm-resource-planning-livewire`](../../../modules/source/liberusoftware--module-crm-resource-planning-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-resource-planning-livewire`  
**Matching domain module:** `crm-resource-planning`  
**Application:** CRM  
**Source feature:** [Crm Resource Planning](../features/crm-resource-planning.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Skills:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capacity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Utilization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tentative/confirmed bookings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conflicts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Staffing forecasts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-resource-planning-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmResourcePlanning::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `skills`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capacity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `utilization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tentative-confirmed-bookings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conflicts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `staffing-forecasts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-resource-planning` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-resource-planning.md) · [API plan](../api/crm-resource-planning.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Skills** | Expose a focused Livewire 4 component and namespaced Blade default view for `skills` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capacity** | Expose a focused Livewire 4 component and namespaced Blade default view for `capacity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Utilization** | Expose a focused Livewire 4 component and namespaced Blade default view for `utilization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tentative/confirmed bookings** | Expose a focused Livewire 4 component and namespaced Blade default view for `tentative/confirmed bookings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conflicts** | Expose a focused Livewire 4 component and namespaced Blade default view for `conflicts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rates** | Expose a focused Livewire 4 component and namespaced Blade default view for `rates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Staffing forecasts** | Expose a focused Livewire 4 component and namespaced Blade default view for `staffing forecasts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ResourcePlanningDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-livewire/src/Components/ResourcePlanningDashboard.php) · [ResourcePlanningLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-livewire/src/ResourcePlanningLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ResourcePlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Queries/ResourcePlanningQuery.php) | `public function skills(int $teamId)`<br>`public function capacity(int $teamId)`<br>`public function bookings(int $teamId)`<br>`public function forecasts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/CreateBooking.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceBooking` |
| [RecordForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/RecordForecast.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceForecast` |
| [SetCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetCapacity.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceCapacity` |
| [SetRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetRate.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceRate` |
| [UpsertSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/UpsertSkill.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceSkill` |
| [ResourcePlanningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Services/ResourcePlanningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ResourceBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceBooking.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceCapacity.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceForecast.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceRate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceSkill.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
