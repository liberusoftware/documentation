# Genealogy: Genealogy Reports Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-reports). Observed identity: [`liberusoftware/module-genealogy-reports-livewire`](../../../modules/source/liberusoftware--module-genealogy-reports-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-genealogy-reports-livewire`  
**Matching domain module:** `genealogy-reports`  
**Application:** Genealogy  
**Source feature:** [Genealogy Reports](../features/genealogy-reports.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Family groups:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pedigrees:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Descendants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Timelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Research:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exportable charts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-genealogy-reports-livewire` component namespace and service provider; use explicit aliases such as `<livewire:genealogyGenealogyReports::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `family-groups`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pedigrees`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `descendants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `timelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `research`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exportable-charts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-reports` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/genealogy-reports.md) · [API plan](../api/genealogy-reports.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Family groups** | Expose a focused Livewire 4 component and namespaced Blade default view for `family groups` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pedigrees** | Expose a focused Livewire 4 component and namespaced Blade default view for `pedigrees` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Descendants** | Expose a focused Livewire 4 component and namespaced Blade default view for `descendants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Timelines** | Expose a focused Livewire 4 component and namespaced Blade default view for `timelines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Research** | Expose a focused Livewire 4 component and namespaced Blade default view for `research` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sources** | Expose a focused Livewire 4 component and namespaced Blade default view for `sources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exportable charts** | Expose a focused Livewire 4 component and namespaced Blade default view for `exportable charts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ReportsLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports-livewire/src/ReportsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BuildGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Queries/BuildGenealogyReport.php) | `public function execute(string $type, string $teamId, array $parameters = []): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/CreateGenealogyReport.php) | `public function execute(array $attributes): GenealogyReport`<br>`public function validate(array $values): void` |
| [DeleteGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/DeleteGenealogyReport.php) | `public function execute(GenealogyReport $report): void` |
| [GenerateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/GenerateGenealogyReport.php) | `public function __construct(private ?BuildGenealogyReport $builder = null)`<br>`public function execute(GenealogyReport $report, array $parameters = []): GenealogyReport` |
| [UpdateGenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Actions/UpdateGenealogyReport.php) | `public function execute(GenealogyReport $report, array $attributes): GenealogyReport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GenealogyReport.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-reports/src/Models/GenealogyReport.php) | `team_id`, `name`, `type`, `status`, `metadata`, `generated_output`, `generated_at` |
<!-- layer-implementation-plan:end -->
