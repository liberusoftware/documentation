# Liberu Music: Export, Mastering and Delivery — Domain specifications

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

## Ownership and workflow

Offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests.

**Required journey:** Export a mix and stems, inspect loudness and verify delivery checksums.

**Invariant:** A render records source revision, graph/plugin versions, format and processing settings.

**Dependencies:** audio-engine, mixer-routing, media-library. Dependencies use public contracts rather than private tables or models.

## Acceptance

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Include denied access, missing dependencies and recovery after interruption. Store musical positions, sample positions and frame positions with explicit units wherever used.

See the [core plan](../core/export-mastering.md), [API plan](../api/export-mastering.md) and [surface support](../PRESENTATION.md).
