# Accounting: Accounting Bill Payments Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bill-payments). Observed identity: [`liberusoftware/module-accounting-bill-payments-livewire`](../../../modules/source/liberusoftware--module-accounting-bill-payments-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-bill-payments-livewire`  
**Matching domain module:** `accounting-bill-payments`  
**Application:** Accounting  
**Source feature:** [Accounting Bill Payments](../features/accounting-bill-payments.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Payment proposals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Due-date/discount optimization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bank details validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maker-checker approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Files/APIs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Remittances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-bill-payments-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingBillPayments::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `payment-proposals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `due-date-discount-optimization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bank-details-validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maker-checker-approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `files-apis`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `remittances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-bill-payments` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-bill-payments.md) · [API plan](../api/accounting-bill-payments.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Payment proposals** | Expose a focused Livewire 4 component and namespaced Blade default view for `payment proposals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Due-date/discount optimization** | Expose a focused Livewire 4 component and namespaced Blade default view for `due-date/discount optimization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bank details validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank details validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maker-checker approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `maker-checker approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Files/APIs** | Expose a focused Livewire 4 component and namespaced Blade default view for `files/apis` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Remittances** | Expose a focused Livewire 4 component and namespaced Blade default view for `remittances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Status** | Expose a focused Livewire 4 component and namespaced Blade default view for `status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Proposals.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-livewire/src/Livewire/Proposals.php) · [BillPaymentsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-livewire/src/BillPaymentsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BillPaymentOptimizationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Queries/BillPaymentOptimizationQuery.php) | `public function handle(BillPaymentProposal $payment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/ApproveBillPayment.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [CreateBillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/CreateBillPaymentProposal.php) | `public function handle(array $attributes): BillPaymentProposal` |
| [MarkBillPaymentPaid.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/MarkBillPaymentPaid.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [RejectBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RejectBillPayment.php) | `public function handle(BillPaymentProposal $payment, string $reason): BillPaymentProposal` |
| [RequestBillPaymentApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RequestBillPaymentApproval.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [SubmitBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/SubmitBillPayment.php) | `public function handle(BillPaymentProposal $payment, PaymentProviderAdapter $adapter): BillPaymentProposal` |
| [BillPaymentsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Policies/BillPaymentsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $payment): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $payment): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Models/BillPaymentProposal.php) | `team_id`, `supplier_id`, `bill_reference`, `amount`, `currency`, `due_date`, `discount_date`, `discount_rate`, `payment_date`, `bank_details`, `provider`, `provider_connection_id`, `payment_payload`, `idempotency_key`, `status`, `requested_by`, `approved_by`, `approved_at`, `submitted_at`, `paid_at`, `rejected_at`, `failure_code`, `failure_message`, `provider_reference`, `provider_result`, `remittance_reference`, `remittance_sent_at`, `metadata` |
| [Bill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/Bill.php) | `vendor_id`, `bill_number`, `bill_date`, `due_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `amount_paid`, `tax_rate_id`, `status`, `payment_status`, `purchase_order_id`, `reference_number`, `notes`, `document_path`, `approved_by`, `approved_at`, `approval_status`, `rejection_reason`, `team_id`, `is_recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
| [BillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/BillPayment.php) | `bill_id`, `payment_date`, `amount`, `payment_method`, `reference_number`, `bank_account_id`, `notes` |
<!-- layer-implementation-plan:end -->
