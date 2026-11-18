# Music: design and source reconciliation

This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.

**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.

Liberu Music DAW defines 22 proposed domain, API, web, mobile and desktop capabilities with explicit native audio runtime boundaries. Use [MUSIC.md](MUSIC.md), [ARCHITECTURE.md](ARCHITECTURE.md), [PRESENTATION.md](PRESENTATION.md) and the [capability repository catalog](../../modules/skeletons/README.md).

## Read the mapping

Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.

Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.

| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |
| --- | --- | --- | --- | --- |
| <a id="arrangement"></a>[arrangement](features/arrangement.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="audio-devices"></a>[audio-devices](features/audio-devices.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="audio-engine"></a>[audio-engine](features/audio-engine.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="automation-modulation"></a>[automation-modulation](features/automation-modulation.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="clip-launcher"></a>[clip-launcher](features/clip-launcher.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="collaboration"></a>[collaboration](features/collaboration.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="composition-score"></a>[composition-score](features/composition-score.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="controllers"></a>[controllers](features/controllers.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="effects"></a>[effects](features/effects.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="export-mastering"></a>[export-mastering](features/export-mastering.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="instruments"></a>[instruments](features/instruments.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="live-performance"></a>[live-performance](features/live-performance.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="media-library"></a>[media-library](features/media-library.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="midi-sequencing"></a>[midi-sequencing](features/midi-sequencing.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="mixer-routing"></a>[mixer-routing](features/mixer-routing.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="plugin-hosting"></a>[plugin-hosting](features/plugin-hosting.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="presets"></a>[presets](features/presets.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="projects"></a>[projects](features/projects.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="recording"></a>[recording](features/recording.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="sync-offline"></a>[sync-offline](features/sync-offline.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="tempo-groove"></a>[tempo-groove](features/tempo-groove.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |
| <a id="video-timecode"></a>[video-timecode](features/video-timecode.md) | No dedicated name match | No dedicated name match | No dedicated name match | No dedicated name match |

## Observed packages without a design-name match

These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.

| Actual directory | Manifest identity and implementation reference |
| --- | --- |
| — | No unmatched dedicated package identities in this scan |

Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.
