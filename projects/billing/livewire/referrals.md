# Billing: Referrals and Advocate Rewards Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-referrals-livewire`  
**Matching domain module:** `referrals`  
**Matching core package:** [`module-billing-referrals`](../core/referrals.md) (`liberusoftware/billing-referrals`)  
**Application:** Billing  
**Source feature:** [Referrals and Advocate Rewards](../features/referrals.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

- **Referral programs and two-sided reward rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Advocate share links and referral codes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Referred signup and subscription qualification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicate, household, and self-referral prevention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Automated reward fulfillment and clawback handling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-referrals-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `referral-programs-and-two-sided-reward-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `advocate-share-links-and-referral-codes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `referred-signup-and-subscription-qualification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicate-household-and-self-referral-prevention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `automated-reward-fulfillment-and-clawback-handling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/referrals.md) · [API plan](../api/referrals.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Referral programs and two-sided reward rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `referral programs and two-sided reward rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Advocate share links and referral codes** | Expose a focused Livewire 4 component and namespaced Blade default view for `advocate share links and referral codes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Referred signup and subscription qualification** | Expose a focused Livewire 4 component and namespaced Blade default view for `referred signup and subscription qualification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicate, household, and self-referral prevention** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicate, household, and self-referral prevention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Automated reward fulfillment and clawback handling** | Expose a focused Livewire 4 component and namespaced Blade default view for `automated reward fulfillment and clawback handling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
