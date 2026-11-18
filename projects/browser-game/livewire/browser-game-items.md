# Browser Game: Browser Game Items Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-items). Observed identity: [`liberusoftware/module-browser-game-items-livewire`](../../../modules/source/liberusoftware--module-browser-game-items-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-items-livewire`  
**Matching domain module:** `browser-game-items`  
**Application:** Browser Game  
**Source feature:** [Browser Game Items](../features/browser-game-items.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Definitions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Equipment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Durability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Binding:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Containers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stack rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-items-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameItems::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `definitions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `equipment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `durability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `binding`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `containers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stack-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-items` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-items.md) · [API plan](../api/browser-game-items.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Definitions** | Expose a focused Livewire 4 component and namespaced Blade default view for `definitions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inventory** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventory` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Equipment** | Expose a focused Livewire 4 component and namespaced Blade default view for `equipment` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Durability** | Expose a focused Livewire 4 component and namespaced Blade default view for `durability` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Binding** | Expose a focused Livewire 4 component and namespaced Blade default view for `binding` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Containers** | Expose a focused Livewire 4 component and namespaced Blade default view for `containers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Stack rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `stack rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `provenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ItemsCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-livewire/src/Livewire/ItemsCatalog.php) · [ItemsLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-livewire/src/ItemsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ItemsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Queries/ItemsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InventoryEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/InventoryEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [ItemsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/ItemsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
