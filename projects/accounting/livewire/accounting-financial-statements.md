# Accounting: Accounting Financial Statements Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-financial-statements). Observed identity: [`liberusoftware/module-accounting-financial-statements-livewire`](../../../modules/source/liberusoftware--module-accounting-financial-statements-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-financial-statements-livewire`  
**Matching domain module:** `accounting-financial-statements`  
**Application:** Accounting  
**Source feature:** [Accounting Financial Statements](../features/accounting-financial-statements.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Profit and loss:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Balance sheet:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cash flow:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Changes in equity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Comparative periods:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dimensions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drill-through:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-financial-statements-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingFinancialStatements::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `profit-and-loss`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `balance-sheet`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cash-flow`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `changes-in-equity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `comparative-periods`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dimensions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drill-through`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-financial-statements` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-financial-statements.md) · [API plan](../api/accounting-financial-statements.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Profit and loss** | Expose a focused Livewire 4 component and namespaced Blade default view for `profit and loss` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Balance sheet** | Expose a focused Livewire 4 component and namespaced Blade default view for `balance sheet` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cash flow** | Expose a focused Livewire 4 component and namespaced Blade default view for `cash flow` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Changes in equity** | Expose a focused Livewire 4 component and namespaced Blade default view for `changes in equity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Comparative periods** | Expose a focused Livewire 4 component and namespaced Blade default view for `comparative periods` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dimensions** | Expose a focused Livewire 4 component and namespaced Blade default view for `dimensions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drill-through** | Expose a focused Livewire 4 component and namespaced Blade default view for `drill-through` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Statements.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-livewire/src/Livewire/Statements.php) · [FinancialStatementsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-livewire/src/FinancialStatementsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinancialStatementsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Policies/FinancialStatementsPolicy.php) | `public function view(?Authenticatable $user): bool` |
<!-- layer-implementation-plan:end -->
