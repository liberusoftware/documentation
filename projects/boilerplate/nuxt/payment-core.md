# Boilerplate: Payment Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-payment-core-nuxt`
**Matching domain module:** `payment-core`
**Matching core package:** [`module-payment-core`](../core/payment-core.md) (`liberusoftware/payment-core`)
**Application:** Boilerplate
**Source feature:** [Payment Core](../features/payment-core.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`liberusoftware/payment-contracts (PaymentGatewayRegistryContract, PaymentOrchestratorContract, WebhookInboxProcessorContract, SettlementReconciliationEngineContract)`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `payment-core` public API boundary.

## 2. Module-specific surfaces

- **Payment gateway registry and tenant/currency routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment intent orchestration and state machine:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Idempotency locking and immutable transaction ledger:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tokenized payment method vault and mandate directory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Verified webhook inbox and out-of-order reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dispute management and settlement batch reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-payment-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `payment-gateway-registry-and-tenant-currency-routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-intent-orchestration-and-state-machine`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `idempotency-locking-and-immutable-transaction-ledger`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tokenized-payment-method-vault-and-mandate-directory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `verified-webhook-inbox-and-out-of-order-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dispute-management-and-settlement-batch-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payment-core.md)) |
| Capability Nuxt module skeleton | `module-boilerplate-payment-core-nuxt` | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Payment gateway registry and tenant/currency routing** | Expose composable and Vue 3 component for `payment gateway registry and tenant/currency routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Payment intent orchestration and state machine** | Expose composable and Vue 3 component for `payment intent orchestration and state machine` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Idempotency locking and immutable transaction ledger** | Expose composable and Vue 3 component for `idempotency locking and immutable transaction ledger` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Tokenized payment method vault and mandate directory** | Expose composable and Vue 3 component for `tokenized payment method vault and mandate directory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Verified webhook inbox and out-of-order reconciliation** | Expose composable and Vue 3 component for `verified webhook inbox and out-of-order reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Dispute management and settlement batch reconciliation** | Expose composable and Vue 3 component for `dispute management and settlement batch reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payment-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
