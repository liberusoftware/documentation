# Browser Game: Browser Game Competition Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-competition). Observed identity: [`liberusoftware/module-browser-game-competition-livewire`](../../../modules/source/liberusoftware--module-browser-game-competition-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-competition-livewire`  
**Matching domain module:** `browser-game-competition`  
**Application:** Browser Game  
**Source feature:** [Browser Game Competition](../features/browser-game-competition.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **PvP modes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Matchmaking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Seasons:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rankings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Leaderboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rewards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Anti-collusion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-competition-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameCompetition::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `pvp-modes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `matchmaking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `seasons`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rankings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `leaderboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rewards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `anti-collusion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-competition` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-competition.md) · [API plan](../api/browser-game-competition.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **PvP modes** | Expose a focused Livewire 4 component and namespaced Blade default view for `pvp modes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Matchmaking** | Expose a focused Livewire 4 component and namespaced Blade default view for `matchmaking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Seasons** | Expose a focused Livewire 4 component and namespaced Blade default view for `seasons` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rankings** | Expose a focused Livewire 4 component and namespaced Blade default view for `rankings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Leaderboards** | Expose a focused Livewire 4 component and namespaced Blade default view for `leaderboards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rewards** | Expose a focused Livewire 4 component and namespaced Blade default view for `rewards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Anti-collusion** | Expose a focused Livewire 4 component and namespaced Blade default view for `anti-collusion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CompetitionCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-livewire/src/Livewire/CompetitionCatalog.php) · [CompetitionLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-livewire/src/CompetitionLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CompetitionQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Queries/CompetitionQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CompetitionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionFlag.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionMatch.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionMatch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionReward.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionReward.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
