# Accounting: Year End Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#year-end). Observed identity: [`liberusoftware/module-accounting-year-end-livewire`](../../../modules/source/liberusoftware--module-accounting-year-end-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-year-end-livewire`  
**Matching domain module:** `accounting-year-end`  
**Application:** Accounting  
**Source feature:** [Year End](../features/year-end.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Final adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retained earnings/roll-forward:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Opening balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statutory/tax handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lock:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Archive:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-year-end-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-year-end::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `final-adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retained-earnings-roll-forward`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `opening-balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statutory-tax-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lock`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `archive`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-year-end` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/year-end.md) · [API plan](../api/year-end.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Final adjustments** | Expose a focused Livewire 4 component and namespaced Blade default view for `final adjustments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retained earnings/roll-forward** | Expose a focused Livewire 4 component and namespaced Blade default view for `retained earnings/roll-forward` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Opening balances** | Expose a focused Livewire 4 component and namespaced Blade default view for `opening balances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statutory/tax handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `statutory/tax handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lock** | Expose a focused Livewire 4 component and namespaced Blade default view for `lock` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Archive** | Expose a focused Livewire 4 component and namespaced Blade default view for `archive` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [YearEndCloses.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-livewire/src/Livewire/YearEndCloses.php) · [YearEndOverview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-livewire/src/Livewire/YearEndOverview.php) · [YearEndLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-livewire/src/YearEndLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [YearEndQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Queries/YearEndQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddYearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/AddYearEndAdjustment.php) | `public function handle(YearEndPeriod $period, array $attributes): YearEndAdjustment` |
| [ArchiveYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ArchiveYearEnd.php) | `public function handle(YearEndPeriod $period): YearEndPeriod` |
| [CloseYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CloseYearEnd.php) | `public function handle(YearEndClose $close, string $closingEntryRef): YearEndClose` |
| [CreateYearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndClose.php) | `public function handle(array $attributes): YearEndClose` |
| [CreateYearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndPeriod.php) | `public function handle(array $attributes): YearEndPeriod` |
| [LockYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/LockYearEnd.php) | `public function handle(YearEndPeriod $period, int $actor): YearEndPeriod` |
| [ReopenYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ReopenYearEnd.php) | `public function handle(YearEndClose $close): YearEndClose` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [YearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndAdjustment.php) | `period_id`, `team_id`, `adjustment_ref`, `amount`, `description`, `journal_ref`, `status`, `evidence` |
| [YearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndClose.php) | `team_id`, `fiscal_year`, `period_end`, `retained_earnings_account_ref`, `net_income`, `status`, `closed_at`, `locked_at`, `closing_entry_ref`, `metadata` |
| [YearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndPeriod.php) | `team_id`, `period_ref`, `period_end`, `status`, `retained_earnings`, `opening_balances`, `statutory_handoff`, `evidence`, `locked_by`, `locked_at`, `archived_at` |
<!-- layer-implementation-plan:end -->
