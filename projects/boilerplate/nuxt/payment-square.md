# Boilerplate: Payment Square Adapter Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-square-nuxt`
**Matching domain module:** `payment-square`
**Matching core package:** [`module-payment-square`](../core/payment-square.md) (`liberusoftware/payment-square`)
**Application:** Boilerplate
**Source feature:** [Payment Square Adapter](../features/payment-square.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-square.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-square` public API boundary.

## 2. Module-specific surfaces

- **Square Payments API and Web Payments SDK tokenization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delayed capture, CompletePayment, CancelPayment, and Refunds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Square Cards on File and customer vaulting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Square Terminal API and in-person POS hardware bridge:** page/component/composable/API-action behavior for this module's authorized workflow.
- **HMAC-SHA256 webhook verification, Disputes API, and Payouts:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-square-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `square-payments-api-and-web-payments-sdk-tokenization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delayed-capture-completepayment-cancelpayment-and-refunds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `square-cards-on-file-and-customer-vaulting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `square-terminal-api-and-in-person-pos-hardware-bridge`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `hmac-sha256-webhook-verification-disputes-api-and-payouts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-square.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-square-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Square Payments API and Web Payments SDK tokenization** | Expose composable and Vue 3 component for `square payments api and web payments sdk tokenization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-square.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Delayed capture, CompletePayment, CancelPayment, and Refunds** | Expose composable and Vue 3 component for `delayed capture, completepayment, cancelpayment, and refunds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-square.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Square Cards on File and customer vaulting** | Expose composable and Vue 3 component for `square cards on file and customer vaulting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-square.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Square Terminal API and in-person POS hardware bridge** | Expose composable and Vue 3 component for `square terminal api and in-person pos hardware bridge` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-square.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **HMAC-SHA256 webhook verification, Disputes API, and Payouts** | Expose composable and Vue 3 component for `hmac-sha256 webhook verification, disputes api, and payouts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-square.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
