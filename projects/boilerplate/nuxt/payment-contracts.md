# Boilerplate: Payment Contracts Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-contracts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-contracts-nuxt`
**Matching domain module:** `payment-contracts`
**Matching core package:** [`module-payment-contracts`](../core/payment-contracts.md) (`liberusoftware/payment-contracts`)
**Application:** Boilerplate
**Source feature:** [Payment Contracts](../features/payment-contracts.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-contracts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-contracts` public API boundary.

## 2. Module-specific surfaces

- **PaymentGatewayAdapterContract and capability descriptors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PaymentIntentServiceContract and 3DS/SCA client actions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PaymentCaptureAndRefundContract with idempotency:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SavedPaymentMethodVaultContract and mandates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **MerchantWebhookVerifierContract:** page/component/composable/API-action behavior for this module's authorized workflow.
- **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-contracts-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `paymentgatewayadaptercontract-and-capability-descriptors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `paymentintentservicecontract-and-3ds-sca-client-actions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `paymentcaptureandrefundcontract-with-idempotency`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `savedpaymentmethodvaultcontract-and-mandates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `merchantwebhookverifiercontract`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disputeandchargebackhandlercontract-and-payoutandsettlementreconcilercontract`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-contracts.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-contracts-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **PaymentGatewayAdapterContract and capability descriptors** | Expose composable and Vue 3 component for `paymentgatewayadaptercontract and capability descriptors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **PaymentIntentServiceContract and 3DS/SCA client actions** | Expose composable and Vue 3 component for `paymentintentservicecontract and 3ds/sca client actions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **PaymentCaptureAndRefundContract with idempotency** | Expose composable and Vue 3 component for `paymentcaptureandrefundcontract with idempotency` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **SavedPaymentMethodVaultContract and mandates** | Expose composable and Vue 3 component for `savedpaymentmethodvaultcontract and mandates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **MerchantWebhookVerifierContract** | Expose composable and Vue 3 component for `merchantwebhookverifiercontract` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract** | Expose composable and Vue 3 component for `disputeandchargebackhandlercontract and payoutandsettlementreconcilercontract` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-contracts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
