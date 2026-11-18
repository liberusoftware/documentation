# Accounting: Accounting Construction Tax Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-construction-tax). Observed identity: [`liberusoftware/module-accounting-construction-tax-livewire`](../../../modules/source/liberusoftware--module-accounting-construction-tax-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-construction-tax-livewire`  
**Matching domain module:** `accounting-construction-tax`  
**Application:** Accounting  
**Source feature:** [Accounting Construction Tax](../features/accounting-construction-tax.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **CIS-style subcontractor verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deduction rates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Monthly returns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Corrections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Filing adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-construction-tax-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingConstructionTax::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `cis-style-subcontractor-verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deduction-rates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `monthly-returns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `corrections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `filing-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-construction-tax` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-construction-tax.md) · [API plan](../api/accounting-construction-tax.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **CIS-style subcontractor verification** | Expose a focused Livewire 4 component and namespaced Blade default view for `cis-style subcontractor verification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deduction rates** | Expose a focused Livewire 4 component and namespaced Blade default view for `deduction rates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Monthly returns** | Expose a focused Livewire 4 component and namespaced Blade default view for `monthly returns` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Corrections** | Expose a focused Livewire 4 component and namespaced Blade default view for `corrections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Filing adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `filing adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ConstructionTaxLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-livewire/src/ConstructionTaxLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConstructionTaxQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Queries/ConstructionTaxQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CorrectConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, array $correction): ConstructionTaxRecord` |
| [CreateConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CreateConstructionTaxRecord.php) | `public function handle(array $attributes): ConstructionTaxRecord` |
| [IssueConstructionTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/IssueConstructionTaxStatement.php) | `public function handle(ConstructionTaxRecord $record, array $statement): ConstructionTaxRecord` |
| [SubmitConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/SubmitConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, string $adapter): ConstructionTaxRecord` |
| [VerifySubcontractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/VerifySubcontractor.php) | `public function handle(ConstructionTaxRecord $record, array $verification): ConstructionTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Models/ConstructionTaxRecord.php) | `team_id`, `subcontractor_ref`, `verification_status`, `deduction_rate`, `tax_period`, `gross_amount`, `deduction_amount`, `return_status`, `filing_adapter`, `verification`, `statement`, `correction` |
<!-- layer-implementation-plan:end -->
