# Genealogy: Genealogy Places Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-places). Observed identity: [`liberusoftware/module-genealogy-places-livewire`](../../../modules/source/liberusoftware--module-genealogy-places-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-genealogy-places-livewire`  
**Matching domain module:** `genealogy-places`  
**Application:** Genealogy  
**Source feature:** [Genealogy Places](../features/genealogy-places.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Historical/current place hierarchy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Names over time:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Coordinates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Jurisdictions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maps:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-genealogy-places-livewire` component namespace and service provider; use explicit aliases such as `<livewire:genealogyGenealogyPlaces::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `historical-current-place-hierarchy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `names-over-time`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `coordinates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `jurisdictions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maps`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-places` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/genealogy-places.md) · [API plan](../api/genealogy-places.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Historical/current place hierarchy** | Expose a focused Livewire 4 component and namespaced Blade default view for `historical/current place hierarchy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Names over time** | Expose a focused Livewire 4 component and namespaced Blade default view for `names over time` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Coordinates** | Expose a focused Livewire 4 component and namespaced Blade default view for `coordinates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Jurisdictions** | Expose a focused Livewire 4 component and namespaced Blade default view for `jurisdictions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maps** | Expose a focused Livewire 4 component and namespaced Blade default view for `maps` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PlacesLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places-livewire/src/PlacesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PlaceHierarchy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Queries/PlaceHierarchy.php) | `public function execute(bool $flat = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/CreatePlace.php) | `public function execute(array $attributes): Place`<br>`public function validate(array $values): void` |
| [CreatePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/CreatePlaceName.php) | `public function execute(array $attributes): PlaceName`<br>`public function validate(array $values): void` |
| [DeletePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/DeletePlace.php) | `public function execute(Place $place): void` |
| [DeletePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/DeletePlaceName.php) | `public function execute(PlaceName $placeName): void` |
| [UpdatePlace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/UpdatePlace.php) | `public function execute(Place $place, array $attributes): Place` |
| [UpdatePlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Actions/UpdatePlaceName.php) | `public function execute(PlaceName $placeName, array $attributes): PlaceName` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Place.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Models/Place.php) | `team_id`, `name`, `parent_id`, `historical_names`, `latitude`, `longitude`, `jurisdiction`, `is_current`, `status`, `metadata` |
| [PlaceName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-places/src/Models/PlaceName.php) | `team_id`, `place_id`, `name`, `type`, `locale`, `valid_from`, `valid_to`, `metadata` |
<!-- layer-implementation-plan:end -->
