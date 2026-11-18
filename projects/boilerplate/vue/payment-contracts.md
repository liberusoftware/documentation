# Boilerplate: Payment Contracts Vue + Inertia

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-payment-contracts-vue-inertia`
**Matching domain module:** `payment-contracts`
**Matching core package:** [`module-payment-contracts`](../core/payment-contracts.md) (`liberusoftware/payment-contracts`)
**Application:** Boilerplate
**Source feature:** [Payment Contracts](../features/payment-contracts.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [VUE.md](../../../standards/VUE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-contracts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract (`PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, composables, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **PaymentGatewayAdapterContract and capability descriptors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PaymentIntentServiceContract and 3DS/SCA client actions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PaymentCaptureAndRefundContract with idempotency:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SavedPaymentMethodVaultContract and mandates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **MerchantWebhookVerifierContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-payment-contracts-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `paymentgatewayadaptercontract-and-capability-descriptors`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `paymentintentservicecontract-and-3ds-sca-client-actions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `paymentcaptureandrefundcontract-with-idempotency`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `savedpaymentmethodvaultcontract-and-mandates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `merchantwebhookverifiercontract`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `disputeandchargebackhandlercontract-and-payoutandsettlementreconcilercontract`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | `module-boilerplate-payment-contracts-vue-inertia` | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/payment-contracts.md) · [Core plan](../core/payment-contracts.md) · [API plan](../api/payment-contracts.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **PaymentGatewayAdapterContract and capability descriptors** | Render `paymentgatewayadaptercontract and capability descriptors` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **PaymentIntentServiceContract and 3DS/SCA client actions** | Render `paymentintentservicecontract and 3ds/sca client actions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **PaymentCaptureAndRefundContract with idempotency** | Render `paymentcaptureandrefundcontract with idempotency` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **SavedPaymentMethodVaultContract and mandates** | Render `savedpaymentmethodvaultcontract and mandates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **MerchantWebhookVerifierContract** | Render `merchantwebhookverifiercontract` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract** | Render `disputeandchargebackhandlercontract and payoutandsettlementreconcilercontract` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
