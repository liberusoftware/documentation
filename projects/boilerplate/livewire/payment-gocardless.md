# Boilerplate: Payment GoCardless Adapter Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-payment-gocardless-livewire`  
**Matching domain module:** `payment-gocardless`  
**Matching core package:** [`module-payment-gocardless`](../core/payment-gocardless.md) (`liberusoftware/payment-gocardless`)  
**Application:** Boilerplate  
**Source feature:** [Payment GoCardless Adapter](../features/payment-gocardless.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

- **GoCardless Billing Requests and Instant Bank Pay (Open Banking):** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS):** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bank payment collection, cancellation, retry, and refunds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **GoCardless Webhook-Signature HMAC-SHA256 verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Late failure, chargeback claim, and payout batch reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-payment-gocardless-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `gocardless-billing-requests-and-instant-bank-pay-open-banking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `direct-debit-mandate-lifecycle-bacs-sepa-ach-pad-becs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bank-payment-collection-cancellation-retry-and-refunds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gocardless-webhook-signature-hmac-sha256-verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `late-failure-chargeback-claim-and-payout-batch-reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/payment-gocardless.md) · [API plan](../api/payment-gocardless.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **GoCardless Billing Requests and Instant Bank Pay (Open Banking)** | Expose a focused Livewire 4 component and namespaced Blade default view for `gocardless billing requests and instant bank pay (open banking)` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS)** | Expose a focused Livewire 4 component and namespaced Blade default view for `direct debit mandate lifecycle (bacs, sepa, ach, pad, becs)` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bank payment collection, cancellation, retry, and refunds** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank payment collection, cancellation, retry, and refunds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **GoCardless Webhook-Signature HMAC-SHA256 verification** | Expose a focused Livewire 4 component and namespaced Blade default view for `gocardless webhook-signature hmac-sha256 verification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Late failure, chargeback claim, and payout batch reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `late failure, chargeback claim, and payout batch reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
