# Boilerplate: Affiliate Contracts Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-affiliate-contracts-nuxt`
**Matching domain module:** `affiliate-contracts`
**Matching core package:** [`module-affiliate-contracts`](../core/affiliate-contracts.md) (`liberusoftware/affiliate-contracts`)
**Application:** Boilerplate
**Source feature:** [Affiliate Contracts](../features/affiliate-contracts.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/affiliate-contracts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `affiliate-contracts` public API boundary.

## 2. Module-specific surfaces

- **AffiliateProgramContract and attribution window DTOs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **ReferralAttributionContract and signed touch tokens:** page/component/composable/API-action behavior for this module's authorized workflow.
- **ConversionRecorderContract and idempotent clawbacks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CommissionCalculatorContract and tiered rate rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **FraudAndSelfReferralPolicyContract:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PayoutSettlementContract and RewardFulfillmentContract:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-affiliate-contracts-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `affiliateprogramcontract-and-attribution-window-dtos`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `referralattributioncontract-and-signed-touch-tokens`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conversionrecordercontract-and-idempotent-clawbacks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commissioncalculatorcontract-and-tiered-rate-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fraudandselfreferralpolicycontract`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payoutsettlementcontract-and-rewardfulfillmentcontract`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/affiliate-contracts.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-affiliate-contracts-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **AffiliateProgramContract and attribution window DTOs** | Expose composable and Vue 3 component for `affiliateprogramcontract and attribution window dtos` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **ReferralAttributionContract and signed touch tokens** | Expose composable and Vue 3 component for `referralattributioncontract and signed touch tokens` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **ConversionRecorderContract and idempotent clawbacks** | Expose composable and Vue 3 component for `conversionrecordercontract and idempotent clawbacks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **CommissionCalculatorContract and tiered rate rules** | Expose composable and Vue 3 component for `commissioncalculatorcontract and tiered rate rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **FraudAndSelfReferralPolicyContract** | Expose composable and Vue 3 component for `fraudandselfreferralpolicycontract` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Expose composable and Vue 3 component for `payoutsettlementcontract and rewardfulfillmentcontract` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliate-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
