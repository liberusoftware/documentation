# Boilerplate: Payment Mollie Adapter Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-mollie-nuxt`
**Matching domain module:** `payment-mollie`
**Matching core package:** [`module-payment-mollie`](../core/payment-mollie.md) (`liberusoftware/payment-mollie`)
**Application:** Boilerplate
**Source feature:** [Payment Mollie Adapter](../features/payment-mollie.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-mollie.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-mollie` public API boundary.

## 2. Module-specific surfaces

- **Mollie Payments API, Components, and APM redirects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mollie Customers and SEPA/card recurring Mandates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Authorized payment capture, release, and partial refunds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mollie webhook verification and authoritative state fetch:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Chargeback handling and Settlements API reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-mollie-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `mollie-payments-api-components-and-apm-redirects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mollie-customers-and-sepa-card-recurring-mandates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `authorized-payment-capture-release-and-partial-refunds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mollie-webhook-verification-and-authoritative-state-fetch`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `chargeback-handling-and-settlements-api-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-mollie.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-mollie-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Mollie Payments API, Components, and APM redirects** | Expose composable and Vue 3 component for `mollie payments api, components, and apm redirects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-mollie.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Mollie Customers and SEPA/card recurring Mandates** | Expose composable and Vue 3 component for `mollie customers and sepa/card recurring mandates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-mollie.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Authorized payment capture, release, and partial refunds** | Expose composable and Vue 3 component for `authorized payment capture, release, and partial refunds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-mollie.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Mollie webhook verification and authoritative state fetch** | Expose composable and Vue 3 component for `mollie webhook verification and authoritative state fetch` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-mollie.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Chargeback handling and Settlements API reconciliation** | Expose composable and Vue 3 component for `chargeback handling and settlements api reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-mollie.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
