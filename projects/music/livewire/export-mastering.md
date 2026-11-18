# Liberu Music: Export, Mastering and Delivery — Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#export-mastering). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-export-mastering-livewire`. Uses [core](../core/export-mastering.md) and, for remote access, [API](../api/export-mastering.md).

## Surface workflow

Present: export a mix and stems, inspect loudness and verify delivery checksums. Domain scope: offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests.

Use server-rendered forms for metadata and review. Keep frequent meter/waveform updates in a client component with explicit lifecycle cleanup; avoid server round trips for audio control loops.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: a render records source revision, graph/plugin versions, format and processing settings.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/export-mastering.md) · [API plan](../api/export-mastering.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Offline bounce** | Expose a focused Livewire 4 component and namespaced Blade default view for `offline bounce` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Stems** | Expose a focused Livewire 4 component and namespaced Blade default view for `stems` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Freeze/flatten** | Expose a focused Livewire 4 component and namespaced Blade default view for `freeze/flatten` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dithering** | Expose a focused Livewire 4 component and namespaced Blade default view for `dithering` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Loudness/true-peak analysis** | Expose a focused Livewire 4 component and namespaced Blade default view for `loudness/true-peak analysis` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery manifests** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery manifests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
