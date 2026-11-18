# Accounting: Accounting Management Reporting Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-management-reporting). Observed identity: [`liberusoftware/module-accounting-management-reporting-livewire`](../../../modules/source/liberusoftware--module-accounting-management-reporting-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-management-reporting-livewire`  
**Matching domain module:** `accounting-management-reporting`  
**Application:** Accounting  
**Source feature:** [Accounting Management Reporting](../features/accounting-management-reporting.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Report packs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Narratives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Charts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **PDF/spreadsheet delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Archive:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-management-reporting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingManagementReporting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `report-packs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `narratives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `charts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pdf-spreadsheet-delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `archive`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-management-reporting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-management-reporting.md) · [API plan](../api/accounting-management-reporting.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Report packs** | Expose a focused Livewire 4 component and namespaced Blade default view for `report packs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Narratives** | Expose a focused Livewire 4 component and namespaced Blade default view for `narratives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Charts** | Expose a focused Livewire 4 component and namespaced Blade default view for `charts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review** | Expose a focused Livewire 4 component and namespaced Blade default view for `review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **PDF/spreadsheet delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `pdf/spreadsheet delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Archive** | Expose a focused Livewire 4 component and namespaced Blade default view for `archive` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReportPacks.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-livewire/src/Livewire/ReportPacks.php) · [ManagementReportingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-livewire/src/ManagementReportingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Queries/ReportQuery.php) | `public function packs(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(ReportPack $report): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReportContent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/AddReportContent.php) | `public function narrative(ReportPack $report, array $attributes): ReportNarrative`<br>`public function chart(ReportPack $report, array $attributes): ReportChart` |
| [ArchiveReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ArchiveReport.php) | `public function handle(ReportPack $report): ReportPack` |
| [CreateReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/CreateReportPack.php) | `public function handle(array $attributes): ReportPack` |
| [DeliverReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/DeliverReport.php) | `public function handle(ReportPack $report, string $format, array $attributes = []): ReportDelivery` |
| [ReviewReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ReviewReport.php) | `public function handle(ReportPack $report, string $actor, string $decision, ?string $comment = null): ReportPack` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportChart.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportChart.php) | `report_pack_id`, `chart_ref`, `title`, `chart_type`, `data_source`, `series`, `options`, `metadata` |
| [ReportDelivery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportDelivery.php) | `report_pack_id`, `format`, `file_ref`, `status`, `recipients`, `checksum`, `delivered_at`, `failure_message`, `metadata` |
| [ReportNarrative.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportNarrative.php) | `report_pack_id`, `section_ref`, `title`, `body`, `author_ref`, `version`, `metadata` |
| [ReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportPack.php) | `team_id`, `report_ref`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `owner_ref`, `approved_by`, `approved_at`, `delivered_at`, `archived_at`, `metadata` |
| [ReportReview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportReview.php) | `report_pack_id`, `actor_ref`, `decision`, `comment`, `reviewed_at`, `metadata` |
| [ReportSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportSchedule.php) | `report_pack_id`, `frequency`, `timezone`, `recipients`, `next_run_at`, `active`, `last_run_at`, `failure_message`, `metadata` |
<!-- layer-implementation-plan:end -->
