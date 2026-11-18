# Boilerplate: Affiliates and Partner Programs Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-affiliates`
**Intended Composer identity:** `liberusoftware/affiliate-core`
**Contracts implemented / exposed:** `liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`
**Domain specification:** [Affiliates and Partner Programs](../features/affiliates.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Affiliate program and commission tier rules, Partner applications, KYC/tax readiness, and approval, Tracking links, campaign parameters, and promo codes, Authoritative conversion ingestion and hold ledger, Automated refund, cancellation, and dispute clawbacks, Self-referral, velocity, and fraud screening, Payout approval batches and settlement handoff.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Affiliates and Partner Programs. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [AFFILIATES.md](../../../architecture/AFFILIATES.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, contract compliance, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, Next.js, Nuxt, React Native, and Flutter/Dart consumers use only this package's public contracts. See [AFFILIATES.md](../../../architecture/AFFILIATES.md), [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Model `affiliate program and commission tier rules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Partner applications, KYC/tax readiness, and approval** | Model `partner applications, kyc/tax readiness, and approval` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Tracking links, campaign parameters, and promo codes** | Model `tracking links, campaign parameters, and promo codes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Authoritative conversion ingestion and hold ledger** | Model `authoritative conversion ingestion and hold ledger` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Automated refund, cancellation, and dispute clawbacks** | Model `automated refund, cancellation, and dispute clawbacks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Self-referral, velocity, and fraud screening** | Model `self-referral, velocity, and fraud screening` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Payout approval batches and settlement handoff** | Model `payout approval batches and settlement handoff` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/affiliates.md) · [Filament 5](../filament/affiliates.md) · [Livewire 4](../livewire/affiliates.md) · [React + Inertia](../react/affiliates.md) · [Vue + Inertia](../vue/affiliates.md) · [Nuxt 4](../nuxt/affiliates.md) · [Next.js](../nextjs/affiliates.md) · [React Native](../react-native/affiliates.md) · [Flutter & Dart](../flutter/affiliates.md)
<!-- core-implementation-plan:end -->
