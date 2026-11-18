# Accounting: Project Costing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#project-costing). Observed identity: [`liberusoftware/module-accounting-project-costing-livewire`](../../../modules/source/liberusoftware--module-accounting-project-costing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-project-costing-livewire`  
**Matching domain module:** `accounting-project-costing`  
**Application:** Accounting  
**Source feature:** [Project Costing](../features/project-costing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Labor:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expense:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bill:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Subcontractor:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Overhead:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Commitments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **WIP:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost-to-complete:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Variance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-project-costing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-project-costing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `labor`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expense`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bill`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `subcontractor`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `overhead`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `commitments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `wip`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost-to-complete`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `variance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-project-costing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/project-costing.md) · [API plan](../api/project-costing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Labor** | Expose a focused Livewire 4 component and namespaced Blade default view for `labor` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expense** | Expose a focused Livewire 4 component and namespaced Blade default view for `expense` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bill** | Expose a focused Livewire 4 component and namespaced Blade default view for `bill` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inventory** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventory` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Subcontractor** | Expose a focused Livewire 4 component and namespaced Blade default view for `subcontractor` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Overhead** | Expose a focused Livewire 4 component and namespaced Blade default view for `overhead` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Commitments** | Expose a focused Livewire 4 component and namespaced Blade default view for `commitments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **WIP** | Expose a focused Livewire 4 component and namespaced Blade default view for `wip` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost-to-complete** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost-to-complete` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Variance** | Expose a focused Livewire 4 component and namespaced Blade default view for `variance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProjectCosts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing-livewire/src/Livewire/ProjectCosts.php) · [ProjectCostingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing-livewire/src/ProjectCostingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectCostSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Queries/ProjectCostSummary.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordProjectCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Actions/RecordProjectCost.php) | `public function handle(array $attributes): ProjectCost` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Models/ProjectCost.php) | `team_id`, `project_job_id`, `type`, `occurred_on`, `amount`, `currency`, `committed`, `actual`, `wip_amount`, `source_ref`, `dimensions`, `metadata` |
<!-- layer-implementation-plan:end -->
