# CRM: Events and Webinars Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#events-and-webinars). Observed identity: [`liberusoftware/module-crm-events-and-webinars-livewire`](../../../modules/source/liberusoftware--module-crm-events-and-webinars-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-events-and-webinars-livewire`  
**Matching domain module:** `crm-events-and-webinars`  
**Application:** CRM  
**Source feature:** [Events and Webinars](../features/events-and-webinars.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Physical/virtual events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Registration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capacity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tickets/attendance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sessions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Speakers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reminders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Check-in:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recording links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Follow-up:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-events-and-webinars-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-events-and-webinars::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `physical-virtual-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `registration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capacity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tickets-attendance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sessions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `speakers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reminders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `check-in`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recording-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `follow-up`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-events-and-webinars` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/events-and-webinars.md) · [API plan](../api/events-and-webinars.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Physical/virtual events** | Expose a focused Livewire 4 component and namespaced Blade default view for `physical/virtual events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Registration** | Expose a focused Livewire 4 component and namespaced Blade default view for `registration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capacity** | Expose a focused Livewire 4 component and namespaced Blade default view for `capacity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tickets/attendance** | Expose a focused Livewire 4 component and namespaced Blade default view for `tickets/attendance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sessions** | Expose a focused Livewire 4 component and namespaced Blade default view for `sessions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Speakers** | Expose a focused Livewire 4 component and namespaced Blade default view for `speakers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reminders** | Expose a focused Livewire 4 component and namespaced Blade default view for `reminders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Check-in** | Expose a focused Livewire 4 component and namespaced Blade default view for `check-in` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recording links** | Expose a focused Livewire 4 component and namespaced Blade default view for `recording links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Follow-up** | Expose a focused Livewire 4 component and namespaced Blade default view for `follow-up` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EventsDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-livewire/src/Livewire/EventsDashboard.php) · [EventsAndWebinarsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-livewire/src/EventsAndWebinarsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EventQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Queries/EventQuery.php) | `public function events(int $teamId)`<br>`public function sessions(int $teamId, int $eventId)`<br>`public function attendance(int $teamId, int $eventId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckInAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CheckInAttendee.php) | `public function execute(int $teamId, EventRegistration $registration): EventRegistration` |
| [CreateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CreateEvent.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CrmEvent` |
| [RecordEventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RecordEventFollowUp.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CrmEvent $event, array $input): EventFollowUp` |
| [RegisterAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RegisterAttendee.php) | `public function execute(int $teamId, CrmEvent $event, array $input): EventRegistration` |
| [EventPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Services/EventPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CrmEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/CrmEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventSession.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
