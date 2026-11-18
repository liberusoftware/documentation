# Boilerplate: Affiliates and Partner Programs Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-affiliates-nuxt`
**Matching domain module:** `affiliates`
**Matching core package:** [`module-affiliates`](../core/affiliates.md) (`liberusoftware/affiliate-core`)
**Application:** Boilerplate
**Source feature:** [Affiliates and Partner Programs](../features/affiliates.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/affiliates.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `affiliates` public API boundary.

## 2. Module-specific surfaces

- **Affiliate program and commission tier rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partner applications, KYC/tax readiness, and approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tracking links, campaign parameters, and promo codes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Authoritative conversion ingestion and hold ledger:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Automated refund, cancellation, and dispute clawbacks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Self-referral, velocity, and fraud screening:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payout approval batches and settlement handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-affiliates-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `affiliate-program-and-commission-tier-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partner-applications-kyc-tax-readiness-and-approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tracking-links-campaign-parameters-and-promo-codes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `authoritative-conversion-ingestion-and-hold-ledger`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `automated-refund-cancellation-and-dispute-clawbacks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `self-referral-velocity-and-fraud-screening`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payout-approval-batches-and-settlement-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/affiliates.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-affiliates-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Expose composable and Vue 3 component for `affiliate program and commission tier rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Partner applications, KYC/tax readiness, and approval** | Expose composable and Vue 3 component for `partner applications, kyc/tax readiness, and approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Tracking links, campaign parameters, and promo codes** | Expose composable and Vue 3 component for `tracking links, campaign parameters, and promo codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Authoritative conversion ingestion and hold ledger** | Expose composable and Vue 3 component for `authoritative conversion ingestion and hold ledger` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Automated refund, cancellation, and dispute clawbacks** | Expose composable and Vue 3 component for `automated refund, cancellation, and dispute clawbacks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Self-referral, velocity, and fraud screening** | Expose composable and Vue 3 component for `self-referral, velocity, and fraud screening` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Payout approval batches and settlement handoff** | Expose composable and Vue 3 component for `payout approval batches and settlement handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/affiliates.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
