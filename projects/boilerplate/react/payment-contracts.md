# Boilerplate: Payment Contracts React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-contracts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-payment-contracts-react-inertia`
**Matching domain module:** `payment-contracts`
**Matching core package:** [`module-payment-contracts`](../core/payment-contracts.md) (`liberusoftware/payment-contracts`)
**Application:** Boilerplate
**Source feature:** [Payment Contracts](../features/payment-contracts.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payment-contracts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract (`PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **PaymentGatewayAdapterContract and capability descriptors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PaymentIntentServiceContract and 3DS/SCA client actions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PaymentCaptureAndRefundContract with idempotency:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SavedPaymentMethodVaultContract and mandates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **MerchantWebhookVerifierContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-payment-contracts-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `paymentgatewayadaptercontract-and-capability-descriptors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paymentintentservicecontract-and-3ds-sca-client-actions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `paymentcaptureandrefundcontract-with-idempotency`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `savedpaymentmethodvaultcontract-and-mandates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `merchantwebhookverifiercontract`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `disputeandchargebackhandlercontract-and-payoutandsettlementreconcilercontract`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
| Capability React Inertia module skeleton | `module-boilerplate-payment-contracts-react-inertia` | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/payment-contracts.md) · [Core plan](../core/payment-contracts.md) · [API plan](../api/payment-contracts.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **PaymentGatewayAdapterContract and capability descriptors** | Render `paymentgatewayadaptercontract and capability descriptors` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PaymentIntentServiceContract and 3DS/SCA client actions** | Render `paymentintentservicecontract and 3ds/sca client actions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PaymentCaptureAndRefundContract with idempotency** | Render `paymentcaptureandrefundcontract with idempotency` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **SavedPaymentMethodVaultContract and mandates** | Render `savedpaymentmethodvaultcontract and mandates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **MerchantWebhookVerifierContract** | Render `merchantwebhookverifiercontract` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract** | Render `disputeandchargebackhandlercontract and payoutandsettlementreconcilercontract` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
