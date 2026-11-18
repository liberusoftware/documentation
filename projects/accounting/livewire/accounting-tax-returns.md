# Accounting: Accounting Tax Returns Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-tax-returns). Observed identity: [`liberusoftware/module-accounting-tax-returns-livewire`](../../../modules/source/liberusoftware--module-accounting-tax-returns-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-tax-returns-livewire`  
**Matching domain module:** `accounting-tax-returns`  
**Application:** Accounting  
**Source feature:** [Accounting Tax Returns](../features/accounting-tax-returns.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Return preparation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Diagnostics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Submission adapter:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Receipt/status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Amendments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-tax-returns-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingTaxReturns::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `return-preparation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `diagnostics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `submission-adapter`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `receipt-status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `amendments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-tax-returns` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-tax-returns.md) · [API plan](../api/accounting-tax-returns.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Return preparation** | Expose a focused Livewire 4 component and namespaced Blade default view for `return preparation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `source reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Diagnostics** | Expose a focused Livewire 4 component and namespaced Blade default view for `diagnostics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review** | Expose a focused Livewire 4 component and namespaced Blade default view for `review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Submission adapter** | Expose a focused Livewire 4 component and namespaced Blade default view for `submission adapter` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Receipt/status** | Expose a focused Livewire 4 component and namespaced Blade default view for `receipt/status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payment** | Expose a focused Livewire 4 component and namespaced Blade default view for `payment` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Amendments** | Expose a focused Livewire 4 component and namespaced Blade default view for `amendments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [TaxReturns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-livewire/src/Livewire/TaxReturns.php) · [TaxReturnsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-livewire/src/TaxReturnsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AmendTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/AmendTaxReturn.php) | `public function handle(TaxReturn $taxReturn): TaxReturn` |
| [CreateTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/CreateTaxReturn.php) | `public function handle(array $attributes): TaxReturn` |
| [SubmitTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/SubmitTaxReturn.php) | `public function handle(TaxReturn $taxReturn, string $externalReference): TaxReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturn.php) | `team_id`, `tax_type`, `jurisdiction`, `period_start`, `period_end`, `due_on`, `status`, `external_reference`, `submitted_at`, `metadata` |
| [TaxReturnLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturnLine.php) | `team_id`, `tax_return_id`, `code`, `amount`, `currency`, `metadata` |
<!-- layer-implementation-plan:end -->
