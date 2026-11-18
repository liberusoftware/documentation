# Liberu Music: Mixer and Routing — Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mixer-routing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-mixer-routing-filament`. Uses [core](../core/mixer-routing.md) and, for remote access, [API](../api/mixer-routing.md).

## Surface workflow

Present: route tracks through a bus, add a sidechain and save a mix snapshot. Domain scope: channels, buses, sends, sidechains, pan, gain, groups, solo/mute and routing snapshots.

Provide tenant-scoped resources, read-only revision/engine diagnostics and audited recovery actions. Limit destructive/bulk actions through core policies; do not expose a live DSP graph editor as ordinary CRUD.

Apply the [surface support matrix](../PRESENTATION.md) before enabling editing, capture or DSP. For unsupported local capabilities, provide metadata/review and an explicit handoff to a capable host; never imply that a remote server is monitoring live audio.

Show loading, empty, denied, missing-device/plugin/media, pending-sync, conflict and failed-job states as applicable. Preserve drafts and expose retry/cancel with authoritative results. Use keyboard and screen-reader alternatives for visual controls, scalable text, reduced motion and labeled meters.

## Verification

Verify routing cycle detection, solo behavior, channel layouts and delay compensation. Verify the supported subset on the actual target runtime, navigation cleanup, permission denial and offline recovery. Mobile acceptance requires physical iOS/Android devices and release builds. Honor the invariant through the owning contract: routing cycles are rejected unless an explicitly supported delayed feedback node exists.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-music-daw-laravel-filament`](https://github.com/liberusoftware/project-music-daw-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-music-mixer-routing-filament`](https://github.com/liberusoftware/module-music-mixer-routing-filament) (`liberusoftware/music-mixer-routing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/mixer-routing.md) · [API plan](../api/mixer-routing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Channels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Buses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `buses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sends** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sends`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sidechains** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sidechains`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pan** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pan`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gain** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gain`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Groups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `groups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Solo/mute** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `solo/mute`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing snapshots** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing snapshots`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
