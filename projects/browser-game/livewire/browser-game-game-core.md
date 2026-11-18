# Browser Game: Browser Game Game Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-game-core). Observed identity: [`liberusoftware/module-browser-game-game-core-livewire`](../../../modules/source/liberusoftware--module-browser-game-game-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-game-core-livewire`  
**Matching domain module:** `browser-game-game-core`  
**Application:** Browser Game  
**Source feature:** [Browser Game Game Core](../features/browser-game-game-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Worlds/shards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Game clock:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rulesets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Content versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feature flags:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maintenance state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-game-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameGameCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `worlds-shards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `game-clock`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rulesets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `content-versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feature-flags`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maintenance-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-game-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-game-core.md) · [API plan](../api/browser-game-game-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Worlds/shards** | Expose a focused Livewire 4 component and namespaced Blade default view for `worlds/shards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Game clock** | Expose a focused Livewire 4 component and namespaced Blade default view for `game clock` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rulesets** | Expose a focused Livewire 4 component and namespaced Blade default view for `rulesets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Content versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `content versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feature flags** | Expose a focused Livewire 4 component and namespaced Blade default view for `feature flags` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maintenance state** | Expose a focused Livewire 4 component and namespaced Blade default view for `maintenance state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [WorldOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-livewire/src/Livewire/WorldOverview.php) · [GameCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-livewire/src/GameCoreLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GameCoreOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Queries/GameCoreOverview.php) | `public function forWorld(GameCoreContext $context, string $worldId): array`<br>`public function enabledFlags(?string $worldId = null): Collection`<br>`public function isEnabled(GameCoreContext $context, ?GameWorld $world, string $key, array $attributes = []): bool`<br>`public function enabledFor(GameCoreContext $context, ?GameWorld $world, array $attributes = []): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Contracts/GameCoreContext.php) | `public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [GameCorePolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Policies/GameCorePolicy.php) | `public function view(GameCoreContext $context, GameWorld $world): bool`<br>`public function manage(GameCoreContext $context, GameWorld $world): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GameClock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameClock.php) | `world_id`, `current_at`, `speed`, `paused`, `updated_by` |
| [GameContentVersion.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameContentVersion.php) | `world_id`, `version`, `status`, `content_hash`, `manifest`, `published_at`, `published_by` |
| [GameFeatureFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameFeatureFlag.php) | `world_id`, `key`, `enabled`, `rollout_percentage`, `constraints`, `changed_by` |
| [GameMaintenanceState.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameMaintenanceState.php) | `world_id`, `status`, `message`, `starts_at`, `ends_at`, `changed_by` |
| [GameRuleset.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameRuleset.php) | `world_id`, `version`, `status`, `rules`, `published_at`, `published_by` |
| [GameWorld.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameWorld.php) | `tenant_id`, `team_id`, `name`, `slug`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
