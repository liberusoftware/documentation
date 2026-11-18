# Boilerplate: Payment PayPal Adapter React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-payment-paypal-react-inertia`
**Matching domain module:** `payment-paypal`
**Matching core package:** [`module-payment-paypal`](../core/payment-paypal.md) (`liberusoftware/payment-paypal`)
**Application:** Boilerplate
**Source feature:** [Payment PayPal Adapter](../features/payment-paypal.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-paypal.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **PayPal Orders v2 creation, approval, and authorization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PayPal Vault v3 setup tokens and recurring payment tokens:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Order capture, authorization reauthorization/void, and refunds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PayPal transmission-signature webhook verification:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PayPal Customer Disputes and chargeback lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PayPal transaction search and settlement reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-payment-paypal-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `paypal-orders-v2-creation-approval-and-authorization`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paypal-vault-v3-setup-tokens-and-recurring-payment-tokens`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `order-capture-authorization-reauthorization-void-and-refunds`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paypal-transmission-signature-webhook-verification`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paypal-customer-disputes-and-chargeback-lifecycle`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paypal-transaction-search-and-settlement-reconciliation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
| Product Inertia React host skeleton | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | `module-boilerplate-payment-paypal-react-inertia` | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/payment-paypal.md) · [Core plan](../core/payment-paypal.md) · [API plan](../api/payment-paypal.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **PayPal Orders v2 creation, approval, and authorization** | Render `paypal orders v2 creation, approval, and authorization` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PayPal Vault v3 setup tokens and recurring payment tokens** | Render `paypal vault v3 setup tokens and recurring payment tokens` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Order capture, authorization reauthorization/void, and refunds** | Render `order capture, authorization reauthorization/void, and refunds` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PayPal transmission-signature webhook verification** | Render `paypal transmission-signature webhook verification` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PayPal Customer Disputes and chargeback lifecycle** | Render `paypal customer disputes and chargeback lifecycle` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PayPal transaction search and settlement reconciliation** | Render `paypal transaction search and settlement reconciliation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
