# Accounting: Contractor Compliance Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#contractor-compliance). Observed identity: [`liberusoftware/module-accounting-contractor-compliance-livewire`](../../../modules/source/liberusoftware--module-accounting-contractor-compliance-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-contractor-compliance-livewire`  
**Matching domain module:** `accounting-contractor-compliance`  
**Application:** Accounting  
**Source feature:** [Contractor Compliance](../features/contractor-compliance.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Contractor records:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status/evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Withholding schemes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CIS/1099-style classifications:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deductions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Regional exports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-contractor-compliance-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-contractor-compliance::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `contractor-records`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `withholding-schemes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cis-1099-style-classifications`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deductions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `regional-exports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-contractor-compliance` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/contractor-compliance.md) · [API plan](../api/contractor-compliance.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Contractor records** | Expose a focused Livewire 4 component and namespaced Blade default view for `contractor records` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Status/evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `status/evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Withholding schemes** | Expose a focused Livewire 4 component and namespaced Blade default view for `withholding schemes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CIS/1099-style classifications** | Expose a focused Livewire 4 component and namespaced Blade default view for `cis/1099-style classifications` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deductions** | Expose a focused Livewire 4 component and namespaced Blade default view for `deductions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Regional exports** | Expose a focused Livewire 4 component and namespaced Blade default view for `regional exports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ContractorComplianceLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-livewire/src/ContractorComplianceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Queries/ContractorQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExportContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/ExportContractorCompliance.php) | `public function handle(Contractor $contractor, string $region): Contractor` |
| [IssueContractorStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/IssueContractorStatement.php) | `public function handle(Contractor $contractor, array $statement): Contractor` |
| [RecordContractorEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RecordContractorEvidence.php) | `public function handle(Contractor $contractor, array $evidence): Contractor` |
| [RegisterContractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RegisterContractor.php) | `public function handle(array $attributes): Contractor` |
| [UpdateContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/UpdateContractorCompliance.php) | `public function handle(Contractor $contractor, array $attributes): Contractor` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Models/Contractor.php) | `team_id`, `contractor_ref`, `legal_name`, `classification`, `status`, `withholding_scheme`, `deductions`, `evidence`, `statement`, `regional_export` |
<!-- layer-implementation-plan:end -->
