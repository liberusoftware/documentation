# Liberu Music: Mixer and Routing — Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mixer-routing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-mixer-routing-nuxt`. Uses [core](../core/mixer-routing.md) and, for remote access, [API](../api/mixer-routing.md).

## Surface workflow

Present: route tracks through a bus, add a sidechain and save a mix snapshot. Domain scope: channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: routing cycles are rejected unless an explicitly supported delayed feedback node exists.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mixer-routing.md)) |
| Capability Nuxt module skeleton | [`module-music-mixer-routing-nuxt`](https://github.com/liberusoftware/module-music-mixer-routing-nuxt) (`@liberusoftware/module-music-mixer-routing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Channels** | Expose composable and Vue 3 component for `channels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Buses** | Expose composable and Vue 3 component for `buses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Sends** | Expose composable and Vue 3 component for `sends` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Sidechains** | Expose composable and Vue 3 component for `sidechains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Pan** | Expose composable and Vue 3 component for `pan` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Gain** | Expose composable and Vue 3 component for `gain` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Groups** | Expose composable and Vue 3 component for `groups` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Solo/mute** | Expose composable and Vue 3 component for `solo/mute` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Routing snapshots** | Expose composable and Vue 3 component for `routing snapshots` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mixer-routing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
