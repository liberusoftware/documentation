# Boilerplate: Affiliate Contracts Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-affiliate-contracts-livewire`  
**Matching domain module:** `affiliate-contracts`  
**Matching core package:** [`module-affiliate-contracts`](../core/affiliate-contracts.md) (`liberusoftware/affiliate-contracts`)  
**Application:** Boilerplate  
**Source feature:** [Affiliate Contracts](../features/affiliate-contracts.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

- **AffiliateProgramContract and attribution window DTOs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **ReferralAttributionContract and signed touch tokens:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **ConversionRecorderContract and idempotent clawbacks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CommissionCalculatorContract and tiered rate rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **FraudAndSelfReferralPolicyContract:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **PayoutSettlementContract and RewardFulfillmentContract:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-affiliate-contracts-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `affiliateprogramcontract-and-attribution-window-dtos`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `referralattributioncontract-and-signed-touch-tokens`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conversionrecordercontract-and-idempotent-clawbacks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `commissioncalculatorcontract-and-tiered-rate-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fraudandselfreferralpolicycontract`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payoutsettlementcontract-and-rewardfulfillmentcontract`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/affiliate-contracts.md) · [API plan](../api/affiliate-contracts.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **AffiliateProgramContract and attribution window DTOs** | Expose a focused Livewire 4 component and namespaced Blade default view for `affiliateprogramcontract and attribution window dtos` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **ReferralAttributionContract and signed touch tokens** | Expose a focused Livewire 4 component and namespaced Blade default view for `referralattributioncontract and signed touch tokens` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **ConversionRecorderContract and idempotent clawbacks** | Expose a focused Livewire 4 component and namespaced Blade default view for `conversionrecordercontract and idempotent clawbacks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CommissionCalculatorContract and tiered rate rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `commissioncalculatorcontract and tiered rate rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **FraudAndSelfReferralPolicyContract** | Expose a focused Livewire 4 component and namespaced Blade default view for `fraudandselfreferralpolicycontract` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Expose a focused Livewire 4 component and namespaced Blade default view for `payoutsettlementcontract and rewardfulfillmentcontract` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
