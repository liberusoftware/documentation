# Browser Game: Browser Game Economy Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-economy). Observed identity: [`liberusoftware/module-browser-game-economy-livewire`](../../../modules/source/liberusoftware--module-browser-game-economy-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-browser-game-economy-livewire`  
**Matching domain module:** `browser-game-economy`  
**Application:** Browser Game  
**Source feature:** [Browser Game Economy](../features/browser-game-economy.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Currencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Faucets/sinks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Vendors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pricing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Trading:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Auction house:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fees:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Anti-abuse controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-browser-game-economy-livewire` component namespace and service provider; use explicit aliases such as `<livewire:browsergameBrowserGameEconomy::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `currencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `faucets-sinks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `vendors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pricing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `trading`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `auction-house`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fees`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `anti-abuse-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-economy` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/browser-game-economy.md) · [API plan](../api/browser-game-economy.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Currencies** | Expose a focused Livewire 4 component and namespaced Blade default view for `currencies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Faucets/sinks** | Expose a focused Livewire 4 component and namespaced Blade default view for `faucets/sinks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Vendors** | Expose a focused Livewire 4 component and namespaced Blade default view for `vendors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pricing** | Expose a focused Livewire 4 component and namespaced Blade default view for `pricing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Trading** | Expose a focused Livewire 4 component and namespaced Blade default view for `trading` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Auction house** | Expose a focused Livewire 4 component and namespaced Blade default view for `auction house` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fees** | Expose a focused Livewire 4 component and namespaced Blade default view for `fees` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Anti-abuse controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `anti-abuse controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EconomyCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-livewire/src/Livewire/EconomyCatalog.php) · [EconomyLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-livewire/src/EconomyLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EconomyQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Queries/EconomyQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EconomyLedgerEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyLedgerEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyListing.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyListing.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendor.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendor.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendorOffer.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendorOffer.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyWallet.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyWallet.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
