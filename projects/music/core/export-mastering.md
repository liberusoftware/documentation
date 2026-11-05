# Liberu Music: Export, Mastering and Delivery — Core

**Status: proposed design.** These are requirements and design identifiers, not verified source packages, published artifacts or implemented features.

**Design identifier:** `module-music-export-mastering`. See [domain specification](../features/export-mastering.md).

## Public application boundary

Own offline bounce, stems, freeze/flatten, dithering, loudness/true-peak analysis and delivery manifests. Provide typed commands, immutable query DTOs, versioned serialized state and after-commit events for saved changes.

**Invariant:** A render records source revision, graph/plugin versions, format and processing settings.

**Dependencies:** audio-engine, mixer-routing, media-library. Resolve foundation services through their canonical contracts. Authorize actor, workspace and referenced assets for all server actions; local audio execution consumes an already validated snapshot.

## Persistence and runtime

Laravel persists metadata and coordinates jobs. Audio device, DSP and sample scheduling behavior belongs in the separately versioned native runtime described in [architecture](../ARCHITECTURE.md). Never run a PHP action in the audio callback. Record schema version, revision and asset references; support migration preview, backups and safe disablement without deleting recordings.

## Verification

Compare realtime/offline output within declared tolerances and test clipping, tails and cancellation. Verify policy, revision conflict, idempotent command replay and cross-module contract compatibility. See [core architecture](../../../architecture/MODULES.md).
