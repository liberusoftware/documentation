# Accounting: Accounting Project Profitability Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-project-profitability). Observed identity: [`liberusoftware/module-accounting-project-profitability-livewire`](../../../modules/source/liberusoftware--module-accounting-project-profitability-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-project-profitability-livewire`  
**Matching domain module:** `accounting-project-profitability`  
**Application:** Accounting  
**Source feature:** [Accounting Project Profitability](../features/accounting-project-profitability.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Revenue:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Margin:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Estimates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Committed/actual:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unbilled WIP:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Realization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dashboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drill-through:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-project-profitability-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingProjectProfitability::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `revenue`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `margin`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `estimates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `committed-actual`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unbilled-wip`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `realization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dashboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drill-through`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-project-profitability` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-project-profitability.md) · [API plan](../api/accounting-project-profitability.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Revenue** | Expose a focused Livewire 4 component and namespaced Blade default view for `revenue` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Margin** | Expose a focused Livewire 4 component and namespaced Blade default view for `margin` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Estimates** | Expose a focused Livewire 4 component and namespaced Blade default view for `estimates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Committed/actual** | Expose a focused Livewire 4 component and namespaced Blade default view for `committed/actual` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unbilled WIP** | Expose a focused Livewire 4 component and namespaced Blade default view for `unbilled wip` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Realization** | Expose a focused Livewire 4 component and namespaced Blade default view for `realization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dashboards** | Expose a focused Livewire 4 component and namespaced Blade default view for `dashboards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drill-through** | Expose a focused Livewire 4 component and namespaced Blade default view for `drill-through` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-livewire/src/Livewire/ProjectProfitability.php) · [ProjectProfitabilityLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-livewire/src/ProjectProfitabilityLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectProfitabilityDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Queries/ProjectProfitabilityDashboard.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinalizeProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/FinalizeProjectProfitability.php) | `public function handle(ProjectProfitability $record): ProjectProfitability` |
| [RecordProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/RecordProjectProfitability.php) | `public function handle(array $attributes): ProjectProfitability` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Models/ProjectProfitability.php) | `team_id`, `project_job_id`, `period_start`, `period_end`, `currency`, `revenue_amount`, `cost_amount`, `estimate_amount`, `committed_amount`, `actual_amount`, `unbilled_wip_amount`, `billed_amount`, `status`, `dimensions`, `source_links`, `metadata` |
<!-- layer-implementation-plan:end -->
