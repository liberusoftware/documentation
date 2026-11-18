# Liberu: Revenue and Care Orchestration Nuxt

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-nuxt`

Expose public website entry points and authenticated staff/customer views over the [API](../api/revenue-and-care-orchestration.md). Keep public SSR limited to approved, cacheable content; do not leak health, consent, invoice, or infrastructure data into SSR payloads. Use mobile-first responsive components, Core Web Vitals budgets, accessible chat/support handoff, typed composables, and explicit queued/error states.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-liberu-official-nuxt-vue`](https://github.com/liberusoftware/project-liberu-official-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revenue-and-care-orchestration.md)) |
| Capability Nuxt module skeleton | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customer health constellation** | Expose composable and Vue 3 component for `customer health constellation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |
| **Revenue-aware service recovery** | Expose composable and Vue 3 component for `revenue-aware service recovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |
| **Contact-protection ledger** | Expose composable and Vue 3 component for `contact-protection ledger` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |
| **Cross-brand consent and quiet-hour evaluation** | Expose composable and Vue 3 component for `cross-brand consent and quiet-hour evaluation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |
| **Approval-gated AI recommendations** | Expose composable and Vue 3 component for `approval-gated ai recommendations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |
| **Mobile-ready daily queues** | Expose composable and Vue 3 component for `mobile-ready daily queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-and-care-orchestration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-liberu-official-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
