# Boilerplate: Payment Core Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-payment-core`
**Intended Composer identity:** `liberusoftware/payment-core`
**Contracts implemented / exposed:** `liberusoftware/payment-contracts (PaymentGatewayRegistryContract, PaymentOrchestratorContract, WebhookInboxProcessorContract, SettlementReconciliationEngineContract)`
**Domain specification:** [Payment Core](../features/payment-core.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Payment gateway registry and tenant/currency routing, Payment intent orchestration and state machine, Idempotency locking and immutable transaction ledger, Tokenized payment method vault and mandate directory, Verified webhook inbox and out-of-order reconciliation, Dispute management and settlement batch reconciliation.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Payment Core. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [PAYMENTS.md](../../../architecture/PAYMENTS.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`liberusoftware/payment-contracts (PaymentGatewayRegistryContract, PaymentOrchestratorContract, WebhookInboxProcessorContract, SettlementReconciliationEngineContract)`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
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
| **Payment gateway registry and tenant/currency routing** | Model `payment gateway registry and tenant/currency routing` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Payment intent orchestration and state machine** | Model `payment intent orchestration and state machine` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Idempotency locking and immutable transaction ledger** | Model `idempotency locking and immutable transaction ledger` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tokenized payment method vault and mandate directory** | Model `tokenized payment method vault and mandate directory` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Verified webhook inbox and out-of-order reconciliation** | Model `verified webhook inbox and out-of-order reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Dispute management and settlement batch reconciliation** | Model `dispute management and settlement batch reconciliation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/payment-core.md) · [Filament 5](../filament/payment-core.md) · [Livewire 4](../livewire/payment-core.md) · [React + Inertia](../react/payment-core.md) · [Vue + Inertia](../vue/payment-core.md) · [Nuxt 4](../nuxt/payment-core.md) · [Next.js](../nextjs/payment-core.md) · [React Native](../react-native/payment-core.md) · [Flutter & Dart](../flutter/payment-core.md)
<!-- core-implementation-plan:end -->
