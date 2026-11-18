# Social Network: Events Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#events). Observed identity: [`liberusoftware/module-social-network-events-livewire`](../../../modules/source/liberusoftware--module-social-network-events-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-events-livewire`  
**Matching domain module:** `social-network-events`  
**Application:** Social Network  
**Source feature:** [Events](../features/events.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invitations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attendance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capacity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reminders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Updates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-events-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-social-network-events::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invitations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attendance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capacity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reminders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `updates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-events` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/events.md) · [API plan](../api/events.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Events** | Expose a focused Livewire 4 component and namespaced Blade default view for `events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invitations** | Expose a focused Livewire 4 component and namespaced Blade default view for `invitations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attendance** | Expose a focused Livewire 4 component and namespaced Blade default view for `attendance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capacity** | Expose a focused Livewire 4 component and namespaced Blade default view for `capacity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locations** | Expose a focused Livewire 4 component and namespaced Blade default view for `locations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reminders** | Expose a focused Livewire 4 component and namespaced Blade default view for `reminders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Updates** | Expose a focused Livewire 4 component and namespaced Blade default view for `updates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Creator.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-livewire/src/Components/Creator.php) · [EventsLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-livewire/src/EventsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/AddEventUpdate.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, string $body): EventUpdate` |
| [CreateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/CreateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, array $data): Event` |
| [InviteProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/InviteProfile.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $owner, Event $event, Profile $invitee): Invitation` |
| [ListEvents.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ListEvents.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/PublishEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event): Event` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ScheduleReminder.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $sendAt): EventReminder` |
| [SetAttendance.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/SetAttendance.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $state): void` |
| [UpdateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/UpdateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, array $data): Event` |
| [EventsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Contracts/EventsAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function manage(Profile $owner, Event $event): void`<br>`public function attend(Profile $profile, Event $event): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Event.php) | `id`, `owner_profile_id`, `state`, `visibility`, `timezone`, `title`, `description`, `starts_at`, `ends_at`, `capacity`, `location`, `metadata` |
| [EventReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventReminder.php) | `event_id`, `profile_id`, `send_at`, `sent_at` |
| [EventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventUpdate.php) | `event_id`, `author_profile_id`, `body` |
| [Invitation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Invitation.php) | `event_id`, `profile_id`, `state` |
<!-- layer-implementation-plan:end -->
