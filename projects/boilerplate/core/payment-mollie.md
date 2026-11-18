# Boilerplate: Payment Mollie Adapter Core Module

## Package contract

**Design package identifier:** `module-payment-mollie`
**Intended Composer identity:** `liberusoftware/payment-mollie`
**Contracts implemented / exposed:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`
**Domain specification:** [Payment Mollie Adapter](../features/payment-mollie.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Mollie Payments API, Components, and APM redirects, Mollie Customers and SEPA/card recurring Mandates, Authorized payment capture, release, and partial refunds, Mollie webhook verification and authoritative state fetch, Chargeback handling and Settlements API reconciliation.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Payment Mollie Adapter. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [PAYMENTS.md](../../../architecture/PAYMENTS.md).

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
| **Mollie Payments API, Components, and APM redirects** | Model `mollie payments api, components, and apm redirects` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Mollie Customers and SEPA/card recurring Mandates** | Model `mollie customers and sepa/card recurring mandates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Authorized payment capture, release, and partial refunds** | Model `authorized payment capture, release, and partial refunds` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Mollie webhook verification and authoritative state fetch** | Model `mollie webhook verification and authoritative state fetch` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Chargeback handling and Settlements API reconciliation** | Model `chargeback handling and settlements api reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/payment-mollie.md) · [Filament 5](../filament/payment-mollie.md) · [Livewire 4](../livewire/payment-mollie.md) · [React + Inertia](../react/payment-mollie.md) · [Vue + Inertia](../vue/payment-mollie.md) · [Nuxt 4](../nuxt/payment-mollie.md) · [Next.js](../nextjs/payment-mollie.md) · [React Native](../react-native/payment-mollie.md) · [Flutter & Dart](../flutter/payment-mollie.md)
<!-- core-implementation-plan:end -->
