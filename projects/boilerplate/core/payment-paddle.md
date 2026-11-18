# Boilerplate: Payment Paddle Adapter Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-paddle). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-payment-paddle`
**Intended Composer identity:** `liberusoftware/payment-paddle`
**Contracts implemented / exposed:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`
**Domain specification:** [Payment Paddle Adapter](../features/payment-paddle.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Paddle Billing transactions and Merchant-of-Record checkout, Paddle adjustments for full/partial refunds and credits, Customer saved payment methods and subscription bridge, Paddle-Signature ts/h1 HMAC webhook verification, Tax, Merchant-of-Record fee, and payout reconciliation.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Payment Paddle Adapter. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [PAYMENTS.md](../../../architecture/PAYMENTS.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
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
| **Paddle Billing transactions and Merchant-of-Record checkout** | Model `paddle billing transactions and merchant-of-record checkout` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Paddle adjustments for full/partial refunds and credits** | Model `paddle adjustments for full/partial refunds and credits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Customer saved payment methods and subscription bridge** | Model `customer saved payment methods and subscription bridge` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Paddle-Signature ts/h1 HMAC webhook verification** | Model `paddle-signature ts/h1 hmac webhook verification` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tax, Merchant-of-Record fee, and payout reconciliation** | Model `tax, merchant-of-record fee, and payout reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/payment-paddle.md) · [Filament 5](../filament/payment-paddle.md) · [Livewire 4](../livewire/payment-paddle.md) · [React + Inertia](../react/payment-paddle.md) · [Vue + Inertia](../vue/payment-paddle.md) · [Nuxt 4](../nuxt/payment-paddle.md) · [Next.js](../nextjs/payment-paddle.md) · [React Native](../react-native/payment-paddle.md) · [Flutter & Dart](../flutter/payment-paddle.md)
<!-- core-implementation-plan:end -->
