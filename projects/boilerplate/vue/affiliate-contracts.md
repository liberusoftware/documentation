# Boilerplate: Affiliate Contracts Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliate-contracts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-affiliate-contracts-vue-inertia`
**Matching domain module:** `affiliate-contracts`
**Matching core package:** [`module-affiliate-contracts`](../core/affiliate-contracts.md) (`liberusoftware/affiliate-contracts`)
**Application:** Boilerplate
**Source feature:** [Affiliate Contracts](../features/affiliate-contracts.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)
**Architecture:** [VUE.md](../../../standards/VUE.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/affiliate-contracts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, composables, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

- **AffiliateProgramContract and attribution window DTOs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **ReferralAttributionContract and signed touch tokens:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **ConversionRecorderContract and idempotent clawbacks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **CommissionCalculatorContract and tiered rate rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **FraudAndSelfReferralPolicyContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PayoutSettlementContract and RewardFulfillmentContract:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-affiliate-contracts-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `affiliateprogramcontract-and-attribution-window-dtos`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `referralattributioncontract-and-signed-touch-tokens`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `conversionrecordercontract-and-idempotent-clawbacks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `commissioncalculatorcontract-and-tiered-rate-rules`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `fraudandselfreferralpolicycontract`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payoutsettlementcontract-and-rewardfulfillmentcontract`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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
| Capability Vue Inertia module skeleton | `module-boilerplate-affiliate-contracts-vue-inertia` | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/affiliate-contracts.md) · [Core plan](../core/affiliate-contracts.md) · [API plan](../api/affiliate-contracts.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **AffiliateProgramContract and attribution window DTOs** | Render `affiliateprogramcontract and attribution window dtos` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **ReferralAttributionContract and signed touch tokens** | Render `referralattributioncontract and signed touch tokens` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **ConversionRecorderContract and idempotent clawbacks** | Render `conversionrecordercontract and idempotent clawbacks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **CommissionCalculatorContract and tiered rate rules** | Render `commissioncalculatorcontract and tiered rate rules` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **FraudAndSelfReferralPolicyContract** | Render `fraudandselfreferralpolicycontract` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Render `payoutsettlementcontract and rewardfulfillmentcontract` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
