# Billing: Referrals and Advocate Rewards Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#referrals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-referrals-nuxt`
**Matching domain module:** `referrals`
**Matching core package:** [`module-billing-referrals`](../core/referrals.md) (`liberusoftware/billing-referrals`)
**Application:** Billing
**Source feature:** [Referrals and Advocate Rewards](../features/referrals.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/referrals.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `referrals` public API boundary.

## 2. Module-specific surfaces

- **Referral programs and two-sided reward rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Advocate share links and referral codes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Referred signup and subscription qualification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate, household, and self-referral prevention:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Automated reward fulfillment and clawback handling:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-referrals-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `referral-programs-and-two-sided-reward-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `advocate-share-links-and-referral-codes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `referred-signup-and-subscription-qualification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-household-and-self-referral-prevention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `automated-reward-fulfillment-and-clawback-handling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/referrals.md)) |
| Capability Nuxt module skeleton | `module-billing-referrals-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Referral programs and two-sided reward rules** | Expose composable and Vue 3 component for `referral programs and two-sided reward rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/referrals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Advocate share links and referral codes** | Expose composable and Vue 3 component for `advocate share links and referral codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/referrals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Referred signup and subscription qualification** | Expose composable and Vue 3 component for `referred signup and subscription qualification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/referrals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Duplicate, household, and self-referral prevention** | Expose composable and Vue 3 component for `duplicate, household, and self-referral prevention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/referrals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Automated reward fulfillment and clawback handling** | Expose composable and Vue 3 component for `automated reward fulfillment and clawback handling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/referrals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
