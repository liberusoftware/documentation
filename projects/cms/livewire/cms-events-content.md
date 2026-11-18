# CMS: Cms Events Content Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-events-content). Observed identity: [`liberusoftware/module-cms-events-content-livewire`](../../../modules/source/liberusoftware--module-cms-events-content-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-events-content-livewire`  
**Matching domain module:** `cms-events-content`  
**Application:** CMS  
**Source feature:** [Cms Events Content](../features/cms-events-content.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Event/session/speaker/venue content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calendars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Registration-provider references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Archives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Structured data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-events-content-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsEventsContent::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `event-session-speaker-venue-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calendars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `registration-provider-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `archives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `structured-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-events-content` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-events-content.md) · [API plan](../api/cms-events-content.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Event/session/speaker/venue content** | Expose a focused Livewire 4 component and namespaced Blade default view for `event/session/speaker/venue content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calendars** | Expose a focused Livewire 4 component and namespaced Blade default view for `calendars` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Registration-provider references** | Expose a focused Livewire 4 component and namespaced Blade default view for `registration-provider references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Archives** | Expose a focused Livewire 4 component and namespaced Blade default view for `archives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Structured data** | Expose a focused Livewire 4 component and namespaced Blade default view for `structured data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EventCalendar.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-events-content-livewire/src/Livewire/EventCalendar.php) · [EventsContentLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-events-content-livewire/src/EventsContentLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EventsContentQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Queries/EventsContentQuery.php) | `public function calendar(int $perPage = 15, string $search = '', bool $includeArchived = false): LengthAwarePaginator`<br>`public function find(string $key): ?Event` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [EventsContentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Services/EventsContentService.php) | `public function speaker(array $attributes, ?int $teamId = null): Speaker`<br>`public function venue(array $attributes, ?int $teamId = null): Venue`<br>`public function event(array $attributes, ?int $teamId = null): Event`<br>`public function session(Event $event, array $attributes): Session`<br>`public function registration(Event $event, array $attributes): RegistrationReference`<br>`public function publish(Event $event): Event`<br>`public function archive(Event $event): Event`<br>`public function structuredData(Event $event): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Event.php) | `key`, `title`, `description`, `status`, `timezone`, `starts_at`, `ends_at`, `archived_at`, `structured_data`, `venue_id`, `team_id` |
| [RegistrationReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/RegistrationReference.php) | `event_id`, `provider`, `external_key`, `url`, `status`, `metadata` |
| [Session.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Session.php) | `event_id`, `key`, `title`, `description`, `starts_at`, `ends_at`, `room` |
| [Speaker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Speaker.php) | `name`, `bio`, `email`, `metadata`, `team_id` |
| [Venue.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Venue.php) | `name`, `address`, `timezone`, `latitude`, `longitude`, `team_id` |
<!-- layer-implementation-plan:end -->
