# Accounting: Withholding Tax Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#withholding-tax). Observed identity: [`liberusoftware/module-accounting-withholding-tax-livewire`](../../../modules/source/liberusoftware--module-accounting-withholding-tax-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-withholding-tax-livewire`  
**Matching domain module:** `accounting-withholding-tax`  
**Application:** Accounting  
**Source feature:** [Withholding Tax](../features/withholding-tax.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Certificates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Supplier/customer deductions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Liabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Remittance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Regional filing adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-withholding-tax-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-withholding-tax::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `certificates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `supplier-customer-deductions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `liabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `remittance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `regional-filing-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-withholding-tax` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/withholding-tax.md) · [API plan](../api/withholding-tax.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Certificates** | Expose a focused Livewire 4 component and namespaced Blade default view for `certificates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Supplier/customer deductions** | Expose a focused Livewire 4 component and namespaced Blade default view for `supplier/customer deductions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Liabilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `liabilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Remittance** | Expose a focused Livewire 4 component and namespaced Blade default view for `remittance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Regional filing adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `regional filing adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [WithholdingTaxRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-livewire/src/Livewire/WithholdingTaxRules.php) · [WithholdingTaxLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-livewire/src/WithholdingTaxLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [CreateWithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [RemitWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WithholdingTaxCertificate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `certificate_ref`, `valid_from`, `valid_until`, `status`, `metadata` |
| [WithholdingTaxDeduction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `source_ref`, `currency`, `gross_amount`, `withheld_amount`, `status`, `metadata` |
| [WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) | `team_id`, `jurisdiction`, `provider`, `status`, `configuration` |
| [WithholdingTaxLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) | `team_id`, `deduction_id`, `amount`, `due_on`, `status`, `metadata` |
| [WithholdingTaxRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) | `team_id`, `liability_id`, `amount`, `remitted_on`, `reference`, `status`, `metadata` |
| [WithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) | `team_id`, `code`, `name`, `jurisdiction`, `rate`, `threshold`, `effective_from`, `effective_until`, `status`, `metadata` |
| [WithholdingTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) | `team_id`, `jurisdiction`, `period_start`, `period_end`, `total_amount`, `status`, `payload` |
<!-- layer-implementation-plan:end -->
