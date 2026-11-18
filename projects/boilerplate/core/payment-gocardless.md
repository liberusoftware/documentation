# Boilerplate: Payment GoCardless Adapter Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-gocardless). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-payment-gocardless`
**Intended Composer identity:** `liberusoftware/payment-gocardless`
**Contracts implemented / exposed:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`
**Domain specification:** [Payment GoCardless Adapter](../features/payment-gocardless.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** GoCardless Billing Requests and Instant Bank Pay (Open Banking), Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS), Bank payment collection, cancellation, retry, and refunds, GoCardless Webhook-Signature HMAC-SHA256 verification, Late failure, chargeback claim, and payout batch reconciliation.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Payment GoCardless Adapter. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [PAYMENTS.md](../../../architecture/PAYMENTS.md).

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
| **GoCardless Billing Requests and Instant Bank Pay (Open Banking)** | Model `gocardless billing requests and instant bank pay (open banking)` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS)** | Model `direct debit mandate lifecycle (bacs, sepa, ach, pad, becs)` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Bank payment collection, cancellation, retry, and refunds** | Model `bank payment collection, cancellation, retry, and refunds` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **GoCardless Webhook-Signature HMAC-SHA256 verification** | Model `gocardless webhook-signature hmac-sha256 verification` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Late failure, chargeback claim, and payout batch reconciliation** | Model `late failure, chargeback claim, and payout batch reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/payment-gocardless.md) · [Filament 5](../filament/payment-gocardless.md) · [Livewire 4](../livewire/payment-gocardless.md) · [React + Inertia](../react/payment-gocardless.md) · [Vue + Inertia](../vue/payment-gocardless.md) · [Nuxt 4](../nuxt/payment-gocardless.md) · [Next.js](../nextjs/payment-gocardless.md) · [React Native](../react-native/payment-gocardless.md) · [Flutter & Dart](../flutter/payment-gocardless.md)
<!-- core-implementation-plan:end -->
