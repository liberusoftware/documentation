# Boilerplate: Payment Square Adapter Core Module

## Package contract

**Design package identifier:** `module-payment-square`
**Intended Composer identity:** `liberusoftware/payment-square`
**Contracts implemented / exposed:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`
**Domain specification:** [Payment Square Adapter](../features/payment-square.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Square Payments API and Web Payments SDK tokenization, Delayed capture, CompletePayment, CancelPayment, and Refunds, Square Cards on File and customer vaulting, Square Terminal API and in-person POS hardware bridge, HMAC-SHA256 webhook verification, Disputes API, and Payouts.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Payment Square Adapter. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [PAYMENTS.md](../../../architecture/PAYMENTS.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, contract compliance, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, Next.js, Nuxt, React Native, and Flutter/Dart consumers use only this package's public contracts. See [PAYMENTS.md](../../../architecture/PAYMENTS.md), [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Square Payments API and Web Payments SDK tokenization** | Model `square payments api and web payments sdk tokenization` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delayed capture, CompletePayment, CancelPayment, and Refunds** | Model `delayed capture, completepayment, cancelpayment, and refunds` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Square Cards on File and customer vaulting** | Model `square cards on file and customer vaulting` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Square Terminal API and in-person POS hardware bridge** | Model `square terminal api and in-person pos hardware bridge` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **HMAC-SHA256 webhook verification, Disputes API, and Payouts** | Model `hmac-sha256 webhook verification, disputes api, and payouts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/payment-square.md) · [Filament 5](../filament/payment-square.md) · [Livewire 4](../livewire/payment-square.md) · [React + Inertia](../react/payment-square.md) · [Vue + Inertia](../vue/payment-square.md) · [Nuxt 4](../nuxt/payment-square.md) · [Next.js](../nextjs/payment-square.md) · [React Native](../react-native/payment-square.md) · [Flutter & Dart](../flutter/payment-square.md)
<!-- core-implementation-plan:end -->
