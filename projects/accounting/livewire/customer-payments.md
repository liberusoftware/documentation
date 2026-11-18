# Accounting: Customer Payments Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-payments). Observed identity: [`liberusoftware/module-accounting-customer-payments-livewire`](../../../modules/source/liberusoftware--module-accounting-customer-payments-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-customer-payments-livewire`  
**Matching domain module:** `accounting-customer-payments`  
**Application:** Accounting  
**Source feature:** [Customer Payments](../features/customer-payments.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Receipts and online payment links via payment-contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gateway/bank references and provider provenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deposits and undeposited funds clearing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocations and partial/overpayments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Refunds and chargeback adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation with merchant settlements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-customer-payments-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-customer-payments::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `receipts-and-online-payment-links-via-payment-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gateway-bank-references-and-provider-provenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deposits-and-undeposited-funds-clearing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocations-and-partial-overpayments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `refunds-and-chargeback-adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation-with-merchant-settlements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-customer-payments` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/customer-payments.md) · [API plan](../api/customer-payments.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Receipts and online payment links via payment-contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `receipts and online payment links via payment-contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gateway/bank references and provider provenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `gateway/bank references and provider provenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deposits and undeposited funds clearing** | Expose a focused Livewire 4 component and namespaced Blade default view for `deposits and undeposited funds clearing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocations and partial/overpayments** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocations and partial/overpayments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Refunds and chargeback adjustments** | Expose a focused Livewire 4 component and namespaced Blade default view for `refunds and chargeback adjustments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation with merchant settlements** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation with merchant settlements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PaymentOverview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-livewire/src/Livewire/PaymentOverview.php) · [CustomerPaymentsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-livewire/src/CustomerPaymentsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerPaymentQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Queries/CustomerPaymentQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function forCustomer(int $teamId, string $customerId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/AllocateCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $documentRef, float $amount): CustomerPaymentAllocation` |
| [ReconcileCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/ReconcileCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $depositReference): CustomerPayment` |
| [RecordCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RecordCustomerPayment.php) | `public function handle(array $attributes): CustomerPayment` |
| [RefundCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RefundCustomerPayment.php) | `public function handle(CustomerPayment $payment, float $amount): CustomerPayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPayment.php) | `team_id`, `customer_id`, `kind`, `reference`, `status`, `currency`, `amount`, `allocated_amount`, `refunded_amount`, `gateway_reference`, `deposit_reference`, `metadata` |
| [CustomerPaymentAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPaymentAllocation.php) | `payment_id`, `team_id`, `document_ref`, `amount` |
| [Customer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-api/src/Models/Customer.php) | `customer_name`, `customer_last_name`, `customer_address`, `customer_email`, `customer_phone`, `customer_city`, `credit_hold`, `qbo_id`, `sage_id`, `xero_id`, `team_id` |
<!-- layer-implementation-plan:end -->
