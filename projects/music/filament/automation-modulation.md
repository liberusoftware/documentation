# Liberu Music: Automation and Modulation — Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#automation-modulation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-automation-modulation-filament`. Uses [core](../core/automation-modulation.md) and, for remote access, [API](../api/automation-modulation.md).

## Surface workflow

Present: record a fader move, edit its curve and add a reversible modulator mapping. Domain scope: parameter automation lanes, read/write/touch/latch modes, envelopes, LFOs and modulation mappings.

Provide tenant-scoped resources, read-only revision/engine diagnostics and audited recovery actions. Limit destructive/bulk actions through core policies; do not expose a live DSP graph editor as ordinary CRUD.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify sample scheduling, seek/chase state and smoothing under dense automation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: automation and modulation have declared precedence and bounded parameter ranges.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-music-automation-modulation-filament`](https://github.com/liberusoftware/module-music-automation-modulation-filament) (`liberusoftware/music-automation-modulation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/automation-modulation.md) · [API plan](../api/automation-modulation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Parameter automation lanes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parameter automation lanes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Read/write/touch/latch modes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `read/write/touch/latch modes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Envelopes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `envelopes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **LFOs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lfos`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Modulation mappings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `modulation mappings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
