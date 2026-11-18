# Boilerplate: Affiliates and Partner Programs React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-affiliates-react-inertia`
**Matching domain module:** `affiliates`
**Matching core package:** [`module-affiliates`](../core/affiliates.md) (`liberusoftware/affiliate-core`)
**Application:** Boilerplate
**Source feature:** [Affiliates and Partner Programs](../features/affiliates.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/affiliates.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **Affiliate program and commission tier rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Partner applications, KYC/tax readiness, and approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tracking links, campaign parameters, and promo codes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Authoritative conversion ingestion and hold ledger:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Automated refund, cancellation, and dispute clawbacks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Self-referral, velocity, and fraud screening:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payout approval batches and settlement handoff:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-affiliates-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `affiliate-program-and-commission-tier-rules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `partner-applications-kyc-tax-readiness-and-approval`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tracking-links-campaign-parameters-and-promo-codes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `authoritative-conversion-ingestion-and-hold-ledger`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `automated-refund-cancellation-and-dispute-clawbacks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `self-referral-velocity-and-fraud-screening`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `payout-approval-batches-and-settlement-handoff`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
| Capability React Inertia module skeleton | `module-boilerplate-affiliates-react-inertia` | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/affiliates.md) · [Core plan](../core/affiliates.md) · [API plan](../api/affiliates.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Render `affiliate program and commission tier rules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Partner applications, KYC/tax readiness, and approval** | Render `partner applications, kyc/tax readiness, and approval` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tracking links, campaign parameters, and promo codes** | Render `tracking links, campaign parameters, and promo codes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Authoritative conversion ingestion and hold ledger** | Render `authoritative conversion ingestion and hold ledger` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Automated refund, cancellation, and dispute clawbacks** | Render `automated refund, cancellation, and dispute clawbacks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Self-referral, velocity, and fraud screening** | Render `self-referral, velocity, and fraud screening` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Payout approval batches and settlement handoff** | Render `payout approval batches and settlement handoff` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
