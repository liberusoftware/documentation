# Boilerplate: Payment Square Adapter Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-square). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-payment-square-livewire`  
**Matching domain module:** `payment-square`  
**Matching core package:** [`module-payment-square`](../core/payment-square.md) (`liberusoftware/payment-square`)  
**Application:** Boilerplate  
**Source feature:** [Payment Square Adapter](../features/payment-square.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

- **Square Payments API and Web Payments SDK tokenization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delayed capture, CompletePayment, CancelPayment, and Refunds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Square Cards on File and customer vaulting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Square Terminal API and in-person POS hardware bridge:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **HMAC-SHA256 webhook verification, Disputes API, and Payouts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-payment-square-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `square-payments-api-and-web-payments-sdk-tokenization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delayed-capture-completepayment-cancelpayment-and-refunds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `square-cards-on-file-and-customer-vaulting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `square-terminal-api-and-in-person-pos-hardware-bridge`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hmac-sha256-webhook-verification-disputes-api-and-payouts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/payment-square.md) · [API plan](../api/payment-square.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Square Payments API and Web Payments SDK tokenization** | Expose a focused Livewire 4 component and namespaced Blade default view for `square payments api and web payments sdk tokenization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delayed capture, CompletePayment, CancelPayment, and Refunds** | Expose a focused Livewire 4 component and namespaced Blade default view for `delayed capture, completepayment, cancelpayment, and refunds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Square Cards on File and customer vaulting** | Expose a focused Livewire 4 component and namespaced Blade default view for `square cards on file and customer vaulting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Square Terminal API and in-person POS hardware bridge** | Expose a focused Livewire 4 component and namespaced Blade default view for `square terminal api and in-person pos hardware bridge` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **HMAC-SHA256 webhook verification, Disputes API, and Payouts** | Expose a focused Livewire 4 component and namespaced Blade default view for `hmac-sha256 webhook verification, disputes api, and payouts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
