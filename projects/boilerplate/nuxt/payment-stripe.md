# Boilerplate: Payment Stripe Adapter Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-stripe-nuxt`
**Matching domain module:** `payment-stripe`
**Matching core package:** [`module-payment-stripe`](../core/payment-stripe.md) (`liberusoftware/payment-stripe`)
**Application:** Boilerplate
**Source feature:** [Payment Stripe Adapter](../features/payment-stripe.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-stripe.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-stripe` public API boundary.

## 2. Module-specific surfaces

- **Latest Stripe SDK client and pinned API version:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PaymentIntents, Checkout Sessions, and 3DS2/SCA confirmation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SetupIntents and PaymentMethod vaulting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Full/partial capture, cancellation, and idempotent refunds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stripe-Signature webhook verification and normalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stripe disputes, Terminal POS, and BalanceTransaction reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-stripe-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `latest-stripe-sdk-client-and-pinned-api-version`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `paymentintents-checkout-sessions-and-3ds2-sca-confirmation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `setupintents-and-paymentmethod-vaulting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `full-partial-capture-cancellation-and-idempotent-refunds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stripe-signature-webhook-verification-and-normalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stripe-disputes-terminal-pos-and-balancetransaction-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-stripe.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-stripe-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Latest Stripe SDK client and pinned API version** | Expose composable and Vue 3 component for `latest stripe sdk client and pinned api version` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **PaymentIntents, Checkout Sessions, and 3DS2/SCA confirmation** | Expose composable and Vue 3 component for `paymentintents, checkout sessions, and 3ds2/sca confirmation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **SetupIntents and PaymentMethod vaulting** | Expose composable and Vue 3 component for `setupintents and paymentmethod vaulting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Full/partial capture, cancellation, and idempotent refunds** | Expose composable and Vue 3 component for `full/partial capture, cancellation, and idempotent refunds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Stripe-Signature webhook verification and normalization** | Expose composable and Vue 3 component for `stripe-signature webhook verification and normalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Stripe disputes, Terminal POS, and BalanceTransaction reconciliation** | Expose composable and Vue 3 component for `stripe disputes, terminal pos, and balancetransaction reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-stripe.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
