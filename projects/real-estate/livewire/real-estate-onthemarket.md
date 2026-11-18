# Real Estate: Real Estate Onthemarket Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-onthemarket). Observed identity: [`liberusoftware/real-estate-onthemarket-livewire`](../../../modules/source/liberusoftware--real-estate-onthemarket-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-real-estate-onthemarket-livewire`  
**Matching domain module:** `real-estate-onthemarket`  
**Application:** Real Estate  
**Source feature:** [Real Estate Onthemarket](../features/real-estate-onthemarket.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **OnTheMarket sync state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider payload boundary:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retry and error state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-real-estate-onthemarket-livewire` component namespace and service provider; use explicit aliases such as `<livewire:realestateRealEstateOnthemarket::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `onthemarket-sync-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-payload-boundary`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retry-and-error-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-onthemarket` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/real-estate-onthemarket.md) · [API plan](../api/real-estate-onthemarket.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **OnTheMarket sync state** | Expose a focused Livewire 4 component and namespaced Blade default view for `onthemarket sync state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider payload boundary** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider payload boundary` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retry and error state** | Expose a focused Livewire 4 component and namespaced Blade default view for `retry and error state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [OnTheMarketSyncList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket-livewire/src/Components/OnTheMarketSyncList.php) · [OnTheMarketLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket-livewire/src/OnTheMarketLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OnTheMarketTransport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket/src/Contracts/OnTheMarketTransport.php) | `public function sendProperty(string $reference, array $payload, array $credentials): array`<br>`public function removeProperty(string $reference, array $credentials): array`<br>`public function branchPropertyList(array $credentials): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OnTheMarketSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-onthemarket/src/Models/OnTheMarketSync.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
