# Accounting: Accounting Asset Events Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-asset-events). Observed identity: [`liberusoftware/module-accounting-asset-events-livewire`](../../../modules/source/liberusoftware--module-accounting-asset-events-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-asset-events-livewire`  
**Matching domain module:** `accounting-asset-events`  
**Application:** Accounting  
**Source feature:** [Accounting Asset Events](../features/accounting-asset-events.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Transfer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Improvement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Revaluation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Impairment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disposal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sale:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Write-off:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gain/loss:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Complete history:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-asset-events-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingAssetEvents::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `transfer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `improvement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `revaluation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `impairment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disposal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sale`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `write-off`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gain-loss`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `complete-history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-asset-events` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-asset-events.md) · [API plan](../api/accounting-asset-events.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Transfer** | Expose a focused Livewire 4 component and namespaced Blade default view for `transfer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Improvement** | Expose a focused Livewire 4 component and namespaced Blade default view for `improvement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Revaluation** | Expose a focused Livewire 4 component and namespaced Blade default view for `revaluation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Impairment** | Expose a focused Livewire 4 component and namespaced Blade default view for `impairment` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disposal** | Expose a focused Livewire 4 component and namespaced Blade default view for `disposal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sale** | Expose a focused Livewire 4 component and namespaced Blade default view for `sale` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Write-off** | Expose a focused Livewire 4 component and namespaced Blade default view for `write-off` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gain/loss** | Expose a focused Livewire 4 component and namespaced Blade default view for `gain/loss` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Complete history** | Expose a focused Livewire 4 component and namespaced Blade default view for `complete history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AssetEvents.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-livewire/src/Livewire/AssetEvents.php) · [AssetEventsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-livewire/src/AssetEventsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AssetEventQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Queries/AssetEventQuery.php) | `public function paginate(int $teamId, ?int $assetId = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordAssetEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Actions/RecordAssetEvent.php) | `public function handle(array $attributes): AssetEvent` |
| [AssetEventPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-api/src/Policies/AssetEventPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AssetEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Models/AssetEvent.php) | `team_id`, `asset_id`, `event_type`, `event_date`, `description`, `source_type`, `source_id`, `old_values`, `new_values`, `evidence`, `actor_id` |
| [Asset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-api/src/Models/Asset.php) | `asset_name`, `asset_cost`, `useful_life_years`, `depreciation_method`, `salvage_value`, `acquisition_date`, `is_active` |
<!-- layer-implementation-plan:end -->
