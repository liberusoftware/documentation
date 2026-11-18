# Browser Game: Browser Game Crafting Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-crafting). Observed identity: [`liberusoftware/module-browser-game-crafting-livewire`](../../../modules/source/liberusoftware--module-browser-game-crafting-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-crafting-livewire`  
**Matching domain module:** `browser-game-crafting`  
**Application:** Browser Game  
**Source feature:** [Browser Game Crafting](../features/browser-game-crafting.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Recipes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Professions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Resources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quality:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Salvage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Outputs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-crafting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameCrafting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `recipes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `professions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `resources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quality`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `salvage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `outputs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-crafting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-crafting.md) · [API plan](../api/browser-game-crafting.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Recipes** | Expose a focused Livewire 4 component and namespaced Blade default view for `recipes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Professions** | Expose a focused Livewire 4 component and namespaced Blade default view for `professions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Resources** | Expose a focused Livewire 4 component and namespaced Blade default view for `resources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quality** | Expose a focused Livewire 4 component and namespaced Blade default view for `quality` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Discovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `discovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Salvage** | Expose a focused Livewire 4 component and namespaced Blade default view for `salvage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Outputs** | Expose a focused Livewire 4 component and namespaced Blade default view for `outputs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CraftingCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-livewire/src/Livewire/CraftingCatalog.php) · [CraftingLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-livewire/src/CraftingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CraftingQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Queries/CraftingQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CraftingDiscovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingDiscovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingOutput.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingOutput.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingProfession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingProfession.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingQueue.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
