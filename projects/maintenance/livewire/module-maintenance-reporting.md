# Maintenance: Module Maintenance Reporting Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-reporting). Observed identity: [`liberusoftware/module-maintenance-reporting-livewire`](../../../modules/source/liberusoftware--module-maintenance-reporting-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-module-maintenance-reporting-livewire`  
**Matching domain module:** `module-maintenance-reporting`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Reporting](../features/module-maintenance-reporting.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Backlog:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Response:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **First-time fix:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Downtime:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Utilization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stock:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SLA:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compliance metrics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-module-maintenance-reporting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:maintenanceModuleMaintenanceReporting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `backlog`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `response`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `first-time-fix`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `downtime`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `utilization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stock`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sla`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compliance-metrics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-maintenance-reporting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-maintenance-reporting.md) · [API plan](../api/module-maintenance-reporting.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Backlog** | Expose a focused Livewire 4 component and namespaced Blade default view for `backlog` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Response** | Expose a focused Livewire 4 component and namespaced Blade default view for `response` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **First-time fix** | Expose a focused Livewire 4 component and namespaced Blade default view for `first-time fix` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Downtime** | Expose a focused Livewire 4 component and namespaced Blade default view for `downtime` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Utilization** | Expose a focused Livewire 4 component and namespaced Blade default view for `utilization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Stock** | Expose a focused Livewire 4 component and namespaced Blade default view for `stock` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SLA** | Expose a focused Livewire 4 component and namespaced Blade default view for `sla` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Compliance metrics** | Expose a focused Livewire 4 component and namespaced Blade default view for `compliance metrics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReportingList.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-livewire/src/Components/ReportingList.php) · [ReportingLivewireServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-livewire/src/ReportingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BuildReportSummary.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Queries/BuildReportSummary.php) | `public function handle(int $teamId, ?CarbonInterface $start = null, ?CarbonInterface $end = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/CreateReportRecord.php) | `public function handle(int $teamId, array $attributes): ReportRecord` |
| [DeleteReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/DeleteReportRecord.php) | `public function handle(int $teamId, ReportRecord $record): void` |
| [PublishReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/PublishReport.php) | `public function execute(int $teamId, ReportRecord $record): ReportRecord` |
| [UpdateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/UpdateReportRecord.php) | `public function handle(int $teamId, ReportRecord $record, array $attributes): ReportRecord` |
| [ReportRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Policies/ReportRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ReportRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ReportRecord $record): bool`<br>`public function delete(object $user, ReportRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportKind.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportKind.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportRecord.php) | `kind`, `title`, `description`, `metric_value`, `period_start`, `period_end`, `status`, `metadata`, `team_id` |
<!-- layer-implementation-plan:end -->
