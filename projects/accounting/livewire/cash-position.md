# Accounting: Cash Position Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-position). Observed identity: [`liberusoftware/module-accounting-cash-position-livewire`](../../../modules/source/liberusoftware--module-accounting-cash-position-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-cash-position-livewire`  
**Matching domain module:** `accounting-cash-position`  
**Application:** Accounting  
**Source feature:** [Cash Position](../features/cash-position.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Available/ledger balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Outstanding receipts/payments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Committed cash:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Entity/currency views:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Freshness:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-cash-position-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-cash-position::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `available-ledger-balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `outstanding-receipts-payments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `committed-cash`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `entity-currency-views`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `freshness`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-cash-position` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cash-position.md) · [API plan](../api/cash-position.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Available/ledger balances** | Expose a focused Livewire 4 component and namespaced Blade default view for `available/ledger balances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Outstanding receipts/payments** | Expose a focused Livewire 4 component and namespaced Blade default view for `outstanding receipts/payments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Committed cash** | Expose a focused Livewire 4 component and namespaced Blade default view for `committed cash` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Entity/currency views** | Expose a focused Livewire 4 component and namespaced Blade default view for `entity/currency views` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Freshness** | Expose a focused Livewire 4 component and namespaced Blade default view for `freshness` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CashPositionLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position-livewire/src/CashPositionLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CashPositionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Queries/CashPositionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/CreateCashPosition.php) | `public function handle(array $attributes): CashPosition` |
| [RefreshCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/RefreshCashPosition.php) | `public function handle(CashPosition $position, array $balances): CashPosition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Models/CashPosition.php) | `team_id`, `view_ref`, `entity_ref`, `currency`, `ledger_balance`, `available_balance`, `outstanding_receipts`, `outstanding_payments`, `committed_cash`, `refreshed_at` |
<!-- layer-implementation-plan:end -->
