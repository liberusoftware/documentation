# Liberu Music: MIDI and Expressive Editing — Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#midi-sequencing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-midi-sequencing-filament`. Uses [core](../core/midi-sequencing.md) and, for remote access, [API](../api/midi-sequencing.md).

## Surface workflow

Present: record a MIDI phrase, quantize selected notes and edit per-note expression. Domain scope: piano roll, drum editor, step entry, controller lanes, note expression, MPE and MIDI import/export.

Provide tenant-scoped resources, read-only revision/engine diagnostics and audited recovery actions. Limit destructive/bulk actions through core policies; do not expose a live DSP graph editor as ordinary CRUD.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Round-trip supported MIDI events and test note-off cleanup after stop or device loss. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: notes and expression retain stable identifiers and explicit time units.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-music-midi-sequencing-filament`](https://github.com/liberusoftware/module-music-midi-sequencing-filament) (`liberusoftware/music-midi-sequencing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/midi-sequencing.md) · [API plan](../api/midi-sequencing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Piano roll** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `piano roll`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drum editor** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drum editor`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Step entry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `step entry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Controller lanes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `controller lanes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Note expression** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `note expression`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **MPE** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mpe`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **MIDI import/export** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `midi import/export`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
