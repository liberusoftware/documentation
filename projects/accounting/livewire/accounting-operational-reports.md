# Accounting: Accounting Operational Reports Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-operational-reports). Observed identity: [`liberusoftware/module-accounting-operational-reports-livewire`](../../../modules/source/liberusoftware--module-accounting-operational-reports-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-operational-reports-livewire`  
**Matching domain module:** `accounting-operational-reports`  
**Application:** Accounting  
**Source feature:** [Accounting Operational Reports](../features/accounting-operational-reports.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Receivables/payables:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sales/purchases:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bank:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expenses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Projects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payroll:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exception reports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-operational-reports-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingOperationalReports::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `receivables-payables`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sales-purchases`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bank`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expenses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `projects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payroll`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exception-reports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-operational-reports` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-operational-reports.md) · [API plan](../api/accounting-operational-reports.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Receivables/payables** | Expose a focused Livewire 4 component and namespaced Blade default view for `receivables/payables` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sales/purchases** | Expose a focused Livewire 4 component and namespaced Blade default view for `sales/purchases` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bank** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inventory** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventory` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assets** | Expose a focused Livewire 4 component and namespaced Blade default view for `assets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expenses** | Expose a focused Livewire 4 component and namespaced Blade default view for `expenses` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Projects** | Expose a focused Livewire 4 component and namespaced Blade default view for `projects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payroll** | Expose a focused Livewire 4 component and namespaced Blade default view for `payroll` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exception reports** | Expose a focused Livewire 4 component and namespaced Blade default view for `exception reports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReportRuns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-livewire/src/Livewire/ReportRuns.php) · [OperationalReportsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-livewire/src/OperationalReportsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Queries/ReportQuery.php) | `public function paginate(?int $teamId = null, ?string $category = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function exceptions(?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GenerateReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/GenerateReport.php) | `public function handle(array $attributes, array $rows = [], array $exceptions = []): ReportRun` |
| [PublishReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/PublishReport.php) | `public function handle(ReportRun $run, int $actorId): ReportRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportAudit.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ReportException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportException.php) | `run_id`, `exception_key`, `severity`, `message`, `source_type`, `source_id`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReportRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRow.php) | `run_id`, `row_key`, `label`, `source_type`, `source_id`, `amount`, `currency`, `state`, `dimensions`, `payload` |
| [ReportRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRun.php) | `team_id`, `report_key`, `name`, `category`, `period_start`, `period_end`, `currency`, `status`, `filters`, `summary`, `source_hash`, `requested_by`, `published_by`, `published_at`, `failure_message`, `metadata` |
<!-- layer-implementation-plan:end -->
