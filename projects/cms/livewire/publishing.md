# CMS: Publishing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#publishing). Observed identity: [`liberusoftware/module-cms-publishing-livewire`](../../../modules/source/liberusoftware--module-cms-publishing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-publishing-livewire`  
**Matching domain module:** `cms-publishing`  
**Application:** CMS  
**Source feature:** [Publishing](../features/publishing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Immediate/scheduled publishing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Embargo:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unpublish/archive:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recurring review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Atomic release:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cache/index events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-publishing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-publishing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `immediate-scheduled-publishing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `embargo`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unpublish-archive`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recurring-review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `atomic-release`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cache-index-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-publishing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/publishing.md) · [API plan](../api/publishing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Immediate/scheduled publishing** | Expose a focused Livewire 4 component and namespaced Blade default view for `immediate/scheduled publishing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Embargo** | Expose a focused Livewire 4 component and namespaced Blade default view for `embargo` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expiry** | Expose a focused Livewire 4 component and namespaced Blade default view for `expiry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unpublish/archive** | Expose a focused Livewire 4 component and namespaced Blade default view for `unpublish/archive` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recurring review** | Expose a focused Livewire 4 component and namespaced Blade default view for `recurring review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Atomic release** | Expose a focused Livewire 4 component and namespaced Blade default view for `atomic release` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cache/index events** | Expose a focused Livewire 4 component and namespaced Blade default view for `cache/index events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReleaseMonitor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-publishing-livewire/src/Livewire/ReleaseMonitor.php) · [PublishingLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-publishing-livewire/src/PublishingLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PublishingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Services/PublishingService.php) | `public function create(array $attributes): PublicationRelease`<br>`public function schedule(PublicationRelease $release): PublicationRelease`<br>`public function publish(PublicationRelease $release): PublicationRelease`<br>`public function unpublish(PublicationRelease $release): PublicationRelease`<br>`public function archive(PublicationRelease $release): PublicationRelease`<br>`public function processDue(): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PublicationRelease.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Models/PublicationRelease.php) | `key`, `state`, `publish_at`, `embargo_until`, `expires_at`, `review_at`, `recurrence`, `targets`, `cache_tags`, `team_id` |
| [PublicationReleaseEvent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Models/PublicationReleaseEvent.php) | `release_id`, `event`, `payload`, `occurred_at` |
<!-- layer-implementation-plan:end -->
