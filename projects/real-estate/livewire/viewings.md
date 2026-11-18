# Real Estate: Viewings Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#viewings). Observed identity: [`liberusoftware/real-estate-viewings-livewire`](../../../modules/source/liberusoftware--real-estate-viewings-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-viewings-livewire`  
**Matching domain module:** `real-estate-viewings`  
**Application:** Real Estate  
**Source feature:** [Viewings](../features/viewings.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Availability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Booking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Confirmation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Accompaniment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reminders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feedback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **No-shows:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-viewings-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-real-estate-viewings::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `availability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `booking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `confirmation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `accompaniment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reminders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feedback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `no-shows`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-viewings` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/viewings.md) · [API plan](../api/viewings.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Availability** | Expose a focused Livewire 4 component and namespaced Blade default view for `availability` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Booking** | Expose a focused Livewire 4 component and namespaced Blade default view for `booking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Confirmation** | Expose a focused Livewire 4 component and namespaced Blade default view for `confirmation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access** | Expose a focused Livewire 4 component and namespaced Blade default view for `access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Accompaniment** | Expose a focused Livewire 4 component and namespaced Blade default view for `accompaniment` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reminders** | Expose a focused Livewire 4 component and namespaced Blade default view for `reminders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feedback** | Expose a focused Livewire 4 component and namespaced Blade default view for `feedback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **No-shows** | Expose a focused Livewire 4 component and namespaced Blade default view for `no-shows` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ViewingBooking.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-livewire/src/Components/ViewingBooking.php) · [ViewingList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-livewire/src/Components/ViewingList.php) · [ViewingsLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-livewire/src/ViewingsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AvailableViewingSlots.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/AvailableViewingSlots.php) | `public function handle( int\|string $teamId, int\|string\|null $propertyId, CarbonImmutable $date, int $durationMinutes = 60, ): array` |
| [ViewingCalendarExport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/ViewingCalendarExport.php) | `public function handle(Viewing\|int\|string $viewing): string` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Policies/ViewingPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Viewing $viewing): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Viewing $viewing): bool`<br>`public function delete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDelete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Viewing $viewing): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Viewing.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/Viewing.php) | No literal fillable array detected; inspect the model and API schema. |
| [ViewingFeedback.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/ViewingFeedback.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
