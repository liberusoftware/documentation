# Browser Game: Browser Game World Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-world). Observed identity: [`liberusoftware/module-browser-game-world-livewire`](../../../modules/source/liberusoftware--module-browser-game-world-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-world-livewire`  
**Matching domain module:** `browser-game-world`  
**Application:** Browser Game  
**Source feature:** [Browser Game World](../features/browser-game-world.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Regions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maps:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Travel:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Encounters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **NPCs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Resources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Weather:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unlocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-world-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameWorld::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `regions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maps`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `travel`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `encounters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `npcs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `resources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `weather`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unlocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-world` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-world.md) · [API plan](../api/browser-game-world.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Regions** | Expose a focused Livewire 4 component and namespaced Blade default view for `regions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locations** | Expose a focused Livewire 4 component and namespaced Blade default view for `locations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maps** | Expose a focused Livewire 4 component and namespaced Blade default view for `maps` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Travel** | Expose a focused Livewire 4 component and namespaced Blade default view for `travel` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Encounters** | Expose a focused Livewire 4 component and namespaced Blade default view for `encounters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **NPCs** | Expose a focused Livewire 4 component and namespaced Blade default view for `npcs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Resources** | Expose a focused Livewire 4 component and namespaced Blade default view for `resources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Weather** | Expose a focused Livewire 4 component and namespaced Blade default view for `weather` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unlocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `unlocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [WorldCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-livewire/src/Livewire/WorldCatalog.php) · [WorldLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-livewire/src/WorldLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorldQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Queries/WorldQuery.php) | `public function visible(?string $tenantId, ?string $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WorldPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Policies/WorldPolicy.php) | `public function view(?string $tenantId, ?string $teamId, WorldEntity $entity): bool`<br>`public function manage(?string $actorId, ?string $tenantId, ?string $teamId, WorldEntity $entity): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldEntity.php) | `tenant_id`, `team_id`, `world_id`, `kind`, `name`, `slug`, `status`, `attributes`, `coordinates`, `unlock_key` |
| [WorldTravel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldTravel.php) | `tenant_id`, `team_id`, `actor_id`, `origin_id`, `destination_id`, `idempotency_key`, `metadata` |
| [WorldUnlock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldUnlock.php) | `tenant_id`, `team_id`, `actor_id`, `entity_id`, `unlock_key`, `status`, `metadata`, `idempotency_key`, `granted_at`, `revoked_at` |
<!-- layer-implementation-plan:end -->
