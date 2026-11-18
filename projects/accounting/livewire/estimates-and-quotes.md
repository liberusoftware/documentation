# Accounting: Estimates and Quotes Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#estimates-and-quotes). Observed identity: [`liberusoftware/module-accounting-estimates-and-quotes-livewire`](../../../modules/source/liberusoftware--module-accounting-estimates-and-quotes-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-estimates-and-quotes-livewire`  
**Matching domain module:** `accounting-estimates-and-quotes`  
**Application:** Accounting  
**Source feature:** [Estimates and Quotes](../features/estimates-and-quotes.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Branded estimates/quotes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Terms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Acceptance/decline:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **History:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-estimates-and-quotes-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-estimates-and-quotes::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `branded-estimates-quotes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `terms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `acceptance-decline`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-estimates-and-quotes` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/estimates-and-quotes.md) · [API plan](../api/estimates-and-quotes.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Branded estimates/quotes** | Expose a focused Livewire 4 component and namespaced Blade default view for `branded estimates/quotes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Items** | Expose a focused Livewire 4 component and namespaced Blade default view for `items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Terms** | Expose a focused Livewire 4 component and namespaced Blade default view for `terms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Acceptance/decline** | Expose a focused Livewire 4 component and namespaced Blade default view for `acceptance/decline` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expiry** | Expose a focused Livewire 4 component and namespaced Blade default view for `expiry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conversion** | Expose a focused Livewire 4 component and namespaced Blade default view for `conversion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **History** | Expose a focused Livewire 4 component and namespaced Blade default view for `history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Estimates.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-livewire/src/Livewire/Estimates.php) · [EstimatesAndQuotesLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-livewire/src/EstimatesAndQuotesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Queries/EstimateQuery.php) | `public function paginate(?int $legalEntityId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(Estimate $e): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/AddEstimateItem.php) | `public function handle(Estimate $e, array $a): EstimateItem` |
| [ConvertEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ConvertEstimate.php) | `public function handle(Estimate $e, string $convertedRef, ?string $actor = null): Estimate` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/CreateEstimate.php) | `public function handle(array $a): Estimate` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/DecideEstimate.php) | `public function handle(Estimate $e, bool $accepted, ?string $reason = null, ?string $actor = null): Estimate` |
| [ExpireEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ExpireEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |
| [SendEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/SendEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Estimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/Estimate.php) | `legal_entity_id`, `customer_ref`, `quote_ref`, `name`, `currency`, `status`, `issue_date`, `expires_on`, `version`, `terms`, `brand`, `accepted_at`, `declined_reason`, `converted_ref`, `metadata` |
| [EstimateHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateHistory.php) | `estimate_id`, `event`, `actor_ref`, `metadata` |
| [EstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateItem.php) | `estimate_id`, `item_ref`, `description`, `quantity`, `unit_price`, `tax_rate`, `amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateVersion.php) | `estimate_id`, `version`, `snapshot`, `created_by` |
<!-- layer-implementation-plan:end -->
