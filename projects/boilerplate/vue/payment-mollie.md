# Boilerplate: Payment Mollie Adapter Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-mollie). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-payment-mollie-vue-inertia`
**Matching domain module:** `payment-mollie`
**Matching core package:** [`module-payment-mollie`](../core/payment-mollie.md) (`liberusoftware/payment-mollie`)
**Application:** Boilerplate
**Source feature:** [Payment Mollie Adapter](../features/payment-mollie.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [VUE.md](../../../standards/VUE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-mollie.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, composables, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **Mollie Payments API, Components, and APM redirects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mollie Customers and SEPA/card recurring Mandates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Authorized payment capture, release, and partial refunds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mollie webhook verification and authoritative state fetch:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Chargeback handling and Settlements API reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-payment-mollie-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `mollie-payments-api-components-and-apm-redirects`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mollie-customers-and-sepa-card-recurring-mandates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `authorized-payment-capture-release-and-partial-refunds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mollie-webhook-verification-and-authoritative-state-fetch`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `chargeback-handling-and-settlements-api-reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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
| Capability Vue Inertia module skeleton | `module-boilerplate-payment-mollie-vue-inertia` | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/payment-mollie.md) · [Core plan](../core/payment-mollie.md) · [API plan](../api/payment-mollie.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Mollie Payments API, Components, and APM redirects** | Render `mollie payments api, components, and apm redirects` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mollie Customers and SEPA/card recurring Mandates** | Render `mollie customers and sepa/card recurring mandates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Authorized payment capture, release, and partial refunds** | Render `authorized payment capture, release, and partial refunds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mollie webhook verification and authoritative state fetch** | Render `mollie webhook verification and authoritative state fetch` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Chargeback handling and Settlements API reconciliation** | Render `chargeback handling and settlements api reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
