# Accounting: Transfers Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#transfers). Observed identity: [`liberusoftware/module-accounting-transfers-livewire`](../../../modules/source/liberusoftware--module-accounting-transfers-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-transfers-livewire`  
**Matching domain module:** `accounting-transfers`  
**Application:** Accounting  
**Source feature:** [Transfers](../features/transfers.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Inter-account/entity transfers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Currency conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fees:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **In-transit state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Paired posting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-transfers-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-transfers::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `inter-account-entity-transfers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `currency-conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fees`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `in-transit-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `paired-posting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-transfers` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/transfers.md) · [API plan](../api/transfers.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Inter-account/entity transfers** | Expose a focused Livewire 4 component and namespaced Blade default view for `inter-account/entity transfers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Currency conversion** | Expose a focused Livewire 4 component and namespaced Blade default view for `currency conversion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fees** | Expose a focused Livewire 4 component and namespaced Blade default view for `fees` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **In-transit state** | Expose a focused Livewire 4 component and namespaced Blade default view for `in-transit state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Paired posting** | Expose a focused Livewire 4 component and namespaced Blade default view for `paired posting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [TransfersList.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-livewire/src/Livewire/TransfersList.php) · [TransfersLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-livewire/src/TransfersLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CompleteTransfer.php) | `public function handle(Transfer $transfer): Transfer` |
| [CreateTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CreateTransfer.php) | `public function handle(array $attributes): Transfer` |
| [ReconcileTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/ReconcileTransfer.php) | `public function handle(Transfer $transfer, array $attributes): TransferReconciliation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Transfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/Transfer.php) | `team_id`, `source_account_ref`, `destination_account_ref`, `source_currency`, `destination_currency`, `source_amount`, `destination_amount`, `exchange_rate`, `fee_amount`, `status`, `reference`, `metadata` |
| [TransferReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/TransferReconciliation.php) | `team_id`, `transfer_id`, `external_ref`, `amount`, `reconciled_on`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
