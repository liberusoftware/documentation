# Billing: Referrals and Advocate Rewards Core Module

## Package contract

**Design package identifier:** `module-billing-referrals`
**Intended Composer identity:** `liberusoftware/billing-referrals`
**Contracts implemented / exposed:** `liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`
**Domain specification:** [Referrals and Advocate Rewards](../features/referrals.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Foundation / product specification:** [BILLING.md](../BILLING.md)
**Capability:** Referral programs and two-sided reward rules, Advocate share links and referral codes, Referred signup and subscription qualification, Duplicate, household, and self-referral prevention, Automated reward fulfillment and clawback handling.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Referrals and Advocate Rewards. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [AFFILIATES.md](../../../architecture/AFFILIATES.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
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
| **Referral programs and two-sided reward rules** | Model `referral programs and two-sided reward rules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Advocate share links and referral codes** | Model `advocate share links and referral codes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Referred signup and subscription qualification** | Model `referred signup and subscription qualification` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Duplicate, household, and self-referral prevention** | Model `duplicate, household, and self-referral prevention` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Automated reward fulfillment and clawback handling** | Model `automated reward fulfillment and clawback handling` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/referrals.md) · [Filament 5](../filament/referrals.md) · [Livewire 4](../livewire/referrals.md) · [React + Inertia](../react/referrals.md) · [Vue + Inertia](../vue/referrals.md) · [Nuxt 4](../nuxt/referrals.md) · [Next.js](../nextjs/referrals.md) · [React Native](../react-native/referrals.md) · [Flutter & Dart](../flutter/referrals.md)
<!-- core-implementation-plan:end -->
