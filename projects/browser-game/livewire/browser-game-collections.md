# Browser Game: Browser Game Collections Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-collections). Observed identity: [`liberusoftware/module-browser-game-collections-livewire`](../../../modules/source/liberusoftware--module-browser-game-collections-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-collections-livewire`  
**Matching domain module:** `browser-game-collections`  
**Application:** Browser Game  
**Source feature:** [Browser Game Collections](../features/browser-game-collections.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Achievements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Titles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reputation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Housing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cosmetics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Collection progress:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-collections-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameCollections::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `achievements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `titles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reputation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `housing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cosmetics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `collection-progress`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-collections` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-collections.md) · [API plan](../api/browser-game-collections.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Achievements** | Expose a focused Livewire 4 component and namespaced Blade default view for `achievements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Titles** | Expose a focused Livewire 4 component and namespaced Blade default view for `titles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reputation** | Expose a focused Livewire 4 component and namespaced Blade default view for `reputation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pets** | Expose a focused Livewire 4 component and namespaced Blade default view for `pets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `mounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Housing** | Expose a focused Livewire 4 component and namespaced Blade default view for `housing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cosmetics** | Expose a focused Livewire 4 component and namespaced Blade default view for `cosmetics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Collection progress** | Expose a focused Livewire 4 component and namespaced Blade default view for `collection progress` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CollectionsCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-livewire/src/Livewire/CollectionsCatalog.php) · [CollectionsLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-livewire/src/CollectionsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Queries/CollectionsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableAchievements(?string $tenantId, ?string $teamId): Builder`<br>`public function forActor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function unlockedForActor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionProgress.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
