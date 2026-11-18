# Boilerplate: Affiliate Contracts Core Module

## Package contract

**Design package identifier:** `module-affiliate-contracts`
**Intended Composer identity:** `liberusoftware/affiliate-contracts`
**Contracts implemented / exposed:** `AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`
**Domain specification:** [Affiliate Contracts](../features/affiliate-contracts.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Foundation / product specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** AffiliateProgramContract and attribution window DTOs, ReferralAttributionContract and signed touch tokens, ConversionRecorderContract and idempotent clawbacks, CommissionCalculatorContract and tiered rate rules, FraudAndSelfReferralPolicyContract, PayoutSettlementContract and RewardFulfillmentContract.
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Affiliate Contracts. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in [AFFILIATES.md](../../../architecture/AFFILIATES.md).

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
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
| **AffiliateProgramContract and attribution window DTOs** | Model `affiliateprogramcontract and attribution window dtos` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **ReferralAttributionContract and signed touch tokens** | Model `referralattributioncontract and signed touch tokens` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **ConversionRecorderContract and idempotent clawbacks** | Model `conversionrecordercontract and idempotent clawbacks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **CommissionCalculatorContract and tiered rate rules** | Model `commissioncalculatorcontract and tiered rate rules` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **FraudAndSelfReferralPolicyContract** | Model `fraudandselfreferralpolicycontract` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Model `payoutsettlementcontract and rewardfulfillmentcontract` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/affiliate-contracts.md) · [Filament 5](../filament/affiliate-contracts.md) · [Livewire 4](../livewire/affiliate-contracts.md) · [React + Inertia](../react/affiliate-contracts.md) · [Vue + Inertia](../vue/affiliate-contracts.md) · [Nuxt 4](../nuxt/affiliate-contracts.md) · [Next.js](../nextjs/affiliate-contracts.md) · [React Native](../react-native/affiliate-contracts.md) · [Flutter & Dart](../flutter/affiliate-contracts.md)
<!-- core-implementation-plan:end -->
