# Browser Game: Browser Game Combat Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-combat). Observed identity: [`liberusoftware/module-browser-game-combat-livewire`](../../../modules/source/liberusoftware--module-browser-game-combat-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-combat-livewire`  
**Matching domain module:** `browser-game-combat`  
**Application:** Browser Game  
**Source feature:** [Browser Game Combat](../features/browser-game-combat.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Turn/action rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Abilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Effects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cooldowns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Enemies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bosses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Loot:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Logs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Simulation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-combat-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameCombat::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `turn-action-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `abilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `effects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cooldowns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `enemies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bosses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `loot`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `logs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `simulation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-combat` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-combat.md) · [API plan](../api/browser-game-combat.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Turn/action rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `turn/action rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Abilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `abilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Effects** | Expose a focused Livewire 4 component and namespaced Blade default view for `effects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cooldowns** | Expose a focused Livewire 4 component and namespaced Blade default view for `cooldowns` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Enemies** | Expose a focused Livewire 4 component and namespaced Blade default view for `enemies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bosses** | Expose a focused Livewire 4 component and namespaced Blade default view for `bosses` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Loot** | Expose a focused Livewire 4 component and namespaced Blade default view for `loot` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Logs** | Expose a focused Livewire 4 component and namespaced Blade default view for `logs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Simulation** | Expose a focused Livewire 4 component and namespaced Blade default view for `simulation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CombatPanel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-livewire/src/Livewire/CombatPanel.php) · [CombatLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-livewire/src/CombatLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CombatQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Queries/CombatQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CombatPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Policies/CombatPolicy.php) | `public function view(mixed $user, CombatBattle $battle): bool`<br>`public function act(mixed $user, CombatBattle $battle): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CombatAction.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatBattle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
