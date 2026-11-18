# Boilerplate: Payment Adyen Adapter Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-adyen-nuxt`
**Matching domain module:** `payment-adyen`
**Matching core package:** [`module-payment-adyen`](../core/payment-adyen.md) (`liberusoftware/payment-adyen`)
**Application:** Boilerplate
**Source feature:** [Payment Adyen Adapter](../features/payment-adyen.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-adyen.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-adyen` public API boundary.

## 2. Module-specific surfaces

- **Adyen Checkout sessions, /payments, and 3DS2 action handling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Asynchronous capture, technical cancel, and refund modifications:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tokenization and recurring storedPaymentMethod vaulting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adyen HMAC-SHA256 webhook notification verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Omnichannel POS Terminal API and settlement batch reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-adyen-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `adyen-checkout-sessions-payments-and-3ds2-action-handling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `asynchronous-capture-technical-cancel-and-refund-modifications`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tokenization-and-recurring-storedpaymentmethod-vaulting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adyen-hmac-sha256-webhook-notification-verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `omnichannel-pos-terminal-api-and-settlement-batch-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-adyen.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-adyen-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Adyen Checkout sessions, /payments, and 3DS2 action handling** | Expose composable and Vue 3 component for `adyen checkout sessions, /payments, and 3ds2 action handling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-adyen.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Asynchronous capture, technical cancel, and refund modifications** | Expose composable and Vue 3 component for `asynchronous capture, technical cancel, and refund modifications` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-adyen.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Tokenization and recurring storedPaymentMethod vaulting** | Expose composable and Vue 3 component for `tokenization and recurring storedpaymentmethod vaulting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-adyen.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Adyen HMAC-SHA256 webhook notification verification** | Expose composable and Vue 3 component for `adyen hmac-sha256 webhook notification verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-adyen.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Omnichannel POS Terminal API and settlement batch reconciliation** | Expose composable and Vue 3 component for `omnichannel pos terminal api and settlement batch reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-adyen.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
