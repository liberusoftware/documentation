# Billing: Payments Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payments). Observed identity: [`liberusoftware/module-billing-payments-livewire`](../../../modules/source/liberusoftware--module-billing-payments-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-payments-livewire`  
**Matching domain module:** `billing-payments`  
**Application:** Billing  
**Source feature:** [Payments](../features/payments.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Unified payment-contracts and payment-core integration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Methods and vaulted payment instruments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mandates and Direct Debit lifecycles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gateway drivers and capability discovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capture, partial invoice payments, and allocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Refunds and credit reversals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes and chargeback evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation and settlement batches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-payments-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-payments::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `unified-payment-contracts-and-payment-core-integration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `methods-and-vaulted-payment-instruments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mandates-and-direct-debit-lifecycles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gateway-drivers-and-capability-discovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capture-partial-invoice-payments-and-allocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `refunds-and-credit-reversals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes-and-chargeback-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation-and-settlement-batches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-payments` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/payments.md) · [API plan](../api/payments.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Unified payment-contracts and payment-core integration** | Expose a focused Livewire 4 component and namespaced Blade default view for `unified payment-contracts and payment-core integration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Methods and vaulted payment instruments** | Expose a focused Livewire 4 component and namespaced Blade default view for `methods and vaulted payment instruments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mandates and Direct Debit lifecycles** | Expose a focused Livewire 4 component and namespaced Blade default view for `mandates and direct debit lifecycles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gateway drivers and capability discovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `gateway drivers and capability discovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capture, partial invoice payments, and allocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `capture, partial invoice payments, and allocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Refunds and credit reversals** | Expose a focused Livewire 4 component and namespaced Blade default view for `refunds and credit reversals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes and chargeback evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes and chargeback evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation and settlement batches** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation and settlement batches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PaymentList.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-livewire/src/Components/PaymentList.php) · [PaymentMethods.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-livewire/src/Components/PaymentMethods.php) · [PaymentOperations.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-livewire/src/Components/PaymentOperations.php) · [PaymentsLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-livewire/src/PaymentsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListPayments.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Queries/ListPayments.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/AllocatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, ?int $invoiceId = null): PaymentAllocation` |
| [CapturePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CapturePayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment): Payment` |
| [CreatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Payment` |
| [CreatePaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMandate` |
| [CreatePaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMethod` |
| [OpenDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/OpenDispute.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason): PaymentDispute` |
| [ReconcilePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/ReconcilePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, string $providerReference, bool $matched = true, ?string $notes = null): PaymentReconciliation` |
| [RefundPayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/RefundPayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason = 'requested'): PaymentRefund` |
| [TransitionPaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMandate $mandate, string $status): PaymentMandate` |
| [TransitionPaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMethod $method, PaymentMethodStatus $status): PaymentMethod` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Payment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/Payment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentAllocation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentAllocation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMandate.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMethod.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentReconciliation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentReconciliation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentRefund.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentRefund.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
