# Accounting: Accounting Custom Report Builder Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-custom-report-builder). Observed identity: [`liberusoftware/module-accounting-custom-report-builder-livewire`](../../../modules/source/liberusoftware--module-accounting-custom-report-builder-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-custom-report-builder-livewire`  
**Matching domain module:** `accounting-custom-report-builder`  
**Application:** Accounting  
**Source feature:** [Accounting Custom Report Builder](../features/accounting-custom-report-builder.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Governed measures/dimensions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Filters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grouping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Formulas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Comparisons:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Layouts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Permissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Saved variants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-custom-report-builder-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingCustomReportBuilder::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `governed-measures-dimensions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `filters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grouping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `formulas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `comparisons`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `layouts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `permissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `saved-variants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-custom-report-builder` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-custom-report-builder.md) · [API plan](../api/accounting-custom-report-builder.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Governed measures/dimensions** | Expose a focused Livewire 4 component and namespaced Blade default view for `governed measures/dimensions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Filters** | Expose a focused Livewire 4 component and namespaced Blade default view for `filters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grouping** | Expose a focused Livewire 4 component and namespaced Blade default view for `grouping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Formulas** | Expose a focused Livewire 4 component and namespaced Blade default view for `formulas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Comparisons** | Expose a focused Livewire 4 component and namespaced Blade default view for `comparisons` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Layouts** | Expose a focused Livewire 4 component and namespaced Blade default view for `layouts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Permissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `permissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Saved variants** | Expose a focused Livewire 4 component and namespaced Blade default view for `saved variants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exports** | Expose a focused Livewire 4 component and namespaced Blade default view for `exports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReportOverview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-livewire/src/Livewire/ReportOverview.php) · [CustomReportBuilderLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-livewire/src/CustomReportBuilderLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Queries/CustomReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/CreateCustomReport.php) | `public function handle(array $attributes): CustomReport` |
| [RequestReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/RequestReportExport.php) | `public function handle(CustomReport $report, string $format, array $parameters = []): CustomReportExport` |
| [SaveReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/SaveReportVariant.php) | `public function handle(CustomReport $report, string $variantRef, array $configuration): CustomReportVariant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReport.php) | `team_id`, `report_ref`, `name`, `measures`, `dimensions`, `filters`, `grouping`, `formulas`, `comparisons`, `layout`, `permissions` |
| [CustomReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportExport.php) | `report_id`, `team_id`, `format`, `status`, `parameters`, `completed_at` |
| [CustomReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportVariant.php) | `report_id`, `team_id`, `variant_ref`, `configuration` |
<!-- layer-implementation-plan:end -->
