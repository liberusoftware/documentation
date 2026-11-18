# Liberu Music: MIDI and Expressive Editing — Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#midi-sequencing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-midi-sequencing-nuxt`. Uses [core](../core/midi-sequencing.md) and, for remote access, [API](../api/midi-sequencing.md).

## Surface workflow

Present: record a MIDI phrase, quantize selected notes and edit per-note expression. Domain scope: piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.

Use API-backed composables with workspace-scoped cache keys. Initialize AudioWorklet/device access only on the client after a user gesture; clear private cached data at logout.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: notes and expression retain stable identifiers and explicit time units.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-music-daw-nuxt-vue`](https://github.com/liberusoftware/project-music-daw-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/midi-sequencing.md)) |
| Capability Nuxt module skeleton | [`module-music-midi-sequencing-nuxt`](https://github.com/liberusoftware/module-music-midi-sequencing-nuxt) (`@liberusoftware/module-music-midi-sequencing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Piano roll** | Expose composable and Vue 3 component for `piano roll` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Drum editor** | Expose composable and Vue 3 component for `drum editor` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Step entry** | Expose composable and Vue 3 component for `step entry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Controller lanes** | Expose composable and Vue 3 component for `controller lanes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **Note expression** | Expose composable and Vue 3 component for `note expression` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **MPE** | Expose composable and Vue 3 component for `mpe` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |
| **MIDI import/export** | Expose composable and Vue 3 component for `midi import/export` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/midi-sequencing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-music-daw-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
