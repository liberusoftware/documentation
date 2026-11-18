# Liberu Music: Export, Mastering and Delivery — Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#export-mastering). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-export-mastering-nuxt`. Uses [core](../core/export-mastering.md) and, for remote access, [API](../api/export-mastering.md).

## Surface workflow

Present: export a mix and stems, inspect loudness and verify delivery checksums. Domain scope: offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: a render records source revision, graph/plugin versions, format and processing settings.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/export-mastering.md)) |
| Capability Nuxt module skeleton | [`module-music-export-mastering-nuxt`](https://github.com/liberusoftware/module-music-export-mastering-nuxt) (`@liberusoftware/module-music-export-mastering-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Offline bounce** | Expose composable and Vue 3 component for `offline bounce` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Stems** | Expose composable and Vue 3 component for `stems` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Freeze/flatten** | Expose composable and Vue 3 component for `freeze/flatten` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Dithering** | Expose composable and Vue 3 component for `dithering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Loudness/true-peak analysis** | Expose composable and Vue 3 component for `loudness/true-peak analysis` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Delivery manifests** | Expose composable and Vue 3 component for `delivery manifests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/export-mastering.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
